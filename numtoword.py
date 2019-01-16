single = ["one", "two", "three", "four", "five", "six",
          "seven", "eight", "nine", "ten", "eleven", "twelve"]
tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
order = ["", "thousand", "million", "billion", "trillion", "quadrillion"]


def numtoword(x):
    x = str(x)[::-1]
    if len(x) % 3 == 1:
        x += "00"
    elif len(x) % 3 == 2:
        x += "0"
    for i in range(len(x) // 3):
        if i == 0:
            #do things for first 3
        else:
            #do things like normal ie 423 = four hundred and twenty three


numtoword(45)
