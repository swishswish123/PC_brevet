from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/acceuil')
def home():
    return render_template('about.html')

@app.route('/annales_brevet')
def brevet_years():
    return render_template('brevet_years.html')

@app.route('/version_complete')
def version_complete():
    return render_template('version_complete.html')

@app.route('/annales_brevet/<id>')
def year(id):
    page = id + '.html'
    return render_template(page)


@app.route('/<file_name>')
def region(file_name):
    return render_template('pdf_view.html', file_name=file_name)



if __name__ == '__main__':
    app.run()
