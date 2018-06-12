Universal Mega Dumper
=====================

Write something inspiring here.


Install
-------

To install run `python3 setup.py install`.

::
|   $ umd -h
|   usage: umd [-h] [--mode {cv,gen,sms,pce,tg,snes}]
|              [--checksum | --byteswap file to byte swap 
|                  | --rd {rom,save,bram,header,fid,sfid,sf,sflist,byte,word,sbyte,sword}
|                  | --wr {rom,save,bram,sf} | --clr {rom,rom2,save,bram,sf}]
|              [--addr ADDR] [--size SIZE] [--file FILE] [--sfile SFILE]
|   
|   optional arguments:
|     -h, --help            show this help message and exit
|     --mode {cv,gen,sms,pce,tg,snes}
|                           Set the cartridge type
|     --checksum            Calculate ROM checksum
|     --byteswap file to byte swap
|                           Reverse the endianness of a file
|     --rd {rom,save,bram,header,fid,sfid,sf,sflist,byte,word,sbyte,sword}
|                           Read from UMD
|     --wr {rom,save,bram,sf}
|                           Write to UMD
|     --clr {rom,rom2,save,bram,sf}
|                           Clear a memory in the UMD
|     --addr ADDR           Address for current command
|     --size SIZE           Size in bytes for current command
|     --file FILE           File path for read/write operations
|     --sfile SFILE         8.3 filename for UMD's serial flash

Install For Devleopment
-----------------------

1. Setup virtual environment, `python3 -m venv venv`.
2. Activate environment `source ./venv/bin/activate`.
3. To install for development `pip install -e .`.

