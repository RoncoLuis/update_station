from distutils.core import setup
import py2exe

setup(
    name="tst-updatestation",
    version="0.1",
    description="prueba ejecutable updatestation",
    author="Luis Ronquillo",
    author_email="13240306@itleon.edu.mx",
    url="https://github.com/RoncoLuis",
    license="GPL",
    scripts=["barcodeReader_2.py"],
    console = ["barcodeReader_2.py"]
)
