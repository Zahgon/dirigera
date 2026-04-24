from pydantic import BaseModel


def to_camel(string: str) -> str:
    pass


class BaseIkeaModel(BaseModel, arbitrary_types_allowed=True, alias_generator=to_camel):
    pass
