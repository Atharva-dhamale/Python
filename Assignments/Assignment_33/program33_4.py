import os
import time
import smtplib
import psutil
from email.message import EmailMessage
from datetime import datetime


SENDER_EMAIL = "atharvaserverpython@gmail.com"
APP_PASSWORD = "abcd efgh ijkl mnop" 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587



def create_log_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def get_system_summary():
    processes = list(psutil.process_iter(['pid', 'name', 'cpu_percent',
                                           'memory_info', 'num_threads']))

    summary = {}
    summary["total_processes"] = len(processes)

    summary["top_cpu"] = sorted(processes,
        key=lambda p: p.info['cpu_percent'],
        reverse=True)[:5]

    summary["top_memory"] = sorted(processes,
        key=lambda p: p.info['memory_info'].rss,
        reverse=True)[:5]

    summary["top_threads"] = sorted(processes,
        key=lambda p: p.info['num_threads'],
        reverse=True)[:5]

    summary["top_open_files"] = sorted(processes,
        key=lambda p: len(p.open_files()) if p.pid else 0,
        reverse=True)[:5]

    return summary

def write_log(folder, summary):
    filename = f"{folder}/Log_{datetime.now().strftime('%d%m%Y_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write("----- System Surveillance Report -----\n\n")

        f.write(f"Total Processes : {summary['total_processes']}\n\n")

        f.write("Top CPU Usage Processes:\n")
        for p in summary["top_cpu"]:
            f.write(f"{p.pid} {p.name()} CPU: {p.cpu_percent()}%\n")

        f.write("\nTop Memory Usage Processes:\n")
        for p in summary["top_memory"]:
            f.write(f"{p.pid} {p.name()} RSS: {p.memory_info().rss}\n")

        f.write("\nTop Thread Count Processes:\n")
        for p in summary["top_threads"]:
            f.write(f"{p.pid} {p.name()} Threads: {p.num_threads()}\n")

        f.write("\nTop Open File Processes:\n")
        for p in summary["top_open_files"]:
            try:
                f.write(f"{p.pid} {p.name()} OpenFiles: {len(p.open_files())}\n")
            except:
                f.write(f"{p.pid} {p.name()} Access Denied\n")

    return filename

def send_email(receiver, logfile):
    msg = EmailMessage()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver
    msg['Subject'] = "Periodic System Surveillance Report"

    msg.set_content("Please find attached system surveillance log file.")

    with open(logfile, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(logfile)
        )

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()



def main():
    if len(os.sys.argv) != 4:
        print("Usage:")
        print('python3 PlatformSurveillance.py "LogFolder" "receiver@gmail.com" interval')
        return

    folder = os.sys.argv[1]
    receiver = os.sys.argv[2]
    interval = int(os.sys.argv[3]) * 60

    create_log_folder(folder)

    print("Platform Surveillance Started...")

    while True:
        summary = get_system_summary()
        logfile = write_log(folder, summary)
        send_email(receiver, logfile)
        time.sleep(interval)

if __name__ == "__main__":
    main()
