#! /usr/bin/env python
import matplotlib.pyplot as plt
from genHumTrajectory import genHumTrajectory, human_start_index, gibbs_sampled_trajectory
from a_star import a_star,indexToWorld
from oneDtotwoD import oneDtotwoD


trajectory_1 = gibbs_sampled_trajectory(no_smaples=10, epoch_length=10)

x_trajectories = []
y_trajectories = []
for i in range(len(trajectory_1)):
    x_gibbs, y_gibbs = oneDtotwoD(trajectory_1[i])
    x_trajectories.append(x_gibbs)
    y_trajectories.append(y_gibbs)


for i in range(len(trajectory_1)):
    plt.plot(x_trajectories[i], y_trajectories[i],linewidth=2)
plt.plot(x_trajectories[0][0], y_trajectories[0][0],'o',linewidth=5 )
plt.title("Gibbs-Sampled Trajectories, #samples =10, epoch_length =10")
plt.show()

'''##2
trajectory_2 = gibbs_sampled_trajectory(no_smaples=5, epoch_length=10)

x_trajectories = []
y_trajectories = []
for i in range(len(trajectory_2)):
    x_gibbs, y_gibbs = oneDtotwoD(trajectory_1[i])
    x_trajectories.append(x_gibbs)
    y_trajectories.append(y_gibbs)


for i in range(len(trajectory_2)):
    plt.plot(x_trajectories[i], y_trajectories[i],linewidth=2)
plt.plot(x_trajectories[0][0], y_trajectories[0][0],'o',linewidth=3 )
plt.title("Gibbs-Sampled Trajectories, #samples =5, epoch_length =10")
plt.show()

##3
trajectory_3 = gibbs_sampled_trajectory(no_smaples=10, epoch_length=5)

x_trajectories = []
y_trajectories = []
for i in range(len(trajectory_1)):
    x_gibbs, y_gibbs = oneDtotwoD(trajectory_3[i])
    x_trajectories.append(x_gibbs)
    y_trajectories.append(y_gibbs)


for i in range(len(trajectory_3)):
    plt.plot(x_trajectories[i], y_trajectories[i], linewidth=2)
plt.plot(x_trajectories[0][0], y_trajectories[0][0],'o',linewidth=3 )
plt.title("Gibbs-Sampled Trajectories, #samples =10, epoch_length =5")
plt.show()

##4
trajectory_4 = gibbs_sampled_trajectory(no_smaples=10, epoch_length=10)

x_trajectories = []
y_trajectories = []
for i in range(len(trajectory_4)):
    x_gibbs, y_gibbs = oneDtotwoD(trajectory_4[i])
    x_trajectories.append(x_gibbs)
    y_trajectories.append(y_gibbs)


for i in range(len(trajectory_4)):
    plt.plot(x_trajectories[i], y_trajectories[i],linewidth=2)
plt.plot(x_trajectories[0][0], y_trajectories[0][0],'o',linewidth=3 )
plt.title("Gibbs-Sampled Trajectories, #samples =10, epoch_length =10")
plt.show()'''