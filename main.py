from src.filter import filter_lines


def main():
    input_file = "input.txt"
    keyword = input("Input word: ")

    result = filter_lines(input_file, keyword)

    print(f"Found lens: {len(result)}")
    print("Result saved in filtered.txt")


if __name__ == "__main__":
    main()
