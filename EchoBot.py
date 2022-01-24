import logging
from time import sleep
from selenium import webdriver,common
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename="EchoBot_logs.log",format='%(asctime)s %(levelname)-8s %(name)s : %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

class EchoBot:

    def __init__(self,username,password):
        logging.info("Starting Bot")
        print("Starting Bot - Login")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://instagram.com/")
        self.driver.maximize_window()
        logging.info("Bot started successfully via Chrome")
        sleep(3)
        if self.driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]"):
            logging.info("Accept Cookies Popup")
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]").click()
            sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
        sleep(6)

        if self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/div[2]"):
            logging.warning("Save Login Info page Bypass")
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
            sleep(3)

        if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/h2"):
            logging.warning("Turn on Notification Popup Bypass")
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        print("Login Successful")

    def open_chat(self,chat_name = None):

        logging.info("Opening Inbox")
        print("Opening Inbox?")
        if not self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a"):
            logging.error("Account Not logged in on Homescreen")

        else:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
            print("Inbox")
            sleep(7)
            chatlist_div = self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div").find_elements_by_class_name("_4EzTm")
            #print("ChatList Div",chatlist_div)
            chat_list = {}
            #Populate Chat List
            for chat_div in chatlist_div:
                #print(chat_div.tag_name)
                for chat_block in chat_div.find_elements_by_class_name("i0EQd"):
                    #print(chat)
                    for chat in chat_block.find_elements_by_class_name("fDxYl"):
                        #print(chat.text,"  ",chat)
                        chat_list.update({chat.text : chat})
            sleep(5)
            logging.debug("Chat List - ",chat_list)
            print("Chat List - ", chat_list)

            chat = [val for key, val in chat_list.items() if chat_name in key.lower()]
            logging.info("Opening chat",str(chat[0]))
            chat[0].click()
            sleep(5)
            if chat_name is None:
                list(chat_list.values())[0].click()
                sleep(5)
            else:
                print("Specified chat not in chat list")


        

try:
    O_bot = EchoBot("echo_repeat","662747786")
    O_bot.open_chat('talk')
    talkative_o = EchoBot("talkative_omar","662747786")
    talkative_o.open_chat("Omar")

except Exception as e:
    print(" Oops! ",e.__class__," occured")
    sleep(5)

finally:
    logging.debug("======================END OF LOG======================")
    print("Ready to close")

