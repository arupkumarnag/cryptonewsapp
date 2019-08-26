from django.shortcuts import render

def home(request):
    import requests
    import json 

    #Crypto Price Data
    price_request = requests.get(#Put your API KEY HERE)
    price = json.loads(price_request.content)

    #Crypto News View
    api_request = requests.get(#Put your API KEY HERE)
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
    if request.method == 'POST':
        import requests
        import json 
    
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(#Put your API KEY HERE)
        crypto = json.loads(crypto_request.content)

        return render(request, 'prices.html', {'quote':quote, 'crypto': crypto})

    else:
        return render(request, 'prices.html')
        



