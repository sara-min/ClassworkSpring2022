print("This is the blood_calculator module"
      " and python calls it {}".format(__name__))
# python automatically concatenates two strings


def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options: ")
        print("1-HDL")
        print("2-LDL")
        print("3-Total Cholesterol")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            totalCholesterol_driver()
    return


def accept_input(test_name):
    entry = input("Enter the {} test result:".format(test_name))
    return int(entry)


def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(
        test_value, test_name, test_class)
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
    elif 130 <= LDL_value < 160:
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


def check_cholesterol(chol_value):
    if chol_value < 200:
        answer = "Normal"
    elif 200 <= chol_value < 240:
        answer = "Borderline High"
    else:
        answer = "High"
    return answer


def totalCholesterol_driver():
    chol_value = accept_input("Total Cholesterol")
    classification = check_cholesterol(chol_value)
    print_result("Total Cholesterol", chol_value, classification)


def function(a, b, x):
    m = slope(a, b)
    print("slope: " + str(m))
    c = y_intercept(a, m)
    print("y-intercept: "+str(c))
    print(m*x + c)
    return m*x + c


def slope(a, b):
    dy = b[1] - a[1]
    dx = b[0] - a[0]
    return dy/dx


def y_intercept(a, m):
    c = a[1] - m*a[0]
    return c


if __name__ == "__main__":
    interface()
    a = (1,1)
    b = (4,9)
    x=5
    function(a, b, x)
    # if you are importing blood calculator as a modeule, skip this line
