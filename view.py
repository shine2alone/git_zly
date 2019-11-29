import random
import requests

def gen_low_letters():

    list_a = map(chr, range(ord('a'), ord('z') + 1))

    for i in list_a:
        print(i, end=',')

def get_response(url):

   res = requests.get(url)
   return res.content.decode()

def post_data(url, data):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    return requests.post(url, data=data, headers=headers).content.decode()
