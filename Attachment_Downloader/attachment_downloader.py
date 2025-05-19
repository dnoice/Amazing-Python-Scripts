"""
Gmail Attachment Downloader
A script to easily search and download Gmail attachments based on search queries.
"""
import os
import ezgmail
import datetime
from typing import List, Optional


def download_attachments(result_threads: List, download_dir: Optional[str] = None) -> None:
    """
    Download all attachments from Gmail threads that match search criteria.
    
    Args:
        result_threads: List of GmailThread objects from search results
        download_dir: Directory to save attachments (defaults to current directory)
    
    Raises:
        Exception: If there's an error during download
    """
    # Ensure download directory exists (atomically avoiding race conditions)
    if download_dir:
        os.makedirs(download_dir, exist_ok=True)
        print(f"Created directory: {download_dir}")
    
    # Store original working directory
    original_dir = os.getcwd()
    
    # Change to download directory if specified
    if download_dir:
        os.chdir(download_dir)
    
    count_of_results = len(result_threads)
    downloaded_files = 0
    
    try:
        print(f"Starting download of attachments from {count_of_results} thread(s)...")
        
        for i, thread in enumerate(result_threads):
            thread_count = i + 1
            print(f"Processing thread {thread_count}/{count_of_results}: {thread.messages[0].subject}")
            
            # Check if thread has multiple messages
            if len(thread.messages) > 1:
                for j, message in enumerate(thread.messages):
                    msg_count = j + 1
                    print(f"  - Downloading attachments from message {msg_count}/{len(thread.messages)}")
                    downloaded = message.downloadAllAttachments()
                    downloaded_files += len(downloaded)
                    if downloaded:
                        print(f"    Downloaded: {', '.join(downloaded)}")
            else:
                # Thread has only one message
                downloaded = thread.messages[0].downloadAllAttachments()
                downloaded_files += len(downloaded)
                if downloaded:
                    print(f"  - Downloaded: {', '.join(downloaded)}")
        
        print(f"\nDownload complete! {downloaded_files} file(s) downloaded.")
        if download_dir:
            print(f"Files saved to: {os.path.abspath(download_dir)}")
        else:
            print(f"Files saved to: {os.getcwd()}")
            
    except Exception as e:
        print(f"Error occurred while downloading attachment(s): {str(e)}")
        raise
    finally:
        # Return to original directory if we changed it
        if download_dir:
            os.chdir(original_dir)


def main():
    """Main function to run when script is executed directly."""
    print("=" * 50)
    print("Gmail Attachment Downloader")
    print("=" * 50)
    
    # Check if ezgmail is authenticated
    try:
        ezgmail.init()
        print(f"Logged in as: {ezgmail.EMAIL_ADDRESS}\n")
    except Exception as e:
        print("Authentication error. Please follow setup instructions in README.md")
        print(f"Error details: {str(e)}")
        return
    
    # Get search query from user
    query = input("Enter search query (e.g., 'from:example@gmail.com'): ").strip()
    if not query:
        print("Search query cannot be empty. Exiting...")
        return
    
    # Always include attachment filter in the search
    search_query = f"{query} has:attachment"
    
    print(f"\nSearching for: {search_query}")
    print("This may take a moment depending on your inbox size...")
    
    try:
        # Perform the search
        result_threads = ezgmail.search(search_query)
        
        if not result_threads:
            print("\nNo results found with attachments matching your query.")
            return
            
        # Display results
        print(f"\nFound {len(result_threads)} result(s) with attachments:")
        for i, thread in enumerate(result_threads):
            subject = thread.messages[0].subject
            date = datetime.datetime.fromtimestamp(thread.messages[0].timestamp)
            formatted_date = date.strftime("%Y-%m-%d %H:%M")
            print(f"{i+1}. [{formatted_date}] {subject}")
        
        # Ask user if they want to download
        while True:
            download_confirmation = input("\nDo you want to download the attachment(s)? (y/n): ").strip().lower()
            if download_confirmation in ['y', 'yes']:
                # Ask for download directory
                custom_dir = input("Enter download directory (leave empty for current directory): ").strip()
                download_attachments(result_threads, custom_dir if custom_dir else None)
                break
            elif download_confirmation in ['n', 'no']:
                print("Download canceled. Exiting...")
                break
            else:
                print("Please enter 'y' or 'n'.")
                
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")


if __name__ == '__main__':
    main()
