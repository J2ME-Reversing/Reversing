// Use ImHex to use this pattern, used to read the contents of a .pak file.
#pragma endian big

struct FileHeader {
    u32 unused;
    u32 offset;
    u32 length;
    u8 contents[length] @ offset; 
} [[hex::visualize("image", contents)]];

struct PakReader {
    u16 length;
    FileHeader file_header[length];
};

PakReader pak @0x00;