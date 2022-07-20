def to_str_base(n, base):
   convert_string = "0123456789ABCDEF"
   if n < base:
      return convert_string[n]
   else:
      return to_str_base(n//base, base) + convert_string[n%base]

print(to_str_base(1453,16))
print(to_str_base(10,2))
