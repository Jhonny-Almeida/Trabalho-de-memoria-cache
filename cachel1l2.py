import random
import time
from dataclasses import dataclass

@dataclass
class NivelCache:
    """Representa um nível de cache"""
    nome: str
    taxa_acerto: float  # Taxa de acerto (0.0 a 1.0)
    tempo_acesso: float  # Tempo de acesso em ns
    
@dataclass
class Estatisticas:
    """Estatísticas da simulação"""
    total_acessos: int = 0
    acertos_l1: int = 0
    acertos_l2: int = 0
    acessos_memoria: int = 0
    tempo_total: float = 0.0
    
    def resetar(self):
        """Reseta as estatísticas"""
        self.total_acessos = 0
        self.acertos_l1 = 0
        self.acertos_l2 = 0
        self.acessos_memoria = 0
        self.tempo_total = 0.0

class SimuladorCache:
    """Simulador de hierarquia de memória cache"""
    
    def __init__(self, l1: NivelCache, l2: NivelCache, tempo_memoria: float = 100.0):
        self.l1 = l1
        self.l2 = l2
        self.tempo_memoria = tempo_memoria
        self.estatisticas = Estatisticas()
        
    def simular_acesso(self) -> float:
        """Simula um único acesso à memória"""
        tempo_acesso = 0.0
        self.estatisticas.total_acessos += 1
        
        # Tenta acessar L1
        tempo_acesso += self.l1.tempo_acesso
        if random.random() < self.l1.taxa_acerto:
            self.estatisticas.acertos_l1 += 1
            return tempo_acesso
        
        # Falha em L1, tenta L2
        tempo_acesso += self.l2.tempo_acesso
        if random.random() < self.l2.taxa_acerto:
            self.estatisticas.acertos_l2 += 1
            return tempo_acesso
        
        # Falha em todas as caches, acessa memória principal
        tempo_acesso += self.tempo_memoria
        self.estatisticas.acessos_memoria += 1
        
        return tempo_acesso
    
    def executar_simulacao(self, num_acessos: int = 1000000) -> float:
        """Executa a simulação"""
        self.estatisticas.resetar()
        tempo_total = 0.0
        
        print(f"Simulando {num_acessos:,} acessos...")
        inicio = time.time()
        
        for _ in range(num_acessos):
            tempo_total += self.simular_acesso()
        
        decorrido = time.time() - inicio
        print(f"Simulação concluída em {decorrido:.2f} segundos\n")
        
        self.estatisticas.tempo_total = tempo_total
        return tempo_total / num_acessos
    
    def calcular_media_teorica(self) -> float:
        """Calcula o tempo médio teórico"""
        # T_medio = T_L1 + (1-H_L1)*T_L2 + (1-H_L1)*(1-H_L2)*T_Memoria
        
        tempo_medio = self.l1.tempo_acesso
        taxa_falha_l1 = 1.0 - self.l1.taxa_acerto
        tempo_medio += taxa_falha_l1 * self.l2.tempo_acesso
        
        taxa_falha_l2 = 1.0 - self.l2.taxa_acerto
        tempo_medio += taxa_falha_l1 * taxa_falha_l2 * self.tempo_memoria
        
        return tempo_medio
    
    def imprimir_resultados(self, tempo_medio_sim: float, tempo_medio_teorico: float):
        """Imprime os resultados da simulação"""
        print("=" * 60)
        print("RESULTADOS DA SIMULAÇÃO".center(60))
        print("=" * 60)
        
        print(f"\nTotal de acessos: {self.estatisticas.total_acessos:,}")
        print("\nDistribuição de Acertos:")
        print(f"  Acertos L1: {self.estatisticas.acertos_l1:,} ({self.estatisticas.acertos_l1/self.estatisticas.total_acessos*100:.2f}%)")
        print(f"  Acertos L2: {self.estatisticas.acertos_l2:,} ({self.estatisticas.acertos_l2/self.estatisticas.total_acessos*100:.2f}%)")
        print(f"  Memória: {self.estatisticas.acessos_memoria:,} ({self.estatisticas.acessos_memoria/self.estatisticas.total_acessos*100:.2f}%)")
        
        print("\n" + "-" * 60)
        print("Tempo Médio de Acesso:")
        print(f"  Simulado:  {tempo_medio_sim:.4f} ns")
        print(f"  Teórico:   {tempo_medio_teorico:.4f} ns")
        diferenca = tempo_medio_sim - tempo_medio_teorico
        print(f"  Diferença: {diferenca:.4f} ns ({diferenca/tempo_medio_teorico*100:.2f}%)")
        
        print("\n" + "=" * 60)
        print("ANÁLISE DE DESEMPENHO".center(60))
        print("=" * 60)
        
        # Aceleração
        aceleracao = self.tempo_memoria / tempo_medio_teorico
        print(f"\nAceleração vs Memória Principal: {aceleracao:.2f}x")
        
        # Tempo economizado
        tempo_economizado = self.tempo_memoria - tempo_medio_teorico
        print(f"Tempo economizado por acesso: {tempo_economizado:.2f} ns ({tempo_economizado/self.tempo_memoria*100:.1f}%)")
        
        # Taxa de acerto global
        acertos_globais = self.estatisticas.acertos_l1 + self.estatisticas.acertos_l2
        taxa_acerto_global = acertos_globais / self.estatisticas.total_acessos
        print(f"Taxa de acerto global: {taxa_acerto_global*100:.2f}%")
        
        print("\n" + "=" * 60)

def main():
    """Função principal"""
    print("=" * 60)
    print("SIMULADOR DE CACHE MULTINÍVEL".center(60))
    print("=" * 60)
    
    # Configuração das caches (L1 e L2 apenas)
    l1 = NivelCache("L1", taxa_acerto=0.90, tempo_acesso=1.0)
    l2 = NivelCache("L2", taxa_acerto=0.99, tempo_acesso=10.0)
    tempo_memoria = 100.0
    
    print("\nConfiguração:")
    print(f"  L1: Taxa de acerto = {l1.taxa_acerto*100:.1f}%, Tempo = {l1.tempo_acesso:.1f} ns")
    print(f"  L2: Taxa de acerto = {l2.taxa_acerto*100:.1f}%, Tempo = {l2.tempo_acesso:.1f} ns")
    print(f"  Memória Principal: Tempo = {tempo_memoria:.1f} ns")
    print()
    
    # Criar simulador
    simulador = SimuladorCache(l1, l2, tempo_memoria)
    
    # Calcular tempo teórico
    tempo_medio_teorico = simulador.calcular_media_teorica()
    
    # Executar simulação
    tempo_medio_sim = simulador.executar_simulacao(num_acessos=100000000)
    
    # Imprimir resultados
    simulador.imprimir_resultados(tempo_medio_sim, tempo_medio_teorico)
    
    print("\n✓ Simulação concluída com sucesso!")

if __name__ == "__main__":
    random.seed(42)  # Para reprodutibilidade
    main()