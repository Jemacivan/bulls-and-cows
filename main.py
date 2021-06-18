import random


class Bulls_and_cows():

    def __init__ (self):
        self.bulls = 0
        self.cows = 0
        self.bulls_and_cows = random.randint(1000,9999)
        self.attempts = 0

        self.settings_and_run()


    def settings_and_run(self):

        attempt = input("Attemps: ")
        if attempt.isdecimal():
            self.attempts = int(attempt)

        cheats = input("Do you want to enable cheats?  [y/N]")
        if (cheats == "Y") or (cheats == "y"):
            print(self.bulls_and_cows)

        self.game()


    def check_answer(self,a,b,c,d,a1,b1,c1,d1):
        if a1 == a:
            self.bulls += 1
        elif (a1 == b) or (a1 == c) or (a1 == d):
            self.cows += 1
        else:
            pass

        if b1 == b:
            self.bulls += 1
        elif (b1 == a) or (b1 == c) or (b1 == d):
            self.cows += 1
        else:
            pass

        if c1 == c:
            self.bulls += 1
        elif (c1 == b) or (c1 == a) or (c1 == d):
            self.cows += 1
        else:
            pass

        if d1 == d:
            self.bulls += 1
        elif (d1 == b) or (d1 == c) or (d1 == a):
            self.cows += 1
        else:
            pass

        return


    def game(self):
        a1,b1,c1,d1 = str(self.bulls_and_cows).strip()

        while True:
            user_input = input("Your answer: ")
            if (user_input.isdecimal()) and (len(user_input) == 4):

                a,b,c,d = user_input.strip()

                self.check_answer(a,b,c,d,a1,b1,c1,d1)

                if (self.bulls == 4) and (self.cows == 0):
                    self.win()
                    break
                else:
                    print("Bulls: {}\nCows: {}\nAttempts: {}".format(self.bulls, self.cows, self.attempts))
                    self.cows = 0
                    self.bulls = 0
                    self.attempts -= 1
                    if self.attempts <= 0:
                        self.lose()
                        break
                    continue

            else:
                print("Error")


    def win(self):
        print(r"""
                                       /;    ;\
                                   __  \\____//
                                  /{_\_/   `'\____
                                  \___   (o)  (o  }
       _____________________________/          :--'   DRINKA
   ,-,'`@@@@@@@@       @@@@@@         \_    `__\
  ;:(  @@@@@@@@@        @@@             \___(o'o)
  :: )  @@@@          @@@@@@        ,'@@(  `===='        PINTA
  :: : @@@@@:          @@@@         `@@@:
  :: \  @@@@@:       @@@@@@@)    (  '@@@'
  ;; /\      /`,    @@@@@@@@@\   :@@@@@)                   MILKA
  ::/  )    {_----------------:  :~`,~~;
 ;;'`; :   )                  :  / `; ;
;;;; : :   ;                  :  ;  ; :                        DAY !!!
`'`' / :  :                   :  :  : :
    )_ \__;      ";"          :_ ;  \_\       `,','
    :__\  \    * `,'*         \  \  :  \   *  8`;'*  *
        `^'     \ :/           `^'  `-^-'   \v/ :  \/   -YOU WIN-

------------------------------------------------
        """)


    def lose(self):
        print(r"""
   /                       \
 /X/                       \X\
|XX\         _____         /XX|
|XXX\     _/       \_     /XXX|___________
 \XXXXXXX             XXXXXXX/            \\\
   \XXXX    /     \    XXXXX/                \\\
        |   0     0   |                         \
         |           |                           \
          \         /                            |______//
           \       /                             |
            | O_O | \                            |
             \ _ /   \________________           |
                        | |  | |      \         /
  No Bullshit,          / |  / |       \______/
   Please...            \ |  \ |        \ |  \ |
                      __| |__| |      __| |__| |
                      |___||___|      |___||___|

        """)
        print("The answer was:",self.bulls_and_cows)





Bulls_and_cows()
