formatter = "{} {} {} {}"
lookHere = "Oii"
print(formatter.format(1, 2 , 3 ,4))
print(formatter.format("one","two","three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, lookHere, formatter))
print(formatter.format(
    1,
    2,
    3,
    4
))