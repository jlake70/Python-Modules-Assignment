
import text_utils as ut

def string_convert():

    string = input("Type a word or sentence. ").strip()
    cap_convert = ut.capitalize_string(string)
    reverse_convert = ut.reverse_string(string)

    print(f"Capitalized String: {cap_convert}")
    print(f"Reversed String: {reverse_convert}")

string_convert()