def find_difference_and_save(unibench_file, mteb_file, output_diff_file):
    with open(mteb_file, "r") as file:
        mteb_datasets = set(line.strip().lower() for line in file if line.strip())
    

    with open(unibench_file, "r") as file:
        unibench_datasets = set(line.strip().lower() for line in file if line.strip())
    
    # Find datasets in UniBench but not in MTEB
    unique_to_unibench = sorted(unibench_datasets - mteb_datasets)
    
    with open(output_diff_file, "w") as file:
        file.write("Datasets in UniBench but not in MTEB:\n")
        for dataset in unique_to_unibench:
            file.write(f"{dataset}\n")
    
    print(f"Differences saved to {output_diff_file}")

# File paths
path = "/Users/yash/Documents/Stanford/mteb/mteb/tasks/Image/UniBenchIntegration/"
unibench_file = path + "UniBenchDatasets.txt"
mteb_file = "/Users/yash/Documents/Stanford/mteb/mteb/tasks/Image/parsed_datasets_of_MIEB.txt"
output_diff_file = path + "UniBench_not_in_MTEB.txt"


find_difference_and_save(unibench_file, mteb_file, output_diff_file)
