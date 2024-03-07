## Prerequisites

- You can spend as much time as you want, but we’d like to see how far you can get within 1 hour
- You need to be able to create a (free) git repository somewhere and share this with the Boloo Team
- Make a commit to the new repository before you start by adding a readme and give the signal that you’ve started your assessment
- Make a (final) commit after one hour
- You don’t have to finish all the user stories below, we just want to see how far you can get within the time given. They are ordered randomly.

- Develop the back-end in Python, all frameworks are allowed.
- Develop the front-end in a single page application, all frameworks are allowed
- Send a message with a link to the repo to [insert email] when you’re done.

## URL shortener Assessment Stories:

- As a customer I want to be able to submit a link and receive a shortened url back
- As a user I want to be redirected to the original url after entering the shortened url
- As a customer I want to be able to create an account using my email address and a password
- As a customer I want to be able to login to the system
- As a customer I want to see all shortened urls I create while logged in
- As a customer I want to be able to delete urls
- As a customer I want to have a pretty interface
- As a customer I want to see the raw number of times the url is requested
- As a customer I want to see the unique number (on IP basis) of times the url is requested
- As a customer I want, for evil purposes, to be able to enter an account wide url where 10% of all requests are redirected.
- As a customer I want to be able to specify a custom shortened url (with availability check)

## Approach I'm taking

1. Grab a TODO app boilerplate with login to start off quickly
2. Write out documentation on how to run it
3. Remove the parts I won't need
4. Create an input field for long urls and a button that shortens, saves, and displays the result
5. Ensure the list of shortened urls can't be viewed when logged out
6. Request counter
7. Account wide url where 10% of requests redirect to
8. Custom shortened url
9. IP-based request counter

## How to run

Requirements: Python, npm

First navigate to the project directory, then
create a virtual environment and activate it:

`python -m venv venv`

`source venv/bin/activate` on mac/ linux or `venv\Scripts\activate.bat` on windows

Install python requirements:

`pip install -r backend/requirements.txt`

Create a sqlite database and apply migrations:

`python backend/server/manage.py migrate`

Run the backend:

`python backend/server/manage.py runserver`

Open up a new terminal, navigate to the frontend folder, and install the frontend dependencies:

`cd frontend`

`npm i --force`

Start the frontend server:

`npm start`

Congratulations! You should now be able to view the site on http://localhost:3000/

When you create an account you are prompted to activate your email before being able to log in. This email doesn't actually go to your inbox, instead you can find the activation link in the terminal where you're running the backend server. It should look something like `http://localhost:3000/activate/MQ/c3ho5x-7f97d440`. Heads-up: the first activation link gave me an error, but after trying to login you will be able to request a second one which should work.

## End of challenge

I set an alarm for 60 minutes and after it went off I committed the code as it was. I was in the process of implementing the request counter, but I did not get to finish the frontend for it.

In its current state things work as intended as long as you shorten a new url every time, but the state management will be wrong when you shorten one that you already shortened before until you refresh the page.
