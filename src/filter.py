def filter_lines(input_file: str, keyword: str) -> list:
    """Read file and return lines containing keyword."""
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    filtered = [
        line for line in lines
        if keyword in line
    ]
    return filtered


def write_lines(output_file: str, lines: list) -> None:
    """Write lines to file."""
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(lines)
