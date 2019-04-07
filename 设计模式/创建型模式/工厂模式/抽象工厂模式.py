""" Python Character Mapping Codec cp1256 generated from 'MAPPINGS/VENDORS/MICSFT/WINDOWS/CP1256.TXT' with gencodec.py.

"""  # "

import codecs


### Codec APIs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='cp1256',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Table

decoding_table = (
    '\x00'  # 0x00 -> NULL
    '\x01'  # 0x01 -> START OF HEADING
    '\x02'  # 0x02 -> START OF TEXT
    '\x03'  # 0x03 -> END OF TEXT
    '\x04'  # 0x04 -> END OF TRANSMISSION
    '\x05'  # 0x05 -> ENQUIRY
    '\x06'  # 0x06 -> ACKNOWLEDGE
    '\x07'  # 0x07 -> BELL
    '\x08'  # 0x08 -> BACKSPACE
    '\t'  # 0x09 -> HORIZONTAL TABULATION
    '\n'  # 0x0A -> LINE FEED
    '\x0b'  # 0x0B -> VERTICAL TABULATION
    '\x0c'  # 0x0C -> FORM FEED
    '\r'  # 0x0D -> CARRIAGE RETURN
    '\x0e'  # 0x0E -> SHIFT OUT
    '\x0f'  # 0x0F -> SHIFT IN
    '\x10'  # 0x10 -> DATA LINK ESCAPE
    '\x11'  # 0x11 -> DEVICE CONTROL ONE
    '\x12'  # 0x12 -> DEVICE CONTROL TWO
    '\x13'  # 0x13 -> DEVICE CONTROL THREE
    '\x14'  # 0x14 -> DEVICE CONTROL FOUR
    '
