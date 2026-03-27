from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine, text

app = Flask(__name__)

engine = create_engine('sqlite:///.database/cyberwatch.db') #link to the cyberwatch database here

#route for index.html
@app.route('/')
def home():
    
    with engine.connect() as connection:
        query = text('SELECT * FROM vulnerabilities ORDER BY owasp_rank;')
        result = connection.execute(query).fetchall()

    return render_template('index.html', vulnerabilities=result)

@app.route('/incidents/<vul_id>')
def incident_page(vul_id):
    # TASK 1: Connect to the database
    with engine.connect() as database:
        query = text('SELECT * FROM incidents WHERE vul_id = {};'.format(vul_id))
        print(query)
        result = database.execute(query).fetchall()
    # TASK 2: Fetch the Vulnerability Name for the heading (JOIN or separate query)
        vulnamequery = text('SELECT vul_name FROM vulnerabilities WHERE id = {};'.format(vul_id))
        vulnameresult = database.execute(vulnamequery).fetchall()
    # TASK 3: Fetch all Incidents linked to this vul_id, return incidents list
    print(result)
    print(vul_id) #this is a print statement to help you understand what data is being returned
    return render_template('incidents.html', vulnerability = vulnameresult[0][0], message = "", incidents = result)

@app.route('/add-incident', methods=['GET'])
def show_form():
    return render_template('add-incident.html')

@app.route('/add-incident/', methods=['POST'])
def add_incident():
    print('hi stirling')
    inc_name = request.form['inc_name']
    inc_url = request.form['inc_url']
    inc_year = request.form['inc_year']
    vul_id = request.form['vul_id']
    
    with engine.connect() as connection:
        query = text("INSERT INTO incidents (inc_name, inc_url, inc_year, vul_id) VALUES ('{}', {}, '{}', {}, '{}');".format(inc_name, inc_url, inc_year, vul_id))
        connection.execute(query, {
            
        })
    connection.execute(text(insert_statement))
    connection.commit()
    
    return render_template('add-incident.html')


app.run(debug=True, reloader_type='stat', port=5000)