# Face-Detection-System
Face detection to show who arrives late
# 📸 Latecomer Tracking System

Welcome to the Latecomer Tracking System! This Python application helps track late arrivals, take photos, and send email notifications. It's designed to make attendance management easier and more efficient. 

## 🎯 Features
- **📅 Database Management**: Records late arrivals in a SQLite database.
- **📷 Photo Capture**: Takes a photo of late arrivals using your camera.
- **🔔 Email Notifications**: Automatically sends email alerts for late arrivals with a photo attachment.
- **🔊 Sound Alerts**: Plays a capture sound when a photo is taken.

## 🛠️ Requirements
To run this application, you will need:
- Python 3.x
- OpenCV (`cv2`)
- SQLite3
- Winsound (Windows only)
- `smtplib` for sending emails

You can install the required packages using pip:

```bash
pip install opencv-python


## 📧 Email Configuration
To send emails, ensure that:

You have enabled less secure app access or used app passwords if using Gmail.
Modify the SENDER_EMAIL and SENDER_PASSWORD fields accordingly.

📁 Project Structure


├── main.py 
├── latecomers.db             
├── requirements.txt      
└── README.md                
### 📊 Example Results

- A record of late arrivals with timestamps. 
![screenshot](.//late_images/Screenshot%202024-10-31%20124308.png)

- Photos of latecomers captured during their arrival.
![latecomers](.//late_images/Mi%20Min_20241031_121550.jpg)
- Automated email notifications sent to the management team.
![email](.//late_images/Screenshot%202024-10-31%20124940.png)

![Example](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXQyNmxoN3hhMnl5ZzBvY3Z2cTEza2xoZ2RsbzZkcmsyeHdhc3YwMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/I7k5k9lZqTC8dXxq3O/giphy.gif)