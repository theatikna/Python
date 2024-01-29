import fitz  # PyMuPDF
from translate import Translator

def translate_pdf(input_pdf, output_pdf):
    # Open the PDF file
    pdf_document = fitz.open(input_pdf)

    # Initialize Translator
    translator = Translator(to_lang="en")

    # Iterate through all the pages
    for page_num in range(pdf_document.page_count):
        # Get text from the current page
        page = pdf_document.load_page(page_num)
        text = page.get_text()

        # Translate the text
        translated_text = translator.translate(text)

        # Print the translated text (optional)
        print(translated_text)

        # Write the translated text to the new PDF
        page_translated = pdf_document.new_page(width=page.rect.width, height=page.rect.height)
        page_translated.insert_text(page.rect, translated_text)

    # Save the translated PDF
    pdf_document.save(output_pdf)
    pdf_document.close()

if __name__ == "__main__":
    input_pdf_path = "path/to/your/hindi_document.pdf"
    output_pdf_path = "path/to/your/output_english_document.pdf"

    translate_pdf(input_pdf_path, output_pdf_path)
