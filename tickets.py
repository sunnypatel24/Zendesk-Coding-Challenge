import requests


# A ticket viewer program for Zendesk accounts (Get all or Get single)
def main():
    print("Hello! You can view your Zendesk tickets here.")
    res = input("Type 'menu' to view options or 'quit' to exit: ")
    # keep getting input if user does not type one of the two valid options
    while res != 'menu' and res != 'quit':
        print('Invalid choice, please try again.')
        res = input("Type 'menu' to view options or 'quit' to exit: ")

    if res == 'menu':
        
        # keep presenting options for user to view all tickets or single ticket 
        # until they enter 'quit'
        while True:
            options()
            choice = input()

            # keep getting input if user does not enter a 1, 2, or 'quit'
            while choice != '1' and choice != '2' and choice != 'quit':
                print("Invalid choice. Please try again.")
                options()
                choice = input()

            # choice is 1 or 2, so ask user for login credentials and url
            if choice != 'quit':
                user = input("\nPlease enter your email address associated with your Zendesk account: ")
                password = input("Please enter your password for your Zendesk account: ")
                url = input("Please enter the url for your Zendesk subdomain (e.g. https://zccfoobar.zendesk.com): ")
                print('\n')

                # if user wants to view all tickets, call all tickets with the # information they provided
                if choice == '1':
                    all_tickets(url, user, password)

                # user wants to view a single ticket, so ask them for ticket id
                else:
                    ticket_id = input("Enter ticket id: ")
                    single_ticket(url, ticket_id, user, password)

            # user typed 'quit' after seeing options, so exit program
            else:
                print("Thanks for using the ticket viewer. Goodbye.")
                exit(0)

    # user typed 'quit' without seeing options, so exit program
    else:
        print("Thanks for using the ticket viewer. Goodbye.")
        exit(0)


# print the different options text to output
def options():
    print("\nSelect view options: ")
    print(" - Press 1 to view all tickets")
    print(" - Press 2 to view a single ticket")
    print(" - Type 'quit' to exit")


# get all tickets for a user's account
def all_tickets(url, user, password):

    # check is used for unit testing to ensure method successfully ran
    check = False
    count = 0

    # append API endpoint to url structure
    endpoint = url + '/api/v2/tickets.json'

    # Try GET ALL request for Zendesk API
    try:  
        response = requests.get(endpoint, auth = (user, password))
        response.raise_for_status()
    
    # Exit program if there was an error relating to invalid login credentials
    except requests.exceptions.HTTPError:
        print("Invalid email or password. Exiting ticket viewer.")
        exit(1)

    # Exit program if there was an error relating to invalid url or API service # unavailable   
    except:
        print("An error with connecting to the API has occurred.")
        exit(1)

    data = response.json()
    
    # print each property and the value for a ticket, until all tickets have 
    # been printed
    for d in data['tickets']:

        # print the ticket # and bold it
        print("\033[1m" + "TICKET #" + str(count + 1) + "\033[0m")
        for i in d:
            print(i + ':', d[i])
        print('\n')

        # display information for 3 tickets at a time, and then let user hit 
        # enter to continue displaying another 3 tickets, until all tickets 
        # have been printed
        count += 1
        if count % 3 == 0:
            input("Press Enter to continue: ")
    print('\n')

    # GET all tickets was successful, return True
    check = True
    return check


# get a single ticket for a user's account
def single_ticket(url, ticket_id, user, password):

    # check is used for unit testing to ensure method successfully ran
    check = False
    print('\n')

    # append API endpoint with given ticket id to url structure
    endpoint = url + '/api/v2/tickets/' + ticket_id + '.json'
    
    # Try GET request for Zendesk API
    try:  
        response = requests.get(endpoint, auth = (user, password))

        # if status code = 404, ticket id was invalid, making the url incorrect
        if response.status_code == 404:
            exit(1)
        response.raise_for_status()

    # Exit program if there was an error relating to invalid login credentials
    except requests.exceptions.HTTPError:
        print("Invalid email or password. Exiting ticket viewer.")
        exit(1)
    
    # Exit program if a 404 error was found (handles a SystemExit error)
    except SystemExit:
        print("The ticket id does not exist. Exiting ticket viewer.")
        exit(1)  
    
    # Exit program if there was an error relating to invalid url or API service # unavailable
    except:
        print("An error with connecting to the API has occurred.")
        exit(1)
        
    data = response.json()

    # print the ticket # and bold it
    print("\033[1m" + "TICKET #" + ticket_id + "\033[0m")
    
    # print each property and the value for the ticket
    for d in data['ticket']:
        print(d + ':', data['ticket'][d])
    print('\n')

    # GET ticket was successful, return True
    check = True
    return check

# call main()
if __name__ == "__main__":
    main()