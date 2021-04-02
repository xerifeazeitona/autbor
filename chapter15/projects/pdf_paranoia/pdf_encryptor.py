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
import PyPDF2

def test_encryption(pdf_file, password):
    """Try to decrypt 'pdf_file' with 'password'"""
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))
    return pdf_reader.decrypt(password)

def encrypt_file(pdf_file, password):
    """Encrypts 'pdf_file' with the provided 'password'."""
    file_to_encrypt = open(pdf_file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(file_to_encrypt)
    # Skip if the file is already encrypted
    if pdf_reader.isEncrypted:
        print('Already encrypted, ', end='')
        return False
    # Create a copy of pdf_file
    pdf_writer = PyPDF2.PdfFileWriter()
    for page_num in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_num))
    # Encrypt the copy
    pdf_writer.encrypt(password)
    # Save the encrypted copy
    encrypted_filename = f'{os.path.splitext(pdf_file)[0]}_encrypted'
    encrypted_filename += os.path.splitext(pdf_file)[1]
    result_pdf = open(encrypted_filename, 'wb')
    pdf_writer.write(result_pdf)
    result_pdf.close()
    # Check if the file was encrypted successfully
    if test_encryption(encrypted_filename, password) == 0:
        return False
    return True

def encrypt_folder(directory, password):
    """Encrypts all PDFs in 'directory' with 'password'"""
    for folder, _, files in os.walk(directory):
        print(f'\nChecking {os.path.basename(folder)}...')
        for filename in files:
            if filename.lower().endswith('pdf'):
                print(f'Encrypting {filename}...', end='')
                if encrypt_file(os.path.join(folder, filename), password):
                    print('OK')
                    os.unlink(os.path.join(folder, filename))
                else:
                    print('skipped.')
    print('\n...done!')

source_folder = os.getcwd() + '/sample_data'
encrypt_folder(source_folder, '123456')
