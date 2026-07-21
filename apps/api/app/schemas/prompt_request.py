from pydantic import Field

from app.schemas.base import PromptEasyBaseModel


class PromptRequest(PromptEasyBaseModel):
    """
    Raw prompt submitted by the user.
    """

    prompt: str = Field(
        ...,
        min_length=3,
        max_length=15000,
    )

    target_model: str | None = None

    language: str = "en"

    project_id: str | None = None