import pandas as pd
import os


def clean_title(title):
    return title.split(':')[0].strip()


def get_read_titles_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    read_books = (
        df[df['Read Status'].str.lower() == 'read']['Title'].str.strip().tolist()
    )
    cleaned_titles = [clean_title(title) for title in read_books]
    return cleaned_titles


def get_local_markdown_titles(directory):
    markdown_titles = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                title = os.path.splitext(file)[0]
                markdown_titles.append(title)
    return markdown_titles


def find_missing_titles(csv_titles, local_titles):
    missing_titles = [title for title in csv_titles if title not in local_titles]
    return missing_titles


if __name__ == "__main__":
    csv_file_name = input("Enter the CSV file name (with extension): ").strip()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_directory, csv_file_name)
    local_directory = (
        "/Users/michaelslain/Documents/library of alexandria/🚬 reading/books"
    )
    csv_titles = get_read_titles_from_csv(csv_path)
    local_titles = get_local_markdown_titles(local_directory)
    missing_titles = find_missing_titles(csv_titles, local_titles)
    print("Titles marked as 'read' in the CSV that are missing locally:")
    for title in missing_titles:
        print(title)
