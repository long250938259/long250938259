import requests


def response_301_code():
    interface_url = 'https://butian.360.cn'
    response_get = requests.get(interface_url)
    response_get_code = response_get.status_code
    print('response_get_code: ', response_get_code)


response_301_code()