from assets.message import Message
from assets.commit_tracker import CommitTracker

def main():
    msg = input("Press Enter to your Message: ")
    
    message = Message(msg)

    message.animate_message(delay=0.1)
    
    commit_tracker = CommitTracker(message)

    commit_tracker.calculateDays()

    commit_tracker.print_commit_summary()

    message.print_stats()

if __name__ == "__main__":
    main() 


    #TODO: Add complete REPO result to the screen
    #TODO: Implement remainder logic and calendar system