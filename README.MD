1. Clone o repositório:

git clone https://github.com/Diessica018/modulo.git

2. Crie e ative um ambiente virtual: 

python -m venv .venv
source .venv/bin/activate

3. Instale as dependências: 
pip install -r requirements.txt

## Uso
python src/main.py
Ou use as funções diretamente:
from utils.utils import calcular_idade
print(calcular_idade(17))  # Saída: Você é menor de idade.

