import pandas as pd
import numpy as np

def write_to_html_file(df, title='', filename='out.html'):
    result = '''
<html>
<head>
<style>

    h2 {
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
    }
    table { 
        margin-left: auto;
        margin-right: auto;
    }
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    th, td {
        padding: 5px;
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 90%;
    }
    table tbody tr:hover {
        background-color: #dddddd;
    }
    .wide {
        width: 90%; 
    }

</style>
</head>
<body>
    '''
    result += '<h2> %s </h2>\n' % title
    result += df.to_html(classes='wide', escape=False)
    result += '''
</body>
</html>
'''
    with open(filename, 'w') as f:
        f.write(result)


def find_potential_dtypes(df):
    possible_stats = []
    for col in df.columns:
        if df[col].dtype == np.dtype('int64'):
            possible_stats.append(col)

        if df[col].dtype == np.dtype('object'):
            try:
                pd.to_numeric(col, downcast='integer')
                possible_stats.append(col)
            except ValueError:
                print("Cannot append " + str(col))
    return possible_stats


def create_values(df, filename='out.html'):
    possible_stats = find_potential_dtypes(df)

    filler = ""
    for possible_stat in possible_stats:
        stat = str(possible_stat)
        input = f'''<input type='checkbox' id='input_place_holder{stat}' name='input_place_holder{stat}' value='{stat}'>
                 <label for='input_place_holder{stat}'>{stat}</label><br>
            '''
        filler += input
    result = f'''<form action=/action_page.php>
             {filler}
</form>'''
    with open(filename, 'w') as f:
        f.write(result)



