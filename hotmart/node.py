import asyncio
import websockets

def is_palindrome(s):
    print(s)
    return s == s[::-1]

def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return "Sem palindromo"
    
    longest = ""
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    
    return longest if longest else "Sem palindromo"

async def process_server_messages(uri):
    async with websockets.connect(uri) as websocket:
        try:
            # Enviar comando para iniciar o desafio
            print("Enviando comando para iniciar o desafio.")
            await websocket.send("start palindromo")
            
            while True:
                # Receber a mensagem do servidor
                message = await websocket.recv()
                print("Mensagem recebida do servidor:", message)
                
                if "Bem-Vindo ao HotCTF" in message:
                    print(message)
                else:
                    # Processar a mensagem recebida
                    response_lines = []
                    for line in message.split('\n'):
                        word = line.strip()
                        if word:
                            response = longest_palindrome(word)
                            response_lines.append(f"{word}: {response}")
                    
                    # Enviar a resposta de volta ao servidor
                    response_message = "\n".join(response_lines)
                    
                    if websocket.open:
                        print("Enviando resposta ao servidor.")
                        await websocket.send(response_message)
                    else:
                        print("A conexão foi fechada antes de enviar a resposta.")
                        break
        
        except websockets.ConnectionClosed as e:
            print(f"A conexão foi fechada pelo servidor: {e}")

# URI do servidor WebSocket
uri = "wss://ctf-challenges.devops.hotmart.com/echo"

# Executar a função de processamento
asyncio.run(process_server_messages(uri))
