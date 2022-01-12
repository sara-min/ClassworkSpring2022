def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options: ")
        print("1-HDL")
        print("2-LDL")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()

    return
    
def accept_input(test_name):
    entry = input ("Enter the {} test result:".format(test_name))
    return int(entry)

def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
    print(out_string)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        answer = "Normal"
    elif 60 > HDL_value >= 40:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer

def HDL_driver():
    HDL_value = accept_input("HDL")
    classification = check_HDL(HDL_value)
    print_result("HDL", HDL_value, classification)

def check_LDL(LDL_value):
    if LDL_value < 130:
        answer = "Normal"
    elif 130 <= LDL_value <160:
        answer = "Borderline High"
    elif 160 <= LDL_value < 190:
        answer = "High"
    else:
        answer = "Very High"
    return answer

def LDL_driver():
    LDL_value = accept_input("LDL")
    classification = check_LDL(LDL_value)
    print_result("LDL", LDL_value, classification)

interface()
