from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

beaker_opts = {
    "cache.type": "ext:redis",
    "cache.url": "redis://127.0.0.1:6379",
    "cache.expire": 1
}
beaker_cache = CacheManager(**parse_cache_config_options(beaker_opts))
