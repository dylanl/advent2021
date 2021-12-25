measurements = open('input.txt', 'r')

depth_measurement = list(map(int, measurements.read().splitlines()))
count = 0
for i in range(0, len(depth_measurement) - 3):
    if sum(depth_measurement[i:i + 3]) < sum(depth_measurement[i + 1 : i + 4]):
        count = count + 1
print(count)
