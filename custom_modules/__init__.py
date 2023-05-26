import os

if not os.path.exists('data'):
    print("📂 Creating 'data' folder")
    os.mkdir('data')