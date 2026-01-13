def is_valid_email(email):
    # Check for exactly one '@'
    if email.count('@') != 1:
        return False

    username, domain = email.split('@')

    # Check username and domain are not empty
    if not username or not domain:
        return False

    # Domain must contain at least one dot
    if '.' not in domain:
        return False

    # Dot should not be at the start or end of domain
    if domain.startswith('.') or domain.endswith('.'):
        return False

    return True


# Example usage
email_input = input("Enter an email address: ")

if is_valid_email(email_input):
    print("Valid email address")
else:
    print("Invalid email address")
