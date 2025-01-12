import os
import re

def find_imports_in_init_files(root_path):
    """Find and return all import statements from __init__.py files in the given directory."""
    import_statements = set()
    for dirpath, _, filenames in os.walk(root_path):
        if "__init__.py" in filenames:
            init_file = os.path.join(dirpath, "__init__.py")
            with open(init_file, "r", encoding="utf-8") as f:
                content = f.read()
                matches = re.findall(r'^\s*(from\s+\S+\s+import\s+\S+|import\s+\S+)', content, re.MULTILINE)
                import_statements.update(matches)
    return import_statements

def extract_dataset_names(import_statements):
    """Extract dataset names from the import statements."""
    dataset_names = set()
    for statement in import_statements:
        # Extract the word after the last dot (.) and before 'import' or '*'
        match = re.search(r'\.\s*([\w\d]+)\s*(import|\*)', statement)
        if match:
            dataset_names.add(match.group(1))
    return sorted(dataset_names)

def save_to_file(data, file_path):
    """Save the provided data to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        for item in data:
            file.write(item + "\n")
    print(f"Data has been saved to {file_path}")

def main():
    import_statements = find_imports_in_init_files(".")
    dataset_names = extract_dataset_names(import_statements)
    #save_to_file(sorted(import_statements), "alldatasetnames.txt") <-- for debug purposes
    save_to_file(dataset_names, "parsed_datasets.txt")

if __name__ == "__main__":
    main()
