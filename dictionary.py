import sqlite3
import pandas as pd

conn = sqlite3.connect('puslapiui.db')
cur= conn.cursor()
cur.execute("""select * from picos_csv""")
pizzas = cur.fetchall()

conn = sqlite3.connect('puslapiui.db')
cur= conn.cursor()
cur.execute("""select * from komentarai""")
kom = cur.fetchall()

conn = sqlite3.connect('puslapiui.db')
cur= conn.cursor()
cur.execute("""select * from picos_csv""")
pizzasBrooklyn= pd.DataFrame(cur.fetchall())
pizzasBrooklyn = pizzasBrooklyn.set_index([0])
pizzasBrooklyn= pizzasBrooklyn.loc['BrooklynBrothers']
pizzasBrooklynBrothers = pizzasBrooklyn.values.tolist()


conn = sqlite3.connect('puslapiui.db')
cur= conn.cursor()
cur.execute("""select * from picos_csv""")
pizzasPica= pd.DataFrame(cur.fetchall())
pizzasPica = pizzasPica.set_index([0])
pizzasPica= pizzasPica.loc['PicaPica']
pizzasPicaPica = pizzasPica.values.tolist()


conn = sqlite3.connect('puslapiui.db')
cur= conn.cursor()
cur.execute("""select * from picos_csv""")
pizzasČil= pd.DataFrame(cur.fetchall())
pizzasČil = pizzasČil.set_index([0])
pizzasČil= pizzasČil.loc['Čilas']
pizzasČilas = pizzasČil.values.tolist()
