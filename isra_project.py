import speech_recognition as sr
import time
import webbrowser
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import sys
import playsound
from gtts import gTTS
import os
import random
import threading
from tkinter import *
from tkinter.ttk import *

#instance of recogniser class
r=sr.Recognizer()
#list acting as global variable
l=[0,0,-1]
sid=[]
t2=[0]
def signcheck(): 
            import pandas as pd
            

            try:
                df=pd.read_excel('userfiles.xlsx')
        
                rown=(df.index[df['username']=='101']).tolist()[0]
                if df['pass'].iloc[rown]=='Y' : 
                               ro=int(df['facebook_id'].iloc[rown])
                               sid.append(df['gmail_id'].iloc[ro])
                               sid.append(df['gmail_pwd'].iloc[ro])
                               sid.append(df['facebook_id'].iloc[ro])
                               sid.append( df['facebook_pwd'].iloc[ro])
                               sid.append( df['instagram_id'].iloc[ro])
                               sid.append( df['instagram_pwd'].iloc[ro])
                               sid.append( df['twitter_id'].iloc[ro])
                               sid.append(df['twitter_pwd'].iloc[ro])
                               l[1]=1
                               l[2]=ro
                                
                    
                               
            except:
                qqq=1
signcheck()    
social_media=['facebook','instagram','twitter','whatsapp','gmail','google']


#ret_speech invokes mic gets input convert to text and returns
def ret_speech() :
    with sr.Microphone() as src : 
        audio=r.listen(src,timeout=3.0)
        audio_text=''
        try : 
            #recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx-works offline
            audio_text=r.recognize_google(audio)
        except sr.UnknownValueError :
            #if couldn't recognize audio
            text_speech('sorry please repeat?')
            audio_text=ret_speech()
            #text_speech("Sorry I couldn't get that mic off")
            
             #change button state function to off
        except sr.RequestError : #if google didnt respond
            text_speech("Either you are not connected or Service is currently down ")
        except sr.WaitTimeoutError : 
            audio_text=ret_speech()
            #text_speech('Timeout try again')
        return audio_text 
def np():
    class Notepad: 
    
        __root = Tk() 
    
        
    
        # default window width and height 
        __thisWidth = 300
        __thisHeight = 300
        __thisTextArea = Text(__root) 
        __thisMenuBar = Menu(__root) 
        __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
        __thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
        __thisHelpMenu = Menu(__thisMenuBar, tearoff=0) 
        
        
        # To add scrollbar 
        __thisScrollBar = Scrollbar(__thisTextArea)     
        __file = None
    
        def __init__(self,**kwargs): 
    
            # Set icon 
            __btn=mic_button = Button(self.__root,text='MIC', command=lambda:self.change_state2(t2[0]))
        
        
        
            __btn.place(relx=0.5, rely=0.05, anchor = CENTER)
            try: 
                    self.__root.wm_iconbitmap("Notepad.ico") 
            except: 
                    pass
    
            # Set window size (the default is 300x300) 
    
            try: 
                self.__thisWidth = kwargs['width'] 
            except KeyError: 
                pass
    
            try: 
                self.__thisHeight = kwargs['height'] 
            except KeyError: 
                pass
    
            # Set the window text 
            self.__root.title("Untitled - Notepad") 
    
            # Center the window 
            screenWidth = self.__root.winfo_screenwidth() 
            screenHeight = self.__root.winfo_screenheight() 
        
            # For left-alling 
            left = (screenWidth / 2) - (self.__thisWidth / 2) 
            
            # For right-allign 
            top = (screenHeight / 2) - (self.__thisHeight /2) 
            
            # For top and bottom 
            self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                                self.__thisHeight, 
                                                left, top)) 
    
            # To make the textarea auto resizable 
            self.__root.grid_rowconfigure(0, weight=1) 
            self.__root.grid_columnconfigure(0, weight=1) 
    
            # Add controls (widget) 
            self.__thisTextArea.grid(ipady=150,sticky =  E + S + W) 
            
            # To open new file 
            self.__thisFileMenu.add_command(label="New", 
                                            command=self.__newFile)     
            
            # To open a already existing file 
            self.__thisFileMenu.add_command(label="Open", 
                                            command=self.__openFile) 
            
            # To save current file 
            self.__thisFileMenu.add_command(label="Save", 
                                            command=self.__saveFile)     
    
            # To create a line in the dialog         
            self.__thisFileMenu.add_separator()                                         
            self.__thisFileMenu.add_command(label="Exit", 
                                            command=self.__quitApplication) 
            self.__thisMenuBar.add_cascade(label="File", 
                                        menu=self.__thisFileMenu)     
            
            # To give a feature of cut 
            self.__thisEditMenu.add_command(label="Cut", 
                                            command=self.__cut)             
        
            # to give a feature of copy     
            self.__thisEditMenu.add_command(label="Copy", 
                                            command=self.__copy)         
            
            # To give a feature of paste 
            self.__thisEditMenu.add_command(label="Paste", 
                                            command=self.__paste)         
            
            # To give a feature of editing 
            self.__thisMenuBar.add_cascade(label="Edit", 
                                        menu=self.__thisEditMenu)     
            
            # To create a feature of description of the notepad 
            self.__thisHelpMenu.add_command(label="About Notepad", 
                                            command=self.__showAbout) 
            self.__thisMenuBar.add_cascade(label="Help", 
                                        menu=self.__thisHelpMenu) 
    
            self.__root.config(menu=self.__thisMenuBar) 
    
            self.__thisScrollBar.pack(side=RIGHT,fill=Y)                     
            
            # Scrollbar will adjust automatically according to the content         
            self.__thisScrollBar.config(command=self.__thisTextArea.yview)     
            self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
        def change_state2(self,i) :
            if i==0 :
                t2[0]=1
                threading.Thread(target=self.hear2).start()
                t2[0]=1
                
            else : 
                t2[0]=0
                text_speech('mic off')
        def hear2(self): 
             
            audio_data=''
            while(t2[0]) : #exit button GUI 
                #self.__thisTextArea.insert(END,audio_data)
                if t2[0]==0 : 
                    break
                try :
                    audio_data=ret_speech()
                except : 
                    try:
                        audio_data=ret_speech()
                    except:
                        continue
                if t2[0]==0 : 
                    break
                #ass_text.insert(END,'\n'+audio_data)#create update user text widget fn
                self.__thisTextArea.insert(END,audio_data)
                        
                #if l[0]==0 : 
                   # mic_button.configure(image=_offmic)    
        def __quitApplication(self): 
            self.__root.destroy() 
            # exit() 
    
        def __showAbout(self): 
            showinfo("ISRA S2T","Speech to Text") 
    
        def __openFile(self): 
            
            self.__file = askopenfilename(defaultextension=".txt", 
                                        filetypes=[("All Files","*.*"), 
                                            ("Text Documents","*.txt")]) 
    
            if self.__file == "": 
                
                # no file to open 
                self.__file = None
            else: 
                
                # Try to open the file 
                # set the window title 
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                self.__thisTextArea.delete(1.0,END) 
    
                file = open(self.__file,"r") 
    
                self.__thisTextArea.insert(1.0,file.read()) 
    
                file.close() 
    
            
        def __newFile(self): 
            self.__root.title("Untitled - Notepad") 
            self.__file = None
            self.__thisTextArea.delete(1.0,END) 
    
        def __saveFile(self): 
    
            if self.__file == None: 
                # Save as new file 
                self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                                defaultextension=".txt", 
                                                filetypes=[("All Files","*.*"), 
                                                    ("Text Documents","*.txt")]) 
    
                if self.__file == "": 
                    self.__file = None
                else: 
                    
                    # Try to save the file 
                    file = open(self.__file,"w") 
                    file.write(self.__thisTextArea.get(1.0,END)) 
                    file.close() 
                    
                    # Change the window title 
                    self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                    
                
            else: 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
    
        def __cut(self): 
            self.__thisTextArea.event_generate("<<Cut>>") 
    
        def __copy(self): 
            self.__thisTextArea.event_generate("<<Copy>>") 
    
        def __paste(self): 
            self.__thisTextArea.event_generate("<<Paste>>") 
    
        def run(self): 
    
            # Run main application 
            self.__root.mainloop() 
    
    
    
    
    # Run main application 
    notepad = Notepad(width=600,height=400) 
    notepad.run()     
#fn to convert text to speech    
def text_speech(tex) : 
    tts=gTTS(text=tex,lang='en')
    r=random.randint(1,100000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
    ass_text.insert(END,'\n'+'ISRA -'+tex)


    
#tells what it can do(to be added at last)    
def social_log(action,soc_media) :
    topost=''
    frend=''

    if l[1]==1:        
        if soc_media=='facebook' :
            if action==1:
                text_speech('sorry that function is not available right now')
            if action==2 : 
                text_speech('Do you want to post only text? answer in yes or no')
                ass_text.insert(END,'\n'+'say(yes/no)')
                ans=ret_speech()
                ass_text.insert(END,'\n'+ans)
                if ans=='yes' : 
                    text_speech('what you want to post?')
                    topost=ret_speech()
                    ass_text.insert(END,'\n'+'TEXT TO POST-'+'"'+topost+'"')
                    
                    text_speech('Do you want to post the text displayed? answer in yes or no')
                    ass_text.insert(END,'\n'+'say (yes/no)')
                    ans=''
                    ans=ret_speech()
                    ass_text.insert(END,'\n'+ans)
                    if ans=='no' : 
                             
                          
                             text_speech('would you like to say it again?')
                             ans2=ret_speech()
                            
                             if ans2=='yes' : 
                                 text_speech('what you want to post?')
    
                                 topost=ret_speech()
                                 ass_text.insert(END,'\n'+'TEXT TO POST-'+'"'+topost+'"')
                                 text_speech('Do you want to post the text displayed? answer in yes or no')
                                 ass_text.insert(END,'\n'+'say (yes/no)')
                                 ans2=ret_speech()
                                 ass_text.insert(END,'\n'+'yes')
    
        
                else : 
                    text_speech('Do you want to post image? answer in yes or no')
                    ans=ret_speech()
                    #complete this
                    
                        #caption           
            text_speech('loging in to face book')
            try :
                driver=webdriver.Chrome()
            except:
                text_speech('please download latest chrome driver to use this feature')
                webbrowser.open_new_tab('https://chromedriver.chromium.org/downloads')
            driver.get('https://facebook.com/login/')
            
            soc_media=''
            emailelement=driver.find_element(By.XPATH,'.//*[@id="email"]')
            emailelement.send_keys(sid[2])
            passelement=driver.find_element(By.XPATH,'.//*[@id="pass"]')
            passelement.send_keys(sid[3])
            signin=driver.find_element_by_id("loginbutton")
            signin.click()
            time.sleep(3)
            driver.find_element_by_css_selector('div._3ixn').click()
            home_button=driver.find_element(By.XPATH,'//*[@id="u_0_c"]/a')
            home_button.click()
            time.sleep(3)
            try:
                driver.find_element_by_css_selector('div._3ixn').click()
            except:
                pass    
            time.sleep(2)
            if action==1 : 
                pass#sending message on facebook also include broadcast
            elif action==2 : 
                statuselem=driver.find_element_by_tag_name('textarea')
                statuselem.click()
                
               
                statuselem.send_keys(topost)
                time.sleep(10)
                try:
                    driver.find_elements_by_css_selector('button')[2].click()
                    time.sleep(5)
                    
                except:
                    time.sleep(5)    
                    driver.close()
        elif soc_media=='instagram' : 
            if action==0 :
                
                
                try :
                    driver=webdriver.Chrome()
                except:
                    text_speech('please download latest chrome driver to use this feature')
                    webbrowser.open_new_tab('https://chromedriver.chromium.org/downloads')
                driver.get('https://www.instagram.com/accounts/login/')
                
                
                time.sleep(3)
                emailelement=driver.find_element_by_name('username')
                
                
                emailelement.send_keys(sid[4])
                passelement=driver.find_element(By.XPATH,'.//*[@id="loginForm"]/div/div[2]/div/label/input')
                passelement.send_keys(sid[5])
                time.sleep(1)
                signin=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
                signin.click()
                    
                time.sleep(3)
                
                try:
                    home=driver.find_element_by_css_selector('svg._8-yf5 ')#(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a/svg')
                    home.click()
                    time.sleep(2)
                except:
                    pass    
                
                try:
                    driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]').click()
                   
                    
                except:
                    pass    
                time.sleep(2)
            if action==1: 
                    
                     
                    text_speech('whom you want to message?')
                    frend=ret_speech()
                    ass_text.insert(END,'\n'+'MESSAGE RECIPIENT-'+'"'+frend+'"')
                    
                    text_speech('Is the displayed name correct?')
                    ass_text.insert(END,'\n'+'say (yes/no)')
                    ans=''
                    ans=ret_speech()
                    ass_text.insert(END,'\n'+ans)
                    if ans=='no' : 
                             
                          
                             text_speech('would you like to say it again?')
                             ans2=ret_speech()
                            
                             if ans2=='yes' : 
                                 text_speech('whom do you want to send message?')
    
                                 frend=ret_speech()
                                 ass_text.insert(END,'\n'+'MESSAGE RECIPIENT-'+'"'+frend+'"')
                    
                                 text_speech('Is the displayed name correct?')
                                 ass_text.insert(END,'\n'+'say (yes/no)')
                                 ans=''
                                 ans=ret_speech()
                                 ass_text.insert(END,'\n'+'yes')
                    text_speech('what you want to message?')
                    topost=ret_speech()
                    ass_text.insert(END,'\n'+'TEXT TO MESSAGE-'+'"'+topost+'"')
                    
                    text_speech('Do you want to send the displayed message?')
                    ass_text.insert(END,'\n'+'say (yes/no)')
                    ans=''
                    ans=ret_speech()
                    ass_text.insert(END,'\n'+ans)
                    if ans=='no' : 
                             
                          
                             text_speech('would you like to say it again?')
                             ans2=ret_speech()
                            
                             if ans2=='yes' : 
                                 text_speech('what you want to post?')
    
                                 topost=ret_speech()
                                 ass_text.insert(END,'\n'+'TEXT TO POST-'+'"'+topost+'"')
                                 text_speech('Do you want to post the text displayed? answer in yes or no')
                                 ass_text.insert(END,'\n'+'say (yes/no)')
                                 ans2=ret_speech()
                                 ass_text.insert(END,'\n'+'yes')  
                    try :
                        driver=webdriver.Chrome()
                    except:
                        text_speech('please download latest chrome driver to use this feature')
                        webbrowser.open_new_tab('https://chromedriver.chromium.org/downloads')
                    driver.get('https://www.instagram.com/accounts/login/')
                    
                    from selenium.webdriver.common.keys import Keys
                    time.sleep(3)
                    emailelement=driver.find_element_by_name('username')
                    
                    
                    emailelement.send_keys(sid[4])
                    passelement=driver.find_element(By.XPATH,'.//*[@id="loginForm"]/div/div[2]/div/label/input')
                    passelement.send_keys(sid[5])
                    time.sleep(1)
                    signin=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
                    signin.click()
                        
                    time.sleep(3)
                    
                    try:
                        home=driver.find_element_by_css_selector('svg._8-yf5 ')#(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a/svg')
                        home.click()
                        time.sleep(2)
                    except:
                        pass    
                    
                    try:
                        driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]').click()
                       
                        
                    except:
                        pass    
                    time.sleep(4)       
                    try : 
                        srch=driver.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]')
                        srch.click()
                        srch=srch.find_element_by_css_selector('input')
                    except : 
                        print('efdszvcdscv')
                        
                    if len(frend)>1 and len(topost)>1:
                        srch.send_keys(frend.lower())
                        time.sleep(2)
                        srch.send_keys(Keys.ENTER)
                        srch.send_keys(Keys.ENTER)
                        time.sleep(2)
                        driver.find_elements_by_css_selector('button')[0].click()
                        time.sleep(2)
                        try:
                            msg=driver.find_element(By.XPATH,'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            
                            msg.send_keys(topost)
                            msg.send_keys(Keys.ENTER)
                        except: 
                            text_speech('Please copy paste your message from israa')
                        
                        time.sleep(2)
                        
                                 
                
    else : 
        text_speech('Please Login to israa account First')
        
        
        
def webdo(data) : 
    
           url='https://www.google.co.in/search?q='+data
           
        
           try :
                webbrowser.open_new_tab(url)
            
           except : 
                text_speech('cannot find a browser')
        
        
def email_send() : 
    pass
#fn to do task as required    
def respond(audio_data) :
    got=0
    audio_data=audio_data.lower()
    audio_data1=audio_data.split(' ')
    if audio_data1[0]=='exit' : 
        text_speech('Bye! have a nice day !')
        l[0]=0
        return 0
    elif audio_data1[0]=='what' :
        if audio_data[5:]=='can you do' or audio_data[5:]=='you do' : 
            text_speech('I can, automate your browser, and handle your social media accounts')
        elif audio_data1[1]=='is' :
            if audio_data1[2]=='your':
                if audio_data1[3]=='name' :
                    text_speech('My name is israa')
            elif audio_data[8:]=='the time' or audio_data[8:12]=='time' :
                text_speech(time.strftime("%H:%M:%S",time.localtime()))
                return 1
            else : 
                webdo(audio_data)
                
    elif audio_data1[0]=='login' :
        if audio_data1[1]=='to' and (audio_data1[2] in social_media) :
            social_log(0,audio_data1[2])
            return 0
            if audio_data1[2]=='my' and (audio_data1[3] in social_media) :
                social_log(0,audio_data1[3])  
                return 0
        elif (audio_data1[1] in social_media) :    
            social_log(0,audio_data1[1])
            return 0
        else : 
                webdo(audio_data)
    elif audio_data1[0]=='send' :
        
        if audio_data1[1]=='email'  :
            
            if audio_data1[2]=='to'  :
                conf=1
                tri=0
                
                while(conf or tri>2) :
                    tri+=1
                    text_speech('would you like to use speech to text for message? confirm by saying yes or no')
                    try :
                        ans=ret_speech()
                        if ans=='yes' : 
                            conf=0
                            emailsend(1)
                            
                        elif ans=='no' :
                            emailsend(0)
                            
                            conf=1
                    except :
                        text_speech('cancelling')
                        return 0
                    if conf==1 : 
                        text_speech('sorry something went wrong')
            else : 
                webdo(audio_data)            
        elif audio_data1[2]=='email'  :
            
            if audio_data1[3]=='to'  :
                conf=1
                tri=0
                
                while(conf or tri>2) :
                    tri+=1
                    text_speech('would you like to use speech to text for message? confirm by saying yes or no')
                    try :
                        ans=ret_speech()
                        if ans=='yes' : 
                            conf=0
                            emailsend(1)
                        elif ans=='no' :
                            emailsend(0)
                            
                            conf=1
                    except :
                        text_speech('cancelling')
                        return 0
                    if conf==1 : 
                        text_speech('sorry something went wrong')  
            else : 
                webdo(audio_data)         
        elif 'message' in audio_data or 'a message' in audio_data  : 
            for item in social_media : 
                if item in audio_data : 
                    social_log(1,item)#1 means login and send message
                    return 0
        else : 
                webdo(audio_data)        
    elif audio_data1[0]=='speech' or (audio_data1[0]=='open' and audio_data1[1]=='speech')  :
              if (audio_data1[1]=='to' and audio_data1[2]=='text')  or (audio_data1[2]=='to' and audio_data1[3]=='text') :
                  l[0]=0
                  np()
                  
                  return 0
    elif audio_data1[0]=='post' : 
        for item in social_media : 
                if item in audio_data : 
                    social_log(2,item)#2 means login and post 
                    return 0
    elif audio_data1[0]=='tell' : 
        if 'about yourself' in audio_data : 
            text_speech('I am israa developed by team Py')
        elif 'time' in audio_data : 
            text_speech((time.strftime("%H:%M:%S",time.localtime())))
        else : 
                webdo(audio_data)    
    elif audio_data1[0]=='search':         
        if audio_data1[1]=='web' or audio_data1[1]=='internet' :
            if len(audio_data1)==2 :
                try :
                    webbrowser.open_new_tab('https://www.google.co.in/search?q=')
                    return 0
                except : 
                    text_speech('cannot find a browser')
            elif audio_data1[2]== 'for' : 
                try :
                    text_speech('Searching, Web')
                    webbrowser.open_new_tab('https://www.google.co.in/search?q='+audio_data1[3])
                    return 0                 
                except : 
                    text_speech('cannot find a browser')
        elif 'internet for' in audio_data or 'web for' in audio_data: 
            tmp=audio_data.find(' for ')
        
            url='https://www.google.co.in/search?q='+audio_data[(tmp+4):]
            try :
                    text_speech('Searching, Web')
                    webbrowser.open_new_tab(url)
                    return 0
                
            except : 
                    text_speech('cannot find a browser')
    else : 
           webdo(audio_data)
           return 0
       
    return 1   
#Main window dimensions
_root = Tk()
_root.title('ISRA')
_root.iconbitmap('ISRA LOGO.ico')
_root.geometry('430x500')
_root.resizable(height = False, width=False)

def _about():
        about = Tk()
        about.title('ISRA')
        about.iconbitmap('ISRA LOGO.ico')
        about.geometry('300x200')
        ab = Label(about, text='Indian Speech Recognition Assistant')
        ab.place(anchor = CENTER, rely=0.15, relx=0.5)
        v = Label(about, text ='Version v1.0 beta')
        v.place(anchor = CENTER ,relx=0.5,rely=0.25)
        c = Label(about, text='Creators: Varun Bhatnagar and Tushar Garg')
        c.place(anchor = CENTER,relx=0.5,rely=0.75)
        
def _help():
        help = Tk()
        help.title('ISRA')
        help.iconbitmap('ISRA LOGO.ico')
        help.geometry('300x50')
        h = Label(help, text='It is a simple program so there is no need for help.')
        h.pack()
def sigform(user1):
    from tkinter.messagebox import askyesno
    from tkinter.messagebox import showinfo
    #import tkcalendar 
    #import threading
    
    q = [0]
    m = [0]
    n = [0]
    o = [0]
    p = [0]
    
    #main window
    sgfrm = Tk()
    sgfrm.title('Sign Up')
    #sgfrm.iconbitmap('C:\ISRA\ISRA LOGO.ico')
    sgfrm.geometry('600x680')
    sgfrm.resizable(height = True, width=False)
    
    #main window scroll
    #form_scroll = tk.Scrollbar(orient="vertical")
    #form_scroll.grid(row = 1, column = 5, sticky = 'ns', in_ = sgfrm)
    
    #sgfrm.config(yscrollcommand = form_scroll.set)
    #form_scroll.config(command = sgfrm.yview)
    
    #New account label
    na = Label(sgfrm, text='New Account!', font=("Verdana",25, "bold"))
    na.grid(row = 1, column = 1, columnspan=2, padx = 15, pady = 15)
    
    #logo label
    #logopic = PhotoImage(file = 'ISRA LOGO.png')
    #logophoto = logopic.subsample(2,2)
    
    logo_photo = Label(sgfrm)
    #logo_photo.config(image = logophoto)
    logo_photo.grid(row = 1, column = 4, rowspan = 2)
    
    #personal info label
    head1 = Label(sgfrm, text='Personal Information', font=("Verdana",11, "bold"))
    head1.grid(row = 2, column = 1, columnspan=2, padx = 5, pady = 15)
    
    #name input
    first_name = StringVar()
    firstname = Label(sgfrm, text = 'First Name', font = ("Verdana", 11))
    firstname.grid(row = 3, column = 1, padx=5, pady=5)
    
    firstname_entry = Entry(sgfrm, textvariable = first_name)
    firstname_entry.config(width = 25)
    firstname_entry.grid(row = 3, column = 2)
    
    last_name = StringVar()
    lastname = Label(sgfrm, text = 'Last Name', font = ("Verdana", 11))
    lastname.grid(row = 3, column = 3, padx=5, pady=5)
    
    lastname_entry = Entry(sgfrm, textvariable = last_name)
    lastname_entry.config(width = 25)
    lastname_entry.grid(row = 3, column = 4)
    
    #date of birth input
    dob = Label(sgfrm, text = 'Date of Birth', font = ("Verdana", 11))
    dob.grid(row = 4, column = 1, padx=5)
    
    def birthdate():
        date = Tk()
        date.title('Date of Birth')
        #date.iconbitmap('C:\ISRA\ISRA LOGO.ico')
        date.resizable(height = False, width=False)
        
        cal = Calendar(date, selectmode = "day", year=2020, month=1, day=1)
        cal.pack(fill = "both", expand = True)
        
        date_of_birth = StringVar()
        date_of_birth = cal.get_date()
        
        style = Style()
        style.configure('ok.TButton', font =('Verdana', "bold"))
        Ok_button = Button(date, text='Ok', style='ok.TButton', command = date.destroy)
        Ok_button.pack(side = 'bottom')
        
        dob_entry.config(textvariable = date_of_birth)
    
        date.mainloop()
     
    f_dob = Frame(sgfrm)
    f_dob.grid(row = 4, column = 2, padx=5, pady=5)
    
    dob_entry = Entry(f_dob)
    dob_entry.config(width = 17)
    dob_entry.pack(side = 'left')
    
    style = Style()
    style.configure('dob.TButton', font =('Verdana', 8, "bold"))
    dob_button = Button(f_dob, text='DOB', style='dob.TButton', command = birthdate)
    dob_button.config(width = 5)
    dob_button.pack(side='right')
    
    #gender input
    gender = Label(sgfrm, text = 'Gender', font = ("Verdana", 11))
    gender.grid(row = 4, column = 3, padx=5, pady=5)
    
    gen_der = StringVar() 
    genderchoosen = Combobox(sgfrm, width = 22, textvariable = gen_der)
    genderchoosen['values'] = ('Male', 'Female', 'Others') 
      
    genderchoosen.grid(column = 4, row = 4) 
    genderchoosen.current()
    
    #email input
    email_ID_pi = StringVar()
    emailID_pi = Label(sgfrm, text = 'E-Mail ID', font = ("Verdana", 11))
    emailID_pi.grid(row = 5, column = 1, padx=5, pady=5)
    
    emailId_pi_entry = Entry(sgfrm, textvariable = email_ID_pi)
    emailId_pi_entry.config(width = 25)
    emailId_pi_entry.grid(row = 5, column = 2)
    
    #phone number input
    contact_no = StringVar()
    contactno = Label(sgfrm, text = 'Contact No.', font = ("Verdana", 11))
    contactno.grid(row = 5, column = 3, padx=5, pady=5)
    
    contactno_entry = Entry(sgfrm, textvariabl = contact_no)
    contactno_entry.config(width = 25)
    contactno_entry.grid(row = 5, column = 4)
    
    #bot credentials heading
    head2 = Label(sgfrm, text='Social Media Credentials', font=("Verdana",11, "bold"))
    head2.grid(row = 6, column = 1, columnspan=2, padx = 5, pady = 15)
    
    #asking for email management
    femail = Frame(sgfrm)
    femail.grid(row = 7, column = 1, columnspan = 2, padx=5, pady=5)
    
    emailask = Label(femail, text = 'Want me to manage your emails?', font = ("Verdana", 9))
    emailask.pack(side = "left")
    def email_ask_yes():
        emailId_entry['state'] = "Normal"
        emailPwd_entry['state'] = "Normal"
        
    def email_ask_no():
        emailId_entry['state'] = "disabled"
        emailPwd_entry['state'] = "disabled"
        
    def email_ask(i):
        if i==0 :
            q[0]=1
            #threading.Thread(target=email_ask_yes).start()
            email_ask_yes()
            q[0]=1
            emailask_button.configure(text = "No")
        else : 
            q[0]=0
            emailask_button.configure(text = "Yes")
            q[0]=0
            #threading.Thread(target=email_ask_no).start()
            email_ask_no()
    
    style = Style()
    style.configure('email.TButton', font =('Verdana', 7, "bold"))
    emailask_button = Button(femail, text='Yes', style='email.TButton', command = lambda:email_ask(q[0]))
    emailask_button.config(width = 5)
    emailask_button.pack(side='right')
    
    email_ID = StringVar()
    emailID = Label(sgfrm, text = 'E-Mail ID', font = ("Verdana", 11))
    emailID.grid(row = 8, column = 1, padx=5, pady=5)
    
    emailId_entry = Entry(sgfrm, textvariable = email_ID, state = "disabled")
    emailId_entry.config(width = 25)
    emailId_entry.grid(row = 8, column = 2)
    
    email_Pwd = StringVar()
    emailPwd = Label(sgfrm, text = 'Password', font = ("Verdana", 11))
    emailPwd.grid(row = 8, column = 3, padx=5, pady=5)
    
    emailPwd_entry = Entry(sgfrm, textvariable = email_Pwd, state = "disabled")
    emailPwd_entry.config(width = 25)
    emailPwd_entry.grid(row = 8, column = 4)
    
    #asking for facebook management
    ffb = Frame(sgfrm)
    ffb.grid(row = 9, column = 1, columnspan = 2, padx=5, pady=5)
    
    fbask = Label(ffb, text = 'Want me to manage your Facebook?', font = ("Verdana", 9))
    fbask.pack(side = "left")
    
    def fb_ask_yes():
        fbId_entry['state'] = "Normal"
        fbPwd_entry['state'] = "Normal"
        
    def fb_ask_no():
        fbId_entry['state'] = "disabled"
        fbPwd_entry['state'] = "disabled"
        
    def fb_ask(i):
        if i==0 :
            m[0]=1
            #threading.Thread(target=fb_ask_yes).start()
            fb_ask_yes()
            m[0]=1
            fbask_button.configure(text = "No")
        else : 
            m[0]=0
            fbask_button.configure(text = "Yes")
            m[0]=0
            #threading.Thread(target=fb_ask_no).start()
            fb_ask_no()
    
    style = Style()
    style.configure('fb.TButton', font =('Verdana', 7, "bold"))
    fbask_button = Button(ffb, text='Yes', style='fb.TButton', command = lambda:fb_ask(m[0]))
    fbask_button.config(width = 5)
    fbask_button.pack(side='right')
    
    fb_ID = StringVar()
    fbID = Label(sgfrm, text = 'Facebook ID', font = ("Verdana", 11))
    fbID.grid(row = 10, column = 1, padx=5, pady=5)
    
    fbId_entry = Entry(sgfrm, textvariable = fb_ID, state = "disabled")
    fbId_entry.config(width = 25)
    fbId_entry.grid(row = 10, column = 2)
    
    fb_Pwd = StringVar()
    fbPwd = Label(sgfrm, text = 'Password', font = ("Verdana", 11))
    fbPwd.grid(row = 10, column = 3, padx=5, pady=5)
    
    fbPwd_entry = Entry(sgfrm, textvariable = fb_Pwd, state = "disabled")
    fbPwd_entry.config(width = 25)
    fbPwd_entry.grid(row = 10, column = 4)
    
    #asking for instagram management
    finsta = Frame(sgfrm)
    finsta.grid(row = 11, column = 1, columnspan = 2, padx=5, pady=5)
    
    instaask = Label(finsta, text = 'Want me to manage your Instagram?', font = ("Verdana", 9))
    instaask.pack(side = "left")
    
    def insta_ask_yes():
        instaID_entry['state'] = "Normal"
        instaPwd_entry['state'] = "Normal"
        
    def insta_ask_no():
        instaID_entry['state'] = "disabled"
        instaPwd_entry['state'] = "disabled"
        
    def insta_ask(i):
        if i==0 :
            n[0]=1
            #threading.Thread(target=insta_ask_yes).start()
            insta_ask_yes()
            n[0]=1
            instaask_button.configure(text = "No")
        else : 
            n[0]=0
            instaask_button.configure(text = "Yes")
            n[0]=0
            #threading.Thread(target=insta_ask_no).start()
            insta_ask_no()
    
    style = Style()
    style.configure('insta.TButton', font =('Verdana', 7, "bold"))
    instaask_button = Button(finsta, text='Yes', style='insta.TButton', command = lambda:insta_ask(n[0]))
    instaask_button.config(width = 5)
    instaask_button.pack(side='right')
    
    insta_ID = StringVar()
    instaID = Label(sgfrm, text = 'Instagram ID', font = ("Verdana", 11))
    instaID.grid(row = 12, column = 1, padx=5, pady=5)
    
    instaID_entry = Entry(sgfrm, textvariable = insta_ID, state = "disabled")
    instaID_entry.config(width = 25)
    instaID_entry.grid(row = 12, column = 2)
    
    insta_Pwd = StringVar()
    instaPwd = Label(sgfrm, text = 'Password', font = ("Verdana", 11))
    instaPwd.grid(row = 12, column = 3, padx=5, pady=5)
    
    instaPwd_entry = Entry(sgfrm, textvariable = insta_Pwd, state = "disabled")
    instaPwd_entry.config(width = 25)
    instaPwd_entry.grid(row = 12, column = 4)
    
    #asking for twitter management
    ftweet = Frame(sgfrm)
    ftweet.grid(row = 13, column = 1, columnspan = 2, padx=5, pady=5)
    
    tweetask = Label(ftweet, text = 'Want me to manage your Twitter?', font = ("Verdana", 9))
    tweetask.pack(side = "left")
    
    def tweet_ask_yes():
        twitterID_entry['state'] = "Normal"
        twitterPwd_entry['state'] = "Normal"
        
    def tweet_ask_no():
        twitterID_entry['state'] = "disabled"
        twitterPwd_entry['state'] = "disabled"
        
    def tweet_ask(i):
        if i==0 :
            o[0]=1
            #threading.Thread(target=tweet_ask_yes).start()
            tweet_ask_yes()
            o[0]=1
            tweetask_button.configure(text = "No")
        else : 
            o[0]=0
            tweetask_button.configure(text = "Yes")
            o[0]=0
            #threading.Thread(target=tweet_ask_no).start()
            tweet_ask_no()
    
    style = Style()
    style.configure('tw.TButton', font =('Verdana', 7, "bold"))
    tweetask_button = Button(ftweet, text='Yes', style='tw.TButton', command = lambda:tweet_ask(o[0]))
    tweetask_button.config(width = 5)
    tweetask_button.pack(side='right')
    
    twitter_ID = StringVar()
    twitterID = Label(sgfrm, text = 'Twitter ID', font = ("Verdana", 11))
    twitterID.grid(row = 14, column = 1, padx=5, pady=5)
    
    twitterID_entry = Entry(sgfrm, textvariable = twitter_ID, state = "disabled")
    twitterID_entry.config(width = 25)
    twitterID_entry.grid(row = 14, column = 2)
    
    twitter_Pwd = StringVar()
    twitterPwd = Label(sgfrm, text = 'Password', font = ("Verdana", 11))
    twitterPwd.grid(row = 14, column = 3, padx=5, pady=5)
    
    twitterPwd_entry = Entry(sgfrm, textvariable = twitter_Pwd, state = "disabled")
    twitterPwd_entry.config(width = 25)
    twitterPwd_entry.grid(row = 14, column = 4)
    
    #whatsapp_ID = StringVar()
    #whatsappID = Label(sgfrm, text = 'WhatsApp No.', font = ("Verdana", 11))
    #whatsappID.grid(row = 12, column = 1, padx=5, pady=5)
    
    #whatsappId_entry = Entry(sgfrm, textvariable = whatsapp_ID, state = "disabled")
    #whatsappId_entry.config(width = 25)
    #whatsappId_entry.grid(row = 12, column = 2)
    
    #email_Pwd = StringVar()
    #emailPwd = Label(sgfrm, text = 'First Name', font = ("Verdana", 11))
    #emailPwd.grid(row = 4, column = 3, padx=5)
    
    #emailPwd_entry = Entry(sgfrm, textvariable = email_ID)
    #emailPwd_entry.config(width = 25)
    #emailPwd_entry.grid(row = 4, column = 4)
    
    #asking for linkedin management
#    flinkedin = Frame(sgfrm)
 #   flinkedin.grid(row = 15, column = 1, columnspan = 2, padx=5, pady=5)
    
 #   linkedinask = Label(flinkedin, text = 'Want me to manage your LinkedIn?', font = ("Verdana", 9))
  #  linkedinask.pack(side = "left")
   
  #  def linkedin_ask_yes():
   #     linkedinId_entry['state'] = "Normal"
   #     linkedinPwd_entry['state'] = "Normal"
        
   # def linkedin_ask_no():
    #    linkedinId_entry['state'] = "disabled"
     #   linkedinPwd_entry['state'] = "disabled"
        
   # def linkedin_ask(i):
    #    if i==0 :
     #       p[0]=1
      #     threading.Thread(target=linkedin_ask_yes).start()
       #     p[0]=1
        #    linkedinask_button.configure(text = "No")
        #else : 
         #   p[0]=0
          #  linkedinask_button.configure(text = "Yes")
           # p[0]=0
            #threading.Thread(target=linkedin_ask_no).start()
    
 #   style = Style()
  #  style.configure('linked.TButton', font =('Verdana', 7, "bold"))
   # linkedinask_button = Button(flinkedin, text='Yes', style='linked.TButton', command = lambda:linkedin_ask(p[0]))
   # linkedinask_button.config(width = 5)
    #linkedinask_button.pack(side='right')
    
   # linkedin_ID = StringVar()
   # linkedinID = Label(sgfrm, text = 'LinkedIn ID', font = ("Verdana", 11))
    #linkedinID.grid(row = 16, column = 1, padx=5, pady=5)
    
   # linkedinId_entry = Entry(sgfrm, textvariable = linkedin_ID, state = "disabled")
    #linkedinId_entry.config(width = 25)
    #linkedinId_entry.grid(row = 16, column = 2)
    
    #linkedin_Pwd = StringVar()
    #linkedinPwd = Label(sgfrm, text = 'Password', font = ("Verdana", 11))
    #linkedinPwd.grid(row = 16, column = 3, padx=5, pady=5)
    
    #linkedinPwd_entry = Entry(sgfrm, textvariable = linkedin_Pwd, state = "disabled")
    #linkedinPwd_entry.config(width = 25)
    #linkedinPwd_entry.grid(row = 16, column = 4)
    
    def gtvl2():
        
        askyesno('Confirmation!', 'Do you want to submit your information?')
        emailid=emailId_entry.get()
        emailpwd=emailPwd_entry.get()
        fbid=fbId_entry.get()
        
        fbpwd=fbPwd_entry.get()
        
        
        insid=instaID_entry.get()
        inspwd=instaPwd_entry.get()
        twitid=twitterID_entry.get()
        twitpwd=twitterPwd_entry.get()
        
        import pandas as pd
        
        
        df=pd.read_excel('userfiles.xlsx',index_col=0)
       
        
          
        rown=(df.index[df['username']==user1]).tolist()[0]
        df['gmail_id'].iloc[rown]=emailid
        df['gmail_pwd'].iloc[rown]=emailpwd
        df['facebook_id'].iloc[rown]=fbid
        df['facebook_pwd'].iloc[rown]=fbpwd
        df['instagram_id'].iloc[rown]=insid
        df['instagram_pwd'].iloc[rown]=inspwd
        df['twitter_id'].iloc[rown]=twitid
        df['twitter_pwd'].iloc[rown]=twitpwd

        
        writer=pd.ExcelWriter('userfiles.xlsx')
        df.to_excel(writer)
        writer.save()
        showinfo(message='Signed Up Please Login')
        sgfrm.destroy()
        
    style = Style()
    style.configure('submit.TButton', font =('Verdana', 11, "bold"))
    submit_button = Button(sgfrm, text='Submit', style='submit.TButton', command = gtvl2)
    submit_button.config(width = 15)
    submit_button.grid(row = 17, column = 2, columnspan=2, padx=10, pady =20)

           
def signupw():
    from tkinter.messagebox import askyesnocancel
    from tkinter.messagebox import showerror
    from tkinter import filedialog
    from PIL import ImageTk,Image
    sgnuw = Tk()
    sgnuw.title('Sign Up')
    #sgnuw.iconbitmap('C:\ISRA\ISRA LOGO.ico')
    sgnuw.geometry('350x350')
    sgnuw.resizable(height = False, width=False)
    user1='ferf'
    #edit profile picture window
    def select_profile():
        sgnuw.filename = filedialog.askopenfilename(initialdir = "/Pictures", title = 'Select a file', filetype = (('png files', '.png'), ("jpg files", '.jpg'), ("jpeg files", '.jpeg')))
        newimage = Image.open(sgnuw.filename)
        resize_newimage = newimage.resize((95,85), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resize_newimage)
        userprofile.configure(image = new_image)
    
    #userimage = Image.open("ONLY LOGO.png")
    #resize_userimage = userimage.resize((95,85), Image.ANTIALIAS)
    #user_image = ImageTk.PhotoImage(resize_userimage)
    
    #dummyimage = Image.open("avatar dummy.png")
    #resize_dummyimage = dummyimage.resize((95,85), Image.ANTIALIAS)
    #dummy_image = ImageTk.PhotoImage(resize_dummyimage)
    
    def profile_change():
        result = askyesnocancel('Edit profile picture', 'Press Yes to change, No to remove and Cancel to abort.', icon = 'info')
        if result == False:
            userprofile.configure(image = dummy_image)
        elif result == True:
            select_profile()
      
    
    #userprofile = Button(sgnuw, height=100, width=80)
    userprofile = Button(sgnuw, width=17,  command = profile_change)#Button(sgnuw, width=17, image = user_image, command = profile_change)
    userprofile.place(relx=0.5, rely=0.15, anchor=CENTER)
    
    un = Label(sgnuw, text='Enter your Username')
    un.configure(font=("Verdana",10))
    un.place(relx=0.5, rely=0.35, anchor=CENTER)
    
    username_var = StringVar()
    
    username_entry = Entry(sgnuw, textvariable = username_var)
    username_entry.config(width = 25)
    username_entry.place(relx=0.5,rely=0.41,anchor=CENTER)
    
    eg = Label(sgnuw, text='for eg: gargtushar')
    eg.configure(font=("Verdana",7))
    eg.place(relx=0.5, rely=0.47, anchor=CENTER)
    
    pw = Label(sgnuw, text='Enter your Password')
    pw.configure(font=("Verdana",10))
    pw.place(relx=0.5, rely=0.53, anchor=CENTER)
    
    password_var = StringVar()
    
    password_entry = Entry(sgnuw, textvariable = password_var)
    password_entry.config(width = 25)
    password_entry.place(relx=0.5,rely=0.59,anchor=CENTER)
    
    pwconf = Label(sgnuw, text='Confirm Password')
    pwconf.configure(font=("Verdana",10))
    pwconf.place(relx=0.5, rely=0.69, anchor=CENTER)
    
    pwdconf_var = StringVar()
    
    pwdconf_entry = Entry(sgnuw, textvariable = pwdconf_var, show = "*")
    pwdconf_entry.config(width = 25)
    pwdconf_entry.place(relx=0.5,rely=0.75,anchor=CENTER)
    
    style = Style()
    style.configure('su.TButton', font =('Verdana', 10, "bold"))
    def gtvl():
        
        user1=username_entry.get()
        
        pwd1=password_entry.get()
        
        
        pwd2=pwdconf_entry.get()
        
        if pwd1==pwd2 :
            import pandas as pd
            
            try:
                df=pd.read_excel('userfiles.xlsx')
            except:
                df=pd.DataFrame(columns=['username','pass','facebook_id','facebook_pwd',
                                    'instagram_id','instagram_pwd','twitter_id',
                                    'twitter_pwd','gmail_id','gmail_pwd'])
                dt=  pd.DataFrame({'username':['101'],'pass':['N'],'facebook_id':[None],'facebook_pwd':[None],
                                     'instagram_id':[None],'instagram_pwd':[None],'twitter_id':[None],
                                     'twitter_pwd':[None],'gmail_id':[None],'gmail_pwd':[None]})  
                df=df.append(dt,ignore_index=True)
            if user1 in list(df['username']):
                showerror(title='user_error',message='User exists try different username!!')
            else :    
                df_tmp=pd.DataFrame({'username':[user1],'pass':[pwd1],'facebook_id':[None],'facebook_pwd':[None],
                                     'instagram_id':[None],'instagram_pwd':[None],'twitter_id':[None],
                                     'twitter_pwd':[None],'gmail_id':[None],'gmail_pwd':[None]})
                df=df.append(df_tmp,ignore_index=True)
                
                writer=pd.ExcelWriter('userfiles.xlsx')
                df.to_excel(writer)
                writer.save()
                sgnuw.destroy()
                sigform(user1)
        else : 
            showerror(title='password_error',message='Passwords do not match')
            
    signup_button = Button(sgnuw, text='Sign Up', style='su.TButton',command=gtvl)
    signup_button.place(relx=0.5, rely=0.87, anchor = CENTER)
    signup_button.config( width = 7)
    
def accwin(usr1):
    acwin = Tk()
    acwin.title('Signed-In')
    #acwin.iconbitmap('C:\ISRA\ISRA LOGO.ico')
    acwin.geometry('350x350')
    acwin.resizable(height = False, width=False)
    
    #dum_image = PhotoImage(file='avatar dummy.png')
    #dum_im_age = dum_image.subsample(2,2)
    
    #first time window
    #dummy = Label(acwin, image = dum_im_age)
    #dummy.place(relx=0.5, rely=0.25, anchor=CENTER)
    
    hey = Label(acwin, text='Hey '+usr1)
    hey.configure(font=("Verdana",20))
    hey.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    new = Label(acwin, text='Not'+usr1+'?')
    new.configure(font=("Verdana",9))
    new.place(relx=0.4, rely=0.8, anchor=CENTER)
    style = Style()
    style.configure('an.TButton', font =('Verdana', 8, "bold"))
    
    another_button = Button(acwin, text='Sign In', style='an.TButton')
    another_button.place(relx=0.6, rely=0.8, anchor = CENTER)
    another_button.config( width = 6)
    
        
def signinw():
        from tkinter.messagebox import askyesno
        from tkinter.messagebox import showerror


        lgin = Tk()
        lgin.title('ISRA')
        #root.iconbitmap('C:\ISRA\ISRA LOGO.ico')
        lgin.geometry('350x350')
        lgin.resizable(height = False, width=False)
        
        #first time window
        misc = Label(lgin, text='Login Here!')
        misc.configure(font=("Verdana",20))
        misc.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        un = Label(lgin, text='Username')
        un.configure(font=("Verdana",10))
        un.place(relx=0.5, rely=0.24, anchor=CENTER)
        
        username_var = StringVar()
        
        username_entry = Entry(lgin, textvariable = username_var)
        username_entry.config(width = 35)
        username_entry.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        pw = Label(lgin, text='Password')
        pw.configure(font=("Verdana",10))
        pw.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        password_var = StringVar()
        
        password_entry = Entry(lgin, textvariable = password_var,show="*")
        password_entry.config(width = 35)
        password_entry.place(relx=0.5,rely=0.46,anchor=CENTER)
        
        
       
        def getv2(): 
            askyesno('Confirmation','Do you want to log in?')
            usr=username_entry.get()
            psd=password_entry.get()
            import pandas as pd
            

            try:
                df=pd.read_excel('userfiles.xlsx')
                    
                if usr not in list(df['username']):
                        
                        showerror(title='user_error',message='User does not exist!! try different username!!')  
                else : 
                        if not psd :
                           showerror(title='password_error',message='password is required!!')  
                        else : 
                           rown=(df.index[df['username']==usr]).tolist()[0]
                           if df['pass'].iloc[rown]==psd : 
                               
                               l[1]=1
                               l[2]=rown
                               ro=(df.index[df['username']=='101']).tolist()[0]
                               df['pass'].iloc[ro]='Y'
                               df['facebook_id'].iloc[ro]=str(rown)
                               writer=pd.ExcelWriter('userfiles.xlsx')
                               df.to_excel(writer)
                               writer.save()
                               lgin.destroy()
                               accwin(usr)
                               signcheck()
                           else : 
                               showerror(title='password_error',message='password is incorrect!!')  
            except:
                showerror(title='no_user',message='user does not exist!! signup first')
                lgin.destroy()
                signupw()  
            
                       
                       
                       
                   
                    
                   
                    
        style = Style()
        style.configure('TButton', font =('Verdana', 10, "bold"))
        login_button = Button(lgin, text='Login', style='TButton', command = getv2)        
        login_button.place(relx=0.5, rely=0.57, anchor = CENTER)
        login_button.config( width = 15)
        
        signup = Label(lgin, text='New User?')
        signup.configure(font=("Verdana",9))
        signup.place(relx=0.4, rely=0.8, anchor=CENTER)
        
        style.configure('su.TButton', font =('Verdana', 8, "bold"))

            
            
        
        signup_button = Button(lgin, text='Sign Up', style='su.TButton',command=signupw)
        signup_button.place(relx=0.6, rely=0.8, anchor = CENTER)
        signup_button.config( width = 7)
        
        
        
 #adding assistant text area
        
ass_text = Text(_root, height = 18 , width=48)
ass_text.place(anchor = CENTER, relx=0.48,rely=0.49)
scroll = Scrollbar(_root)
scroll.pack(side = RIGHT, fill = Y)
ass_text.config(yscrollcommand = scroll.set)
scroll.config(command = ass_text.yview)

#Web search entry
search_lab = Label(_root, text = 'Search Web: ', font = ("Times New Roman", 10, "bold"))
search_lab.place(relx=0.1 , rely = 0.85, anchor = CENTER)
search_entry = Entry(_root)
search_entry.config(width = 53)
search_entry.place(relx=0.56,rely=0.85,anchor=CENTER)

#hear fn invoked as thread after you Activate mic
def hear(): 
    try :
        text_speech('Hi!,How may, I help you?')  
    except : 
        ass_text.insert(END,'\n Please check your internet connection!!')
        l[0]=0
    if(l[0]) :    
        ass_text.insert(END,'\nHi, I am ISRA how may I help you?') 

    while(l[0]) : #exit button GUI 
        ass_text.insert(END,'\nListening...')
        if l[0]==0 : 
            break
        try :
            audio_data=ret_speech()
        except : 
            try:
                audio_data=ret_speech()
            except:
                continue
        if l[0]==0 : 
            break
        ass_text.insert(END,'\n'+audio_data)#create update user text widget fn
        try :
            l[0]=respond(audio_data)
        except:
            text_speech('something went wrong')
            l[0]=0
                
        if l[0]==0 : 
            mic_button.configure(image=_offmic)
    
 #changing state(on/off) of mic using global list variable

onmic = PhotoImage(file = 'MIC.png')
_onmic = onmic.subsample(4,4)

offmic = PhotoImage(file = 'offmic.png')
_offmic = offmic.subsample(4,4)
        
def change_state(i) :
    if i==0 :
        l[0]=1
        threading.Thread(target=hear).start()
        l[0]=1
        mic_button.configure(image = _onmic)
    else : 
        l[0]=0
        text_speech('mic off')
        mic_button.configure(image = _offmic)
#making menus
my_menu = Menu(_root)

_root.config(menu = my_menu)

my_menu.add_cascade(label = 'Settings')

options = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = 'Account', menu = options)
options.add_command(label = 'Sign in',command=signinw)
options.add_command(label = 'General')
options.add_command(label = 'Privacy and Security')
options.add_separator()
options.add_command(label = 'Sign Out')

my_menu.add_cascade(label = 'Help', command = _help)

my_menu.add_cascade(label = 'About', command = _about)

    #Making Exit button
#Making Exit button
style = Style()
style.configure('Exit.TButton', font =('Showcard Gothic', 10))

exit_button = Button(_root, text='Exit', style = 'Exit.TButton', command = _root.destroy)
exit_button.place(relx=0.5, rely=0.95, anchor = CENTER)
exit_button.config( width = 25)

    #Making Mic button

#mic photo not working have to fix
mic_button = Button(_root, image = _offmic, command=lambda:change_state(l[0]))#mic_button = Button(_root, image = _photo,command=hear)
mic_button.place(relx=0.5, rely=0.1, anchor = CENTER)

_root.mainloop()
