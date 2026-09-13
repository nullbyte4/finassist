"""Database entities for FinAssist.

Defines the SQLModel table models used to persist categories, income
entries, and expense entries in the SQLite database.
"""

from datetime import date

from sqlmodel import Field, Relationship, SQLModel


class Category(SQLModel, table=True):
    """A label used to group expenses (e.g. 'Food', 'Rent')."""

    id: int | None = Field(default=None, primary_key=True)
    name: str

    expenses: list["Expense"] = Relationship(back_populates="category")


class Income(SQLModel, table=True):
    """A single income entry (e.g. salary, freelance payment)."""

    id: int | None = Field(default=None, primary_key=True)
    amount: float
    description: str
    date: date


class Expense(SQLModel, table=True):
    """A single expense entry linked to a category."""

    id: int | None = Field(default=None, primary_key=True)
    amount: float
    description: str
    date: date
    category_id: int = Field(foreign_key="category.id")

    category: Category = Relationship(back_populates="expenses")