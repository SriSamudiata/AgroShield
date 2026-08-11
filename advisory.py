
def get_weather_value(weather, key, default=0):

    try:

        return weather["current"].get(
            key,
            default
        )

    except:

        return default


# =========================================================
# CREATE ADVISORY
# =========================================================

def create_advisory(crop, weather, image):

    crop_lower = crop.lower()


    # -----------------------------------------------------
    # WEATHER VALUES
    # -----------------------------------------------------

    temperature = get_weather_value(
        weather,
        "temperature_2m",
        25
    )


    humidity = get_weather_value(
        weather,
        "relative_humidity_2m",
        60
    )


    rainfall = get_weather_value(
        weather,
        "precipitation",
        0
    )


    wind = get_weather_value(
        weather,
        "wind_speed_10m",
        5
    )


    # =====================================================
    # WEATHER RISK
    # =====================================================

    weather_risks = []


    if humidity >= 80:

        weather_risks.append(
            "High humidity may increase the risk of fungal "
            "and bacterial leaf problems."
        )

    elif humidity >= 65:

        weather_risks.append(
            "Moderate humidity means the crop should be "
            "monitored for increasing leaf disease."
        )

    else:

        weather_risks.append(
            "Current humidity is relatively low, which may "
            "reduce prolonged leaf-wetness risk."
        )


    if rainfall > 5:

        weather_risks.append(
            "Recent rainfall may keep leaves wet and can "
            "increase disease spread."
        )

    elif rainfall > 0:

        weather_risks.append(
            "Some rainfall is present. Avoid unnecessary "
            "foliar spraying immediately before rain."
        )

    else:

        weather_risks.append(
            "No significant current rainfall is detected."
        )


    if wind > 20:

        weather_risks.append(
            "Strong wind may reduce spraying effectiveness "
            "and increase spray drift."
        )


    # =====================================================
    # CROP ASSESSMENT
    # =====================================================

    if "paddy" in crop_lower or "rice" in crop_lower:

        if humidity >= 75:

            diagnosis = (
                "Possible fungal leaf disease or leaf-spot stress."
            )

        else:

            diagnosis = (
                "Possible leaf disease, nutrient stress, "
                "or physical damage."
            )


    elif (
        "tomato" in crop_lower
        or "potato" in crop_lower
        or "chilli" in crop_lower
        or "pepper" in crop_lower
    ):

        if humidity >= 75:

            diagnosis = (
                "Possible fungal or bacterial leaf disease "
                "or leaf-spot stress."
            )

        else:

            diagnosis = (
                "Possible leaf disease, pest damage, "
                "or nutrient stress."
            )


    elif (
        "cotton" in crop_lower
        or "maize" in crop_lower
        or "corn" in crop_lower
        or "groundnut" in crop_lower
        or "peanut" in crop_lower
    ):

        if humidity >= 75:

            diagnosis = (
                "Possible moisture-associated leaf disease "
                "or leaf stress."
            )

        else:

            diagnosis = (
                "Possible pest damage, nutrient stress, "
                "or environmental leaf stress."
            )


    else:

        if humidity >= 80:

            diagnosis = (
                "Possible moisture-associated leaf disease "
                "or leaf stress."
            )

        elif rainfall > 2:

            diagnosis = (
                "Possible leaf disease, pest damage, "
                "or weather-related stress."
            )

        else:

            diagnosis = (
                "Possible leaf disease, pest damage, "
                "nutrient deficiency, or environmental stress."
            )


    # =====================================================
    # CONFIDENCE
    # =====================================================

    confidence = "Preliminary"


    # =====================================================
    # IMAGE OBSERVATIONS
    # =====================================================

    visual_evidence = [

        "A crop image was successfully received.",

        "Check the leaves for spots, yellowing, lesions, "
        "holes, curling, discoloration, and drying.",

        "A clear close-up image of the affected area can "
        "improve the assessment."

    ]


    # =====================================================
    # POSSIBLE CAUSES
    # =====================================================

    possible_causes = [

        "Fungal or bacterial infection may become more "
        "likely when humidity and leaf moisture remain high.",

        "Insect feeding can cause holes, spots, curling, "
        "or damaged leaf tissue.",

        "Nutrient imbalance can cause yellowing, "
        "discoloration, or poor leaf development.",

        "Poor drainage, heat, drought, or excessive moisture "
        "can also stress the crop."

    ]


    # =====================================================
    # WHAT TO DO
    # =====================================================

    what_to_do_now = [

        "Inspect several plants in different parts of "
        "the field instead of relying on one leaf.",

        "Check the underside of leaves for insects, "
        "eggs, webbing, or unusual discoloration.",

        "Avoid unnecessary overhead irrigation and "
        "maintain good field ventilation.",

        "Remove severely damaged plant material where "
        "appropriate.",

        "Do not apply pesticides based only on this "
        "preliminary assessment. Follow the product label."

    ]


    # =====================================================
    # WHEN TO ACT
    # =====================================================

    if rainfall > 2:

        when_to_act = (

            "Avoid applying foliar treatments immediately "
            "before rainfall. If treatment is confirmed "
            "necessary, choose a dry weather window after "
            "the foliage has dried."

        )


    elif wind > 20:

        when_to_act = (

            "Avoid spraying during strong winds. Wait for "
            "a calmer period and follow the product label."

        )


    elif humidity >= 80:

        when_to_act = (

            "Inspect the crop as soon as possible. High "
            "humidity means disease symptoms should be "
            "monitored closely."

        )


    else:

        when_to_act = (

            "Inspect affected plants today and monitor "
            "nearby plants for spreading symptoms."

        )


    # =====================================================
    # CROP SAVING PLAN
    # =====================================================

    crop_saving_plan = [

        "Today: inspect affected and nearby plants.",

        "Next 24–48 hours: check irrigation, drainage, "
        "ventilation, and visible pest activity.",

        "Next several days: monitor new leaves and nearby "
        "plants for increasing spots, yellowing, holes, "
        "curling, or wilting.",

        "If the problem spreads rapidly, consult a local "
        "agricultural expert or extension officer."

    ]


    # =====================================================
    # PREVENTION
    # =====================================================

    prevention = [

        "Avoid excessive irrigation and prolonged "
        "leaf wetness.",

        "Maintain appropriate crop spacing and ventilation.",

        "Monitor crops regularly so problems are detected early.",

        "Use healthy planting material.",

        "Maintain balanced crop nutrition."

    ]


    # =====================================================
    # RETURN RESULT
    # =====================================================

    return {

        "diagnosis": diagnosis,

        "confidence": confidence,

        "visual_evidence": visual_evidence,

        "possible_causes": possible_causes,

        "what_to_do_now": what_to_do_now,

        "when_to_act": when_to_act,

        "weather_risk": weather_risks,

        "crop_saving_plan": crop_saving_plan,

        "prevention": prevention,

        "needs_expert_confirmation": True

    }
