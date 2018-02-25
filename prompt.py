bad = "fuck"


m = input ("tell me something: ")
index = m.find(bad)

print(index)
print (m)

if index is not -1:
    print ("naughty")
