from Dashboard.utils.serializer import user_details_serialize

def create_user_detials(User,user_Data):
    try:
        serializer = user_details_serialize(data = user_Data)
        if serializer.is_valid():
            serializer.save(user= User)
            return True
        return serializer.error_messages
    except Exception as e:
        return e