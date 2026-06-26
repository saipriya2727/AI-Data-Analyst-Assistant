from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(summary, insights):

    doc = SimpleDocTemplate("AI_Report.pdf")

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI DATA ANALYSIS REPORT</b>", styles["Title"]))

    story.append(Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/><br/><b>AI Insights</b>", styles["Heading2"]))

    story.append(Paragraph(insights.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)

    return "AI_Report.pdf"