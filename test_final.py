import os
import re

def search_email_in_files(email_to_search, search_root):
    email_pattern = re.compile(re.escape(email_to_search), re.IGNORECASE)
    found_files = []

    print(f"\nStarting search for email '{email_to_search}' under '{search_root}' (this might take some time)...\n")

    for root, dirs, files in os.walk(search_root):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read()
                        if email_pattern.search(content):
                            found_files.append(file_path)
                            print(f"Found email in: {file_path}")
                except Exception as e:
                    # Permission errors, unreadable files etc.
                    continue

    if not found_files:
        print(f"\nEmail '{email_to_search}' NOT FOUND in any files under '{search_root}'.")
    else:
        print(f"\nEmail '{email_to_search}' found in {len(found_files)} files.")

if __name__ == "__main__":
    email_to_find = input("Enter the email address to search for: ").strip()

    search_root = input("Enter root directory to start search (default C:\\ on Windows, / on Linux/Mac): ").strip()
    if not search_root:
        import platform
        if platform.system() == "Windows":
            search_root = "C:\\"
        else:
            search_root = "/"

    search_email_in_files(email_to_find, search_root)
