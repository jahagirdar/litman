import freeplane
from .pdf_parser import parse_pdf


def update_mindmap(filename='/home/vijayvithal/Documents/mindmaps/RISCV.mm'):
    '''
    Takes in a string containing the path to the mindmap file and performs the following actions:

    - finds a node called litman.
    - Parses the child nodes of litman for documents. Documents should have an attribute called `location` containing the path to the pdf file.
    - calls pdf_parser to parse each identified file.
    - Creates child nodes containing the highlights from the pdf file.
    - If the child node already exists, updates it. This was any subchild nodes manually created are retained.
    '''
    mindmap = freeplane.Mindmap(filename)
    lit = mindmap.find_nodes(core="litman")
    if not lit:
        return
    lit = lit[0]
    for child in lit.children:
        pdffile = child.attributes['location']
        highlights = parse_pdf(pdffile)
        for id, page, hl, comment in highlights:
            has_node = False
            for subchild in child.children:
                if subchild.attributes['uuid'] == id:
                    subchild.plaintext = f"{hl}\n{comment}"
                    has_node = True
                    break
            if not has_node:
                new_child = child.add_child(
                    core=f"{hl}<br/>{comment}", TEXT_SHORTENED="true")
                new_child.add_attribute('page', f"{page}")
                new_child.add_attribute('uuid', f"{id}")
    mindmap.save('/tmp/t.mm')
