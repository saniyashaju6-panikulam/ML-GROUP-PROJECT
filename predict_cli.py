import os
import pandas as pd
import joblib
import argparse
import sys

# =====================================================
# LOAD MODEL (FIXED ABSOLUTE PATH)
# =====================================================

model_path = r"C:\Users\Ethnotech\Desktop\ml project\5G_PathLoss_Model.pkl"

if not os.path.exists(model_path):
    print("Error: Model file not found!")
    print("Expected path:", model_path)
    sys.exit(1)

model = joblib.load(model_path)

print("Model loaded successfully!")
print("=" * 60)
print("        5G PATH LOSS PREDICTION SYSTEM")
print("=" * 60)

# =====================================================
# ARGUMENT PARSER
# =====================================================

def parse_args():
    parser = argparse.ArgumentParser(description="5G Path Loss Prediction System")

    parser.add_argument("--sim_run_num", type=int, required=True)
    parser.add_argument("--distance", type=float, required=True)
    parser.add_argument("--time_delay", type=int, required=True)
    parser.add_argument("--received_power", type=float, required=True)
    parser.add_argument("--phase", type=float, required=True)
    parser.add_argument("--azimuth_aod", type=int, required=True)
    parser.add_argument("--elevation_aod", type=float, required=True)
    parser.add_argument("--azimuth_aoa", type=float, required=True)
    parser.add_argument("--elevation_aoa", type=int, required=True)
    parser.add_argument("--rms_delay_spread", type=float, required=True)
    parser.add_argument("--season_num", type=int, required=True)
    parser.add_argument("--frequency", type=float, required=True)
    parser.add_argument("--seasonal_variation", type=str, required=True)

    return parser.parse_args()

# =====================================================
# MAIN FUNCTION
# =====================================================

def main():
    args = parse_args()

    # Create input DataFrame (must match training columns exactly)
    sample = pd.DataFrame({
        "Seasonal Variation (Data Source)": [args.seasonal_variation],
        "Simulation Run Number": [args.sim_run_num],
        "T-R Separation Distance (m)": [args.distance],
        "Time Delay (ns)": [args.time_delay],
        "Received Power (dBm)": [args.received_power],
        "Phase (rad)": [args.phase],
        "Azimuth AoD (degree)": [args.azimuth_aod],
        "Elevation AoD (degree)": [args.elevation_aod],
        "Azimuth AoA (degree)": [args.azimuth_aoa],
        "Elevation AoA (degree)": [args.elevation_aoa],
        "RMS Delay Spread (ns)": [args.rms_delay_spread],
        "Season": [args.season_num],
        "Frequency": [args.frequency]
    })

    # =====================================================
    # PREDICTION
    # =====================================================

    predicted_path_loss = model.predict(sample)[0]

    # =====================================================
    # SIGNAL QUALITY CLASSIFICATION
    # =====================================================

    if predicted_path_loss < 80:
        quality = "Excellent Signal"
    elif predicted_path_loss < 100:
        quality = "Good Signal"
    elif predicted_path_loss < 120:
        quality = "Fair Signal"
    else:
        quality = "Poor Signal"

    # =====================================================
    # OUTPUT
    # =====================================================

    print("\n" + "=" * 60)
    print("Prediction Result")
    print("=" * 60)
    print(f"Predicted Path Loss : {predicted_path_loss:.2f} dB")
    print(f"Signal Quality      : {quality}")
    print("=" * 60)

# =====================================================
# RUN SCRIPT
# =====================================================

if __name__ == "__main__":
    main()