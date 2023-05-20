import random

def handle_response(message, messageAuthorId) -> str:
    p_message = message.lower()
    print(p_message)
    
    if "$addmovie" in p_message:
        return "Filme adicionado na tua cabeça piquene de merd"

    if p_message == 'hello':
        return 'Olá o meu nome é Cristiano Amigo e eu não gosto do pedro porque ele não tem cabelo'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == '!help':
        return "`This is a help message that you can modify`"
    
    if p_message == 'joke':
        return "A cara do pedro"
    
    if messageAuthorId == 171379982046724096:
        return 'https://tenor.com/view/zain-ssbm-melee-summit-smash-gif-22400831'    
