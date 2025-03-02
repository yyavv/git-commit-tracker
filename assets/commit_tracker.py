import git
import os
from datetime import datetime, timedelta
import tempfile
import shutil
from typing import List, Optional
from tqdm import tqdm
import time
import subprocess
import random

class CommitTracker:
    def __init__(self, message_instance, target_year=None):
        """Initialize with a message instance and optional target year."""
        self._message_instance = message_instance
        self.start_date = None
        self.end_date = None
        
        # Set base date to January 1st of target year
        if target_year:
            self.today = datetime(target_year, 1, 1)
        else:
            self.today = datetime.now()

    def calculateNextMonday(self, weekday: int) -> timedelta:
        """Calculate days until next Monday."""
        return timedelta(days=7 - weekday % 7)

    def calculateDays(self) -> List[List[Optional[str]]]:
        """Calculate commit dates for the message pattern."""
        print("Calculating days for commit tracker")
        
        # Start from next Monday
        self.today += self.calculateNextMonday(self.today.weekday())
        self.start_date = self.today.replace()  # Create a copy of today as start_date
        
        # Get the letter grids and iterate over the message
        result_dates = []
        
        # Iterate through actual message characters and their corresponding LetterData
        for idx, letter_data in enumerate(self._message_instance.letters):
            if letter_data:
                grid = letter_data.letter_data  # This is already a list of strings
                letter_dates = []
                
                # Process each column in the grid, top to bottom
                for col in range(5):  # Assuming 5x5 grid
                
                    for row in range(5):
                        current_cell = grid[row][col]
                        if current_cell == '1':
                            letter_dates.append(self.today.strftime("%d-%m-%Y"))
                        else:
                            letter_dates.append(None)
                        self.today += timedelta(days=1)  # Add 1 day for each cell in the grid
                    
                    self.today += self.calculateNextMonday(self.today.weekday())  # Add days until next Monday

                result_dates.append(letter_dates)
                self.today += timedelta(days=7)  # Add 7 days for spacing between letters
            else:
                # Handle spaces
                result_dates.append([None] * 25)
                self.today += timedelta(days=7)  # Add extra 7 days for new word spacing
        
        for col in range(len(result_dates[0]) - 1, -1, -1):
            # Scan rows from bottom to top for each column
            for row in range(len(result_dates) - 1, -1, -1):
                # If there is a value in the cell, return it                 
                if result_dates[row][col]:
                    self.end_date = result_dates[row][col]
                    break
            
            if self.end_date:
                break

        self.print_result(result_dates)
        self.result_dates = result_dates  # Store as instance variable
        return result_dates

    def print_result(self, result_dates: List[List[Optional[str]]]):
        """Print commit dates for each letter."""
        print("\nCommit Dates:")
        
        # Iterate through the actual message characters
        for idx, dates in enumerate(result_dates):
            if dates is None or len(dates) == 0:
                continue
            
            # Get the actual letter from the message
            current_letter = self._message_instance.message[idx]
            print(f"Letter {current_letter}:")
            
            # Print dates in a 5x5 grid format
            for row in range(5):
                row_dates = []
                for col in range(5):
                    index = col * 5 + row  # Calculate correct index for column-first order
                    date = dates[index] if index < len(dates) else None
                    row_dates.append(date if date else "---")
                print(" | ".join(row_dates))
            print("-" * 75)

    def print_commit_summary(self):
        """Print a summary of total commits needed."""
        total_commits = sum(
            sum(1 for row in letter.letter_data for cell in row if cell == '1')
            for letter in self._message_instance.letters
            if letter is not None
        )
        print(f"\nTotal commits needed: {total_commits}")
        
        # Use self.start_date instead of self.date
        print(f"Starting from: {self.start_date.strftime('%d-%m-%Y')} ({self.start_date.strftime('%A')})")
        
        # Ensure self.end_date is a datetime object
        if isinstance(self.end_date, str):
            self.end_date = datetime.strptime(self.end_date, "%d-%m-%Y")
        
        print(f"Ending on: {self.end_date.strftime('%d-%m-%Y')} ({self.end_date.strftime('%A')})")
        
        # Calculate total days
        total_days = (self.end_date - self.start_date).days
        print(f"Total days: {total_days}")

    def validate_dates(self, result_dates):
        """Ensure all dates are in the past or present."""
        today = datetime.now()
        future_dates = []
        
        for letter_dates in result_dates:
            for date_str in letter_dates:
                if date_str:
                    commit_date = datetime.strptime(date_str, "%d-%m-%Y")
                    if commit_date > today:
                        future_dates.append(date_str)
        
        if future_dates:
            print("Warning: The following commit dates are in the future:")
            for date in future_dates[:10]:  # Show first 10 future dates
                print(f"- {date}")
            if len(future_dates) > 10:
                print(f"...and {len(future_dates) - 10} more.")
            
            return False
        return True

    def create_commits(self):
        """Create commits based on the calculated dates."""
        print("\n=== Creating Commits for Pattern ===")
        
        # Ask for GitHub repository URL
        github_url = input("Enter your GitHub repository URL: ")
        if not github_url:
            print("No GitHub URL provided. You'll need to manually connect to GitHub later.")
        
        # Create a temporary repo or use existing one
        repo_path = input("Enter path for local Git repo (or leave empty for a temporary repo): ")
        if not repo_path:
            repo_path = tempfile.mkdtemp()
            print(f"Created temporary repo at: {repo_path}")
            repo = git.Repo.init(repo_path)
        else:
            try:
                repo = git.Repo(repo_path)
            except git.InvalidGitRepositoryError:
                print(f"Initializing new git repo at {repo_path}")
                repo = git.Repo.init(repo_path)
        
        # Create a dummy file to modify for commits
        dummy_file = os.path.join(repo_path, "pattern_file.txt")
        
        # Create the initial commit to establish the branch
        with open(dummy_file, 'w') as f:
            f.write("# Git Contribution Pattern\n\nThis file is used to create commits for a pattern in GitHub contributions.\n")
        
        repo.git.add(dummy_file)
        repo.git.commit('-m', 'Initial commit')
        
        # Add GitHub remote if URL was provided
        if github_url:
            try:
                repo.git.remote('add', 'origin', github_url)
                print(f"Added GitHub remote: {github_url}")
            except Exception as e:
                print(f"Could not add GitHub remote: {e}")
        
        # Get branch name
        try:
            branch_name = repo.active_branch.name
        except:
            branch_name = "master"  # Default fallback
        
        # Flatten the result_dates to get all dates that need commits
        commit_dates = []
        for letter_dates in self.result_dates:
            for date_str in letter_dates:
                if date_str:  # Only process non-None dates
                    commit_dates.append(date_str)
        
        # Sort and remove duplicates
        commit_dates = sorted(set(commit_dates))
        
        # Allow user to enhance visual effect with varying commit densities
        enhance_visuals = input("\nEnhance visual effect with varying commit intensities? (y/n): ").lower() == 'y'
        
        # Default number of commits per date
        base_num_commits = 1
        
        # Calculate total commits needed
        if enhance_visuals:
            # For enhanced visuals with random commit counts
            commit_counts = {}
            total_commits = 0
            
            print("\nEnhancing pattern with random commit intensities (1-7 commits per date)")
            for date_str in commit_dates:
                # Randomly assign 1-7 commits for each date with weighted distribution
                # More weight to lower numbers to make darker squares more rare and special
                num_commits = random.choices([1, 2, 3, 4, 5, 6, 7], weights=[40, 25, 15, 10, 5, 3, 2])[0]
                commit_counts[date_str] = num_commits
                total_commits += num_commits
        else:
            # Without enhancement, one commit per date
            total_commits = len(commit_dates)
            commit_counts = {date_str: 1 for date_str in commit_dates}
        
        # Create commits for each date
        print("\nCreating pattern commits...")
        success_count = 0
        
        # Create progress bar
        from tqdm import tqdm
        
        with tqdm(total=total_commits, desc="Creating commits", unit="commit") as pbar:
            for date_str in commit_dates:
                try:
                    commit_date = datetime.strptime(date_str, "%d-%m-%Y")
                    
                    # Determine number of commits for this date
                    num_commits = commit_counts[date_str]
                    
                    # Create the specified number of commits
                    for i in range(num_commits):
                        # Modify the file
                        with open(dummy_file, 'a') as f:
                            f.write(f"Commit {i+1} for pattern: {date_str}\n")
                        
                        # Stage the file
                        repo.git.add(dummy_file)
                        
                        # Create environment with GIT_AUTHOR_DATE and GIT_COMMITTER_DATE
                        env = {
                            'GIT_AUTHOR_DATE': commit_date.strftime('%Y-%m-%d %H:%M:%S'),
                            'GIT_COMMITTER_DATE': commit_date.strftime('%Y-%m-%d %H:%M:%S')
                        }
                        
                        # Commit with the specific date
                        repo.git.commit('-m', f'Pattern commit {i+1} for {date_str}', env=env)
                        success_count += 1
                        
                        # Update progress bar
                        pbar.update(1)
                        
                except Exception as e:
                    tqdm.write(f"Error creating commit for {date_str}: {e}")
        
        print(f"\nSuccessfully created {success_count} commits out of {total_commits} planned.")
        
        # Ask if user wants to push commits now
        if input("\nWould you like to push commits to GitHub now? (y/n): ").lower() == 'y':
            try:
                print("\n=== Pushing Commits to GitHub ===")
                
                if not github_url:
                    # If no URL was provided earlier, ask for it now
                    github_url = input("Enter your GitHub repository URL: ")
                    if github_url:
                        # Add the remote if not already added
                        try:
                            repo.git.remote('add', 'origin', github_url)
                            print(f"Added GitHub remote: {github_url}")
                        except Exception as e:
                            # Remote might already exist
                            print(f"Note: {e}")
                
                if github_url:
                    # Try pushing the commits
                    print(f"Pushing commits to GitHub repository...")
                    try:
                        # Change to the repository directory and push
                        os.chdir(repo_path)
                        result = subprocess.run(
                            f"git push -u origin {branch_name}", 
                            capture_output=True,
                            text=True,
                            shell=True
                        )
                        
                        if result.returncode == 0:
                            print("Successfully pushed commits to GitHub!")
                            print(f"View your pattern on GitHub's contribution graph for {self.start_date.year}")
                            
                            # Open the GitHub repository in the browser
                            if input("\nOpen GitHub repository in browser? (y/n): ").lower() == 'y':
                                # Convert GitHub SSH URL to HTTPS if needed
                                if github_url.startswith('git@github.com:'):
                                    web_url = github_url.replace('git@github.com:', 'https://github.com/')
                                else:
                                    web_url = github_url
                                    
                                if web_url.endswith('.git'):
                                    web_url = web_url[:-4]
                                    
                                import webbrowser
                                webbrowser.open(web_url)
                        else:
                            print("Failed to push commits. Error:")
                            print(result.stderr)
                            print("\nYou can push manually with these commands:")
                            print(f"cd {repo_path}")
                            print(f"git push -u origin {branch_name}")
                            
                    except Exception as e:
                        print(f"Error pushing commits: {e}")
                        print("\nYou can push manually with these commands:")
                        print(f"cd {repo_path}")
                        print(f"git push -u origin {branch_name}")
                else:
                    print("\nNo GitHub URL provided. You can push manually with these commands:")
                    print(f"cd {repo_path}")
                    print(f"git remote add origin https://github.com/your-username/your-repo-name.git")
                    print(f"git push -u origin {branch_name}")
            except Exception as e:
                print(f"Error during push operation: {e}")
                print("\nYou can push manually with these commands:")
                print(f"cd {repo_path}")
                print(f"git push -u origin {branch_name}")
        else:
            # Provide instructions for manual pushing
            print("\n=== Next Steps ===")
            print(f"To visualize your pattern on GitHub:")
            print(f"1. Navigate to the repository directory:")
            print(f"   cd {repo_path}")
            
            if github_url:
                print(f"2. Push the commits to GitHub:")
                print(f"   git push -u origin {branch_name}")
            else:
                print(f"2. Connect to your GitHub repository:")
                print(f"   git remote add origin https://github.com/your-username/your-repo-name.git")
                print(f"3. Push the commits to GitHub:")
                print(f"   git push -u origin {branch_name}")
            
            print(f"\n4. View your pattern on GitHub's contribution graph for {self.start_date.year}")

