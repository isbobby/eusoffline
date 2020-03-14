

# config database uri here
class Config:
    SECRET_KEY = 'c9970460fc2c3ad324add53c94e3bc2a'
    SQLALCHEMY_DATABASE_URI = 'postgres://bobby:zmq,bs2008@localhost:5432/eusoffline'

    # Shown in and email templates and page footers
    USER_APP_NAME = "Jersey Bidder"
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form
