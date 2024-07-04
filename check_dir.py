import os
import pandas as pd

def get_subdirectories(directory_path, csv_file_path):
    # Get the list of all entries in the directory
    entries = os.listdir(directory_path)
    subdirectories = [entry for entry in entries if os.path.isdir(os.path.join(directory_path, entry))]
    
    # Read the CSV file and extract the values from the "Patient ID (UHID)" column
    df = pd.read_csv(csv_file_path)
    patient_uhids = df['Patient ID (UHID)'].tolist()
    patient_uhids = [uhid for uhid in patient_uhids if isinstance(uhid, str) and uhid.strip() != '']
    patient_uhids = set(patient_uhids)
    
    # Find common and uncommon UHIDs
    subdirectories_set = set(subdirectories)
    common_uhids = patient_uhids.intersection(subdirectories_set)
    uncommon_uhids = patient_uhids.difference(subdirectories_set)
    
    # Save results to CSV files
    save_to_master_csv(patient_uhids, common_uhids, uncommon_uhids, csv_file_path)
    
    return common_uhids, uncommon_uhids

def save_to_master_csv(all_uhids, common_uhids, uncommon_uhids, csv_file_path):
    directory_path=""
    # Read original CSV file
    df = pd.read_csv(csv_file_path)
    
    # Add "Common in Directory" column to original DataFrame
    df['Common in Directory'] = df['Patient ID (UHID)'].apply(lambda x: 'yes' if x in common_uhids else 'no')
    
    # Save modified DataFrame to Master.csv
    master_csv_path = os.path.join(directory_path, 'Master.csv')
    df.to_csv(master_csv_path, index=False)
    
    # Save common and uncommon UHIDs to separate CSV files
    common_csv_path = os.path.join(directory_path, 'common.csv')
    uncommon_csv_path = os.path.join(directory_path, 'uncommon.csv')
    
    pd.DataFrame({'Patient ID (UHID)': list(common_uhids)}).to_csv(common_csv_path, index=False)
    pd.DataFrame({'Patient ID (UHID)': list(uncommon_uhids)}).to_csv(uncommon_csv_path, index=False)

# Example usage
if __name__ == "__main__":
    directory_path = 'C:/Users/EIOT/Desktop/Unziped_dir'  # Replace with your directory path
    csv_file_path = 'C:/Users/EIOT/Desktop/Final.csv'  # Replace with your CSV file path

    common_uhids, uncommon_uhids = get_subdirectories(directory_path, csv_file_path)

    print("Common UHIDs:", common_uhids)
