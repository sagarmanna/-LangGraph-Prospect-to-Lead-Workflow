"""
Light HTTP helpers (wrap requests).
"""

import requests
from requests.adapters import HTTPAdapter, Retry

_session = None

def get_session():
    global _session
    if _session is None:
        s = requests.Session()
        retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
        s.mount("https://", HTTPAdapter(max_retries=retries))
        _session = s
    return _session

def get_json(url, headers=None, params=None):
    resp = get_session().get(url, headers=headers, params=params, timeout=15)
    return resp.json() if resp.ok else {}

def post_json(url, payload=None, headers=None):
    resp = get_session().post(url, json=payload, headers=headers, timeout=20)
    return resp.json() if resp.ok else {}

