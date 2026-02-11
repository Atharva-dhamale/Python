import os
import sys
import zipfile
import logging
from datetime import datetime


def setup_logger():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")

    log_file = f"Logs/Restore_{datetime.now().strftime('%d%m%Y_%H%M%S')}.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )
    return logging.getLogger()


def restore_backup(zip_file, destination, logger):
    try:
        if not os.path.exists(zip_file):
            logger.error("Zip file does not exist")
            return

        if not os.path.exists(destination):
            os.makedirs(destination)
            logger.info("Destination directory created")

        with zipfile.ZipFile(zip_file, 'r') as zipf:
            zipf.extractall(destination)

        logger.info(f"Backup restored successfully to {destination}")

    except zipfile.BadZipFile:
        logger.error("Invalid zip file")
    except Exception as e:
        logger.error(f"Restore error : {str(e)}")



def main():
    logger = setup_logger()

    if len(sys.argv) != 4 or sys.argv[1] != "--restore":
        logger.error("Invalid command usage")
        return

    zip_file = sys.argv[2]
    destination = sys.argv[3]

    restore_backup(zip_file, destination, logger)

if __name__ == "__main__":
    main()
