import os

JSON_SIZE = os.stat("C:\\Users\\ItsTRD\\OneDrive\\Desktop\\Projects\\ProtoBuf\\PresentationProto\\Data\\json_data.json").st_size
print('\nSize of Json File :', JSON_SIZE, 'Bytes.', end='\n\n')
PROTO_SIZE = os.stat("C:\\Users\\ItsTRD\\OneDrive\\Desktop\\Projects\\ProtoBuf\\PresentationProto\\Data\\protobuf_data.bin").st_size
print('Size of Protobuf File :', PROTO_SIZE, 'Bytes.', end='\n\n')

print('Protobuf message is', int(100 - PROTO_SIZE/JSON_SIZE * 100), "% smaller compared to JSON message.", end='\n\n')
