from enum import Enum


class PromptCategory(str, Enum):
    CODING = "coding"
    WRITING = "writing"
    IMAGE = "image"
    VIDEO = "video"
    BUSINESS = "business"
    MARKETING = "marketing"
    RESEARCH = "research"
    EDUCATION = "education"
    PRODUCTIVITY = "productivity"
    UNKNOWN = "unknown"