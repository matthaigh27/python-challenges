single = ["one", "two", "three", "four", "five", "six",
          "seven", "eight", "nine", "ten", "eleven", "twelve",
          "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", ""]
tens = ["", "twenty ", "thirty ", "fourty ", "fifty ",
        "sixty ", "seventy ", "eighty ", "ninety ", ""]
order = ["", "thousand", "million", "billion", "trillion", "quadrillion",
         "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion"]


def numtoword(x):
    word = ""
    x = str(x)
    if len(x) % 3 == 1:
        x = "00" + x
    elif len(x) % 3 == 2:
        x = "0" + x
    for i in range(len(x) // 3):
        if x[3*i] != "0":
            word += single[int(x[3*i]) - 1] + " hundred" + " and "
        elif i != 0:
            word += "and "
        if int(x[3*i + 1]) - 1 :
            word += tens[int(x[3*i + 1]) - 1]
            word += single[int(x[3*i + 2]) - 1] + " "
        else:
            word += single[int(x[3*i+1:3*i + 3]) - 1] + " "
        word += order[len(x) // 3 - i - 1] + " "
    return word


print(numtoword(4029305))
