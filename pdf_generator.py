# pdf_generator.py

from fpdf import FPDF
from PIL import Image
import tempfile
import logging
import numpy as np
import os

logging.basicConfig(level=logging.INFO)

def create_pdf_with_snapshots(steps):
    """
    Creates a PDF with each step and its corresponding snapshot.
    """
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        for i, (timestamp, description, snapshot) in enumerate(steps):
            pdf.add_page()
            pdf.multi_cell(0, 10, f'Step {i+1}: {description}', align='L')
            pdf.ln(5)

            # Create a temporary file path
            fd, img_path = tempfile.mkstemp(suffix=".jpg")
            os.close(fd)  # Close the file descriptor immediately

            # Save the snapshot to the temporary file
            img = Image.fromarray(
                (snapshot * 255).astype(np.uint8)
            ) if snapshot.dtype == np.float32 else Image.fromarray(snapshot)
            img.save(img_path)

            # Calculate image width and height to maintain aspect ratio
            pdf_w = pdf.w - 2 * pdf.l_margin
            img_w, img_h = img.size
            aspect = img_h / img_w
            img_width = pdf_w
            img_height = pdf_w * aspect

            # Add the image to the PDF
            pdf.image(img_path, x=pdf.l_margin, y=pdf.get_y(), w=img_width)

            pdf.ln(img_height + 5)  # Move cursor below the image

            # Delete the temporary image file
            os.remove(img_path)

        output_filename = "step_by_step_tutorial.pdf"
        pdf.output(output_filename)
        logging.info(f"PDF saved as {output_filename}")
    except Exception as e:
        logging.error(f"PDF generation failed: {e}")
        raise
