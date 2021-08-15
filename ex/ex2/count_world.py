import sys
import requests

url = sys.argv[1]
url_2 = sys.argv[2]

response = requests.get(url)
  # HTTPのステータスコード取得
  # レスポンスのHTMLを文字列で取得
if response.status_code == 200:
    print(len(url_2))

else:
    print("ERROR:404")
