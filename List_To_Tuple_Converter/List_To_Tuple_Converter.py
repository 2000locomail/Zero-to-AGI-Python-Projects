def convert_collection_stream():
    user_data_list = []
    for i in range (1,4):
        item = input(f"Enter element {i}: ").strip()
        user_data_list.append(item)
    final_tuple = tuple(user_data_list)
    print(f"\n Final Collection (Tuple Format): {final_tuple}")
    print(f"Verification Type: {type(final_tuple)}")
if __name__ == '__main__':
    convert_collection_stream()