# Longhand

**Insegna al tuo assistente AI a scrivere con la tua voce.** Longhand è una skill per agenti che costruisce un profilo personale del tuo stile di scrittura a partire dai testi che hai scritto davvero, in qualsiasi lingua, così ciò che l'assistente scrive per te sembra scritto da te e non dall'AI.

[Read in English](README.md)

Un humanizer toglie l'AI da un testo. Longhand ci mette te.

## Esempio

Una richiesta, "chiedi al gruppo i commenti sul report entro venerdì", tre risultati. L'esempio è illustrativo.

**AI senza istruzioni:**

> Ciao a tutti, spero che questa mail vi trovi bene! Vi scrivo in merito al report del terzo trimestre. Vi sarei molto grato se poteste condividere i vostri commenti entro venerdì. Non esitate a contattarmi per qualsiasi chiarimento. Cordiali saluti

**Dopo aver tolto gli schemi dell'AI:**

> Ciao a tutti, mandatemi i commenti sul report del terzo trimestre entro venerdì. Grazie.

Pulito, ma potrebbe averlo scritto chiunque.

**Con un profilo Longhand** (qui, di una persona che scrive mail brevi, riparte in minuscola dopo il saluto, spiega il motivo di una scadenza e chiude con "grazie,"):

> Salve,
>
> allego la bozza del report aggiornata alla v_0.2. Vi chiedo di farmi avere i commenti entro venerdì così da chiudere prima del Board.
>
> grazie,
> Sam

## Cosa fa

`longhand` è una skill che ne costruisce un'altra, personale. Legge i tuoi testi, ricava il profilo della tua voce e lo salva come skill a sé (`stile-tuonome`). Da quel momento l'assistente la usa ogni volta che gli chiedi di scrivere a tuo nome.

La skill personale contiene:

- i tratti della tua voce, ognuno con un esempio preso dai tuoi testi;
- le parole, le formule e le figure retoriche che usi;
- le regole di punteggiatura della tua lingua e le tue preferenze;
- i registri (mail brevi, documenti, reclami, messaggi), con saluti e chiusure;
- gli schemi dell'AI che non ti appartengono;
- un controllo finale che l'assistente esegue prima di consegnarti il testo.

## Come funziona

Un modello linguistico scrive la cosa più probabile, quindi sceglie ciò che va bene per il maggior numero di lettori. Tu scegli per un lettore e per un argomento. Longhand registra quelle scelte.

1. **Raccoglie i campioni.** File che alleghi, testo che incolli, posta e documenti se li colleghi e dai il consenso.
2. **Li pesa.** Non tutti i testi valgono uguale: quelli recenti e molto ordinati potrebbero essere già passati dall'AI. Il campione migliore è una bozza scritta dall'AI insieme alla versione che hai riscritto a mano, perché mostra cosa togli, cosa aggiungi e cosa cambi.
3. **Scrive il profilo.** Solo tratti che compaiono almeno due volte nei tuoi testi.
4. **Lo prova con te.** Ti mostra due testi brevi scritti con la nuova skill e ti chiede cosa stona.
5. **Lo aggiorna.** Ogni volta che correggi un testo, la skill può imparare dalla correzione.

Due regole distinguono questo metodo da un elenco di frasi vietate. La prima: ciò che è tuo resta tuo. Se nei tuoi testi scritti a mano c'è uno schema che di solito si attribuisce all'AI, è la tua voce e non viene toccato. La seconda: la voce non coincide con lo scrivere bene. La skill non deve migliorarti, deve somigliarti (refusi esclusi).

## Longhand e gli humanizer

Strumenti come [Humanizer](https://github.com/blader/humanizer) sono molto bravi a trovare e togliere gli schemi dell'AI da un testo che hai già, e Humanizer sa anche seguire un campione di scrittura che incolli insieme al testo. Longhand fa un altro lavoro:

- costruisce il tuo profilo una volta sola, da molti testi, e lo conserva come skill da riusare;
- registra ciò che fai (saluti, formule, ritmo, registri) e non solo ciò che va evitato;
- lavora nella tua lingua, con un pacchetto di schemi e di regole di punteggiatura scritto apposta;
- si aggiorna quando correggi un testo.

Insieme funzionano bene: un humanizer ripulisce qualsiasi testo, Longhand fa nascere i testi già nella tua voce.

Longhand scrive per lettori in carne e ossa. Superare i rilevatori di testi AI non è un obiettivo.

## Installazione

In Claude Code, come plugin:

```text
/plugin install longhand --marketplace fdesimone/longhand
```

Con un agente che supporta le skill, incolla:

```text
Installa la skill longhand da https://github.com/fdesimone/longhand
```

Oppure con `npx`:

```sh
npx skills add fdesimone/longhand --skill longhand --global --yes
```

Oppure a mano: copia la cartella `skills/longhand` nella cartella delle skill del tuo assistente. Nelle app che permettono di caricare skill, comprimi la cartella e caricala dalle impostazioni.

Longhand è una skill standard in Markdown. Finora è stata provata con Claude.

## Uso

```text
/longhand
```

Oppure a parole: "impara il mio stile", "voglio che tu scriva come me". Tieni pronti una decina di mail, un paio di testi lunghi e, se puoi, una bozza dell'AI con la tua riscrittura.

## Lingue

Il metodo è lo stesso per ogni lingua. Cambiano gli schemi con cui l'AI si fa riconoscere e le regole di punteggiatura, che per questo stanno in pacchetti di lingua separati. Oggi ci sono l'italiano (`it`, con un profilo di esempio) e l'inglese (`en`).

Se la tua lingua non ha ancora un pacchetto la skill funziona lo stesso: ricava gli schemi da una bozza AI e dalla tua riscrittura. E puoi aggiungere tu il pacchetto per tutti gli altri.

## Aiutala a crescere

Il progetto migliora con ogni lingua e con ogni schema che qualcuno aggiunge. I contributi più utili:

- **un nuovo pacchetto di lingua**: due file, scritti da chi quella lingua la parla, a partire dagli scheletri in `skills/longhand/languages/_template/`;
- **uno schema in più** per una lingua che ha già il pacchetto: basta una voce per una pull request;
- **una segnalazione** di un profilo che non ti somigliava, con ciò che hai dovuto correggere.

Le istruzioni sono in [CONTRIBUTING.md](CONTRIBUTING.md) (in inglese). La skill stessa propone di preparare un contributo quando trova schemi che al pacchetto mancano, sempre con esempi inventati e mai con i tuoi testi.

## Riservatezza

- La skill legge posta e documenti solo se glielo chiedi e solo quanto serve.
- Nella skill personale non entrano dati personali, nomi di terzi né passaggi di documenti riservati.
- Il profilo resta tuo: questo repository contiene il metodo, non i profili di chi lo usa.
- La skill costruisce il profilo di chi la usa. Non serve a imitare altre persone.

## Limiti

Il metodo è nato costruendo il profilo di una sola persona ed è stato generalizzato da lì. Funziona meglio con più campioni e con almeno una coppia bozza e riscrittura. Segnalazioni e correzioni sono benvenute.

## Crediti

Gli elenchi di schemi partono da [no-ai-slop](https://github.com/petergyang/no-ai-slop) di Peter Yang e da [Humanizer](https://github.com/blader/humanizer) di Siqi Chen, entrambi con licenza MIT, e attraverso di loro dalla pagina di Wikipedia [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Vedi [NOTICE.md](NOTICE.md).

## Licenza

MIT. Vedi [LICENSE](LICENSE). Le modifiche sono elencate in [CHANGELOG.md](CHANGELOG.md).

Se Longhand ti è utile, una stella aiuta altre persone a trovarla.
