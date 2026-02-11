import os

PAGE_SIZE = os.sysconf("SC_PAGE_SIZE") // 1024  
TOTAL_MEMORY_KB = int(open("/proc/meminfo").read().split("MemTotal:")[1].split()[0])

process_list = []

def get_memory_info(pid):
    try:
        with open(f"/proc/{pid}/statm", "r") as f:
            data = f.read().split()
            vms = int(data[0]) * PAGE_SIZE  
            rss = int(data[1]) * PAGE_SIZE   

        mem_percent = (rss / TOTAL_MEMORY_KB) * 100
        return rss, vms, mem_percent

    except PermissionError:
        return "Access Denied", "Access Denied", "Access Denied"
    except FileNotFoundError:
        return None, None, None

def get_process_name(pid):
    try:
        with open(f"/proc/{pid}/comm", "r") as f:
            return f.read().strip()
    except:
        return "Unknown"

def main():
    for entry in os.listdir("/proc"):
        if entry.isdigit():
            rss, vms, mem_percent = get_memory_info(entry)

            if rss is None:
                continue

            process_list.append({
                "pid": entry,
                "name": get_process_name(entry),
                "rss": rss,
                "vms": vms,
                "mem_percent": mem_percent
            })

    
    process_list.sort(
        key=lambda x: x["rss"] if isinstance(x["rss"], int) else 0,
        reverse=True
    )

    print(f"{'PID':<8}{'Process':<20}{'RSS(KB)':<12}{'VMS(KB)':<12}{'MEM %'}")
    print("-" * 65)

    for proc in process_list[:10]:
        if proc["rss"] == "Access Denied":
            print(f"{proc['pid']:<8}{proc['name']:<20}Access Denied")
        else:
            print(f"{proc['pid']:<8}{proc['name']:<20}"
                  f"{proc['rss']:<12}{proc['vms']:<12}"
                  f"{proc['mem_percent']:.2f}")

if __name__ == "__main__":
    main()
