from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *  
from time import sleep
import random
import user_agent
import urllib.parse
import requests


def App():
    put_html('<header><title>ramadan</title><header>')
    put_html('<body background="black"></body>')
    
    fx='''                           
                            R A M A D A N

INSTAGRAM | FX_PY3   &   TELEGRAM | FX_PY
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
[1] - Post Coments Haanat
[2] - Likes For Quran Post
'''
    
    put_text(fx)
    
    
    data=input_group(
        'login',
        [
            input('username & اسم المستخدم',name='user'), 
            input('password & باسورد حسابك',name='pass'),
            input('seconds & عدد الثواني - لتجنب الحظر',name='s'),
            input('choose & [ 1 or 2 ] اختيارك',name='choose'),
            
        ]
    )

    username=data['user']
    password=data['pass']
    s=data['s']
    s=int(s)
    choose=data['choose']
        
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
         'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '275',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=V2pBI84DFh1JRIyxf4TwQKjtUDMey3GI; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent':user_agent.generate_user_agent(),
        'x-csrftoken': 'V2pBI84DFh1JRIyxf4TwQKjtUDMey3GI',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': 'bc3d5af829ea',
        'x-requested-with': 'XMLHttpRequest'
      }
    data = {
             'username': f'{username}',
             'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
             'queryParams': '{}',
             'optIntoOneTap': 'false'
        } 
    rs=requests.session() 
    r = rs.post(url, headers=headers, data=data)
    

    
    
    if  'authenticated":true' in r.text or 'userId' in r.text:
        csrftoken=r.cookies['csrftoken']
        si=r.cookies['sessionid']
        id=r.cookies['ds_user_id']
    	
    	
    else:
        put_text('[-] bad login ')
        exit()
    put_text('\n[+] Done login ')
    tags='استغفرالله','Quran','قران','القران'
    if choose == '1':
      j=s
      good=0
      bad=0
      error=0
      text=[
  	  'فَقُلْتُ اسْتَغْفِرُوا رَبَّكُمْ إِنَّهُ كَانَ غَفَّارًا',
  	'واستغفر لذنبك وسبح بحمد ربك بالعشي والإبكار' ,
  	'واستغفروا الله إن الله كان غفورا رحيما',
  	'وما كان الله ليعذبهم وأنت فيهم وما كان الله معذبهم وهم يستغفرون',
  	'والذين إذا فعلوا فاحشة أو ظلموا أنفسهم ذكروا الله فاستغفروا لذنوبهم ، ومن يغفر الذنوب إلا الله ؟',
  	'ومن يعمل سوءا أو يظلم نفسه ثم يستغفر الله يجد الله غفورا رحيما',
  	'هل من مستغفر ؟؟',
  	]
      put_text(f'''
- - - - - - - - - - - - - - - - - 
Done >>> {good} 
bad >>> {bad}  
Block >>> {error} 
link >>> link
seconse >>> 0
text >>> text
- - - - - - - - - - - - - - - - -''')
      k=0
      
      while True:
          k+=1
          if k == 11:
              k=0
          data={
  			'is_prefetch': 'false',
  			'omit_cover_media': 'false',
  			'module': 'explore_popular',
  			'use_sectional_payload': 'true',
  			'include_fixed_destinations': 'true'
  		}
          url='https://i.instagram.com/api/v1/discover/web/explore_grid/?is_prefetch=false&omit_cover_media=false&module=explore_popular&use_sectional_payload=true&include_fixed_destinations=true'
          headers={
  			'accept': '*/*',
  		'accept-encoding': 'gzip, deflate, br',
  		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
  		'content-length': '16',
  		'content-type': 'application/x-www-form-urlencoded',
  		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
  		'origin': 'https://www.instagram.com',
  		'referer': 'https://www.instagram.com/',
  		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
  		'sec-ch-ua-mobile': '?0',
  		'sec-ch-ua-platform': '"Windows"',
  		'sec-fetch-dest': 'empty',
  		'sec-fetch-mode': 'cors',
  		'sec-fetch-site': 'same-site',
  		'user-agent': user_agent.generate_user_agent(),
  		'x-asbd-id': '198387',
  		'x-csrftoken': csrftoken,
  		'x-frame-options': 'SAMEORIGIN',
  		'x-ig-app-id': '936619743392459',
  		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
  		'x-instagram-ajax': '1006179778'
  		}
          rs=requests.session()
          req=rs.get(url,headers=headers,data=data).json()['sectional_items'][0]['layout_content']['fill_items']
          try:
              q=req[k]['media']['pk']
          except :
              k=1
              req=rs.get(url,headers=headers,data=data).json()['sectional_items'][0]['layout_content']['fill_items']
              q=req[k]['media']['pk']
          for i in req:
              text1=random.choice(text)
              link='https://www.instagram.com/reel/'+i['media']['code']
              comment=rs.post(f'https://i.instagram.com/api/v1/web/comments/{q}/add/',data={
  		'comment_text': text1
  		},headers={
  		'accept': '*/*',
  		'accept-encoding': 'gzip, deflate, br',
  		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
  		'content-length': '16',
  		'content-type': 'application/x-www-form-urlencoded',
  		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
  		'origin': 'https://www.instagram.com',
  		'referer': 'https://www.instagram.com/',
  		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
  		'sec-ch-ua-mobile': '?0',
  		'sec-ch-ua-platform': '"Windows"',
  		'sec-fetch-dest': 'empty',
  		'sec-fetch-mode': 'cors',
  		'sec-fetch-site': 'same-site',
  		'user-agent': user_agent.generate_user_agent(),
  		'x-asbd-id': '198387',
  		'x-csrftoken': csrftoken,
  		'x-frame-options': 'SAMEORIGIN',
  		'x-ig-app-id': '936619743392459',
  		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
  		'x-instagram-ajax': '1006179778'
  		}).json()
              try:
                  if comment["feedback_title"]=="Try Again Later":
                      error+=1
                      s=1000
              except :
                  pass
              try:
                  if comment['message']=='Unable to post comment.':
                      bad+=1
                      s=j
              except :
                  pass
              if comment["status"]=="ok":
                  good+=1
                  s=j
                  put_text(f'''
- - - - - - - - - - - - - - - - - 
Done >>> {good}
bad >>> {bad}  
Block >>> {error} 
link >>> {link}
seconse >>> {s} 
text >>> {text1}
- - - - - - - - - - - - - - - - - ''')
                  sleep(s)
                  
    elif choose == '2' :
           j=s
    good=0
    bad=0
    error=0
    tag=random.choice(tags)
    hashtag=urllib.parse.quote(tag)
    headers={
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cookie': f'mid=Y_vHUAAAAAEFMn5sZkBlXEny0gmc; ig_did=01CC1EB3-C79D-4055-B78A-4FECD92BE72F; ig_nrcb=1; datr=hPb7YwZLehq6PCmMlTaRiQaM; csrftoken={csrftoken}; ds_user_id={id}; shbid="6501\05444852157584\0541710688648:01f7c4a074e0477fb134a0c225df0097c27c12dc10aa5e49788f0fde6a110d666a292340"; shbts="1679152648\05444852157584\0541710688648:01f70dea94f67dce43840b6ae1753d50915ea8ca50c7cf86b85b7b18c7490de3359440f5"; sessionid={si}; dpr=1.5; rur="ASH\05444852157584\0541710935740:01f7f5cd2da38d50c940cb11b7c9cdaef2a0b3caa1b7ea541dd1e0822f63694bc922fc8c"',
    'referer': f'https://www.instagram.com/explore/tags/{hashtag}/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user_agent.generate_user_agent(),
    'viewport-width': '483',
    'x-asbd-id': '198387',
    'x-csrftoken': csrftoken,
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3seKB-R5006bc9z2916PlpRwbNImOpMdpxWLOkzAU1wapG',
    'x-requested-with': 'XMLHttpRequest'
      		}
    url=f'https://www.instagram.com/api/v1/tags/{hashtag}/sections/'
    resp=requests.post(url,headers=headers,data={
      'include_persistent': 0,
      'page': 2,
      'surface': 'grid',
      'tab': 'recent',
    }).json()['sections']
    
    for i in resp:
        med=i['layout_content']['medias']
        for media in med:
          pk=media['media']['pk']
          code=media['media']['code']
          
          link='https://www.instagram.com/p/'+code
          like=rs.post(f'https://www.instagram.com/web/likes/{pk}/like/',headers={
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-length': '0',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-prefers-color-scheme': 'light',
		'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}).json()
          try:
            if like["feedback_title"]=="Try Again Later":
              error+=1
              s=1000
          except :
              pass
          try:
            if like['message']=='Unable to post comment.':
              bad+=1
              s=j
          except :
            pass
          if like["status"]=="ok":
            good+=1
            s=j
          put_text(f'''
- - - - - - - - - - - - - - - - -  
Done >>> {good} 
bad >>> {bad}  
Block >>> {error} 
link >>> {link}
seconse >>> {s}
- - - - - - - - - - - - - - - - -''')
    sleep(s)
          
start_server(App,port=8080,debug=True)
