import json
import requests
while True:
    ticker_url='https://api.coinmarketcap.com/v2/ticker/?structure=array'

    limit=100
    start=1
    sort='rank'
    convert='USD'
    currency_symbol='$'
    choice=input('Özel parametre girmek ister misiniz(e/h)?')
    if choice=='e':
        limit=input('Limit?: ')
        start=input('Başlangıç numarası?: ')
        sort=input('Neye göre sıralamak istersiniz?: ')
        convert=input('Paranız nedir?: ')
        ticker_url+='&limit='+str(limit)+'&sort='+sort+'&start='+str(start)+'&convert='+convert
        currency_symbol=convert+': '
        print()
    request=requests.get(ticker_url)
    result=request.json()

    #print(json.dumps(result,sort_keys=True,indent=4))
    data=result['data']
    for currency in data:
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
        print('Market değeri: \t\t'+currency_symbol+market_cap_string)
        print('Fiyat: \t\t\t'+currency_symbol+str(price))
        print('24 saatlik hacim: \t'+currency_symbol+volume_string)
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
