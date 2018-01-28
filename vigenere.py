import string

class vigenere_cipher:
    inputFile = "";
    cipherKeyFile = "";
    saveFile = "";
    plainText = "";
    encryptedText = "";
    cipherKey = "";
    alphabetType = "";

    def __init__(self, encrypt, inputFile, saveFile, cipherKeyFile, alphabetType):
        self.inputFile = inputFile;
        self.cipherKeyFile = cipherKeyFile;
        self.alphabetType = alphabetType;

        try:
            self.inputFile = open(inputFile, 'r');
            if encrypt is True:
                self.plainText = self.inputFile.read();
            else:
                self.encryptedText = self.inputFile.read();
        except:
            print("[VIGENERE] -> Error.. trying to open file: {0}".format(inputFile));

        try:
            self.cipherKeyFile = open(cipherKeyFile, 'r');
            self.cipherKey = self.cipherKeyFile.read();
        except:
            print("[VIGENERE] -> Error.. trying to open file: {0}".format(cipherKeyFile));
        
        try:
            self.saveFile = open(saveFile, 'w');
        except:
            print("[VIGENERE] -> Error.. trying to open file: {0}".format(saveFile));
        
        print("\n************** OUTPUT *****************")
        if encrypt is True:
            print("[VIGENERE] -> Plain Text: {0}".format(self.plainText));
        else:
            print("[VIGENERE] -> Encrypted Text: {0}".format(self.encryptedText));
        print("[VIGENERE] -> Key: {0}".format(self.cipherKey));
        print("[VIGENERE] -> Alphabet Type: {0}".format(self.alphabetType));
        print("[VIGENERE] -> Saving output to: {0}".format(saveFile));
    
    def cipher(self, PLAIN, ALPHABET, KEY, MOD):
        encryptedText = "";
        k=-1; # Cipher key iterable
        for p in PLAIN:
            if(k==len(KEY)-1):
                k=-1;
            k=k+1;
            try:
                print("[VIGENERE] -> Plain val: {0}".format(ALPHABET.index(p.upper())));
                print("[VIGENERE] -> Key val: {0}".format(ALPHABET.index(KEY[k].upper())));
                if self.alphabetType.lower() == "s":
                    newVal = (ALPHABET.index(p.upper()) + ALPHABET.index(KEY[k].upper())) % MOD;
                else:
                    newVal = (ALPHABET.index(p) + ALPHABET.index(KEY[k])) % MOD;
                encryptedText = encryptedText + ALPHABET[newVal];
                print(ALPHABET[newVal]);
            except:
                continue;
        self.saveFile.write(encryptedText);
        self.saveFile.close();
        return encryptedText;

    def decipher(self, ENCRYPTED, ALPHABET, KEY, MOD):
        plainText = "";
        k=-1; # Cipher key iterable
        for p in ENCRYPTED:
            if(k==len(KEY)-1):
                k=-1;
            k=k+1;
            try:
                print("[VIGENERE] -> Encrypted val: {0}".format(ALPHABET.index(p.upper())));
                print("[VIGENERE] -> Key val: {0}".format(ALPHABET.index(KEY[k].upper())));
                if self.alphabetType.lower() == "s":
                    newVal = (ALPHABET.index(p.upper()) - ALPHABET.index(KEY[k].upper())) % MOD;
                else:
                    newVal = (ALPHABET.index(p) - ALPHABET.index(KEY[k])) % MOD;
                plainText = plainText + ALPHABET[newVal];
                print(ALPHABET[newVal]);
            except:
                continue;
        self.saveFile.write(plainText);
        self.saveFile.close();
        return plainText;

    def encrypt(self):
        ALPHABET = [];
        MOD = 0;
        PLAIN = [];
        PLAIN = list(self.plainText);
        KEY = list(self.cipherKey);
        print("[VIGENERE] -> Plain text list: {0}".format(PLAIN));
        print("[VIGENERE] -> Cipher Key list: {0}".format(KEY));
        if(self.alphabetType.lower() == "s"):
            ALPHABET = list(string.ascii_uppercase);
            MOD = len(ALPHABET);
            print("[VIGENERE] -> Aphabet S: {0}".format(ALPHABET));
            print("[VIGENERE] -> Using MOD: {0}".format(MOD));
            return self.cipher(PLAIN, ALPHABET, KEY, MOD);
        elif(self.alphabetType.lower() == "l"):
            ALPHABET = list(string.ascii_uppercase+string.ascii_lowercase);
            MOD = len(ALPHABET);
            print("[VIGENERE] -> Aphabet L: {0}".format(ALPHABET));
            print("[VIGENERE] -> Using MOD: {0}".format(MOD));
            return self.cipher(PLAIN, ALPHABET, KEY, MOD);
        else:
            print("[VIGENERE] -> Error.. expected alphabet type of S or L!");

    def decrypt(self):
        ALPHABET = [];
        MOD = 0;
        ENCRYPTED = [];
        ENCRYPTED = list(self.encryptedText);
        KEY = list(self.cipherKey);
        print("[VIGENERE] -> Encrypted text list: {0}".format(ENCRYPTED));
        print("[VIGENERE] -> Cipher Key list: {0}".format(KEY));
        if(self.alphabetType.lower() == "s"):
            ALPHABET = list(string.ascii_uppercase);
            MOD = len(ALPHABET);
            print("[VIGENERE] -> Aphabet S: {0}".format(ALPHABET));
            print("[VIGENERE] -> Using MOD: {0}".format(MOD));
            return self.decipher(ENCRYPTED, ALPHABET, KEY, MOD);
        elif(self.alphabetType.lower() == "l"):
            ALPHABET = list(string.ascii_uppercase+string.ascii_lowercase);
            MOD = len(ALPHABET);
            print("[VIGENERE] -> Aphabet L: {0}".format(ALPHABET));
            print("[VIGENERE] -> Using MOD: {0}".format(MOD));
            return self.decipher(ENCRYPTED, ALPHABET, KEY, MOD);
        else:
            print("[VIGENERE] -> Error.. expected alphabet type of S or L!");


def main():
    userInput = raw_input("[VIGENERE] -> Encrypt or Decrypt (E or D)? ");
    if userInput.lower() == "e":
        print("[VIGENERE] -> You are encrypting text...");
        pt = raw_input("[VIGENERE] -> Enter plain text file name (ex: msg.txt): ");
        ck = raw_input("[VIGENERE] -> Enter cipher key file name (ex: ct.txt): ");
        sf = raw_input("[VIGENERE] -> Where do you want to save your encrypted text (ex: out.txt)? ");
        at = raw_input("[VIGENERE] -> Enter alphabet type (S or L): ");
        vig = vigenere_cipher(True, pt,sf,ck,at);
        print(vig.encrypt());
    else:
        print("[VIGENERE] -> You are decrypting text...");
        et = raw_input("[VIGENERE] -> Enter encrypted text file name (ex: out.txt): ");
        ck = raw_input("[VIGENERE] -> Enter cipher key file name (ex: ct.txt): ");
        sf = raw_input("[VIGENERE] -> Where do you want to save your encrypted text (ex: out2.txt)? ");
        at = raw_input("[VIGENERE] -> Enter alphabet type (S or L): ");
        vig = vigenere_cipher(False, et,sf,ck,at);
        print(vig.decrypt());

if __name__ == "__main__":
    main();