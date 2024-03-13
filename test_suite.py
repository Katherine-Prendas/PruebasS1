from src.login_module import Login
from src.form_functionality import Form

class TestExamples:
    def test_001_name_has_more_than_30_chars_message(self):
        form = Form()
        actual_message = form.enter_name("gfasdgasdgasdgasdfgasdgasdgasdgasdgasdgasdgasdgasdgasdgasdggsdfghsdfasdfhfghdfghdfghdfghdfghdfghdfghdfgh")
        assert actual_message == 'name has more than 30 chars'

    def test_002_enter_name_valid(self):
        form = Form()
        actual_message = form.enter_name("Kathy")
        assert actual_message == "Your name is Kathy"

    def test_003_enter_name_too_short(self):
        form = Form()
        actual_message = form.enter_name("Jo")
        assert actual_message == "Invalid value"

    def test_004_enter_age_too_short(self):
        form = Form()
        actual_message = form.enter_age("2")
        assert actual_message == "Invalid value for field age"

    def test_005_validate_user_email_mandatory(self):
        login = Login()
        login.email = ""
        actual_message = login.validate_user()
        assert(actual_message, 'Email is mandatory')

    def test_006_validate_user_invalid_credentials(self):
        login = Login()
        login.email = "wrong@example.com"
        actual_message = login.validate_user()
        assert(actual_message, 'Invalid credentials')

    def test_007_validate_user_valid_email_format(self):
        login = Login()
        login.email = "example@mail.com"
        actual_message = login.validate_user()
        assert(actual_message, 'Valid email format')

    def test_008_validate_user_invalid_email(self):
        login = Login()
        login.email = "invalid_email"
        actual_message = login.validate_user()
        assert(actual_message, 'Invalid email')

    def test_009_validate_password_password_mandatory(self):
        login = Login()
        login.password = ""
        actual_message = login.validate_password()
        assert(actual_message, 'password is mandatory')

    def test_010_validate_password_invalid_password(self):
        login = Login()
        login.password = "password123"
        actual_message = login.validate_password()
        assert(actual_message, 'Invalid password')

    def test_011_validate_password_valid_password(self):
        login = Login()
        login.password = "pass1234"
        actual_message = login.validate_password()
        assert(actual_message, 'Valid password')
        
    def test_012_enter_name_valid(self):
        form = Form()
        actual_message = form.enter_name("Kathy")
        assert actual_message == "Your name is Kathy"