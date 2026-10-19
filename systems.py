class asset:
    def _init_(self,name:str,value:float,leverage_multiplier:int):
        """
        the constructor initializes a high value assett
        """
        self.name=name
        self.value=value
        self.leverage_multiplier=leverage_multiplier
    
    def get_value(self):
        """ getter method to access data securely"""
        return(self.value)
    def calculate_power(self):
        """calculates the total financial leverage of this assett"""
        return self.value * self.leverage_multiplier
    def display_profile(self):
        """output the assett metrics to the profile"""
        print(f"--- asset profile ---: {self.name}")
        print(f"base value : {self.value}")
        print(f"leverage_multiplier: {self.leverage_multiplier}")
        print(f"total leverage : {self.leverage_multiplier * self.value}")

# main code block 
if __name__ == "__main__":
    software_ip = asset("automation engine",50000, 10)
    media_leverage= asset("distribution channel",20000,5)

#execution block
software_ip.display_profile()
media_leverage.display_profile()

#end