from assets.message import Message
from assets.commit_tracker import CommitTracker

def main():
    msg = input("Press Enter to your message: ")
    
    message = Message(msg)

    message.animate_message()
    
    commit_tracker = CommitTracker(message)

    commit_tracker.calculateDays()

    commit_tracker.print_commit_summary()

if __name__ == "__main__":
    main() 
    
    #TODO: Add complete REPO result to the screen
    #TODO: Implement remainder logic and calendar system
    #TODO: Last element being NONE in result_dates causing a problem and terminates the program