import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5
