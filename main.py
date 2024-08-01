

import mood_responses

def my_mood_today():

    moods = input("How are you feeling today? ").strip()
    feelings_response = mood_responses.get_mood_response(moods)

    print(feelings_response)

my_mood_today()