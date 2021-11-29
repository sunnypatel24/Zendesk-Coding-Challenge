# Zendesk-Coding-Challenge
Zendesk Ticket Viewer for 2021 Intern Coding Challenge

A ticket viewer program written in Python to connect to Zendesk API and get all tickets or a single ticket for an account.
* Must have a valid Zendesk subdomain url, such as 'https://zccsunnypatel.zendesk.com'.

## Installation & Usage

#### Requirements
- Python 3
- Pip 3 (for requests package)

### Setting up the project locally

1. Clone the repo to your local machine, or, alternatively, download the project as a zip file and extract it to your local machine.
2. cd into the working directory for the project.
3. Run `python3 tickets.py` to start up the ticket viewer. You will be prompted for your subdomain url and email/password for your associated zendesk account.
4. Follow prompts within the program to view your tickets.

## Usage
The requests package is used to send a GET request to the Zendesk API, retrieving and sending back ticket data. This data will be returned and outputted in acsending order, based on ID, 3 tickets at a time. 

#### Running Tests

To run the unit tests for the ticket viewer, run `python3 test_tickets.py` to run the unit tests for GET ALL and GET API endpoints. The unit testing framework used is the unittest module that comes with Python.
