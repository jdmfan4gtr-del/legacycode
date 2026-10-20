
class asset:
    def __init__(self,name:str,value:float,leverage_multiplier:int):
        """
        the constructor initializes a high value assett
        """
        self.name=name
        self.value=value
        self.leverage_multiplier=leverage_multiplier
    
    def get_value(self):
        """ getter method to access data securely"""
        return self.value
    def calculate_power(self):
        """calculates the total financial leverage of this assett"""
        return self.value * self.leverage_multiplier
    def display_profile(self):
        """output the assett metrics to the profile"""
        print(f"--- asset profile ---: {self.name}")
        print(f"base value : {self.value}")
        print(f"leverage_multiplier: {self.leverage_multiplier}")
        print(f"total leverage : {self.leverage_multiplier * self.value}")

class portfolio:
    def __init__(self,owner_name:str):
        self.owner_name=owner_name
        self.assets = []
    def add_assets(self,asset:asset):
        self.assets.append(asset)
        print(f"[system log] asset {asset.name} added to {self.owner_name}'s portfolio")
    def calculate_total_net_worth(self):
        net_worth=0
        for i in self.assets:
            net_worth+=net_worth + i.get_value()
        return net_worth
    def calculate_total_leverage_power(self):
        total_leverage=0
        for i in self.assets:
            total_leverage+=total_leverage + i.calculate_power()
        return total_leverage
    
    def display_portfolio_summary(self):
        print("portfolio")
        print(f"owner name : {self.owner_name}")
        print(f"total unique assets : {len(self.assets)}")
        print(f"liquid base value : {self.calculate_total_net_worth():}")
        print(f"total leverage power : {self.calculate_total_leverage_power():,}")
        print(f"===================================\n")
        print("***************************************")

from fetcher import datafetcher

if __name__=="__main__":
    market_intelligence=datafetcher()
    live_rates=market_intelligence.fetch_market_prices()
    btc_usd_rate=live_rates.get('bitcoin',{}).get('usd',65000.0)
    eth_usd_rate=live_rates.get('ethereum',{}).get('usd',35000.0)

    my_empire=portfolio("future billionaire")
    bitcoin_reserve=asset("bitcoin reserve",(2.5 * btc_usd_rate), 12)
    eth_reserve=asset("ethereum reserve",(15.0 * eth_usd_rate),8)
    my_empire.add_assets(bitcoin_reserve)
    my_empire.add_assets(eth_reserve)

    my_empire.display_portfolio_summary()
