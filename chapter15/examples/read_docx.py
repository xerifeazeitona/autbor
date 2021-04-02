"""
If you care only about the text, not the styling information, in the
Word document, you can use the `getText()` function. It accepts a
filename of a .docx file and returns a single string value of its text
"""
import docx

def get_text(filename):
    """Returns a single string value of the text in filename"""
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)
