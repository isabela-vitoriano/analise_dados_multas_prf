# Análise de Dados de Multas da PRF

Este projeto tem como objetivo realizar a coleta, consolidação e análise exploratória dos dados de multas da Polícia Rodoviária Federal (PRF). Os dados são obtidos a partir do site oficial da PRF, onde os arquivos CSV contendo as informações das multas são disponibilizados.

## Descrição

Os dados são coletados do site oficial da PRF, especificamente da seção de "Dados Abertos". O scraping é feito utilizando bibliotecas como requests, BeautifulSoup e gdown para realizar o download dos arquivos CSV das multas. Após o download, os arquivos são consolidados e organizados para análise exploratória.

## Status do projeto

Versão 1.0

## Tecnologias Utilizadas

Python 3.9.13 | Bibliotecas: pandas, numpy, requests, beautifulsoup4, matplotlib, plotly, zipfile, os, shutil

## Como usar

1. Clone o repositório em sua máquina local.
2. Certifique-se de ter as dependências instaladas. Caso não tenha, instale-as utilizando o gerenciador de pacotes pip.
3. Execute o arquivo `baixando_bases.py` para realizar o scraping e download dos arquivos CSV das multas, o que vai gerar uma pasta chamda "arquivos_extraidos".
4. Após a conclusão do scraping, execute o arquivo `consolidando_base.ipynb` para consolidar os dados em uma única base parquet, chamada Base_Consolidada.parquet, e prepará-los para a análise exploratória.
5. Utilize o arquivo `analise_exploratoria.ipynb` para realizar a análise exploratória dos dados de multas.

## Importância da Análise de Dados de Multas da PRF

A análise de dados das multas da PRF desempenha um papel fundamental na identificação de padrões de infrações, veículos mais comumente envolvidos, locais de maior incidência de multas e outros insights valiosos. Essas informações podem auxiliar na implementação de medidas de segurança viária mais eficazes, no planejamento de campanhas de conscientização e na elaboração de políticas públicas voltadas para a redução de infrações e acidentes nas estradas.

## Dados Disponíveis

Os dados utilizados neste projeto são disponibilizados pela PRF e podem ser encontrados no seguinte link: [Dados Abertos da PRF](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf)

## Dicionários das variáveis

| Nome Atual                         | Descrição                                        |
|------------------------------------|--------------------------------------------------|
| Número do Auto                     | Identificador único do auto de infração          |
| Data da Infração (DD/MM/AAAA)      | Data da infração no formato dd/mm/aaaa           |
| Indicador de Abordagem             | Identifica se houve abordagem do veículo         |
| Assinatura do Auto                 | Informa se o infrator assinou o auto de infração |
| Indicador Veiculo Estrangeiro      | Informa se o veículo é estrangeiro               |
| Sentido Trafego                    | Sentido da via onde ocorreu a infração           |
| UF Placa                           | Unidade federativa da placa do veículo           |
| UF Infração                        | Unidade federativa do local da infração          |
| BR Infração                        | Identificador da BR onde ocorreu a infração      |
| Km Infração                        | Identificação do quilômetro da infração          |
| Município                          | Nome do município onde ocorreu a infração        |
| Código da Infração                 | Não há correspondência                           |
| Descrição Abreviada Infração       | Descrição abreviada da infração                  |
| Enquadramento da Infração          | Enquadramento da infração de acordo com o CTB    |
| Início Vigência da Infração        | Data do início da vigência da infração           |
| Fim Vigência Infração              | Data do fim da vigência da infração              |
| Medição Infração                   | Registro da medição realizada                    |
| Descrição Especie Veículo          | Espécie do veículo                               |
| Descrição Marca Veículo            | Marca do veículo                                 |
| Hora Infração                      | Horário em que ocorreu a infração                |
| Medição Considerada                | Medição considerada para o registro da infração  |
| Excesso Verificado                 | Excesso verificado nas infrações                 |
| Qtd Infrações                      | Quantidade de infrações (sempre 1)               |
| Descrição Tipo Veículo             | Espécie do veículo                               |
| Descrição Modelo Veiculo           | Modelo do veículo                                |

## Contato

Desenvolvedora do Projeto: Isabela Vitoriano

• Linkedin: [https://www.linkedin.com/in/isabela-vitoriano/](https://www.linkedin.com/in/isabela-vitoriano/)

• E-mail: [isabelavitoriano.ss@gmail.com](isabelavitoriano.ss@gmail.com)
