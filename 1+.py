measurements = open('input.txt', 'r')

depth_measurement = measurements.read().splitlines()
count = 0
for i in range(0, len(depth_measurement) - 3):
    if sum(map(int, depth_measurement[i:i + 3])) < sum(map(int, depth_measurement[i + 1 : i + 4])):
    #if (int(depth_measurement[i]) + int(depth_measurement[i + 1]) + int(depth_measurement[i + 2])) < (int(depth_measurement[i + 1]) + int(depth_measurement[i + 2]) + int(depth_measurement[i + 3])):
        count = count + 1
print(count)
