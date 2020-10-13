tup = ('c', 'b', 'a', 'd', 'e', 'f', 'i', 'j', 'g', 'h', 'k')

print('Top five')
for i in range(5):
    print(tup[i])

count = 0;
print('Last four')
for c in range(len(tup)-1, -1, -1):
    if count < 4:
        count+=1
        print(tup[c])

print("Sorted")
for g in sorted(tup):
    print(g)


print(f"index of 'a': {tup.index('a')}")