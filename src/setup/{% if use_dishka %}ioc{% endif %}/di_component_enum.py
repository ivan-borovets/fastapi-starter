from enum import StrEnum


class ComponentEnum(StrEnum):
    DEFAULT = ""
    ...

    def __repr__(self):
        return self.value
