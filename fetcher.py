import requests

class datafetcher:
    def __init__(self):
        self.target_url="https://www.coingecko.com/"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    def fetch_market_prices(self) -> dict:
        print("initializing hndshake with data provider")
        try:
            response=requests.get(self.target_url,headers=self.headers,timeout=10)

            if response.status_code == 200:
                print("data packet recieved successfully")
                return response.json()

            else:
                print(f"connection failed with status code : {response.status_code}")
                return{}
        except Exception as e:
            print(f"network timeout or hanshake failure : {e}")
            return {}

if __name__=="__main__":
    crawler=datafetcher()
    data=crawler.fetch_market_prices()
    print(data)



