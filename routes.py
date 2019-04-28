from flask import Flask, render_template, request, redirect, url_for
from models import Member, Interests, WorkedOn
from dataLayer import Data
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonista'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):

        newMember = Member(request.form['name'], request.form['email'], request.form['occupation'], request.form['projects'], request.form['years'], request.form['commitment'])
        interests = request.form['areasofinterest']
        workedOn = request.form['areasworkedon']

        # newMember.prev_projects = 0
        # if(newMember.prev_projects == 'True'): newMember.prev_projects = 1

        conn = mysql.connection
        membersInsertedCount = Data.insert(newMember, conn)

        pid = int(Data.getId(conn))
        print(pid, type(pid))

        listOfInterests = Interests.splitInterests(pid, interests)
        interestsInsertedCount = Data.insertInterests(listOfInterests, conn)

        listOfWorkedOn = WorkedOn.splitWorks(pid, workedOn)
        workedOnInsertedCount = Data.insertWorkedOn(listOfWorkedOn, conn)

        mysql.connection.commit()

        if(membersInsertedCount > 0 and interestsInsertedCount > 0 and workedOnInsertedCount > 0):
            print(membersInsertedCount,"Rows successfully inserted!")
            return redirect(url_for('success', count = membersInsertedCount))

    return render_template('index.html')

#@app.route('/formteams/<int:noOfMembers>/<int:noOfTeams>/<int:noOfArchitects>/<int:noOfExperienced>', methods=['GET', 'POST'])
@app.route('/formteams/', methods=['GET', 'POST'])
def formteams():
    if request.method == 'POST':
        return 'Teams successfully added!'
    conn = mysql.connection
    noOfMembers = Data.getMembers(conn)
    if noOfMembers % 5 > 0: noOfTeams = noOfMembers // 5 + 1
    else: noOfTeams = noOfMembers // 5
    noOfArchitects = Data.getArchitects(conn)
    noOfExperienced = Data.getExperienced(conn)
    return render_template('formteams.html', noOfMembers=noOfMembers, noOfTeams=noOfTeams, noOfArchitects=noOfArchitects, noOfExperienced=noOfExperienced)

@app.route('/success/<int:count>')
def success(count):
    return render_template('success.html', count=count)

if __name__ == '__main__':
	app.run(debug='on')
