x = input().strip()
y = x.split(" ")
print(len(y))
a = ""
for i in range(len(y) // 2):
    if y[i * 2] == "0015":
        if y[i * 2 + 1] == "0015":
            a += "0"
        elif y[i * 2 + 1] ==  "003f":
            a += "1"
    else:
        if a != "":
            print(f"{a} ({len(a)})")
            a = ""
# for z in y:
#     if z == "0015":
#         a += "0"
#     elif z ==  "003f":
#         a += "1"
#     elif a != "":
#         print(f"{a} ({len(a)})")
#         a = ""
print(a)