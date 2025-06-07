import requests

def get_all_symbols(exchanges):
    """
    Get a list with all the symbols filtered by a given exchange.
    
    Valid exchanges: {'AMEX', 'OTC', 'NYSE', 'NASDAQ'}
    
    :param exchanges: a set which contains the exchanges you want to keep (all the rest will be ignored)
    :return: list of symbols
    """
    exchanges = {x.upper() for x in exchanges}
    data = requests.get('https://scanner.tradingview.com/america/scan').json()['data']
    
    symbols = []
    for dct in data:
        exchange, symbol = dct['s'].split(':')
        if exchange in exchanges:
            symbols.append(symbol)
    return symbols
    

symbols = get_all_symbols(exchanges={'NYSE', 'NASDAQ'})
print(len(symbols), symbols[:10])  # out: 7768 ['VNT', 'LXP/PC', 'USB/PR', 'NOVVU', 'RITM', 'PSTG', 'SMSI', 'MAQC', 'NX', 'TNC']
