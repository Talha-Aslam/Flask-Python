from flask import Flask
app = Flask(__name__)  # Create a Flask application instance

# Define a route for the root URL       
@app.route('/')
def hello_world():
    return 'Hello, World!'  # Return a simple response  

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode