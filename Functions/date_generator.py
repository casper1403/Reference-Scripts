
""""Script that generates dates between two different values in the YYYY-MM-DD Format"""

def DateGenerator(date1,date2):
    """Input is a date like 01-01-2018, output is an iterable object."""
    import datetime
    start = datetime.datetime.strptime(date1, '%d-%m-%Y')
    end = datetime.datetime.strptime(date2, '%d-%m-%Y')
    step = datetime.timedelta(days=1)
    while start <= end:
        yield start.date()
        start += step
