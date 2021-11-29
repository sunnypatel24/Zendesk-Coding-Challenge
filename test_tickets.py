import unittest
import tickets

# Unit tests for tickets.py
class TestTickets(unittest.TestCase):
    # Initialize test variables for all possible test cases
    valid_user = input("Enter a valid email address: ")
    valid_password = input("Enter a correct password: ")
    valid_url = input("Enter a valid url subdomain: ")
    invalid_user = input("Enter an incorrect email address: ")
    invalid_password = input("Enter an incorrect password: ")
    invalid_url = input("Enter an incorrect url: ")
    ticket_id = input("Please enter a ticket id: ")

    # test for getting all tickets for an associated account
    def test_all_tickets(self):
        # test getting all tickets provided valid url and login information
        existing_login = tickets.all_tickets(self.valid_url, self.valid_user, self.valid_password)

        # if function made it to the end, it will return True, meaning it was 
        # successful
        self.assertEqual(existing_login, True)

        # test with a valid url but incorrect login credentials
        with self.assertRaises(SystemExit) as cm:
            tickets.all_tickets(self.valid_url, self.invalid_user, self.invalid_password)
        self.assertEqual(cm.exception.code, 1)

        # test with an invalid url and valid login credentials
        with self.assertRaises(SystemExit) as cm:
            tickets.all_tickets(self.invalid_url, self.valid_user, self.valid_password)
        self.assertEqual(cm.exception.code, 1)

        # test with invalid url and invalid login credentials
        with self.assertRaises(SystemExit) as cm:
            tickets.all_tickets(self.invalid_url, self.invalid_user, self.invalid_password)
        self.assertEqual(cm.exception.code, 1)
        
    
    # test for getting a single ticket by ticket id for an associated account
    def test_single_ticket(self):
        # test getting a ticket provided valid url and login information
        existing_login = tickets.single_ticket(self.valid_url, self.ticket_id, self.valid_user, self.valid_password)

        # if function made it to the end, it will return True, meaning it was 
        # successful
        self.assertEqual(existing_login, True)

        # test with a valid url but invalid login credentials
        with self.assertRaises(SystemExit) as cm:
            tickets.single_ticket(self.valid_url, self.ticket_id, self.invalid_user, self.invalid_password)
        self.assertEqual(cm.exception.code, 1)

        # test with invalid url and valid login credentials
        with self.assertRaises(SystemExit) as cm:
            tickets.single_ticket(self.invalid_url, self.ticket_id, self.valid_user, self.valid_password)
        self.assertEqual(cm.exception.code, 1)

        # test with invalid url and login credentials
        with self.assertRaises(SystemExit) as cm:
            tickets.single_ticket(self.invalid_url, self.ticket_id, self.invalid_user, self.invalid_password)
        self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
