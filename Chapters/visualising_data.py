from matplotlib import pyplot as plt
from collections import Counter
import random

iran_gdp = [109591,	126878,	128626,	153544,	190043,	226452,	266298,	349881,	412336,	416397,
            486807,	62613,	644035,	492775,	460382,	408212,	457954,	486630,	329691,	283649,
            239735,	359096,	413394,	401504]
year = [year for year in range(2000, 2024)]

plt.plot(year, iran_gdp, color = "green", marker = "o", linestyle = "solid")
plt.title("Iran GDP")
plt.ylabel("millions of $")
plt.show()

# Bar Charts
movies = ["Annie hall", "Ben-Hur", "Casablanca", "Gandhi", "West side story"]
num_oscars = [5, 11, 3, 8, 10]
plt.bar(range(len(movies)), num_oscars)
plt.title("My Favorite Movies")
plt.ylabel("number of academy awards")
plt.xticks(range(len(movies)), movies)
plt.show()

grades = random.sample(range(0,101), 30)
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
plt.bar([x + 5 for x in histogram.keys()],
        histogram.values(), width = 10, edgecolor = (0, 0, 0))
plt.axis([-5, 105, 0, 10])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("number of students")
plt.title("Distribution of grades")
plt.show()


# Line charts
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label = "variance")
plt.plot(xs, bias_squared, 'r-', label = "bias^2")
plt.plot(xs, total_error, 'b-', label = "total error")
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The bias variance trade-off")
plt.show()

# Scatterplots
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, xy = (friend_count, minute_count), xytext = (5, -5),
                 textcoords = 'offset points')
plt.title("Daily minutes Vs. Number of friends")
plt.xlabel("number of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()
