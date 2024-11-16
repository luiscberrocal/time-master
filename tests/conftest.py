from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def output_folder() -> Path:
    """Return the output folder for the tests."""
    return Path(__file__).parent.parent / "output"


@pytest.fixture(scope="session")
def fixtures_folder() -> Path:
    """Return the fixtures folder for the tests."""
    return Path(__file__).parent / "fixtures"
