from beanie import Document
from pydantic import EmailStr, HttpUrl, Field
from typing import Optional
from datetime import datetime

class SellsCollection(Document):
    account_id: str = Field(alias="Account Id")
    lead_owner: str = Field(alias="Lead Owner")
    first_name: str = Field(alias="First Name")
    last_name: str = Field(alias="Last Name")
    company: str = Field(alias="Company")
    phone_1: str = Field(alias="Phone 1")
    phone_2: Optional[str] = Field(alias="Phone 2")
    email_1: EmailStr = Field(alias="Email 1")
    email_2: Optional[EmailStr] = Field(alias="Email 2")
    website: Optional[HttpUrl] = Field(alias="Website")
    source: str = Field(alias="Source")
    deal_stage: str = Field(alias="Deal Stage")
    notes: Optional[str] = Field(alias="Notes")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "sells_data"  # Name of the MongoDB collection
        indexes = [
            "account_id",  # Index on the account_id field
            "lead_owner",  # Index on the lead_owner field
        ]
