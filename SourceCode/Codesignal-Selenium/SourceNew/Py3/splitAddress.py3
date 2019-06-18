def splitAddress(address):
    protocol = address[0:address.index(":")]
    domain = address[address.index(":")+3:address.index(".com")]
    context = address[address.index(".com")+5:len(address)]
    if len(context)>0:
        return [protocol,domain,context]
    return [protocol, domain]