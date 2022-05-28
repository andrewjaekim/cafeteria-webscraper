from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib, ssl
from providers import PROVIDERS

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


""" Using selenium to pull html data from Bruin Cafe """
driver = webdriver.Edge(r'/Users/andrewkim/Downloads/edgedriver_mac64/msedgedriver')
driver.get('https://menu.dining.ucla.edu/Menus/BruinCafe')

""" User defined functions"""
def parse_menu(menu):
    # grab all the items found inside the specified menu
    items = menu.find_elements(By.CLASS_NAME, 'menu-item')

    # create 3 lists
    itemName = []
    itemPrice = []
    itemInfo = []

    # loop through the menu items and store corresponding information inside corresponding list
    for item in items:
        itemName.append(item.find_element(By.CLASS_NAME, 'menu-item-name').text)

        itemPrice.append(item.find_element(By.CLASS_NAME, 'menu-item-price').text)

        # use try-except block to catch exceptions when expected data is not present
        try: 
            itemInfo.append(item.find_element(By.CLASS_NAME, 'menu-item-description').text)
        except Exception as e:
            itemInfo.append("None")

    return itemName, itemPrice, itemInfo

def print_full_menu():
    print("Bruin Cafe Menu")
    print("~~ LUNCH SPECIAL ~~")

    for (a, b, c) in zip(lunchSpecialName, lunchSpecialPrice, lunchSpecialInfo):
        print(a, b)
        print("Description:", c, '\n')


    print("~~ PIZZA ~~")

    for (a, b, c) in zip(pizzaName, pizzaPrice, pizzaInfo):
        print(a, b)
        print("Description:", c, '\n')

    print("~~ TOASTED SANDWICHES ~~")

    for (a, b, c) in zip(toastedSandwichName, toastedSandwichPrice, toastedSandwichInfo):
        print(a, b)
        print("Description:", c, '\n')

    print("~~ COLD SANDWICHES ~~")

    for (a, b, c) in zip(coldSandwichName, coldSandwichPrice, coldSandwichInfo):
        print(a, b)
        print("Description:", c, '\n')

    print("~~ TOASTED OR COLD SANDWICHES ~~")

    for (a, b, c) in zip(toastedColdSandwichName, toastedColdSandwichPrice, toastedColdSandwichInfo):
        print(a, b)
        print("Description:", c, '\n')

    print("~~ WRAPS ~~")

    for (a, b, c) in zip(wrapsName, wrapsPrice, wrapsInfo):
        print(a, b)
        print("Description:", c, '\n')

    print("~~ SALADS ~~")

    for (a, b, c) in zip(saladsName, saladsPrice, saladsInfo):
        print(a, b)
        print("Description:", c, '\n')    

def write_menu_to_file():
    f = open("Bruin-Cafe-Menu.txt", "w")
    f.write("Bruin Cafe Menu\n")

    f.write("\n~~ LUNCH SPECIAL ~~")
    for x in range(len(lunchSpecialName)):
        f.write('\n' + lunchSpecialName[x] + " ")
        f.write(lunchSpecialPrice[x] + '\n')
        f.write("Description: " + lunchSpecialInfo[x] + '\n')


    f.write("\n~~ PIZZA ~~")
    for x in range(len(pizzaName)):
        f.write('\n' + pizzaName[x] + " ")
        f.write(pizzaPrice[x] + '\n')
        f.write("Description: " + pizzaInfo[x] + '\n')

    f.write("\n~~ TOASTED SANDWICHES ~~")
    for x in range(len(toastedSandwichName)):
        f.write('\n' + toastedSandwichName[x] + " ")
        f.write(toastedSandwichPrice[x] + '\n')
        f.write("Description: " + toastedSandwichInfo[x] + '\n')

    f.write("\n~~ COLD SANDWICHES ~~")
    for x in range(len(coldSandwichName)):
        f.write('\n' + coldSandwichName[x] + " ")
        f.write(coldSandwichPrice[x] + '\n')
        f.write("Description: " + coldSandwichInfo[x] + '\n')

    f.write("\n~~ TOASTED OR COLD SANDWICHES ~~")
    for x in range(len(toastedColdSandwichName)):
        f.write('\n' + toastedColdSandwichName[x] + " ")
        f.write(toastedColdSandwichPrice[x] + '\n')
        f.write("Description: " + toastedColdSandwichInfo[x] + '\n')

    f.write("\n~~ WRAPS ~~")
    for x in range(len(wrapsName)):
        f.write('\n' + wrapsName[x] + " ")
        f.write(wrapsPrice[x] + '\n')
        f.write("Description: " + wrapsInfo[x] + '\n')

    f.write("\n~~ SALADS ~~")
    for x in range(len(saladsName)):
        f.write('\n' + saladsName[x] + " ")
        f.write(saladsPrice[x] + '\n')
        f.write("Description: " + saladsInfo[x] + '\n')

    f.close()

""" This function was built by https://www.youtube.com/watch?v=4-ysecoraKo """
def send_mms(number:str, message:str, provider:str, email:str, password:str, subject:str="Bruin Cafe", smtp_server="smtp.gmail.com", smtp_port:int = 465):
    # information of the sender
    sender_email = email
    email_password = password

    # information of the receiver
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("mms")}'

    # MMS message information
    email_message = MIMEMultipart()
    email_message["Subject"] = "Bruin Cafe"
    email_message["To"] = receiver_email
    email_message["From"] = email
    email_message.attach(MIMEText(message, "plain"))
    text = email_message.as_string()

    # Sending the message to the corresponding carrier. From there it will conver the email to a text to the desired phone number
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, text)
    return

""" copying the style-entree path """
lunchSpecialMenu = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div/div[2]/div[2]/div[1]')

pizzaMenu = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div/div[2]/div[2]/div[2]')

toastedSandwichesMenu = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div/div[2]/div[3]/div[1]')

coldSandwichesMenu = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div/div[2]/div[4]/div[1]')

toastedOrColdSandwichesMenu = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div/div[2]/div[4]/div[3]')

wrapsMenu = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div/div[2]/div[4]/div[4]')

saladsMenu = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div/div[2]/div[5]/div'
)

""" Parsing the web scraped data for each category """
lunchSpecialName, lunchSpecialPrice, lunchSpecialInfo = parse_menu(lunchSpecialMenu)

pizzaName, pizzaPrice, pizzaInfo = parse_menu(pizzaMenu)

toastedSandwichName, toastedSandwichPrice, toastedSandwichInfo = parse_menu(toastedSandwichesMenu)

coldSandwichName, coldSandwichPrice, coldSandwichInfo = parse_menu(coldSandwichesMenu)

toastedColdSandwichName, toastedColdSandwichPrice, toastedColdSandwichInfo = parse_menu(toastedOrColdSandwichesMenu)

wrapsName, wrapsPrice, wrapsInfo = parse_menu(wrapsMenu)

saladsName, saladsPrice, saladsInfo = parse_menu(saladsMenu)


driver.quit()

""" Main File"""
def main():
    # automatically runs writing menu to file
    write_menu_to_file()

    # print_full_menu()
    print("\nWhat would you like to do?")
    print("Enter 1 to print menu to console")
    print("Enter 2 to send an mms message")
    print("Enter 3 to quit")

    while True:
        command = input("\nEnter a command: ")

        if command == '3':
            break
        elif command == '1':
            print_full_menu()
            print("What would you like to do next?")
            print("Enter 1 to print menu to console")
            print("Enter 2 to send an mms message")
            print("Enter 3 to quit")
        elif command == '2':
            # Read file created and assign it to message
            read_file = open('Bruin-Cafe-Menu.txt', 'r')
            message = read_file.read()

            number = input("Enter in a 10 digit phone number. Only digits: ")
            answer = input("Please select the receiver's provider from the following list: \n1. AT&T\n2. Sprint\n3. T-Mobile\n4. Verizon\nEnter 1-4: ")

            if answer == '1':
                provider = "AT&T"
            elif answer == '2':
                provider = "Sprint"
            elif answer == '3':
                provider = "T-Mobile"
            elif answer == '4':
                provider = "Verizon"

            email = input("Enter the sender's email address: ")
            password = input("Enter the sender's email password: ")
            send_mms(number, message, provider, email, password)
            print("\nWhat would you like to do next?")
            print("Enter 1 to print menu to console")
            print("Enter 2 to send an mms message")
            print("Enter 3 to quit")
        else:
            print("Unrecognized command!")
            print("Enter 1 to print menu to console")
            print("Enter 2 to send an mms message")
            print("Enter 3 to quit")

if __name__ == "__main__":
    main()