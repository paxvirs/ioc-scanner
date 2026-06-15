# IOC Scanner

with open("ioc_list.txt", "r") as file:
    iocs = [line.strip() for line in file]

with open("sample_log.txt", "r") as file:
    log_data = file.read()

print("=" * 50)
print("IOC SCANNER V2")
print("=" * 50)

matches_found = 0

for ioc in iocs:

    if ioc in log_data:

        if "." in ioc and any(char.isalpha() for char in ioc):
            print(f"[ALERT] Suspicious Domain Detected: {ioc}")

        else:
            print(f"[ALERT] Suspicious IP Detected: {ioc}")

        matches_found += 1

print("\n" + "=" * 50)

if matches_found == 0:
    print("No IOCs Detected")
else:
    print(f"Total IOCs Detected: {matches_found}")

print("=" * 50)