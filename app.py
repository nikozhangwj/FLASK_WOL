# encoding: utf-8

from flask import Flask, render_template, request, jsonify
from wakeonlan import send_magic_packet
from nettools import search_mac
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', welcome_words="Hello, Niko!", macs=search_mac())


@app.route('/wake', methods=['post'])
def wake():
    response = {}

    try:
        mac = request.values.get('mac_addr')
        br = request.values.get('br_addr')
        if mac == "":
            raise ValueError('MAC address cannot be none.')
        send_magic_packet(mac, ip_address=br)
        response['code'] = 1
        response['message'] = '请验证'
    except ValueError as error:
        response['code'] = 0
        response['message'] = str(error)

    return jsonify(response)


# Debug调试的时候从这里启用，正式环境使用gunicorn启动
if __name__ == '__main__':
    app.run(debug=True, port=50005, host='127.0.0.1')
