from config_settings import config

from _class import Parser
# Определение формата пакета ЕГТС
packet_format = config.packet_format

# Чтение и распаковка данных пакета ЕГТС
def parse_egts_packet(data):
    parser = Parser(packet_format)
    return parser.parse(data)

# Пример использования парсера
egts_packet_data = b'\x45\x47\x54\x53\x01\x00\x0c\x00\x00\x00\x00\x00\x01\x02\x03\x04'
parsed_packet = parse_egts_packet(egts_packet_data)
print(parsed_packet)