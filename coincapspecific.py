import requests
import json
convert='USD'

listings_url='https://api.coinmarketcap.com/v2/listings'
url_end='?structure=array&convert='+convert
request=requests.get(listings_url)
results=request.json()


data=results['data']
ticker_url_pairs = {}
for currency in data:
    symbol=currency['symbol']
    url=currency['id']
    ticker_url_pairs[symbol] = url
#print(ticker_url_pairs)

while True:
    print()
    choice=input('enter the ticker symbol of a cryptocurrency: ')
    choice=choice.upper()

    ticker_url='https://api.coinmarketcap.com/v2/ticker/'+str(ticker_url_pairs[choice])+'/'+url_end
    #print(ticker_url)
    request=requests.get(ticker_url)
    results=request.json()
    #print(json.dumps(results,sort_keys=True,indent=4))

    currency=results['data'][0]

    rank=currency['rank']
    name=currency['name']
    symbol=currency['symbol']

    circulating_supply=int(currency['circulating_supply'])
    total_supply=int(currency['total_supply'])

    quotes=currency['quotes'][convert]
    market_cap=quotes['market_cap']
    hour_change=quotes['percent_change_1h']
    day_change=quotes['percent_change_24h']
    week_change=quotes['percent_change_7d']
    price=quotes['price']
    volume=quotes['volume_24h']

    volume_string='{:,}'.format(volume)
    market_cap_string='{:,}'.format(market_cap)
    circulating_supply_string='{:,}'.format(circulating_supply)
    total_supply_string='{:,}'.format(total_supply)

    print(str(rank)+': '+name+' ('+symbol+')')
    print('Market değeri: \t\t'+market_cap_string)
    print('Fiyat: \t\t\t'+str(price))
    print('24 saatlik hacim: \t'+volume_string)
    print('Saatlik değişim: \t'+str(hour_change)+ '%')
    print('Günlük değişim: \t'+str(day_change)+ '%')
    print('Haftalık değişim: \t'+str(week_change)+ '%')
    print('Toplam arz: \t\t'+total_supply_string)
    print('Dolaşan arz: \t\t'+circulating_supply_string)
    print('Dolaşımdaki paraların yüzdesi:  '+str(int(circulating_supply/total_supply*100)))
    print()
    choice=input('Tekrar(e/h)?')
    if choice=='h':
        break
