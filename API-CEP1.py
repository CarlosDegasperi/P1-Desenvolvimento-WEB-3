import requests

def main():
    print('|-------------------------------------------------|')
    print('| Consulta CEP - Utilizando API (ViaCEP.com.br)   |')
    print('|-------------------------------------------------|')
    cep_UF = ''
    cep_CIDADE = ''
    cep_LOGRADOURO = ''
    cep_INFORMADO = ''
    
    # Verificação do CEP
    while not cep_INFORMADO.isdecimal() or not len(cep_INFORMADO) == 8:
        cep_INFORMADO = input('Infomar o CEP a ser consultado (8 dígitos) ou (ENTER) para SAIR: ')
        if cep_INFORMADO == '':
            cep_UF =         input('Informar a UF desejada....>: ')
            if len(cep_UF) != 2:
                print('- ERRO: UF é obrigatório!!!!')
                main()            
            cep_CIDADE =     input('Informar a Cidade desejada>: ')
            if len(cep_CIDADE) < 3:
                print('- ERRO: Cidade tem que ter no mínimo TRES letras!!!')
                main()
            cep_LOGRADOURO = input('Informar o Logradouro.....>: ')
            if len(cep_LOGRADOURO) < 3:
                print('- ERRO: Logradouro tem que ter no mínimo TRES letras!!!')                
                main()
            
            consumo_api = requests.get(f'https://viacep.com.br/ws/{cep_UF}/{cep_CIDADE}/{cep_LOGRADOURO}/json/')
            
            print('SAINDO...')
            exit()
        else:
            if cep_INFORMADO.isdecimal() is False or len(cep_INFORMADO) != 8:
                print(f'- ERRO: CEP INFORMADO ({cep_INFORMADO}) É INVÁLIDO!!!')
            # Usando API com retorno de arquivo em JSON
            consumo_api = requests.get(f'https://viacep.com.br/ws/{cep_INFORMADO}/json/')
            # Usando API com retorno de arquivo em XML
#           consumo_api = requests.get(f'https://viacep.com.br/ws/{cep_INFORMADO}/xml/')

#           A Implementar: (Usando cep_UF, cep_CIDADE, cep_LOGRADOURO)
#           Também existe a opçao de se Consultar UF+CIDADE+Logradouro quando o USUARIO não sabe o seu CEP
#           consumo_api = requests.get(f'https://viacep.com.br/ws/SP/Rio Claro/22/json/')
            cep_data = consumo_api.json()

            # Organização das informações
            if 'erro' not in cep_data.keys() and consumo_api.status_code == 200:
                print(f'- CEP consultado: {cep_data["cep"]}')
                print(f'- Endereço.....>: {cep_data["logradouro"]} {cep_data["complemento"]}')
                print(f'- Bairro.......>: {cep_data["bairro"]}')
                print(f'- Cidade/UF....>: {cep_data["localidade"]}-{cep_data["uf"]}')
            else:
                # Tratamento de Erros
#               if consumo_api.status_code == 400:
                    print(f'- ERRO: CEP INFORMADO ({cep_INFORMADO}) NÃO ENCONTRADO NA API VIACEP!!!')
                    user_option = input('- Deseja consultar outro CEP [S/N]? ').upper()
                    while user_option not in 'SN':
                        print(f'- ERRO: ({user_option}) NÃO É UMA OPÇÃO VÁLIDA!!!')
                        user_option = input('- Deseja consultar outro CEP [S/N]? ').upper()
                        if user_option.upper() == 'S':
                            main()
                        else:
                            print('- SAINDO DO PROGRAMA...')

main()
