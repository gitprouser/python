from Crypto.Cipher import AES
from Crypto import Random
import sys
import base64
import getopt

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]


class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

def usage():
    print " python urlshortner.py 'URL' "
    print "   -e     Encrypt URL"
    print "   -d     Decrypt URL"


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "e:d:h", ["encrypt=", "decrypt=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    encrypt_url = None
    decrypt_url = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-e", "--encrypt"):
            print "I am encrypting" 
            encrypt_url = a
        elif o in ("-d", "--decrypt"):
            print "I am in decrypt" 
            decrypt_url = a
        else:
            assert False, "unhandled option"


    aes = AESCipher("6wVqvzotCxFsjg==6wVqvzotCxFsjg==") 
    if encrypt_url:
        print "encrypt:'%s'" % aes.encrypt(encrypt_url)
    elif decrypt_url:
        print "decrypt:'%s'" % aes.decrypt(decrypt_url)
    else:
        usage()
        sys.exit(2)

if __name__ == '__main__': 
            main()
