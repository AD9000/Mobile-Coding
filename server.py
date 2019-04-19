from flask import Flask
from OnlineOrderingSystem import OnlineOrderingSystem
from staff import Staff

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

ordering_system = OnlineOrderingSystem()
staff = Staff(ordering_system)