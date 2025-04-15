import tkinter as tk
from tkinter import messagebox
import numpy as np
import pickle

# Load the trained model and scaler
model = pickle.load(open('model.pkl', 'rb'))  # Ensure 'model.pkl' is in the same directory
scaler = pickle.load(open('scaler.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))  # Ensure this file is saved correctly

# Function to predict the crop
def predict_crop():
    try:
        # Get user inputs
        n = float(entry_n.get())
        p = float(entry_p.get())
        k = float(entry_k.get())
        temperature = float(entry_temperature.get())
        humidity = float(entry_humidity.get())
        ph = float(entry_ph.get())
        rainfall = float(entry_rainfall.get())

        # Prepare the input array
        input_features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
        scaled_features = scaler.transform(input_features)

        # Predict the label
        prediction = model.predict(scaled_features)
        predicted_label = label_encoder.inverse_transform(prediction)  # Convert to label name

        # Display the result
        messagebox.showinfo("Prediction Result", f"The suitable crop for growth is: {predicted_label[0]}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input or missing values.\nError details: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Crop Recommendation System")
root.geometry("400x400")

# Add labels and entry fields
tk.Label(root, text="Enter the values below:", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Nitrogen (N):").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Label(root, text="Phosphorus (P):").pack()
entry_p = tk.Entry(root)
entry_p.pack()

tk.Label(root, text="Potassium (K):").pack()
entry_k = tk.Entry(root)
entry_k.pack()

tk.Label(root, text="Temperature (°C):").pack()
entry_temperature = tk.Entry(root)
entry_temperature.pack()

tk.Label(root, text="Humidity (%):").pack()
entry_humidity = tk.Entry(root)
entry_humidity.pack()

tk.Label(root, text="pH:").pack()
entry_ph = tk.Entry(root)
entry_ph.pack()

tk.Label(root, text="Rainfall (mm):").pack()
entry_rainfall = tk.Entry(root)
entry_rainfall.pack()

# Add a Predict button
predict_button = tk.Button(root, text="Predict", command=predict_crop, bg="green", fg="white")
predict_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
