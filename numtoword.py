single = ["one", "two", "three", "four", "five", "six",
          "seven", "eight", "nine", "ten", "eleven", "twelve"]
order = ["", "thousand", "million", "billion", "trillion", "quadrillion"]


def numtoword(x):
    x = str(x)[::-1]
    print(len(x) % 3)
    if len(x) % 3 == 1:
        x += "00"
    elif len(x) % 3 == 2:
        x += "0"
    for i in range(len(x) / 3)


numtoword(45)
