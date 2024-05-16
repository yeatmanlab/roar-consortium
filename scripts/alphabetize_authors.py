import json


def alphabetize_authors(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        authors = json.load(file)

    sorted_authors = sorted(authors, key=lambda x: x["name"])

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(sorted_authors, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    alphabetize_authors("authors.json")
