import dotenv
import os

try:
	dotenv.load_dotenv(".env")
	dev_db_settings = {"drivername": 'postgresql+psycopg2',
						"database": os.environ["DBNAME"],
						"username": os.environ["USERNAME"],
						"password": os.environ["PASSWORD"],
						"host": os.environ["HOST"]}

except Exception as e:
	raise Exception("File .env is not found")