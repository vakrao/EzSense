import matplotlib.pyplot as plt

plt.figure()

#plots w example data
x_series = [8,9,10,11,12,13]
y_series_1 = [34,37,39,35,34,37]
#y_series_2 = [x**3 for x in x_series]

#labels
plt.xlabel("Hours")
plt.ylabel("Temperature")
plt.title("Temperature Over 24H. Period")

#limits
plt.xlim(0,24)
plt.ylim(25,45)

plt.plot(x_series, y_series_1)
plt.plot(x_series, y_series_2)

#save as png
plt.savefig("graph_example.png")
