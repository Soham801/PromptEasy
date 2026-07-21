from pydantic import Field

from app.schemas.base import PromptEasyBaseModel
from app.prompt_engine.shared.enums import (
    PromptCategory,
    PromptIntent,
    PromptComplexity,
)


class PromptAnalysis(PromptEasyBaseModel):

    category: PromptCategory

    intent: PromptIntent

    complexity: PromptComplexity

    confidence: float = Field(
        ge=0,
        le=1,
    )

    missing_information: list[str] = Field(
        default_factory=list,
    )

    extracted_entities: list[str] = Field(
        default_factory=list,
    )