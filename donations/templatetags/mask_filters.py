from django import template


register = template.Library()

@register.filter
def mask_tc(value):
    """
    TC kimlik numarasını maskeler; tüm rakamları * yapar, yalnızca son 3 hanesini gösterir.
    Örnek: 12345678901 -> *********901
    """
    try:
        value = str(value)
        if len(value) > 3:
            return '*' * (len(value) - 3) + value[-3:]
        return value
    except Exception:
        return value

@register.filter
def mask_name(value):
    """
    İsim ve soyisim bilgisini maskeler. Her kelimenin ilk iki harfi gösterilir, geri kalanı maskelenir.
    Örnek: "Ahmet Yılmaz" -> "Ah**** Yı****"
    """
    try:
        words = value.split()
        masked_words = []
        for word in words:
            if len(word) > 2:
                masked = word[:2] + '*' * (len(word) - 2)
            else:
                masked = word
            masked_words.append(masked)
        return ' '.join(masked_words)
    except Exception:
        return value