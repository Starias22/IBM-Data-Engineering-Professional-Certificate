# pip install requests
import requests

url='https://www.ibm.com'
response=requests.get(url)
print(response.url)
print('Response of the request:',response)
print('Status of the response:',response.status_code)

print('Header of the request:',response.request.headers)
print('*****************')

print('Body of the request:',response.request.body)

response_header=response.headers
print('Header of the respone:',response_header)

print('*****************')

print('Request send date:',response_header['date'])

print('*****************')

print('Content type:',response_header['Content-Type'])
print('*****************')

print('Encoding:',response.encoding)
print('*****************')

print('Text:',response.text[:100])







