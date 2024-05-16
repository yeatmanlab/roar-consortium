import json
import sys

REQUIRED_KEYS = {"name", "affiliation", "email", "orcid", "github", "role"}


def validate_authors(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        authors = json.load(file)

    for author in authors:
        missing_keys = REQUIRED_KEYS - author.keys()
        if missing_keys:
            print(
                f"Error: Author '{author.get('name', 'Unknown')}' is missing keys: {', '.join(missing_keys)}"
            )
            return False

    return True


if __name__ == "__main__":
    if not validate_authors("authors.json"):
        sys.exit(1)
    print("All authors are valid.")
