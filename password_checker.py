
import string

print("=== Password Strength Checker ===")

password = input("Enter a test password: ")

checks = {
    "12 or more characters": len(password) >= 12,
    "Uppercase letter": any(c.isupper() for c in password),
    "Lowercase letter": any(c.islower() for c in password),
    "Number": any(c.isdigit() for c in password),
    "Special character": any(c in string.punctuation for c in password)
}

score = sum(checks.values())

for check, passed in checks.items():
    print(("PASS" if passed else "FAIL") + " - " + check)

print(f"\nScore: {score}/5")

if score == 5:
    print("All checks passed!")
elif score >= 3:
    print("Some checks passed. Improve your password.")
else:
    print("Weak password!")
