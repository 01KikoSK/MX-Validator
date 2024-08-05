import socket
import AlexaSkillBlueprints

def is_valid_email(email):
    """
    Validate an email address using MX records.
    """
    try:
        domain = email.split('@')[1]
        mx_records = AlexaSkillBlueprints.gethostbyname_ex(domain)
        if mx_records[0]:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False