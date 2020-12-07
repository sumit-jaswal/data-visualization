import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv')

# Code to draw different figures for each plot.

# Figure 1 for College Rank vs Full Time Jobs
fig1, ax = plt.subplots(figsize = (10,5))
ax.set_title('College Rank vs Students getting Full Time Job')
ax.plot(data.Rank, data.Full_time)
ax.set_ylabel('Number of Students who got Full Time Job')
ax.set_xlabel('College Rank')

# Figure 2 for College Rank vs Part Time Jobs
fig2, ax = plt.subplots(figsize = (10,5))
ax.set_title('College Rank vs Students getting Part Time Job')
ax.plot(data.Rank, data.Part_time)
ax.set_ylabel('Number of Students who got Part Time Job')
ax.set_xlabel('College Rank')

# Figure 3 for College Rank vs Unemployment Rate
fig3, ax = plt.subplots(figsize = (10,5))
ax.set_title('College Rank vs Unemployment Rate')
ax.plot(data.Rank, data.Unemployment_rate)
ax.set_ylabel('Unemployment Rate among those college students')
ax.set_xlabel('College Rank')


plt.style.use('ggplot')

# Figure 4 for College Rank vs Jobs requiring a College Degree
fig4, ax = plt.subplots(figsize = (10,5))
ax.set_title("Jobs requiring a College Degree")
ax.bar(data.Rank, data.College_jobs)
ax.set_ylabel('Number of Jobs')
ax.set_xlabel('College Rank')
ax.legend(['College Jobs'])

# Figure 4 for College Rank vs Jobs not requiring a College Degree
fig5, ax = plt.subplots(figsize = (10,5))
ax.set_title("Jobs not requiring a College Degree")
ax.bar(data.Rank, data.Non_college_jobs)
ax.set_ylabel('Number of Jobs')
ax.set_xlabel('College Rank')
ax.legend(['Non College Jobs'])

plt.show()