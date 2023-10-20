def problem9():
  # Problem 9 ################################################################
  password = input("Enter a password: ")
  num_character = len(password)
  if num_character < 6:
    print("Password too short")
  elif password.isdigit():
    print("Weak password")
  elif password.isalpha():
    print("Moderate password.")
  else:
    print("Strong password")
