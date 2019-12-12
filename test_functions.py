import Calc
import Driver

# first test: decin
my_str = "23 * 9 "
result = Calc.decin(my_str)
assert result == "23" , "decin error"

my_str = "983 ! * 10"
result = Calc.decin(my_str)
assert result == "983", "decin error"

# second test: isvalid_exp
my_str = "9 &&& )"
result = Driver.isvalid_exp(my_str)
assert result == False, "isvalid_exp error"

my_str= " 8 * 9 / 2"
result = Driver.isvalid_exp(my_str)
assert result == True, "isvalid_exp error"
