import requests


class Personagem:
    """Classe Personagem"""

    def __init__(self, id):
        """Método construtor da classe"""
        
        self.id = id
    
    def realizar_request(self):
        """Método para fazer a requisição da api do rick and morty"""

        # url da requisição
        url = f'https://rickandmortyapi.com/api/character/{self.id}'

        # realizando a requisição e convertendo os dados em um json
        response = requests.get(url)
        dados = response.json()

        # passo os dados que será utilizado para uma lista
        dados_lista = [dados["name"], dados["status"], dados["species"],
        dados["image"], dados["location"]["name"], dados["episode"]]

        return dados_lista
    

    def pegar_episodio(self, ep):
        """Método para fazer slice na string do dado da lista"""

        if len(ep) == 1:
            numero_episodio = ep[0]
            numero_episodio[2:-2]
            return numero_episodio
        else:
            numero_episodio = ep[-1]
            numero_episodio[2:-2]
            return numero_episodio
    

    def request_nome_episodio(self, episodio):
        """Método para realizar a requisição para obter o nome
        do episodio"""

        # realizar a requisição para obter os dados
        response = requests.get(self.pegar_episodio(episodio))
        dados = response.json()

        # passando o dado para variavel
        nome_episodio = dados["name"]

        return nome_episodio
