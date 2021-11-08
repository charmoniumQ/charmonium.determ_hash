from __future__ import annotations

from typing import Generic, TypeVar, Union, cast

_T = TypeVar("_T")

class GetAttr(Generic[_T]):
    """When you want to getattr or use a default, with static types.

    Example: ``obj_hash = GetAttr[Callable[[], int]]()(obj, "__hash__", lambda: hash(obj))()``

    """

    error = object()

    def __init__(self) -> None:
        ...

    def __call__(
        self,
        obj: object,
        attr_name: str,
        default: Union[_T, object] = error,
        check_callable: bool = False,
    ) -> _T:
        if hasattr(obj, attr_name):
            attr_val = getattr(obj, attr_name)
            if check_callable and not hasattr(attr_val, "__call__"):
                raise TypeError(
                    f"GetAttr expected ({obj!r}).{attr_name} to be callable, but it is {type(attr_val)}."
                )
            else:
                return cast(_T, attr_val)
        elif default is not GetAttr.error:
            return cast(_T, default)
        else:
            raise AttributeError(
                f"{obj!r}.{attr_name} does not exist, and no default was provided"
            )
