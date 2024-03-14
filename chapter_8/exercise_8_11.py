# exercise 8-11 archived messages
# exercise 8-10 redux with pass by value instead of pass by reference
# copy and don't modify the list
def send_messages(messages: list[str], sent_messages: list[str]) -> None:
    """Modifies data. Prints all of the values in messages and moves them to sent_messages. Messages
    will be empty after function runs.

    Args:
        messages (list[str]): Input list of messages.
        sent_messages (list[str]): Output list of message.
    """
    while messages:
        message = messages.pop()
        print(message)
        # keeps order; .append(message) reverses order
        sent_messages.insert(0, message)


messages = ['Test message.', 'Another message.',
            'One more message.', 'Last message.']
sent_messages = []

print(f'messages -> {messages}')
print(f'sent_messages -> {sent_messages}\n')

# this line here is all that's needed to pass a copy instead
send_messages(messages[:], sent_messages)

print(f'\nmessages -> {messages}')
print(f'sent_messages -> {sent_messages}')
