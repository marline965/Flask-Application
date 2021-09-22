from flask import Flask, request, jsonify
#rivescript import
import MovieBot
import utilities
#app creation
app=Flask(__name__)

#Route + return as objects
@app.route("/chat", methods=["POST"])
def chat():
        request_data = request.get_json()
        message = request_data['message']
        status, response = MovieBot.chat(message)
        data = {}
        if status == 0:
            data["reply"] = response
            data["status"] = 'Success'
            return jsonify(data)
        else:
            data["reply"] = response
            data["status"] = 'failed'
            return jsonify(data)

#Route to test           
@app.route("/test", methods=["POSTS"])
def TEST():
    request_data = request.get_json()
    message = request_data['message']
    return jsonify(utilities.save(message))


#app run
if __name__ == "__main__":
    app.run() 