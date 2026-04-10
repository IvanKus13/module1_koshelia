import sys
import os
import pytest
from src.filter import filter_lines
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("hello\nworld\nhello python\n")
    return file


@pytest.mark.parametrize("keyword, expected", [
    ("hello", ["hello\n", "hello python\n"]),
    ("world", ["world\n"]),
    ("python", ["hello python\n"]),
])
def test_filter_lines(sample_file, keyword, expected, tmp_path):
    output = tmp_path / "out.txt"

    result = filter_lines(str(sample_file), keyword, str(output))

    assert result == expected
    assert output.read_text().splitlines(keepends=True) == expected
