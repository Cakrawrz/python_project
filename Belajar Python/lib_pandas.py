import pandas

mydataset = {
    "cars": ["bmw", "void", "ford"],
    "passings": [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)