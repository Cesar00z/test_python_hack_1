"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    #...
    resultado = ""
    for letter in result:
        if letter == "o":
            resultado += letter.replace('o', "0")

        elif letter == "a":
            resultado += letter.replace('a', "@")

        elif letter == "i":
            resultado += letter.replace('i', "1")
        
        elif letter != "":
            resultado += letter
    return resultado 