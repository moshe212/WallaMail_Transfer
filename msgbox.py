import time
import datetime
import tkinter as tk

from tkinter import *
from tkinter import messagebox
from time import sleep

# from PIL import ImageTk, Image
from tkinter.font import Font

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver import Actionchains
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as ec


chrome_path = r"C:\WallaTransfer\chromedriver_win32\chromedriver.exe"
chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
#chrome_options.headless = True
chrome_options.add_argument('log-level=2')
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")


a = Tk()
a.geometry('500x300+800+400')
a.title("מערכת הסבת וואלה מייל")

r = StringVar()
UN = StringVar()
PW = StringVar()
Co = StringVar()
Ds = StringVar()
Ps = StringVar()


def msg(Co, UN, PW, Ds, Ps):

    b = Tk()
    b.geometry('350x210+800+400')
    b.title("מערכת הסבת וואלה מייל")

    C = Canvas(b)
    filename = PhotoImage(file="C:\\WallaTransfer\\takNet4.png")
    background_label = Label(b, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    R0 = Label(b, bg="white", text=".תודה, תהליך ההסבה מתחיל כעת",
               font="David 11 bold")
    R0.place(x=80, y=80)

    def close():
        d.destroy()
        driver.quit()

        # f.close()
        sys.exit()

    driver = webdriver.Chrome(
        executable_path=chrome_path, chrome_options=chrome_options)

    try:
        Path = 'https://frienDs.walla.co.il/#/login'
        driver.get(Path)
    except:
        b.destroy()
        d = Tk()
        d.geometry('350x210+800+400')
        d.title("מערכת הסבת וואלה מייל")

        C = Canvas(d)
        filename = PhotoImage(file="C:\\WallaTransfer\\takNet4.png")
        background_label = Label(d, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        R0 = Label(d, bg="white", text=".אין אפשרות להיכנס לאתר וואלה",
                   font="David 11 bold")
        R0.place(x=80, y=60)
        R1 = Label(d, bg="white",
                   text=".נא צור קשר בטלפון 052-3587990", font="David 11 bold")
        R1.place(x=80, y=80)
        s = Button(d, text="OK", command=close, height=1, width=8)
        # s.grid(row=5,column=1)
        s.place(x=130, y=100)

    driver.save_screenshot('C:\WallaTransfer\screen10.png')

    try:
        user = driver.find_element_by_xpath(
            '//*[@id="wrapper"]/section[1]/form/fieldset/ul/li[1]/app-input-user-name/form/input')

        user.send_keys(UN)
        driver.find_element_by_xpath(
            '//*[@id="wrapper"]/section/form/fieldset/ul/li[3]/button').click()
        time.sleep(3)
    except:
        b.destroy()
        d = Tk()
        d.geometry('350x210+800+400')
        d.title("מערכת הסבת וואלה מייל")

        C = Canvas(d)
        filename = PhotoImage(file="C:\\WallaTransfer\\takNet4.png")
        background_label = Label(d, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        R0 = Label(d, bg="white", text=".אין אפשרות להיכנס לאתר וואלה",
                   font="David 11 bold")
        R0.place(x=80, y=60)
        R1 = Label(d, bg="white",
                   text=".נא צור קשר בטלפון 052-3587990", font="David 11 bold")
        R1.place(x=80, y=80)
        s = Button(d, text="OK", command=close, height=1, width=8)
        # s.grid(row=5,column=1)
        s.place(x=130, y=100)

    try:
        # passwd = driver.find_element_by_xpath('//*[@id="wrapper"]/section[1]/form/fieldset/ul/li[2]/app-input-password/form/div[1]/input').send_keys(PW, Keys.ENTER)
        passwd = driver.find_element_by_class_name(
            'form-control').send_keys(PW, Keys.ENTER)
        driver.find_element_by_xpath(
            '//*[@id="wrapper"]/section/form/fieldset/button[1]').click()
        time.sleep(3)
    except:
        b.destroy()
        d = Tk()
        d.geometry('350x200+800+400')
        d.title("מערכת הסבת וואלה מייל")

        C = Canvas(d)
        filename = PhotoImage(file="C:\\WallaTransfer\\takNet4.png")
        background_label = Label(d, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        R0 = Label(d, bg="white", text=".אין אפשרות להיכנס לאתר וואלה",
                   font="David 11 bold")
        R0.place(x=80, y=60)
        R1 = Label(d, bg="white",
                   text=".נא צור קשר בטלפון 052-3587990", font="David 11 bold")
        R1.place(x=80, y=80)
        s = Button(d, text="OK", command=close, height=1, width=8)
        # s.grid(row=5,column=1)
        s.place(x=130, y=100)

    driver.save_screenshot('C:\WallaTransfer\screen11.png')

    try:
        Enter = driver.find_element_by_xpath(
            '//*[@id="wrapper"]/section[1]/form/fieldset/button')
        now = datetime.datetime.now()
        with open("Output.txt", "w") as text_file:
            print(str(str(now)) + f"   Get In Not Succes", file=text_file)

        b.destroy()
        d = Tk()
        d.geometry('350x210+800+400')
        d.title("מערכת הסבת וואלה מייל")

        C = Canvas(d)
        filename = PhotoImage(file="C:\\WallaTransfer\\takNet4.png")
        background_label = Label(d, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        R0 = Label(d, bg="white", text=".שם משתמש או ססמה אינם נכונים",
                   font="David 11 bold")
        R0.place(x=80, y=60)
        R1 = Label(
            d, bg="white", text=".נא הזן מחדש את שם המשתמש והססמה ונסה שוב", font="David 11 bold")
        R1.place(x=40, y=80)
        s = Button(d, text="OK", command=close, height=1, width=8)
        # s.grid(row=5,column=1)
        s.place(x=130, y=110)

    except:
        now = datetime.datetime.now()
        with open("Output.txt", "w") as text_file:
            print(str(str(now)) + f"   Get In Succes", file=text_file)

    b.update()
    sleep(2)
    b.geometry('350x210')
    b.title("מערכת הסבת וואלה מייל")

    C = Canvas(b)
    filename = PhotoImage(file="C:\\WallaTransfer\\takNet4.png")
    background_label = Label(b, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    R0 = Label(b, bg="white", text=".תודה, תהליך ההסבה מתחיל כעת",
               font="David 11 bold")
    R0.place(x=80, y=80)

    def find(driver):
        Next_Page = driver.find_element_by_xpath(
            '//*[@id="main-content"]/div/div[1]/div[4]/button[2]/span')
        if Next_Page:
            return Next_Page
        else:
            return False

    def finDs(driver):
        SendTo1 = driver.find_element_by_xpath(
            '//*[@id="mainContent"]/form/div[2]/ul/li[1]/div/ul/li/input')
        if SendTo1:
            return SendTo1
        else:
            return False

    def findT(driver):
        # Transform = driver.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div[1]/div[2]/button[1]/span[1]')
        Transform = driver.find_element_by_xpath(
            '//*[@id="mainContent"]/div[1]/div[2]/div[2]/button[1]')
        if Transform:
            return Transform
        else:
            return False

# def FindSA(driver,Email):
##        ScrollArea = driver.find_element_by_xpath(Email)
# if ScrollArea:
# return ScrollArea
# else:
# return False

    e = int(int(int(Ps)/25))
    if (25*e) != int(Ps):
        ClickNext = e
    else:
        ClickNext = e-1

    Miss = 0
    Total = 1
    TotalCount = int(Co)+1
    now = datetime.datetime.now()
    with open("Output.txt", "a") as text_file:
        print(str(str(now)) + f"   Total-"+str(Total), file=text_file)
        print(str(str(now)) + f"   TotalCount-" +
              str(TotalCount), file=text_file)

    while int(Total) < int(Ps)+int(Co):

        i = 1
        Count25 = 1

        while Count25 < 26 and Total < int(Ps)+int(Co):

            a = int(int(int(Ps)/25))
            if (25*a) != int(Ps):
                FirstCount = int(int(Ps)-(25*a))
            else:
                FirstCount = 25

            if int(Ps) > 1 and Total == 1:
                Total = int(Ps)
                i = FirstCount
                Count25 = FirstCount

                for p in range(ClickNext):
                    try:
                        time.sleep(1)
                        Next_Page = WebDriverWait(driver, 60).until(find)
                        Next_Page.click()
                    except:
                        now = datetime.datetime.now()
                        #print("Can't Get Next_Page")
                        with open("Output.txt", "a") as text_file:
                            print(f"Can't Get Next_Page", file=text_file)

            now = datetime.datetime.now()
            with open("Output.txt", "a") as text_file:
                print(str(str(now)) + f"   Count25-" +
                      str(Count25), file=text_file)
                print(str(now) + f"   i-"+str(i), file=text_file)
                print(str(now) + f"   Miss-"+str(Miss), file=text_file)
            #print (Count25)
            #print (i)
            #print (Miss)

            Email = '//*[@id="main-content"]/div/div[1]/div[3]/ul/li[{}]'.format(
                i)
            #print (Email)
            ScrollArea = driver.find_element_by_xpath(Email)
            hover = ActionChains(driver).move_to_element(ScrollArea)
            hover.perform()

            # time.sleep(7)
            try:
                time.sleep(2)
                ScrollArea.click()

            except:
                time.sleep(2)
                ScrollArea2 = driver.find_element_by_xpath(Email)
                hover = ActionChains(driver).move_to_element(ScrollArea2)
                hover.perform()
                try:
                    time.sleep(1)
                    ScrollArea2.click()
                    # print('ScrollArea2')
                except:
                    time.sleep(2)
                    ScrollArea3 = driver.find_element_by_xpath(Email)
                    hover = ActionChains(driver).move_to_element(ScrollArea3)
                    hover.perform()
                    try:
                        time.sleep(2)
                        ScrollArea3.click()
                        # print('ScrollArea3')
                    except:
                        now = datetime.datetime.now()
                        #print("Can't get ScrollArea3 ")
                        with open("Output.txt", "a") as text_file:
                            print(str(now) + f"   Can't get ScrollArea3 ",
                                  file=text_file)

            Transform = WebDriverWait(driver, 60).until(findT)

            try:

                time.sleep(3)
                Transform.click()
                #print ('Transform Succes')
            except:
                try:
                    time.sleep(2)
                    Transform = driver.find_element_by_xpath(
                        '//*[@id="mainContent"]/div[1]/div[1]/div[2]/button[1]/span[1]')
                    time.sleep(1)
                    Transform.click()
                    #print ('Transform2 Succes')
                except:
                    try:
                        time.sleep(3)
                        Transform = driver.find_element_by_xpath(
                            '//*[@id="mainContent"]/div[1]/div[1]/div[2]/button[1]/span[1]')
                        time.sleep(1)
                        Transform.click()
                        #print ('Transform3 Succes')
                    except:
                        now = datetime.datetime.now()
                        #print('Transform Not Clicked')
                        with open("Output.txt", "a") as text_file:
                            print(str(now) + f"   Transform Not Clicked",
                                  file=text_file)

            driver.save_screenshot('C:\WallaTransfer\screen0.png')
            # time.sleep(1)
            #print ('SendTo1')
            driver.save_screenshot('C:\WallaTransfer\screen1.png')
            try:
                SendTo1 = WebDriverWait(driver, 60).until(finDs)
                #SendTo1 = driver.find_element_by_xpath('//*[@id="mainContent"]/form/div[2]/ul/li[1]/div/ul/li/input')
                SendTo1.send_keys(Ds)
                Send = driver.find_element_by_xpath(
                    '//*[@id="mainContent"]/form/div[1]/div/button[1]').click()
            except:
                time.sleep(3)

                #print ('SendTo2')
                driver.save_screenshot('C:\WallaTransfer\screen2.png')
                try:
                    SendTo2 = driver.find_element_by_xpath(
                        '//*[@id="mainContent"]/form/div[2]/ul/li[1]/div/ul/li/input')
                    SendTo2.send_keys(Ds)
                    Send = driver.find_element_by_xpath(
                        '//*[@id="mainContent"]/form/div[1]/div/button[1]').click()
                except:
                    time.sleep(3)

                    #print ('SendTo3')
                    driver.save_screenshot('C:\WallaTransfer\screen3.png')
                    try:
                        SendTo3 = driver.find_element_by_xpath(
                            '//*[@id="mainContent"]/form/div[2]/ul/li[1]/div/ul/li/input')
                        SendTo3.send_keys(Ds)
                        Send = driver.find_element_by_xpath(
                            '//*[@id="mainContent"]/form/div[1]/div/button[1]').click()
                    except:
                        time.sleep(3)

                        #print ('SendTo4')
                        driver.save_screenshot('C:\WallaTransfer\screen4.png')
                        try:
                            SendTo4 = driver.find_element_by_xpath(
                                '//*[@id="mainContent"]/form/div[2]/ul/li[1]/div/ul/li/input')
                            SendTo4.send_keys(Ds)
                            Send = driver.find_element_by_xpath(
                                '//*[@id="mainContent"]/form/div[1]/div/button[1]').click()
                        except:
                            #print("Can't SendTo, Try Go Back")
                            with open("Output.txt", "a") as text_file:
                                print(
                                    str(now) + f"   Can't SendTo, Try Go Back", file=text_file)
                            try:
                                driver.find_element_by_xpath(
                                    '//*[@id="foldersNav"]/div/div/section[2]/ul/li[2]/a').click()
                                # driver.execute_script("window.history.go(-1)")
                                Miss = Miss + 1
                                now = datetime.datetime.now()
                                with open("Output.txt", "a") as text_file:
                                    print(
                                        str(now) + f"   Go Back. Miss_Mail- " + str(Miss), file=text_file)
                                #print ('Miss_Mail'+'-'+Miss)
                            except:
                                #print ("Can't Go Back")
                                Miss = Miss + 1
                                now = datetime.datetime.now()
                                with open("Output.txt", "a") as text_file:
                                    print(
                                        str(now) + f"  Can't Go Back. Miss_Mail- " + str(Miss), file=text_file)

                                #print ('Miss_Mail'+'-'+Miss)

            Count25 = Count25+1

            i = i+1

            Total = Total+1

            if int(Ps) == 1:

                text = "{}/".format(Total)
                #print (text)
                b.update()
                sleep(2)
                b.geometry('350x210')
                b.title("מערכת הסבת וואלה מייל")

                C = Canvas(b)
                filename = PhotoImage(file="C:\\WallaTransfer\\takNet4.png")
                background_label = Label(b, image=filename)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                R0 = Label(
                    b, bg="white", text=".תהליך ההסבה החל,להלן התקדמות תהליך ההסבה", font="David 11 bold")
                R0.place(x=30, y=60)

                R1 = Label(b, bg="white", text='.' + 'נשלחו ' +
                           text+Co + ' מיילים', font="David 11 bold")
                R1.place(x=120, y=80)

            if int(Ps) > 1:

                TotalForCount = int(Total)-int(Ps)+1

                text = "{}/".format(TotalForCount)
                #print (text)
                b.update()
                sleep(2)
                b.geometry('350x210')
                b.title("מערכת הסבת וואלה מייל")

                C = Canvas(b)
                filename = PhotoImage(file="C:\\WallaTransfer\\takNet4.png")
                background_label = Label(b, image=filename)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                R0 = Label(
                    b, bg="white", text=".תהליך ההסבה החל,להלן התקדמות תהליך ההסבה", font="David 11 bold")
                R0.place(x=30, y=60)

                R1 = Label(b, bg="white", text='.' + 'נשלחו ' +
                           text+Co + ' מיילים', font="David 11 bold")
                R1.place(x=120, y=80)

            if Total > 25:
                f = int(int(int(Total)/25))
                if (25*f) != int(Total):
                    Page = f
                else:
                    Page = f-1
            else:
                Page = 0
            #Page = int(int(int(Total)/25))
            #print (Page)
            for n in range(Page):
                try:
                    time.sleep(0.5)
                    Next_Page = WebDriverWait(driver, 60).until(find)
                    Next_Page.click()
                except:
                    #print("Can't Get Next_Page")
                    now = datetime.datetime.now()
                    with open("Output.txt", "a") as text_file:
                        print(f"Can't Get Next_Page", file=text_file)

# if Total > 25 and Total < 51:
# for p in range(1):
# try:
##                        Next_Page = WebDriverWait(driver, 120).until(find)
# Next_Page.click()
# except:
# print("Can't Get Next_Page")
# with open("Output.txt", "a") as text_file:
##                            print(f"Can't Get Next_Page", file=text_file)

    b.destroy()

    TotalSend = str(int(Co)-int(Miss))

    c = Tk()
    c.geometry('350x210+800+400')
    c.title("מערכת הסבת וואלה מייל")

    Ca = Canvas(c)
    filename = PhotoImage(file="C:\\WallaTransfer\\takNet4.png")
    background_label = Label(c, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    R0 = Label(c, bg="white", text=".תהליך ההסבה הסתיים בהצלחה",
               font="David 11 bold")
    R0.place(x=90, y=60)

    R1 = Label(c, bg="white", text='.' + 'נשלחו ' +
               TotalSend + ' מיילים', font="David 11 bold")
    R1.place(x=130, y=80)

    R2 = Label(c, bg="white", text='.' + 'נכשלו ' +
               str(Miss) + ' מיילים ', font="David 11 bold")
    R2.place(x=130, y=100)

    c.mainloop()
    driver.quit()

    # f.close()
    sys.exit()


def ex():
    # r=e1.get()
    UN = e1.get()
    PW = e2.get()
    Co = e3.get()
    Ps = e4.get()
    Ds = e5.get()
    print(UN)
    #print (PW)
    #print (Co)
    #print (Ds)

    a.destroy()
    msg(Co, UN, PW, Ds, Ps)


C = Canvas(a)
filename = PhotoImage(file="C:\\WallaTransfer\\takNet3.png")
background_label = Label(a, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


##text = tk.Text(a)
##myFont = Font(family="Times New Roman", size=12)
# text.configure(font=myFont)
# l0=Label(a,bg="white",text="")
l1 = Label(a, bg="white",
           text=". OK להתחלת התהליך אנא מלא את הפרטים הבאים ולחץ על ", font="David 11 bold")
#l0.grid(row=0,column=1,padx=2, pady=8)
l1.place(x=80, y=50)


l1 = Label(a, bg="white", text=":שם משתמש")
l1.grid(row=4, column=2)
l1.place(x=410, y=90)

e1 = Entry(a, bg="white", fg="black", bd=2, w=25, textvariable=UN)
e1.grid(row=4, column=1, padx=20, pady=5)
e1.place(x=250, y=90)

l2 = Label(a, bg="white", text=":ססמה")
# l2.grid(row=5,column=2)
l2.place(x=180, y=90)

e2 = Entry(a, bg="white", bd=2, w=25, fg="black", show="*")
#e2.grid(row=5,column=1,padx=20, pady=5)
e2.place(x=20, y=90)

l3 = Label(a, bg="white", text=":כמות מיילים")
# l3.grid(row=6,column=2)
l3.place(x=410, y=130)

e3 = Entry(a, bg="white", fg="black", bd=2, w=35, textvariable=Co)
#e3.grid(row=6,column=1,padx=20, pady=5)
e3.place(x=190, y=130)

l4 = Label(a, bg="white", text=":מיקום")
# l5.grid(row=8,column=2)
l4.place(x=120, y=130)

e4 = Entry(a, bg="white", fg="black", bd=2, w=15, textvariable=Ps)
#e5.grid(row=8,column=1,padx=20, pady=5)
e4.place(x=20, y=130)

l5 = Label(a, bg="white", text=":מייל יעד")
# l4.grid(row=7,column=2)
l5.place(x=310, y=170)

e5 = Entry(a, bg="white", fg="black", bd=2, w=45, textvariable=Ds)
#e4.grid(row=7,column=1,padx=20, pady=5)
e5.place(x=20, y=170)


s = Button(a, text="OK", command=ex, height=1, width=15)
s.place(x=130, y=215)
# s.grid(row=9,column=1)
a.mainloop()
