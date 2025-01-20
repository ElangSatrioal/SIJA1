from dotenv import load_dotenv
import os

# load_dotenv(dotenv_path=".env")
load_dotenv()

nama_depan = os.getenv("Elang")
nama_belakang = os.getenv("Satrio Al-Alyyu")

print("VARIABLE_DEPAN: ", nama_depan)
print("VARIABLE_BELAKANG: ", nama_belakang)
