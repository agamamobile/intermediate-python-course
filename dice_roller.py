import random
dice_rolls = 2
def main():
  dice_sum = 0
  for i in range(0, dice_rolls):
    die = random.randint(1, 6)
    print(f'You rolled a {die}')
    dice_sum += die
  print(f'You rolled total {dice_sum}')
if __name__== "__main__":
  main()