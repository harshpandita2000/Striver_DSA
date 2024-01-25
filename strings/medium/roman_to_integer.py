def roman_to_integer(s):
        roman= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
            #XI 
            #IX
        for i in reversed(s):
            current_value = roman[i]  #1 #10

            if current_value >= prev_value:
                result += current_value # 1+10=11
            else:
                result -= current_value

            prev_value = current_value #1 #10

        return result

s = "IX"
print(roman_to_integer(s))