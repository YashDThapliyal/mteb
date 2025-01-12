import re

def extract_datasets(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    
    dataset_urls = re.findall(r'dataset_url="([^"]+)"', content)
    
    # Remove '/wds_' prefix and get unique dataset names
    unique_datasets = sorted(set(url.split("/")[-1].replace("wds_", "") for url in dataset_urls))
    
    return unique_datasets

def save_to_file(datasets, output_file):
    with open(output_file, "w") as file:
        for dataset in datasets:
            file.write(f"{dataset}\n")

file_path = "/Users/yash/Documents/Stanford/mteb/mteb/tasks/Image/UniBenchIntegration/UniBench-Benchmarks.py"
output_file = "/Users/yash/Documents/Stanford/mteb/mteb/tasks/Image/UniBenchIntegration/UniBenchDatasets.txt"

datasets = extract_datasets(file_path)
save_to_file(datasets, output_file)

print(f"Extracted datasets have been saved to {output_file}")
