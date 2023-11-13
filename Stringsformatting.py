name = ["John", "Edy", "Jane", "Kane"]
scores = [80, 95, 80, 75]
print("{0:<10} {1:<5}".format("Name", "scores"))
for index in range(len(name)):
    # print(f"{name[index]} {scores[index]}")
    names = name[index]
    score = scores[index]
    print("{0:<10} {1:<5}".format(names, score))
