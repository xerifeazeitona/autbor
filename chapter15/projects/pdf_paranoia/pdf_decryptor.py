"""
PDF Paranoia
Using the os.walk() function from Chapter 10, write a script that will
go through every PDF in a folder (and its subfolders) and encrypt the
PDFs using a password provided on the command line.
Save each encrypted PDF with an *_encrypted.pdf* suffix added to the
original filename.
Before deleting the original file, have the program attempt to read and
decrypt the file to ensure that it was encrypted correctly.
Then, write a program that finds all encrypted PDFs in a folder
(and its subfolders) and creates a decrypted copy of the PDF using a
provided password.
If the password is incorrect, the program should print a message to the
user and continue to the next PDF.
"""
import os
import re
import PyPDF2

def test_decryption(pdf_file):
    """Check if 'pdf_file' is encrypted"""
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))
    return pdf_reader.isEncrypted

def decrypt_file(pdf_file, password):
    """Decrypts 'pdf_file' with the provided 'password'."""
    file_to_decrypt = open(pdf_file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(file_to_decrypt)
    if not pdf_reader.isEncrypted:
        print('Already decrypted, ', end='')
        return False
    pdf_reader.decrypt(password)
    pdf_writer = PyPDF2.PdfFileWriter()
    for page_num in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_num))

    regex = re.compile(r'(.*)_encrypted\.')
    mo = regex.match(pdf_file)
    if mo:
        decrypted_filename = mo.group(1)
    decrypted_filename += os.path.splitext(pdf_file)[1]
    result_pdf = open(decrypted_filename, 'wb')
    pdf_writer.write(result_pdf)
    result_pdf.close()
    # Check if the file was decrypted successfully
    if test_decryption(decrypted_filename):
        return False
    return True

def decrypt_folder(directory, password):
    """Decrypts all PDFs in 'directory' with 'password'"""
    for folder, _, files in os.walk(directory):
        print(f'\nChecking {os.path.basename(folder)}...')
        for filename in files:
            if filename.lower().endswith('pdf'):
                print(f'Decrypting {filename}...', end='')
                if decrypt_file(os.path.join(folder, filename), password):
                    print('OK')
                    os.unlink(os.path.join(folder, filename))
                else:
                    print('skipped.')
    print('\n...done!')

source_folder = os.getcwd() + '/sample_data'
decrypt_folder(source_folder, '123456')
