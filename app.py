# Libraries
# ------------------------------------------------------------------------------
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, jsonify

from linkedin_summarizer import linkedin_summarizer


# Code
# ------------------------------------------------------------------------------
# Initialize a Flask application
app = Flask(__name__)

# Define the root route that renders the index.html template
@app.route("/")
def index():
    return render_template("index.html")

# Define a route to handle POST requests when the form is submitted
@app.route("/process", methods=["POST"])
def process():
    # Extract the 'name' field from the form data sent in the POST request
    name = request.form["name"]

    # Call linkedin_summarizer
    summary, profile_pic_url = linkedin_summarizer(name=name)
    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "picture_url": profile_pic_url,
        }
    )

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    # Run in local
    app.run(host="0.0.0.0", debug=True)