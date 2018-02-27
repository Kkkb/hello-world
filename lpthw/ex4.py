# -- coding:utf-8 --
# 车辆的数目
cars = 100

# 车辆的空间
space_in_a_car = 4.0

# 驾驶员数目
drivers = 30

# 乘客数目
passengers = 90

# 未驾驶的车辆数目
cars_not_driven = cars - drivers

# 有人驾驶的车辆数目
cars_driven = drivers

# 车辆空间
carpool_capacity = cars_driven * space_in_a_car

# 每辆车的乘客数量
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."