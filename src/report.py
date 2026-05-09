from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(total, top_category):
    doc = SimpleDocTemplate("reports/report.pdf")
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph(f"Total Spending: ₹{total}", styles['Title']))
    content.append(Paragraph(f"Top Category: {top_category}", styles['Normal']))

    doc.build(content)