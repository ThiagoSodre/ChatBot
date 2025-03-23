# Gênio Sarcástico da Lâmpada - Chat com IA

Este projeto implementa um assistente virtual baseado no modelo **Gemini 2.0 Flash**, que simula um gênio da lâmpada sarcástico e mal-humorado. Ele responderá três perguntas sobre um contexto escolhido pelo usuário, sempre com respostas irônicas e engraçadas.

## Requisitos

Antes de rodar o código, certifique-se de ter:

1. **Python 3.8 ou superior**
2. A biblioteca `google-generativeai` instalada
3. Uma chave de API válida para acessar o **Gemini AI**

## Instalação

Clone este repositório e instale as dependências necessárias:

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/genio-sarcastico.git
cd genio-sarcastico

# Criar um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Gemini:

```
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

## Como Usar

1. **Executar o script:**

   ```bash
   python main.py
   ```

2. O gênio fará uma apresentação breve e mal-humorada.
3. Você deve fornecer um contexto para suas perguntas.
4. Depois de escolher o contexto, faça suas perguntas.
5. O gênio responderá de maneira sarcástica e divertida.
6. Após três perguntas, o gênio se despedirá de forma arrogante.

## Exemplo de Uso

```bash
Digite o contexto da sua 1ª pergunta? Magia
Gênio: Ah, vocês, mortais, sempre querendo saber de tudo. Tá, fala logo, qual a sua pergunta sobre Magia?
pergunta (1/3): Como lançar um feitiço?
Gênio: Ah, claro, porque você é um mago prodígio agora? Basta mexer as mãos e acreditar. Boa sorte não explodindo!
```

## Estrutura do Código

- **`main.py`**: Contém o script principal do gênio.
- **`.env`**: Arquivo para armazenar a chave da API (não deve ser commitado).
- **`requirements.txt`**: Lista de dependências do projeto.

## Personalização

- **Mudar o número de perguntas**: Altere `QTDE_PERGUNTAS` no código.
- **Modificar o tom do gênio**: Edite a prompt dentro da função `obter_desejo()`.



