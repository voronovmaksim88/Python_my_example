# https://pymodbus.readthedocs.io/en/latest/readme.html#example-code

from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('192.168.1.213')
client.connect()
result = client.read_discrete_inputs(address=0, slave=1)
print("SMH4 answered", result.bits[0])
client.close()
