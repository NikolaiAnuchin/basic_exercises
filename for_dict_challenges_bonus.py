"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений. - DONE
2. Вывести айди пользователя, на сообщения которого больше всего отвечали. - DONE
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей. - DONE
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов). - DONE
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

def search_max_messages(messages):
    user_messages_info = {}
    for user_info in messages:
        #print(user_info["id"], type(user_info["id"]),type(str(user_info["id"])))

        if user_messages_info.get(str(user_info["sent_by"])) == None:
            user_messages_info[str(user_info["sent_by"])] = 1
        else:
            user_messages_info[str(user_info["sent_by"])] += 1
    print(messages)
    print(len(user_messages_info), len(messages))
    print(user_messages_info[max(user_messages_info, key=user_messages_info.get)])
    print(max(user_messages_info, key=user_messages_info.get))

    
def search_max_replies(messages):
    user_replies = {}
    messages_info = {}
    for user_info in reversed(messages):
        #print(user_info["id"], type(user_info["id"]),type(str(user_info["id"])))

        if messages_info.get(str(user_info["reply_for"])) == None:
            messages_info[user_info["reply_for"]] = 1
            
        else:
            messages_info[user_info["reply_for"]] += 1
        print(user_info.get("id"))
        if user_info.get("id") in messages_info:
            if user_replies.get(user_info["sent_by"]) == None:
                user_replies[user_info["sent_by"]] =  messages_info[user_info.get("id")]
            else:
                user_replies[user_info["sent_by"]] +=  messages_info[user_info.get("id")]
                print(user_info["sent_by"])
        print(user_info["sent_by"])
    print(user_replies)


def search_max_views(messages):

    user_messages_info = {}
    
    for message_info in messages:
        #print(user_info["id"], type(user_info["id"]),type(str(user_info["id"])))
        if user_messages_info.get(str(message_info["sent_at"])) == None:
            user_messages_info[str(message_info["sent_by"])] = set(message_info["seen_by"])
        else:
            user_messages_info[str(message_info["sent_by"])].update(message_info["seen_by"])

    
    #print(len(user_messages_info), len(messages))
    #print(user_messages_info[max(user_messages_info, key=user_messages_info.get)])
    print(max(user_messages_info, key=user_messages_info.get))

def search_prime_time(messages):
    
    from datetime import datetime
    prime_time = {'morning': 0,'afternoon': 0,'evening': 0}

    for message_info in messages:
        #print(user_info["id"], type(user_info["id"]),type(str(user_info["id"])))
        message_time = message_info["sent_at"]
        messages_time_info = message_time.strftime("%H")
        if int(messages_time_info) < 12:
            prime_time['morning'] += 1
        elif 12 <= int(messages_time_info) < 18 :
            prime_time['afternoon'] += 1
        else: 
            prime_time['evening'] += 1
        
        messages_time_info = str()
        message_time = 0 
            

    print(max(prime_time, key=prime_time.get))
    print(prime_time)
            
def search_long_thread_ids(messages):
    replies_info = {}
    for info in reversed(messages):
        print(str(info["reply_for"]))
        if info["reply_for"] != None:
            print(replies_info)
            #keys = [key for key, value in replies_info.items() if value == info["id"]]
            #Если встретились две ветки реплаев, один из которых ответил раньше на сообщение
            if replies_info.get(info["reply_for"]) and replies_info.get(info["id"]): 
                replies_info[info["reply_for"]] = max(replies_info[info["reply_for"]],replies_info[info["id"]] + 1)

            if replies_info.get(info["id"]): #проверка, есть ли id реплая в списке реплаев
                replies_info[info["reply_for"]]= replies_info.pop(info["id"]) + 1 #если есть, увеличиваем счётчик реплаев на 1 и меняем id реплая на id исходного сообщения
            else:
                print('huy')
                replies_info.setdefault(info["reply_for"],1) #если нет, создаем новую ветку реплаев и ставим 1 в счётчике
                
    print(max(replies_info, key=replies_info.get))        #осталось только потом по ключу найти максимум
         



if __name__ == "__main__":
    #print(generate_chat_history())
    #search_max_messages(generate_chat_history())
    #search_max_replies(generate_chat_history())
    #search_max_views(generate_chat_history())
    #search_prime_time(generate_chat_history())
    search_long_thread_ids(generate_chat_history())
