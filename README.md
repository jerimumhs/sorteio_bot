# Como usar

Primeiro, precisa gerar o API_ID e API_HASH no site https://my.telegram.org ;
Depois, pegar o API_TOKEN do seu bot com o @BotFather ;

Com os dados em mãos, vamos editar o arquivo `config.json.sample`. Faça uma copia dele e o renomei deixando apenas `config.json` e lá coloque as credenciais adquiridas em `user` e `bot`. Em `group`, é necessario que coloque o nome do grupo em que o sorteio vai acontecer e os IDs das pessoas autorizadas a rodar o comando `/sorteio`.

O bot deve ser colocado no grupo especificado anteriormente e lá ser enviado o comando. A pessoa quem vai rodar o sistema do sorteio e utilizar suas credenciais, tem que está participando do grupo desde a hora da configuração, para que não haja problemas.

Os comandos são restritos tanto aos usuarios listados como ao grupo, não sendo possivel executar o comando por outras pessoas e/ou em outros grupos.

Para configurar o ambiente basta instalar as dependencias listadas no arquivo requirements.txt com o comando `pip install -r requirements.txt` e depois executar o script `run_bot.py`.

A primeira vez que o script for rodado, ele irá fazer uma autenticação do usuario, parecida com a que fazemos nos clientes com interface gráfica, isso gerará uma session com o nome que foi colocado no arquivo de configurações. Caso seja aut. 2 fatores, ele pedirá a senha para validar tambem.