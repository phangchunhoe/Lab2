def display_main_menu():
    print("\nET0735 Lab 2 \nExercise 2 \nWritten by: Phang Chun Hoe\n")

def get_user_input():
    user_input_float = []
    valid_value = False
    
    while not valid_value:
        try:
            user_input_string = input("Please enter your values (for eg 5, 3, etc): ").split(", ")
            user_input_float = [float(user_input) for user_input in user_input_string]
            valid_value = True
        
        except ValueError:
            print("\nPlease enter a valid value!")

    return user_input_float

def calc_average(user_inputs):
    total = 0
    for user_input in user_inputs:
        total += user_input
    
    average = total / len(user_inputs)
    return average

def find_min_max(sorted_user_inputs):
    min_max_array = [sorted_user_inputs[0], sorted_user_inputs[len(sorted_user_inputs) - 1]]

    return min_max_array


def sort_temperature(user_inputs):
    user_inputs.sort()
    return user_inputs


def calc_median_temperature(sorted_user_inputs):
    median = 0.0
    if len(sorted_user_inputs) % 2 == 1:
        median = sorted_user_inputs[int(len(sorted_user_inputs) // 2)]
    else:
        median = (sorted_user_inputs[int(len(sorted_user_inputs) / 2)] + sorted_user_inputs[int(len(sorted_user_inputs) / 2 - 1)]) / 2
    return median

def main():
    display_main_menu()
    sorted_user_inputs = sort_temperature(get_user_input())

    min_max_array = find_min_max(sorted_user_inputs)
    print(f"""
The inputs recieved were: {sorted_user_inputs}
          
The average of all inputs is: {calc_average(sorted_user_inputs)}
The median of all inputs is: {calc_median_temperature(sorted_user_inputs)}
The minimum value is: {min_max_array[0]}
The maximum value is: {min_max_array[1]}


""")

if __name__ == "__main__":
    main()