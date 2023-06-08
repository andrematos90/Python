import inspect
import webbrowser

help_data = {
    'math': {
        'description': 'Funções matemáticas',
        'functions': {
            'sqrt': {
                'description': 'Retorna a raiz quadrada de um número',
                'syntax': 'sqrt(n)',
                'example': 'sqrt(25) retorna 5'
            },
            'sin': {
                'description': 'Retorna o seno de um ângulo em radianos',
                'syntax': 'sin(angle)',
                'example': 'sin(0) retorna 0.0'
            },
            # mais funções matemáticas...
        }
    },
    'string': {
        'description': 'Operações de string',
        'functions': {
            'capitalize': {
                'description': 'Retorna a string com o primeiro caractere em maiúsculo',
                'syntax': 'capitalize()',
                'example': '"hello".capitalize() retorna "Hello"'
            },
            'replace': {
                'description': 'Substitui todas as ocorrências de uma substring por outra',
                'syntax': 'replace(old, new)',
                'example': '"banana".replace("a", "o") retorna "bonono"'
            },
            # mais funções de string...
        }
    },
    # mais categorias...
}

def display_help(category=None, function=None):
    if category:
        if category in help_data:
            if function:
                if function in help_data[category]['functions']:
                    display_function_help(category, function)
                else:
                    print(f"A função '{function}' não foi encontrada na categoria '{category}'.")
            else:
                display_category_help(category)
        else:
            print(f"A categoria '{category}' não foi encontrada.")
    else:
        print("SISTEMA DE AJUDA")
        print("Use 'help(categoria)' para obter ajuda sobre uma categoria específica.")
        print("Use 'help(categoria, função)' para obter ajuda sobre uma função específica.")
        print("Use 'categorias()' para listar todas as categorias disponíveis.")

def display_category_help(category):
    print(f"{category.upper()} - {help_data[category]['description']}")
    print("Funções disponíveis:")
    for function in help_data[category]['functions']:
        print(f"- {function}")

def display_function_help(category, function):
    help_info = help_data[category]['functions'][function]
    print(f"{category.upper()} - {function}")
    print(f"Descrição: {help_info['description']}")
    print(f"Sintaxe: {help_info['syntax']}")
    print(f"Exemplo: {help_info['example']}")

def categorias():
    print("CATEGORIAS DISPONÍVEIS:")
    for category in help_data:
        print(f"- {category}")

def open_external_resource(url):
    webbrowser.open(url)

# Exemplo de uso
display_help()  # Exibe uma visão geral do sistema de ajuda

display_help('math')  # Exibe ajuda para a categoria 'math'
display_help('math', 'sqrt
