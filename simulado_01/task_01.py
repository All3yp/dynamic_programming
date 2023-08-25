class CalculadoraAbstrata:
    
    def por_extenso_para_operador(self, operacao):
        operadores = {
            '+': ['mais'],
            '-': ['menos'],
            '*': ['vezes'],
            '/': ['dividido', 'por'],
            '**': ['elevado', 'a']
        }

        for operador, palavras in operadores.items():
            if all(palavra in operacao for palavra in palavras):
                return operador
        return None

    def extrai_numeros(self, operacao):
        palavras = operacao.split()
        
        numeros = {
            'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'tres': 3, 'quatro': 4,
            'cinco': 5, 'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10
        }

        num1 = numeros.get(palavras[0], None)
        num2 = numeros.get(palavras[-1], None)

        return (num1, num2)

    def calcula_por_extenso(self, operacao):
        operador = self.por_extenso_para_operador(operacao)
        if operador is not None:
            num1, num2 = self.extrai_numeros(operacao)
            print(num1, num2, "extracao")
            if operador == '+':
                resultado = self.soma(num1, num2)
                return f'{num1} mais {num2} é igual a {resultado}'
            elif operador == '-':
                resultado = self.subtracao(num1, num2)
                return f'{num1} menos {num2} é igual a {resultado}'
            elif operador == '*':
                resultado = self.multiplicacao(num1, num2)
                return f'{num1} vezes {num2} é igual a {resultado}'
            elif operador == '/':
                if num2 != 0:
                    resultado = self.divisao(num1, num2)
                    return f'{num1} dividido por {num2} é igual a {resultado:.1f}'
                else:
                    return 'Divisão por zero não é permitida.'
            elif operador == '**':
                resultado = self.potencia(num1, num2)
                return f'{num1} elevado a {num2} é igual a {resultado}'
        
        return 'Operação inválida ou não suportada'

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

    def potencia(self, a, b):
        return a ** b


class CalculadoraConsole(CalculadoraAbstrata):
    def main(self):
        print("Bem-vindo/a à calculadora console!")
        print('Digite a operação desejada por extenso (exemplo: "dois mais dois"): ')
        operacao = input()
        resultado = self.calcula_por_extenso(operacao)
        print(resultado)

if __name__ == "__main__":
    c = CalculadoraConsole()
    c.main()
