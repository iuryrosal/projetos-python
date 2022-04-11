from requests import get

class ConvertCurrency:
    def __init__(self, api_key):
        self.url_base = "https://free.currconv.com"
        self.api_key = api_key
        self.currencies = self.get_currencies()
    
    def get_currencies(self):
        endpoint = f"/api/v7/currencies?apiKey={self.api_key}"
        url = self.url_base + endpoint
        data = get(url).json()["results"]
        data = list(data.values())
        return data

    def show_currencies(self):
        for currency in self.currencies:
            name = currency.get("currencyName", "")
            _id = currency.get("id", "")
            symbol = currency.get("currencySymbol", "")
            print(f"{_id} | {name} | {symbol}")
    
    def transform_currency(self, initial_currency, amount, end_currency):
        endpoint = f"/api/v7/convert?q={initial_currency}_{end_currency}"
        parameters = ["&compact=ultra", f"&apiKey={self.api_key}"]
        url = self.url_base + endpoint +\
            "".join([str(parameter) for parameter in parameters])
        data = get(url).json()
        if len(data) == 0:
            print("Moedas Inválidas")
            return
        rate = data[f"{initial_currency}_{end_currency}"]
        try:
            amount = float(amount)
        except:
            print("Quantidade Inválida.")
            return
        new_value = rate*amount
        return new_value
