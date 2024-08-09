import re

def assess_password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 10  # Increased minimum length
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Scoring the password
    score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_char_criteria
    ])

    # Adjusted strength assessment
    if score == 5 and len(password) >= 12:
        strength = "Very Strong"
    elif score == 4 and len(password) >= 10:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Providing feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 10 characters long.")
    if not uppercase_criteria:
        feedback.append("Add at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Add at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Include at least one number.")
    if not special_char_criteria:
        feedback.append("Include at least one special character (e.g., !@#$%^&*).")

    return strength, feedback

# Example usage
password = input("Enter a password to assess its strength: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback for improvement:")
    for item in feedback:
        print(f"- {item}")
