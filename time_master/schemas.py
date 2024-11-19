from typing import Optional

from pydantic import BaseModel


class TimeWarriorSummaryRecordSchema(BaseModel):
    """Time warrior summary record schema."""

    week: str
    date: str
    day: str
    tags: list[str]
    start: str
    end: Optional[str] = None
    duration: Optional[str] = None
    total: Optional[str] = None
