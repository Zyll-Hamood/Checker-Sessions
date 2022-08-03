from requests import get
sessions = open('sessions.txt','r').read().splitlines()
def check(session):
    url = 'https://i.instagram.com/api/v1/users/search/?timezone_offset=10800&q=zyl7&count=10&rank_token=0'
    headers={
        "User-Agent": "Instagram 9.7.0 Android (24/7.0; 420dpi; 1080x1920; samsung; SM-N920P; nobleltespr; samsungexynos7420; ar_IQ)",
        "Cookie": f"sessionid={session}"
    }
    resp = get(url,headers=headers).text
    return resp
work = 0
notwork = 0
for session in sessions:
    resp = check(session)
    if '"status":"ok"' in resp:
        print(session)
        work +=1
        with open('sessions working.txt', 'a', encoding='utf-8', errors='ignore') as p:
            p.writelines(session + '\n')
    else:
        notwork+=1
print(f'Working : {str(work)}')