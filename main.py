from assets.message import Message

def main():
    msg = input("Press Enter to your Message: ")
    
    message = Message(msg)

    message.animate_message_by_row(delay=0.1)
    
    message.print_stats()

if __name__ == "__main__":
    main() 