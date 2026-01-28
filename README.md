# **DDoS Simulation Experiments (L3/L4)**

Este repositório reúne os comandos, códigos, *scripts* e arquivos de apoio utilizados nos experimentos do artigo:

***“Uma Comparação das Ferramentas Open Source de CLI para Geração de Ataques DDoS em Ambientes de Internet”***

O repositório também inclui a **tabela completa com a descrição das anomalias de tráfego** avaliadas no trabalho, disponível no arquivo ***ANOMALIAS (Descrição e Resultados).pdf***, localizado no diretório raiz do projeto.

**Artigo disponível em:** <link>

---

## Resumo do artigo

*Os ataques DDoS comprometem a disponibilidade de infraestruturas críticas por meio de fluxos de dados massivos e coordenados. O emprego de ferramentas de simulação de DDoS permitem reproduzir esses comportamentos de forma controlada e segura apoiando o desenvolvimento de sistemas de segurança. Apesar das avaliações existentes, observa-se uma carência de dados comparativos sistematizados que auxiliem na seleção de ferramentas quanto à fidelidade e ao desempenho Este trabalho apresenta uma análise comparativa de ferramentas open source de linha de comando (CLI) voltadas à simulação de ataques DDoS nas **camadas de rede e transporte**. A avaliação levou em conta a capacidade de geração~de tráfego e a aderência à taxonomia de Jelena Mirkovic para modelagem de anomalias. Os resultados evidenciam diferenças significativas entre as ferramentas, indicando que a eficácia dos testes de mitigação depende da escolha de um simulador alinhado aos objetivos do experimento, favorecendo avaliações mais realistas e reprodutíveis.*

---

## Estrutura do repositório

### 📁 `Experiments/`

Contém os diretórios das ferramentas avaliadas. Cada ferramenta possui uma pasta própria:

```
Experiments/
 ├── bonesi/
 ├── hping3/
 ├── mausezahn/
 ├── scapy/
 ├── t50/
 ├── tcpreplay/
 └── trafgen/
```

Dentro de cada diretório de ferramenta, os arquivos seguem uma estrutura padrão:

* `/` (raíz)  
  Implementações das anomalias de tráfego gerais. 

* `icmp/`, `udp/`, `tcp/`  
  Implementações das anomalias de tráfego separadas por protocolo.

* `flood_tests/`  
  Testes voltados à avaliação de desempenho volumétrico (*flood*).

---

### 📁 `IPv6_Check/`

Inclui códigos e arquivos usados na verificação de suporte a *IPv6* pelas ferramentas, como:

* listas de endereços *IPv6* para *IP Spoofing*,
* comandos e arquivos de configuração usados para testar o suporte ao *IPv6*.

Esses testes serviram apenas para avaliação de suporte e não foram usados nos experimentos principais, que consideram exclusivamente *IPv4*.

---

### 📁 `tshark_scripts/`

Scripts utilizados para processamento das capturas de tráfego, incluindo:

* contagem de pacotes capturados,
* cálculo da duração das simulações.

Os scripts foram utilizados apenas na aferição do desempenho volumétrico, sendo executados antes de cada simulação conforme o protocolo testado. 

---

### 📄 Arquivos adicionais

* `ANOMALIAS (Descrição e Resultados).pdf`  
  Documento com a **descrição das anomalias de tráfego avaliadas** e seus respectivos resultados.

* `server.py`  
  Servidor simples utilizado nos experimentos da anomalia de reflexão *TCP SYN Reflection*.

---

## Ferramentas avaliadas

Os experimentos envolvem ferramentas *open source* de linha de comando (CLI) que atuam nas camadas de rede e transporte, operam no sistema operacional Linux e não dependem de interação continua do usuário:

* BoNeSi
* Hping3
* Mausezahn
* Scapy
* Tcpreplay
* Trafgen
* T50

Cada ferramenta foi executada em seu código original, sem modificações, respeitando suas funcionalidades nativas.  Além disso, não foram consideradas opções de construção manual de pacotes em modo *raw*. 

As ferramentas Hping3 e Mausezahn oferecem um modo de operação interativo, que não foi avaliado neste trabalho por estar fora do escopo do estudo.

---

## Observações importantes

* Este repositório **não deve ser utilizado para ataques reais**.
* Todo o conteúdo foi desenvolvido **exclusivamente para fins acadêmicos e experimentais**.
* Os *scripts* refletem exatamente os cenários avaliados no artigo, sem ajustes posteriores.
* A taxonomia de **Jelena Mirkovic** contribuiu para a análise da capacidade de geração de anomalias, sendo utilizada como principal referência. A análise incorporou diversos itens da lista da pesquisadora de forma integral, enquanto adaptou outros, descartou alguns por estarem fora do escopo e definiu novos a partir das capacidades de customização das ferramentas. Disponível em: [https://www.isi.edu/people-mirkovic/ddos-benchmarks/ddos-attack-list/](https://www.isi.edu/people-mirkovic/ddos-benchmarks/ddos-attack-list/)


---

## Citação

Se você utilizar este repositório em trabalhos acadêmicos, considere citar o artigo correspondente.
A entrada BibTeX será adicionada após a publicação.
