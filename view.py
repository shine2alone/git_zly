import random
import requests

def gen_low_letters():

    list_a = map(chr, range(ord('a'), ord('z') + 1))

    for i in list_a:
        print(i, end=',')

def get_response(url):

   res = requests.get(url)
   return res.content.decode()
