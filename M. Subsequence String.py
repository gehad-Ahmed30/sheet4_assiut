def calculate_sequence(string_input):

    string_constant="hello"
    length=len(string_constant)
    cal_index=0

    for char in string_input:
        if char==string_constant[cal_index]:      #h==h (cal_index=1) ..............
            cal_index+=1
            if length==cal_index:
                return "YES"
    return "NO"

string_input=input().strip()
print(calculate_sequence(string_input))




