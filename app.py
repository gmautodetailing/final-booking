from flask import Flask, render_template, request, redirect
import utils.sheet_handler as sheet

app = Flask(__name__)

def categorize_postcode(postcode):
    cleaned = postcode.replace(" ", "").upper()
    if cleaned.startswith("SW147"):
        return "West"
    elif cleaned.startswith("SW148"):
        return "East"
    return "Out of Area"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        postcode = request.form["postcode"]
        service = request.form["service"]
        date = request.form["date"]
        time = request.form["time"]
        zone = categorize_postcode(postcode)
        if sheet.is_slot_available(date, time, zone):
            sheet.save_booking(name, phone, postcode, service, date, time, zone)
            return redirect("/success")
        else:
            return render_template("index.html", error="Slot already booked!", zone=zone)
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run()
