# Web-scraping-capital-social

Este projeto automatiza a captura do captal social das empresas, no site casadosdados.com.br, capturando também a razão social e o CNPJ para identificar cada valor capturado.
Ele consome um CSV com um digito a mais no inicio do CNPJ que a propria automação retira servindo para segurar os zeros a esquerda portanto adicione a sua base de dados este numero a mais, duas colunas ''nome'' e ''cnpj'' mas se o CSV possuir apenas uma coluna ''cnpj'' vai funcionar, o valor da coluna do csv vai ser combinado com outra variável cada vez que o loop for excutado para criar as URL's de consulta nos sites dentro do navegador que esta automação abre.
Então a automação seleciona os valores desejados copia-os, e guarda dentro das variáveis, posteriormente coloca os valores em uma lista, fecha o navegador utilizado para não sobrecarregar o processamento da máquina, por ultimo ele abre um arquivo CSV no local desejado, e preenche os dados capturados no mesmo.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/SEU USUARIO/Web-scraping-capital-social.git
    cd ecf_automation
    pip install -r requirements.txt
    ```

## Requerimentos

1. Configure a resolução = 1366x768 100%
2. Se você utiliza barra do windows móvel, configure-a como fixa
3. Configure como navegador padrão no windows o google chrome


## Uso

1. **Execute Web-scraping-capital-social na sua IDE**
    ```bash
    python app.py
    ```


## Dependências

- Python 3.x
- pyautogui
- pandas
- time
- webbrowser
- pyperclip
- csv

Certifique-se de que todas as dependências estão listadas no arquivo `requirements.txt`.

## Updates

1. Inclusão de uma interface para exibir a mensagem de conclusão do processo.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para o branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob direitos reservados ao autor.






