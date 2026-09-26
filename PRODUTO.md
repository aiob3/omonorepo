# omonorepo: o produto

## O problema

O marketplace do Omarchy cresceu rápido: **4.178 plugins** no catálogo de 26/09/2026.
Muitos fazem a mesma coisa, e nada ajuda o usuário a decidir entre eles:

| Família | Plugins no catálogo |
|---|---|
| Agentes de IA (agent, Claude, Codex, Herdr) | 228 |
| só Herdr | 29 |
| Relógio, calendário, clima | 172 |
| Bateria e energia | 242 |

O marketplace valida **cada plugin isolado**: o manifest, uma varredura de segurança
estática do commit e um checklist de submissão. Ele **não valida a relação entre
plugins**. Quem instala não fica sabendo:

- o que **já tem** que faz a mesma coisa (sobreposição);
- o que vai **brigar** com o que já está instalado (conflito): a mesma tecla, o mesmo alvo
  de IPC, o mesmo lugar na barra, dois plugins mexendo no mesmo arquivo de configuração;
- o que **depende** do quê (relação): um plugin que precisa do Herdr, de um agente, de
  outro plugin.

O resultado é um sistema que acumula funções repetidas e comportamentos que se
atropelam, e o usuário só descobre no uso.

## A proposta

O omonorepo é o **normatizador** do que está instalado. Ele responde três perguntas
antes e depois de instalar:

1. **Eu já tenho isso?** Sobreposição de função com o que está instalado.
2. **Isso conflita com algo?** Teclas, IPC, posição na barra, arquivos de configuração.
3. **Do que isso depende?** Ferramentas, agentes e outros plugins.

Ele trabalha em duas frentes:

- **Para quem escreve plugins (conformidade):** as regras do Omarchy, do marketplace e
  as nossas de estabilidade, com uma verificação que todo plugin da série passa antes
  de publicar. Ver [`conformidade/`](conformidade/).
- **Para quem usa (normatização):** ler os plugins instalados, mapear sobreposições,
  conflitos e dependências, e propor uma configuração coerente.

## Por onde começamos: agentes

Agentes são a família em que a falta de uniformidade mais pesa. Cada ferramenta abre
o agente do seu jeito: o atalho padrão do Omarchy abre uma janela solta, os plugins
do Herdr só observam, os instaladores trocam o agente padrão sem avisar.

O **omany**, primeiro app da série, uniformiza isso:

- todo agente abre no mesmo lugar (um workspace do Herdr, uma aba por agente, uma janela só);
- quatro vagas previsíveis (A padrão, Z o par, S e X livres), com a mesma regra para todos;
- o agente já nasce com o contexto do sistema (skill do Omarchy no primeiro turno);
- o painel mostra o que está instalado e o que só instala no primeiro uso, sem executar nada.

Os próximos passos dessa frente são mostrar quando outro plugin de agentes já está
instalado e o que ele faz de igual ao omany, e unificar a escolha do agente padrão
entre o Omarchy e os plugins.

## Relação com o omaplug

O omaplug (nosso fork do gerenciador de plugins) já lida com conflito de tecla ao
atribuir atalhos. O item nº 1 do nosso backlog nele é **"conflito entre plugins
ativos"**. É a mesma frente vista pelo gerenciador: o omonorepo define as regras e o
mapa de relações, e o omaplug é um dos lugares onde o usuário as vê.
