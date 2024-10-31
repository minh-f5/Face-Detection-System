import sqlite3
import cv2
import winsound
import smtplib
import getpass
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email settings
SENDER_EMAIL = input("Enter your email: ")
SENDER_PASSWORD = getpass.getpass("Enter your email password (input hidden): ")
RECEIVER_EMAIL = input("Enter the receiver's email: ")


def init_db():
    conn = sqlite3.connect('latecomers.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS latecomers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            arrival_time TEXT,
            date TEXT,
            is_late INTEGER,
            photo_path TEXT
        )
    ''')
    conn.commit()
    conn.close()


def capture_photo(name):
  
    cap = cv2.VideoCapture(0)
    
   
    ret, frame = cap.read()
    if ret:
      
        photo_path = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(photo_path, frame) 
        play_capture_sound()  
    else:
        photo_path = None
    
    cap.release()  #
    return photo_path

def play_capture_sound():
    winsound.PlaySound("camera_capture_sound.wav", winsound.SND_FILENAME)


def send_email_notification(name, arrival_time, photo_path):

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = "Late Arrival Notification"

    body = f"{name} Alert : This person arrived late at {arrival_time}. See attached photo for reference."
    msg.attach(MIMEText(body, 'plain'))

  
    if photo_path:
        attachment = open(photo_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {photo_path}")
        msg.attach(part)

 
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("Email notification sent.")
    except Exception as e:
        print("Error: unable to send the email. Check your credentials and try again.")
        print("Details:", e)
    finally:
        server.quit()


def record_latecomer(name):
    arrival_time = datetime.now()
    weekday = arrival_time.weekday() 
    is_late = 1 if (weekday < 5 and arrival_time.hour >= 9) else 0  # Mon-Fri after 9 AM is late
    
 
    photo_path = capture_photo(name) if is_late else None
    

    conn = sqlite3.connect('latecomers.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO latecomers (name, arrival_time, date, is_late, photo_path)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, arrival_time.strftime('%H:%M:%S'), arrival_time.date(), is_late, photo_path))
    
    conn.commit()
    conn.close()
    
    if is_late:
        print(f"{name} recorded as late at {arrival_time.strftime('%H:%M:%S')} with photo taken.")
        send_email_notification(name, arrival_time.strftime('%H:%M:%S'), photo_path)  # Send email
    else:
        print(f"{name} arrived on time or it's a weekend.")


init_db()


record_latecomer("An An")
