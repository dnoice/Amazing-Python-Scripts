# Gmail Attachment Downloader

A Python script to easily search and download Gmail attachments based on search queries.

## Features

- Search Gmail using Google's powerful search operators
- View email search results with dates and subjects
- Download attachments from search results to a specified directory
- Progress tracking during downloads
- User-friendly command-line interface

## Requirements

- Python 3.6+
- ezgmail library
- Google API credentials

## Setup Instructions

### 1. Install Required Packages

```bash
pip install ezgmail
```

### 2. Get Google API Credentials

1. Visit the [Google API Console](https://developers.google.com/gmail/api/quickstart/python)
2. Click the "Enable the Gmail API" button
3. Select "Desktop app" as the OAuth Client type when prompted
4. Download the `credentials.json` file and place it in the same directory as this script

### 3. First-Time Authentication

The first time you run the script, it will:
1. Open a browser window asking you to log in to your Gmail account
2. Request permission for the app to access your Gmail
3. Generate a `token.json` file in the script directory to save your authentication

## Usage

1. Run the script:
```bash
python attachment_downloader.py
```

2. Enter your search query when prompted. The script supports all Gmail search operators, for example:
   - `from:example@gmail.com` - Emails from a specific address
   - `subject:report` - Emails with "report" in the subject
   - `after:2023/01/01 before:2023/12/31` - Emails within a date range
   - `label:work` - Emails with a specific label
   - `has:pdf` - Emails with PDF attachments
   - Combine operators: `from:example@gmail.com subject:report has:pdf`

3. Review the search results

4. Confirm if you want to download the attachments

5. Specify a download directory (optional)

## Search Query Examples

- `from:payroll@company.com has:spreadsheet` - Payroll spreadsheets
- `subject:(invoice OR receipt) after:2023/05/01` - Recent invoices or receipts
- `from:newsletter@example.com label:newsletters` - Newsletter emails with a specific label
- `filename:pdf larger:5M` - PDF attachments larger than 5MB
- `from:myteam@company.com has:attachment -has:document` - Team emails with attachments that aren't documents

## Troubleshooting

### Authentication Issues

- Make sure you have the `credentials.json` file in the same directory as the script
- If you change Google accounts, delete the `token.json` file and re-authenticate
- If you see permission errors, check that you've enabled the Gmail API for your Google account

### Search Problems

- Gmail search can be case-sensitive for some operators
- Ensure your search syntax is correct (see [Gmail search operators](https://support.google.com/mail/answer/7190?hl=en))
- Very large inboxes may take longer to search or time out

### Download Issues

- Check if you have write permissions for the download directory
- Very large attachments might take time to download
- Gmail API has usage limits that might affect bulk downloads

## Advanced Usage

- To automate downloads, you can modify the script to accept command-line arguments
- For recurring downloads, consider setting up as a scheduled task
- To filter by attachment types, use search operators like `has:pdf`, `has:spreadsheet`, etc.

## License

This project is open source and available under the MIT License.

# Author

Contributed by Kirtan Bhatt

Updated: Dennis 'dnoice' Smaltz May 19, 2025
