from scipy.optimize import linprog
obj = [1, 1, 1, 1, 1, 1, 1, 1]
lhs_ineq = [
	[ -1, -1, 0, 0, 0, 0, 0, 0],
	[ -1, 0, 0, -1, 0, 0, 0, 0],
	[ 0, -1, -1, 0, 0, 0, 0, 0],
	[ 0, -1, 0, 0, -1, 0, 0, 0],
	[ 0, 0, -1, -1, 0, 0, 0, 0],
	[ 0, 0, 0, -1, 0, 0, 0, -1],
	[ 0, 0, 0, -1, 0, 0, -1, 0],
	[ 0, 0, 0, 0, -1, -1, 0, 0],
	[ 0, 0, 0, 0, 0, -1, -1, 0],
	[ 0, 0, 0, 0, 0, -1, 0, -1]]
rhs_ineq = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
bnd = [
	(0, float("inf")),
	(0, float("inf")),
	(0, float("inf")),
	(0, float("inf")),
	(0, float("inf")),
	(0, float("inf")),
	(0, float("inf")),
	(0, float("inf"))] 
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, 
	bounds=bnd, method="revised simplex")
print(opt)

def solve():
  print("Solving...")
  print(opt)
