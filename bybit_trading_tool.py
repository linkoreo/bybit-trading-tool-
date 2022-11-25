import ccxt
import time
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0


config = ConfigParser()
config.read(r"C:\Users\user\Desktop\bybitapiconfig\configfile.ini")

         # definitions / order tickers.

t = 'BTCUSDT' 
t2 = 'ETHUSDT' 
t3 = 'CHZUSDT'
t4 = 'BCHUSDT'
t5 = 'DOTUSDT'  # strings for order ticker
t6 = 'KNCUSDT'
t7 = '1INCHUSDT'
t8 = 'AAVEUSDT' 
t9 = 'SOLUSDT'
t10 = 'MATICUSDT'

# list for all defined tickers
ticker_list = [t,t2,t3,t4,t5,t6,t7,t8,t9,t10]

{
'contract': True,
'settle': 'USDT',
}
usd = 100
order_params = {'timeInForce': 'postOnly'} # parameters for when orders are made
# config:
config_xpkey = config.get('bybit_API_main', 'xpkey')
config_xpsecret = config.get('bybit_API_secret', 'xpsecret')

# initialize exchange
exchange = ccxt.bybit ({ 
    'enableRateLimit': True, 
    'apiKey': config_xpkey, 
    'secret': config_xpsecret, 
     })

# function to retrieve bid and ask from specified ticker orderbook
def get_bid_ask(ticker):
    ob = exchange.fetch_order_book(ticker)

    bid = ob['bids'][0] [0]
    ask = ob['asks'][0] [0]
    
    return bid, ask


#array list for specified tickers / inputing into the function for bid/ask 

bid_list = []

for i in ticker_list:
    bid_list.append(get_bid_ask(i)[0])
    
order_position_size = usd / 10 

for i in range(len(ticker_list)):
    exchange.createLimitBuyOrder(ticker_list[int(i)], order_position_size, bid_list[int(i)])
    time.sleep(0.5)

