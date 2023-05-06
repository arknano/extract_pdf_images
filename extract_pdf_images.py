import fitz
import os
import sys

if len(sys.argv) < 2:
    print("Usage: python extract_pdf_images.py \"path/to/your/pdf.pdf\"")
    sys.exit(1)

file = sys.argv[1]

pdf_file = fitz.open(file)
pdf_dir = os.path.dirname(file)


for page_index in range(len(pdf_file)):

    page = pdf_file[page_index]

    for image_index, img in enumerate(page.get_images(), start=1):

        # get the XREF of the image
        xref = img[0]

        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]

        # get the image extension
        image_ext = base_image["ext"]

        # create the image file name
        image_name = f"image{page_index}_{image_index}.{image_ext}"

        # save the image in the same folder as the input PDF
        image_path = os.path.join(pdf_dir, image_name)
        with open(image_path, "wb") as f:
            f.write(image_bytes)

        print(f"Saved image {image_index} on page {page_index} as {image_path}")