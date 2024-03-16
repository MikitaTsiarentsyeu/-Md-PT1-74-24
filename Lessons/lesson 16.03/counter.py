test_str = "some relatively long string"

d = {}

for i in test_str:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

# s_count = 0
# o_count = 0
# m_count = 0
# w_count = 0

# for i in test_str:
#     if i == 's':
#         s_count += 1
#     elif i == 'o':
#         o_count += 1
#     elif i == 'm':
#         m_count += 1
#     elif i == 'w':
#         w_count += 1

# print(s_count, o_count, m_count, w_count)