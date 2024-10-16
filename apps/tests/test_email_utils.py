from ..email_utils import is_valid_email

def test_valid_email():
    assert is_valid_email("example@example.com") == True

def test_invalid_email_no_at():
    assert is_valid_email("example.com") == False

def test_invalid_email_no_domain():
    assert is_valid_email("example@domain") == False

def test_valid_org_email():
    assert is_valid_email("example@example.org") == True
