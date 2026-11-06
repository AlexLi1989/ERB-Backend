import re

def main():
  exp = input("Please enter expression: ")
  # check for alphabets
  if re.search(r'[a-zA-Z]',exp):
    return print("Expression cannot contain alphabets!")
  exp_list = input_to_list(exp)
  try:
    while has_operator(exp_list):
      if "*" in exp_list or "/" in exp_list:
        if "*" in exp_list and "/" in exp_list:
          index = exp_list.index("*") if exp_list.index("*") < exp_list.index("/") else exp_list.index("/")
          first_num = float(exp_list[index-1])
          second_num = float(exp_list[index+1])
          result = first_num * second_num if exp_list.index("*") < exp_list.index("/") else first_num / second_num
          exp_list[(index-1):(index+2)] = [f"{result:g}"]
        elif "*" in exp_list and not "/" in exp_list:
          index = exp_list.index("*")
          first_num = float(exp_list[index-1])
          second_num = float(exp_list[index+1])
          result = first_num * second_num
          exp_list[(index-1):(index+2)] = [f"{result:g}"]
        else:
          index = exp_list.index("/")
          first_num = float(exp_list[index-1])
          second_num = float(exp_list[index+1])
          result = first_num / second_num
          exp_list[(index-1):(index+2)] = [f"{result:g}"]
      elif "+" in exp_list or "-" in exp_list:
        if "+" in exp_list and "-" in exp_list:
          index = exp_list.index("+") if exp_list.index("+") < exp_list.index("-") else exp_list.index("-")
          first_num = float(exp_list[index-1])
          second_num = float(exp_list[index+1])
          result = first_num + second_num if exp_list.index("+") < exp_list.index("-") else first_num - second_num
          exp_list[(index-1):(index+2)] = [f"{result:g}"]
        elif "+" in exp_list and not "-" in exp_list:
          index = exp_list.index("+")
          first_num = float(exp_list[index-1])
          second_num = float(exp_list[index+1])
          result = first_num + second_num
          exp_list[(index-1):(index+2)] = [f"{result:g}"]
        else:
          index = exp_list.index("-")
          first_num = float(exp_list[index-1])
          second_num = float(exp_list[index+1])
          result = first_num - second_num
          exp_list[(index-1):(index+2)] = [f"{result:g}"]
  except ZeroDivisionError:
    return print("Cannot divide by zero!")
  except Exception as e:
    return print(f"Error: {e}")
  print("".join(exp_list))

#helper for checking operator exists
def has_operator(list):
  operators = ["+","-","*","/"]
  if any(operator in list for operator in operators):
    return True
  return False

#helper for processing input
def input_to_list(str):
  list = re.split(r'([+\-*/])',str.strip())
  # filter '' if first num is negative
  list = [e for e in list if e != '']
  # first num is negative case
  if list[0] == "-":
    list[0:2] = [f"-{list[1]}"]
  # other num is negative case
  for index,element in enumerate(list):
    if element in ["+","-","*","/"]:
      if list[(index+1)] == "-":
        list[(index+1):(index+3)] = [f"-{list[index+2]}"]
  return list

if __name__ == '__main__':
  main()
