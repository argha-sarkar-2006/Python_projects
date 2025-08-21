from PIL import Image, ImageDraw, ImageFont
import os
if os.path.exists("C:\O Kaaj Ar Jinis\chrome download\Handwriting.png"):
    os.remove("C:\O Kaaj Ar Jinis\chrome download\Handwriting.png")
def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Display the application banner"""
    banner = """
    ******************************************
    *        Handwriting Automation          *
    ******************************************
    """
    print(banner)
def main():
    clear_screen()
    display_banner()
    print("Welcome to the Handwriting Automation Programme!")
main()
path = input("Enter the path of the file (text/docx/pdf): ").strip()
if not os.path.exists(path):
    print("File does not exist. Please check the path and try again.")
    exit()
name = input("Enter the name of the output image file (default is 'Handwriting.png' ): ").strip()
if not name:
    name = "Handwriting.png"
location = input("Enter the location to save the image (default is current directory): ").strip()
if not location:
    location = os.getcwd()+f"//{name}.png"  
else:
    location = os.path.join(location, f"{name}.png")
def text_file():
    with open(path, "r") as file:
        text = file.read()
    return text
def docx_file():                        # install python-docx (pip install python-docx)
    from docx import Document
    doc = Document(path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text
def pdf_file():                              # install PyPDF2 (pip install PyPDF2)
    import PyPDF2
    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text
user = input("Enter the file type (text/docx/pdf): ").strip().lower()
if user == "text":
    text= text_file()
elif user == "docx":
    text= docx_file()
elif user == "pdf":
    text= pdf_file()
else:
    print("Invalid file type. Please enter 'text', 'docx', or 'pdf'.")
    exit()

# Create white canvas
img = Image.new('RGB', (800, 600), color='white')
draw = ImageDraw.Draw(img)
font_path_1 = "D:\O Kaaj Ar Jinis\Software projects\Python Projects\personal\properties\ShadowsIntoLightTwo-Regular.ttf"  # Make sure this file exists


try:
    def create_handwriting_image(text, font_path=font_path_1, font_size=24, output_file= location  ):
    #creating the handwriting image
      font = ImageFont.truetype(font_path, font_size)
      dummy_img = Image.new('RGB', (1, 1))
      draw = ImageDraw.Draw(dummy_img)

    # Calculate image size dynamically using textbbox
      lines = text.split('\n')
      max_width = max([draw.textbbox((0, 0), line, font=font)[2] for line in lines]) + 40
      total_height = len(lines) * (font_size + 10) + 40
    # Create final image
      img = Image.new('RGB', (max_width, total_height), color='white')
      draw = ImageDraw.Draw(img)

      y = 20
      for line in lines:
        draw.text((20, y), line, font=font, fill=(0, 0, 255))
        y += font_size + 10

      img.save(output_file)
      print(f"✅ Image saved as at {output_file}")
    create_handwriting_image(text)
except OSError:
    link_1 = "https://fonts.google.com/selection?categoryFilters=Feeling:%2FExpressive%2FChildlike"
    print(f"Font file '{font_path_1}' not found or could not be opened.")
    print("Please check the font path or Download the font file.")
    print(f"from {link_1} and paste it into font_path_1 variable.")
    print("line number 65 in Handwriting.py")
    exit()