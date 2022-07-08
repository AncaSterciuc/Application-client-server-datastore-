from flask import Flask, render_template, jsonify, request, redirect
import cx_Oracle
from datetime import datetime 

app = Flask(__name__)

con = cx_Oracle.connect("anca", "12345", "localhost/xe")



@app.route('/rame_ochelari')
def dep():
	rame_ochelari = []
	
	cur = con.cursor()
	cur.execute('select * from rame_ochelari')
	for result in cur:
		rame = {}
		rame['id_rama'] = result[0]
		rame['nume_rama'] = result[1]
		rame['pret_rama'] =result[2]
		rame['firma rama'] = result[3]
		
		rame_ochelari.append(rame)
	cur.close()

	return render_template('rame_ochelari.html',rame_ochelari=rame_ochelari)


@app.route('/addRama', methods=['POST'])
def ad_rama():
	error = None
	if request.method == 'POST':
		cur = con.cursor()
		values = []
		values2 = []

		values.append("'" + request.form['id_rama'] + "'")
		values.append("'" + request.form['nume_rama'] + "'")

		values.append("'" + request.form['pret_rama'] + "'")
		values.append("'" + request.form['firma rama'] + "'")

		query = 'INSERT INTO rame_ochelari VALUES (%s)' % (', '.join(values))
		cur.execute(query)

		cur.execute('commit')
		return redirect('/rame_ochelari')

@app.route('/delRame', methods=['POST'])
def del_rama():
	ram = request.form['id_rama']
	cur = con.cursor()

	cur.execute('delete from rame_ochelari where id_rama=:c', [ram])
	# cur.execute('delete from cumparator where nume_rama=:c' ,[ram])
	# cur.execute('delete from rame_ochelari where nume_rama=:c' ,[ram])


	cur.execute('commit')
	return redirect('/rame_ochelari')

@app.route('/dioptrii_ochelari')
def och():
	dioptrii_ochelari = []

	cur = con.cursor()
	cur.execute('select * from dioptrii_ochelari')
	for result in cur:
		dioptrii = {}
		dioptrii['id_dioptrii'] = result[0]
		dioptrii['cilindru_ochi_sg'] = result[1]
		dioptrii['cilindru_ochi_dr'] = result[2]
		dioptrii['sfera_ochi_sg'] = result[3]
		dioptrii['sfera_ochi_dr'] = result[4]
		dioptrii['AX_sg'] = result[5]
		dioptrii['AX_dr'] = result[6]

		dioptrii_ochelari.append(dioptrii)
	cur.close()

	return render_template('dioptrii_ochelari.html', dioptrii_ochelari=dioptrii_ochelari)

@app.route('/addDio', methods=['POST'])
def ad_dio():
	error = None
	if request.method == 'POST':
		cur = con.cursor()
		values = []
		values2 = []

		values.append("'" + request.form['id_dioptrii'] + "'")

		values2.append("'" + request.form['id_dioptrii'] + "'")

		values2.append("'" + request.form['cilindru_ochi_sg'] + "'")
		values2.append("'" + request.form['cilindru_ochi_dr'] + "'")

		values2.append("'" + request.form['sfera_ochi_sg'] + "'")
		values2.append("'" + request.form['sfera_ochi_dr'] + "'")

		values2.append("'" + request.form['AX_sg'] + "'")
		values2.append("'" + request.form['AX_dr'] + "'")


		query = 'INSERT INTO cumparator VALUES (%s)' % (', '.join(values))
		cur.execute(query)

		query = 'INSERT INTO dioptrii_ochelari VALUES (%s)' % (', '.join(values2))
		cur.execute(query)

		

		cur.execute('commit')
		return redirect('/dioptrii_ochelari')

@app.route('/delOch', methods=['POST'])
def del_och():

	dioptrii = "'" + request.form['id_dioptrii'] + "'"
	cur = con.cursor()
	cur.execute('delete from locations where id_dioptrii=' + dioptrii)
	cur.execute('commit')
	return redirect('/dioptrii_ochelari')
@app.route('/cumparator')
def cum():
	cumparator = []

	cur = con.cursor()
	cur.execute('select * from cumparator')
	for result in cur:
		cump = {}
		cump['id_cumparator'] = result[0]
		cump['rama'] = result[1]
		cump['dioptrii'] = result[2]

		cumparator.append(cump)
	cur.close()

	return render_template('cumparator.html', cumparator=cumparator)

@app.route('/delCumparator', methods=['POST'])
def del_cum():
	cu = request.form['id_cumparator']
	cur = con.cursor()
	cur.execute('delete from cumparator where id_cumparator=' + cu)
	cur.execute('commit')
	return redirect('/cumparator')

@app.route('/addCumparator', methods=['POST'])
def ad_cump():
	error = None
	if request.method == 'POST':
		cur = con.cursor()
		values = []
		values.append("'" + request.form['id_cumparator'] + "'")
		values.append("'" + request.form['rama'] + "'")
		values.append("'" + request.form['dioptrii'] + "'")
		query = 'INSERT INTO rame_ochelari VALUES (%s)' % (', '.join(values))
		cur.execute(query)
		cur.execute('commit')
		return redirect('/cumparator')

@app.route('/accesorii')
def acce():
	accesorii = []

	cur = con.cursor()
	cur.execute('select * from rame_ochelari')
	for result in cur:
		acc = {}
		acc['id_cumparator'] = result[0]
		acc['toc_pret'] = result[1]
		acc['laveta_pret'] = result[2]
		acc['solutie_curatare_pret'] = result[3]

		accesorii.append(acc)
	cur.close()

	return render_template('accesorii.html', accesorii=accesorii)

@app.route('/delAcc', methods=['POST'])
def del_acc():
	ac = request.form['id_cumparator']
	cur = con.cursor()
	cur.execute('delete from accesorii where id_cumparator=' + ac)
	cur.execute('commit')
	return redirect('/accesorii')

#main	
if __name__ == '__main__':
	app.run(debug=True)
	con.close()
