import Data_template_pb2
import json

proto_message = Data_template_pb2.Person()
proto_message.age = 23
proto_message.first_name = "Tushar"
proto_message.last_name = "Deshmukh"
proto_message.is_profile_verified = True
phone = proto_message.phone_numbers
phone.append('9403100123')
phone.append('9423100123')

json_data = {
    "age" : 23,
    "first_name" : "Tushar",
    "last_name" : "Deshmukh",
    "is_profile_verified" : True,
    "phone_numbers" : ['9403100123', '9423100123']
}

with open("C:\\Users\\ItsTRD\\OneDrive\\Desktop\\Projects\\ProtoBuf\\PresentationProto\\Data\\protobuf_data.bin", "wb") as f:
    f.write(proto_message.SerializeToString())
with open("C:\\Users\\ItsTRD\\OneDrive\\Desktop\\Projects\\ProtoBuf\\PresentationProto\\Data\\json_data.json", "w") as f:
    json.dump(json_data, f)

