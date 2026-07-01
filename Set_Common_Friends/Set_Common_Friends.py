def find_common_friends():
    group_a = {"Amit", "Rahul", "Satyam", "Vijay"}
    group_b = {"Satyam", "Vikas", "Rahul", "Anand"}
    common_friends = group_a.intersection(group_b)
    print(f"The common friends between Group A and Group B is: {common_friends}")

if __name__ == "__main__":
    find_common_friends()