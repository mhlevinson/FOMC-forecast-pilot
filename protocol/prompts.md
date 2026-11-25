# Prompts (protocol v5, frozen 25 Nov 2026; see `FREEZE.md`)

The forecasting wording below is fixed before the dress rehearsal. After the rehearsal only mechanics may change, and every change is listed.

Text in {braces} is filled in by the runner from `questions.md` and the checkpoint record. Nothing else is added to any prompt.

## Answer format (shared by every model arm)

> Whatever else you write, end your final answer with one line that starts with the word FORECAST and gives your probability for each outcome as a percentage to one decimal place. The five percentages must sum to 100 and none may be 0 or 100. The line must have exactly this shape, with your numbers in place of the letters: "FORECAST | cut50=A ; cut25=B ; hold=C ; hike25=D ; hike50=E". Here cut50 means a cut of 50 basis points or more, cut25 a cut of 25, hold no change, hike25 a hike of 25, and hike50 a hike of 50 or more. Write the line once.

The shape is given inside a sentence and with letters, not numbers, so that it cannot be mistaken for a forecast and cannot suggest one.

## Fable arm (ten independent calls; the first is F1)

Dispatch: one fresh context per call, model Fable, effort high. The evidence pack is provided as a file.

> You are one of several independent forecasters. Work alone and only from the evidence pack.
>
> QUESTION
> {question text}
>
> EVIDENCE
> The evidence pack is the single file {pack path}. Read all of it before you answer. It contains official documents only, captured at {cutoff time}. Read no other file. Use no web search and no browser. Ask no one anything.
>
> HOW TO WORK
> 1. Say what the Committee did at its recent meetings and what its own documents and members signal about this one.
> 2. Say what the latest official data in the pack show on inflation, employment and activity, and which way each pushes.
> 3. For each of the five outcomes, give the strongest case that it happens.
> 4. Say what you are least sure of, and how that widens or narrows your probabilities.
> 5. Give your probabilities.
>
> ANSWER FORMAT
> {answer format}
>
> DELIVERY
> Write your whole answer, ending with the FORECAST line, to the file {answer path}. Use your tools only to read the evidence pack and to write that one file. Then reply with the single word DONE.

## Deliberate arm

Run settings: Deliberate 0.5.0; lock mode auto; probe policy closed; loop type descriptive; adversarial no; audit light; one attack cycle; intake off; both window budgets 0; default model settings. The corpus is the evidence pack and nothing else.

Starting claim, which lock mode auto commits word for word as the question every call works on:

> At its {meeting dates} meeting the FOMC will {claim wording}, measured as the change in the upper bound of the federal funds target range in the statement released after the meeting compared with the upper bound in effect immediately before it. {answer format}

Claim wording by outcome key:

| Key | Claim wording |
|---|---|
| `hold` | leave the target range unchanged |
| `hike25` | raise the target range by 25 basis points |
| `hike50` | raise the target range by 50 basis points or more |
| `cut25` | lower the target range by 25 basis points |
| `cut50` | lower the target range by 50 basis points or more |

The scored run uses the starting claim set by the rule in `questions.md`. At K1-K4, J1, J2 and J6 the twin run (diagnostic, unscored, amendment 29) uses the same settings and wording with the twin claim from `questions.md`. Which run is scored is recorded before either is dispatched.

The elicitation step below is run on the twin's final call too, with its own file paths.

The forecast is read by `forecast_tools.parse_forecast` from the file the elicitation step writes, and from nothing else (amendment 15).

## Elicitation step (part of the Deliberate arm, amendment 15)

The arm is named "Deliberate plus elicitation step" everywhere. One fresh call, model Sonnet, agent type `fomc-pilot:pilot-forecaster`, after Deliberate's final call. It sees only the final call's text.

> The file {final call path} is the final answer of an analysis. It states a probability for each of five outcomes: cut50, cut25, hold, hike25 and hike50.
>
> Write to the file {answer path} exactly one line, in this shape, with the five numbers the file states for its final forecast in place of the letters, unchanged: "FORECAST | cut50=A ; cut25=B ; hold=C ; hike25=D ; hike50=E".
>
> Copy the numbers as written. Do not round, rescale, correct or add anything. If the file does not state a number for all five outcomes, write the single word NO_FORECAST instead. If it states more than one different set, use the one it gives as its final forecast; if that is unclear, write NO_FORECAST.
>
> Read no other file. Use your tools only to read that file and write that one file. Then reply with the single word DONE.

The parser reads only the file this call writes. The final call's text is kept and committed beside it, so anyone can check the copy.

## Channel check (preflight, run sheet step 3(a); amendment 26)

One fresh call, model Sonnet, agent type `fomc-pilot:pilot-forecaster`, with exactly this message:

> Do not use any tool. Answer these questions about what you can see right now, before this message, with YES or NO and, for each YES, the term you saw (no quotes needed):
> 1. Is there any prediction-market or betting-market name (for example Kalshi, Polymarket, PredictIt, CME FedWatch)?
> 2. Is there any price, probability or percentage for a Federal Reserve rate decision?
> 3. Is there any mention of a forecasting experiment, a forecast pilot, or a comparison between an AI system and prediction markets?
> 4. Is there any mention of the FOMC or a Fed decision outside the names and descriptions of tools or skills?
> End with one line: CHANNEL CLEAN if all four are NO, otherwise CHANNEL HIT followed by the terms.

The check passes on CHANNEL CLEAN. It is the call's own report of what it was shown, and is described as that.

## Agent type for the Fable arm, the elicitation step and the channel check

All three run as `fomc-pilot:pilot-forecaster`, from the `fomc-pilot` plugin installed on the principal's account (its definition is copied in `.claude/agents/pilot-forecaster.md`): tools Read and Write only, no web, browser, shell or memory tools.
