<div align="center">

<br/>

```
╔══════════════════════════════════════╗
║   🍔  CARDÁPIO DIGITAL  🍔          ║
╚══════════════════════════════════════╝
```

# Cardápio Digital 🍽️

> Sistema simples de pedidos via terminal — escolha seu lanche, bebida ou sobremesa e saiba o valor na hora!

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-22c55e?style=for-the-badge)
![Terminal](https://img.shields.io/badge/Interface-Terminal-111827?style=for-the-badge&logo=windowsterminal&logoColor=white)

</div>

---

## 📋 Sobre o Projeto

O **Cardápio Digital** é um sistema de pedidos desenvolvido em Python que roda diretamente no terminal. O usuário navega por um menu interativo, escolhe a categoria desejada (lanche, bebida ou sobremesa), seleciona o item e informa a quantidade — o sistema calcula o valor total automaticamente.

Ideal para quem está aprendendo lógica de programação, estruturas condicionais e o comando `match/case` do Python 3.10+.

---

## 🗂️ Estrutura do Menu

```
📦 Cardápio
├── 🌭  [1] Lanche
│   ├── Cachorro Quente ........... R$ 20,00
│   └── Hambúrguer ................ R$ 30,00
│
├── 🥤  [2] Bebida
│   ├── Refrigerante .............. R$ 12,00
│   └── Suco ...................... R$  6,00
│
├── 🍰  [3] Sobremesa
│   ├── Sorvete ................... R$ 15,00
│   └── Bolo ...................... R$  8,00
│
└── 🚪  [4] Sair
```

---

## ⚙️ Como Executar

**Pré-requisito:** Python 3.10 ou superior instalado na máquina.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/cardapio-digital.git

# Acesse a pasta do projeto
cd cardapio-digital

# Execute o programa
python main.py
```

---

## 🖥️ Exemplo de Uso

```
[1] Lanche
[2] Bebida
[3] Sobremesa
[4] Sair
Escolha uma opcao: 1

[1] Cachorro quente: 20R$
[2] Hamburguer: 30R$
Escolha um dos lanches: 2
Quantos você deseja? 3
Você terá que pagar 90R$
```

---

## 🧠 Conceitos Utilizados

| Conceito | Descrição |
|---|---|
| `match / case` | Estrutura condicional moderna do Python 3.10+ para navegar pelo menu principal |
| `if / elif / else` | Validação das escolhas dentro de cada categoria |
| `input()` | Captura das escolhas e quantidades digitadas pelo usuário |
| `int()` | Conversão das entradas para número inteiro |
| `f-strings` | Formatação dinâmica dos valores totais na saída |

---

## 🛠️ Tecnologia

<div align="center">

<br/>

<table>
  <tr>
    <td align="center" width="160">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" height="60" alt="Python"/>
      <br/>
      <strong>Python</strong>
      <br/>
      <sub>v3.10+</sub>
      <br/><br/>
      <img src="https://img.shields.io/badge/-Linguagem%20Principal-3776AB?style=flat-square&logo=python&logoColor=white"/>
    </td>
  </tr>
</table>

<br/>

</div>

---

## 📁 Estrutura de Arquivos

```
cardapio-digital/
└── main.py       # Arquivo principal com toda a lógica do sistema
```

---

## 🚀 Possíveis Melhorias Futuras

- [ ] Permitir escolher múltiplos itens no mesmo pedido
- [ ] Calcular troco com base no valor pago
- [ ] Salvar histórico de pedidos em arquivo `.txt`
- [ ] Adicionar interface gráfica com `tkinter`
- [ ] Criar versão web com Flask

---

<div align="center">

Feito com ❤️ e Python

</div>
