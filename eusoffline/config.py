

# config database uri here
class Config:
    SECRET_KEY = 'c9970460fc2c3ad324add53c94e3bc2a'
    # SQLALCHEMY_DATABASE_URI = 'postgres://bobby:zmq,bs2008@localhost:5432/eusoffline'
    SQLALCHEMY_DATABASE_URI = 'postgres://ittldgsyeuwklc:e8222e6169a4f74b4725bd21cfdb566177a4591ab52eedee4603c9fec7a07e4b@ec2-52-73-247-67.compute-1.amazonaws.com:5432/d8il6ph5hhlh28'
    # Shown in and email templates and page footers
    USER_APP_NAME = "Jersey Bidder"
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form
