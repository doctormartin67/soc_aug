import sys
import numpy as np
import pandas as pd
from scipy import stats

def print_results(df, ddof=0):
	r1, r2, r3 = (df["ROT_FUNC1"], df["ROT_FUNC2"], df["ROT_FUNC3"])
	p1, p2, p3 = (df["PROT_FUNC1"], df["PROT_FUNC2"], df["PROT_FUNC3"])
	c1, c2, c3 = (df["CONN_FUNC1"], df["CONN_FUNC2"], df["CONN_FUNC3"])
	
	rot_des_cols = []
	rot_fears_cols = []
	prot_des_cols = []
	prot_fears_cols = []
	conn_des_cols = []
	conn_fears_cols = []
	for key in df.keys():
		if "PROT_DESIRES" in key:
			prot_des_cols.append(key)
		elif "ROT_DESIRES" in key:
			rot_des_cols.append(key)
		if "CONN_DESIRES" in key:
			conn_des_cols.append(key)
		if "PROT_FEARS" in key:
			prot_fears_cols.append(key)
		elif "ROT_FEARS" in key:
			rot_fears_cols.append(key)
		if "CONN_FEARS" in key:
			conn_fears_cols.append(key)

	func1 = stats.kruskal(r1, p1, c1, nan_policy="omit")
	func2 = stats.kruskal(r2, p2, c2, nan_policy="omit")
	func3 = stats.kruskal(r3, p3, c3, nan_policy="omit")

	if ddof == 0:
		assert(round(func1.statistic, 2) == 36.04)
		assert(round(func2.statistic, 2) == 14.05)
		assert(round(func3.statistic, 2) == 0.56)

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

	print()
	print("function 1:")
	print("prot and conn:")
	print(func1_no_rot)
	print("rot and conn:")
	print(func1_no_prot)
	print("rot and prot:")
	print(func1_no_conn)

	print()
	print("function 2:")
	print("prot and conn:")
	print(func2_no_rot)
	print("rot and conn:")
	print(func2_no_prot)
	print("rot and prot:")
	print(func2_no_conn)

	print()
	print("function 3:")
	print("prot and conn:")
	print(func3_no_rot)
	print("rot and conn:")
	print(func3_no_prot)
	print("rot and prot:")
	print(func3_no_conn)

	print()
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
	rot_des = df[rot_des_cols].to_numpy()
	rot_fears = df[rot_fears_cols].to_numpy()
	rot = np.append(rot_des, rot_fears)
	print(df[rot_des_cols].std(ddof=ddof))
	print(df[prot_des_cols].std(ddof=ddof))
	print(df[conn_des_cols].std(ddof=ddof))
	print("rot desires", np.nanmean(rot_des))
	print("rot fears", np.nanmean(rot_fears))
	print("rot", np.nanmean(rot))
	print("rot std", np.nanstd(rot, ddof=ddof))
	print(len(df["ROT_DESIRES_1"]) - df["ROT_DESIRES_1"].isna().sum())
	prot_des = df[prot_des_cols].to_numpy()
	prot_fears = df[prot_fears_cols].to_numpy()
	prot = np.append(prot_des, prot_fears)
	print("prot desires", np.nanmean(prot_des))
	print("prot fears", np.nanmean(prot_fears))
	print("prot", np.nanmean(prot))
	print("prot std", np.nanstd(prot, ddof=ddof))
	conn_des = df[conn_des_cols].to_numpy()
	conn_fears = df[conn_fears_cols].to_numpy()
	conn = np.append(conn_des, conn_fears)
	print("conn desires", np.nanmean(conn_des))
	print("conn fears", np.nanmean(conn_fears))
	print("conn", np.nanmean(conn))
	print("conn std", np.nanstd(conn, ddof=ddof))

if "__main__" == __name__:
	df = pd.read_excel("SOCIAL IMPACT QUESTIONNAIRE - manip.xlsx",
	sheet_name="python_data",
	index_col=0)
	print(df)
	print_results(df)
	df = df.drop([83, 88, 89, 90, 91, 92, 93, 94])
	print("---------------------------")
	print("above is jill's, below is update database")
	print("---------------------------")
	print_results(df, ddof=1)
