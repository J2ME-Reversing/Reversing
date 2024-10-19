from zipfile import ZipFile
import os
import binascii

directory = "./OriginalDumps/Sonic the Hedgehog 2 Dash"

dumps = []
for file_name in os.listdir(directory):
    if os.path.isfile(directory + "/" + file_name):
        zip_file = ZipFile(directory + "/" + file_name, 'r')
        macro_checksum = b""

        # Read .class contents
        for sub_file in zip_file.namelist():
            if sub_file.find(".class") > 0:
                macro_checksum = macro_checksum + zip_file.read(sub_file)

        # Insert results into array and close file
        dumps.insert(0,{
            "file_name": file_name,
            "file_hash": hex(binascii.crc32(zip_file.fp.read())),
            "class_hash": hex(binascii.crc32(macro_checksum))
        })
        zip_file.close()


# Export CSV
dumps.sort(key=lambda d: d['class_hash'])
print("File name,File CRC,Class CRC")
for i in dumps:
    print(i["file_name"] + "," + i["file_hash"] + "," + i["class_hash"])