HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["5948661"])
    API_HASH = environ["ed081430c75f3e9a95b3b5d461fa73"]
    SESSION_STRING = environ["SESSION_STRING"]  # Check Readme for session
    ARQ_API_KEY = environ["KEONLX-JNUZAE-DPBEDF-MLSDGP-ARQ"]
    DEFAULT_SERVICE = (
        environ["DEFAULT_SERVICE"]
        if "DEFAULT_SERVICE" in environ
        else "youtube"
    )

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"deezer"/"saavn"

# don't make changes below this line
ARQ_API = "https://thearq.tech"
