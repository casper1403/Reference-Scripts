
import pycountry

def country_codes(country):
    """ Function that tales country name as input and outputs the ISO country code """
    countryObject = None
    try:
        countryObject = pycountry.countries.search_fuzzy(country)
        return countryObject[0].alpha_2
    except LookupError:
        pass
    try:
        splittedCountry = country.split(',')[0]
        countryObject = pycountry.countries.search_fuzzy(splittedCountry)
        return countryObject[0].alpha_2
    except LookupError:
        return 'No Code'
