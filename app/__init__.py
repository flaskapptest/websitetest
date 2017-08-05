from flask import Flask



app = Flask(__name__, instance_relative_config = True,static_url_path='/static')


from app import views


app.config.from_object('config')
