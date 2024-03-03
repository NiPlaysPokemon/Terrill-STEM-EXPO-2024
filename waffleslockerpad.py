import argparse


def open_locker(pizza):
    if pizza.password=='1234':
        print('open locker')
    else:
        print('no')


def close_locker(pizza):
    if pizza.password=='1234':
        print('close locker')
    else:
        print('no')



def run(sauce):
    if sauce.direction=='open':
        open_locker(sauce)
    else:
        close_locker(sauce)



if __name__ == "__main__":
   crust=argparse.ArgumentParser()
   crust.add_argument('--password')
   crust.add_argument('--direction')
   cheese=crust.parse_args()
   run(cheese)
