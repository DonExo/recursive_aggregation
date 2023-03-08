lst = [
  {
    "country": "US",
    "city": "Boston",
    "currency": "USD",
    "amount": 100
  },
  {
    "country": "FR",
    "city": "Paris",
    "currency": "EUR",
    "amount": 20
  },
  {
    "country": "FR",
    "city": "Lyon",
    "currency": "EUR",
    "amount": 11.4
  },
  {  # extra item
    "country": "FR",
    "city": "Lyon",
    "currency": "EUR",
    "amount": 8.5
  },
  {
    "country": "ES",
    "city": "Madrid",
    "currency": "EUR",
    "amount": 8.9
  },
  {
    "country": "UK",
    "city": "London",
    "currency": "GBP",
    "amount": 12.2
  },
  {
    "country": "UK",
    "city": "London",
    "currency": "FBP",
    "amount": 10.9
  }
]


def aggregate(data, key_list):
  if len(key_list) == 1:
    # base case: only one key left in the list
    result = {}
    for item in data:
      key = item[key_list[0]]
      amount = item['amount']
      if key in result:
        result[key]['amount'] += amount
      else:
        result[key] = {'amount': amount}
    return result
  else:
    # recursive case: there are multiple keys left in the list
    result = {}
    sub_data = {}
    for item in data:
      key = item[key_list[0]]
      if key not in sub_data:
        sub_data[key] = []
      sub_data[key].append(item)
    for sub_key in sub_data:
      sub_result = aggregate(sub_data[sub_key], key_list[1:])
      result[sub_key] = sub_result
    return result


result = aggregate(lst, ["currency", "country", "city"])
print(result)

result = aggregate(lst, ["city"])
print(result)
