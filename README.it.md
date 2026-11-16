# Longhand

Insegna al tuo assistente AI a scrivere di tuo pugno, partendo dai testi che hai scritto davvero. Funziona in ogni lingua.

[Read in English](README.md)

## Il problema

I testi scritti con l'AI si assomigliano tutti e chi legge se ne accorge alla prima riga. Gli strumenti che "tolgono l'AI" da un testo aiutano, ma lavorano per sottrazione: eliminano gli schemi tipici dei modelli e lasciano un testo pulito che non è di nessuno.

Per avere un testo tuo serve l'altra metà: un profilo di come scrivi tu. Dove metti il punto, quanto tagli, che parole usi, come saluti, quali figure retoriche ti vengono naturali, cosa non scriveresti mai.

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

1. **Raccoglie i campioni.** File che alleghi, testo che incolli, posta e documenti se li colleghi e dai il consenso.
2. **Li pesa.** Non tutti i testi valgono uguale: quelli recenti e molto ordinati potrebbero essere già passati dall'AI. Il campione migliore è una bozza scritta dall'AI insieme alla versione che hai riscritto a mano, perché mostra cosa togli, cosa aggiungi e cosa cambi.
3. **Scrive il profilo.** Solo tratti che compaiono almeno due volte nei tuoi testi.
4. **Lo prova con te.** Ti mostra due testi brevi scritti con la nuova skill e ti chiede cosa stona.
5. **Lo aggiorna.** Ogni volta che correggi un testo, la skill può imparare dalla correzione.

Due regole distinguono questo metodo da un elenco di frasi vietate. La prima: ciò che è tuo resta tuo. Se nei tuoi testi scritti a mano c'è uno schema che di solito si attribuisce all'AI, è la tua voce e non viene toccato. La seconda: la voce non coincide con lo scrivere bene. La skill non deve migliorarti, deve somigliarti (refusi esclusi).

## Installazione

Con un agente che supporta le skill, incolla:

```text
Installa la skill longhand da https://github.com/fdesimone/longhand
```

Oppure con `npx`:

```sh
npx skills add fdesimone/longhand --skill longhand --global --yes
```

Oppure a mano: copia la cartella `skills/longhand` nella cartella delle skill del tuo assistente. Nelle app che permettono di caricare skill, comprimi la cartella e caricala dalle impostazioni.

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

L'elenco degli schemi da evitare e l'idea del controllo finale partono da [no-ai-slop](https://github.com/petergyang/no-ai-slop) di Peter Yang (licenza MIT). Vedi [NOTICE.md](NOTICE.md).

## Licenza

MIT. Vedi [LICENSE](LICENSE).
