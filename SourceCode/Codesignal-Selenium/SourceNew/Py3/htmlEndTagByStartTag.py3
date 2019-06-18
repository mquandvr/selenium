def htmlEndTagByStartTag(s):
    return "</" + s.split()[0][1:] + ">" if s.split()[0][-1] != ">" else "</" + s.split()[0][1:]
    