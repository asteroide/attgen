from . import generate
from . import pdf_reference

def run():
    pdf_reference.generate()
    generate.main()

if __name__ == "__main__":
    run()
