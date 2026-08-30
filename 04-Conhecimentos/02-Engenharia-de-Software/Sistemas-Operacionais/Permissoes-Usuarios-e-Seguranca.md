---
title: "Permissões, Usuários e Segurança em S.O."
date: 2026-07-07
updated: 2026-07-07
type: knowledge
status: active
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
tags: [permissoes, usuarios, seguranca, windows, linux, acl, hardening]
summary: "Base sobre usuários, grupos, permissões, ACLs e segurança operacional em Windows e Linux."
---

# Permissões, Usuários e Segurança em S.O.

Permissão é a fronteira entre operação e desastre. Dominar S.O. exige saber **quem executa**, **com quais privilégios** e **sobre qual recurso**.

## Conceitos centrais

| Conceito | Significado |
|---|---|
| Usuário | identidade que executa ações |
| Grupo | conjunto de usuários com permissões compartilhadas |
| Privilégio | capacidade especial do sistema |
| Permissão | regra sobre arquivo, pasta, processo ou recurso |
| ACL | lista detalhada de controle de acesso |
| Elevação | execução com permissões administrativas |

## Windows - identidade e grupos

```bat
whoami
whoami /groups
net user
net localgroup
```

PowerShell:

```powershell
Get-LocalUser
Get-LocalGroup
```

## Windows - inspeção de permissões

Interface gráfica:

```txt
Propriedades do arquivo > Segurança
```

PowerShell:

```powershell
Get-Acl .\arquivo.txt
Get-Acl .\pasta
```

CMD:

```bat
icacls arquivo.txt
icacls pasta
```

## Linux - identidade e grupos

```bash
whoami
id
groups
who
w
last
getent passwd usuario
getent group grupo
```

## Linux - inspeção de permissões

```bash
ls -l
ls -ld pasta
stat arquivo.txt
umask
```

Formato comum:

```txt
-rw-r--r-- 1 usuario grupo 1234 jul 07 10:00 arquivo.txt
```

Interpretação:

| Bloco | Significado |
|---|---|
| primeiro caractere | tipo: arquivo, diretório, link |
| primeiro trio | permissões do dono |
| segundo trio | permissões do grupo |
| terceiro trio | permissões de outros |

## Números comuns no Linux

| Valor | Uso comum |
|---:|---|
| 600 | arquivo privado |
| 644 | arquivo legível por todos, editável pelo dono |
| 700 | diretório privado |
| 755 | executável ou diretório acessível |
| 775 | projeto compartilhado por grupo |

## Princípio do menor privilégio

Usuário ou serviço deve ter apenas o acesso necessário para executar sua função.

Aplicações práticas:

- serviço web não deve rodar como usuário administrativo sem necessidade;
- arquivos de configuração sensíveis devem ter leitura restrita;
- diretórios de upload não devem executar arquivos quando possível;
- automações devem usar contas próprias;
- mudanças recursivas exigem revisão de escopo.

## Sinais de problema de permissão

| Sintoma | Possível causa |
|---|---|
| Access denied | usuário sem permissão |
| Permission denied | usuário ou grupo incorreto no Linux |
| serviço não lê configuração | dono/permissão incompatível |
| app funciona localmente e falha em produção | usuário de execução diferente |
| script roda manualmente e falha agendado | ambiente e usuário diferentes |

## Checklist para problema de permissão

1. Qual usuário executa o processo?
2. Qual arquivo ou pasta está falhando?
3. Qual permissão atual?
4. Qual dono/grupo atual?
5. O serviço usa outro usuário?
6. Existe ACL extra?
7. A aplicação precisa ler, escrever ou executar?
8. A mudança pode ser restrita ao menor escopo?
9. Há log confirmando erro de permissão?
10. Como validar após ajuste?

## Anti-padrões

- liberar permissão ampla para resolver pressa;
- alterar diretórios inteiros sem mapear impacto;
- rodar serviço como usuário administrativo por conveniência;
- ignorar diferença entre usuário interativo e usuário do serviço;
- não registrar mudança de permissão.

## Modelo mental

Permissão é catraca de prédio. Se todo mundo tem chave mestra, ninguém sabe quem entrou. Se ninguém tem chave, o prédio para. Administração boa é chave certa, porta certa, horário certo. 🔐
