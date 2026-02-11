import os
import sys
import zipfile
import logging
from datetime import datetime



def setup_logger():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")

    log_file = f"Logs/Exclude_{datetime.now().strftime('%d%m%Y_%H%M%S')}.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )
    return logging.getLogger()



def validate_source(path):
    return os.path.exists(path)



def is_excluded(filename, excluded_exts):
    _, ext = os.path.splitext(filename)
    return ext.lower() in excluded_exts



def create_backup(source, excluded_exts, logger):
    try:
        if not validate_source(source):
            logger.error("Invalid source folder")
            return

        zip_name = f"Backup_{datetime.now().strftime('%d%m%Y_%H%M%S')}.zip"
        files_added = 0
        files_ignored = 0

        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source):
                for file in files:
                    if is_excluded(file, excluded_exts):
                        files_ignored += 1
                        continue

                    full_path = os.path.join(root, file)
                    zipf.write(full_path)
                    files_added += 1

        logger.info(f"Excluded extensions : {excluded_exts}")
        logger.info(f"Files added : {files_added}")
        logger.info(f"Files ignored : {files_ignored}")
        logger.info(f"Zip file created : {zip_name}")

    except Exception as e:
        logger.error(f"Backup error : {str(e)}")



def main():
    logger = setup_logger()

    try:
        if len(sys.argv) < 2:
            logger.error("Invalid arguments")
            return

        source_folder = sys.argv[1]

        
        excluded_exts = {".tmp", ".log", ".exe"}

        if len(sys.argv) > 2:
            for ext in sys.argv[2:]:
                if not ext.startswith("."):
                    ext = "." + ext
                excluded_exts.add(ext.lower())

        create_backup(source_folder, excluded_exts, logger)

    except Exception as e:
        logger.error(f"Unhandled error : {str(e)}")

if __name__ == "__main__":
    main()
