# P1-Desenvolvimento-WEB III - Python Consumo de API
- 3.Semestre DSM-Desenvolvimento de Sistemas Multiplataforma (FATEC-Araras)
- Prof Me Orlando Saraiva Jr
- Consulta de Informações do Endereço atraves do CEP informado (executar: python API-CEP.py)
- O programa solicita (input) um CEP e faz a validação, consome uma API e retorna informações do endereço (Logradouro/Complemento/Bairro/Cidade/UF)
- Foi usada a API do ViaCEP que é um webservice gratuito e de alto desempenho para consultar Códigos de Endereçamento Postal (CEP) do Brasil, com futura implementação para consultar a UF+CIDADE+Logradouro retornando o CEP

## Como Ativar o Ambiente Virtual
- python -m venv P1-DW3
- cd P1-DW3	
- cd Scripts
- activate.bat

## Comando usado para a criação do requirements.txt
- pip freeze > requirements.txt
## Comando usado para execução correta do Sistema
- pip install -r requirements.txt
- pip install requests

## Sites de referência
- https://www.w3schools.com/python/module_requests.asp
- https://jtemporal.com/requirements-txt/
- https://docs.python.org/3/
- https://viacep.com.br
