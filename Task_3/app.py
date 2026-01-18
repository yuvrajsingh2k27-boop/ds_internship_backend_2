from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for notes (for demo purposes)
notes = []

@app.route("/", methods=["GET", "POST"])
def home():
    global notes
    if request.method == "POST":
        note = request.form.get("note")
        if note and note.strip():  # Prevent empty notes
            notes.append(note.strip())
        return redirect(url_for("home"))  # Redirect to avoid form resubmission
    return render_template("home.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)