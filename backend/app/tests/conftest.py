from app.db.session import SessionLocal

import pytest


@pytest.fixture(scope="session")
def db() -> None:
    yield SessionLocal
