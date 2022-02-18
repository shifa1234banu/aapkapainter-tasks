string1 = "Mary"
string2 = "Army"


string1 = string1.lower()
string2 = string2.lower()

if(len(string1) == len(string2)):

    sorted_str1 = sorted(string1)
    sorted_str2 = sorted(string2)

    if(sorted_str1 == sorted_str2):
        print("yes")
    else:
        print("no")

else:
    print("no")