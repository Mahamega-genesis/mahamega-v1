import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("mahamega-credentials.json", scope)
client = gspread.authorize(creds)

SHEET_ID = "16_5-YppelzsLXqmvFnjJNSFfWI2EKIgeQlPZ7i_Qg_o"
sheet = client.open_by_key(SHEET_ID).sheet1

def log_to_sheet(signal):
    sheet.append_row([signal['coin'], signal['price'], signal['ema'], signal['rsi'], signal['volume'], signal['whale_alerts'], signal['timestamp']])
