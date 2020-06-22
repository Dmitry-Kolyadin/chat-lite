import threading, random, vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
vk_session = vk_api.VkApi(token="a97639c2920a7c1f0c7eb68f0dace4e53ebdcf04344f56cf349335b97c2314328d66a8fdb21849f864a20")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '171219131')
def d():
    while 1:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW and event.obj['message']['text']:
                    print('\n----:'+event.obj['message']['text'])
                    while 1:
                        try:
                            vk.messages.send(peer_id='362987116', message='Доставлено', random_id=random.randint(-99474836, +99474836))
                            break
                        except: pass
        except: pass
threading.Thread(target=d).start()
while 1:
    try: vk.messages.send(peer_id='362987116', message=input(), random_id=random.randint(-99474836, +99474836))
    except: pass
#Keenetic-6
#dyz6vTkB
