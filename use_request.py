import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success..Respon {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'Upss..terjadi kesalahan requests {response.status_code}')
except Exception as er:
    print(f'You got error {er}')
print('Program ended')