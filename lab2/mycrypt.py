import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    #max value
    s = s.ljust(1000,"x")
    for c in s:
        #invalid characters (not UTF-8)
        if c in ["ä", "ö", "å"]:
            raise ValueError
        if c.isalpha():
            if c.islower():
                c=c.upper()
            #if not lower case then upper case
            else:
                c.lower()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        #if not letter and not in digitmapping then it is wrong
        else:
            raise ValueError
    #return the original length
    return crypted[:origlen]

def decode(s):
    return encode(s).lower()

