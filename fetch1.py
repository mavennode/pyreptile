# Tornado web server
# HTTP Client

import tornado.httpclient

def fetch(url):
	http_header = {'Uer-Agent': 'Chrome'}
	http_request = tornado.httpclient.HTTPRequest(url=url,method='GET',headers=http_header,connect_timeout=20,request_timeout=600)
	
	http_client = tornado.httpclient.HTTPClient()
	print("START downloading data...")
	http_response = http_client.fetch(http_request)
	print("Finish")
	
	print(http_response.code)
	
	# Different from urllib
	all_fields = http_response.headers.get_all()
	for field in all_fields:
		print(field)
	
	print(http_response.body)
	
if __name__ =="__main__":
	fetch("http://www.baidu.com")