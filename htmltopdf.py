import pdfkit
url = input("请输入网页的完整网址：")
conf = pdfkit.configuration(wkhtmltopdf='e:/wkhtmltox/bin/wkhtmltopdf.exe')
pdfkit.from_url(url,'网页.pdf',configuration=conf)