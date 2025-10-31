from ..std import *

def millis2datetime(ms:int, format:str="%Y-%m-%d %H:%M:%S.{ms}", timezone:str="Europe/Madrid") -> str:
    """
    Converts a timestamp in milliseconds to a formatted date-time string.
    """
    try:
        tz = ZoneInfo(timezone)
    except Exception:
        raise ValueError(f"Invalid timezone")
    dt = datetime.datetime.fromtimestamp(ms/1000, tz=tz).replace(tzinfo=None)
    return dt.strftime(format.replace("{ms}", f"{dt.microsecond // 1000:03d}"))

if __name__ == "__main__":
    print(millis2datetime(1700000000123))   # 2023-11-14 23:13:20.123
    print(millis2datetime(1700000000123, "%Y-%m-%d"))   # 2023-11-14
    print(millis2datetime(1700000000123, timezone="America/Santiago"))  # 2023-11-14 19:13:20.123