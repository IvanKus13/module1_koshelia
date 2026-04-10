import pytest

from src.filter import filter_lines, write_lines


@pytest.fixture
def sample_file(tmp_path):
    """Create a temporary input file."""
    file = tmp_path / "input.txt"
    file.write_text(
        "hello\n"
        "test line\n"
        "another test\n"
        "nothing\n"
    )
    return file


@pytest.mark.parametrize(
    "keyword, expected_count",
    [
        ("test", 2),
        ("hello", 1),
        ("none", 0),
    ]
)
def test_filter_lines(sample_file, keyword, expected_count):
    result = filter_lines(sample_file, keyword)
    assert len(result) == expected_count


def test_write_lines(tmp_path):
    output_file = tmp_path / "output.txt"
    lines = ["one\n", "two\n"]

    write_lines(output_file, lines)

    content = output_file.read_text()
    assert content == "one\ntwo\n"