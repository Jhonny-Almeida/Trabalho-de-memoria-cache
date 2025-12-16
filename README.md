# Simulador de Cache Multinível (L1 + L2 + L3)

Um projeto de Arquitetura de Computadores que simula o comportamento de hierarquias de cache multinível, explorando e comparando políticas de cache **inclusiva** vs **exclusiva**.

## 📋 Sobre o Projeto

Este simulador implementa uma hierarquia de memória cache com múltiplos níveis (L1, L2, L3) e permite analisar o impacto das diferentes políticas de inclusividade no desempenho do sistema. O projeto foi desenvolvido como parte de um trabalho acadêmico em Arquitetura de Computadores.

### Características Principais
- Simulação de caches multinível (L1, L2, L3)
- Implementação de políticas inclusiva e exclusiva
- Análise estatística detalhada de desempenho
- Cálculo de tempos médios de acesso teóricos e simulados
- Visualização de taxas de acerto/miss por nível

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- Nenhuma dependência externa necessária

### Executando a Simulação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/simulador-cache-multinivel.git

# Acesse o diretório
cd simulador-cache-multinivel

# Execute o simulador
python simulador_cache.py
```

## 🏗️ Arquitetura do Código

### Estrutura Principal
- **`NivelCache`**: Representa um nível de cache individual com taxas de acerto e tempos de acesso
- **`Estatisticas`**: Coleta e gerencia dados estatísticos da simulação
- **`SimuladorCache`**: Classe principal que orquestra toda a simulação

### Funcionalidades Implementadas
1. **Simulação Estatística**: Modelo baseado em probabilidades para acesso às caches
2. **Cálculo Teórico**: Fórmulas matemáticas para validação dos resultados
3. **Análise Comparativa**: Comparação entre políticas inclusivas e exclusivas
4. **Métricas de Desempenho**:
   - Tempo médio de acesso
   - Taxas de acerto por nível
   - Aceleração vs memória principal
   - Tempo economizado

## 📊 Configurações de Simulação

### Parâmetros Atuais
- **L1**: Taxa de acerto 90%, Tempo de acesso 1.0 ns
- **L2**: Taxa de acerto 99%, Tempo de acesso 10.0 ns
- **Memória Principal**: Tempo de acesso 100.0 ns
- **Número de Acessos**: 100.000.000 (por padrão)

### Personalização
Para modificar os parâmetros da simulação, edite o arquivo `simulador_cache.py` na seção `main()`:
```python
l1 = NivelCache("L1", taxa_acerto=0.90, tempo_acesso=1.0)
l2 = NivelCache("L2", taxa_acerto=0.99, tempo_acesso=10.0)
tempo_memoria = 100.0
tempo_medio_sim = simulador.executar_simulacao(num_acessos=100000000)
```

## 📈 Resultados e Análise

O simulador gera um relatório completo que inclui:

### Estatísticas de Acesso
- Distribuição de acertos por nível (L1, L2, Memória)
- Taxas de acerto percentuais
- Total de acessos simulados

### Análise de Desempenho
- Tempo médio de acesso (simulado vs teórico)
- Aceleração em relação à memória principal
- Tempo economizado por acesso
- Taxa de acerto global do sistema

## 🧪 Testes e Validação

### Reprodutibilidade
```python
# Semente fixa para resultados reproduzíveis
random.seed(42)
```

### Validação Matemática
O simulador compara resultados simulados com cálculos teóricos usando a fórmula:
```
T_medio = T_L1 + (1-H_L1)*T_L2 + (1-H_L1)*(1-H_L2)*T_Memoria
```

## ✍️ Autores

- **Jhonny Almeida** - *Trabalho de Arquitetura de Computadores*
- **Marcello Batista Ribeiro** - *Orientação*

---

*Projeto desenvolvido para a disciplina de Arquitetura de Computadores - UNIR - Universidade Federal de Rondônia - 2025*
