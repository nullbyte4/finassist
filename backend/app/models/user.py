# SQLModel lets a single class act as both a database table and a Pydantic validation schema
from sqlmodel import SQLModel, Field

# Optional is a Python typing tool — it means a value can be its declared type OR None
from typing import Optional

# table=True tells SQLModel to create a real table in PostgreSQL for this class
# Without table=True it would only be a validation schema, not a DB table
class User(SQLModel, table=True):
    # Optional[int] because the id doesn't exist yet when a new user is created
    # PostgreSQL assigns it automatically after the row is inserted
    # Field(primary_key=True) marks this as the unique identifier for each row
    id: Optional[int] = Field(default=None, primary_key=True)

    # Plain str columns — PostgreSQL stores these as TEXT
    email: str
    hashed_password: str  # Never store plain passwords — only the hashed version

    # Default value of True so new users are active unless explicitly deactivated
    # Allows soft-deleting users without removing their data from the DB
    is_active: bool = True
