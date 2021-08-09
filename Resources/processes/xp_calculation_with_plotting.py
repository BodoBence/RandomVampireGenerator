
import matplotlib.pyplot as plt

ages = []
values = []

def live_calculation():
    for age in range(3001):

        max_age=3000
        xp_points = 0
        yearly_xp_base = 2
        min_xp = 300

        for i in range(age):
            yearly_xp = yearly_xp_base - (yearly_xp_base * (i / max_age))
            xp_points = xp_points + yearly_xp
            
        xp_points = max(min_xp, xp_points)

        ages.append(age)
        values.append(xp_points)

def calculation_1():
    for age in range(3001):
        
        max_age=3000
        xp_points = 0
        yearly_xp_base = 1
        start_xp = 400

        for i in range(age):
            yearly_xp = (yearly_xp_base - (yearly_xp_base * (i / max_age)))*0.8
            xp_points = xp_points + yearly_xp
            
        xp_points = start_xp + xp_points

        ages.append(age)
        values.append(xp_points)

# live_calculation()

calculation_1()

plt.plot(ages, values)
plt.ylabel('XP points')
plt.xlabel('Age')
plt.show()



