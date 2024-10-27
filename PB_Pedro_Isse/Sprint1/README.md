# Resumo

## **Git e GitHub:**

### **Controle de Versão:** 
- Uma técnica que ajuda a gerenciar o código-fonte de uma aplicação, registrando todas as modificações de código, também podendo reverter essas modificações. Ou seja, criar versões de um software em diferentes estágios.

### **Git:**
- Sistema de controle de versão mais utilizado no mundo, é baseado em repositórios que contêm todas as versões do código. É muito otimizado, protegidos com criptografia e possui código aberto.

### **Comandos essênciais:** 

**Inicialização e configuração:**
	- git init
	- git remote
	- git clone

- **Controle de versão:**
	- git add 
	- git commit
	- git branch
	- git tag

- **Sincronização:**
	- git pull
	- git push

- **Manipulação de Arquivos e Branches:**
	- git rm
	- git mv
	- git checkout

- **Gerenciamento de Alterações e Conflitos:**
	- git merge
	- git rebase
	- git stash
	- git reset

- **Manutenção de Repositório:**
	- git gc
	- git reflog
	- git shortlog
	- git gc
	- git fsch

### **Padronização de commits:**
- Commits sem sentido atrapalham o projeto, por isso, precisa-se padronizar os commits, para que o projeto cresça de forma saudável. Melhora o review do pull request, dos logs em git log e manutenção do código. 
- Boas mensagens de commit separam o assunto do corpo do texto, com no máximo 50 caracteres no Assunto e 72 caracteres no Corpo.

### **GitHub:**
- Code
- Issues
- Pull Request
- Actions
- Projects
- Security
- Insights
- Settings
- MarkDown

## **Linux para Desenvolvedores:**

### **Linux:**
- Aprendi o que são distribuições do linux, e as que normalmente utilizamos em ambientes de trablho. 
- Aprendi sobre o Kernel do Linux, que ele é o core do sistema que se comunica com o hardware.

### **Terminal x Shell:**
- O terminal é uma janela que recebe comandos e retorna a execução do shell.
- O shell executa os comando do terminal e devolve a saída para ele, é executado dentro do diretório "bin".

### **Estrutura de diretórios do Linux:**
![EstruturaDiretórios](/Assets/EstruturaDiretorios.jpg)

### **Comandos essências:**
- cd
    - Caminhos relativos e absolutos
- ls
    - Paramêtros (e.g. -l, -a, -lh...)
- cat 
- touch
- man
- cp 
- mv 
- pwd
- mkdir
- rm e rmdir
    - Paramêtros (e.g. -i, -dr, -p...)
- find
    - Paramêtros (e.g. -name, -iname, -empty...)
- locate
- sudo
- witch
- tail, head e grep 

### **Gerenciamento de Pacotes:**
- Atualizar repositórios: sudo apt-get update
- Atualizar pacotres/aplicativos: sudo apt-get upgrade
- Instalando pacotes/aplicativos: sudo apt-get install <pacote>
- Deletando pacotes/aplicativos: sudo apt-get purge <pacote>
- Atualizar Linux: sudo apt-get dist-upgrade
- Limpando pacotes desnecessários: sudo apt-get autoremove
- Buscando aplicaitvo: apt-cache search <pacote>

### **Editores de texto:**
- Nano
    - Alguns de seus atalhos (e.g. Crtl + O, Crtl + X, Crtl + C...) e seu funcionamento
- Vim 
    - Alguns de seus atalhos (e.g. Crtl + R, u, dd...), seus modos (Normal, inserção, comando e visual) e seu funcionamento

### **Gerenciamento de Permissões:**    
- "-' significa arquivo "d" diretório
- "r" - permissão de leitura
- "w" - permissão de escrita
- "x" - permissão de execução
- Formato: 1 (Arquivo ou Diretório) 222 (Permissões de dono) 333 (Permissões de grupo) 444 (Permissões de Usuário)
- Comando: chmod <num.permissão.dono><num.permissão.grupo><num.permissão.usuário>
- Alterando proprietário:
    - sudo chow <novodono> <arquivo>
    - sudo chow <novodono>:<novogrupo> <arquivo>
- Alterando o grupo do arquivo:
    - sudo chgrp <novogrupo> <arquivo>

### **Gerenciamento de Usuários e grupos:**
- Grupos contém vários usuários, assim facilita o gerenciamento de permissões.
- Adicionando Usuários: sudo adduser <user>
- Deletando Usuários: sudo userdel --remove <user>
- Mudando nome do usuário
    - Display: sudo usermod -c <novo_nome> <user>
    - Diretório base: sudo usermod -l <novo_nome> -d /home/<novo_nome> -m <user>
- Bloqueando e Desbloqueando Usuários:
    - Bloq: sudo usermod -L <user>
    - Unbloq: sudo usermod -U <user>

### **Gerenciamento básico de redes:**

1. Envio de requisição de domínio (Domain Name System)
2. Verificação de domínio (DNS = IP)
3. Requisição da resposta para o servidor que pertence a este domínio
4. Retorno da resposta a quem solicitou

- Entendimento individual de:
    - DNS
    - Portas
    - TCP
    - UDP

___

# Exercícios

Nesta Sprint não foram fornecidos [Exercícios](/PB_Pedro_Isse/Sprint1/Exercicios) para resolução!

___

# Evidências


1. Criação da pasta [ecommerce](/PB_Pedro_Isse/Sprint1/Evidencias/ecommerce) com o arquivo [dados_de_vendas.csv](/PB_Pedro_Isse/Sprint1/Evidencias/ecommerce/dados_de_vendas.csv)

2. Criação do [processamento_de_vendas.sh](/PB_Pedro_Isse/Sprint1/Evidencias/processamento_de_vendas.sh) e programando data e horário de execução com o [crontab](/PB_Pedro_Isse/Sprint1/Evidencias/crontab.png). 

- Geração de relatórios:

	- [Relatório 2024/10/22](/PB_Pedro_Isse/Sprint1/Evidencias/vendas/backup/relatorio-20241022.txt)
	- [Relatório 2024/10/23](/PB_Pedro_Isse/Sprint1/Evidencias/vendas/backup/relatorio-20241023.txt) 
	- [Relatório 2024/10/24](/PB_Pedro_Isse/Sprint1/Evidencias/vendas/backup/relatorio-20241024.txt)
	- [Relatório 2024/10/25](/PB_Pedro_Isse/Sprint1/Evidencias/vendas/backup/relatorio-20241025.txt)

- Geração de backups compactados:

	- [Backup de dados 2024/10/22](/PB_Pedro_Isse/Sprint1/Evidencias/vendas/backup/backup-dados-20241022.zip)
	- [Backup de dados 2024/10/23](/PB_Pedro_Isse/Sprint1/Evidencias/vendas/backup/backup-dados-20241023.zip)
	- [Backup de dados 2024/10/24](/PB_Pedro_Isse/Sprint1/Evidencias/vendas/backup/backup-dados-20241024.zip)
	- [Backup de dados 2024/10/25](/PB_Pedro_Isse/Sprint1/Evidencias/vendas/backup/backup-dados-20241025.zip)

3. Criação do [consolidador_de_processos.sh](/PB_Pedro_Isse/Sprint1/Evidencias/consolidador_de_processamento.sh) e geração do [relatorio_final.txt](/PB_Pedro_Isse/Sprint1/Evidencias/vendas/backup/relatorio_final.txt)

#### **Elaboração do [Desafio](/PB_Pedro_Isse/Sprint1/Desafio/README.md)**

___

# Certificados


### **Certificado do curso: Linux para Desenvolvedores (c/ terminal , Shell, Apache e +):**

![Certificado Linux](/PB_Pedro_Isse/Sprint1/Certificados/CursoLinux.jpg)

### **Certificado do curso: Git e GitHUb do básico ao avançado (c/ gist e GitHub Pages)**

![Certificado Git e GitHub](/PB_Pedro_Isse/Sprint1/Certificados/CursoGitGitHub.jpg)

