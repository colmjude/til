from typing import List, Optional
from pydantic import BaseModel, Field


class Note(BaseModel):
    title: str
    content: str
    author: str
    section: str = "notes"
    draft: bool = False
    tags: List[str] = Field(default_factory=list)
    created: Optional[str] = None
    updated: Optional[str] = None
    source: str = None
    slug: str = None
