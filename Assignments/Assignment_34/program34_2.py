import os
import sys
import zipfile
import logging
import smtplib
from datetime import datetime
from email.message import EmailMessage

SENDER_EMAIL = "atharvaserverpython@gmail.com"
APP_PASSWORD = "abcd efgh ijkl mnop"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587



def setup_logger():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")

    log_file = f"Logs/Marvellous_{datetime.now().strftime('%d%m%Y_%H%M%S')}.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )
    return logging.getLogger(), log_file



def validate_path(path):
    return os.path.exists(path)



def create_backup(source, logger):
    try:
        if not validate_path(source):
            logger.error("Invalid source folder")
            return None

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

        return zip_name

    except Exception as e:
        logger.error(f"Backup Error : {str(e)}")
        return None



def send_email(receiver, zip_file, log_file, logger):
    try:
        msg = EmailMessage()
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver
        msg['Subject'] = "Marvellous Data Shield : Backup Completed"

        msg.set_content("Backup completed successfully.\nPlease find attached log and backup zip file.")

       
        with open(log_file, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(log_file)
            )

        with open(zip_file, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(zip_file)
            )

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

        logger.info("Email sent successfully")

    except Exception as e:
        logger.error(f"Email Error : {str(e)}")


def main():
    logger, log_file = setup_logger()

    try:
        if len(sys.argv) != 3:
            logger.error("Invalid arguments")
            return

        source = sys.argv[1]
        receiver = sys.argv[2]

        zip_file = create_backup(source, logger)

        if zip_file:
            send_email(receiver, zip_file, log_file, logger)

    except Exception as e:
        logger.error(f"Unhandled Error : {str(e)}")

if __name__ == "__main__":
    main()
