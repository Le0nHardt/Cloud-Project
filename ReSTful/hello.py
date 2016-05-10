from flask import Flask,url_for,request,Response,json,jsonify

app = Flask(__name__)

# cd folder
# cd flask
# source bin/activate
# cd ..
# python hello.py

# @app.route("/")
# def hello():
#     with open('users.xml',encoding='utf-8') as f:
#         output = f.read()
#         return output
#     # return "Hello~~"
#
# @app.route('/articles')
# def api_articles():
#     return url_for('users.xml')
#
# @app.route('/articles/<articleid>')
# def api_article(articleid):
#     return articleid

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello zhenwei'

@app.route('/zhenwei', methods = ['GET'])
def api_zhenwei():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp


@app.route('/aurin',methods = ['GET'])
def api_aurin():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    return jsonify(data)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
@app.route('/aurin/rate_in_adelaide',methods = ['GET'])
def aurin_adelaide():
    adelaide_data_aurin = {
        'unemployment population':  73414,
        'employment population':  730754,
        'population':  1297410,
        'unemp rate':  0.05658504250776547,
        'emp rate':  0.5632406101386609
    }
    return jsonify(adelaide_data_aurin)

@app.route('/aurin/popandage_in_adelaide',methods = ['GET'])
def pop_adelaide():
    adelaide_data_pop = {
        'age15 to age19': 81781,
        'age80 to age84': 29456,
        'age75 to age79': 36786,
        'age60 to age64': 73618,
        'age50 to age54': 89191,
        'age45 to age49': 87905,
        'age35 to age39': 81967,
        'total persons': 1297410,
        'age10 to age14': 73658,
        'age over 85': 31747,
        'age0 to age4': 77491,
        'age65 to age69': 64209,
        'age25 to age29': 93862,
        'age5 to age9': 74484,
        'age30 to age34': 87094,
        'age40 to age44': 91298,
        'age55 to age59': 81293,
        'age70 to age74': 46277,
        'age over 65': 208475,
        'age20 t0 age24': 95293
    }
    return jsonify(adelaide_data_pop)

@app.route('/aurin/twitter_in_adelaide',methods = ['GET'])
def twitter_adelaide():
    adelaide_data_twitter = {

    }
    return jsonify(adelaide_data_twitter)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

@app.route('/aurin/rate_in_brisbane',methods = ['GET'])
def aurin_brisbane():
    brisbane_data_aurin = {
        'unemployment population':  123930,
        'employment population':  1366124,
        'population':  2181419,
        'unemp rate':  0.05681164416373012,
        'emp rate':  0.6262547451910889
    }
    return jsonify(brisbane_data_aurin)

@app.route('/aurin/popandage_in_brisbane',methods = ['GET'])
def pop_brisbane():
    brisbane_data_pop = {
        'age5 to age9': 144870,
        'age30 to age34': 167527,
        'age75 to age79': 42453,
        'age15 to age19': 146208,
        'age25 to age29': 178552,
        'age35 to age39': 155597,
        'age over 65': 255352,
        'age40 to age44': 163637,
        'age0 to age4': 151948,
        'total persons': 2181419,
        'age over 85': 32905,
        'age10 to age14': 135698,
        'age65 to age69': 88104,
        'age45 to age49': 143544,
        'age55 to age59': 119909,
        'age20 to age24': 174313,
        'age50 to age54': 139036,
        'age70 to age74': 59758,
        'age60 to age64': 105228,
        'age80 to age84': 32132
    }

    return jsonify(brisbane_data_pop)

@app.route('/aurin/twitter_in_brisbane',methods = ['GET'])
def twitter_brisbane():
    brisbane_data_twitter = {
        '_id' : 'Brisbane',
        '_rev' : '1-169481506d37e1b174f509a5340eafb8',
        'politics relevant' : 130493,
        'politics irrelevant' : 247475,
        'positive' : 25457,
        'negative' : 7134,
        'neutral' : 345377,
        'total' : 377968
    }
    return jsonify(brisbane_data_twitter)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

@app.route('/aurin/rate_in_sydney',methods = ['GET'])
def aurin_sydney():
    sydney_data_aurin = {
        'unemployment population':  261049,
        'employment population':  2725959,
        'population':  4447961,
        'unemp rate':  0.05868958833047322,
        'emp rate':  0.6128558681157501
    }
    return jsonify(sydney_data_aurin)

@app.route('/aurin/popandage_in_sydney',methods = ['GET'])
def pop_sydney():
    brisbane_data_pop = {
        'age45 to age49': 292744,
        'age10 to age14': 255946,
        'age40 to age44': 328273,
        'age0 to age4': 304263,
        'age60 to age64': 217019,
        'age35 to age39': 328342,
        'age30 to age34': 366424,
        'age over 65': 570853,
        'age20 to age24': 328571,
        'age50 to age54': 288734,
        'total persons': 4447961,
        'age80 to age84': 76804,
        'age15 to age19': 269521,
        'age75 to age79': 99423,
        'age5 to age9': 275324,
        'age70 to age74': 130012,
        'age65 to age69': 184797,
        'age over 85': 79817,
        'age25 to age29': 368220,
        'age55 to age59': 253727
    }
    return jsonify(sydney_data_pop)

@app.route('/aurin/twitter_in_sydney',methods = ['GET'])
def twitter_sydney():
    sydney_data_twitter = {

    }
    return jsonify(sydney_data_twitter)


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

@app.route('/aurin/rate_in_melbourne',methods = ['GET'])
def aurin_melbourne():
    melboure_data_aurin = {
        'unemployment population':  176645,
        'employment population':  1971396,
        'population':  3225542,
        'unemp rate':  0.054764439588757485,
        'emp rate':  0.6111828647712539
    }
    return jsonify(melbourne_data_aurin)

@app.route('/aurin/popandage_in_melbourne',methods = ['GET'])
def pop_melbourne():
    melbourne_data_pop = {
        'age25 to age29': 288769,
        'age35 to age39': 236334,
        'age75 to age79': 75975,
        'age over 65': 421375,
        'age10 to age14': 174582,
        'age60 to age64': 155091,
        'age65 to age69': 133216,
        'age80 to age84': 58137,
        'age70 to age74': 96378,
        'age15 to age19': 190085,
        'age30 to age34': 271482,
        'total persons': 3225542,
        'age45 to age49': 212326,
        'age over 85': 57669,
        'age5 to age9': 188358,
        'age0 to age4': 206655,
        'age50 to age54': 204161,
        'age55 to age59': 179702,
        'age20 to age24': 257012,
        'age40 to age44': 239610
    }
    return jsonify(melbourne_data_pop)

@app.route('/aurin/twitter_in_melbourne',methods = ['GET'])
def twitter_melbourne():
    sydney_data_twitter = {

    }
    return jsonify(melbourne_data_twitter)



#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run()
