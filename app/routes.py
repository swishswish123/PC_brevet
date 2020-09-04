from flask import render_template, Blueprint

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
@bp_main.route('/acceuil')
def home():
    return render_template('about.html')


@bp_main.route('/annales_brevet')
def brevet_years():
    return render_template('brevet_years.html')


@bp_main.route('/version_complete')
def version_complete():
    return render_template('version_complete.html')


@bp_main.route('/annales_brevet/<id>')
def year(id):
    page = id + '.html'
    return render_template(page)


@bp_main.route('/<file_name>')
def region(file_name):
    return render_template('pdf_view.html', file_name=file_name)



