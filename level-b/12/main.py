from convert_currency import ConvertCurrency

api_key = ""
conv_curr = ConvertCurrency(api_key)
conv_curr.show_currencies()
print("\n")

#Exemplo de Uso
print(conv_curr.transform_currency("USD", 20, "BRL"))