import json
from urllib import request

url = "https://doa-doa-api-ahmadramadhan.fly.dev/api"

# melakukan http request
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())

# menggunakan perulangan untuk menampilkan data yang memiliki banyak item
for dt in data:
    print(f"- {dt['id']}")
    print(f"- {dt['doa']}")
    print(f"- {dt['ayat']}")
    print(f"- {dt['latin']}")
    print(f"- {dt['artinya']}")