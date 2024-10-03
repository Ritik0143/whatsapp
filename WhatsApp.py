import pywhatkit as kit
import pandas as pd
import time
import pyautogui

# Read data from CSV file
def read_csv(file_path):
    return pd.read_csv(file_path, dtype={'Phone': str})

# Add country code prefix if not present
def add_country_code(number, country_code='+91'):
    if not number.startswith(country_code):
        return country_code + number
    return number

# Function to send message
def send_message(number, name, msg): 
    try:
        # Personalize message
        personalized_msg = f"Hey {name}, {msg}"
        
        # Send the message instantly
        kit.sendwhatmsg_instantly(number, personalized_msg, wait_time=9)
        print(f"Message sent to {number}")

        # Wait to ensure the message is sent
        time.sleep(5)

        # Locate the message input box to paste the image
        locate_and_send_image()

        return True

    except Exception as e:
        print(f"Failed to send message or image to {number}. Error: {str(e)}")
        return False

# Function to locate the message input box and paste the image
def locate_and_send_image():
    try:
        # Press 'Ctrl + V' to paste the image in the message box (assuming the image is already copied)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(3)  # Give time to upload the image

        # Add the caption
        caption = "Here is a quick design idea for your business, we would love to create a full site for you. Just drop a message to get started!"
        
        # Type the caption
        pyautogui.typewrite(caption)
        time.sleep(3)
        
        # Press 'Enter' to send the image and caption
        pyautogui.press('enter')
        print("Image and caption sent")

        # Wait a bit to ensure the message is sent
        time.sleep(7)

        # Close the current tab (Ctrl + W)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(2)  # Wait a bit to ensure the tab is closed

    except Exception as e:
        print(f"Failed to send image and caption. Error: {str(e)}")

# Function to send messages to multiple numbers
def send_messages_from_csv(csv_file):
    data = read_csv(csv_file)
    
    # Define different messages based on the Type column
    message_templates = {
        0: """ 
        
Makeup artist hain, par abhi tak website nahi banwayi?
🌐 Online bookings ko boost karne ka best tareeka hai ek professional website – jo aapka portfolio aur booking tool dono hoti hai. Social media se zyada, ek website se aap trust build karte hain. 💼

Exclusive offer: Agle 24 ghanton mein website order karein aur paayein 50% ka discount! 
🕒 Jaldi kijiye – clock tick kar rahi hai! ⏳

Just drop a message to get started!! ✉️ """,
        1: """
        Struggling to get more clients as a makeup artist? Without a website, you're missing out on potential bookings.

In today's world, people look for services online. If they can't find your website, they might choose someone else. A website is your professional portfolio, booking tool, and the key to standing out from the competition. Social media isn’t enough – a website builds trust and makes it easy for clients to book your services.

Don’t miss another opportunity. Message today to get started on your professional website!""",
        2: """I just saw your website although your business is all about selling luxury and properties, your current website doesn't describe it well, it doesn't give the sense of luxury and is impacting your brand's online image...

You can see websites which shows luxury

https://philipscheinfeld.com/

We can help you to create such a website... 

Just drop a message to get started..."""
    }
    
    for index, row in data.iterrows():
        name = 'there'  #row['Name']
        
        number = row['Phone']
        message_type = row['Type']  # Assuming the new column is named 'Type'
        
        # Get the message based on the type
        msg = message_templates.get(message_type, "Default message if type not found")

        # Add country code prefix if not present
        number = add_country_code(number)
        
        if send_message(number, name, msg):
            # Delete the row if the message and image were sent successfully
            data.drop(index, inplace=True)
            # Save the updated DataFrame back to the CSV
            data.to_csv(csv_file, index=False)
            print(f"Row {index} deleted and CSV updated.")

# Path to your CSV file
csv_file_path = './data.csv'  # Replace with your actual file path

# Send the messages
send_messages_from_csv(csv_file_path)


