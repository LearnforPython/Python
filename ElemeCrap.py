import hashlib
import urllib
from cgi import FieldStorage
import binascii

import urllib.request

def concat_params(params,flag):
    pairs = []
    for key in sorted(params):
        if key == 'sig'and flag==True:
            continue
        val = params[key]
        if isinstance(val, str):
            val = urllib.parse.quote_plus(val)
        if not isinstance(val, FieldStorage):
            pairs.append("{}={}".format(key, val))
    return '&'.join(pairs)

def gen_sig(path_url, params, consumer_secret):
    params = concat_params(params,True)

    to_hash = binascii.hexlify(u'{}?{}{}'.format(
        path_url, params, consumer_secret
    ).encode('utf-8'))

    sig = hashlib.new('sha1', to_hash).hexdigest()
    return sig

path_url = 'https://openapi.ele.me/v2/restaurants/'

params = {'consumer_key':'0170804777','timestamp':'1374908054'}

consumer_secret = '87217cb263701f90316236c4df00d9352fb1da76'

gen_sig(path_url,params,consumer_secret)

def mainCrap(path_url, params, consumer_secret):
    sig = gen_sig(path_url, params, consumer_secret)
    print(sig)
    params.update({'sig':sig})
    params.update({'geo':'121.371422,31.105650'})
    print(params)
    paramsStr = concat_params(params,False)
    url = path_url + '?' + paramsStr
    print(url)
    response = urllib.request.urlopen(url)
    print(response.read())

mainCrap(path_url, params, consumer_secret)
