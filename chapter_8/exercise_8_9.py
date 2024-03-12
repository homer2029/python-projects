# exercise 8-9 messages
# list of messages
# pass to function that prints each message -> show messages
def show_messages(messages: list) -> None:
    """Prints each message in a list.

    Args:
        messages (list): The list of messages.
    """
    for message in messages:
        print(message)


show_messages(['Test message.', 'Another message.',
              'One more message.', 'Last message.'])
