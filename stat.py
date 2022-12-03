import sys
import numpy as np
import pandas as pd
from scipy import stats

pd.options.display.float_format = "{:,.2f}".format

def print_exit(a):
	print(a)
	sys.exit(0)

def print_wc(df, name, ddof=0):
	print("---------------------------")
	print(name + "---------")
	ignore = (1, 2, 3, 4)
	w = (5, 7, 8, 9)
	c = (6, 10, 11, 12)
	colw = []
	colc = []
	for key in df.keys():
		if key.startswith(name + "_WC"):
			if int(key[-1]) in ignore and not key[-2].isdigit():
				continue
			if int(key[-1]) in w:
				colw.append(key)
			if int(key[-1]) in c:
				colc.append(key)
			tmp = key[-2] + key[-1]
			if tmp.isdigit() and int(tmp) in c:
				colc.append(key)

	warmth = df[colw].to_numpy()
	comp = df[colc].to_numpy()
	print("%-18s %.2f" %("mean warmth", np.nanmean(warmth)))
	print("%-18s %.2f" %("mean competence", np.nanmean(comp)))
	print("%-18s %.2f" %("std warmth", np.nanstd(warmth, ddof=ddof)))
	print("%-18s %.2f" %("std competence", np.nanstd(comp, ddof=ddof)))
	

def print_res(df, name, ddof=0):
	print("---------------------------")
	print(name + "---------")
	des_cols = []
	fears_cols = []
	for key in df.keys():
		if key.startswith(name + "_DESIRES"):
			des_cols.append(key)
		if key.startswith(name + "_FEARS"):
			fears_cols.append(key)

	des = df[des_cols].to_numpy()
	fears = df[fears_cols].to_numpy()
	both = np.append(des, fears)
	print(df[des_cols].mean())
	print(df[des_cols].std(ddof=ddof))
	print((df[fears_cols]).mean())
	print((df[fears_cols]).std(ddof=ddof))
	print("%-18s %.2f" %("mean desires", np.nanmean(des)))
	print("%-18s %.2f" %("mean fears", np.nanmean(fears)))
	print("%-18s %.2f" %("mean both", np.nanmean(both)))
	print("%-18s %.2f" %("std desires", np.nanstd(des, ddof=ddof)))
	print("%-18s %.2f" %("std fears", np.nanstd(fears, ddof=ddof)))
	print("%-18s %.2f" %("std both", np.nanstd(both, ddof=ddof)))
	print("Amount considered:", len(df[name + "_DESIRES_1"]) - df[name + "_DESIRES_1"].isna().sum())

def print_results(df, ddof=0):
	r1, r2, r3 = (df["ROT_FUNC1"], df["ROT_FUNC2"], df["ROT_FUNC3"])
	p1, p2, p3 = (df["PROT_FUNC1"], df["PROT_FUNC2"], df["PROT_FUNC3"])
	c1, c2, c3 = (df["CONN_FUNC1"], df["CONN_FUNC2"], df["CONN_FUNC3"])
	
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
	print_res(df, "ROT", ddof)
	print_res(df, "PROT", ddof)
	print_res(df, "CONN", ddof)

	print()
	print("printing all desire anovas...")
	for i in range(1, 9):
		rot = df["ROT" + "_DESIRES_" + str(i)].dropna()
		prot = df["PROT" + "_DESIRES_" + str(i)].dropna()
		conn = df["CONN" + "_DESIRES_" + str(i)].dropna()
		deg = len(rot) + len(prot) + len(conn) - 3
		res = stats.f_oneway(rot, prot, conn)
		print("F(2, %d) = %.3f, p = %.3f" % (deg, res[0], res[1]))
		res = stats.f_oneway(rot, conn)
		print("   (rot, conn) = %.3f, p = %.3f" % (res[0], res[1]))
		res = stats.f_oneway(conn, prot)
		print("   (prot, conn) = %.3f, p = %.3f" % (res[0], res[1]))
		res = stats.f_oneway(rot, prot)
		print("   (prot, rot) = %.3f, p = %.3f" % (res[0], res[1]))
	print()
	print("printing all fear anovas...")
	for i in range(1, 7):
		if 5 == i:
			key = "_FEARS_" + "DANGER"
		else:
			key = "_FEARS_" + str(i)
			
		rot = df["ROT" + key].dropna()
		prot = df["PROT" + key].dropna()
		conn = df["CONN" + key].dropna()
		deg = len(rot) + len(prot) + len(conn) - 3
		res = stats.f_oneway(rot, prot, conn)
		print("F(2, %d) = %.3f, p = %.3f" % (deg, res[0], res[1]))
		res = stats.f_oneway(rot, conn)
		print("   (rot, conn) = %.3f, p = %.3f" % (res[0], res[1]))
		res = stats.f_oneway(conn, prot)
		print("   (prot, conn) = %.3f, p = %.3f" % (res[0], res[1]))
		res = stats.f_oneway(rot, prot)
		print("   (prot, rot) = %.3f, p = %.3f" % (res[0], res[1]))

	print()
	print("printing all the warmth and c's...")
	print_wc(df, "ROT", ddof)
	print_wc(df, "PROT", ddof)
	print_wc(df, "CONN", ddof)

if "__main__" == __name__:
	df = pd.read_excel("SOCIAL IMPACT QUESTIONNAIRE - manip.xlsx",
	sheet_name="python_data",
	index_col=0)
	#print(df)
	print_results(df)
	df = df.drop([83, 88, 89, 90, 91, 92, 93, 94])
	print("---------------------------")
	print("above is jill's, below is update database")
	print("---------------------------")
	print_results(df, ddof=1)
