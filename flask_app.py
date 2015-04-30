import pymysql
from flask import Flask, request,  \
     render_template, redirect
from flask_table import Table, Col
from flask.ext.wtf import Form
from wtforms import TextField, validators, RadioField, SubmitField, BooleanField

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

        db = connect_db()
        c = db.cursor()
        c.execute("""SELECT main_video_link from project_table WHERE series_number = %s""", (series, ))
        vidlink = c.fetchall()[0][0]

        # if videopressent is '0':
        series = series.replace("'", '')
        if vidlink is None:
            return 'N/A'
        if graded is '0':
            # series = series.replace("'", '')
            return '<a href=grade_project/' + grade_num + '/' + series + '> Grade Me </a>'
        else:
            return '<a href=grade_project/' + grade_num + '/' + series + '> Done</a>'


class ReGradeCol(Col):
    def td_format(self, content):
        series = str(content).split(':')[3] #TODO check
        grade_num = str(content).split(':')[2]
        graded = str(content).split(':')[1]

        db = connect_db()
        c = db.cursor()
        c.execute("""SELECT main_video_link from project_table WHERE series_number = %s""", (series, ))
        vidlink = c.fetchall()[0][0]

        # if videopressent is '0':
        series = series.replace("'", '')
        if int(series) < 53:
            if vidlink is None:
                return 'N/A'
            if graded is '0':
                return '<a href=regrade_project/' + grade_num + '/' + series + '> Regrade</a>'
            else:
                return '<a href=regrade_project/' + grade_num + '/' + series + '> Done</a>'
        else:
            return ''

class ReconcileCol(Col):
    def td_format(self, content):
        series = str(content).split(':')[3] #TODO check
        grade_num = str(content).split(':')[2]
        graded = str(content).split(':')[1]

        db = connect_db()
        c = db.cursor()
        c.execute("""SELECT main_video_link from project_table WHERE series_number = %s""", (series, ))
        vidlink = c.fetchall()[0][0]

        # if videopressent is '0':
        series = series.replace("'", '')
        series_num = series

        c.execute("""SELECT grader1PID FROM project_table WHERE series_number = %s""", (series_num, ))
        g1ID = c.fetchall()[0][0]
        c.execute("""SELECT videoquaility1 FROM project_table WHERE series_number = %s""", (series_num, ))
        vidqual1 = c.fetchall()[0][0]
        c.execute("""SELECT soldlevel1 FROM project_table WHERE series_number = %s""", (series_num, ))
        sl1 = c.fetchall()[0][0]
        c.execute("""SELECT othcompreference1 FROM project_table WHERE series_number = %s""", (series_num, ))
        ocr1 = c.fetchall()[0][0]
        c.execute("""SELECT othcompname1 FROM project_table WHERE series_number = %s""", (series_num, ))
        ocn1 = c.fetchall()[0][0]
        c.execute("""SELECT pitchFounder1 FROM project_table WHERE series_number = %s""", (series_num, ))
        pf1 = c.fetchall()[0][0]
        c.execute("""SELECT pitchTechnology1 FROM project_table WHERE series_number = %s""", (series_num, ))
        pt1 = c.fetchall()[0][0]
        c.execute("""SELECT pitchCustomer1 FROM project_table WHERE series_number = %s""", (series_num, ))
        pc1 = c.fetchall()[0][0]
        c.execute("""SELECT founderschool1 FROM project_table WHERE series_number = %s""", (series_num, ))
        fsr1 = c.fetchall()[0][0]
        c.execute("""SELECT founderschoolname1 FROM project_table WHERE series_number = %s""", (series_num, ))
        fsn1 = c.fetchall()[0][0]
        c.execute("""SELECT founderstartup1 FROM project_table WHERE series_number = %s""", (series_num, ))
        fsur1 = c.fetchall()[0][0]
        c.execute("""SELECT founderstartupname1 FROM project_table WHERE series_number = %s""", (series_num, ))
        fsun1 = c.fetchall()[0][0]
        c.execute("""SELECT prototypes1 FROM project_table WHERE series_number = %s""", (series_num, ))
        p1 = c.fetchall()[0][0]
        c.execute("""SELECT endorsements1 FROM project_table WHERE series_number = %s""", (series_num, ))
        e1 = c.fetchall()[0][0]
        c.execute("""SELECT endorsementname1 FROM project_table WHERE series_number = %s""", (series_num, ))
        en1 = c.fetchall()[0][0]
        c.execute("""SELECT music1 FROM project_table WHERE series_number = %s""", (series_num, ))
        m1 = c.fetchall()[0][0]
        c.execute("""SELECT animations1 FROM project_table WHERE series_number = %s""", (series_num, ))
        a1 = c.fetchall()[0][0]
        c.execute("""SELECT patent1 FROM project_table WHERE series_number = %s""", (series_num, ))
        pat1 = c.fetchall()[0][0]
        # c.execute("""SELECT logo1 FROM project_table WHERE series_number = %s""", (series_num, ))
        # logo1 = c.fetchall()[0][0]
        c.execute("""SELECT rewardsMentioned1 FROM project_table WHERE series_number = %s""", (series_num, ))
        rm1 = c.fetchall()[0][0]
        ####
        c.execute("""SELECT grader2PID FROM project_table WHERE series_number = %s""", (series_num, ))
        g2ID = c.fetchall()[0][0]
        c.execute("""SELECT videoquaility2 FROM project_table WHERE series_number = %s""", (series_num, ))
        vidqual2 = c.fetchall()[0][0]
        c.execute("""SELECT soldlevel2 FROM project_table WHERE series_number = %s""", (series_num, ))
        sl2 = c.fetchall()[0][0]
        c.execute("""SELECT othcompreference2 FROM project_table WHERE series_number = %s""", (series_num, ))
        ocr2 = c.fetchall()[0][0]
        c.execute("""SELECT othcompname2 FROM project_table WHERE series_number = %s""", (series_num, ))
        ocn2 = c.fetchall()[0][0]
        c.execute("""SELECT pitchFounder2 FROM project_table WHERE series_number = %s""", (series_num, ))
        pf2 = c.fetchall()[0][0]
        c.execute("""SELECT pitchTechnology2 FROM project_table WHERE series_number = %s""", (series_num, ))
        pt2 = c.fetchall()[0][0]
        c.execute("""SELECT pitchCustomer2 FROM project_table WHERE series_number = %s""", (series_num, ))
        pc2 = c.fetchall()[0][0]
        c.execute("""SELECT founderschool2 FROM project_table WHERE series_number = %s""", (series_num, ))
        fsr2 = c.fetchall()[0][0]
        c.execute("""SELECT founderschoolname2 FROM project_table WHERE series_number = %s""", (series_num, ))
        fsn2 = c.fetchall()[0][0]
        c.execute("""SELECT founderstartup2 FROM project_table WHERE series_number = %s""", (series_num, ))
        fsur2 = c.fetchall()[0][0]
        c.execute("""SELECT founderstartupname2 FROM project_table WHERE series_number = %s""", (series_num, ))
        fsun2 = c.fetchall()[0][0]
        c.execute("""SELECT prototypes2 FROM project_table WHERE series_number = %s""", (series_num, ))
        p2 = c.fetchall()[0][0]
        c.execute("""SELECT endorsements2 FROM project_table WHERE series_number = %s""", (series_num, ))
        e2 = c.fetchall()[0][0]
        c.execute("""SELECT endorsementname2 FROM project_table WHERE series_number = %s""", (series_num, ))
        en2 = c.fetchall()[0][0]
        c.execute("""SELECT music2 FROM project_table WHERE series_number = %s""", (series_num, ))
        m2 = c.fetchall()[0][0]
        c.execute("""SELECT animations2 FROM project_table WHERE series_number = %s""", (series_num, ))
        a2 = c.fetchall()[0][0]
        c.execute("""SELECT patent2 FROM project_table WHERE series_number = %s""", (series_num, ))
        pat2 = c.fetchall()[0][0]
        # c.execute("""SELECT logo2 FROM project_table WHERE series_number = %s""", (series_num, ))
        # logo2 = c.fetchall()[0][0]
        c.execute("""SELECT rewardsMentioned2 FROM project_table WHERE series_number = %s""", (series_num, ))
        rm2 = c.fetchall()[0][0]

        c.execute("""SELECT graded1 FROM project_table WHERE series_number = %s""", (series_num, ))
        graded1 = c.fetchall()[0][0]
        c.execute("""SELECT graded2 FROM project_table WHERE series_number = %s""", (series_num, ))
        graded2 = c.fetchall()[0][0]

        needs_reconcile = False

        if ((vidqual1 != vidqual2) or (sl1 != sl2) or (ocr1 != ocr2) or (ocn1 != ocn2)
        or (pf1 != pf2) or (pt1 != pt2) or (pc1 != pc2) or (fsr1 != fsr2)
        or (pc2 != pc2) or (fsn1 != fsn2) or (fsur1 != fsur2) or (fsun1 != fsun2) or
         (p1 != p2) or (en1 != en2) or (e1 != e2) or (m1 != m2) or (a1 != a2) or (pat1 != pat2)
        or ( rm1 != rm2)):
            needs_reconcile = True

        if (graded1 != graded2):
            needs_reconcile = False

        if ((vidlink is None) or (not needs_reconcile)):
            return 'N/A'
        if graded is '0':
            return '<a href=reconcile_project/' + grade_num + '/' + series + '> Reconcile</a>'
        else:
            return '<a href=reconcile_project/' + grade_num + '/' + series + '> Done</a>'


class SeriesCol(Col):
    def td_format(self, content):
        if int(content) > 1346:
            return str(int(content) - 1346 + 53)
        else:
            return content

# Declare your table
class TopTable(Table):
    series_number = SeriesCol('Series')
    project_id = IdCol('Project_ID')
    project_name = Col('Project Name')
    graded1 = GradeCol('Graded1')
    graded2 = GradeCol('Graded2')
    regraded1 = ReGradeCol('Regrade1')
    regraded2 = ReGradeCol('Regrade2')
    reconciled = ReconcileCol('Reconcile')

def connect_db():
    db = pymysql.connect(host="mysql.server", user="joeacanfora", passwd="password",db="joeacanfora$CrowdStore") #charset='utf8')
    return db

def rename(dictionary,old_key,new_key):
    dictionary[new_key] = dictionary.pop(old_key)


@app.route('/')
def homepage():
    try:
        db = connect_db()
        c = db.cursor(pymysql.cursors.DictCursor)
        c.execute("""SELECT series_number, project_id, project_name,
        CONCAT(videopressent, ':', graded1, ':1:', series_number),
        CONCAT(videopressent, ':', graded2, ':2:', series_number),
        CONCAT(videopressent, ':', regraded1, ':1:', series_number),
        CONCAT(videopressent, ':', regraded2, ':2:', series_number),
        CONCAT(videopressent, ':', reconciled, ':1:', series_number) FROM project_table
        WHERE series_number < 54 OR series_number > 1086""")

        query = c.fetchall()
        for q in query:
            rename(q, str("CONCAT(videopressent, ':', graded1, ':1:', series_number)"), str('graded1'))
            rename(q, str("CONCAT(videopressent, ':', graded2, ':2:', series_number)"), str('graded2'))
            rename(q, str("CONCAT(videopressent, ':', regraded1, ':1:', series_number)"), str('regraded1'))
            rename(q, str("CONCAT(videopressent, ':', regraded2, ':2:', series_number)"), str('regraded2'))
            rename(q, str("CONCAT(videopressent, ':', reconciled, ':1:', series_number)"), str('reconciled'))
        table = TopTable(query)

        return render_template('list.html', table = str(table.__html__()))
    except Exception as inst:
        return str(inst)# + '\n' + str(query)

@app.route('/project_page/<int:proj_id>')
def project_info_page(proj_id):
    try:
        db = connect_db()
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
        c.execute("""SELECT soldlevel1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        sl1 = c.fetchall()[0][0]
        c.execute("""SELECT othcompreference1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        ocr1 = c.fetchall()[0][0]
        c.execute("""SELECT othcompname1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        ocn1 = c.fetchall()[0][0]
        c.execute("""SELECT pitchFounder1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pf1 = c.fetchall()[0][0]
        c.execute("""SELECT pitchTechnology1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pt1 = c.fetchall()[0][0]
        c.execute("""SELECT pitchCustomer1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pc1 = c.fetchall()[0][0]
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
        c.execute("""SELECT music1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        m1 = c.fetchall()[0][0]
        c.execute("""SELECT animations1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        a1 = c.fetchall()[0][0]
        c.execute("""SELECT patent1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pat1 = c.fetchall()[0][0]
        # c.execute("""SELECT logo1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        # logo1 = c.fetchall()[0][0]
        c.execute("""SELECT rewardsMentioned1 FROM project_table WHERE project_id = %s""", (proj_id, ))
        rm1 = c.fetchall()[0][0]

        ####
        c.execute("""SELECT grader2PID FROM project_table WHERE project_id = %s""", (proj_id, ))
        g2ID = c.fetchall()[0][0]
        c.execute("""SELECT videoquaility2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        vidqual2 = c.fetchall()[0][0]
        c.execute("""SELECT soldlevel2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        sl2 = c.fetchall()[0][0]
        c.execute("""SELECT othcompreference2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        ocr2 = c.fetchall()[0][0]
        c.execute("""SELECT othcompname2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        ocn2 = c.fetchall()[0][0]
        c.execute("""SELECT pitchFounder2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pf2 = c.fetchall()[0][0]
        c.execute("""SELECT pitchTechnology2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pt2 = c.fetchall()[0][0]
        c.execute("""SELECT pitchCustomer2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pc2 = c.fetchall()[0][0]
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
        c.execute("""SELECT music2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        m2 = c.fetchall()[0][0]
        c.execute("""SELECT animations2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        a2 = c.fetchall()[0][0]
        c.execute("""SELECT patent2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        pat2 = c.fetchall()[0][0]
        # c.execute("""SELECT logo2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        # logo2 = c.fetchall()[0][0]
        c.execute("""SELECT rewardsMentioned2 FROM project_table WHERE project_id = %s""", (proj_id, ))
        rm2 = c.fetchall()[0][0]


        return render_template("project.html", project_id = proj_id, project_name = name, series_number = series_number, project_url = project_url,
        status = status, currency = currency, goal = goal, end_date = end_date, author_name = author,
        location = location, category = category, main_video_link = video,
        grader1PID = g1ID, videoquaility1 = vidqual1, othcompreference1 = ocr1, othcompname1 = ocn1,
        pitchFounder1 = pf1, pitchTechnology1 = pt1, pitchCustomer1 = pc1, founderschool1 = fsr1, founderschoolname1 = fsn1, founderstartup1 = fsur1,
        founderstartupname1 = fsun1, prototypes1 = p1, endorsementname1 = en1, endorsements1 = e1,
        grader2PID = g2ID, videoquaility2 = vidqual2, othcompreference2 = ocr2, othcompname2 = ocn2,
        pitchFounder2 = pf2, pitchTechnology2 = pt2, pitchCustomer2 = pc2, founderschool2 = fsr2, founderschoolname2 = fsn2, founderstartup2 = fsur2,
        founderstartupname2 = fsun2, prototypes2 = p2, endorsementname2 = en2, endorsements2 = e2, videocontent2 = sl2, videocontent1 = sl1,
        music1 = m1, music2 = m2, patent1 = pat1, patent2 = pat2)
    except Exception as inst:
        return str(inst)

class GradeForm(Form):
    """edit user Profile EditForm"""
    graderPID = TextField('graderPID', [validators.Length(min=3, max=50), validators.Required()])
    videoquaility = RadioField('videoquaility', choices=[(1, '(1) poor'), (2, '(2) below average'), (3, '(3) average'),
        (4, '(4) above average'), (5, '(5) high')], validators=[validators.Required()])
    soldlevel = RadioField('videoquaility', choices=[(1, '(1) not at all'), (2, '(2) somewhat'), (3, '(3) adequately'),
        (4, '(4) strongly'), (5, '(5) completely')], validators=[validators.Required()])
    othcompreference = BooleanField('othcompreference', validators=[validators.Required()])
    othcompname = TextField('othcompname', validators = [validators.Length(max=100)])
    founderschool = BooleanField('founderschool', validators=[validators.Required()])
    founderschoolname = TextField('founderschoolname', validators = [validators.Length(max=100)])
    founderstartup = BooleanField('founderstartup', validators=[validators.Required()])
    founderstartupname = TextField('founderstartupname', validators = [validators.Length(max=100)])
    prototype = BooleanField('prototype', validators=[validators.Required()])
    music = BooleanField('music', validators=[validators.Required()])
    animations = BooleanField('animations', validators=[validators.Required()])
    patent = BooleanField('patent', validators=[validators.Required()])
    logo = BooleanField('logl', validators=[validators.Required()])
    rewardsmentioned = BooleanField('rewardsmentioned', validators=[validators.Required()])
    endorsement = BooleanField('endorsement', validators=[validators.Required()])
    endorsementname = TextField('endorsementname', validators = [validators.Length(max=100)])
    pitchfocusfounder = BooleanField('pitchfocusfounder', validators=[validators.Required()])
    pitchfocustechnology = BooleanField('pitchfocustechnology', validators=[validators.Required()])
    pitchfocuscustomer = BooleanField('pitchfocuscustomer', validators=[validators.Required()])
    videolength = TextField('videolength', [validators.Length(min=3, max=50), validators.Required()])
    submitButton = SubmitField('Submit')

@app.route('/grade_project/<int:grade_num>/<int:series_num>',  methods=['GET', 'POST'])
def project_grade_page(grade_num, series_num):
    form = GradeForm(request.form, csrf_enabled = False)
    try:
        if request.method == 'POST':

            # return form_saved(form, grade_num, series_num)
            form_saved(form, grade_num, series_num, '')
            return redirect('http://joeacanfora.pythonanywhere.com/')
        else:
            db = connect_db()
            c = db.cursor()
            c.execute("""SELECT main_video_link from project_table WHERE series_number = %s""", (series_num, ))
            video = c.fetchall()
            video = video[0][0]

            c.execute("""SELECT project_name from project_table WHERE series_number = %s""", (series_num, ))
            proj_name = c.fetchall()
            proj_name = proj_name[0][0]

            return render_template("grade_project.html", title = proj_name, video_link = video, form = form,
                url= 'https://www.pythonanywhere.com/user/joeacanfora/form_saved/' + str(grade_num) + '/' + str(series_num))
    except Exception as inst:
        return str(inst)

@app.route('/regrade_project/<int:grade_num>/<int:series_num>',  methods=['GET', 'POST'])
def project_regrade_page(grade_num, series_num):
    form = GradeForm(request.form, csrf_enabled = False)
    try:
        if request.method == 'POST':

            # return form_saved(form, grade_num, series_num)
            form_saved(form, grade_num, series_num, '_regrade')
            return redirect('http://joeacanfora.pythonanywhere.com/')
        else:
            db = connect_db()
            c = db.cursor()
            c.execute("""SELECT main_video_link from project_table WHERE series_number = %s""", (series_num, ))
            video = c.fetchall()
            video = video[0][0]

            c.execute("""SELECT project_name from project_table WHERE series_number = %s""", (series_num, ))
            proj_name = c.fetchall()
            proj_name = proj_name[0][0]

            return render_template("grade_project.html", title = proj_name, video_link = video, form = form,
                url= 'https://www.pythonanywhere.com/user/joeacanfora/form_saved/' + str(grade_num) + '/' + str(series_num))
    except Exception as inst:
        return str(inst)

@app.route('/reconcile_project/<int:grade_num>/<int:series_num>',  methods=['GET', 'POST'])
def project_reconcile_page(grade_num, series_num):
    form = GradeForm(request.form, csrf_enabled = False)
    try:
        if request.method == 'POST':

            # return form_saved(form, grade_num, series_num)
            form_saved(form, grade_num, series_num, '_reconcile')
            return redirect('http://joeacanfora.pythonanywhere.com/')
        else:
            db = connect_db()
            c = db.cursor()
            c.execute("""SELECT main_video_link from project_table WHERE series_number = %s""", (series_num, ))
            video = c.fetchall()
            video = video[0][0]

            c.execute("""SELECT project_name from project_table WHERE series_number = %s""", (series_num, ))
            proj_name = c.fetchall()
            proj_name = proj_name[0][0]

            c.execute("""SELECT project_name from project_table WHERE series_number = %s""", (series_num, ))
            name = c.fetchall()[0][0]
            c.execute("""SELECT series_number from project_table WHERE series_number = %s""", (series_num, ))
            series_number = c.fetchall()[0][0]
            c.execute("""SELECT project_url from project_table WHERE series_number = %s""", (series_num, ))
            project_url = c.fetchall()[0][0]
            c.execute("""SELECT status from project_table WHERE series_number = %s""", (series_num, ))
            status = c.fetchall()[0][0]
            c.execute("""SELECT currency FROM project_table WHERE series_number = %s""", (series_num, ))
            currency = c.fetchall()[0][0]
            c.execute("""SELECT goal FROM project_table WHERE series_number = %s""", (series_num, ))
            goal = c.fetchall()[0][0]
            c.execute("""SELECT end_date FROM project_table WHERE series_number = %s""", (series_num, ))
            end_date = c.fetchall()[0][0]
            c.execute("""SELECT author_name FROM project_table WHERE series_number = %s""", (series_num, ))
            author = c.fetchall()[0][0]
            c.execute("""SELECT location FROM project_table WHERE series_number = %s""", (series_num, ))
            location = c.fetchall()[0][0]
            c.execute("""SELECT category FROM project_table WHERE series_number = %s""", (series_num, ))
            category = c.fetchall()[0][0]
            c.execute("""SELECT main_video_link FROM project_table WHERE series_number = %s""", (series_num, ))
            video = c.fetchall()[0][0]
            #######
            c.execute("""SELECT grader1PID FROM project_table WHERE series_number = %s""", (series_num, ))
            g1ID = c.fetchall()[0][0]
            c.execute("""SELECT videoquaility1 FROM project_table WHERE series_number = %s""", (series_num, ))
            vidqual1 = c.fetchall()[0][0]
            c.execute("""SELECT soldlevel1 FROM project_table WHERE series_number = %s""", (series_num, ))
            sl1 = c.fetchall()[0][0]
            c.execute("""SELECT othcompreference1 FROM project_table WHERE series_number = %s""", (series_num, ))
            ocr1 = c.fetchall()[0][0]
            c.execute("""SELECT othcompname1 FROM project_table WHERE series_number = %s""", (series_num, ))
            ocn1 = c.fetchall()[0][0]
            c.execute("""SELECT pitchFounder1 FROM project_table WHERE series_number = %s""", (series_num, ))
            pf1 = c.fetchall()[0][0]
            c.execute("""SELECT pitchTechnology1 FROM project_table WHERE series_number = %s""", (series_num, ))
            pt1 = c.fetchall()[0][0]
            c.execute("""SELECT pitchCustomer1 FROM project_table WHERE series_number = %s""", (series_num, ))
            pc1 = c.fetchall()[0][0]
            c.execute("""SELECT founderschool1 FROM project_table WHERE series_number = %s""", (series_num, ))
            fsr1 = c.fetchall()[0][0]
            c.execute("""SELECT founderschoolname1 FROM project_table WHERE series_number = %s""", (series_num, ))
            fsn1 = c.fetchall()[0][0]
            c.execute("""SELECT founderstartup1 FROM project_table WHERE series_number = %s""", (series_num, ))
            fsur1 = c.fetchall()[0][0]
            c.execute("""SELECT founderstartupname1 FROM project_table WHERE series_number = %s""", (series_num, ))
            fsun1 = c.fetchall()[0][0]
            c.execute("""SELECT prototypes1 FROM project_table WHERE series_number = %s""", (series_num, ))
            p1 = c.fetchall()[0][0]
            c.execute("""SELECT endorsements1 FROM project_table WHERE series_number = %s""", (series_num, ))
            e1 = c.fetchall()[0][0]
            c.execute("""SELECT endorsementname1 FROM project_table WHERE series_number = %s""", (series_num, ))
            en1 = c.fetchall()[0][0]
            c.execute("""SELECT music1 FROM project_table WHERE series_number = %s""", (series_num, ))
            m1 = c.fetchall()[0][0]
            c.execute("""SELECT animations1 FROM project_table WHERE series_number = %s""", (series_num, ))
            a1 = c.fetchall()[0][0]
            c.execute("""SELECT patent1 FROM project_table WHERE series_number = %s""", (series_num, ))
            pat1 = c.fetchall()[0][0]
            # c.execute("""SELECT logo1 FROM project_table WHERE series_number = %s""", (series_num, ))
            # logo1 = c.fetchall()[0][0]
            c.execute("""SELECT rewardsMentioned1 FROM project_table WHERE series_number = %s""", (series_num, ))
            rm1 = c.fetchall()[0][0]
            ####
            c.execute("""SELECT grader2PID FROM project_table WHERE series_number = %s""", (series_num, ))
            g2ID = c.fetchall()[0][0]
            c.execute("""SELECT videoquaility2 FROM project_table WHERE series_number = %s""", (series_num, ))
            vidqual2 = c.fetchall()[0][0]
            c.execute("""SELECT soldlevel2 FROM project_table WHERE series_number = %s""", (series_num, ))
            sl2 = c.fetchall()[0][0]
            c.execute("""SELECT othcompreference2 FROM project_table WHERE series_number = %s""", (series_num, ))
            ocr2 = c.fetchall()[0][0]
            c.execute("""SELECT othcompname2 FROM project_table WHERE series_number = %s""", (series_num, ))
            ocn2 = c.fetchall()[0][0]
            c.execute("""SELECT pitchFounder2 FROM project_table WHERE series_number = %s""", (series_num, ))
            pf2 = c.fetchall()[0][0]
            c.execute("""SELECT pitchTechnology2 FROM project_table WHERE series_number = %s""", (series_num, ))
            pt2 = c.fetchall()[0][0]
            c.execute("""SELECT pitchCustomer2 FROM project_table WHERE series_number = %s""", (series_num, ))
            pc2 = c.fetchall()[0][0]
            c.execute("""SELECT founderschool2 FROM project_table WHERE series_number = %s""", (series_num, ))
            fsr2 = c.fetchall()[0][0]
            c.execute("""SELECT founderschoolname2 FROM project_table WHERE series_number = %s""", (series_num, ))
            fsn2 = c.fetchall()[0][0]
            c.execute("""SELECT founderstartup2 FROM project_table WHERE series_number = %s""", (series_num, ))
            fsur2 = c.fetchall()[0][0]
            c.execute("""SELECT founderstartupname2 FROM project_table WHERE series_number = %s""", (series_num, ))
            fsun2 = c.fetchall()[0][0]
            c.execute("""SELECT prototypes2 FROM project_table WHERE series_number = %s""", (series_num, ))
            p2 = c.fetchall()[0][0]
            c.execute("""SELECT endorsements2 FROM project_table WHERE series_number = %s""", (series_num, ))
            e2 = c.fetchall()[0][0]
            c.execute("""SELECT endorsementname2 FROM project_table WHERE series_number = %s""", (series_num, ))
            en2 = c.fetchall()[0][0]
            c.execute("""SELECT music2 FROM project_table WHERE series_number = %s""", (series_num, ))
            m2 = c.fetchall()[0][0]
            c.execute("""SELECT animations2 FROM project_table WHERE series_number = %s""", (series_num, ))
            a2 = c.fetchall()[0][0]
            c.execute("""SELECT patent2 FROM project_table WHERE series_number = %s""", (series_num, ))
            pat2 = c.fetchall()[0][0]
            # c.execute("""SELECT logo2 FROM project_table WHERE series_number = %s""", (series_num, ))
            # logo2 = c.fetchall()[0][0]
            c.execute("""SELECT rewardsMentioned2 FROM project_table WHERE series_number = %s""", (series_num, ))
            rm2 = c.fetchall()[0][0]

            if (vidqual1 == vidqual2):
                form.videoquality = ''
            if (sl1 == sl2):
                form.soldlevel = ''
            if (ocr1 == ocr2):
                form.othcompreference = ''
            if (ocn1 == ocn2):
                form.othcompname = ''
            if (pf1 == pf2):
                form.pitchfocusfounder = ''
            if (pt1 == pt2):
                form.pitchfocustechnology = ''
            if (pc1 == pc2):
                form.pitchfocuscustomer = ''
            if (fsr1 == fsr2):
                form.founderschool = ''
            if (pt1 == pt2):
                form.pitchtecnology = ''
            if (pc1 == pc2):
                form.pitchcustomer = ''
            if (fsn1 == fsn2):
                form.founderschoolname = ''
            if (fsur1 == fsur2):
                form.founderstartup = ''
            if (fsun1 == fsun2):
                form.founderstartupname = ''
            if (p1 == p2):
                form.prototype = ''
            if (en1 == en2):
                form.endorsementname = ''
            if (e1 == e2):
                form.endorsement = ''
            if (m1 == m2):
                form.music = ''
            if (a1 == a2):
                form.animations = ''
            if (pat1 == pat2):
                form.patent = ''
            # if (logo1 == logo2):
            #     form.logo = ''
            if (rm1 == rm2):
                form.rewardsmentioned = ''

            return render_template("reconcile_project.html", title = proj_name, video_link = video, form = form,
                project_name = name, series_number = series_number, project_url = project_url,
                status = status, currency = currency, goal = goal, end_date = end_date, author_name = author,
                location = location, category = category, main_video_link = video,
                grader1PID = g1ID, videoquaility1 = vidqual1, othcompreference1 = ocr1, othcompname1 = ocn1,
                pitchFounder1 = pf1, pitchTechnology1 = pt1, pitchCustomer1 = pc1, founderschool1 = fsr1, founderschoolname1 = fsn1, founderstartup1 = fsur1,
                founderstartupname1 = fsun1, prototypes1 = p1, endorsementname1 = en1, endorsements1 = e1,
                grader2PID = g2ID, videoquaility2 = vidqual2, othcompreference2 = ocr2, othcompname2 = ocn2,
                pitchFounder2 = pf2, pitchTechnology2 = pt2, pitchCustomer2 = pc2, founderschool2 = fsr2, founderschoolname2 = fsn2, founderstartup2 = fsur2,
                founderstartupname2 = fsun2, prototypes2 = p2, endorsementname2 = en2, endorsements2 = e2, videocontent2 = sl2, videocontent1 = sl1,
                music1 = m1, music2 = m2, patent1 = pat1, patent2 = pat2, animations1 = a1, animations2 = a2,
                rewards1 = rm1, rewards2 = rm2,
                url= 'https://www.pythonanywhere.com/user/joeacanfora/form_saved/' + str(grade_num) + '/' + str(series_num))
    except Exception as inst:
        return str(inst)

def form_saved(form, grade_num, series_num, regrade):

    return save_form_to_db(form, grade_num, series_num, regrade)


def save_form_to_db(form, grade_num, series_num, regrade):
    try:
        db = connect_db()
        db.autocommit(True)
        c = db.cursor()
        graded = True
        videoLength = None
        colon = (int(str(form.videolength.data).find(":")))
        if  colon != -1:
            videoLength = int(str(form.videolength.data).split(":")[0]) * 60 + (int(str(form.videolength.data).split(":")[1]))
        args = (series_num, project_id, graded, str(form.graderPID.data) + regrade, form.videoquaility.data, form.soldlevel.data, form.othcompreference.data,
                form.othcompname.data, form.founderschool.data, form.founderschoolname.data, form.founderstartup.data,
                form.founderstartupname.data, form.prototype.data, form.endorsement.data, form.endorsementname.data,
                form.music.data, form.animations.data, form.patent.data, form.rewardsmentioned.data,
                form.pitchfocusfounder.data, form.pitchfocustechnology.data, form.pitchfocuscustomer.data, videoLength, series_num)
        if grade_num == 1 and regrade == '':
            c.execute('''UPDATE project_table SET graded1=TRUE
                WHERE series_number=%s''', (series_num,))
        elif grade_num == 2 and regrade == '':
            c.execute('''UPDATE project_table SET graded2=TRUE
                    WHERE series_number=%s''',(series_num,))

        elif grade_num == 1 and regrade == '_regrade':
            c.execute('''UPDATE project_table SET regraded1=TRUE
                WHERE series_number=%s''', (series_num,))
        elif grade_num == 1 and regrade == '_regrade':
            c.execute('''UPDATE project_table SET regraded2=TRUE
                WHERE series_number=%s''', (series_num,))
        elif grade_num == 0 and regrade == '_reconcile':
            c.execute('''UPDATE project_table SET reconciled=TRUE
                WHERE series_number=%s''', (series_num,))
        else:
            return 'Fail ' + str(grade_num)
        c.connection.commit()
        c.execute('''INSERT INTO video_grades_table (project_id, series_number, graded, graderPID,
                    videopressent, videoquaility, soldlevel,
                    othcompreference, othcompname, founderschool, founderschoolname,
                    founderstartup, founderstartupname, prototypes, endorsements,
                    endorsementname, music, animations, paten1,
                    rewardsMentioned, pitchFounder, pitchTechnology, pitchCustomer,
                    videoLength)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,
                    %s,%s,%s,%s)''', args)
        c.connection.commit()
        return str(c.fetchall())
    except Exception as inst:
        return str(inst)


