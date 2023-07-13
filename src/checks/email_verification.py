import re

def verify_email(email: str) -> bool:
    pattern = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    valid_email = re.compile(pattern).findall(email)
    if not valid_email:
        return False
    return True
