import random

NOMES = [
    "Ana", "Lucas", "Rafaela", "João", "Beatriz", "Mateus", "Clara", "Gabriel", "Sofia", "Pedro",
    "Larissa", "Enzo", "Lívia", "Felipe", "Marina", "Thiago", "Aline", "Igor", "Camila", "Ricardo",
    "Juliana", "Daniel", "Fernanda", "Bruno", "Isabela", "Rafael", "Carolina", "Miguel", "Bianca", "André",
    "Marcela", "Carlos", "Cecília", "Diego", "Lorena", "Gustavo", "Valentina", "Rodrigo", "Mariana", "Alex",
    "Fernanda", "Victor", "Helena", "Márcio", "Alessandra", "Jorge", "Patrícia", "Aurélio", "Vanessa", "Leandro",
    "Simone", "Antônio", "Claudia", "Heitor", "Débora", "Renato", "Elisa", "Paulinho", "Fabiana", "Tiago",
    "Gisele", "Claudio", "Roberta", "Ernesto", "Adriana", "Sergio", "Joana", "Arlindo", "Marta", "Vicente"
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Costa", "Ferreira", "Rodrigues", "Martins", "Alves", "Pereira",
    "Gomes", "Dias", "Neves", "Barbosa", "Ribeiro", "Carvalho", "Rocha", "Mendes", "Correia", "Monteiro",
    "Lopes", "Medeiros", "Campos", "Araújo", "Fonseca", "Pimentel", "Machado", "Teixeira", "Pinto", "Moura",
    "Cabral", "Duarte", "Figueiredo", "Coelho", "Amaral", "Chaves", "Goulart", "Barcelos", "Reis", "Borges"
]

def nome_aleatorio():
    """Retorna um nome e sobrenome aleatório."""
    return f"{random.choice(NOMES)} {random.choice(SOBRENOMES)}"

def nome_simples():
    """Retorna apenas o primeiro nome aleatório."""
    return random.choice(NOMES)
