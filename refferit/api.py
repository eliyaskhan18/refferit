from __future__ import unicode_literals
import frappe
from frappe import _, throw, msgprint, utils
from datetime import datetime, timedelta
import datetime

def auto_points():
	reffer_point = frappe.db.sql(""" select * from `tabreferral`""", as_dict = 1)
	data = []
	for ref in reffer_point:
		key = ref.referre_to
		if len(data) != 0:
			for d in data:
				if key in [d['referre_to'] for d in data]:
					d.update({"referre_to":key ,"point": d['point']+1})
				else:
					data.append({"referre_to":key , "point": 1})
		else:
			data.append({"referre_to":key , "point": 1})
	f= open("/home/frappe/frappe-bench/apps/refferit/refferit/refferit/output.out","a+")
	f.write("data---------------------------"+str(data)+"\n")
	for d in data:
		f.write("d.referre_to---------------------------"+str(d['referre_to'])+"\n")
		frappe.db.set_value("Contact", d['referre_to'], "points", d['point'])
