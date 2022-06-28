from expiringdict import ExpiringDict

cache = ExpiringDict(max_len=100, max_age_seconds=3000)
