from datetime import tzinfo, timedelta, datetime, timezone
class UTC0530(tzinfo):
    def __init__(self, offset=21600, name=None):
        self.offset = timedelta(seconds=offset)
        self.name = name or self.__class__.__name__
    def utcoffset(self, dt):
        return self.offset
    def tzname(self, dt):
        return self.name
    def dst(self, dt):
        return timedelta(0)
times= datetime.now(UTC0530())
times = times.strftime("%H:%M")


TOKEN ="5366249644:AAFyr5UH6BL1L7MtfJDSVSLVJ6p3NzKAELs"
api_keys = "468ae2bc7698a8d423312d275f613869"
