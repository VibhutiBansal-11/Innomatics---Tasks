from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []

@app.route("/delete", methods=["POST"])
def delete():
    global notes
    note_delete = request.form.get("note")
    notes.remove(note_delete)
    return redirect("/")


@app.route('/', methods=["GET","POST"])
def index():
    global notes
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)