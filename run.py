"""File containing examples on how to run the QuoteEngine and MemeGenerator."""
from QuoteEngine import Ingestor
from MemeGenerator import MemeGenerator

# Quote engine examples
print()
print('QUOTE ENGINE EXAMPLES')
print(f"CSV: {Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')}")
print(f"DOCX: {Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx')}")
print(f"TXT: {Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt')}")
print(f"PDF: {Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf')}")
print()

# Meme Generator examples
print('MEME GENERATOR EXAMPLE')
img_path = '_data/photos/dog/xander_1.jpg'
output_dir = 'tmp'

meme = MemeGenerator(output_dir)
output_path = meme.make_meme(img_path, 'Hello my family!', 'Takeshi')
print(f'Output path for meme generator: {output_path}')
print()
