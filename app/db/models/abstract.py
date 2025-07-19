from datetime import datetime, timezone
from beanie import Document
from pydantic import Field
from beanie import before_event, Replace, Update

class BaseDocument(Document):
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    @before_event(Replace)
    @before_event(Update)
    def update_timestamp(self):
        self.updated_at = lambda: datetime.now(timezone.utc)

    class Settings:
        use_state_management = True