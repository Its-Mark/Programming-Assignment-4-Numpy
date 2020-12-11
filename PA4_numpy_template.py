import numpy as np

kobe = [[18, 7.6], [19, 15.4], [20, 19.9], [21, 22.5], [22, 28.5], [23, 25.2],
		[24, 30], [25, 24], [26, 27.6] , [27, 35.4], [28, 31.6], [29, 28.3],
		[30, 26.8], [31, 27], [32, 25.3], [33, 27.9], [34, 27.4], [35,13.8],
		[36, 22.3], [37, 17.6]]


# Part2: TODO- Make kobe into numpy array (kobe_np) and getting dimensions

kobe_np = np.array(kobe)
#print(kobe_np)
#print(type(kobe_np))
num_rows = 20
num_columns = 20



# Part3a: TODO- Make transpose of kobe_np (kobe_transpose)

kobe_transpose = kobe_np.T
#print(kobe_transpose)


# Part3b: TODO- Ones

ones = np.ones(num_rows)
#print(ones)


# Part3c: TODO- Getting value ([18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36. 37.])

#print(kobe_np[1])
#print(kobe_transpose[1])
#print(kobe_np[1, 0])
#print(kobe_transpose[1, 0])
A = kobe_transpose[0]
Y = kobe_transpose[1]
#print(A)
#print(Y)


# Part3d: TODO- Use column_stack

X = np.column_stack((A, ones))
#print(X)


# Part3e: TODO- Use matrix multiplication

X_prod = np.matmul(X.T, X)
#print(X_prod)
#print(X_prod.shape)



# Part3f: TODO- Find inverse

X_prod_inv = np.linalg.inv(X_prod)
#print(X_prod_inv)


# Part 4:

xTy = np.matmul(X.T, Y)

theta = np.matmul(X_prod_inv, xTy)

print("X_prod_inv: \n " + str(X_prod_inv))
print("theta0: \n" + str(theta[0]))
print("theta1: \n" + str(theta[1]))

exit()







