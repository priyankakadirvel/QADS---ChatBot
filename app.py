from flask import Flask, render_template, request, jsonify
from retriever import retrieve_context
from generator import generate_answer
from gemini_fallback import query_gemini
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        context = retrieve_context(question)
        if not context:
            # Fallback to Gemini API if local retrieval fails
            context = query_gemini(question)
        answer = generate_answer(question, context)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
