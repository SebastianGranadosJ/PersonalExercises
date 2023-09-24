def get_y(m, b, x):
  y = m*x + b
  return y

def calculate_error(m, b, point):
  x_point, y_point = point
  y = m*x_point + b
  distance = abs(y - y_point)
  return distance

def calculate_all_error(m, b, datapoints):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error

possible_ms = [m/10 for m in range(-100, 101)]
possible_bs = [b/10 for b in range(-200, 201)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
             best_m = m
             best_b = b
             smallest_error = error
       	 
print(best_m, best_b, smallest_error)