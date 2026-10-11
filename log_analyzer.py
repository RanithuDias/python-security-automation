
print("=== Security Log Analyzer ===")

with open("sample.log", "r") as file:
    logs = file.readlines()

failed_attempts = 0

for log in logs:
    if "FAILED LOGIN" in log:
        failed_attempts += 1
        print("Suspicious event:", log.strip())

print("\nTotal failed logins:", failed_attempts)

if failed_attempts >= 3:
    print("ALERT: Multiple failed login attempts!")
