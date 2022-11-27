import pandas as pd
from scipy import stats

def print_results(df, ddof=0):
	r1, r2, r3 = (df["ROT_FUNC1"], df["ROT_FUNC2"], df["ROT_FUNC3"])
	p1, p2, p3 = (df["PROT_FUNC1"], df["PROT_FUNC2"], df["PROT_FUNC3"])
	c1, c2, c3 = (df["CONN_FUNC1"], df["CONN_FUNC2"], df["CONN_FUNC3"])
	func1 = stats.kruskal(r1, p1, c1, nan_policy="omit")
	func2 = stats.kruskal(r2, p2, c2, nan_policy="omit")
	func3 = stats.kruskal(r3, p3, c3, nan_policy="omit")

	func1_no_rot = stats.kruskal(p1, c1, nan_policy="omit")
	func1_no_prot = stats.kruskal(r1, c1, nan_policy="omit")
	func1_no_conn = stats.kruskal(r1, p1, nan_policy="omit")
	func2_no_rot = stats.kruskal(p2, c2, nan_policy="omit")
	func2_no_prot = stats.kruskal(r2, c2, nan_policy="omit")
	func2_no_conn = stats.kruskal(r2, p2, nan_policy="omit")
	func3_no_rot = stats.kruskal(p3, c3, nan_policy="omit")
	func3_no_prot = stats.kruskal(r3, c3, nan_policy="omit")
	func3_no_conn = stats.kruskal(r3, p3, nan_policy="omit")

	print("all 3:")
	print(func1, func2, func3, sep="\n")

	print("function 1:")
	print("prot and conn:")
	print(func1_no_rot)
	print("rot and conn:")
	print(func1_no_prot)
	print("rot and prot:")
	print(func1_no_conn)

	print("function 2:")
	print("prot and conn:")
	print(func2_no_rot)
	print("rot and conn:")
	print(func2_no_prot)
	print("rot and prot:")
	print(func2_no_conn)

	print("function 3:")
	print("prot and conn:")
	print(func3_no_rot)
	print("rot and conn:")
	print(func3_no_prot)
	print("rot and prot:")
	print(func3_no_conn)

	print("rotator means %.2f, %.2f, %.2f" % (r1.mean(), r2.mean(), r3.mean()))
	print("rotator std %.2f, %.2f, %.2f" % (r1.std(ddof=ddof), r2.std(ddof=ddof),
	r3.std(ddof=ddof)))
	print("protector means %.2f, %.2f, %.2f" % (p1.mean(), p2.mean(), p3.mean()))
	print("protector std %.2f, %.2f, %.2f" % (p1.std(ddof=ddof), p2.std(ddof=ddof),
	p3.std(ddof=ddof)))
	print("connector means %.2f, %.2f, %.2f" % (c1.mean(), c2.mean(), c3.mean()))
	print("connector std %.2f, %.2f, %.2f" % (c1.std(ddof=ddof), c2.std(ddof=ddof),
	c3.std(ddof=ddof)))

	"""
	print(len(r1) - r1.isna().sum())
	print(len(r2) - r2.isna().sum())
	print(len(r3) - r3.isna().sum())
	print(len(p1) - p1.isna().sum())
	print(len(p2) - p2.isna().sum())
	print(len(p3) - p3.isna().sum())
	print(len(c1) - c1.isna().sum())
	print(len(c2) - c2.isna().sum())
	print(len(c3) - c3.isna().sum())
	"""

if "__main__" == __name__:
	df = pd.read_excel("SOCIAL IMPACT QUESTIONNAIRE - manip.xlsx", sheet_name=3,
	index_col=0)
	print(df)
	print_results(df)
	df = df.drop([83, 88, 89, 90, 91, 92, 93, 94])
	print("---------------------------")
	print("above is jill's, below is update database")
	print("---------------------------")
	print_results(df, ddof=1)
