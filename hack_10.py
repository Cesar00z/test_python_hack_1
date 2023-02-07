"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""


def fn_hack_10():
    result = "fooziman"
    # ...
    new_string = ""
    for letter in result:
        if letter == "a":
            new_string += letter.replace("a", "@")

        elif letter == "i":
            new_string += letter.replace("i", "1")

        elif letter == "o":
            new_string += letter.replace("o", "0")

        else:
            new_string += letter

    return list(new_string.upper())
