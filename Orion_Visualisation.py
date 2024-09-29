import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

plt.figure(figsize=(6, 8))
plt.subplot(1, 1, 1)
plt.scatter(x, y)
plt.title('Orion constellation 2D projection')
# plt.savefig('/Users/olly/PycharmProjects/Constellation_Orion_Visualisation/2D_Orion.png')
# plt.show()
plt.clf()

plt.figure(figsize=(8, 10))
plt.subplot(projection="3d")
plt.scatter(x, y, z)
plt.title('Orion constellation 3D projection')
# plt.savefig('/Users/olly/PycharmProjects/Constellation_Orion_Visualisation/3D_Orion.png')
# plt.show()
plt.clf()