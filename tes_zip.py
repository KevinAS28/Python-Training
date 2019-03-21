import zipfile

with zipfile.ZipFile("oke", mode="w") as oke:
    oke.write("solo1.py")