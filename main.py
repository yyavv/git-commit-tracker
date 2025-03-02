from assets.message import Message
from assets.commit_tracker import CommitTracker
import datetime
import webbrowser
import time

def main():
    print("\n===== GitHub Contribution Pattern Generator =====\n")
    msg = input("Enter your message: ")
    
    # Ask for which year to create the commit pattern
    current_year = datetime.datetime.now().year
    year_input = input(f"Enter year for commit pattern (default: {current_year}): ")
    target_year = int(year_input) if year_input.strip() else current_year
    
    message = Message(msg)
    message.animate_message()
    
    commit_tracker = CommitTracker(message, target_year=target_year)
    commit_tracker.calculateDays()
    commit_tracker.print_commit_summary()
    
    # Validate the dates before creating commits
    if commit_tracker.validate_dates(commit_tracker.result_dates):
        # Guide user through GitHub repository creation
        if input("\nWould you like to create a GitHub repository for this pattern? (y/n): ").lower() == 'y':
            print("\n=== GitHub Repository Setup ===")
            print("1. You'll need to create a new repository on GitHub first.")
            print("2. The repository should be empty (no README, LICENSE, or .gitignore).")
            
            if input("\nOpen GitHub new repository page now? (y/n): ").lower() == 'y':
                webbrowser.open("https://github.com/new")
                print("\nCreating a new repository on GitHub:")
                print("- Repository name: Choose a meaningful name (e.g., 'git-contribution-pattern')")
                print("- Description: Optional")
                print("- Make it Public or Private as you prefer")
                print("- Do NOT initialize with README, .gitignore, or license")
                print("- Click 'Create repository'")
                
                input("\nPress Enter when you've created the repository...")
                
                print("\nOn the next page, you'll see your repository URL.")
                print("It should look like: https://github.com/your-username/your-repo-name.git")
                print("Copy this URL - you'll need it when the program asks for the repository URL.")
                
                time.sleep(2)
            
            # Ask if user wants to create the commits
            if input("\nReady to create the commits now? (y/n): ").lower() == 'y':
                commit_tracker.create_commits()
    else:
        print("Aborting due to future dates. Please adjust the target year or pattern.")

if __name__ == "__main__":
    main()