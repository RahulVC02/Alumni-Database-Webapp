from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import MySQLdb.cursors

app = Flask(__name__)

db = yaml.load(open('credentials.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


@app.route('/', methods=['POST'])
def home_post():
    # Fetch form data
    # userDetails = request.form
    # name = userDetails['name']
    # email = userDetails['email']
    # cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
    # mysql.connection.commit()
    # cur.close()


    return redirect('/tables')
    

@app.route('/', methods =['GET'])
def index():
    return render_template('index.html')


@app.route('/tables', methods =['GET'])
def tables():
    cursor = mysql.connection.cursor()
    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()
    cursor.close()
    table_names=[]

    for i in range(len(tables)):
        row =[]
        row.append(i+1)
        row.append(tables[i][0])
        table_names.append(row)
    
    return render_template('display_tables.html',table_data=table_names)



@app.route('/tables', methods =['POST'])
def tables_post():
    x = request.form

    button_pressed=None
    table_name = x['tableName']
    
    if(x.get('entries')==None):
        button_pressed='schema'
    else:
        button_pressed='entries'
       
    table_name_string = str(table_name)
    table_name_string = table_name_string.encode('utf-8').decode('utf-8')
    table_name_string = str(table_name_string)



    
    if(button_pressed=='entries'):

        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM {table_name_string}")
        mysql.connection.commit()
        table_data = cur.fetchall()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=%s and TABLE_NAME=%s", ("alumni", table_name_string,))
        table_column_names_tuples = cursor.fetchall()
        TABLE_COLUMN_NAMES =[]

        for dict in table_column_names_tuples:
            x = dict['COLUMN_NAME']
            TABLE_COLUMN_NAMES.append(x)
        
        cur.close()

        return render_template('display_entries.html', userDetails=table_data, table_name=table_name_string, table_col_names=TABLE_COLUMN_NAMES, EntriesOrSchema="Entries")
        
    else:

        cur = mysql.connection.cursor()
        cur.execute(f"SHOW COLUMNS FROM {table_name_string}")
        mysql.connection.commit()
        table_data = cur.fetchall()
        TABLE_COLUMN_NAMES = ["Field","Type","Null","Key","Default","Extra"]
        cur.close()

        return render_template('display_entries.html', userDetails=table_data, table_col_names=TABLE_COLUMN_NAMES, table_name=table_name_string, EntriesOrSchema="Schema")


if __name__ == '__main__':
    app.run(debug=True, port=4999)