from dotenv import load_dotenv, find_dotenv
# Load nearest .env starting from CWD, falling back to parents
load_dotenv(find_dotenv(), override=False)
