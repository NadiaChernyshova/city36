from flask import Flask, Response, json, render_template
from DBcm import UseDatabase
from core.Weather import Weather
from core.News import News


app = Flask(__name__)
host = '10.0.255.218'


app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'city36user',
                          'password': 'Hydroquinone.alexeev999',
                          'database': 'City36',
                          'charset': 'utf8'}




@app.route('/')
def index():

    contents = []
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = "SELECT * FROM User"

        cursor.execute(_SQL)

        contents = cursor.fetchall()
    
    empList = []
    for emp in contents:
        empDict = {
            'User_Id': emp[0],
            'Name': emp[1],
            'Surname': emp[2],
            'Telephone': emp[3],
            'Role_Id': emp[4] 
        }
        empList.append(empDict)
        
    return json.dumps(empList)



#Отвечает за погоду
@app.route('/weather')
def weather():
    weather = Weather('6acbbc55257aa6d085fd9e1813999d0c')
    return str(weather.format_data())

@app.route('/news')
def news():
    news = News()
    return str(news.parse())




#Сайты


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    weather = Weather('6acbbc55257aa6d085fd9e1813999d0c')
    weather = weather.format_data()
    news_d = News()
    news_d = news_d.parse()
    return render_template('main.html', data=weather, news = news_d)


@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/poll')
def poll():
    return render_template('poll.html')

if __name__ == "__main__":
    app.run(host=host, debug=True)