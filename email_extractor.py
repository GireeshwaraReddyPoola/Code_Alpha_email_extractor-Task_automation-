
import os
import re

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(input_path):
    """
    Read input_path and return a sorted list of unique email addresses.
    Raises FileNotFoundError if the file does not exist.
    """
    with open(input_path, "r", encoding="utf-8") as file:
        text = file.read()

    found = re.findall(EMAIL_PATTERN, text)
    unique_emails = sorted(set(email.lower() for email in found))
    return unique_emails


def save_emails(emails, output_path):
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")


def main():
    input_path = "sample_input.txt"
    output_path = "output/emails_found.txt"

    try:
        emails = extract_emails(input_path)
    except FileNotFoundError:
        print(f"Input file not found: {input_path}")
        return

    if not emails:
        print("No email addresses found.")
        return

    save_emails(emails, output_path)
    print(f"Found {len(emails)} unique email(s).")
    for email in emails:
        print(f"  - {email}")
    print(f"\nSaved to {output_path}")


if __name__ == "__main__":
    main()
