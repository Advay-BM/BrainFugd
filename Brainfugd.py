# Start Date: 2/8/2024
"""
To Do:
1. Implement poly-cell mode
4. Make code readable
"""
import random
print("\t\t\t\t\t\t Welcome to BrainFugd")
print("\t\t\t\tA programming language for your gmd software\n")
help = 0
debug_mode = False
# Help
while help == 0:
  start = str(input("Type 'start' to begin: "))
  if start == 'start' :
    print("\nMake sure that you have familiarized yourself with the basics of BrainFugd before continuing.\n")
    print("Commands: \n\t'+' : Increment the value of the current cell by 1")
    print("\n\t'-' : Decrement the value of the current cell by 1(Values cannot be negative)")
    print("\n\t'>' : Move the current cell to the right by 1")
    print("\n\t'<' : Move the current cell to the left by 1")
    print("\n\t'.' : Print the value of the current cell along with the letter associated with it")
    print("\n\t',' : Take a number input and store it in the current cell")
    print("\n\t'[' : If the current cell is 0, skip all the commands until ']' is reached")
    print("\n\t']' : If the current cell is not 0, go back to the previous '['")
    print("\n\t'!' : Tells the program that the end of the command list has been reached")
    print("\n1. Notice that '[]' essentially creates a loop of the commands inside them until the selected cell's value is 0(Just, make sure that the code reaches 0 eventually or you will never get the output. You'll have to restart the entire program as well)")
    print("\n2. Always use '!' at the end of your code. You will get an error if you don't")
    print("\n3. In challenges that depend on inputs, an anticheat system will be used to enter random values. To further prevent cheating in such challenges, you need to be successful 3 times in a row to show that your code actually works and is not based on luck.")
    print("\n4. Make sure to only use the above characters or you will get an error")
    print("\n5. The currently selected call has an '^' below it. This is called the cell selector")
    print("\n6. Make sure to close a '[' with ']' and vice versa. Open brackets will give errors")
    print("\n7. Challenges will have character limits to encourage you think of the most optimal way to solve a problem. If you don't like that... suffer")
    print("\n8. This is a program recreating another programming language called BrainF***(Yes it actually exists go look it up)")
    print("\n9. I have given you certain tasks to complete using this programming language. You don't get rewards(naturally) but it will test your intelligence")
    print("\n10. With all that said, you can use use 'skip' to skip this message the next time you run the program")
    ask = str(input("Show examples? (You need to see and understand these atleast once)[y/n]: "))
    if ask == "y":
      print("\nExamples:\n")
      print("+++++.!\t Adds 5 to first cell and outputs 5 along with the E(the corresponding letter)")
      print("+>+>+!\t Adds 1 to the first 3 cells")
      print("+++[->++<]!\t Adds 3 to first cell. Then it subtracts 1 then and adds 2 to the next cell. It keeps doing this until the first cell is 0 and the second cell is 6. Notice how this essentially multiplies 3 with 2.\n")
    help = 1
    break
  elif start == "skip":
    help = 1
    break
  elif start == "debug_mode":
    print("\n Debug Mode Enabled...\n")
    debug_mode = True
    help = 1
  else:
    print("Please input 'start' to begin")
    help = 0
    continue
print("\n")

## The actual code
#Cheat codes: SCCSM, SCCRS, SCCSC

#Initialization
challenge_count = 0
challenge_passed = False
output = ""
input_code = ""
reveal_check = False
os = ""
c = -1
str_length = 0
c_limit = 0
loop_end = None
loop_start = None
output = ""
otpt = ""
r_value = 0
triple_trial = 0
dict = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
c5_list = [0,6,7,13,7,13,0,6,0,13]
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
cell_list = [c1,c2,c3,c4,c5,c6]
char_list = ["+","-","<",">","]","[",".",",","!"]
r_list = []
c_multiplier = 0
current_cell = cell_list[c_multiplier]
c_selector = "     "*c_multiplier
cells = "\t"+str(cell_list[0])+"    "+str(cell_list[1])+"    "+str(cell_list[2])+"    "+str(cell_list[3])+"    "+str(cell_list[4])+"    "+str(cell_list[5])+"\n\t"+c_selector+"^"

#Functions
def updater():
  global c_multiplier, c_selector, cells, current_cell
  current_cell = cell_list[c_multiplier]
  c_selector = "     "*c_multiplier
  cells = "\t"+str(cell_list[0])+"    "+str(cell_list[1])+"    "+str(cell_list[2])+"    "+str(cell_list[3])+"    "+str(cell_list[4])+"    "+str(cell_list[5])+"\n\t"+c_selector+"^"

def Reveal():
  global challenge_count, reveal_check
  if challenge_count == 0:
    print("\nSolution: +++.!")
  elif challenge_count == 1:
    print("\nSolution: +++++[->++++++++<]>.!")
  elif challenge_count == 2:
    print("\nSolution: ,[->++<]>.!")
  elif challenge_count == 3:
    print("\nSolution: ,>,[->+<]>.!")
  elif challenge_count == 4:
    print("\nSolution: +>>,>,[[-<]>>]>>[>]>>+<<<[<]<<.!")
  # elif challenge_count == 5:
  #   print("\nSolution: ")
  elif challenge_count > 5:
    print("No solution to reveal.")
  reveal_check = True

def code():
  global input_code, cells, challenge_count, triple_trial
  print("\n")
  print(cells)
  input_code = str(input("\nC:\Brainfugd> "))
  if input_code == "SCCSM":
    print("\nSandbox Mode enabled!\n")
    challenge_count = 7
  elif input_code == "SCCRS":
    print("Revealing solution...")
    Reveal()
  elif input_code == "SCCSC":
    print(f"\nChallenge {challenge_count+1} skipped...\n")
    challenge_count += 1
    triple_trial = 0

def reset_cells():
  global cell_list, input_code, c_selector, c_multiplier, c_selector, cells
  input_code = ""
  c_multiplier = 0
  cell_list[0],cell_list[1],cell_list[2],cell_list[3],cell_list[4],cell_list[5]=0,0,0,0,0,0
  cells = "\t"+str(cell_list[0])+"    "+str(cell_list[1])+"    "+str(cell_list[2])+"    "+str(cell_list[3])+"    "+str(cell_list[4])+"    "+str(cell_list[5])+"\n\t"+c_selector+"^"
  updater()

def translator(inp):
  global cells, cell_list, c_multiplier, current_cell, c, str_length, loop_end, loop_start, otpt, os, r_value, r_list, c5_list,c_limit
  otpt=""
  os = ""
  while c <= str_length:
    if debug_mode == True:
      print(cells)
      input("Press enter to continue")
    c+=1
    updater()
    if inp[c] not in char_list:
      print(f"\nError 02: Invalid character {str(inp[c])}")
      break
    str_length = len(inp)-1
    if str_length > c_limit:
      if str_length > 2147483646 :
        print(f"n Error 01: Character limit exceeded at wait what... how did you do that?")      
      print(f"\n Error 01: Character limit exceeded at {inp[c_limit]}")
      c=-1
      break
    if "!" not in inp:
      print("\nError 05: Missing '!'")
      c=-1
      break
    if inp[c] == "+":
      cell_list[c_multiplier] += 1
      updater()
    elif inp[c] == "-":
      if cell_list[c_multiplier] == 0:
        cell_list[c_multiplier] = 0
      else:
        cell_list[c_multiplier] -= 1
      updater()
    elif inp[c] == ">":
      if c_multiplier == 5:
        c_multiplier = 0
        updater()
      else:
        c_multiplier += 1
        updater()
    elif inp[c] == "<":
      if c_multiplier == 0:
        c_multiplier = 5
        updater()
      else:
        c_multiplier -= 1
        updater()
    elif inp[c] == "[":
      updater()
      loop_start = c
      nest_counter=0
      for i in range(loop_start,len(inp)-1):
        if inp[i] == "[":
          nest_counter+=1
        elif inp[i] == "]":
          nest_counter-=1
          if nest_counter == 0:
            loop_end=i
            break
      if loop_end == None:
        print("\nError 04: Missing ']'")
        c=-1
        break
      if current_cell != 0:
        continue
      elif current_cell == 0:
        c = loop_end
        continue
    elif inp[c] == "]":
      updater()
      loop_end = c
      nest_counter = 0
      for i in range(loop_end, 0, -1):
        if inp[i] == "]":
          nest_counter+=1
        elif inp[i] == "[":
          nest_counter-=1
          if nest_counter == 0:
            loop_start=i
            break
      if loop_start == None:
        print("\nError 03: Missing '['")
        c=-1
        break
      else:
        if current_cell == 0:
          continue
        else:
          c = loop_start-1
          continue
    elif inp[c] == ".":
      updater()
      if current_cell > 26:
        os = ""
      else:
        os = os+dict[current_cell]
      otpt=str(current_cell)+"\t"+os
    elif inp[c] == ",":
      updater()
      if challenge_count <=1:
        print("\nInput command cannot be used for this challenge.\n")
        break
      if challenge_count <= 5:
        if challenge_count == 4:
          if triple_trial == 2 and r_list != []:
            r_value = r_list[0]
            r_list.append(r_value)
            print(f"\nAnticheat, entering random value...\n Value: {str(r_value)}({dict[r_value]})\n")
            cell_list[c_multiplier] = r_value
          else:
            r_value = random.randint(c5_list[0],c5_list[1])
            r_list.append(r_value)
            del c5_list[0:2]
            print(f"\nAnticheat, entering random value...\n Value: {str(r_value)}({dict[r_value]})\n")
            cell_list[c_multiplier] = r_value
        else:
          r_value = random.randint(0,13)
          r_list.append(r_value)
          print(f"\nAnticheat, entering random value...\n Value: {str(r_value)}({dict[r_value]})\n")
          cell_list[c_multiplier] = r_value
      else:
        comma = int(input("\nEnter a value: "))
        if type(comma) != type(-69) or comma<0:
          print("\nError 06: Input can only be of type 'whole number'")
          c=-1
          break
        else:
          cell_list[c_multiplier] = comma
      updater()
    elif inp[c] == "!":
      c=-1
      break
  print(f"\nOutput: {otpt}\n")
  print(cells)
  return otpt

def answer_check(cc,o):
  global r_value, r_list
  if cc == 0:
    if o == "3\tC":
      return True
    else:
      return False
  if cc == 1:
    if o == "40\t":
      return True
    else:
      return False
  if cc == 2:
    if o == str(2*r_list[0])+"\t"+dict[2*r_list[0]]:
      r_list = []
      return True
    else:
      r_list = []
      return False
  if cc == 3:
    if o == str(r_list[0]+r_list[1])+"\t"+dict[r_list[0]+r_list[1]]:
      r_list = []
      return True
    else:
      r_list = []
      return False
  if cc == 4:
    if r_list[0] > r_list[1]:
      if o == str(r_list[0]-r_list[1])+"\t"+dict[r_list[0]-r_list[1]]:
        r_list = []
        return True
      else:
        r_list = []
        return False
    elif r_list[0] < r_list[1]:
      if o == str(r_list[1]-r_list[0])+"\t"+dict[r_list[1]-r_list[0]]:
        r_list = []
        return True
      else:
        r_list = []
        return False
    elif r_list[0] == r_list[1]:
      if o == "0\t ":
        r_list = []
        return True
      else:
        r_list = []
        return False
  if cc == 5:
    if (r_list[0]+1)**r_list[1]<=26:
      d = str(dict[(r_list[0]+1)**r_list[1]])
    else:
      d = ""
    if o == f"{str((r_list[0]+1)**r_list[1])}\t{d}":
      r_list = []
      return True
    else:
      r_list = []
      return False
#Main Loop
while True:
  if challenge_count == 0:
    print("\nChallenge 1\n")
    print("Print 3\n")
    print("Character Limit: 25")
    while challenge_count == 0:
      c_limit = 25
      code()
      if challenge_count>0:
        break
      if reveal_check == True:
        reveal_check == False
        continue
      output = translator(input_code)
      challenge_passed = answer_check(challenge_count,output)
      if challenge_passed == True:
        challenge_count += 1
        print("\nChallenge 1 Passed!\n")
      else:
        print("\nChallenge Failed\n")
        reset_cells()
        continue
  
  if challenge_count == 1:
    reset_cells()
    print("\nChallenge 2\n\nPrint 40\n")
    print("Character Limit: 40\n")
    while challenge_count == 1:
      c_limit = 40
      code()
      if challenge_count>1:
        break
      if reveal_check == True:
        reveal_check == False
        continue
      output = translator(input_code)
      challenge_passed = answer_check(challenge_count,output)
      if challenge_passed == True:
        challenge_count += 1
        print("\nChallenge 2 Passed!\n")
        reset_cells()
      else:
        print("\nChallenge Failed\n")
        reset_cells()
        continue
  
  if challenge_count == 2:
    reset_cells()
    print("\nChallenge 3\n\nTake a number as input and ouput double that number.\n")
    print("Character Limit: 30\n")
    while challenge_count == 2:
      c_limit = 30
      code()
      if challenge_count>2:
        break
      if reveal_check == True:
        reveal_check == False
        continue
      output = translator(input_code)
      challenge_passed = answer_check(challenge_count,output)
      if challenge_passed == True:
        triple_trial+=1
        if triple_trial == 1:
          print("\nChallenge Success 1/3\n")
        if triple_trial == 2:
          print("\nChallenge Success 2/3\n")
        if triple_trial == 3:
          print("\nChallenge Success 3/3\n")
        reset_cells()
      else:
        print("\nChallenge Failed\n")
        reset_cells()
        triple_trial = 0
        continue
      if triple_trial == 3:
        print("\nChallenge 3 passed!\n")
        print("\nHint: Typing 'debug_mode' when you run the code will allow you to go step by step with the execution of your code.\n")
        challenge_count += 1
        triple_trial = 0
        reset_cells()
        break
      else:
        continue

  
  if challenge_count == 3:
    reset_cells()
    print("\nChallenge 4\n\nTake 2 numbers as input and ouput their sum.\n")
    print("Character Limit: 30\n")
    while challenge_count == 3:
      c_limit = 30
      code()
      if challenge_count>3:
        break
      if reveal_check == True:
        reveal_check == False
        continue
      output = translator(input_code)
      challenge_passed = answer_check(challenge_count,output)
      if challenge_passed == True:
        triple_trial+=1
        if triple_trial == 1:
          print("\nChallenge Success 1/3\n")
        if triple_trial == 2:
          print("\nChallenge Success 2/3\n")
        if triple_trial == 3:
          print("\nChallenge Success 3/3\n")
        reset_cells()
      else:
        print("\nChallenge Failed\n")
        reset_cells()
        triple_trial = 0
        continue
      if triple_trial == 3:
        print("Challenge 4 passed!")
        print("\n Hint: Typing SCCSM in the interpreter at any time will enter sandbox mode. You can no longer re-enter challenge mode after entering into sandbox mode.\n")
        challenge_count += 1
        triple_trial = 0
        reset_cells()
        break
      else:
        continue
  
  if challenge_count == 4:
    reset_cells()
    print("\nChallenge 5\n\nTake 2 numbers as input and ouput the difference of the greater number from the smaller one.\n")
    print("Character Limit: 50\n")
    while challenge_count == 4:
      c_limit = 50
      code()
      if challenge_count>4:
        break
      if reveal_check == True:
        reveal_check == False
        continue
      output = translator(input_code)
      challenge_passed = answer_check(challenge_count,output)
      if challenge_passed == True:
        triple_trial+=1
        if triple_trial == 1:
          print("\nChallenge Success 1/3\n")
        if triple_trial == 2:
          print("\nChallenge Success 2/3\n")
        if triple_trial == 3:
          print("\nChallenge Success 3/3\n")
        reset_cells()
      else:
        c5_list = [0,6,7,13,7,13,0,6,0,13]
        print("\nChallenge Failed\n")
        reset_cells()
        triple_trial = 0
        continue
      if triple_trial == 3:
        print("Challenge 5 passed!")
        print("\nHint: Using SCCRS in the interpreter will allow you to reveal the optimal solution to a challenge while using SCCSC will skip non-optional challenges entirely.\n")
        challenge_count += 1
        triple_trial = 0
        reset_cells()
        break
      else:
        continue
  
  if challenge_count == 5:
    if str(input("Attempt optional challenge?[y/n]")) == "y":
      reset_cells()
      print("\nChallenge 6\n\nTake 2 numbers as input and output the value of (1+x)^n where x is the first input and n is the second input.\n")
      print("Hint: Just add 1 to the first input and then all you have to do is square it.\n")
      while challenge_count == 5:
        code()
        if challenge_count>5:
          break
        if reveal_check == True:
          reveal_check == False
          continue
        output = translator(input_code)
        challenge_passed = answer_check(challenge_count,output)
        if challenge_passed == True:
          triple_trial+=1
          if triple_trial == 1:
            print("\nChallenge Success 1/3\n")
          if triple_trial == 2:
            print("\nChallenge Success 2/3\n")
          if triple_trial == 3:
            print("\nChallenge Success 3/3\n")
          reset_cells()
        else:
          print("\nChallenge Failed\n")
          reset_cells()
          triple_trial = 0
          continue
        if triple_trial == 3:
          print("Challenge 6 passed!")
          challenge_count += 1
          triple_trial = 0
          reset_cells()
          break
        else:
          continue
  if challenge_count>5:
    code()
    c_limit = 2147483646
    if reveal_check == True:
      reveal_check == False
      continue
    if input_code == "quit" or input_code == "q":
      break
    output = translator(input_code)
    reset_cells()
    continue