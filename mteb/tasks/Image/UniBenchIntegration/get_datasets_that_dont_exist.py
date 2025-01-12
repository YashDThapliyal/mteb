def preprocess_and_compare(unibench_file, mteb_raw_file, output_unique_mteb, output_diff_file):
    with open(mteb_raw_file, "r") as file:
        mteb_lines = file.readlines()
    
    unique_mteb_datasets = sorted(set(line.strip() for line in mteb_lines if line.strip()))
    
    with open(output_unique_mteb, "w") as file:
        file.write("Unique Datasets in MTEB:\n")
        for dataset in unique_mteb_datasets:
            file.write(f"{dataset}\n")
    
    print(f"Unique MTEB datasets saved to {output_unique_mteb}")
    
    with open(unibench_file, "r") as file:
        unibench_datasets = set(line.strip().lower() for line in file if line.strip())
    
    unique_to_unibench = sorted(unibench_datasets - set(dataset.lower() for dataset in unique_mteb_datasets))
    
    with open(output_diff_file, "w") as file:
        file.write("Datasets in UniBench but not in MTEB:\n")
        for dataset in unique_to_unibench:
            file.write(f"{dataset}\n")
    
    print(f"Comparison result saved to {output_diff_file}")

path = "/Users/yash/Documents/Stanford/mteb/mteb/tasks/Image/UniBenchIntegration/"
unibench_file = path + "UniBenchDatasets.txt"
mteb_raw_file = path + "MTEB_all_datasets.txt" # Raw copy-pasted MTEB dataset names
output_unique_mteb =path+ "MTEB_unique_datasets.txt"
output_diff_file = path + "UniBench_not_in_MTEB.txt"

preprocess_and_compare(unibench_file, mteb_raw_file, output_unique_mteb, output_diff_file)
