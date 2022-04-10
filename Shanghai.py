count = int(0)
for count in range(0,10):
    print("""
          Welcome to Pranto's Testing Site!""")

    print("""
To join this Grand Tournament, you have to fill in this forms:
          Team Name, Team members name, Team mmr; and Local Gaming Server.

          """)


    team = input("Enter your team's name: ")
    member1 = input("Enter team-member 1's name: ")
    member2 = input("Enter 'team-member 2's' name: ")
    member3 = input("Enter 'team-member 3's' name: ")
    member4 = input("Enter 'team-member 4's' name: ")
    member5 = input("Enter 'team-member 5's' name: ")
    Coach = input("Enter you're team's coach's name: ")

    mmr = int(input("Enter you're team's avarage mmr: "))

    server = input("Enter you're Local Gaming Server's name: ")

    count = (count + 1)
    print(count)
                 #WTF am i doing with the count?#        #what happens when the count goes to 10?#
print("""
Congratulations, you have finished the Admin form.
          Now you're officially regestered in the DOTA Shanghai Tournament!



          """)
if count >= 10:
        print("""
Sorry, we are out of registeration spaces;
              Fill free to try again the nest year! Thank You



              """)
