from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/can_build', methods=['POST'])
def can_build_route():
    data = request.json
    length = data.get('length')
    bricks_5m = data.get('bricks_5m')
    bricks_1m = data.get('bricks_1m')

    def can_build(length, bricks_5m, bricks_1m):
        if length <= bricks_5m * 5:
            return True
        
        if length - bricks_5m * 5 <= bricks_1m:
            return True
        
        return False

    result = can_build(length, bricks_5m, bricks_1m)
    response = jsonify({'can_build': result})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)































# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/can_build', methods=['POST'])
# def can_build():
    # data = request.json
    # length = data.get('length')
    # bricks_5m = data.get('bricks_5m')
    # bricks_1m = data.get('bricks_1m')

    # def can_build(length, bricks_5m, bricks_1m):
        # # Check if we have enough 5-meter bricks to cover the entire length
        # if length <= bricks_5m * 5:
            # return True
        
        # # Check if we can cover the remaining length with 1-meter bricks after using all 5-meter bricks
        # if length - bricks_5m * 5 <= bricks_1m:
            # return True
        
        # return False

    # result = can_build(length, bricks_5m, bricks_1m)
    # return jsonify({'can_build': result})

# if __name__ == '__main__':
    # app.run(debug=True)
