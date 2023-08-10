import struct

class Parser:
    def __init__(self, packed_format) -> None:
        self.packed_format = packed_format
        self.parser = struct
    def parse(self, data):
        self.data = data[:14]
        parsed_data = self.parser.unpack( self.packed_format, self.data)
        parsed_packet = {
            "header": parsed_data[0],
            "version": parsed_data[1],
            "length": parsed_data[2],
            "source": parsed_data[3],
            "destination": parsed_data[4]
        }
        return parsed_packet
    
    def __repr__(self) -> str:
        return f'{__class__}({self.packed_format})'