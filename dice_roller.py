import random
def main():
  dice_sum = 0
  dice_rolls = int(input('how many dice to roll?'))
  dice_sides = int(input('how many sides?'))
  for i in range(0, dice_rolls):
    die = random.randint(1, dice_sides)
    if die == 1:
      print(f'You rolled a {die}. Failed')
    elif die == dice_sides:
      print(f'You rolled a {die}. Success')
    else:
      print(f'You rolled a {die}')
    dice_sum += die
  print(f'You rolled total {dice_sum}')
if __name__== "__main__":
  main()