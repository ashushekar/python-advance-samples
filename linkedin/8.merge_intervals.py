intervals = [[3,9],[2,6],[8,10],[15,18]]
start = sorted([x[0] for x in intervals])
end = sorted([x[1] for x in intervals]) #mimicking your start/end lists
merged = []
j = 0
new_start = 0

for i in range(len(start)):
    if start[i]<end[j]:
        continue
    else:
        j = j + 1
        merged.append([start[new_start], end[j]])
        new_start = i
print(merged) 