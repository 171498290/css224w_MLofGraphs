import snap

# 创建一个空的向量
v = snap.TIntV()

# 添加元素
v.Add(1)
v.Add(2)
v.Add(3)
v.Add(4)
v.Add(5)

# 打印向量的长度
print(v.Len())

# 获取元素值
print(v[3])
v[3] = 2*v[2]
print(v[3])

for item in v:
    print(item)
for i in range(0, v.len()):
    print(i, v[i])
