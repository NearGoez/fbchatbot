import requests
from bs4 import BeautifulSoup as bs

session = requests.session()


cookies = {
    'ig_did': '168B8BC3-88D8-44B4-A125-52A7EA1B4939',
    'datr': '4t-BZ49grEe0WXG8EFbQwM7w',
    'wd': '360x882',
    'mid': 'Z4Hf4wAEAAHjIOng_-aOlT9L9cJn',
    'dpr': '1.0714285714285714',
    'ig_nrcb': '1',
    'ps_l': '1',
    'ps_n': '1',
    'ig_direct_region_hint': '"PRN\\0547880059102\\0541770427573:01f70227cc951a7eacd7acb59ce7d2d9b41b6eb743714ceecc4393a8d4535b7bc1010d24"',
    'csrftoken': 'TEimCZL4bE4C7BAheS1S3r1meZWFHi6b',
    'ds_user_id': '63763585480',
    'sessionid': '63763585480%3AXaIPQ71HPDuv5Q%3A7%3AAYeJwPSl_2RtDGztxhQzpbhNsFrVBZ3BNSASzU9fpQ',
    'rur': '"NHA\\05463763585480\\0541770472786:01f7653889926c6a572ebaf0f3c2cc3f0b4011ab3ee6c376835d8cd27cd18845170dda32"',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.instagram.com/direct/t/17850140373323486/',
    'Alt-Used': 'www.instagram.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'ig_did=168B8BC3-88D8-44B4-A125-52A7EA1B4939; datr=4t-BZ49grEe0WXG8EFbQwM7w; wd=360x882; mid=Z4Hf4wAEAAHjIOng_-aOlT9L9cJn; dpr=1.0714285714285714; ig_nrcb=1; ps_l=1; ps_n=1; ig_direct_region_hint="PRN\\0547880059102\\0541770427573:01f70227cc951a7eacd7acb59ce7d2d9b41b6eb743714ceecc4393a8d4535b7bc1010d24"; csrftoken=TEimCZL4bE4C7BAheS1S3r1meZWFHi6b; ds_user_id=63763585480; sessionid=63763585480%3AXaIPQ71HPDuv5Q%3A7%3AAYeJwPSl_2RtDGztxhQzpbhNsFrVBZ3BNSASzU9fpQ; rur="NHA\\05463763585480\\0541770472786:01f7653889926c6a572ebaf0f3c2cc3f0b4011ab3ee6c376835d8cd27cd18845170dda32"',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0, i',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = session.get('https://www.instagram.com/direct/inbox/', cookies=cookies, headers=headers)

soup = bs(response.text, 'html.parser')
print(soup.get_text())


