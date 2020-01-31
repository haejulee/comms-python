import numpy as np

msg = np.array([[10,10],[20,20]])

out = bytes([1]) + bytes([0]) + str(msg.dtype).encode() + bytes([0]) + len(msg.shape).to_bytes(4, byteorder="big")
for i in msg.shape:
    out += i.to_bytes(4, byteorder="big")
out += msg.tobytes()

re = out

# get type
t = np.dtype(re.split(bytes([0]),2)[1].decode("utf-8"))
print(t)
# get dimentions
aftertype = re.split(bytes([0]),2)[2]
d = int.from_bytes(aftertype[:4], byteorder="big")
print(d)
# get shape
shape = []
for i in range(d):
    shape.append(int.from_bytes(aftertype[i*4 + 4: i*4 + 8], byteorder="big"))
shape = tuple(shape)
print(shape)
array = np.frombuffer(aftertype[d*4 + 4:], dtype = t)
array = array.reshape(*shape)

print(array)
