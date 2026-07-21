from pydantic import BaseModel, ConfigDict


class PromptEasyBaseModel(BaseModel):
    """
    Base model for every schema in PromptEasy.

    Provides common configuration for
    validation and serialization.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        frozen=False,
    )