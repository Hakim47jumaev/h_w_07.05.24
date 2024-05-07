def format_date(datem):
    from datetime import datetime
    datem=datetime.strptime(datem,"%m/%d/%Y")
    datem=datetime.strftime(datem,"%Y%d%m")
    return datem
date=input()
print(format_date(date))