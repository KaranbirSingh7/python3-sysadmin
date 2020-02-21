# Simple WeatherCLI using python and open-weather-map

## Installing/Running

1. Make sure python3 is installed on machine. Any python3.\* would work.
2. Create a new virtualenv in the folder where this cli/script is present.

   ```bash
   python3 -m venv virtualenv
   ```

3. Activate virtualenv by sourcing/running active script: `source ./virtualenv/bin/activate`
4. Install dependencies using pip: `pip install -r requirements.txt`
5. An API KEY from OpenWeatherMap is needed to have this app running. It's free, sign up and get one.
6. Put that API_KEY in `.env` file.

   ```bash
   cp .env.sample .env

   vim .env
   # Replace empty strings with your new API KEY
   ```

7. Once key is in place and app have executable permissions. You have to source and load your API key into current terminal session.

   ```bash
   source .env
   ```

8. Try running by using this command: `./app.py --location toronto --country canada`

9. If key is in working state and city exists. App would print out JSON
