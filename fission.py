from flask import Flask, jsonify
import simplejson as json
import os
import copy
import requests

from lxml import etree

#from pprint import pprint

JSON_PATH = os.path.join(os.path.dirname(__file__), 'request_data.json')

with open(JSON_PATH) as json_file:
    json_data = json.load(json_file)
    json_file.close()


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/search/<string:search_number>')
def search(search_number):

    #pprint(json_data)

    comp, number = unicode.split(search_number, '-', 1)
    request_data = [copy.deepcopy(d) for d in json_data if str.upper(d['key']) == unicode.upper(comp)][0]

    request_data['data'][request_data['search']] = number

    cookies = None

    if request_data['cookies']:
        request_result_with_cookies = requests.get(request_data['cookies']['url'], params=request_data['data'])
        cookies = {request_data['cookies']['key']: request_result_with_cookies.cookies[request_data['cookies']['key']]}
    #pprint(request_data)

    if str.upper(request_data['method']) == 'GET':
        request_result = requests.get(request_data['url'], params=request_data['data'], cookies=cookies)
    else:
        request_result = requests.post(request_data['url'], data=request_data['data'], headers=request_data['headers'], cookies=cookies)

    return request_result.text


    doc = etree.HTML(unicode.encode(request_result.text,encoding='utf-8'))


    r = request_data['result']

    for k in r.keys():
        e = doc.xpath(r[k])
        if e:
            r[k] = e[0].strip()
        else:
            r[k] = ''

    #return request_result.text
    return jsonify(r)


if __name__ == '__main__':
    app.run()
