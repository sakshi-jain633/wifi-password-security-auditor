# Importing Regular Expression module
import re

# Function to evaluate password strength
def check_password_strength(password):
    
    # Initial security score
    score = 0
    
    # List to store improvement suggestions
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 25
    else:
        suggestions.append("Use at least 12 characters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        suggestions.append("Add uppercase letters.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 15
    else:
        suggestions.append("Add lowercase letters.")

    # Check for numeric digits
    if re.search(r"\d", password):
        score += 15
    else:
        suggestions.append("Add numbers.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        suggestions.append("Add special characters.")

    # List of commonly used weak passwords
    common_passwords = [
        "password",
        "12345678",
        "qwerty",
        "admin",
        "wifi123",
        "password123"
    ]

    # Check if password is common
    if password.lower() not in common_passwords:
        score += 10
    else:
        suggestions.append("Avoid common passwords.")

    # Determine password strength level
    if score >= 85:
        strength = "Strong"
    elif score >= 60:
        strength = "Medium"
    else:
        strength = "Weak"

    # Return results
    return score, strength, suggestions


# Project Header
print("=" * 50)
print("      Wi-Fi Password Security Auditor")
print("=" * 50)

# Taking Wi-Fi password as input from user
password = input("\nEnter Wi-Fi Password to Audit: ")

# Perform password security audit
score, strength, suggestions = check_password_strength(password)

# Display security report
print("\nSecurity Report")
print("-" * 30)
print(f"Strength : {strength}")
print(f"Score    : {score}/100")

# Display recommendations if any weaknesses are found
if suggestions:
    print("\nRecommendations:")
    for suggestion in suggestions:
        print(f"• {suggestion}")
else:
    print("\nExcellent! No security issues found.")

# End of audit
print("\nAudit Complete.")