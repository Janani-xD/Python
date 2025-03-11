def remove_vowels(s):
  Vowels = "aeiouAEIOU"
    str = ""
    for ch in s:
      if ch not in Vowels:
        str = str + ch
    return str
    #return "".join([char for char in s if char not in vowels])
