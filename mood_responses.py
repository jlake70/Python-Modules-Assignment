

def get_mood_response(moods):
    moods = moods.lower()
    if moods == "sad":
        return "I'm sorry to hear that."
    if moods == "happy":
        return "Keep that beautiful smile!"
    if moods == "mad":
        return "Calm down, it will get better."
    else:
        return "Sorry, no response for that feeling."


 