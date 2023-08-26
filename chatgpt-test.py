import requests

url = 'https://free.churchless.tech/v1/chat/completions'
myobj ={
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "generate a 10 question quizz on game of thrones with 4 options for each question"}]
}
x = requests.post(url, json = myobj)

print(x.text)