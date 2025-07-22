from random import randint

def main():
    lvl = get_level()
    generate_integer(int(lvl))

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
            else:
                pass
        except:
            pass

def generate_integer(level):
    i = 0
    ded_mark = 0
    while i < 10:
        global error
        error = 0
        if level == 1:
            x = randint(1,9)
            y = randint(1,9)

            while True:
                try:
                    user_sol = int(input(f'{x} + {y} = '))
                    if user_sol == x + y:
                        i = i+1
                        break
                except:
                    if error < 3:
                        print("EEE")
                        error += 1
                        pass

                    else:
                        print(f'{x + y}')
                        ded_mark = ded_mark + 1
                        i = i+1
                        break


        elif level == 2:
            x = randint(10,99)
            y = randint(10,99)
            user_sol = input(f'{x} + {y} = ')
            if int(user_sol) == x + y:
                i = i+1
            else:
                while error < 3:
                    print("EEE")
                    error = error + 1

                if error == 3:
                    print(f'{x} + {y} = {x + y}')
                    ded_mark = ded_mark + 1
                    i = i+ 1

        else:
            x = randint(100,999)
            y = randint(100,999)
            user_sol = int(input(f'{x} + {y} = '))
            if user_sol == x + y:
                i = i+1
            else:
                while error < 3:
                    print("EEE")
                    error = error + 1

                if error == 3:
                    print(f'{x} + {y} = {x + y}')
                    ded_mark = ded_mark + 1
                    i = i + 1

    print("Score: ", 10 - ded_mark)



main()
