from requests import get,post
import re
from threading import Thread
import random as ran
import os

class api:

  email=None
  dhead={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
  def facebook(email):
    head={"Host":"m.facebook.com","Connection":"keep-alive","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}
    try:
      resposta1=get(url="https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2F&multiple_results=0&ars=facebook_login&lwv=100&_rdr",headers=head)
      values=re.findall(r"value=\"([\w_?-?]+)\"",resposta1.text)
      dt={"lsd":values[0],"jazoest":values[1],"email":email,"first_name":"","last_name":"","did_submit":values[2]}
      head={"Host":"m.facebook.com","Connection":"keep-alive","Content-Length":"89","Cache-Control":"max-age=0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Origin":"https://m.facebook.com","User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Content-Type":"application/x-www-form-urlencoded","Referer":"https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2F&multiple_results=0&ars=facebook_login&lwv=100&_rdr","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}
      resposta2=post(url="https://m.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login",data=dt,headers=head)
    except:
      print("FACEBOOK (Fail)")
      return False

    if "https://m.facebook.com/login/identify/?ctx=recover&search_attempts" in resposta2.url:
      print(str(email)+" FACEBOOK (False)")
    else:
      print(str(email)+" FACEBOOK (True)")

  def instagram(email):
    try:
      head={"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
      resposta1 = get(url="https://www.instagram.com/accounts/password/reset/",headers=head)
      cook=resposta1.cookies.get_dict()
      ex=re.findall(r"rollout_hash\"\:\"([\w_?-?]+)\"",resposta1.text)
      dt1={"email_or_username":email,"recaptcha_challenge_field":""}
      head={"Host":"www.instagram.com","Connection":"keep-alive","Content-Length":"61","Origin":"https://www.instagram.com","X-IG-WWW-Claim":"0","CSP":"active","X-Instagram-AJAX":ex[0],"Content-Type":"application/x-www-form-urlencoded","Accept":"*/*","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","X-CSRFToken":cook["csrftoken"],"Referer":"https://www.instagram.com/accounts/password/reset/","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}

      resposta2=post(url="https://www.instagram.com/accounts/account_recovery_send_ajax/",headers=head,data=dt1,cookies=cook)
    except:
      print("INSTAGRAM (Fail")
      return False

    if "No users found" in resposta2.text:
      print(str(email)+" INSTAGRAM (False)")
    else:
      print(str(email)+" INSTAGRAM (True)")


  def twitter(email):
    go = True
    if go == True:
      try:
        dhead={"User-Agent":"Mozilla/5.0 (Linux; U; Android 6.0; en-us; Nexus 30 Build/JOJeG) AppleWebKit/587.20 (KHTML, like Gecko) Version/3.0 Mobile Safari/5894.10"}
        resposta1 = get(url="https://twitter.com/account/begin_password_reset",headers=dhead)
        values=re.findall(r"value=\"([\w_?-?]+)\"",resposta1.text)
        head={"Host":"twitter.com","Connection":"keep-alive","Content-Length":"95","Cache-Control":"max-age=0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Origin":"https://twitter.com","User-Agent":"Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Content-Type":"application/x-www-form-urlencoded","Referer":"https://twitter.com/account/begin_password_reset","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}
        dt={"authenticity_token":values[0],"account_identifier":email}
        cook=resposta1.cookies.get_dict()
        resposta2 = post(url="https://twitter.com/account/begin_password_reset",headers=head,data=dt,cookies=cook)
        html = resposta2.text
      except:
        print("TWITTER (Fail)")
        return False

      if "Email a link to" in html:
        print(str(email)+" TWITTER (True)")
      elif "We found more than one account with that information" in html:
        print(str(email)+" TWITTER (True)")
      elif "later" in html:
        print(email+" TWITTER (try later) --> Use VPN")
      else:
        print(str(email)+" TWITTER (False)")


  def github(email):
    try:
      dhead={"User-Agent":"Mozilla/5.0 (Linux; U; Android 6.0; en-us; Nexus 30 Build/JOJeG) AppleWebKit/587.20 (KHTML, like Gecko) Version/3.0 Mobile Safari/5894.10"}
      resposta1 = get(url="https://github.com/password_reset",headers=dhead)
      values=re.findall(r"value=\"([\w\_?\-?\&?\#?\;?\+?\=?\/?\ ?]+)\"",resposta1.text)
      head = {"Host":"github.com","Connection":"keep-alive","Content-Length":"188","Cache-Control":"max-age=0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Origin":"https://github.com","User-Agent":"User-Agent: Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 11 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Content-Type":"application/x-www-form-urlencoded","Referer":"https://github.com/password_reset","Accept-Encoding":"gzip, deflate","Accept-Language":"pt-BR,en-US;q=0.8"}
      cook = resposta1.cookies.get_dict()
      dt = {"utf8":".","authenticity_token":values[2],"email":email,"commit":values[3]}
      resposta2 = post(url="https://github.com/password_reset",headers=head,cookies=cook,data=dt)
    except:
      print("GITHUB (Fail)")
      return False

    if not "Password sent!" in resposta2.text:
      print(str(email)+" GITHUB (False)")
    else:
      print(str(email)+" GITHUB (True)")


  def steam(email):
    try:
      agent="IR4ndOn"+str(ran.randint(1,9999))
      dhead={"User-Agent":"{}".format(agent)}
      resposta1 = get(url="https://help.steampowered.com/pt-br/wizard/HelpWithLoginInfo?issueid=404",headers=dhead)
      cook = resposta1.cookies.get_dict()
      sid=cook["sessionid"]
      head = {"Host":"help.steampowered.com","Connection":"keep-alive","Accept":"*/*","X-Requested-With":"XMLHttpRequest","CSP":"active","User-Agent":"{}".format(agent),"Referer":"https://help.steampowered.com/pt-br/wizard/HelpWithLoginInfo?issueid=406","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US"}
      gtmail=email.replace("@","%40")
      resposta2 = get(url="https://help.steampowered.com/en/wizard/AjaxLoginInfoSearch?reset=0&lost=0&issueid=404&searches=1&search={}&sessionid={}&wizard_ajax=1".format(gtmail,sid),headers=head,cookies=cook)
    except:
      print("STEAM (Fail)")
      return False

    if "wizard" in resposta2.text:
      if not "Please try again later" in resposta2.text:
        print(email+" STEAM (True)")
        return False
    if "we were unable to find" in resposta2.text:
      print(email+" STEAM (False)")
      return False
    if "Please try again later" in resposta2.text:
      print(email+" STEAM (try later) --> Use VPN")
      return False


  #AQUI É ONDE VOCE ESCOLHE EM QUAIS SITES A API VAI VERIFICAR A EXISTENCIA
  #DE CONTAS DE UM CERTO EMAIL

  def main(email):
    th1 = Thread(target = api.facebook(email))
    th2 = Thread(target = api.instagram(email))
    th3 = Thread(target = api.twitter(email))
    th4 = Thread(target = api.github(email))
    th5 = Thread(target = api.steam(email))
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
