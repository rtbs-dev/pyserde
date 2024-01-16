from dataclasses import InitVar, dataclass
from typing import Optional

from serde import serde, field
from serde.json import from_json, to_json


@serde
@dataclass
class Foo:
    a: int
    b: Optional[int] = field(default=None, init=False)
    c: InitVar[Optional[int]] = 1000

    def __post_init__(self, c: Optional[int]) -> None:  # type: ignore
        self.b = self.a * 10


def main() -> None:
    f = Foo(10)
    print(f"Into Json: {to_json(f)}")

    s = '{"a": 10}'
    print(f"From Json: {from_json(Foo, s)}")


if __name__ == "__main__":
    main()
