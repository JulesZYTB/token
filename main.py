import requests, time, colorama, threading, user_agent, random, string, json, base64, discord_build_info_py, re
import os

import capmonster_python
import httpx
import art, gratient, PyMailGw

CAPTCHA_KEY = '57c30fcf1f36c94041d1eaf9f891c973'
CAPTCHA_KEY

class Settings():
      __DATA__ = {
               'CAPTCHA_KEY'    : CAPTCHA_KEY or os.environ['CAPTCHA_KEY'] or '',
               'THREADS'        :  1, 'SITE_KEY'     : '4c672d35-0701-42b2-88c3-78380b0db560', 'SITE_URL': 'https://discord.com/register',
               'PROXY_PATH'     : 'bongo/proxies.txt',
               'AUTHENTICATION' :  {
                                  'SITE_KEY' : 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34',
                                  'SITE_URL' : 'https://discord.com/verify'
               }, 'BASIC'       : {
                                'SITE_URL'   : 'https://discord.com',
                                'SITE_KEY'   : 'a9b5fb07-92ff-493f-86fe-352a2803b3df',
               }
      }

class Captcha():
      def __init__(self, site_key, site_url):
          if True:
             self.site_key, self.site_url = site_key, site_url
             self
        
          self.solver   = capmonster_python.HCaptchaTask(Settings.__DATA__['CAPTCHA_KEY'])
          self

      def create_task(self):
          if True:
             return self.solver.create_task(
                         self.site_url,
                         self.site_key,
             )

      def solve_task(
          self,
          task_id,
      ):
          if True:
             return self.solver.join_task_result(
                         task_id
             )

class Listener():
      def __init__(self) -> None:
          self.mail = PyMailGw.MailGwApi()
          self

      def get_mail(self):
          return self.mail.get_mail()

      def get_messages(self):
          return self.mail.fetch_inbox()

      def search_for_discord(self):
          for mail in self.mail.fetch_inbox():
              if mail["from"]["address"] == 'noreply@discord.com':
                 return re.findall(r'(https?://\S+)', self.mail.get_message_content(mail['id']))[0]
                 

class Discord():
      def __init__(self) -> None:
          self.api = 'https://discord.com/api/v9'
          self

      def get_super_properties(
          self,
          user_agent_string
      ):
          return base64.b64encode(
                        json.dumps(
                             {
                                 'os'                 : user_agent_string['appCodeName'],
                                 'browser'            : user_agent_string['platform'],
                                 'device'             : "",
                                 'system_locale'      : "en-US",
                                 'browser_user_agent' : "%s" % (user_agent_string['userAgent']),
                                 'browser_version'    : "%s" % (user_agent_string['appVersion'].split(" ")[0]),
                                 'os_version'         : "%s" % (user_agent_string['userAgent'].split("/")[1].split(" ")[0]),
                                 'referrer'           : "",
                                 'referring_domain'   : "",
                                 'referrer_current'   : "",
                                 'referring_domain_current'  : "",
                                 'release_channel'           : "stable",
                                 'client_build_number'       : discord_build_info_py.getClientData('stable')[0],
                                 'client_event_source'       : None
                             }, separators = (',', ':')
                        ).encode()
          ).decode()

      
          
      def create_token(self, invite_code: str = None, email: str = "", username: str = 'BoOm-BoOsT', DISCORD_WEBHOOK_URL = ''):
          if True:
             if True:
                if True:
                   USER_AGENT = user_agent.generate_navigator_js()
                   USER_AGENT

             if True:
                captcha = Captcha(site_key = Settings.__DATA__['SITE_KEY'], site_url = Settings.__DATA__['SITE_URL'])
                captcha

             task_id            = captcha.create_task()
             result             = captcha.solve_task(task_id = task_id)['gRecaptchaResponse']
             proxy              = self.get_proxy()

             while True:
                   try:
                      fingerprint        = self.get_fingerprint(proxy)
                      print('[>] Fingerprint Received: %s' % fingerprint)
                      break
                   except Exception as E:
                      if True:
                         if True:
                            print(E)
                            print
                           
                         time.sleep(10)
                         time
                        
             super_properties   = self.get_super_properties(user_agent_string = USER_AGENT)
             cookies            = self.get_cookies()

             if True:
                sep    = cookies.split(";")
                sx     = sep[0]
                sx2    = sx.split("=")
                dfc    = sx2[1]
                split  = sep[6]
                split2 = split.split(",")
                split3 = split2[1]
                split4 = split3.split("=")
                sdc    = split4[1]
             

          response = requests.post(
                     f'{self.api}/auth/register',
                        headers = {
                               'User-Agent'            : f'%s' % (USER_AGENT),
                               'Origin'                : f'https://discord.com',
                               'Referer'               : f'https://discord.com/invite/%s' % (invite_code),
                               'Content-Type'          : f'application/json',
                               'Sec-Fetch-Dest'        : f'empty',
                               'Sec-Fetch-Mode'        : f'cors',
                               'Sec-Fetch-Site'        : f'same-origin', 
                               'X-Fingerprint'         : f'%s' % (fingerprint),
                               'X-Discord-Locale'      : f'en-US',
                               'TE'                    : f'trailers',
                               'X-Debug-Options'       : f'bugReporterEnabled',
                               'Host'                  : f'discord.com',
                               'DNT'                   : f'1',
                               'Content-Length'        : f'161',
                               'Accept'                : f'*/*',
                               'Accept-Encoding'       : f'gzip, deflate, br',
                               'Accept-Language'       : f'en-US,en;q=0.5',
                               'Connection'            : f'keep-alive',
                               'X-Super-Properties'    : f'%s' % (super_properties),
                               'Cookie'                : f'__dcfduid={dfc}; __sdcfduid={sdc}; _gcl_au=1.1.33345081.1647643031; _ga=GA1.2.291092015.1647643031; _gid=GA1.2.222777380.1647643031; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+18+2022+18%3A53%3A43+GMT-0400+(%E5%8C%97%E7%BE%8E%E4%B8%9C%E9%83%A8%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=.fksdoBlzBs1zuhiY0rYFqFhDkstwwQJultZ756_yrw-1647645226-0-AaluVZQHZhOL5X4GXWxqEIC5Rp3/gkhKORy7WXjZpp5N/a4ovPxRX6KUxD/zpjZ/YFHBokF82hLwBtxtwetYhp/TSrGowLS7sC4nnLNy2WWMpZSA7Fv1tMISsR6qBZdPvg==; locale=en-US',
                               'Authorization'.lower() : f'undefined'
                       }, json = {
                               'Fingerprint'.lower()      : '%s' % (fingerprint),
                               'Captcha_Key'.lower()      : '%s' % (result),
                               'Consent'.lower()          :  True,
                               'Gift_Code_Sku_Id'.lower() :  "",
                               'Username'.lower()         : '%s | %s' % (username, ''.join(random.choice(string.ascii_letters) for x in range(3))) if username != '' else username,
                               'Invite'.lower()           : '%s' % (invite_code),
                               'Date_Of_Birth'.lower()    : "1991-04-06",
                               'Password'.lower()         : "BoOm-BoOsT!",
                               'Email'.lower()            : f"{''.join(random.choice(string.ascii_letters) for x in range(12))}" + random.choice(['@gmail.com', '@outlook.com', '@replit.com']) if email == "" else email
                       }, proxies = {
                                  'http'     : 'http://%s' % (
                                                proxy
                                   ), 'https': 'http://%s' % (proxy)
                       }
          ).json()

          try:
             print('[>] Token Generated: %s' % (response['token']))
             print

             if DISCORD_WEBHOOK_URL != '':
                requests.post(
                         DISCORD_WEBHOOK_URL,
                         json = {
                              'embeds': [
                                      {
                                          'title'       : 'Token Generated',
                                          'description' : '```\n%s```' % (response['token'])
                                      }
                              ]
                         }
                )
          except:
             pass
            
          try:
             if True:
                with open('bongo/tokens.txt', 'a+') as tokens:
                     tokens.write('%s\n' % (response['token']))
                     tokens

                return response['token']
          
          Discord().create_token(invite_code = 'mhn5XW3SEg', username = 'BoOm-BoOsT | %s' % ''.join(random.choice(string.ascii_letters) for x in range(3)), DISCORD_WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1011695195957506128/1AlySVlFfom62TdOkFrRKusR0iSJ-SKeE-0IV98BFLeZTQvZmL-Uoq9Zn-30sBHBw9Ev', email = '')
          Discord()

      def start_email(
          self,
          invite_code,
          webhook,
          email,
          listener
      ):
          
                     
              print(gratient.red(art.text2art("BoOm-BoOsT")))
           
            