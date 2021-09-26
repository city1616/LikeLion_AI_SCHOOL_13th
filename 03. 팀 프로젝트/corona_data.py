# Team Project
# corona data 수집

# Python 샘플 코드 #

# from urllib2 import Request, urlopen
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
servicekey = 'GCyZSspoE7iPOuN+4UKO10fOhJyXmQhnhGwke3KcD8v2qaWYLQkoGLNn7vTwbctZkR/3uEECJAykpO4UJxUwTQ=='
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : servicekey, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('startCreateDt') : '20200310', quote_plus('endCreateDt') : '20200315' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)

print(type(response_body))

print(request)

'''
import requests

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
res = requests.get(url)
print(res.text)
'''