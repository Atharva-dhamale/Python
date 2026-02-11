import os
import sys
import zipfile
import logging
from datetime import datetime


def create_logs_folder():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")

def setup_logger():
    create_logs_folder()
    log_file = f"Logs/Marvellous_{datetime.now().strftime('%d%m%Y_%H%M%S')}.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )
    return logging.getLogger()


def validate_source(path):
    return os.path.exists(path)


def create_backup(source, logger):
    try:
        if not validate_source(source):
            logger.error("Invalid source folder path")
            return

        start_time = datetime.now()
        logger.info(f"Backup start time : {start_time}")

        zip_name = f"Backup_{start_time.strftime('%d%m%Y_%H%M%S')}.zip"
        files_copied = 0

        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source):
                for file in files:
                    full_path = os.path.join(root, file)
                    zipf.write(full_path)
                    files_copied += 1

        logger.info(f"Files copied : {files_copied}")
        logger.info(f"Zip file name : {zip_name}")

    except Exception as e:
        logger.error(f"Error occurred : {str(e)}")


def main():
    logger = setup_logger()

    try:
        if len(sys.argv) != 2:
            logger.error("Invalid number of arguments")
            return

        source_folder = sys.argv[1]
        create_backup(source_folder, logger)

    except Exception as e:
        logger.error(f"Unhandled exception : {str(e)}")

if __name__ == "__main__":
    main()
