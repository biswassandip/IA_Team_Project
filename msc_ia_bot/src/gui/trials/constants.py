"""
This is a constants module that is used for setting GUI properties.
"""

# GENERAL
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PWD_REGEX = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,12}$'
FONT_NAME="Helvetica"
FONT_SIZE=12

# LOGIN SCREEN (login_screen.py)
LOGIN_TITLE = "Login"
EMAIL_LABEL = "Email:"
PWD_LABEL = "Password:"
LOGIN_BTN = "Login"
CANCEL_BTN = "Cancel"
CREATE_BTN = "Create & Login"
EMAIL_TOOLTIP="Email should be in the format example@email.com"
PWD_TOOLTIP="6-12 in length, uppercase, number and a special character"
LOGIN_SCREEN_SIZE="315x220"
LOGIN_SCREEN_WIDTH=315
LOGIN_SCREEN_HEIGHT=220