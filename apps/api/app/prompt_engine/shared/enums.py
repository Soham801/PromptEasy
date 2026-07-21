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

class PromptIntent(str, Enum):
    CREATE = "create"
    IMPROVE = "improve"
    ANALYZE = "analyze"
    SUMMARIZE = "summarize"
    DESIGN = "design"
    DEBUG = "debug"
    UNKNOWN = "unknown"

class PromptComplexity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"