from flask import Flask,jsonify,request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
import pathlib
desktop = pathlib.Path.home() / 'Desktop'

rounds = 0
playersa = 0
round_data = 0
question_data = 0

@app.route('/')
def jeopardy_board():
    round_number = request.args.get('round')
    print(round_number)

    questions = round_data[round_number]['questions']
    headers = round_data[round_number]['headers']
    print(questions)
    print(headers)
    data = {
        "questions": questions,
        "headers": headers
    }

    return jsonify(data)


@app.route('/question')
def question():
    round_number = request.args.get('round')
    # Default to question 1 if no question number is provided
    question_number = int(request.args.get('question'))
    question_index = question_number - 1
    print(round_number)
    if question_index >= 0 and question_index < len(question_data[round_number]['questions']):
        return jsonify({"question": question_data[round_number]['questions'][question_index],
                        "answer": question_data[round_number]['answers'][question_index]})
    else:
        return jsonify({"question": "Question number out of range"})


@app.route("/players")
def players():
    return jsonify(playersa)


@app.route("/questionDone")
def completedQuestion():
    round_number = request.args.get('round')
    question_number = int(request.args.get('question'))
    question_index = question_number - 1
    if question_index < len(round_data[str(round_number)]['questions']):
        round_data[round_number]['questions'][question_index] = '-'
        return jsonify({"done": True})
    else:
        return jsonify({"done": False})


@app.route("/rounds")
def totalrounds():
    return jsonify({"rounds": rounds})

@app.route("/uploadjson", methods = {"POST"})
def uploadJson():
    if request.method == "POST":
        global rounds,round_data,playersa,question_data
        rounds = request.json["rounds"]
        round_data = request.json["round_data"]
        playersa = request.json["playersa"]
        question_data = request.json["question_data"]
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
@app.route("/updateScore", methods=['POST'])
def updateScore():
    dct = {element['id']: element for element in playersa}
    data = request.get_json()
    for i in data['incrementPlayer']:
        dct[i]['score'] += data['score']
    for i in data['decrementPlayer']:
        dct[i]['score'] -= data['score']
    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(debug=True,port=5000)
