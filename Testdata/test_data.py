import sys
sys.path.append(".")

from Utils.utils import Utility

class Data():
    BASE_URL = 'https://the-internet.herokuapp.com/login'
    USERNAME = 'tomsmith'
    FAKE_USERNAME = 'nguyetpa'
    PASSWORD = 'SuperSecretPassword!'
    FAKE_PASSWORD = 'SuperSecretPassword'
    BROWSER = 'Chrome'

    ACCOUNT_CSV_FILE = './Testdata/accounts.csv'
    ACCOUNT_JSON_FILE = './Testdata/accounts.json'


    def get_account_csv(self):
        utility = Utility()
        return utility.read_csv(Data.ACCOUNT_CSV_FILE)

    def get_account_json(self):
        utility = Utility()
        return utility.read_json(Data.ACCOUNT_JSON_FILE)