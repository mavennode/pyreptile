# URL
# HTTP Request
#	http header (key/value pairs)
#	GET / POST (data)
# HTTP Requese

import urllib.request

def fetch(url):
	http_header = {'User-Agent': 'Chrome'}   #dictionary
	http_request = urllib.request.Request(url,None,http_header)
	
	http_response = urllib.request.urlopen(http_request)
	
	# Status code
	# 200 / ok
	# 404 / Invalid URL
	# 500 / Iternal Error
	print(http_response.code)
	
	# http header (key/value pairs)
	print(http_response.info())
	
	print("-----data-------")
	
	print("Start downloading data")
	print(http_response.read())
	print('finish')
	
if __name__ == "__main__":
	fetch("http://www.meituan.com/api/v1/divisions")