import os
from flask import Flask, jsonify
from extenso import real
app = Flask(__name__)

#we define the route /
@app.route('/<int:num>', methods=["GET"])
def get_extenso(num):
    extenso = real(num)
    # return a json
    return jsonify({'extenso': extenso})

if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
