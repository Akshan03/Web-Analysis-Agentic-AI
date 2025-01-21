from flask import Flask, request, render_template, jsonify
import subprocess
import nbformat

# Initialize Flask app
app = Flask(__name__)

# Load the notebook and define a function to execute it
def execute_agentic_rag(url, question):
    # Path to your notebook
    notebook_path = "agentic_rag.ipynb"

    # Load the notebook
    with open(notebook_path, 'r') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Inject the question and URL into the notebook's variables
    injected_code = f"""
url = "{url}"
question = "{question}"
"""
    notebook['cells'].insert(0, nbformat.v4.new_code_cell(injected_code))
    
    # Execute the notebook
    exec_namespace = {}
    for cell in notebook.cells:
        if cell.cell_type == "code":
            exec(cell.source, exec_namespace)
    
    # Get the answer from the executed notebook
    return exec_namespace.get("answer", "Error: Could not generate an answer.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask():
    url = request.form.get("url")
    question = request.form.get("question")

    if not url or not question:
        return jsonify({"error": "Both URL and question are required!"}), 400

    try:
        # Call the agentic_rag function
        answer = execute_agentic_rag(url, question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
