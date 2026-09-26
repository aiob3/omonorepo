# Homologação do omany

Feita no uso real, em 25 e 26/09/2026, numa estação Omarchy com Hyprland 0.56,
Herdr 0.8.2, Claude Code 2.1.283 e Codex 0.157. Regra do teste: o operador aperta
a tecla ou clica, e o assistente confirma pelo log (`~/.local/state/omany.log`) e
pelo estado do Herdr. Nada de teste automático.

## O que foi homologado

| Recurso | Resultado |
|---|---|
| Super+Ctrl+Shift+A abre o agente padrão no Herdr, aba nova a cada tecla, uma janela só | aprovado |
| Super+Ctrl+Shift+Z abre o outro agente (Claude Code ↔ Codex) | aprovado |
| Super+Ctrl+Shift+S / X abrem os agentes escolhidos para as vagas | aprovado (Copilot, Grok) |
| Vaga vazia avisa e não abre nada | aprovado |
| Skill do Omarchy no primeiro turno (`/omarchy` no Claude, `$omarchy` no Codex) | aprovado |
| Ícone na barra, logo depois do relógio | aprovado |
| Painel: vagas com seletor, Open, agentes rodando com Focus, instalados | aprovado |
| Configurações: posição, workspace, pasta com Save, skill | aprovado |
| Reset para instalação nova, com confirmação em dois cliques | aprovado |

## Problemas encontrados e corrigidos no caminho

- **Janela avulsa:** o atalho original do Omarchy abria o agente fora do Herdr.
- **Enter do Codex:** o `$` abre o menu de skills e o primeiro Enter só escolhe o item.
- **Partida a frio:** com o servidor do Herdr desligado, a janela precisa abrir antes dos comandos.
- **Ícone invisível:** o widget sem `implicitWidth` ficava com largura zero na barra.
- **"File name case mismatch":** cache de diretório do Qt; resolve com `omarchy restart shell`.
- **Plugin "ativo" sem ícone:** entrada residual em `plugins[]` do `shell.json`.
- **Agentes que o Herdr não reconhece** (OpenClaw, Crush, Muse): abrem como comando comum numa aba.
- **Stubs de instalação:** alguns agentes instalam no primeiro uso; o painel lê o arquivo e nunca executa.
- **Grok sem nome:** uma nova tentativa encontrava o agente já rodando; agora ele só recebe o nome.
- **Viés do Omarchy:** instalar um agente pelo menu o torna o padrão; a vaga A do omany pode ficar independente.

## Prints

| Prévia | Painel | Configurações | Herdr |
|---|---|---|---|
| ![](preview.png) | ![](panel.png) | ![](settings.png) | ![](herdr.png) |
