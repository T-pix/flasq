from flask import Flask
from routes.home import home_page
from routes.customer import customer_route

app = Flask(__name__)

app.register_blueprint(home_page)
app.register_blueprint(customer_route,url_prefix='/customers')

app.run(debug=True)