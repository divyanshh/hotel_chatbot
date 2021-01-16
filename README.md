## Hotel Management Chatbot

Hi, Welcome to the hotel management chatbot

The chatbot is developed on the RASA 2.0 framework and python 3.6.8

## Prerequisites

Python should be pre-installed

## Set up the project

To set up the project

   1. Clone the repo using `git clone <repo_remote_url>`
   2. Install `pyenv` using `pip install pyenv`
   3. Run `pyenv install 3.6.8` to install python version 3.6.8
   4. Go to the path where the repo is cloned and run `pyenv local 3.6.8` to set up this specific version for the project
   5. Install python virtual environment using `pip install virtualenv`
   6. Run `python -m venv venv` to create a virtual environment for the project
   7. Activate your virtual environment using `source ./venv/bin/activate`
   7. Run `pip install -r requirements.txt` to install the dependencies in the virtual environment to run the project
   
## Train Chatbot Model

To train the chatbot

   1. Run `rasa train --domain domain`
   
## Test chatbot

To test the bot using test stories

   1. Run `rasa test`
   
## Deploy chatbot using RASA X

To deploy the chatbot on your local machine

   1. Train the chatbot model
   2. Run `rasa run actions --actions actions -vv` to bring up an action server with custom actions
   3. In a separate shell run `rasa x` to bring up interactive rasa chat
   
   
## SUPPORTED FEATURES

To book room try saying
   
   - book deluxe rooms for 5 people
   - book room for 4 persons
   - book rooms
   - book 4 rooms
   - book simple rooms
   - book deluxe rooms
   
To order room cleaning try
   
   - room cleaning
   - send room cleaning right now
   - arrange for room cleaning after 2 hours
   - room cleaning after 20 minutes
   - arrange room cleaning at 8 pm today
   - arrange room cleaning at 8 pm tomorrow
   
For faq's try something on the lines of
    
   - What are your check-in timings?
   - What are your check-out timings?
   - How do I cancel a reservation?
   - What is your cancellation policy?
   - Does the hotel have a restaurant?
   - Does the hotel offer breakfast?
   - What are the breakfast timings?
   - What are the timings of your restaurant?
   
**NOTE:** The bonus section feature has been implemented for a single intent only (book_room)
To test it try saying
   
   - I want to book a room
   - I would like to book a room
   - I want to book a room for my stay
   - book room
   - room booking
   - how do I book a room
   - book rooms for stay
   - book rooms