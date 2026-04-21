🎓 Attendify – AI Attendance System

Attendify is an AI-powered smart attendance management system that automatically records attendance using face recognition technology. The system detects and identifies individuals in real time through a webcam and marks their attendance without manual input.

This project aims to eliminate manual attendance errors, proxy attendance, and time-consuming roll calls by leveraging computer vision and machine learning techniques.

🚀 Features

👤 Face ans Voice Recognition Attendance
Automatically detects and recognizes faces
Marks attendance in real time
Prevents proxy attendance

🔐 Secure Login System
Admin authentication
Student registration and login
Credential-based access control

📊 Attendance Management
Automatic attendance logging
View attendance history
View Enrolled Students

📷 Student Registration
First-time user face & voice registration
Image dataset creation for training

🧠 How It Works
Student Registration
Students register and capture facial images, record voice.
Images and Voice are stored as training data.
Model Training
The system trains the recognition model using stored face images and voice records.
Face Detection
Webcam captures live video frames or Microphone record voice.
Faces are detected using computer vision.
Face & Voice Recognition
The system identifies the student.
Attendance is automatically recorded.

🛠 Tech Stack
Programming
  Python
Computer Vision
  OpenCV
Machine Learning
  dlib
  SVC
Database
  SQL / supabase
Interface
  streamlit / Web Interface
  
📂 Project Structure
attendify
│
├── dataset/              # Student face dataset
├── trainer/              # Trained model files
├── attendance/           # Attendance records
│
├── register.py           # Student registration
├── train_model.py        # Model training
├── recognize.py          # Face recognition & attendance
│
├── admin_login.py        # Admin authentication
├── email_notification.py # Email credential system
│
└── README.md

⚙️ Installation

1️⃣ Clone the repository
git clone https://github.com/adityaraj-12/attendify.git

2️⃣ Navigate to project directory
cd attendify

3️⃣ Install dependencies
pip install opencv-python
pip install numpy
pip install pillow

▶️ Run the Project
Register new students
python register.py
Train the face recognition model
train model piplines 
Start attendance system

👨‍💻 Author

Adityaraj

GitHub
https://github.com/adityaraj-12

⭐ Contributing

Contributions are welcome!
