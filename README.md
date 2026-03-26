# **DDoS Simulation Experiments (L3/L4)**

Este repositório reúne os comandos, códigos, *scripts* e arquivos de apoio utilizados nos experimentos do artigo:

***“Uma Comparação de Ferramentas Open Source de CLI para Geração de Ataques DDoS em Ambientes de Internet”***

O repositório também inclui a **tabela completa com a descrição das anomalias de tráfego** avaliadas no trabalho, disponível no arquivo ***ANOMALIAS (Descrições e Resultados).pdf***, localizado no diretório raiz do projeto.

**Artigo disponível em:** <link>

---

## Resumo do artigo

*Os ataques DDoS comprometem a disponibilidade de infraestruturas críticas de rede por meio de fluxos de dados massivos e coordenados. O uso de ferramentas de simulação de DDoS permite reproduzir esses comportamentos de forma controlada e segura, colaborando assim ao desenvolvimento de sistemas de segurança. Entretanto, há ainda uma carência de estudos comparativos que auxiliem na seleção de ferramentas quanto à fidelidade e ao desempenho. Este trabalho apresenta uma análise comparativa de sete ferramentas open source de linha de comando (CLI) voltadas à simulação de ataques DDoS nas camadas de rede e transporte. Essa avaliação experimental levou em conta a capacidade de geração de tráfego, a capacidade de customização e a aderência à taxonomia de Jelena Mirkovic para modelagem de anomalias. Os resultados alcançados apontam diferenças significativas entre as ferramentas, no qual a T50 favorece experimentos volumétricos, a Scapy a flexibilidade na modelagem de anomalias e a Trafgen um equilíbrio entre ambos aspectos.*

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

* `ANOMALIAS (Descrições e Resultados).pdf`  
  Documento com a **descrição das anomalias de tráfego avaliadas** e seus respectivos resultados.

* `server.py`  
  Servidor simples utilizado nos experimentos da anomalia de reflexão *TCP SYN Reflection*.

---

## Ferramentas avaliadas

Os experimentos envolvem ferramentas *open source* de linha de comando (CLI) que atuam nas camadas de rede e transporte, operam no sistema operacional Linux e não dependem de interação continua do usuário:

* BoNeSi — [GitHub](https://github.com/Markus-Go/bonesi)  
* Hping3 — [Debian Salsa](https://salsa.debian.org/debian/hping3) (instalado com `sudo apt install hping3`)
* Mausezahn — [GitHub](https://github.com/netsniff-ng/netsniff-ng)  
* Scapy — [Site oficial](https://scapy.net/) (instalado com `pip install scapy`)
* Tcpreplay — [GitHub](https://github.com/appneta/tcpreplay) (instalado com `sudo apt install tcpreplay`)
* Trafgen — [GitHub](https://github.com/netsniff-ng/netsniff-ng)  
* T50 — [GitLab](https://gitlab.com/fredericopissarra/t50)  

Cada ferramenta foi executada em seu código original, sem modificações, e sem scripts externos que pudessem contornar suas limitações, respeitando suas funcionalidades nativas. Além disso, não foram consideradas opções de construção manual de pacotes em modo *raw*. 

As ferramentas Hping3 e Mausezahn oferecem um modo de operação interativo, que não foi avaliado neste trabalho por estar fora do escopo do estudo.

---

## Observações importantes

* Este repositório **não deve ser utilizado para ataques reais**.
* Todo o conteúdo foi desenvolvido **exclusivamente para fins acadêmicos e experimentais**.
* Os códigos e comandos refletem exatamente os cenários avaliados no artigo, sem ajustes posteriores.
* A taxonomia de **Jelena Mirkovic** contribuiu para a análise da capacidade de geração de anomalias, sendo utilizada como principal referência. A análise incorporou diversos itens da lista da pesquisadora de forma integral, enquanto adaptou outros, descartou alguns por estarem fora do escopo e definiu novos a partir das capacidades de customização das ferramentas. Disponível em: [https://www.isi.edu/people-mirkovic/ddos-benchmarks/ddos-attack-list/](https://www.isi.edu/people-mirkovic/ddos-benchmarks/ddos-attack-list/)


---

## Citação

Se você utilizar este repositório em trabalhos acadêmicos, considere citar o artigo correspondente.
A entrada BibTeX será adicionada posteriormente.
