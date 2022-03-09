"""
Module description
"""
def to_roman(num):
    """
    method description - converts numbers to a roman numeral equivalent
    """
    arabic_to_roman = {
      'M': 1000,
      'CM': 900,
      'D': 500,
      'CD': 400,
      'C': 100,
      'XC': 90,
      'L': 50,
      'XL': 40,
      'X': 10,
      'IX': 9,
      'V': 5,
      'IV': 4,
      'I': 1
    }
    answer = ''
    for item in arabic_to_roman.items():
        arabic = item[1]
        if num >= arabic:
            counter = 0
            times = num // arabic
            while counter < times:
                counter += 1
                answer += item[0]
                num -= arabic
    return answer

print(to_roman(999))
