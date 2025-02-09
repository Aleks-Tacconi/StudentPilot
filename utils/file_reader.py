def read_file(file: str) -> str:
    string_builder = ""

    with open(file, mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            string_builder += line.strip() + "\n"

    return string_builder
