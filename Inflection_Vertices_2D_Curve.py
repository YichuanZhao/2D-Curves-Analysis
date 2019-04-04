import numpy as np

from scipy.misc import derivative

import math

import matplotlib.pyplot as plt


def getX(x):

	y = (math.cos(x) + (1.0 - 0.25*(math.sin(x))**(2.0))**(0.5) + (1 - (361.0/400.0)*(math.sin(x))**(2.0))**(0.5))*math.cos(x)

	return y

def getY(x):

	y = (math.cos(x) + (1.0 - 0.25*(math.sin(x))**(2.0))**(0.5) + (1 - (361.0/400.0)*(math.sin(x))**(2.0))**(0.5))*math.sin(x)

	return y

def getD(a, b):


	l = len(a)

	res = [0.0]*(l-1)

	for i in range(l-1):

		res[i] = (a[i] - a[i+1])/(b[i] - b[i+1])

	return res

def getK(a, b, c, d):

	l = len(b)

	res = [0.0]*l

	for i in range(l):
		
		t1 = a[i]*d[i] - b[i]*c[i]
		t2 = (a[i]**2 + c[i]**2)**(1.5)
		res[i] = t1/t2

	return res


def findIndex(a):

	res = []

	for i in range(len(a)):
		if math.fabs(a[i]) < 2e-3:
			res.append(i)

	return res


def findIndex_2(a):

	res = []

	for i in range(len(a)-1):
		if a[i]*a[i+1] < 0:
			res.append(i)

	return res

def getIndex_1(a, b):

	res = []
	for i in range(len(a)):

		if a[i] not in b:
			res.append(a[i])

	return res

def getIndex_2(a, b):

	res = []
	for i in range(len(b)-1):

		if b[i]*b[i+1] < 0:
			res.append(a[i])

	return res


def elIndex(a):

	res = []
	res.append(a[0])

	for i in range(len(a)-1):
		if a[i+1] - a[i] > 10:
			res.append(a[i+1])
	return res



index = np.arange(0,2*math.pi,1e-3)

xValue = [getX(v) for v in index]

yValue = [getY(v) for v in index]


x_1 = getD(xValue, index)

x_2 = getD(x_1, index)


y_1 = getD(yValue, index)

y_2 = getD(y_1, index)

K = getK(x_1, x_2, y_1, y_2)


K_1 = getD(K, index)

K_2 = getD(K_1, index) 

# ind_1 = findIndex(K)

# ind_2 = findIndex(K_1)

# ind_3 = findIndex(K_2)

in_1 = findIndex_2(K)

in_2 = findIndex_2(K_1)
# in_2 = getIndex_2(K_1, K_2)

# print(in_1)
# print(in_2)
fIndex_1 = elIndex(in_1)

fIndex_2 = elIndex(in_2)

flectionXValue = [xValue[v] for v in fIndex_1]

flectionYValue = [yValue[v] for v in fIndex_1]

flectionAngle = [index[v] for v in fIndex_1]

print("Inflection points are:")

for i in range(len(flectionXValue)):

	print "x: " + str(flectionXValue[i]) + ", y: " + str(flectionYValue[i]) + ", angle: " + str(flectionAngle[i]) + "\n"


verXValue = [xValue[v] for v in fIndex_2]

verYValue = [yValue[v] for v in fIndex_2]

verAngle = [index[v] for v in fIndex_2]

print("Vertex points are:")

for i in range(len(verXValue)):

	print "x: " + str(verXValue[i]) + ", y: " + str(verYValue[i]) + ", angle: " + str(verAngle[i]) + "\n"
# test = [xValue[v] for v in ind_2]
# print(test)


# plt.plot(index[0:6281],K_1)

# plt.show()
# v_1 = getD(value, index)

# v_2 = getD(v_1, index)

# K = getK(value, v_1, v_2)

# K_1 = getD(K, index)

# K_2 = getD(K_1, index) 

# ind_1 = findIndex(K)

# ind_2 = findIndex(K_1)

# ind_3 = findIndex(K_2)

# # getF((ind/len(index))*2*math.pi)

# # print(value[ind[4]])

# # print(value[ind[1]])

# # print(value[ind_1[1]])

# in_1 = getIndex(ind_1, ind_2)

# in_2 = getIndex(ind_2, ind_3)

# print(len(in_1))
# print(len(in_2))


# print(len(ind_2))

# print(len(ind_3))


# print(len(findIndex(K_1)))

# print(len(findIndex(K_2)))



# print(getF(0))

