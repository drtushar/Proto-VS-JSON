import Data_template_pb2
import json

with open("C:\\Users\\ItsTRD\\OneDrive\\Desktop\\Projects\\ProtoBuf\\PresentationProto\\Data\\json_data.json") as json_file:
    json_data = json.load(json_file)
    json_data["is_profile_verified"] = "True" # This will work! No schema checked, that is boolean can be assigned string!
    print("\nJSON has no schema enforcement applied!", end='\n\n')

with open("C:\\Users\\ItsTRD\\OneDrive\\Desktop\\Projects\\ProtoBuf\\PresentationProto\\Data\\protobuf_data.bin", "rb") as f:
    proto_message_read = Data_template_pb2.Person().FromString(f.read())
    proto_message_read.is_profile_verified = "True" # This will raise TypeError! hence schema is enforced on data!
    print("This statment will be never executed!")
