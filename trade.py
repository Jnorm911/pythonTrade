from kucoin.client import Trade
from market import *
from constant import *

client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)

# Trade
#order_id = client.create_market_order('BTC-USDT', 'sell', size='.001')
