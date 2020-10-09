import turtle
import time
import sys
global celllock
global inv
global janitorjob
writer = turtle.Turtle()
writer.hideturtle()
screen = turtle.Screen()
screen.title("Text Adventures!")
writer.speed("fastest")
writer.penup()
def choice(prompt, optionlist):
    ans = screen.textinput("Choice", prompt)
    print(ans.lower())
    if ans.lower() == "end":
        sys.exit()
    for i in optionlist:
        if str(i).lower() == str(ans.lower()):
            return i
def goon():
    var = screen.textinput("Enter to continue", "Type end to stop game")
    if var.lower() == "end":
        sys.exit()
def type(content):
    writer.clear()
    writer.write(content, align="center", font=("Verdana", 15, "normal"))
    goon()
def start():
    writer.write("Welcome to type adventures!", align="center", font=("Verdana", 15, "normal"))
    time.sleep(2)
    writer.clear()
    writer.write("Press enter to continue!", align="center", font=("Verdana", 15, "normal"))
    var = screen.textinput("Enter to continue", "Type end to stop game")
    if var.lower() == "end":
        sys.exit()
    else:
        beginstory()
def beginstory():
    inv = []
    type("You wake up, in your jail cell. But this time, things are different")
    type("Sleep-Deprived Guards are shuffled in to take the prisoners to breakfast, or at least the slop they call "
         "breakfast")
    type("""A guard walks up to your chamber and opens the door. "Don't make this any harder than it needs to be" """)
    var = choice("Do you follow the guard? (Yes or no?)", ["yes", "no"])
    var = str(var)
    print(var)
    if var == "yes":
        celldoor = True
        type("you walk into the cafeteria. The guard peels off and you go sit alone. No use having friends in prison.")
        type("The warden himself has made an appearance today, and announces to the prison, ")
        type('"Today I am accepting volenteers for janitorial work on the prison. You will put your name in the hat,')
        type('...and we will draw 5 winners. Winners will get different jobs for rooms in the prison. Got it?"')
        var = str(choice("Do you put your name in the hat?", ["yes", "no"]))
        if var == "yes":
            print("got janitor job.")
            type("They shake the hat around, and draw five names. Your name is one of them")
            type("Job accepted in: Security room")
            janitorjob = True
        if var == "no":
            print("I declined the opportunity, I would rather just waste away in my cell.")
            janitorjob = False
        type("The day flies by until it is over")
    elif var == "no":
        type("""You put your foot down. You refuse to follow the guard.""")
        type('the guard promptly pulls out his nightstick and begins to threaten you. "Dont make me put you in the hole"')
        type("He whacks the lock of your cell, as if to display authority.")
        celldoor = False
        type("You put your head down and follow the guard into the cafeteria, defeated.")
        type("you walk into the cafeteria. The guard peels off and you go sit alone. No use having friends in prison.")
        type("The warden himself has made an appearance today, and announces to the prison, ")
        type('"Today I am accepting volenteers for janitorial work on the prison. You will put your name in the hat,')
        type('...and we will draw 5 winners. Winners will get different jobs for rooms in the prison. Got it?"')
        var = str(choice("Do you put your name in the hat?", ["yes", "no"]))
        if var == "yes":
            print("got janitor job.")
            type("They shake the hat around, and draw five names. Your name is one of them")
            type("Job accepted in: Security room")
            janitorjob = True
        if var == "no":
            print("I declined the opportunity, I would rather just waste away in my cell.")
            janitorjob = False
        type("The day flies by until it is over")
    if janitorjob:
        type("Congratulations! You got a job as a janitor!")
    if not celldoor:
        type("as you finish your day, you notice the lock on your cell door seems to be broken on the inside")
        type("it must have happened when the guard threatened you.")
        type("if you had something small to get inside, you could break the lock")
    type("press enter to go to sleep")
    type("you wake up early to the sounds of breakfast: guards marching around, prisoners getting up and jeering, the usual.")
    type("the same guard from yesterday walks up to your cell,")
    if celldoor:
        type('"just be cooperative, like yesterday and I will look kindly on you."')
        type("You smile and follow him to the cafeteria.")
    else:
        type('"listen punk, give me any trouble today and I will make sure you wont be able to walk to breakfast"')
        type('"Got it?"')
        type("You nod your head meekly and follow him to breakfast")
    if janitorjob:
        type("After you eat breakfast, you and 4 other people are shuffled into different rooms for your janitorial job.")
        type("The security room is a rats nest, wires and dust bunnies are scattered everywhere")
        type("While you're in the security room, you spot a warden access card in the bottom of one of the drawers")
        type("Surely nobody will notice if I take it, you think to yourself.")
        var = str(choice("Do you grab the card?", ["yes", "no"]))
        if var == "yes":
            type("Card added to inventory")
            inv = inv + ["card"]
            type("There was a paperclip under the card, you also grab that")
            inv = inv + ["paperclip"]
        if var == "no":
            type("you call to your supervisor, who is busy looking on his phone,")
            type('"Hey, is this supposed to be here?"')
            type('The supervisor rushes over. "Heavens no, thank you for telling us, you could open all the doors in the prison with this!')
        type("You finish cleaning the security room. While you worked, you realised the east tunnel is a blind spot.")
        type("You recall that the east tunnel leads directly to the front gate of the prison.")
    else:
        type("At breakfast, you eat in your normal spot. While you sit, you think about how you could escape")
        type("First off, there is a lock in front of your door.")
        type("Second, you would need to know of a blind spot, as to avoid being detected by security.")
        type("Finally, you would need a keycard to open the front gate")
        type("After that, all you need is to look casual, like you just was let out.")
    type("at the end of the day, you shuffle back to your cell and sleep early. You have a big day tomorrow.")
    type("Press enter to sleep.")
    type("Today is the big day. Today things are different. You just know it.")
    type("Its a sunday, so most of the guards are off at church and the prisoners are allowed to sleep in.")
    type("You wake up at 4:00 AM to start your escape")
    if celldoor:
        type("Unfortunately, you are stopped immediately when you realise your cell door is locked. If only you could break the lock.")
        type("You quickly go back to bed.")
        type("You wake up and go to breakfast. After breakfast you are called to the warden's office...")
        type("You get there and see multiple prison officials. They say 'welcome to your parole hearing'")
        parolepoints = 0
        if janitorjob:
            type('One says, "you did a janitorial job, which we are grateful for,"')
            parolepoints = parolepoints + 1
            if len(inv) == 0:
                type('"And you reported a missing warden access card"')
                parolepoints = parolepoints + 1
        if celldoor:
            type('The guard walks in, "this one has been good for as long as I have known them, and they really '
                 'helped me out on my first day"')
            parolepoints = parolepoints + 1
        else:
            type('With a look of disdain on his face, the guard from earlier walks in.')
            type('The guard says "This one is a handful. I dont believe they are ready to join society."')
        if parolepoints == 3:
            type('After much scribbling, the warden has made his decision.')
            type('"Congratulations! You have been accepted for parole! meet me in an hour with your stuff at the door!"')
            type("You meet the warden, and are let out on parole. Just don't break any more laws.")
            type("Ending 1")
        else:
            type('After much scribbling, the warden has made his decision.')
            type("Sorry, your parole has been declined. We need a parole candidate to be a hard working, honest, and stable person")
            type("Better luck next year.")
            type("Ending 2")
    else:
        type("You remember that your cell lock is broken.")
        if len(inv) > 0:
            type("you use a paperclip and unlock the broken lock.")
            type("You creak open the door. No going back now")
            if janitorjob:
                type("You remember the security camera blind spots, and take the east tunnel.")
                type("everything goes smoothly and you arrive at the front get. There is a guard sleeping next to the gate")
                type("You notice an open bottle of sleeping pills and a glass of water.")
                type("You need him to be asleep, as the door makes a not-quiet grinding noise.")
                var = str(choice("Do you force-feed him sleeping pills?", ["yes", "no"]))
                if var == "yes":
                    type("You pour the water and the entire bottle of sleeping pills down his throat")
                    type("He starts to stir and opens his eyes...")
                    type("But the sleeping pills kick in and he passes out cold, or worse. Best not to think of it now.")
                    type("You open the door with your warden keycard, and the guard is still asleep, even as the massive doors open.")
                    type("You simply walk out of the door, taking care to be on the blind spot of the camera. ")
                    type("And just like that it's over. You are a free person.")
                    type("Ending 4")
                else:
                    type("you don't feed him the sleeping pills. I'm a felon, but not a murderer")
                    type("You open the door with your keycard, and the guard wakes up to the sound of the massive doors opening.")
                    type("He raises the alarm, and you are surrounded by guards within minutes.")
                    type("You are caught and transferred to a high security prison.")
                    type("You think as you drive up to it,")
                    type("No getting out of this one.")
                    type("Ending 3")
            else:
                type("You run through the west tunnel. A security guard spots you through the cameras and sounds the alarm.")
                type("The entire prison wakes up and guards surround you while you are attempting to open the front gate.")
                type("You are caught and transferred to a high security prison.")
                type("You think as you drive up to it,")
                type("No getting out of this one.")
                type("Ending 3")
        else:
            type("you try your best to get it open, but the lock is robust. If only you had something small to get in it with")
            type("You trying to open the lock is so loud, it wakes a guard. He realizes what you are doing and immediately sounds the alarm")
            type("You are caught and transferred to a high security prison.")
            type("You think as you drive up to it,")
            type("No getting out of this one.")
            type("Ending 3")
start()
screen.mainloop()