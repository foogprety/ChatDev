from pdf_parser import parse_pdf
from bullet_point import format_with_bullet_points
from translation import translate_to_french
# Specify the path to the PDF file
pdf_file_path = "C:/Users/Web/Downloads/Avis de cotisation Samia Ahmed Nour.pdf"
# Parse the PDF file and extract the content
content = parse_pdf(pdf_file_path)
# Format the content with bullet points
formatted_content = format_with_bullet_points(content)
# Translate the content to French
translated_content = translate_to_french(formatted_content)
# Print the translated content
print(translated_content)