import pandas as pd
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Função para selecionar o arquivo saldo.xlsx
def selecionar_arquivo_saldo():
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o Extrato",
        filetypes=[("Planilhas", "*.xlsx")]
    )
    if caminho_arquivo:
        return caminho_arquivo
    else:
        messagebox.showerror("Erro", "Nenhum arquivo foi selecionado.")
        root.quit()

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Gerador de Arquivos ELN e ECM")

# Solicitar arquivo saldo.xlsx ao usuário
caminho_saldo = selecionar_arquivo_saldo()
df = pd.read_excel(caminho_saldo)

# Carregar os demais arquivos Excel
empresas_df = pd.read_excel("empresas.xlsx")
contas_df = pd.read_excel("contas.xlsx")
historicos_df = pd.read_excel("historico.xlsx")
contas_clientes_df = pd.read_excel("contas-clientes.xlsx")

# Converter data de competência
df['data de competência'] = pd.to_datetime(df['Data de competência'], errors='coerce', dayfirst=True)
df = df.iloc[:-1]  # Remove a última linha

# Opções de histórico principais
opcoes_historico = {
    "0002": "Valor ref. Nota Fiscal Nr.",
    "0004": "Valor ref. pagto via Internet",
    "0918": "Valor ref ISS Sobre Nf. nr.",
    "0924": "Valor ref. retenção de INSS s/NF.nr",
    "0926": "Valor ref. tarifa bancária",
}

# Função para extrair o número do lote dos 5 últimos dígitos antes da extensão .ELN
def extrair_numero_lote(nome_arquivo):
    return nome_arquivo.split(".")[0][-5:]

# Função para gerar uma linha do arquivo ECM
def gerar_linha_ecm(lote, numero_lancamento, descricao_historico, descricao_cliente):
    return f'"{lote}","{numero_lancamento}"\n{descricao_historico} - {descricao_cliente}'

# Função para gerar o arquivo ECM com base no arquivo ELN
def gerar_arquivo_ecm(nome_arquivo_eln, nome_arquivo_ecm):
    lote = extrair_numero_lote(nome_arquivo_eln)
    
    with open(nome_arquivo_eln, "r") as eln_file, open(nome_arquivo_ecm, "w", newline="\r\n") as ecm_file:
        for linha in eln_file:
            dados = linha.strip().split(",")
            numero_lancamento = dados[1]
            conta_debito = int(dados[2])
            conta_credito = int(dados[3])
            codigo_historico = int(dados[4])

            # Buscar o histórico correspondente
            historico = historicos_df[historicos_df['Codigo'] == codigo_historico]
            descricao_historico = historico['Descricao'].values[0] if not historico.empty else "Histórico não encontrado"

            # Buscar a descrição do cliente no arquivo 'contas-clientes.xlsx'
            cliente = contas_clientes_df[contas_clientes_df['Codreduzido'] == conta_debito]
            if cliente.empty:
                cliente = contas_clientes_df[contas_clientes_df['Codreduzido'] == conta_credito]

            descricao_cliente = cliente['Descricao'].values[0] if not cliente.empty else "Cliente não encontrado"

            # Escrever no arquivo ECM
            linha_ecm = gerar_linha_ecm(lote, numero_lancamento, descricao_historico, descricao_cliente)
            ecm_file.write(linha_ecm + "\n\n")

# Função para gerar arquivo ELN
def gerar_arquivo_eln(df, numero_empresa, numero_lote):
    numero_sequencial = 1
    cliente_anterior = None

    nome_arquivo_eln = f"{numero_empresa}{numero_lote}.ELN"
    with open(nome_arquivo_eln, "w", newline="\r\n") as eln_file:
        for index, row in df.iterrows():
            data_lancamento = row['data de competência'].strftime('%d%m%Y') if pd.notna(row['data de competência']) else '00000000'
            numero_sequencial_formatado = str(numero_sequencial).zfill(6)
            descricao = row['Nome do cliente ou fornecedor']
            if pd.notna(descricao):
                cliente_anterior = descricao
            else:
                descricao = cliente_anterior

            codreduzido_match = contas_df[contas_df['Descricao'].str.upper() == descricao.upper()]
            codreduzido = str(codreduzido_match['Codreduzido'].values[0]).zfill(5) if not codreduzido_match.empty else "00000"

            # Exibir informações para confirmação via interface
            messagebox.showinfo(f"Lançamento {numero_sequencial}", f"Cliente/Fornecedor: {descricao}\nData de Competência: {data_lancamento}\nValor: {row['Valor']}")

            # Interface para escolha de histórico
            escolha = simpledialog.askstring("Código do Histórico", "Digite o código do histórico ou 'OUTRO  para outro valor':")
            if escolha.lower() == "outro":
                escolha = simpledialog.askstring("Histórico", "Informe o código do histórico desejado (4 dígitos):")
            cod_historico = escolha if escolha.isdigit() and len(escolha) == 4 else "0000"

            valor_bruto = abs(row['Valor'])

            if cod_historico == "0002":
                conta_debito = simpledialog.askstring("Conta", "Digite a conta para o primeiro lançamento (5 dígitos):").zfill(5)
                eln_file.write(f"{data_lancamento},{numero_sequencial_formatado},{conta_debito},00000,0002,00000,00000,{valor_bruto:.2f}\n")
                numero_sequencial += 1

                # Confirmação de ISS
                if messagebox.askyesno("ISS", "Haverá lançamento de ISS?"):
                    valor_iss = valor_bruto * 0.10
                    numero_sequencial_formatado = str(numero_sequencial).zfill(6)
                    eln_file.write(f"{data_lancamento},{numero_sequencial_formatado},{'00000'},00049,0918,00000,00000,{valor_iss:.2f}\n")
                    numero_sequencial += 1

                # Confirmação de INSS
                if messagebox.askyesno("INSS", "Haverá lançamento de INSS?"):
                    valor_inss = valor_bruto * 0.11
                    numero_sequencial_formatado = str(numero_sequencial).zfill(6)
                    eln_file.write(f"{data_lancamento},{numero_sequencial_formatado},{'00000'},01297,0924,00000,00000,{valor_inss:.2f}\n")
                    numero_sequencial += 1

                valor_liquido = valor_bruto - (valor_iss if 'valor_iss' in locals() else 0) - (valor_inss if 'valor_inss' in locals() else 0)
                numero_sequencial_formatado = str(numero_sequencial).zfill(6)
                eln_file.write(f"{data_lancamento},{numero_sequencial_formatado},{'00000'},{codreduzido},0002,00000,00000,{valor_liquido:.2f}\n")
                numero_sequencial += 1
            else:
                conta_debito = codreduzido if row['Valor'] < 0 else "00000"
                conta_credito = "00000" if row['Valor'] < 0 else codreduzido
                valor_lancamento = f"{valor_bruto:.2f}"
                eln_file.write(f"{data_lancamento},{numero_sequencial_formatado},{conta_debito},{conta_credito},{cod_historico},00000,00000,{valor_lancamento}\n")
                numero_sequencial += 1

    return nome_arquivo_eln

# Solicitar ao usuário número da empresa e número do lote via interface
numero_empresa = simpledialog.askstring("Número da Empresa", "Informe o número da empresa:")
numero_lote = simpledialog.askstring("Número do Lote", "Informe o número do lote (5 dígitos):")
while len(numero_lote) != 5 or not numero_lote.isdigit():
    numero_lote = simpledialog.askstring("Número Inválido", "Número de lote inválido. Informe um número de lote com 5 dígitos:")

# Gerar arquivo ELN e ECM
nome_arquivo_eln = gerar_arquivo_eln(df, numero_empresa, numero_lote)
nome_arquivo_ecm = nome_arquivo_eln.replace(".ELN", ".ECM")
gerar_arquivo_ecm(nome_arquivo_eln, nome_arquivo_ecm)

messagebox.show
