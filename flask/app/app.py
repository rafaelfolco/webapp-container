from flask import Flask, render_template, json, request
import mysql.connector

app = Flask(__name__)

# mysql config
mysql_config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'db_poll'
}

def allPeople():
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tbl_people')
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    return data

@app.route('/')
def webForm():
    return render_template('webform.html', data=allPeople())

@app.route('/newPeople',methods=['POST','GET'])
def newPeople():
    connection = None
    try:
        input_name = request.form['Name']
        input_color = request.form['Color']
        input_pet = request.form['Pet']

        if input_name:
            connection = mysql.connector.connect(**mysql_config)
            cursor = connection.cursor()
            _sql = (
                "INSERT INTO db_poll.tbl_people (name, color, pet) "
                "VALUES (%s, %s, %s)"
            )
            cursor.execute(_sql, (input_name, input_color, input_pet))
            connection.commit()
            msg = "New record has been inserted."
        else:
            msg = "Name is required."

    except Exception as e:
        msg = "Error: " + str(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return render_template('webform.html', data=allPeople(), msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
