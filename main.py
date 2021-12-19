from os import makedirs
from functions.GenerateQR import GenQRCode
import sys

if __name__ == "__main__":
    if len(sys.argv)<=1:
        sys.exit("Missing arguments!")
    else:
        GenQRCode(sys.argv[1])
        sys.exit("QRCode saved!")