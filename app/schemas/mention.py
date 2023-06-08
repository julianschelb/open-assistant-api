# ---------------------------------------------------------------------------
#                            Entity Mention
# ---------------------------------------------------------------------------

from pydantic import BaseModel, Field
from typing import Dict, Optional, List
from enum import Enum

# --------------------------------- Context --------------------------------


class EntityMention(BaseModel):
    context: List = Field(
        default=[],
        title="Context",
        description="Context with marked Entity Mention",
    )

    class Config:
        schema_extra = {
            "example": {
                "context": [
                    "[START_ENT]",
                    "Einstein",
                    "[END_ENT]",
                    "was",
                    "a",
                    "German",
                    "physicist.",
                ]
            }
        }


# --------------------------------- Disambiguated Entity --------------------------------


class EntityDisambiguated(BaseModel):
    candidates: List = Field(
        default=[],
        title="Candidates",
        description="Candidates",
    )

    class Config:
        schema_extra = {
            "example": {
                "candidates": [
                    "Albert Einstein",
                    "Albert Einstein (disambiguation)",
                    "Albert Einstein (physicist)",
                    "Albert Einstein (physicist, born 1918)",
                    "Albert Einstein (physicist, born 1948)",
                ]
            }
        }
