from requests import post
mj=0
email=input(' Put Username Just : ')
url='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
h={
 'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
 'X-Pigeon-Rawclienttime':'1707104597.347',
 'X-IG-Connection-Speed':'-1kbps',
 'X-IG-Bandwidth-Speed-KBPS':'-1.000',
 'X-IG-Bandwidth-TotalBytes-B':'0',
 'X-IG-Bandwidth-TotalTime-MS':'0',
 'X-IG-VP9-Capable':'false',
 'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
 'X-IG-Connection-Type':'WIFI',
 'X-IG-Capabilities':'3brTvw==',
 'X-IG-App-ID':'567067343352427',
 'User-Agent':'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
 'Accept-Language':'ar-IQ, en-US',
 'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
 'Accept-Encoding':'gzip, deflate',
 'Host':'i.instagram.com',
 'X-FB-HTTP-Engine':'Liger',
 'Connection':'keep-alive',
 'Content-Length':'364',
 }
da={
 'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',
 
 'ig_sig_key_version':'4',
 }
s=post(url,headers=h,data=da).text
 #print(s)
if '"تم إرسال البريد الإلكتروني"' in s:
 print(f'Done Send Rest :[{email}]')
else:
 print(f'Dont Send Email : [{email}]')
