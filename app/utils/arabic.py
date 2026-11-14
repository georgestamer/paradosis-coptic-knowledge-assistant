import re
DIACRITICS = re.compile(r'[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed]')
def normalize_arabic(value: str) -> str:
    value = DIACRITICS.sub('', value).replace('ـ','')
    value = value.translate(str.maketrans({'أ':'ا','إ':'ا','آ':'ا','ٱ':'ا','ى':'ي','ة':'ه'}))
    value = re.sub(r'[،؛؟!,.?:;()\[\]{}"\']', ' ', value)
    return re.sub(r'\s+', ' ', value).strip().casefold()
