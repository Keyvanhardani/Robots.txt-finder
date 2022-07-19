import urllib.request 
import io

def get_robot(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()
print('\nRobots.txt Finder V1 by Keyvan Hardani \n')
print('usage: python app.py')
print('Target URL should start with http or https \n')
target = input('Enter your target URL: ')
print('\n')
print(get_robot(target))
print('\n')
