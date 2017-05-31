import  re
print re.findall(r'[^a-zA-Z0-9\d\s!@*-=+\[\]|:\";\'<>,./]', 'john & joan ^ were {walking  }  t#rough the w % od$ t_day', re.I|re.M)
