from lesson19.proxy.csv_reader import CsvReader
from lesson19.proxy.csv_proxy_reader import CsvProxyReader

csv_reader = CsvReader('users.csv')
reader = CsvProxyReader(csv_reader)
print(reader.read())
print(reader.read())