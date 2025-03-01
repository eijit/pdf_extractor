import sys
import pyocr
from pypdf import PdfReader
from PIL import Image
from io import BytesIO

def main():
    argv = sys.argv
    if len(argv) < 2:
        sys.stderr.write('python {} input.pdf'.format(argv[0]))
        return
    pdf_path = argv[1]

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("OCR tool is not found.")
        return
    tool = tools[0]
    lan = "jpn"

    reader = PdfReader(pdf_path)

    print("# {}".format(pdf_path))
    for i, page in enumerate(reader.pages):
        print("\n## page.{}\n".format(i + 1))
        for image in page.images:
            text = tool.image_to_string(Image.open(BytesIO(image.data)), lang=lan)
            print(text)


if __name__ == '__main__':
    main()
