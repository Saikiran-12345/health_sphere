import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime

class InvoicePDFGenerator:
    @staticmethod
    def generate_invoice_pdf(invoice_data: dict) -> bytes:
        """
        Generates a highly detailed, professional Medical Invoice PDF.
        """
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        
        # Header
        c.setFont("Helvetica-Bold", 24)
        c.drawString(0.5 * inch, height - 1 * inch, "HEALTHSPHERE MEDICAL")
        c.setFont("Helvetica", 10)
        c.drawString(0.5 * inch, height - 1.2 * inch, "123 Enterprise Way, Tech District")
        c.drawString(0.5 * inch, height - 1.35 * inch, "contact@healthsphere.com | 1-800-555-0199")
        
        # Invoice Info
        c.setFont("Helvetica-Bold", 16)
        c.drawString(5.5 * inch, height - 1 * inch, "INVOICE")
        c.setFont("Helvetica", 10)
        c.drawString(5.5 * inch, height - 1.2 * inch, f"Invoice ID: {invoice_data.get('id', 'N/A')}")
        c.drawString(5.5 * inch, height - 1.35 * inch, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        
        # Patient Info
        c.setFont("Helvetica-Bold", 12)
        c.drawString(0.5 * inch, height - 2 * inch, "BILL TO:")
        c.setFont("Helvetica", 10)
        c.drawString(0.5 * inch, height - 2.2 * inch, f"Patient Name: {invoice_data.get('patient_name', 'Unknown')}")
        c.drawString(0.5 * inch, height - 2.35 * inch, f"Patient ID: {invoice_data.get('patient_id', 'N/A')}")
        
        # Line Items Table Header
        y_position = height - 3 * inch
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0.5 * inch, y_position, "Description")
        c.drawString(4.0 * inch, y_position, "Qty")
        c.drawString(5.0 * inch, y_position, "Unit Price")
        c.drawString(6.5 * inch, y_position, "Total")
        
        c.line(0.5 * inch, y_position - 0.1 * inch, 7.5 * inch, y_position - 0.1 * inch)
        
        # Line Items
        y_position -= 0.4 * inch
        c.setFont("Helvetica", 10)
        total_amount = 0
        for item in invoice_data.get('items', []):
            desc = item.get('description', '')
            qty = item.get('qty', 1)
            price = item.get('price', 0.0)
            total = qty * price
            total_amount += total
            
            c.drawString(0.5 * inch, y_position, desc)
            c.drawString(4.0 * inch, y_position, str(qty))
            c.drawString(5.0 * inch, y_position, f"${price:.2f}")
            c.drawString(6.5 * inch, y_position, f"${total:.2f}")
            y_position -= 0.25 * inch
            
        c.line(0.5 * inch, y_position, 7.5 * inch, y_position)
        
        # Total
        y_position -= 0.3 * inch
        c.setFont("Helvetica-Bold", 12)
        c.drawString(5.0 * inch, y_position, "TOTAL DUE:")
        c.drawString(6.5 * inch, y_position, f"${total_amount:.2f}")
        
        # Footer
        c.setFont("Helvetica-Oblique", 8)
        c.drawString(0.5 * inch, 0.5 * inch, "Thank you for trusting HealthSphere. Please pay within 30 days.")
        
        c.showPage()
        c.save()
        
        buffer.seek(0)
        return buffer.read()
