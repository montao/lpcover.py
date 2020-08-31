from scipy.optimize import linprog
n=8
obj = [1] * n
lhs_ineq = [
	[-1, -1, 0, 0, 0, 0, 0, 0],
	[-1, 0, 0, -1, 0, 0, 0, 0],
	[0, -1, -1, 0, 0, 0, 0, 0],
	[0, -1, 0, 0, -1, 0, 0, 0],
	[0, 0, -1, -1, 0, 0, 0, 0],
	[0, 0, 0, -1, 0, 0, 0, -1],
	[0, 0, 0, -1, 0, 0, -1, 0],
	[0, 0, 0, 0, -1, -1, 0, 0],
	[0, 0, 0, 0, 0, -1, -1, 0],
	[0, 0, 0, 0, 0, -1, 0, -1]]
rhs_ineq = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
bnd = [(0, float("inf"))] * n
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, 
	bounds=bnd, method="revised simplex")
print(opt)

def solve():
  print("Solving...")
  print(opt)
