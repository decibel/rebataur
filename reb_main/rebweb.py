import sqlite3
from bottle import route, run, debug, template, request,redirect, static_file, error
from os.path import expanduser

from reb_main.pg_srv import PGService

home = expanduser("~")
sqlite_loc = home + "/rebconfig.db"


@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root="./static")
	

@route('/')
def config():
    initialize()
    r = {"one":1,"two":2}
    return template('reb_config', val=r)


@route('/config')
def config():
  
    pg_config = get_pg_config()
    pg_con = ""
    try:   
    	pg = PGService(pg_config[0][1],pg_config[1][1],pg_config[2][1],pg_config[3][1],pg_config[4][1])
	pg.execute_dml("select 1")
	pg_con = "success"
    except:
	pg_con = "failed"
	

    result = {"pg_con":pg_con}
    return template('reb_config', val=result)


@route('/wizard')
def wizard():
    r = {"one":1,"two":2}
    return template('reb_wizard', val=r)


@route('/analytics')
def analytics():
    r = {"one":1,"two":2}
    return template('reb_analytics', val=r)

@route("/submit_config/<path:path>",method="POST")
def submit_config(path):
	if path == "pg":
		pgprops = ["pgserver","pgport","pgdb","pguser","pgpwd"]
	
		conn = sqlite3.connect(sqlite_loc)
		c = conn.cursor()
		sql = """ delete from config where name = 'pg' """
		c.execute(sql)
		conn.commit	
		for i in pgprops:
			sql = """insert into config(name,key,value) values('pg','%s','%s') """ %(i,request.forms.get(i)) 
			c.execute(sql)
		conn.commit()	
		rows = c.execute("select value from config").fetchall()
		c.close()
		redirect("/config")
		

def initialize():
	conn = sqlite3.connect(sqlite_loc)
	c = conn.cursor()
	c.execute(""" create table if not exists config(name varchar,key varchar,value varchar) """)
	conn.commit()
	c.close()
def get_pg_config():
	conn = sqlite3.connect(sqlite_loc)
	c = conn.cursor()
	rows = c.execute("select key,value from config where name='pg'").fetchall()
	conn.commit()
	c.close()
	
	return rows

	
run(host='localhost', port=8080,debug=True, reloader=True)	
