import pandas as pd
import os
from datetime import datetime

def iniciar_automacao():
    print("Iniciando robô de automação da KL STORE...")
    print("Lendo a base de dados de vendas...")
    
    try:
        # 1. Carrega os dados da planilha
        df = pd.read_csv('vendas.csv')
        
        # 2. Processamento: Calcula o faturamento por linha (Qtd * Valor)
        df['Faturamento'] = df['Quantidade'] * df['Valor_Unitario']
        
        # 3. Análise: Agrupa os dados para saber o total vendido por produto
        resumo_produtos = df.groupby('Produto')['Faturamento'].sum().reset_index()
        
        # 4. Geração de Relatório Automático
        data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M")
        nome_arquivo = f"relatorio_gerencial_{data_atual}.txt"
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write("=== RELATÓRIO AUTOMÁTICO DE VENDAS - KL STORE ===\n")
            arquivo.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}\n")
            arquivo.write("=" * 49 + "\n\n")
            
            arquivo.write("Faturamento Total por Produto:\n")
            arquivo.write("-" * 49 + "\n")
            
            total_geral = 0
            for index, row in resumo_produtos.iterrows():
                arquivo.write(f"- {row['Produto']}: R$ {row['Faturamento']:.2f}\n")
                total_geral += row['Faturamento']
                
            arquivo.write("-" * 49 + "\n")
            arquivo.write(f"FATURAMENTO GERAL DO PERÍODO: R$ {total_geral:.2f}\n")
            arquivo.write("=================================================\n")
            
        print(f"Sucesso! Relatório gerado e salvo como: {nome_arquivo}")
        
    except FileNotFoundError:
        print("Erro: O arquivo 'vendas.csv' não foi encontrado na pasta.")

if __name__ == "__main__":
    iniciar_automacao()