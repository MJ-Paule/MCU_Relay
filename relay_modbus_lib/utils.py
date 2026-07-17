'''
    Generall utilities for Relay Modbus library

'''

# Utility function for the relay_modbus_lib package to display HEX-Data in a human-readable format
#--------------------------------
def _hex_dump(data:bytes) -> str:
    return " ".join(f"{b:02x}" for b in data)


# Utility function to change integer to big-endian bytes
#--------------------------------
def _u16_be(x: int) -> bytes:
    return bytes([(x >> 8) & 0xFF, x & 0xFF])


# Utility function to calculate CRC16 for ModBus RTU, returns integer value
#--------------------------------
def _crc16_modbus(data: bytes) -> int:                      
    """
    CRC16/MODBUS: init=0xFFFF, poly=0xA001, output little-endian in frame.
    """
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc & 0xFFFF


# Utility function to calculate CRC16 for ModBus RTU, returns byte value
#--------------------------------
def _crc16_modbus_bytes(data: bytes) -> bytes:
    return _crc16_modbus(data).to_bytes(2,"little")


