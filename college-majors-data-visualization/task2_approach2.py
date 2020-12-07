import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv')


# Code to draw multiple plots in the same figure, 3 plots are drawn in 1 figure
fig1, (ax1, ax2, ax3) = plt.subplots(figsize = (13,6), ncols=3, constrained_layout=True)
ax1.set_title('College Rank vs Students getting Full Time Job')
ax1.plot(data.Rank, data.Full_time)
ax1.set_ylabel('Number of Students who got Full Time Job')
ax1.set_xlabel('College Rank')

ax2.set_title('College Rank vs Students getting Part Time Job')
ax2.plot(data.Rank, data.Part_time)
ax2.set_ylabel('Number of Students who got Part Time Job')
ax2.set_xlabel('College Rank')

ax3.set_title('College Rank vs Unemployment Rate')
ax3.plot(data.Rank, data.Unemployment_rate)
ax3.set_ylabel('Unemployment Rate among those college students')
ax3.set_xlabel('College Rank')

plt.style.use('ggplot')
# Code to draw multiple plots in the same figure, 2 plots are drawn in 1 figure
fig2, (ax4, ax5) = plt.subplots(figsize = (10,5), nrows = 2, constrained_layout=True)
ax4.set_title("Jobs requiring a College Degree")
ax4.bar(data.Rank, data.College_jobs)
ax4.set_ylabel('Number of Jobs')
ax4.set_xlabel('College Rank')
ax4.legend(['College Jobs'])

ax5.set_title("Jobs not requiring a College Degree")
ax5.bar(data.Rank, data.Non_college_jobs)
ax5.set_ylabel('Number of Jobs')
ax5.set_xlabel('College Rank')
ax5.legend(['Non College Jobs'])

plt.show()