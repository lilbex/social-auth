from app import api
from app.resources import UserRegistration, HomePage

api.add_resource(UserRegistration, '/register')
api.add_resource(HomePage, '/')

# Add more routes if needed using regular Flask routes
