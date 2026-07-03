
# Utility functions for the relay_modbus_lib package to display HEX-Data in a human-readable format
#--------------------------------

def hex_dump(data:bytes) -> str:
    return " ".join(f"{b:02x}" for b in data)

