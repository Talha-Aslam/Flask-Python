from flask import Flask

app = Flask(__name__)

#http://127.0.0.1:5000/vstring/talha
# We defined string  function
@app.route('/vstring/<name>')
def string(name):
    return "My Name is %s" % name


#http://127.0.0.1:5000/vint/23
# We defined int function
@app.route('/vint/<int:age>')
def vint(age):
    return "My age is %d" % age

# we run app debugging mode
app.run(debug=True)