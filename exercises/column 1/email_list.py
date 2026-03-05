# Initialize empty sets
subscribers = set()
unsubscribers = set()

# Function to add an email
def add_email(email, set_name):
    if set_name == subscribers:
        subscribers.add(email)
    else:
        unsubscribers.add(email)
    print(f"Email '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}.")

# Function to remove an email
def remove_email(email, set_name):
    if email in set_name:
        set_name.remove(email)
        print(f"Email {email} was removed from {set_name}")
    else:
        print(f"Email {email} was not found.")

# Function to display emails
def display_emails(set_name):
    for email in set_name:
        print(email)

# Function to find active subscribers. Return the set.
def find_active_subscribers():
    return subscribers.difference(unsubscribers)

# Adding emails to subscribers (notice that some people subscribe more than once)
add_email("user1@example.com", subscribers)
add_email("user3@example.com", subscribers)
add_email("user4@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user6@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user8@example.com", subscribers)
add_email("user9@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)

# Adding emails to unsubscribers
add_email("user6@example.com", unsubscribers)
add_email("user8@example.com", unsubscribers)
add_email("user1@example.com", unsubscribers)
add_email("user10@example.com", unsubscribers)

# Displaying subscribers and unsubscribers
print("All Subscribers:")
display_emails(subscribers)


print("All Unsubscribers:")
display_emails(unsubscribers)


# Finding active subscribers
print("Active Subscribers:")
subscriber_emails = find_active_subscribers()
print(subscriber_emails)

