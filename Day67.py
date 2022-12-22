print("diketahui : ")
print(" u : (-6, 0, 4)")
print(" v : (3, 1, 6)")

print()
print("ditanyakan ?")

print("lancip ?")
print("tumpul ?")
print("ortogonal ?")


lancip = "lancip"
tumpul = "tumpul"
ortogonal = "ortogonal"

print()
print("rumus yang di gunakan : u.v")
print()
print("u.v = (-6)*3 + 0*1 + 4*6")
uv = (-6)*3 + 0*1 + 4*6

print()
if uv > 0:
    print("hasil : ", uv, "berarti dia di katakan", lancip)

elif uv < 0:
    print("hasil : ", uv, "berarti dia di katakan", tumpul)

elif uv == 0:
    print("hasil : ", uv, "berarti dia di katakan", ortogonal)
