import google.generativeai as genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")  

model = genai.GenerativeModel("gemini-2.0-flash")
QTDE_PERGUNTAS = 3

def obter_desejo(pergunta, contexto, model):
    model = model
    try:
        resposta = model.generate_content(f"Você é um gênio da lampada gosta de ficar na sua lampada, mas é obrigado a responder as pergundas do usuário sobre o {contexto}, responda de forma sarcastica e malhumorada, mas que seja tão malhumorada que se torne até engraçado as vezes {pergunta}")
        return resposta.text
    except Exception as e:
        return f"Gênio: Houve um erro ao processar sua pergunta: {e}"

def main():
    
    genai.configure(api_key = API_KEY)
    print(obter_desejo("Faça uma apresentação breve e mal humorada de como vc não queria atender o usuário e diga que tem apenas 3 respostas e será sobre um tema","a ser escolhido pelo usuário em breve", model))


    for i in range(QTDE_PERGUNTAS):
        contexto = input(f"me de o contexto da sua {i+1}º Pergunta?")
        print(f"Gênio: Ah, vocês, mortais, sempre querendo saber de tudo. Tá, fala logo, qual a sua pergunta sobre {contexto}?")
        pergunta = input(f"pergunta ({i+1}/3): ")
        print(obter_desejo(pergunta, contexto, model))
        


    print("Gênio: Já chega! Três perguntas é o limite. Vocês, mortais, não têm mais nada para fazer? Sumam da minha frente!")
    print(model.generate_content("crie uma despedida breve irozinando como as perguntas anteriores foram inuteis e que o gênio tem coisas mais importantes para fazer").text)
if __name__ == "__main__":
    main()