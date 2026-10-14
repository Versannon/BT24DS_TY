import os
import markdown
from playwright.sync_api import sync_playwright

def generate_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, 'answers.md')
    html_path = os.path.join(base_dir, 'answers.html')
    pdf_path = os.path.join(base_dir, 'answers.pdf')

    print(f"Reading markdown from: {md_path}")
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Convert markdown to HTML with necessary extensions
    html_body = markdown.markdown(
        text,
        extensions=[
            'tables',
            'fenced_code',
            'toc',
            'attr_list',
            'def_list'
        ]
    )

    # HTML template with publication-quality CSS
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ETL & Apache Kafka Question Bank Answers</title>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap');

    @page {{
        size: A4;
        margin: 20mm 15mm 20mm 15mm;
    }}

    body {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: #1e293b;
        line-height: 1.55;
        font-size: 9.5pt;
        background-color: #ffffff;
        margin: 0;
        padding: 0;
    }}

    h1 {{
        color: #0f172a;
        font-size: 20pt;
        font-weight: 800;
        border-bottom: 2.5px solid #4f46e5;
        padding-bottom: 8px;
        margin-top: 0;
        margin-bottom: 16px;
        page-break-after: avoid;
    }}

    h2 {{
        color: #1e1b4b;
        font-size: 13.5pt;
        font-weight: 700;
        border-bottom: 1.5px solid #e2e8f0;
        padding-bottom: 6px;
        margin-top: 26px;
        margin-bottom: 12px;
        page-break-after: avoid;
        break-before: page;
    }}

    /* First h2 after table of contents does not need extra break */
    h2:first-of-type {{
        break-before: auto;
    }}

    h3 {{
        color: #312e81;
        font-size: 11pt;
        font-weight: 600;
        margin-top: 16px;
        margin-bottom: 6px;
        page-break-after: avoid;
    }}

    h4 {{
        color: #4338ca;
        font-size: 10pt;
        font-weight: 600;
        margin-top: 12px;
        margin-bottom: 4px;
        page-break-after: avoid;
    }}

    p {{
        margin-top: 0;
        margin-bottom: 7px;
        text-align: justify;
    }}

    blockquote {{
        background-color: #f8fafc;
        border-left: 4px solid #4f46e5;
        margin: 10px 0;
        padding: 8px 12px;
        color: #334155;
        font-style: italic;
        border-radius: 0 4px 4px 0;
        page-break-inside: avoid;
    }}

    blockquote p {{
        margin: 0;
        font-style: normal;
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 12px 0;
        font-size: 8pt;
        page-break-inside: avoid;
    }}

    th {{
        background-color: #f1f5f9;
        color: #0f172a;
        font-weight: 700;
        border: 1px solid #cbd5e1;
        padding: 5px 7px;
        text-align: left;
    }}

    td {{
        border: 1px solid #e2e8f0;
        padding: 4px 7px;
        vertical-align: top;
    }}

    tr:nth-child(even) {{
        background-color: #f8fafc;
    }}

    code {{
        font-family: 'Fira Code', Consolas, monospace;
        font-size: 8pt;
        background-color: #f1f5f9;
        color: #0f172a;
        padding: 1px 4px;
        border-radius: 3px;
        border: 1px solid #e2e8f0;
    }}

    pre {{
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 3.5px solid #4f46e5;
        padding: 8px 10px;
        border-radius: 4px;
        overflow-x: auto;
        margin: 8px 0;
        page-break-inside: avoid;
    }}

    pre code {{
        background: transparent;
        border: none;
        padding: 0;
        font-size: 7.8pt;
        line-height: 1.4;
        color: #0f172a;
    }}

    img {{
        max-width: 90%;
        height: auto;
        display: block;
        margin: 12px auto 4px auto;
        border: 1px solid #e2e8f0;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        page-break-inside: avoid;
    }}

    em {{
        color: #64748b;
        font-size: 8pt;
        display: block;
        text-align: center;
        margin-bottom: 10px;
    }}

    ul, ol {{
        margin-top: 3px;
        margin-bottom: 8px;
        padding-left: 18px;
    }}

    li {{
        margin-bottom: 3px;
    }}

    hr {{
        border: none;
        border-top: 1px solid #e2e8f0;
        margin: 18px 0;
    }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated HTML at: {html_path}")

    # Launch Chromium and print to PDF
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Convert path to file URL for windows
        file_url = 'file:///' + html_path.replace('\\', '/')
        print(f"Loading URL: {file_url}")
        page.goto(file_url)
        page.wait_for_load_state('networkidle')

        print(f"Generating PDF: {pdf_path}")
        page.pdf(
            path=pdf_path,
            format='A4',
            print_background=True,
            margin={
                'top': '18mm',
                'bottom': '18mm',
                'left': '14mm',
                'right': '14mm'
            },
            display_header_footer=True,
            header_template='<div style="font-size: 7.5pt; color: #64748b; width: 100%; text-align: right; padding-right: 14mm; font-family: -apple-system, sans-serif;">ETL & Apache Kafka — Complete Question Bank Answers</div>',
            footer_template='<div style="font-size: 7.5pt; color: #64748b; width: 100%; text-align: center; font-family: -apple-system, sans-serif;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>'
        )
        browser.close()

    print(f"SUCCESS: PDF generated at: {pdf_path}")

if __name__ == '__main__':
    generate_pdf()
