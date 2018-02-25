kim = 1234
ed = 45

car = 20000
fruit = 10
eds_fruit = 0

while ed >= fruit:
    eds_fruit = 1 + eds_fruit
    print("Ed has %d, and kim has %d" % (ed, kim))
    ed = ed - fruit
print ("ed bought %d fruits" % (eds_fruit))


