class PlatformException(Exception):
    code = 500


class InvalidArgumentException(PlatformException):
    code = 403


class EmptyLotteryPool(PlatformException):
    code = 403
