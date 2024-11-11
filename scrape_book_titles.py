import os


def collect_markdown_titles(base_path):
    book_titles = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md'):
                title = os.path.splitext(file)[0]
                book_titles.append(title)

    return book_titles


def export_titles_to_txt(titles, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for title in titles:
            f.write(title + '\n')


base_directory = "/Users/michaelslain/Documents/library of alexandria/🚬 reading/books"
output_file_path = "/Users/michaelslain/Documents/dev/book-scripts/book_titles.txt"

titles = collect_markdown_titles(base_directory)
export_titles_to_txt(titles, output_file_path)

print(f"Markdown file titles collected and exported to {output_file_path}")
