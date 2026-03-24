# ============================================================
#  WEEK 11 LAB — Q2: PASSWORD STRENGTH CHECKER
#  COMP2152 — Berhan Erdogan
# ============================================================
#
#  For the term project, you'll be looking for weak passwords
#  on 0x10.cloud. This class helps you understand what makes
#  a password weak or strong.
#
# ============================================================


class PasswordChecker:

    def __init__(self):
        self.common_passwords = [
            "admin",
            "password",
            "123456",
            "root",
            "guest",
            "letmein",
            "welcome"
        ]
        self.history = []

    def check_common(self, password):
        return password.lower() in self.common_passwords

    def check_strength(self, password):
        has_length = len(password) >= 8
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
        strength = {
            "length": has_length,
            "digit": has_digit,
            "special": has_special
        }
        return strength

    def evaluate(self, password):
        if self.check_common(password):
            result = "WEAK (common password)"
        else:
            strength = self.check_strength(password)
            result = {0: "WEAK", 1: "WEAK", 2: "MEDIUM", 3: "STRONG"}[sum(strength.values())]
        return result


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: PASSWORD STRENGTH CHECKER")
    print("=" * 60)

    checker = PasswordChecker()

    test_passwords = ["admin", "hello", "hello123", "MyP@ss99", "p@ssw0rd!", "root"]

    print("\n--- Checking Passwords ---")
    for pw in test_passwords:
        result = checker.evaluate(pw)
        if result:
            print(f"  {pw:<15} → {result}")

    print("\n--- Check History ---")
    if hasattr(checker, 'history') and checker.history:
        for pw, result in checker.history:
            print(f"  {pw:<15} : {result}")
    else:
        print("  (no history)")

    print("\n" + "=" * 60)
