# encoding: utf-8

from flask import Flask, render_template, request, jsonify
from FLASK_WOL.wakeonlan import send_magic_packet
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/wake', methods=['post'])
def wake():
    response = {}

    try:
        mac = request.values.get('mac_addr')
        if mac == None:
            raise ValueError
        send_magic_packet(mac)
        response['code'] = 1
        response['message'] = '请求成功'
    except ValueError as error:
        response['code'] = 0
        response['message'] = str(error)

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=False, port=50005, host='0.0.0.0')