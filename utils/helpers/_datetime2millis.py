from ..std import *

def datetime2millis(dt:str, timezone="Europe/Madrid") -> int:
    """ Converts a datetime string in various formats to milliseconds since the Unix epoch, considering the specified timezone.

    >>> datetime2millis("2024-12-01") # 1733007600000
    >>> datetime2millis("2024/12/01") # 1733007600000
    >>> datetime2millis("2024/12/01", "America/Santiago") # 1733022000000
    """
    tz = ZoneInfo(timezone)
    formats = [
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%Y%m%d%H%M%S%f",
        "%Y%m%d%H%M%S",
        "%Y%m%d%H%M",
        "%Y%m%d"
    ]
    
    for fmt in formats:
        try:
            _dt = datetime.datetime.strptime(dt, fmt)
            _dt = _dt.replace(tzinfo=tz)
            return int(_dt.timestamp() * 1000)
        except ValueError:
            continue
    
    raise ValueError(f"Invalid format: {dt}")

if __name__ == "__main__":
    print(datetime2millis("2024-12-01"))
    print(datetime2millis("2024/12/01"))
    print(datetime2millis("2024/12/01", "America/Santiago"))