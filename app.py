from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## assignment10
from pages.assignment10.assignment10 import assignment10  # the last "assignment10" is row 4 in the assignment10.py file
app.register_blueprint(assignment10)

##### Components
## base
from components.base.base import base
app.register_blueprint(base)


if __name__ == '__main__':
    app.run(debug=True)

