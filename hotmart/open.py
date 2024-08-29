"""
import asyncio
import websockets

async def connect():
    uri = "wss://ctf-challenges.devops.hotmart.com/echo"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, Server!")
        process.stdin.write(b'start palindromo\n')
        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(connect())
"""
import requests

def is_palindrome(word):
    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]

def send_challenge_solution(word):
    url = "wss://ctf-challenges.devops.hotmart.com/echo" # Substitua pelo endereço real do servidor
    payload = {
        'challenge_code': 'palindromo',
        'word': word
    }
    response = requests.post(url, data=payload)
    return response.text

test_word = "100"
if is_palindrome(test_word):
    print(f"A palavra '{test_word}' é um palíndromo.")
    result = send_challenge_solution(test_word)
    print("Resposta do servidor:", result)
else:
    print(f"A palavra '{test_word}' não é um palíndromo.")
 #.bat