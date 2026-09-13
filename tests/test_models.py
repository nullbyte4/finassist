"""Tests for FinAssist SQLModel entities and basic CRUD behavior.

Each test uses a fresh in-memory SQLite database so tests never touch
the real `finassist.db` file and stay isolated from one another.
"""

from datetime import date

import pytest
from sqlmodel import Session, SQLModel, create_engine

from app.models import Category, Expense, Income


@pytest.fixture(name="session")
def session_fixture():
    """Provide a Session backed by a fresh in-memory SQLite database."""
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_category(session: Session):
    """A Category can be created and receives an auto-generated id."""
    category = Category(name="Food")
    session.add(category)
    session.commit()
    session.refresh(category)

    assert category.id is not None
    assert category.name == "Food"


def test_create_income(session: Session):
    """An Income entry can be created with its own fields."""
    income = Income(amount=1500.0, description="Salary", date=date(2026, 9, 1))
    session.add(income)
    session.commit()
    session.refresh(income)

    assert income.id is not None
    assert income.amount == 1500.0


def test_create_expense_linked_to_category(session: Session):
    """An Expense can be created and linked to an existing Category."""
    category = Category(name="Groceries")
    session.add(category)
    session.commit()
    session.refresh(category)

    expense = Expense(
        amount=45.50,
        description="Weekly groceries",
        date=date(2026, 9, 5),
        category_id=category.id,
    )
    session.add(expense)
    session.commit()
    session.refresh(expense)

    assert expense.id is not None
    assert expense.category_id == category.id
    assert expense.category.name == "Groceries"


def test_update_expense_amount(session: Session):
    """An existing Expense's amount can be updated and persisted."""
    category = Category(name="Transport")
    session.add(category)
    session.commit()
    session.refresh(category)

    expense = Expense(
        amount=20.0,
        description="Bus fare",
        date=date(2026, 9, 6),
        category_id=category.id,
    )
    session.add(expense)
    session.commit()
    session.refresh(expense)

    expense.amount = 25.0
    session.add(expense)
    session.commit()
    session.refresh(expense)

    assert expense.amount == 25.0


def test_delete_category(session: Session):
    """A Category can be deleted from the database."""
    category = Category(name="Temporary")
    session.add(category)
    session.commit()
    session.refresh(category)
    category_id = category.id

    session.delete(category)
    session.commit()

    deleted = session.get(Category, category_id)
    assert deleted is None
