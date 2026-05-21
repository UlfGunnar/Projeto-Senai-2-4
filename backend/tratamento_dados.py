class ValidadorSeguranca:

    def verificar_senha(self, teste_senha: str):
        # Print para mostrar qual senha está sendo analisada no momento
        print(f"\n[ANÁLISE] Testando a senha: '{teste_senha}'")
        
        # Correção: usando os parênteses () para o Python executar a função
        if teste_senha.isalnum():
            print(" -> Resultado: A senha contém APENAS letras e números.")
            print(" -> Ação: REJEITADA (Falta caractere especial). Retornando False.")
            return False
        else:
            print(" -> Resultado: A senha POSSUI caracteres especiais (ex: @, !, #).")
            print(" -> Ação: APROVADA! Retornando True.")
            return True


# =====================================================================
# ÁREA DE TESTES (Fora da classe)
# =====================================================================
validador = ValidadorSeguranca()

print("=== INICIANDO OS TESTES DE SENHA ===")

# Teste 1: Uma senha que DEVE SER REJEITADA (só tem letras e números)
resultado_1 = validador.verificar_senha("xebinhas123")
print(f" Retorno da função no Teste 1: {resultado_1}")

print("-" * 40)

# Teste 2: A sua senha com '@' que DEVE SER APROVADA
resultado_2 = validador.verificar_senha("xebinhas@123")
print(f" Retorno da função no Teste 2: {resultado_2}")

print("\n=== FIM DOS TESTES ===")