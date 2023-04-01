import requests
import json

requests.packages.urllib3.disable_warnings()

count = 1
for i in range(1, 9):

    date = "1402-01-01"
    listed_date = list(date)
    listed_date[-1] = str(count)
    date = "".join(listed_date)
    airline = "irz" # ایرلاین ساها
    url = "https://www.airport.ir/NetForm/Service/fids?"
    result = f"{url}date={date}&airline={airline}&AUTH_TOKEN=9890071"
    print(result)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36", "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    response = requests.get(result, headers = headers ,verify = False)
    data = json.loads(response.text)
    
    count += 1

    print(data)