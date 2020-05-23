#Diana Balderas
#5/17/20
#Zodiac Sign Calculator
#Instructions: Enter you birth month in lowercase letters.

month = input('What month were you born?  ')
month.lower()
day = int(input('What day were you born?  '))
months = [
    'january',
    'feburary',
    'march',
    'april',
    'june',
    'july',
    'august',
    'september',
    'november',
    'december',
    ]

if month in months:
    if month == 'december':
        astro_sign = ('sagittarius' if day < 22 else 'capricorn')
    elif month == 'january':
        astro_sign = ('capricorn' if day < 20 else 'aquarius')
    elif month == 'february':
        astro_sign = ('aquarius' if day < 19 else 'pisces')
    elif month == 'march':
        astro_sign = ('pisces' if day < 21 else 'aries')
    elif month == 'april':
        astro_sign = ('aries' if day < 20 else 'taurus')
    elif month == 'may':
        astro_sign = ('taurus' if day < 21 else 'gemini')
    elif month == 'june':
        astro_sign = ('gemini' if day < 21 else 'cancer')
    elif month == 'july':
        astro_sign = ('cancer' if day < 23 else 'leo')
    elif month == 'august':
        astro_sign = ('leo' if day < 23 else 'virgo')
    elif month == 'september':
        astro_sign = ('virgo' if day < 23 else 'libra')
    elif month == 'october':
        astro_sign = ('libra' if day < 23 else 'scorpio')
    elif month == 'november':
        astro_sign = ('scorpio' if day < 22 else 'sagittarius')

    print ('Your zodiac sign is '+ astro_sign + ' !')

