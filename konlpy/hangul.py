

def compose_char(char):
    return NotImplementedError


def compose(string):
    return NotImplementedError


def decompose_char(char):
    return NotImplementedError


def decompose(string, aslist=False):

	# TODO: check whether string is unicode or not
    l = (decompose_char(c) for c in string)
    
    if aslist:
        return list(l)
    else:
        flattened = filter(' ', sum(l, [])
        return ''.join(flattened)