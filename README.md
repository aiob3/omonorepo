# omonorepo

Casa dos nossos projetos para o [Omarchy](https://omarchy.org) com o
[Herdr](https://github.com/herdrdev/herdr): Claude Code e Codex trabalhando lado a
lado, com o Herdr como interface agêntica.

Cada plugin tem repositório próprio, porque o marketplace do Omarchy exige o
`manifest.json` na raiz do repositório. Aqui eles entram como submódulos, junto
com a documentação e a homologação de cada um.

## Plugins

| Plugin | O que faz | Repositório |
|---|---|---|
| **omany** | Abre o agente padrão do Omarchy dentro do Herdr: um workspace, uma aba nova por tecla, painel na barra e o skill do Omarchy carregado no primeiro turno | [aiob3/omany](https://github.com/aiob3/omany) |
| **omaplug** | Gerenciador de plugins do Omarchy (nosso fork, com seleção de atualizações) | [aiob3/omaplug](https://github.com/aiob3/omaplug) |

## omany em uma imagem

![Painel do omany ao lado do Herdr](docs/omany/homologacao/preview.png)

| Tecla | Abre |
|---|---|
| Super+Ctrl+Shift+A | o agente padrão (Claude Code) |
| Super+Ctrl+Shift+Z | o outro (Codex) |
| Super+Ctrl+Shift+S / X | vagas livres, escolhidas no painel |

A homologação, feita no uso real em 25 e 26/09/2026, está em
[docs/omany/homologacao](docs/omany/homologacao/README.md).

## Como clonar

```bash
git clone --recurse-submodules https://github.com/aiob3/omonorepo.git
```
