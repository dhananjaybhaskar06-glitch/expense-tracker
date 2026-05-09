from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

os.makedirs("reports", exist_ok=True)

def generate_pdf(total, top_category):
    doc = SimpleDocTemplate("reports/report.pdf")
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph(f"Total Spending: ₹{total}", styles['Title']))
    content.append(Paragraph(f"Top Category: {top_category}", styles['Normal']))

    doc.build(content)