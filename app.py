import imaplib

# Connect to the IMAP server
imap_server = imaplib.IMAP4('sprjapan.com')

username = input("username: ")
password = input("Password: ")
sender = input("sender: ")
# Login to the email account
imap_server.login(username, password)


# Define the search criteria
search_criteria = f'(FROM "{sender}")'

# Select the mailbox before executing the search command
imap_server.select('INBOX')

# Search for emails from the specified sender
_, message_ids = imap_server.search(None, search_criteria)
a = 1
# Delete the emails
for message_id in message_ids[0].split():
    imap_server.store(message_id, '+FLAGS', '\\Deleted')
    a += 1
    if a%500 == 0:
        imap_server.expunge()
        print(f"Done {a}")
    

# Permanently remove the deleted emails

# Close the connection
imap_server.logout()
