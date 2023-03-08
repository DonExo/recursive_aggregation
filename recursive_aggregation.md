# Recursive Aggregation

## Build a recursive aggregation

Given a list of inputs, e.g. the total amount of sales by an organizations store-front
locations, calculate the sum of all sales according to a key-list. The key-list may
contain any of the object properties (except for `amount`) and may contain each key
at most once. The result should be an object structured according to the key-list
containing the sum of the `amount` property of all objects falling into the given
category. Some examples of key lists are:
- `["currency", "city"]`
- `["country", "city", "currency"]`
- `["city"]`

Notes:
- ask any question you might have, conceptually, or related to code (i'm your peer in this excercise)
- do not focus on json file-reading or command line interfaces (hard-code the necessary overhead)
- google is your friend - the goal is simulate a realistic work-day experience

### Example

This input file:

```input.json
[
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
```

We should be able to call:

```
   # pseudo
   aggregate(input_data, ["currency", "country", "city"])
```

Which should return

```json
{
   "EUR":{
      "ES":{
         "Madrid":{
            "amount":8.9
         }
      },
      "FR":{
         "Lyon":{
            "amount":11.4
         },
         "Paris":{
            "amount":20
         }
      }
   },
   "FBP":{
      "UK":{
         "London":{
            "amount":10.9
         }
      }
   },
   "GBP":{
      "UK":{
         "London":{
            "amount":12.2
         }
      }
   },
   "USD":{
      "US":{
         "Boston":{
            "amount":100
         }
      }
   }
}
```

We should also be able to call

```
   # pseudo
   aggregate(input_data, ["city"])
```

Which should return

```json
{
   "Madrid":{
     "amount": 8.9
   },
   "Lyon":{
     "amount": 11.4
   },
   "Paris":{
     "amount": 20
   },
   "London":{
     "amount": 23.1
   },
   "Boston":{
     "amount": 100
   },
}
```

As visible, the result data should be nested according to the number of parameters provided.

## Additional Tasks

1. Change the code to have an additional parameter defining which property gets summed up: `aggregate(input_data, ["currency", "country"], "amount")`
2. Change the code to allow an arbitrary aggregation function: e.g. `aggregate(input_data, ["currency", "country"], "amount", "avg|sum|min")`
3. Write a unit test for your function

