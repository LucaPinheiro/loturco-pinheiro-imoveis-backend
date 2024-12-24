class Constants:
    REGEX_EMAIL = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    REGEX_PASSWORD = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=\[{\]};:'\",<.>/?]).{8,}$"
    REGEX_PASSWORD_ERROR = "password must be at least 8 characters long and contain at least one letter, one number and one special digit"