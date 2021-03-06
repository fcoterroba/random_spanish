# Random Spanish Information
## What is that?
This library is my first library created for Python (so sorry if there are any bugs).
With this library you will be able to obtain both names (for men and women) and Spanish surnames

## How can I install it?
Just install with: `pip install random-spanish` or `pip3 install random-spanish`

## How can I use it?
You've got two ways:
### Download the CSVs locally (Recommended)
I recommend you download and import the csv file locally, otherwise the library will load the CSV from my online hosting, which can slow down the speed of your program.
Just download the CSV here:
- [Mens](https://fcoterroba.com/wp-content/uploads/2022/04/hombres.csv)
- [Womens](https://fcoterroba.com/wp-content/uploads/2022/04/mujeres.csv)
- [Surnames](https://fcoterroba.com/wp-content/uploads/2022/04/apellidos.csv)

Then, import files to your project and pass it in the third parameter of each function (files' parameter)
```python
mens_csv = "./path/to/your/mans.csv"
surnames_csv = "./path/to/your/surnames.csv"

print(getRandomMaleName(2, True, ["men.csv", "apellidos.csv"])) # Return an array with two full names
```
### Use it without download CSV (Unrecommended)
If you prefer, you can ignore the third parameter and then the library will load the CSV from my online hosting and then continue working.
```python
print(getRandomMaleName(2, True)) # Return an array with two full names
```

## Documentation
In this library you've got three functions
### Get random male name
`getRandomMaleName` expects three optional parameters:
- **First one** expects a integer with the number of the names you need. Default is 1
    -  If you pass 1, function will return a string. Otherwise, It'll return an array of strings
-  **Second one** expects a boolean to return a full name or not. Default is False
    -  If you pass True, function will return a full name with name and surname. Otherwise It'll return just the name
-  **Third one** expects a array string with the path to the CSV. Default is my website host.
    - See the **Download the CSVs locally (Recommended)**  point for more info

### Get random female name
`getRandomFemaleName` expects three optional parameters:
- **First one** expects a integer with the number of the names you need. Default is 1
    -  If you pass 1, function will return a string. Otherwise, It'll return an array of strings
-  **Second one** expects a boolean to return a full name or not. Default is False
    -  If you pass True, function will return a full name with name and surname. Otherwise It'll return just the name
-  **Third one** expects a array string with the path to the CSV. Default is my website host.
    - See the **Download the CSVs locally (Recommended)**  point for more info

### Get random surname
`getRandomSurname` expects three optional parameters:
- **First one** expects a integer with the number of the surnames you need. Default is 1
    -  If you pass 1, function will return a string. Otherwise, It'll return an array of strings
-  **Second one** expects a boolean to return a pair of surnames or not. Default is False
    -  If you pass True, function will return a pairs of surnames as in Spain everybody got two surnames. Otherwise It'll return just one surname
-  **Third one** expects a array string with the path to the CSV. Default is my website host.
    - See the **Download the CSVs locally (Recommended)**  point for more info

---
Last test was done in Python 3.9.7
