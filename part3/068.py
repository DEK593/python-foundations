txt = input("Word: ")
hashh = "*"


txt1 = len(txt)
lil = 30 - txt1 - 2
int(lil)


spaces = lil // 2
space_left  = " " * spaces
right_count = lil - spaces
right_space = " " * right_count
print(hashh * 30)
print(f"{hashh}{space_left}{txt}{right_space}{hashh}")
print(hashh * 30)

