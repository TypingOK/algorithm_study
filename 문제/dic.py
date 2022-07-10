test = {}
test[0] = [6, 2]
test[1] = [13, 14]
test[2] = [7, 5]
test[3] = [7, 4]

test = dict(sorted(test.items(), key=lambda x: (x[1][0],x[1][1])))

print(test.keys())
