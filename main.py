def convert_to_integer(word):
    #import must be a dictionary word
    #Must return an integer (as a string)  
    word=word.lower()
    replace_dict = {
        'l': '1',
        'n': '2',
        'm': '3',
        'r': '4',
        'f': '5',
        'v': '5',
        'b': '6',
        'p': '6',
        't': '7',
        'ch': '8',
        'sh': '8',
        'g': '9',
        's': '0',
        'd': '9',
        'z': '0'
    }

    # Reverse the replace_dict for easier replacement
    replace_dict_reverse = {k: v for k, v in replace_dict.items()}

    for key, value in replace_dict_reverse.items():
        word = word.replace(key, value)
    # Remove all non-numeric characters
    result = ''.join([char for char in word if char.isdigit()])
    
    return result

def confirm(number, text):
    number=number.replace(".","")
    words=text.lower().split()
    result_number = ''.join(convert_to_integer(word) for word in words)
    if number==result_number:
        print("match")
    else:
        print("fail")

print(convert_to_integer("Calm cheeseboard"))
confirm("1380649","Calm cheeseboard")
