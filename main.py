from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/process-data', methods=['GET','POST'])
def process_data():
    if request.method == "GET":
        return render_template("index.html")
    else:
        data = request.form['input-data']  # Assuming JSON data is sent from frontend
        # Process the data (e.g., perform some computation)
    
        return f"<p>{data}</p>"    

if __name__ == '__main__':
    app.run(debug=True)
