# Collect data about any university of your choice and the number of courses they run for Science,Technology and Humanities,
#  store it in a CSV file and present it using a bar plot.

#importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading the data from the csv file
data = pd.read_csv('data.csv')

#plotting the data using bar plot
plt.bar(data['university_name'], data['Science'], color='red')  # plotting science courses
plt.bar(data['university_name'], data['Technology'], color='green')  # plotting technology courses
plt.bar(data['university_name'], data['Humanities'], color='blue')  # plotting humanities courses
plt.legend(['Science', 'Technology', 'Humanities']);  # adding legend to the plot

#naming in Bold
plt.title('Number of courses for Science,Technology and Humanities', fontweight='bold')
#adding x-axis and y-axis labels in bold
plt.xlabel('Name of University', fontweight='bold')
plt.ylabel('Number of courses', fontweight='bold')
#adding a grid

plt.show()  # showing the plot


#printing the data
print(data)
