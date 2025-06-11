from Dashboard.utils.serializer import user_details_serialize

def create_user_detials(User, user_Data):
    try:
        serializer = user_details_serialize(data=user_Data)
        print(f'here serializer {serializer.is_valid()}')
        if serializer.is_valid():
            serializer.save(user=User)  # ✅ pass user
            print(serializer)
            return True
        print(serializer.errors)
        return serializer.errors
    except Exception as e:
        print(e)
        return {"error": str(e)}  # ✅ return string not raw exception
