from lxml import etree
from scrapy import cmdline


def find_max_texts_el(xml_filename):
    tree = etree.parse(xml_filename)
    root = tree.getroot()
    pages = root.xpath('/data/page')
    max_texts_el = pages[0]
    for i in range(1, len(pages)):
        if pages[i].xpath('count(fragment[@type="text"])') > max_texts_el.xpath('count(fragment[@type="text"])'):
            max_texts_el = pages[i]
    print(etree.tostring(max_texts_el, method='xml', encoding='utf-8', pretty_print=True))


def process_xsl(xml_filename, xsl_filename, html_filename):
    dom = etree.parse(xml_filename)
    xslt = etree.parse(xsl_filename)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    newdom.write(html_filename, xml_declaration=True, encoding='utf-8', pretty_print=True)


def parse_data():
    cmdline.execute("scrapy crawl data".split())


def parse_products():
    cmdline.execute("scrapy crawl eshop".split())


def consoleUi():
    while True:
        print("1.Crawling internet shop\n"
              "2.Process XML to HTML\n"
              "3.Crawling data from website\n"
              "4.Get max amount of text elements page\n"
              "5.Exit\n")
        userInput = input(": ")
        if userInput == '1':
            parse_products()
        elif userInput == '2':
            process_xsl("results/products.xml", "xsl/products.xsl", "results/products.html")
        elif userInput == '3':
            parse_data()
        elif userInput == '4':
            find_max_texts_el("results/data.xml")
        elif userInput == '5':
            break


if __name__ == '__main__':
    consoleUi()


