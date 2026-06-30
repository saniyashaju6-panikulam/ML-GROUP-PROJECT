https://path-loss-model--saniyashaju6.replit.app/ 
5G Wireless Path Loss Prediction System

A Machine Learning-powered web application that predicts 5G wireless signal path loss and classifies signal quality based on communication parameters.

🚀 Live Demo


https://path-loss-model--saniyashaju6.replit.app/ 

📌 Project Description

This project uses a trained Machine Learning model (Scikit-learn) to predict wireless path loss (dB) in 5G communication systems.

It also categorizes signal strength into:

Excellent
Good
Fair
Poor

The system is designed for ECE final year capstone projects focusing on wireless communication and ML integration.

🧠 Features
🌐 Modern responsive web UI
🤖 ML model-based prediction
⚡ Real-time inference using Flask API
📊 Signal quality classification
📱 Mobile-friendly dashboard
🔄 Instant prediction without page reload
📊 Input Features

The model takes the following inputs:

Simulation Run Number
T-R Separation Distance (m)
Time Delay (ns)
Received Power (dBm)
Phase (rad)
Azimuth AoD (degree)
Elevation AoD (degree)
Azimuth AoA (degree)
Elevation AoA (degree)
RMS Delay Spread (ns)
Season
Frequency
Seasonal Variation (Data Source)
🎯 Output
📌 Predicted Value:
Path Loss (dB)
📌 Classification:
Path Loss	Signal Quality
< 80	Excellent
80–100	Good
100–120	Fair
> 120	Poor
🏗️ Project Structure
project/
│
├── app.py                  # Flask backend API
├── 5G_PathLoss_Model.pkl   # Trained ML model
│
├── templates/
│   └── index.html          # Frontend UI
│
├── static/
│   ├── style.css           # Styling
│   └── script.js          # Frontend logic
│
└── README.md               # Documentation
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/5g-pathloss-predictor.git
cd 5g-pathloss-predictor
2️⃣ Install Dependencies
pip install flask pandas scikit-learn joblib
3️⃣ Run the Application
python app.py
4️⃣ Open in Browser
http://127.0.0.1:5000
🔌 API Endpoint
POST /predict
Request Example:
{
  "sim_run_num": 1,
  "distance": 100,
  "time_delay": 5,
  "received_power": -60,
  "phase": 0.5,
  "azimuth_aod": 30,
  "elevation_aod": 10,
  "azimuth_aoa": 45,
  "elevation_aoa": 15,
  "rms_delay_spread": 2.5,
  "season_num": 1,
  "frequency": 3.5,
  "seasonal_variation": "SummerM"
}
Response:
{
  "path_loss": 92.45,
  "quality": "Good Signal"
}
🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Machine Learning: Scikit-learn
Model Format: Joblib (.pkl)
📈 Future Improvements
📊 Add real-time RF signal visualization
☁️ Deploy on cloud (Render / AWS / Vercel)
📡 Integrate live telecom datasets
🤖 Improve model using XGBoost / Deep Learning
📱 Convert into mobile app
👩‍💻 Author


Machine Learning for Wireless Communication Systems

📜 License

This project is for educational purposes only.

⭐ If you like this project

Give it a ⭐ on GitHub to support the project!
