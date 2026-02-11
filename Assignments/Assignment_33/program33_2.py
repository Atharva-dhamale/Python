import os

def is_number(s):
    return s.isdigit()

def count_open_files(pid):
    fd_path = f"/proc/{pid}/fd"
    try:
        return len(os.listdir(fd_path))
    except PermissionError:
        return "Access Denied"
    except FileNotFoundError:
        return None

def main():
    print(f"{'PID':<10} {'Open Files'}")
    print("-" * 30)

    for entry in os.listdir("/proc"):
        if is_number(entry):
            result = count_open_files(entry)

            if result is None:
                continue
            elif result == "Access Denied":
                print(f"{entry:<10} Access Denied")
            else:
                print(f"{entry:<10} {result}")

if __name__ == "__main__":
    main()
