#if 4 == 4:
  #  age = 25
  #  print(age)
#else:
 #   name = "Mitchell"
   # print(name)

#if 4 == 4: # if false then it will ignore this code block,
  #  age = 25 # and it will check the "elif" section, if false
 #   print(age) # then it will check the "else" section.
#elif 3 == 3:
 #   hungry = True
  #  print(hungry)
#else:
  #  name = "Mitchell"
  #  print(name)

devs_money = 100
dev_can_play_smash = True

if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tornament!")
elif devs_money < 1 and dev_can_play_smash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")