# Based on https://stackoverflow.com/a/62859169/562769

from typing import List, Tuple

import fitz  # install with 'pip install pymupdf'


def _parse_highlight(
        annot: fitz.Annot,
        wordlist: List[
            Tuple[float, float, float, float, str, int, int, int]
        ]
) -> str:
    points = annot.vertices
    quad_count = int(len(points) / 4)
    sentences = []
    for i in range(quad_count):
        # where the highlighted part is
        r = fitz.Quad(points[i * 4: i * 4 + 4]).rect

        words = [w for w in wordlist if fitz.Rect(w[:4]).intersects(r)]
        sentences.append(" ".join(w[4] for w in words))
    sentence = " ".join(sentences)
    return sentence


def handle_page(page):
    wordlist = page.get_text("words")  # list of words on page
    wordlist.sort(key=lambda w: (w[3], w[0]))  # ascending y, then x

    highlights = []
    annot = page.first_annot
    while annot:
        if annot.type[0] == 8:
            hl = _parse_highlight(annot, wordlist)
            highlights.append(
                (annot.info['id'], page.number, hl, annot.info['content']))
        annot = annot.next
    return highlights


def parse_pdf(filepath: str) -> List:
    '''
    Parse the given pdf file, extract all highlights and comments. return a list of tuples containing the  following values

    - id : a uuid string
    - Page number: The page on which the annotation was found
    - highlight: the sting that was highlighted
    - comment: Any comment associated with the highlight.
    '''

    doc = fitz.open(filepath)

    highlights = []
    for page in doc:
        highlights += handle_page(page)

    return highlights


if __name__ == "__main__":
    print(parse_pdf("/home/vijayvithal/Downloads/riscv-spec-20191213.pdf"))
