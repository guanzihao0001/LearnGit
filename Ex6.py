one_more = "y"
while one_more == "y":
    print("enter 'y' to add onr more student or just press <ENTER> to quit:", end="")
    one_more = input()
    if one_more == '\r': break
    print("enter your name:",end="")
    name=input()
    print("do you have SAT or ACT score(enter 'sat' or 'act')?",end="")
    type=input()


    if type=="SAT":
        print("Your SAT score:")
        print("math:", end="")
        math=int(input())
        print("reading:",end="")
        reading=int(input())
        print("writing:",end="")
        writing=int(input())
        print("Your GPA score")
        print("actual:",)
    elif type=="ACT":
        print("Your ACT score:")
        print("english:", end="")
        english = int(input())
        print("math:", end="")
        math = int(input())
        print("reading:", end="")
        reading = int(input())
        print("science:", end="")
        science= int(input())

