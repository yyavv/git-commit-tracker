from assets.message import Message

def main():
    message = input("Press Enter to your Message: ")
    print(Message(message))

if __name__ == "__main__":
    main()