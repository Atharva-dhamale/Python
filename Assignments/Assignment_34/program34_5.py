import os
import zipfile
import argparse
import csv
from datetime import datetime


HISTORY_FILE = "backup_history.csv"
BACKUP_DIR = "backups"  

def log_backup(file_count, zip_size_bytes):
    """Appends backup metadata to the CSV history file."""
    size_mb = round(zip_size_bytes / (1024 * 1024), 2)
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    file_exists = os.path.isfile(HISTORY_FILE)
    
    with open(HISTORY_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Files", "Size"])
        writer.writerow([date_str, file_count, f"{size_mb} MB"])

def show_history():
    """Reads and prints the backup history in a formatted table."""
    if not os.path.exists(HISTORY_FILE):
        print("\n[!] No backup history found.")
        return

    print(f"\n{'Date':<20} | {'Files':<10} | {'Size'}")
    print("-" * 45)
    
    with open(HISTORY_FILE, mode='r') as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            print(f"{row[0]:<20} | {row[1]:<10} | {row[2]}")
    print("")

def perform_backup(source_folder):
    """Zips the contents of a folder and triggers the logger."""
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = os.path.join(BACKUP_DIR, f"backup_{timestamp}.zip")
    
    file_count = 0
    
    print(f"Creating backup: {zip_name}...")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_folder))
                file_count += 1
    
    zip_size = os.path.getsize(zip_name)
    log_backup(file_count, zip_size)
    print(f"Done! Backed up {file_count} files ({round(zip_size/1024, 2)} KB).")

def main():
    parser = argparse.ArgumentParser(description="Simple Backup System with History Tracking")
    parser.add_argument("--history", action="store_true", help="Display the backup history log")
    parser.add_argument("--source", type=str, help="The folder you want to back up")
    
    args = parser.parse_args()

    if args.history:
        show_history()
    elif args.source:
        perform_backup(args.source)
    else:
        print("Usage:")
        print("  To backup:  python Script.py --source ./my_folder")
        print("  To history: python Script.py --history")

if __name__ == "__main__":
    main()