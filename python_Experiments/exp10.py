tabby_cat="\tI'm tabbed in"
persian_cat="I'm split \n on a line"
back_cat="I'm \\ a \\ cat"
fat_cat="""
I'll do a list
\t*cat food
\t*cat fishes
\t* catnip\n\t* grass
"""
print tabby_cat
print persian_cat
print back_cat
print fat_cat
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

