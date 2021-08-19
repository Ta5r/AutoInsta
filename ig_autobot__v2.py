from time import sleep
import cred
from socket import close
#import threading
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import _find_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#THREAD OUT MSG HANDLING HERE
exitFlag = 0

#PATH VAR TO SPECIFIC PAGES
uname = cred.username
path_home = "https://www.instagram.com/"
path_inbox = path_home+"direct/inbox/"
path_profile_page = path_home+""+uname+"/"
path_saved = path_home+""+uname+"/saved/"
path_explore = path_home+"explore/"
path_edit_settings = path_home+"accounts/edit/"
path_tagged = path_home+""+uname+"/tagged/"
path_igtv = path_home+""+uname+"/channel/"
path_followers = path_home+""+uname+"/followers"
path_following = path_home+""+uname+"/following"

var_ud= "UNDER DEVELOPMENT"
auto_mode_status = False
recent_profile = "https://www.instagram.com/"

#FUNCTIONs to do some work
def get_title():
    print(driver.title)

def msg():
    msg_val = input("MESSAGE TO SEND ===> ")
    
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "sqdOP.L3NKy._4pI4F._8A5w5"))
        )
        element.click()
    except:
        print("TRY AGAIN LATER :-/")
        input_comand()
     
    time.sleep(5)
    msg_input = driver.find_elements_by_tag_name("textarea")
    print("num of text areas = ")
    print(msg_input[0])
    msg_input[0].send_keys(msg_val)
    msg_input[0].send_keys(Keys.RETURN)
    print("Message SENT")
    srch()

def un_block():
    uid = input("Enter Valid USERNAME")
    pth = path_home+""+uid+"/"
    driver.get(pth)
    time.sleep(2)
    unblk_btn = driver.find_element_by_class_name("_5f5mN.jIbKX._6VtSN.yZn4P")
    time.sleep(1)
    unblk_btn.click()
    btn = driver.find_element_by_class_name("aOOlW.bIiDR")
    blc_confrm = btn
    blc_confrm.click()
    time.sleep(1)
    btn = driver.find_element_by_class_name("aOOlW.HoLwm")
    dismis = btn
    time.sleep(1)
    dismis.click()
    print("UNBLOCKED !!")
    to_search(uid)
    input_comand()

def list_followers():
    try:
        btn = driver.find_elements_by_class_name("-nal3")
    except:
        btn = driver.find_elements_by_class_name("_81NM2")
    print("btns")
    print(len(btn))
    flwr_btn = btn[1]
    flwr_btn.click()
    time.sleep(1)
    sleep(1)
    ul_element = driver.find_element_by_class_name("jSC57._6xe7A")
    print(ul_element)
    time.sleep(3)
    page_navig()
    print()

def list_following():
    btn = driver.find_elements_by_class_name("-nal3")
    flwn_btn = btn[2]
    flwn_btn.click()
    time.sleep(1)
    print()

def folo():
    follow_btn = driver.find_element_by_class_name("_5f5mN.jIbKX._6VtSN.yZn4P")
    follow_btn.click()
    time.sleep(1)
    print("FOLLOWED")
    input_comand()

def unfolo():
    unfolo_btn = driver.find_element_by_class_name("_5f5mN.-fzfL._6VtSN.yZn4P")
    unfolo_btn.click()
    time.sleep(1)
    unfolo_cnfrm = driver.find_element_by_class_name("aOOlW.-Cab_")
    unfolo_cnfrm.click()
    time.sleep(1)
    print("UNFOLLOWED !")
    srch()
    print()

def block():
    #BLOCKING CODE
    btn = driver.find_elements_by_class_name("wpO6b")
    blck_btn = btn[0]
    blck_btn.click()
    time.sleep(1)
    btn = driver.find_elements_by_class_name("aOOlW.-Cab_")
    blc_usr = btn[0]
    time.sleep(1)
    blc_usr.click()
    btn = driver.find_element_by_class_name("aOOlW.bIiDR")
    blc_confrm = btn
    blc_confrm.click()
    time.sleep(1)
    btn = driver.find_element_by_class_name("aOOlW.HoLwm")
    dismis = btn
    time.sleep(1)
    dismis.click()
    print("BLOCKED !!")
    time.sleep(3)
    driver.get(path_home)
    input_comand()

def cmnt_post():
    cmnt = input("COMMENT to Post : -->  ")
    on_post = input("COMMENT ON POST : -->  ")
    posts = driver.find_elements_by_class_name("v1Nh3.kIKUG._bz0w")
    on_post = int(on_post)-1
    post = posts[on_post]
    post.click()
    time.sleep(1)
    btns = driver.find_elements_by_class_name("wpO6b")
    cmnt_btn = btns[3]
    time.sleep(1)
    cmnt_btn.click()
    time.sleep(1)
    text_area = driver.find_element_by_class_name("Ypffh")
    text_area.send_keys(cmnt)
    text_area.send_keys(Keys.RETURN)
    time.sleep(1)
    print("")
    srch()

def like_posts():
    n = input("HOW MANY POSTS TO LIKE : ")
    n = int(n)
    posts = driver.find_elements_by_class_name("v1Nh3.kIKUG._bz0w")
    n_posts = len(posts)
    print("NUMBER OF POSTS")
    print(n_posts)
    i = 0
    while i<n:
        posts[i].click()
        i=i+1
        time.sleep(1)
        btns = driver.find_elements_by_class_name("wpO6b")
        like_btn = btns[2]
        close_btn = driver.find_element_by_class_name("Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG")
        like_btn.click()
        time.sleep(1)
        cond=True     
        while cond:
            kode = str(uuid.uuid4())
            print("TAKING SCREENSHOT - "+kode)
            driver.save_screenshot("./images/post_"+kode+".png")
            print("Saved - OK")
            try:
                nxtbtn = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "_6CZji")) or EC.element_to_be_clickable((By.CLASS_NAME,"_6CZji"))
                )
                nxtbtn.click()
                print("next pic on same post . . .")
                time.sleep(1)
            except:
                cond==False

        close_btn.click()
        time.sleep(1)
        srch()

def srch():
    try:
        get_no_posts = driver.find_elements_by_class_name("g47SY")
    except:
        get_no_posts = driver.find_elements_by_class_name("g47SY ")
    
    no_posts = get_no_posts[0].text
    no_flwr = get_no_posts[1].text
    no_flwn = get_no_posts[2].text
    print("________________")
    print(str(no_posts)+"_ : _POSTS")
    print(str(no_flwr)+"_ : _FOLLOWERS")
    print(str(no_flwn)+"_ : _FOLLOWING")
    print("________________")
    cmnd = input("What to do now ? ")
    print(cmnd)
    if cmnd=="msg":
        msg()
    elif cmnd=="blck":
        print("BLOCKING. . . .")
        block()
    
    elif cmnd=="folo":
        print("FOLLOW")
        folo()

    elif cmnd=="nfolo":
        print("UNFOLLOW")
        unfolo()

    elif cmnd=="rstr":
        #Todo
        print(var_ud)
    elif cmnd=="bio":
        #Todo
        print(var_ud)
    elif cmnd=="dnld":
        #Todo
        print(var_ud)

    elif cmnd=="back":
        input_comand()

    elif cmnd=="like":
        like_posts()
        print()

    elif cmnd=="cmnt":
        cmnt_post()
        print()

    elif cmnd=="exit":
        to_exit()

    elif cmnd=="gtle":
        get_title()
        srch()

    else:
        print("")
        print("msg")
        print("like")
        print("blck")
        print("folo")
        print("rstr")
        print("bio")
        print("dnld")
        print("back")
        print("exit")
        print("")
        srch()

def notif():
    notif_btn = driver.find_element_by_class_name("_0ZPOP.kIKUG")
    notif_btn.click()
    time.sleep(1)
    print("COMMAND ic/exit: ")
    cmnd = input()
    if cmnd=="exit":
        to_exit()
    elif cmnd=="ic":
        input_comand()
    else:
        notif()

def xplr():
    print("COMMAND : ")
    cmnd = input()
    if cmnd=="exit":
        to_exit()
    elif cmnd=="ic":
        input_comand()
    else:
        xplr()

def sved():
    print("COMMAND : ")
    cmnd = input()
    if cmnd=="exit":
        to_exit()
    elif cmnd=="ic":
        input_comand()
    else:
        sved()

def inbx():
    print("COMMAND : ")
    cmnd = input()
    if cmnd=="exit":
        to_exit()
    elif cmnd=="ic":
        input_comand()
    else:
        inbx()

def prpg():
    print("COMMAND : ")
    cmnd = input()
    if cmnd=="exit":
        to_exit()
    elif cmnd=="ic":
        input_comand()
    elif cmnd=="flwr":
        list_followers()
        print()
    elif cmnd=="flwn":
        list_following()
        print()
    else:
        print("flwr = check FOLLOWERS")
        print("flwn = check FOLLOWING")
        print("exit = EXIT")
        print("ic = input command")
        print("___")
        prpg()

def auto_mode():
    print("auto - AUTOMATIC OPeration handler MODE")
    print("Initiating. . .")
    time.sleep(2)
    print("CHECKING NOTIFICATIONS")
    n = 0
    try:
        notif = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "uk0Yc.GGDyX")) or EC.element_to_be_clickable((By.CLASS_NAME,"uk0Yc.GGDyX"))
        )
        time.sleep(1)
        print("NEW NOTIFICATION")
        try:
            notif = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_7UhW9.vy6Bb.MMzan.h_zdq.uL8Hv.T0kll")) or EC.element_to_be_clickable((By.CLASS_NAME,"_7UhW9.vy6Bb.MMzan.h_zdq.uL8Hv.T0kll"))
            )
            no_of_notif = driver.find_element_by_class_name("_7UhW9.vy6Bb.MMzan.h_zdq.uL8Hv.T0kll").text
            n = no_of_notif
        except:
            print()
    except:
        print("NO NEW NOTIFACTION YET")
    n = str(n)
    print("GOT --> "+n+" <-- NOTIFICATION(s)")

    # FRIENDS' posts liker / commenter
    # reads txt file list of friends to monitor who are close then use that list to 
    # one by one navigate to their profile page and like / comment their posts

    # INBOX HANDLER / MESSAGER
    n = 0
    try:
        notif = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "KdEwV")) or EC.element_to_be_clickable((By.CLASS_NAME,"KdEwV"))
        )
        time.sleep(1)
        print("NEW MESSAGE")
        no_of_msg = driver.find_element_by_class_name("bqXJH").text
        n = no_of_msg
    except:
        print("NO NEW MESSAGE YET")
    
    n = str(n)
    print("GOT --> "+n+" <-- MESSAGES(s)")
    n = int(n)
    if n>0:
        chat_bot(n)

    # CHECK FOR NEW FOLLOWERS / FOLLOWING
    input_comand()

def chat_bot(n):
    #GET LIST OF PEOPLE WHO MESSAGED
    #OPEN ONE BY ONE IN INBOX
    #READ THE "UNREAD" MESSAGES
    #COMPARE CASES AND DECIDE MSG TO 
    #SEND AND SEND THEN MOVE TO THE NEXT PERSON

    print(str(n)+" people message(d) you")
    driver.get(path_inbox)
    print("please wait ... rendering...")
    time.sleep(5)
    print("Ready... proceeding ...")
   
    i = 0
    while i < n:
        inbx_btns = driver.find_elements_by_class_name("-qQT3.rOtsg")
        len_inbx = len(inbx_btns)
        print("some flag")
        print(len_inbx)
        print("#####")
        print("Please wait -- "+str(i))
        time.sleep(1)
        inbx_btns[i].click()
        time.sleep(2)
        unrd_msg = driver.find_elements_by_class_name("_7UhW9.xLCgt.MMzan.KV-D4.p1tLr.hjZTB")
        len_unrd_msg = len(unrd_msg)
        print("unread msgs")
        print(len_unrd_msg)
        print("****")
        msg_txt = unrd_msg[(len_unrd_msg-1)].text
        msg_rcvd = msg_txt
        print("MESSAGE RECIEVED : - : "+str(msg_rcvd))
        if msg_rcvd.upper()=="EXIT":
            continue
        reply = msg_read_reply(msg_rcvd)
        print("REPLYING . . . : "+reply)
        msg_cht_bt(reply)
        driver.get(path_inbox)
        print("please wait ... rendering again...")
        time.sleep(5)
        print("Ready... proceeding again...")
        i=i+1
    
    driver.get(path_home)
    print()

def msg_cht_bt(msg):
    msg_val = msg
    print("processing.....")
    time.sleep(3)
    msg_input = driver.find_elements_by_tag_name("textarea")
    time.sleep(2)
    msg_input[0].send_keys(msg_val)
    msg_input[0].send_keys(Keys.RETURN)

    print("MSG SENT FROM CHAT BOT :-)")

def msg_read_reply(msg):
    msg = msg.upper()
    msg_greet = ['HI','HELLO','NAMASTEY','HEY','BONJOUR','NAMASTE','NAMSTE','NMSTE']
    msg_q1 = ['SUP','WASSUP','WHAT\'S UP','WHAT IS UP']
    msg_q2 = ['WHAT YOU DOIN','WHAT ARE YOU DOIN','WHAT YOU DOING','WHAT ARE YOU DOING']
    msg_q3 = ['KYA KAR RHE HO','KYA HO RHA HAI']
    msg_q4 = ['KI HAAL CHAAL','KYA HALCHAL','KYA HAALCHAAL','KYA HAL CHAL','KYA HAAL CHAAL','KAISE HO','AUR BHAI KAISE HO','AUR KAISE HO','THEEK HO']
    msg_q5 = ['']
    reply="."
    if msg in msg_greet:    
        reply = "Hey MAN !! HOW YOU DOIN' !!"
    elif msg in msg_q1:
        reply = "NOTHIN JUST THE SKY, HAHA KIDDIN, WORK... WILL GET BACK TO YOU LATER GOTTA GO..TTYL..TC"
    elif msg in msg_q2:
        reply = cred.username+" IS CURRENTLY BUSY WITH SOME IMPORTANT WORK...I HAVE SENT HIM THE NOTIICATION THAT YOU CONTACTED HIM , HE WILL SURELY GET BACK TO YOU SOON... THANX !"
    elif msg in msg_q3:
        reply = cred.username+" ABHI VYASTH HAI KISI ZAROORI KAAM MEI,... MAINE UNHE NOTTIFY KARDIYA HAI KI AAPNE CONTACT KIYA HAI, WO AAPSE JALD HI BAAT KARENGE... SHUKRIYA !"
    elif msg in msg_q4:
        reply = "HAAAL CHAAL SAB CHANGA SI TEENU DASSO KITHE GAYAB THE !!"
    return reply


#FUNCTIONs to go to:
def to_exit():
    print("PROCESS COMPLETED")
    time.sleep(3)
    driver.quit()

def to_home():
    driver.get(path_home)
    print("Reached Homepage")
    input_comand()

def to_notifications():
    print(var_ud)
    notif()

def to_search(to_search=""):
    search = driver.find_element_by_class_name("XTCLo.x3qfX")
    if to_search=="":
        to_search = input("Search for ? :::>>> ")
    search.send_keys(to_search)
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    print("NEW TITLE IS :")
    print(driver.title)
    print("_ _ _ _ _ _")
    driver.save_screenshot("./images/"+str(uuid.uuid4())+".png")
    srch()

def to_inbox():
    driver.get(path_inbox)
    time.sleep(2)
    print(driver.title)
    time.sleep(1)
    inbx()

def to_explore():
    driver.get(path_explore)
    time.sleep(2)
    print(driver.title)
    time.sleep(1)
    xplr()

#profile menu items
def to_profile_page():
    driver.get(path_profile_page)
    time.sleep(2)
    print(driver.title)
    time.sleep(2)
    prpg()

def to_saved():
    driver.get(path_saved)
    time.sleep(2)
    print(driver.title)
    time.sleep(2)
    sved()

def to_settings():
    driver.get(path_edit_settings)
    time.sleep(2)
    print(driver.title)
    time.sleep(3)

def to_switch_acc():
    print(var_ud)
    input_comand()

def to_logout():
    print(var_ud)
    input_comand()

#START
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get(path_home)
print(driver.title)
time.sleep(4)

#SIGNING IN
search = driver.find_element_by_name("username")
search.send_keys(cred.username)
search = driver.find_element_by_name("password")
search.send_keys(cred.password)
search.send_keys(Keys.RETURN)
print("logging in")

#SIGNED IN
print("loggED in")
time.sleep(5)

#CLOSING SAVE-LOGIN-INFO POP-UP
try:
    notNow = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sqdOP.yWX7d.y3zKF")) or EC.element_to_be_clickable((By.CLASS_NAME,"sqdOP.yWX7d.y3zKF"))
    )
    notNow.click()
    print("clicked pop-up-1")
    time.sleep(3)
except:
    print("ERROR at first popUp exiting . . .")
    time.sleep(2)
    driver.quit()

#CLOSING NOTIFICATOIN POPUP
try:
    notNow2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "aOOlW.HoLwm")) or EC.element_to_be_clickable((By.CLASS_NAME,"aOOlW.HoLwm"))
    )
    notNow2.click()
    print("Notifications turned OFF")
    
except:
    print("FAILED : trying to turn off Notifications")
    time.sleep(2)
    driver.quit()

#MISC FUNCTIONS
def help():
    print("")
    print("1. nav - to navigate to a specific page")
    print("2. mod - Activate module")
    print("..")
    print("x.")

def exec_mod():
    ch = input("WHICH MOD TO EXECUTE ? -- ")
    if ch=="1":
        path_trgt = "https://www.instagram.com/direct/t/340282366841710300949128183857631438370"
        driver.get(path_trgt)
        i = 0
        f = 100
        print("starting...")
        print("CLICK target to SPAM")
        time.sleep(5)
        print("S T A R T E D . . .")
        while i<f:
            i += 1
            msg = "Hello"+str(i)
            print(i)
            print("_________")
            #random_time = random.random()
            in_Sec = 1
            time.sleep(in_Sec)
            msg_input = driver.find_elements_by_tag_name("textarea")
            msg_input[0].send_keys(msg)
            msg_input[0].send_keys(Keys.RETURN)
            print("Message SENT")
            time.sleep(3)
    else:
        print("NO SUCH MODs LOADED . . .")
        input_comand()
    print("task completed")
    to_exit()
    # input_comand()

def page_navig():
    name = input("NAVIGATE TO : ")

    if name=="noti":
        print("Case Matched - NOTIFICATIONS")
        to_notifications()
        #UD

    elif name=="home":
        print("Case Matched - HOME PAGE")
        to_home()

    elif name=="srch":
        print("Case Matched - SEARCH")
        to_search()

    elif name=="xplr":
        print("Case Matched - EXPLORE")
        to_explore()

    elif name=="lgot":
        print("Case Matched - LOGOUT")
        to_logout()        

    elif name=="sved":
        print("Case Matched - SAVED")
        to_saved()        

    elif name=="inbx":    
        print("Case Matched - INBOX")        
        to_inbox()

    elif name=="stng":   
        print("Case Matched - SETTINGS")         
        to_settings()

    elif name=="prpg":   
        print("Case Matched - PROFILE PAGE")         
        to_profile_page()

    elif name=="swac":     
        print("Case Matched - SWITCH ACCOUNTS")       
        to_switch_acc()

    elif name=="exit":
        to_exit()
    
    elif name=="nblk":
        print("UN-BLOCKING. . . .")
        un_block()

    else:
        print("")
        print("noti - notifications")
        print("srch - search")
        print("inbx - inbox")
        print("xplr - explore")
        print("prpg - profile page")
        print("sved - saved")
        print("stng - settings")
        print("swac - switch accounts")
        print("lgot - logout")
        print("nblok- unblock")
        print("exit - exit")
        print("")
        page_navig()
        
def input_comand():
    cmnd = input("ENTER YOUR COMMAND HERE :")
    print(cmnd)
    if cmnd=="help":
        help()
        input_comand()
    elif cmnd=="nav":
        page_navig()
    elif cmnd=="stry":
        print("STORY SAVER OF FRIENDS IF FACES NOT RECOGNIZED, DELETE IMAGE SAVED")
        input_comand()
    elif cmnd=="exit":
        to_exit()
    elif cmnd=="gtle":
        get_title()
        input_comand()
    elif cmnd=="auto":
        auto_mode()
    elif cmnd=="mod":
        exec_mod()
        #UD
    else:
        print("N_A")
        input_comand()

def input_comand_V2():
    comnd = input("POWER COMMAND ::--:: ")
    print(comnd)

auto_mode()