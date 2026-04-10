def filter_lines(input_file: str, keyword: str, output_file: str = "filtered.txt"):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    filtered = [line for line in lines if keyword in line]

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(filtered)

    return filtered