def is_valid_email(email):
    if "@" not in email or not (email.endswith(".com") or email.endswith(".org")):
        return False
    return True
