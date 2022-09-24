from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r"^996\d{9}$", message="The client's phone number in the format 996XXXXXXXXX"
)
