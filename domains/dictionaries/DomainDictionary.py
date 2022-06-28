import re

patterns = {
    re.compile('.*(.{2}座|星座|幸運|健康|桃花|財運|速配|工作|運勢|人緣).*'): ['intents.IntentZodiacSigns', 'dispatch'],
}
