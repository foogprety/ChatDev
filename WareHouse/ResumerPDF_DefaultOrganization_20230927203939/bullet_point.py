'''
This file contains functions to format the content with bullet points.
'''
import re
def format_with_bullet_points(content):
    '''
    Format the content with bullet points.
    Args:
        content (str): The content to be formatted.
    Returns:
        str: The formatted content with bullet points.
    '''
    bullet_points = re.findall(r'^\s*[-•*]\s*(.*)$', content, flags=re.MULTILINE)
    formatted_content = ""
    for point in bullet_points:
        formatted_content += f"• {point}\n"
    return formatted_content