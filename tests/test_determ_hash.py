from __future__ import annotations

import json
import logging
import subprocess
import sys
from typing import Any, Hashable, List

import pytest

from charmonium.determ_hash import determ_hash

values: List[Hashable] = [
    None,
    b"",
    b"abc",
    "abc",
    12,
    12.0,
    12 + 0j,
    (1, 2, 3),
    ((1, 2, 3)),
    ((1, 2), 3),
    (1, (2, 3)),
    frozenset({1, 2, 3}),
    frozenset({3, 2, 1}),
    ...,
]

value_hashes = {str(value): determ_hash(value) for value in values}


def test_uniqueness() -> None:
    for this_value, this_hash in value_hashes.items():
        matches = [
            other_value
            for other_value, other_hash in value_hashes.items()
            if this_hash == other_hash and this_value != other_value
        ]
        assert not matches


def test_persistence() -> None:
    code = fr"""
import json
from charmonium.determ_hash import determ_hash
print(json.dumps({{
    str(value): determ_hash(value)
    for value in {values!r}
}}))
"""
    proc = subprocess.run(
        [sys.executable, "-c", code],
        check=False,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr)
        raise RuntimeError("proc returned non-zero")
    their_value_hashes = json.loads(proc.stdout)
    assert value_hashes == their_value_hashes


unhashable_values: List[Any] = [
    [1, 2, 3],
    {"a": 1, "b": 2},
    object(),
]


def test_raises() -> None:
    for value in unhashable_values:
        with pytest.raises(TypeError):
            determ_hash(value)


def test_logs(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO, logger="charmonium.cache.determ_hash"):
        determ_hash(frozenset({(1, "hello")}))
    assert not caplog.text
    with caplog.at_level(logging.DEBUG, logger="charmonium.cache.determ_hash"):
        determ_hash(frozenset({(1, "hello")}))
    assert caplog.text
