# omonorepo

**🇺🇸 [English](#english) | 🇧🇷 [Tupiniquim](#tupiniquim)**

*Made in Brazil 🇧🇷 · Feito no Brasil*

---

<a id="english"></a>

## English

**The normalizer for Omarchy plugins: it tells you what you already have, what
conflicts, and what each thing depends on.**

### Why we exist

The Omarchy marketplace has thousands of plugins (4,178 on 2026-09-26), and many of
them do the same thing: 228 deal with AI agents, 242 with battery and power, 172 with
clock, calendar and weather.

The marketplace validates **each plugin on its own**. Nobody validates **how plugins
relate to each other**. You only find out while using them that:

- you already had another plugin doing the same thing;
- two plugins fight over the same key, the same spot on the bar, or the same config file;
- a plugin needed something that was not there.

### What we solve

Before and after you install, omonorepo answers:

1. **Do I already have this?** Overlap with what is installed.
2. **Does it conflict with anything?** Keys, IPC, bar placement, config files.
3. **What does it depend on?** Tools, agents, other plugins.

For people who **write** plugins, it gathers the rules of Omarchy, of the marketplace
and our own stability rules, and checks every plugin in the series before it ships.
For people who **use** plugins, it maps what is installed and proposes a coherent setup.

We start with **AI agents**, the family with the least consistency today: every tool
opens agents its own way, the Herdr plugins only watch, and installers switch your
default agent without asking. Details in [PRODUCT.md](PRODUCT.md).

### The series

Each plugin has its own repository (the marketplace requires `manifest.json` at the
root) and joins this one as a submodule, with its docs and acceptance record.

| Plugin | What it does | Repository |
|---|---|---|
| **omany** (first in the series) | Makes agents consistent: all of them open in Herdr, one tab per agent, four predictable slots, and the Omarchy skill loaded on the first turn | [aiob3/omany](https://github.com/aiob3/omany) |
| **omaplug** | Omarchy plugin manager (our fork); where you see key conflicts today and conflicts between active plugins next | [aiob3/omaplug](https://github.com/aiob3/omaplug) |

#### omany at a glance

![omany panel next to Herdr](docs/omany/acceptance/preview.png)

| Key | Opens |
|---|---|
| Super+Ctrl+Shift+A | your default agent (Claude Code) |
| Super+Ctrl+Shift+Z | the other one (Codex) |
| Super+Ctrl+Shift+S / X | free slots, picked in the panel |

Tested in real use on 2026-09-25 and 26; the acceptance record is in
[docs/omany/acceptance](docs/omany/acceptance/README.md).

### Clone

```bash
git clone --recurse-submodules https://github.com/aiob3/omonorepo.git
```

---

<a id="tupiniquim"></a>

## 🇧🇷 Tupiniquim

**Uma solução brasileira.** O normatizador dos plugins do Omarchy: diz ao usuário o
que ele já tem, o que conflita e do que cada coisa depende.

### Por que existimos

O marketplace do Omarchy tem milhares de plugins (4.178 em 26/09/2026) e muitos fazem
a mesma coisa: 228 tratam de agentes de IA, 242 de bateria e energia, 172 de relógio,
calendário e clima.

O marketplace valida **cada plugin isolado**. Ninguém valida **a relação entre eles**.
Quem instala só descobre no uso que:

- já tinha outro plugin fazendo o mesmo;
- dois plugins disputam a mesma tecla, o mesmo lugar na barra ou o mesmo arquivo de
  configuração;
- um plugin dependia de algo que não estava lá.

### O que resolvemos

Antes e depois de instalar, o omonorepo responde:

1. **Eu já tenho isso?** Sobreposição com o que está instalado.
2. **Isso conflita com algo?** Teclas, IPC, barra, arquivos de configuração.
3. **Do que isso depende?** Ferramentas, agentes, outros plugins.

Para quem **escreve** plugins, ele reúne as regras do Omarchy, do marketplace e as
nossas de estabilidade, e confere cada plugin da série antes de publicar. Para quem
**usa**, ele mapeia o que está instalado e propõe uma configuração coerente.

Começamos pelos **agentes**, a família com menos uniformidade hoje: cada ferramenta
abre o agente de um jeito, os plugins do Herdr só observam, e os instaladores trocam o
agente padrão sem avisar. O detalhe (em inglês) está em [PRODUCT.md](PRODUCT.md).

### A série

| Plugin | O que faz | Repositório |
|---|---|---|
| **omany** (1º da série) | Uniformiza os agentes: todos abrem no Herdr, uma aba por agente, quatro vagas previsíveis e o skill do Omarchy no primeiro turno | [aiob3/omany](https://github.com/aiob3/omany) |
| **omaplug** | Gerenciador de plugins do Omarchy (nosso fork); onde o usuário vê conflitos de tecla e, em seguida, entre plugins ativos | [aiob3/omaplug](https://github.com/aiob3/omaplug) |

A homologação do omany (em inglês), feita no uso real em 25 e 26/09/2026, está em
[docs/omany/acceptance](docs/omany/acceptance/README.md).

### Como clonar

```bash
git clone --recurse-submodules https://github.com/aiob3/omonorepo.git
```
