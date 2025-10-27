from ..std import *

def http_request(base_url:str, path:str, method:str, params:dict=None, headers:dict=None) -> requests.Response:
    """ Sends an HTTP request with the specified method to a given URL, including optional parameters and headers.

    >>> response = http_request("https://api.example.com", "/users", "GET", params={"id": 123})
    >>> response.status_code
    200
    """
    query = urllib.parse.urlencode(params) if params else ''
    url = f"{base_url}{path}"
    if method.upper() in ['POST', 'PUT', 'PATCH']:  # If the method requires data
        res = requests.request(method, url, headers=headers, data=params)
    else:
        url += f'?{query}' if query else ''
        res = requests.request(method, url, headers=headers)

    return res

if __name__ == "__main__":
    response = http_request("https://postman-echo.com", "/get", "GET", params={"foo1": "bar1", "foo2": "bar2"})
    print(response.json())

    response = http_request("https://reqres.in", "/api/users", "POST", params={"name": "John", "job": "developer"})
    print(response.json())