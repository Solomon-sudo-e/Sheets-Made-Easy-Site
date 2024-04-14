import sys
import pandas as pd
from flask import Flask, render_template, request
from file_scraper.html_files import write_to_html_file, create_values


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello_world():  # put application's code here
    print(sys.version)
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.content_type.__contains__('text/csv'):
        df = pd.read_csv(file)
    else:
        return 'not a csv file'
    create_values(df)
    write_to_html_file(df.head(5), 'Your File', 'templates/table.html')
    return render_template('upload_success.html', values=df.columns.values.tolist())


@app.route('/statistics', methods=['GET','POST'])
def statistics():
    return render_template('upload_success.html')

if __name__ == '__main__':
    app.run()
