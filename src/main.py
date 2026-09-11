number_of_motors=int(input("How many motors are carrying the packages? "))
package_weight=int(input("How much does each package weigh in pounds? "))
weight_per_motor=package_weight/number_of_motors
if weight_per_motor<=12:
    print("Yes! The conveyor belt can carry the packages.")
else:
    print("No! The conveyor belt cannot carry the packages.")
