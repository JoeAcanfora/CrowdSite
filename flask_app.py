import MySQLdb
import MySQLdb.cursors
from flask import Flask, request,  \
     render_template, flash, url_for, redirect
from flask_table import Table, Col
from flask.ext.wtf import Form
from wtforms import TextField, validators, RadioField, SubmitField

# A very simple Flask Hello World app for you to get started with...

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

class IdCol(Col):
    def td_format(self, content):
        return '<a href=project_page/'+ content +'>' + content + '</a>'

class GradeCol(Col):
    def td_format(self, content):
        series = str(content).split(':')[3] #TODO check
        grade_num = str(content).split(':')[2]
        graded = str(content).split(':')[1]
        videopressent = str(content).split(':')[0]
        if videopressent is '0':
            return 'N/A'
        if graded is '0':

            return '<a href=grade_project/' + grade_num + '/' + series + '> Grade Me </a>'
        else:
            return 'Done'


# Declare your table
class TopTable(Table):
    series_number = Col('Series')
    project_id = IdCol('Project_ID')
    project_name = Col('Project Name')
    graded1 = GradeCol('Graded1')
    graded2 = GradeCol('Graded2')

def connect_db():
    db = MySQLdb.connect(host="mysql.server", user="joeacanfora", passwd="password",db="joeacanfora$CrowdStore", cursorclass=MySQLdb.cursors.DictCursor, charset='utf8')
    return db

def rename(dictionary,old_key,new_key):

    dictionary[new_key] = dictionary.pop(old_key)

@app.route('/')
def homepage():
    try:
        db = connect_db()
        c = db.cursor()
        c.execute("""SELECT series_number, project_id, project_name,
        CONCAT(videopressent, ':', graded1, ':1:', series_number), CONCAT(videopressent, ':', graded2, ':2:', series_number) FROM project_table""")
        query = c.fetchall()
        for q in query:
            rename(q, str("CONCAT(videopressent, ':', graded1, ':1:', series_number)"), str('graded1'))
            rename(q, str("CONCAT(videopressent, ':', graded2, ':2:', series_number)"), str('graded2'))
        table = TopTable(query)

        return render_template("list.html", table = str(table.__html__()))
    except Exception, e:
        return str(e)

@app.route('/project_page/<int:proj_id>')
def project_info_page(proj_id):
    try:
        db = MySQLdb.connect(host="mysql.server", user="joeacanfora", passwd="password",db="joeacanfora$CrowdStore", charset='utf8')
        c = db.cursor()
        c.execute("""SELECT project_name from project_table WHERE project_id = %s""", (proj_id, ))
        name = c.fetchall()[0][0]
        c.execute("""SELECT series_number from project_table WHERE project_id = %s""", (proj_id, ))
        series_number = c.fetchall()[0][0]
        c.execute("""SELECT project_url from project_table WHERE project_id = %s""", (proj_id, ))
        project_url = c.fetchall()[0][0]
        c.execute("""SELECT status from project_table WHERE project_id = %s""", (proj_id, ))
        status = c.fetchall()[0][0]
        c.execute("""SELECT currency FROM project_table WHERE project_id = %s""", (proj_id, ))
        currency = c.fetchall()[0][0]
        c.execute("""SELECT goal FROM project_table WHERE project_id = %s""", (proj_id, ))
        goal = c.fetchall()[0][0]
        c.execute("""SELECT end_date FROM project_table WHERE project_id = %s""", (proj_id, ))
        end_date = c.fetchall()[0][0]
        c.execute("""SELECT author_name FROM project_table WHERE project_id = %s""", (proj_id, ))
        author = c.fetchall()[0][0]
        c.execute("""SELECT location FROM project_table WHERE project_id = %s""", (proj_id, ))
        location = c.fetchall()[0][0]
        c.execute("""SELECT category FROM project_table WHERE project_id = %s""", (proj_id, ))
        category = c.fetchall()[0][0]
        c.execute("""SELECT main_video_link FROM project_table WHERE project_id = %s""", (proj_id, ))
        video = c.fetchall()[0][0]
        #######
        c.execute("""SELECT grader1PID FROM project_table WHERE project_id = %s""", (proj_id, ))
        g1ID = c.fetchall()[0][0]
        c.execute("""SELECT videoquaility1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        vidqual1 = c.fetchall()[0][0]
        c.execute("""SELECT othcompreference1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        ocr1 = c.fetchall()[0][0]
        c.execute("""SELECT othcompname1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        ocn1 = c.fetchall()[0][0]
        c.execute("""SELECT pitchfocus1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pf1 = c.fetchall()[0][0]
        c.execute("""SELECT founderschool1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        fsr1 = c.fetchall()[0][0]
        c.execute("""SELECT founderschoolname1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        fsn1 = c.fetchall()[0][0]
        c.execute("""SELECT founderstartup1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        fsur1 = c.fetchall()[0][0]
        c.execute("""SELECT founderstartupname1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        fsun1 = c.fetchall()[0][0]
        c.execute("""SELECT prototypes1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        p1 = c.fetchall()[0][0]
        c.execute("""SELECT endorsements1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        e1 = c.fetchall()[0][0]
        c.execute("""SELECT endorsementname1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        en1 = c.fetchall()[0][0]
        ####
        c.execute("""SELECT grader2PID FROM project_table WHERE project_id = %s""", (proj_id, ))
        g2ID = c.fetchall()[0][0]
        c.execute("""SELECT videoquaility2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        vidqual2 = c.fetchall()[0][0]
        c.execute("""SELECT othcompreference2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        ocr2 = c.fetchall()[0][0]
        c.execute("""SELECT othcompname2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        ocn2 = c.fetchall()[0][0]
        c.execute("""SELECT pitchfocus2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pf2 = c.fetchall()[0][0]
        c.execute("""SELECT founderschool2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        fsr2 = c.fetchall()[0][0]
        c.execute("""SELECT founderschoolname2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        fsn2 = c.fetchall()[0][0]
        c.execute("""SELECT founderstartup2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        fsur2 = c.fetchall()[0][0]
        c.execute("""SELECT founderstartupname2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        fsun2 = c.fetchall()[0][0]
        c.execute("""SELECT prototypes2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        p2 = c.fetchall()[0][0]
        c.execute("""SELECT endorsements2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        e2 = c.fetchall()[0][0]
        c.execute("""SELECT endorsementname2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        en2 = c.fetchall()[0][0]


        return render_template("project.html", project_id = proj_id, project_name = name, series_number = series_number, project_url = project_url,
        status = status, currency = currency, goal = goal, end_date = end_date, author_name = author,
        location = location, category = category, main_video_link = video,
        grader1PID = g1ID, videoquaility1 = vidqual1, othcompreference1 = ocr1, othcompname1 = ocn1,
        pitchfocus1 = pf1, founderschool1 = fsr1, founderschoolname1 = fsn1, founderstartup1 = fsur1,
        founderstartupname1 = fsun1, prototypes1 = p1, endorsementname1 = en1, endorsements1 = e1,
        grader2PID = g2ID, videoquaility2 = vidqual2, othcompreference2 = ocr2, othcompname2 = ocn2,
        pitchfocus2 = pf2, founderschool2 = fsr2, founderschoolname2 = fsn2, founderstartup2 = fsur2,
        founderstartupname2 = fsun2, prototypes2 = p2, endorsementname2 = en2, endorsements2 = e2)
    except Exception, e:
        return str(e)

class GradeForm(Form):
    """edit user Profile EditForm"""
    graderPID = TextField('graderPID', [validators.Length(min=3, max=50), validators.Required()])
    videoquaility = RadioField('videoquaility', choices=[(1, '(1) poor quaility'), (2, '(2) below average'), (3, '(3) average quaility'),
        (4, '(4) above average quaility'), (5, '(5) high quaility')], validators=[validators.Required()])
    othcompreference = RadioField('othcompreference', choices = [(0, 'False'), (1, 'True')], validators=[validators.Required()])
    othcompname = TextField('othcompname', validators = [validators.Length(max=100)])
    pitchfocus = RadioField('pitchfocus', choices = [ (1, "founder's characteristics"), (2, 'customer needs'), (3, 'the technology'), (4, 'something else')],
        validators=[validators.Required()])
    founderschool = RadioField('founderschool', choices = [(0, 'False'), (1, 'True')], validators=[validators.Required()])
    founderschoolname = TextField('founderschoolname', validators = [validators.Length(max=100)])
    founderstartup = RadioField('founderstartup', choices = [(0, 'False'), (1, 'True')], validators=[validators.Required()])
    founderstartupname = TextField('founderstartupname', validators = [validators.Length(max=100)])
    prototype = RadioField('prototype', choices = [(0, 'False'), (1, 'True')], validators=[validators.Required()])
    endorsement = RadioField('endorsement', choices = [(0, 'False'), (1, 'True')], validators=[validators.Required()])
    endorsementname = TextField('endorsementname', validators = [validators.Length(max=100)])
    submitButton = SubmitField('Submit')

@app.route('/grade_project/<int:grade_num>/<int:series_num>',  methods=['GET', 'POST'])
def project_grade_page(grade_num, series_num):
    form = GradeForm(request.form, csrf_enabled = False)
    try:
        if request.method == 'POST':

            save_form_to_db(form, grade_num, series_num)
            return redirect('http://joeacanfora.pythonanywhere.com/')
        else:
            db = MySQLdb.connect(host="mysql.server", user="joeacanfora", passwd="password",db="joeacanfora$CrowdStore", charset='utf8')
            c = db.cursor()
            c.execute("""SELECT main_video_link from project_table WHERE series_number = %s""", (series_num, ))
            video = c.fetchall()
            video = video[0][0]
            return render_template("grade_project.html", video_link = video, form = form,
                url= 'https://www.pythonanywhere.com/user/joeacanfora/form_saved/' + str(grade_num) + '/' + str(series_num))
    except Exception, e:
        return str(e)

def save_form_to_db(form, grade_num, series_num):
    try:
        db = MySQLdb.connect(host="mysql.server", user="joeacanfora", passwd="password",db="joeacanfora$CrowdStore", charset='utf8')
        db.autocommit(True)
        c = db.cursor()
        graded = True
        args = (graded, form.graderPID.data, form.videoquaility.data, form.othcompreference.data,
                form.othcompname.data, form.pitchfocus.data, form.founderschool.data, form.founderschoolname.data, form.founderstartup.data,
                form.founderstartupname.data, form.prototype.data, form.endorsement.data, form.endorsementname.data, series_num)
        if grade_num == 1:

            c.execute('''UPDATE project_table SET graded1=%s, grader1PID=%s, videoquaility1=%s, othcompreference1=%s,
                othcompname1=%s, pitchfocus1=%s, founderschool1=%s, founderschoolname1=%s, founderstartup1=%s,
                founderstartupname1=%s, prototypes1=%s, endorsements1=%s, endorsementname1=%s
                WHERE series_number=%s''', args)
            c.connection.commit()
        elif grade_num == 2:
            c.execute('''UPDATE project_table SET graded2=%s, grader2PID=%s, videoquaility2=%s, othcompreference2=%s,
                    othcompname2=%s, pitchfocus2=%s, founderschool2=%s, founderschoolname2=%s, founderstartup2=%s,
                    founderstartupname2=%s, prototypes2=%s, endorsements2=%s, endorsementname2=%s
                    WHERE series_number=%s''',args)
            c.connection.commit()
        else:
            return 'Fail ' + str(grade_num)
        return str(c.fetchall())
    except Exception, e:
        return str(e)
