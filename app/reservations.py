import pandas as pd
import os

FILE_PATH = "./tabela/reservations.csv"

def create_reservation(name, hotel_name, check_in, check_out):
    reservation = {"name": name, "hotel_name": hotel_name, "check_in": check_in, "check_out": check_out}
    if not os.path.isfile(FILE_PATH):
        pd.DataFrame([reservation]).to_csv(FILE_PATH, index=False)
    else:
        pd.DataFrame([reservation]).to_csv(FILE_PATH, mode='a', header=False, index=False)
    return {"message": "Reservation created successfully"}

def list_reservations():
    if os.path.isfile(FILE_PATH):
        return pd.read_csv(FILE_PATH).to_dict(orient="records")
    return {"message": "No reservations found"}
