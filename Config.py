import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "7706053"))
    API_HASH = os.environ.get("API_HASH", "a87b492b8fe379c5fd63793d29ca7a27")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6568673101:AAG9leUDdoKfvj0p-uGin1Lpwesqn-pyBS0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AgHCSf0AWT7IHpddVoB6TZhkhqBzHG4Y9dpuSXwmc2wSeu3H0m8YGZzQUGuO6P7Cp1IuakqAD-TTeD4oi1sOdCXi5mQbgFI2NH2R4TcpvMR09CIc-CNuBiQx3XbTnPHOfYxpT9uj0_DjCd8RzRc2gSfL0aLvZtGCZl8V-TvE3Fjgfyf7DAeAardYfp02oIIilMjQ9K0nSj_DZ95G52aXPTEL9kz9UyEIQ_APAADVfQfLR520DrOL7jypIp6KF_ozXR5AgbWeAS2L4rgj04nW21m2cSSoq6hKWsu7vxeoQdumN-xDu1n_V45oXl3Pd3foQW967fzYBEudVBCmeRMB2G95ZTwwAAAAFGxBevAA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "PlayINCallsBot")
    SUPPORT = os.environ.get("SUPPORT", "TeamRecode")
    CHANNEL = os.environ.get("CHANNEL", "TeamRrcode")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
