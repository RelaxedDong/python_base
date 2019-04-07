""" Python Character Mapping Codec koi8_t
"""
# http://ru.wikipedia.org/wiki/КОИ-8
# http://www.opensource.apple.com/source/libiconv/libiconv-4/libiconv/tests/KOI8-T.TXT

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
        name='koi8-t',
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
    '\t'  # 0x09 -> HORIZONTAL TABULAT
