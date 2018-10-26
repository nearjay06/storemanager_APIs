from flask import Flask
from view import views
# app = Flask(__name__)

   
if __name__ =='__main__':
 views.app.run(debug=True, port=8080)







