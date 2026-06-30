
import pandas as pd
import joblib
import argparse
import sys

# =====================================================
# Load Saved Model
# =====================================================

try:
    model = joblib.load("5G_PathLoss_Model.pkl")
except FileNotFoundError:
    print("Error: Model file '5G_PathLoss_Model.pkl' not found. Please ensure it's in the current directory.")
    sys.exit(1)

# =====================================================
# Command Line Argument Parsing
# =====================================================

def parse_args():
    parser = argparse.ArgumentParser(description="5G Path Loss Prediction System")
    parser.add_argument("--sim_run_num", type=int, required=True, help="Simulation Run Number (int)")
    parser.add_argument("--distance", type=float, required=True, help="T-R Separation Distance (m) (float)")
    parser.add_argument("--time_delay", type=int, required=True, help="Time Delay (ns) (int)")
    parser.add_argument("--received_power", type=float, required=True, help="Received Power (dBm) (float)")
    parser.add_argument("--phase", type=float, required=True, help="Phase (rad) (float)")
    parser.add_argument("--azimuth_aod", type=int, required=True, help="Azimuth AoD (degree) (int)")
    parser.add_argument("--elevation_aod", type=float, required=True, help="Elevation AoD (degree) (float)")
    parser.add_argument("--azimuth_aoa", type=float, required=True, help="Azimuth AoA (degree) (float)")
    parser.add_argument("--elevation_aoa", type=int, required=True, help="Elevation AoA (degree) (int)") # Reverted to int based on original df.dtypes
    parser.add_argument("--rms_delay_spread", type=float, required=True, help="RMS Delay Spread (ns) (float)")
    parser.add_argument("--season_num", type=int, required=True, help="Season (numerical, e.g., 0 for FallL, 1 for SpringH) (int)")
    parser.add_argument("--frequency", type=float, required=True, help="Frequency (float)")
    parser.add_argument("--seasonal_variation", type=str, required=True, help="Seasonal Variation (Data Source) (e.g., FallL, SummerM, WinterH)")
    return parser.parse_args()


def main():
    args = parse_args()

    # =====================================================
    # Create DataFrame from Arguments
    # =====================================================

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
    # Prediction
    # =====================================================

    predicted_path_loss = model.predict(sample)[0]

    # =====================================================
    # Classification
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
    # Output
    # =====================================================

    print("\n" + "="*60)
    print("Prediction Result")
    print("="*60)
    print(f"Predicted Path Loss : {predicted_path_loss:.2f} dB")
    print(f"Signal Quality      : {quality}")
    print("="*60)


if __name__ == "__main__":
    main()
