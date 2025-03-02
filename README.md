# Git Commit Tracker

A powerful tool that allows you to create custom patterns in your GitHub contribution graph. Write messages, create art, or showcase meaningful dates through your contribution activity.

## Overview

Git Commit Tracker manipulates your GitHub contribution graph by strategically creating commits on specific dates. This allows you to form visual patterns that display text, simple designs, or highlight important dates in your contribution history. Perfect for developers who want to add a creative touch to their GitHub profile.

## Features

- Create text messages that appear in your GitHub contribution graph
- Select specific years for your patterns
- Automatically calculate and generate all required commits
- Support for all alphanumeric characters and many special symbols
- Visual enhancement with varying commit intensities
- Interactive command-line interface with visual feedback
- Detailed progress tracking and summaries

## Requirements

- Python 3.6+
- Git installed and configured
- GitHub account
- GitPython library
- tqdm library (for progress bars)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/username/git-commit-tracker.git
   cd git-commit-tracker
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure the main script is executable:
   ```bash
   chmod +x git_commit_tracker.py
   ```

## Usage

### Basic Command

- bash
- python git_commit_tracker.py --message "HELLO" --year 2023

### Command Line Options

- `--message` or `-m`: The text message to display (required)
- `--year` or `-y`: The year to create the pattern in (default: current year)
- `--repo` or `-r`: Path to repository (default: creates a new repo)
- `--intensity` or `-i`: Commit intensity (1-4, where 4 is darkest)
- `--preview` or `-p`: Preview the pattern without making commits
- `--help` or `-h`: Display help information

### Examples

Create a "HELLO" message in 2023:

bash
python git_commit_tracker.py -m "HELLO" -y 2023

Create a "2024" pattern with maximum intensity:

```bash
python git_commit_tracker.py -m "2024" -i 4
```

Preview what "GITHUB" would look like without committing:

```bash
python git_commit_tracker.py -m "GITHUB" -p
```

## How It Works

The tool works by creating a series of commits with specific dates. GitHub's contribution graph displays different colors based on your activity level for each day. By strategically planning commits on specific days, we can create patterns that form letters, numbers, or simple designs.

Each character in your message is translated into a grid pattern of commits, which when viewed on your GitHub profile, displays your message.

## Customization

You can customize commit patterns by editing the `patterns.py` file, which contains the grid layouts for each supported character.

## FAQ

### Will this affect my existing repositories?

No, unless you specifically target an existing repository. By default, the tool creates a new repository.

### Is this against GitHub's terms of service?

While not explicitly prohibited, use this tool responsibly and avoid excessive commit generation.

### Can I make multiple patterns in different years?

Yes, run the tool multiple times with different year parameters.

## Troubleshooting

### Commits not showing on GitHub

- Ensure your Git email matches your GitHub account email
- GitHub may take time to update the contribution graph
- Verify that the repository has been pushed to GitHub

### Error when running the script

- Check that all dependencies are installed
- Ensure you have proper Git configuration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
