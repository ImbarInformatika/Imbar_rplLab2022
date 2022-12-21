print("u = 3, 2, -1")
print("v = 0, 2, -3")
print("w = 2, 6, 7")

print()
print("ditanya = u x (u x w)")

print()
print('''penyelesaian
U1 U2 U3
V1 V2 V3
W1 W2 W3''')

print()

u1 = 3
u2 = 2
u3 = -1

v1 = 0
v2 = 2
v3 = -3

w1 = 2
w2 = 6
w3 =  7


print(f'''{u1}, {u2}, {u3},
{v1}, {v2}, {v3},
{w1}, {w2}, {w3},''')

print()
print(f'''{u1} {u2} {u3} * |{u2} {u3}|  |{u1} {u3}|
         |{w2}  {w3}|  |{w1}  {w3}|
''')
print("<========> mencari nilai (u x w) ")
angka1 = (u2 * w3) + (u3 * w2)
angka2 = (u1 * w3) + (u3 * w1)

hasiluw = angka1 - angka2
print("hasil u * w : ", hasiluw)
print()

print("<========> mencari nilai u * (u x w) ")
hasiluuw = hasiluw * u1, hasiluw * u2, hasiluw * 3
print(hasiluuw)
