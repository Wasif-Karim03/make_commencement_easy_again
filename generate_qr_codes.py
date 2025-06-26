import pandas as pd
import qrcode
import os

# Read the CSV file
df = pd.read_csv('students.csv')

# Create output directory for QR codes
output_dir = 'qr_codes'
os.makedirs(output_dir, exist_ok=True)

for idx, row in df.iterrows():
    name = row['Name']
    major = row['Major']
    # Data to encode in QR (as JSON string)
    qr_data = f'{{"Name": "{name}", "Major": "{major}"}}'
    # Generate QR code
    qr = qrcode.make(qr_data)
    # Create a safe filename
    filename = f"{name.replace(' ', '_')}.png"
    filepath = os.path.join(output_dir, filename)
    # Save QR code image
    qr.save(filepath)
    print(f"Saved QR code for {name} at {filepath}")

print("All QR codes generated.") 