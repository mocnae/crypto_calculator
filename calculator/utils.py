from pybit import usdt_perpetual, spot

session_unauth = spot.HTTP(
        endpoint="https://api.bybit.com"
)
USDT = 'USDT'
counter = 0


def get_currency(base: str) -> float:
    if base == USDT:
        return 1
    else:
        curr = session_unauth.latest_information_for_symbol(symbol=base + USDT)['result']['lastPrice']
    return float(curr)


def calculatePairs(basec, quotec) -> float:
    base = get_currency(basec)
    quote = get_currency(quotec)
    return base / quote


def upload_currencys():
    base = set()
    quote = set()
    for res in session_unauth.query_symbol()['result']:
        # print(res)
        base.add(res['baseCurrency'])
        quote.add(res['quoteCurrency'])
    base.union(quote)
    base.add('USDT')
    base = list(base)
    base.sort(key=lambda x: ord(x[0]))
    costs = [get_currency(name) for name in base]
    res = [{name: cost} for name, cost in zip(base, costs)]
    return res
