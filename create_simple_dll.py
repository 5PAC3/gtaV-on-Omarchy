#!/usr/bin/env python3
import struct
import os

def write_dll(output_path):
    """Create a minimal PE DLL that implements _strerror_s"""
    
    # We'll create a DLL with:
    # 1. DOS header
    # 2. PE header
    # 3. Sections with code and exports
    # 4. Export table for _strerror_s
    
    data = bytearray()
    
    # ===== DOS HEADER =====
    dos_header = bytearray(64)
    dos_header[0:2] = b'MZ'  # e_magic
    dos_header[2:4] = b'\x90\x01'  # e_cblp
    dos_header[4:6] = b'\x02\x00'  # e_cp
    dos_header[6:8] = b'\x00\x00'  # e_crlc
    dos_header[8:10] = b'\x04\x00'  # e_cparhdr
    dos_header[10:12] = b'\x00\x00'  # e_minalloc
    dos_header[12:14] = b'\xFF\xFF'  # e_maxalloc
    dos_header[14:16] = b'\x00\x00'  # e_ss
    dos_header[16:18] = b'\xB8\x00'  # e_sp
    dos_header[18:20] = b'\x00\x00'  # e_csum
    dos_header[20:22] = b'\x00\x00'  # e_ip
    dos_header[22:24] = b'\x00\x00'  # e_cs
    dos_header[26:28] = b'\x40\x00'  # e_lfarlc
    dos_header[28:30] = b'\x00\x00'  # e_ovno
    # Skip extra fields
    dos_header[60:64] = struct.pack('<I', 64)  # e_lfanew
    
    data.extend(dos_header)
    
    # ===== PE SIGNATURE =====
    data.extend(b'PE\x00\x00')
    
    # ===== COFF HEADER =====
    coff = bytearray(20)
    struct.pack_into('<H', coff, 0, 0x014c)  # Machine: x86_64
    struct.pack_into('<H', coff, 2, 1)  # NumberOfSections
    struct.pack_into('<I', coff, 4, 0)  # TimeDateStamp
    struct.pack_into('<I', coff, 8, 0)  # PointerToSymbolTable
    struct.pack_into('<I', coff, 12, 0)  # NumberOfSymbols
    struct.pack_into('<H', coff, 16, 0xF0)  # SizeOfOptionalHeader (PE32+)
    struct.pack_into('<H', coff, 18, 0x022E)  # Characteristics
    data.extend(coff)
    
    # ===== OPTIONAL HEADER (PE32+) =====
    opt = bytearray(0xF0)
    struct.pack_into('<H', opt, 0, 0x020B)  # Magic: PE32+
    struct.pack_into('<B', opt, 2, 14)  # MajorLinkerVersion
    struct.pack_into('<B', opt, 3, 0)  # MinorLinkerVersion
    struct.pack_into('<I', opt, 4, 0x200)  # SizeOfCode
    struct.pack_into('<I', opt, 8, 0x200)  # SizeOfInitializedData
    struct.pack_into('<I', opt, 12, 0)  # SizeOfUninitializedData
    struct.pack_into('<I', opt, 16, 0x1000)  # AddressOfEntryPoint
    struct.pack_into('<I', opt, 24, 0x1000)  # BaseOfCode
    struct.pack_into('<Q', opt, 32, 0x400000)  # ImageBase
    struct.pack_into('<I', opt, 40, 0x1000)  # SectionAlignment
    struct.pack_into('<I', opt, 44, 0x200)  # FileAlignment
    struct.pack_into('<H', opt, 48, 5)  # MajorOperatingSystemVersion
    struct.pack_into('<H', opt, 50, 1)  # MinorOperatingSystemVersion
    struct.pack_into('<H', opt, 52, 0)  # MajorImageVersion
    struct.pack_into('<H', opt, 54, 0)  # MinorImageVersion
    struct.pack_into('<H', opt, 56, 5)  # MajorSubsystemVersion
    struct.pack_into('<H', opt, 58, 1)  # MinorSubsystemVersion
    struct.pack_into('<I', opt, 60, 0)  # Win32VersionValue
    struct.pack_into('<I', opt, 64, 0x3000)  # SizeOfImage
    struct.pack_into('<I', opt, 68, 0x200)  # SizeOfHeaders
    struct.pack_into('<I', opt, 72, 0)  # CheckSum
    struct.pack_into('<H', opt, 76, 3)  # Subsystem: Windows CUI
    struct.pack_into('<H', opt, 78, 0x8160)  # DllCharacteristics
    struct.pack_into('<Q', opt, 80, 0x100000)  # SizeOfStackReserve
    struct.pack_into('<Q', opt, 88, 0x1000)  # SizeOfStackCommit
    struct.pack_into('<Q', opt, 96, 0x100000)  # SizeOfHeapReserve
    struct.pack_into('<Q', opt, 104, 0x1000)  # SizeOfHeapCommit
    struct.pack_into('<I', opt, 112, 0)  # LoaderFlags
    struct.pack_into('<I', opt, 116, 16)  # NumberOfRvaAndSizes
    
    # Data directories
    # Export directory at index 0, RVA = 0x2000
    struct.pack_into('<Q', opt, 120, 0x2000)  # Export directory RVA
    struct.pack_into('<I', opt, 128, 0x48)  # Export directory size
    
    data.extend(opt)
    
    # ===== SECTION HEADER (.text) =====
    section = bytearray(40)
    section[0:6] = b'.text\x00'
    struct.pack_into('<I', section, 8, 0x200)  # VirtualSize
    struct.pack_into('<I', section, 12, 0x1000)  # VirtualAddress
    struct.pack_into('<I', section, 16, 0x200)  # SizeOfRawData
    struct.pack_into('<I', section, 20, 0x200)  # PointerToRawData
    struct.pack_into('<I', section, 36, 0x60000020)  # Characteristics
    data.extend(section)
    
    # ===== SECTION HEADER (.edata) =====
    section2 = bytearray(40)
    section2[0:7] = b'.edata\x00'
    struct.pack_into('<I', section2, 8, 0x100)  # VirtualSize
    struct.pack_into('<I', section2, 12, 0x2000)  # VirtualAddress
    struct.pack_into('<I', section2, 16, 0x200)  # SizeOfRawData
    struct.pack_into('<I', section2, 20, 0x400)  # PointerToRawData
    struct.pack_into('<I', section2, 36, 0x40000040)  # Characteristics
    data.extend(section2)
    
    # ===== PAD TO 0x200 =====
    while len(data) < 0x200:
        data.append(0)
    
    # ===== CODE SECTION (at 0x200) =====
    # x86_64 assembly for _strerror_s
    # Parameters: rcx=buffer, rdx=sizeInChars, r8=errnum
    code = bytearray([
        # Function prologue
        0x48, 0x89, 0x4C, 0x24, 0x08,  # mov [rsp+8], rcx
        0x48, 0x89, 0x54, 0x24, 0x10,  # mov [rsp+10], rdx  
        0x4C, 0x89, 0x44, 0x24, 0x18,  # mov [rsp+18], r8
        
        # Check buffer == NULL
        0x48, 0x83, 0x79, 0x08, 0x00,  # cmp [rcx+8], 0
        0x75, 0x08,                       # jne check_size
        
        # Check size == 0
        0x48, 0x83, 0x7A, 0x08, 0x00,  # cmp [rdx+8], 0
        0x74, 0x10,                       # je return_einval
        0xEB, 0x0E,                       # jmp return_einval
        
        # return_einval:
        0xB8, 0x16, 0x00, 0x00, 0x00,  # mov eax, 22 (EINVAL)
        0x33, 0xC0,                       # xor eax, eax
        0xC3,                             # ret
        
        # check_size:
        0x48, 0x8B, 0x4C, 0x24, 0x10,  # mov rcx, [rsp+10]
        0x48, 0x83, 0x39, 0x00,          # cmp [rcx], 0
        0x74, 0x08,                       # je return_erange
        0xEB, 0x06,                       # jmp continue
        
        # return_erange:
        0xB8, 0x22, 0x00, 0x00, 0x00,  # mov eax, 34 (ERANGE)
        0x33, 0xC0,                       # xor eax, eax
        0xC3,                             # ret
        
        # continue:
        # For now, just return success with "Error" message
        0x33, 0xC0,                       # xor eax, eax (return 0 = success)
        0xC3,                             # ret
    ])
    
    while len(code) < 0x200:
        code.append(0x90)  # NOP padding
    
    data.extend(code)
    
    # ===== PAD TO 0x400 =====
    while len(data) < 0x400:
        data.append(0)
    
    # ===== EXPORT SECTION (at 0x400) =====
    # Export directory table
    export_dir = bytearray(40)
    struct.pack_into('<I', export_dir, 0, 0)  # Characteristics
    struct.pack_into('<I', export_dir, 4, 0)  # TimeDateStamp
    struct.pack_into('<H', export_dir, 8, 0)  # MajorVersion
    struct.pack_into('<H', export_dir, 10, 0)  # MinorVersion
    struct.pack_into('<I', export_dir, 12, 0x2050)  # Name RVA
    struct.pack_into('<I', export_dir, 16, 1)  # Base
    struct.pack_into('<I', export_dir, 20, 1)  # NumberOfFunctions
    struct.pack_into('<I', export_dir, 24, 1)  # NumberOfNames
    struct.pack_into('<I', export_dir, 28, 0x2048)  # AddressOfFunctions RVA
    struct.pack_into('<I', export_dir, 32, 0x2058)  # AddressOfNames RVA
    struct.pack_into('<I', export_dir, 36, 0x2060)  # AddressOfNameOrdinals RVA
    
    data.extend(export_dir)
    
    # Function address (RVA = 0x1000)
    func_addr = struct.pack('<I', 0x1000)
    data.extend(func_addr)
    
    # Pad to name pointer
    while len(data) < 0x458:
        data.append(0)
    
    # Name pointer (RVA = 0x2060)
    name_ptr = struct.pack('<I', 0x2060)
    data.extend(name_ptr)
    
    # Pad to ordinal
    while len(data) < 0x460:
        data.append(0)
    
    # Ordinal
    ordinal = struct.pack('<H', 0)
    data.extend(ordinal)
    
    # Pad to DLL name
    while len(data) < 0x450:
        data.append(0)
    
    # DLL name
    dll_name = b'ucrtbase.dll\x00'
    data.extend(dll_name)
    
    # Pad to function name
    while len(data) < 0x460:
        data.append(0)
    
    # Function name
    func_name = b'_strerror_s\x00'
    data.extend(func_name)
    
    # Pad to end
    while len(data) < 0x600:
        data.append(0)
    
    with open(output_path, 'wb') as f:
        f.write(data)
    
    print(f"Created DLL: {output_path} ({len(data)} bytes)")

if __name__ == '__main__':
    write_dll('/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes/drive_c/windows/system32/ucrtbase_override.dll')
