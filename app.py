
from flask import Flask, render_template, request, jsonify

from weather import get_weather
from advisory import create_advisory


app = Flask(__name__)


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# ASSESSMENT
# =========================================================

@app.route("/assess", methods=["POST"])
def assess():

    try:

        crop = request.form.get("crop", "").strip()

        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")

        image = request.files.get("image")


        # -------------------------------------------------
        # CHECK CROP
        # -------------------------------------------------

        if not crop:

            return jsonify({
                "error": "Please enter the crop name."
            }), 400


        # -------------------------------------------------
        # CHECK IMAGE
        # -------------------------------------------------

        if not image:

            return jsonify({
                "error": "Please upload a crop image."
            }), 400


        # -------------------------------------------------
        # CHECK LOCATION
        # -------------------------------------------------

        if not latitude or not longitude:

            return jsonify({
                "error": "Please allow your location."
            }), 400


        # -------------------------------------------------
        # GET WEATHER
        # -------------------------------------------------

        weather = get_weather(
            latitude,
            longitude
        )


        # -------------------------------------------------
        # CREATE ADVISORY
        # -------------------------------------------------

        result = create_advisory(
            crop,
            weather,
            image
        )


        return jsonify(result)


    except Exception as error:

        print("ASSESSMENT ERROR:")
        print(error)

        return jsonify({
            "error": "Something went wrong while creating the assessment."
        }), 500


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )

