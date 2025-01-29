# --- OOP Email Simulator --- #

# --- Email Class --- #

# Email class represents an individual email with an email address, 
# subject line, content, and a flag ('has_been_read') to track if the email has been read.
# By default, 'has_been_read' is set to False when an Email object is created.
class Email:
    
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    # 'mark_as_read()' method updates the 'has_been_read' attribute to True 
    # to indicate that the email has been read.
    def mark_as_read(self):
        self.has_been_read = True



# --- Functions --- #

# Populates the inbox with three sample emails. 
def populate_inbox(inbox):

    existing_emails = [
        Email("mina@email.com", "Meeting Reminder", "Don't forget the meeting at 3 PM."),
        Email("hrteam@email.com", "Welcome!", "Welcome to our platform."),
        Email("financeteam@email.com", "Invoice", "Your invoice for January is attached."),
        ]
    inbox.extend(existing_emails) # existing_emails list added to inbox list

# Lists all emails in the inbox with their corresponding index numbers. 
# This function does not differentiate between read and unread emails.
def list_emails(inbox):
    if inbox:
        for index, email in enumerate(inbox):
            print(f"{index}: {email.subject_line} hello")
    else:
        print("No emails available.")

# Displays all details (email address, subject line, and content) of a specific email 
# selected by its index. If the index is invalid, an error message is displayed. 
# Marks the email as read by calling the 'mark_as_read' method.
def read_email(index, inbox):
    try:
        email = inbox[index] 
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()    # Calls mark_as_read function to mark email as read when user opens an email
    except IndexError:
        print("Invalid email index. Please select a valid email.")

# Displays all unread emails in the inbox with their corresponding index numbers. 
# The list of unread emails is updated based on the 'has_been_read' attribute, 
# which is set to True when an email is read using the 'read_email' function.
def view_unread_emails(index, inbox):

    unread_found = False
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{index}: {email.subject_line} (unread)")
            unread_found = True
    if not unread_found:
        print("No undread emails.")


# --- Lists --- #
# Initializes empty List to store all email objects.
inbox = []
populate_inbox(inbox)

# --- Email Program --- #

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Calls the 'list_emails' function to display all emails with their index numbers, 
        # allowing the user to select an email to read.
        list_emails(inbox)
        index = int(input("Select the index of the email you want to read: "))
        print("\nReading email:")
        read_email(index, inbox)

    elif user_choice == 2:
        # Calls the 'view_unread_emails' function to display all unread emails in the inbox.
        view_unread_emails(index, inbox)

    elif user_choice == 3:
        # Terminate program with a farewell message.
        print("Thank you for using this program-- have a nice day!")
        break

    else:
        print("Oops - incorrect input.")
