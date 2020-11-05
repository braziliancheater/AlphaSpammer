#simple simple example of a spammer?
#Made from ground by brazilian aka crim3s
import pyautogui, time, pymsgbox, ctypes, sys, smtplib
from pynput.mouse import Listener
from ctypes import wintypes

#this should get the window PID
#for now its only gonna used for astetics
user32 = ctypes.windll.user32
h_wnd = user32.GetForegroundWindow()
pid = wintypes.DWORD()
user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))

#name of the file that contains plain text
f = open("text",'r')

print("   ___   __     __        ")
print("  / _ | / /__  / /  ___ _ ")
print(" / __ |/ / _ \/ _ \/ _ `/ ")
print("/_/ |_/_/ .__/_//_/\_,_(_)")
print("       /_/                ")

print("\nAlpha Spammer 0.1 by brazilian")

time.sleep(3)

print("\n--- Options ---")
print("Generic Spam (PyAutoGUI) - 1")
print("Email Nuker - 2")
print("--- Misc ---")
print("Edit text - 3")
print("Print text - 4")
print("...")
d = int(input("Method - "))

if d == 1:
    b = int(input("Delay (Seconds) - "))
    c = int(input("Repeat how many times - "))
    if d == 1:
        print("Select the target Window - \n")
        time.sleep(3)
        #print("Window found PID - " + pid.value)
        print("...\n")
                
        for word in f:
            for i in range(c):
                try:
                    pyautogui.typewrite(word)
                    pyautogui.press("enter")
                    time.sleep(b)

                except KeyboardInterrupt:
                    print("\nKeyboard Interrupt")          
                
                
    #if you want to use a prompt box
    #pymsgbox.alert('Done..', 'Alpha')
elif d == 2:
    try:
        spammail = input("\nThe email you want to spam - ")
        email = input("Your email - ")
        password = input("Your password - ")
        message = input("the message you want to spam - ")
        counter = int(input("How many times - "))

        s_ = input('which provider (1-Gmail|2-Outlook): ')

        if s_ == "1":
            mail = smtplib.SMTP('smtp.gmail.com',587)
        elif s_ == "2":
            mail = smtplib.SMTP('smtp.office365.com',587)

        for x in range(0,counter):
            print("Message number - : ", x+1)
            mail.ehlo()
            mail.starttls()
            mail.login(email,password)
            mail.sendmail(email,spammail,message)
            time.sleep(1)

        mail.close()
    except Exception as e:
        print("Error.")
if d == 3:
    print("You can edit the main text file here -\n")
    e = input("Insert text - ")
    f.write(e)
    print("Successful Written! exiting...")
    time.sleep(3)
    sys.exit()
if d == 4:
    print("This prints what is inside your 'text' file. \n")
    print(f.read())
    print("\nSuccessful read! exiting...")
    time.sleep(3)
    sys.exit()