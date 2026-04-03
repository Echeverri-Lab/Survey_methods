# SES Method-Selection Decision Tree

> A four-layer decision aid for choosing research methods in **Socio-Ecological Systems (SES)** fieldwork.
> Edit the [Mermaid](https://mermaid.js.org/) graph below and preview it in GitHub, VS Code, or the [Mermaid Live Editor](https://mermaid.live/).

---

## Decision Tree

```mermaid
graph TD
    %% ===== LAYER 1 — Epistemology (Philosophical Paradigm) =====
    EP[[What is your philosophical worldview?]]

    EP -->|Reality is objective<br>& measurable| POS[[Positivism]]
    EP -->|Reality is socially<br>constructed| CON[[Constructivism]]
    EP -->|What works is<br>what matters| PRA[[Pragmatism]]
    EP -->|Reality is shaped by<br>individual perspective| SUB[[Subjectivism]]
    EP -->|Knowledge must expose<br>power & oppression| CRT[[Critical Theory]]

    %% ===== LAYER 2 — Research Objective =====
    POS --> OBJ_GEN{Objective: Generalize}
    CON --> OBJ_UND{Objective: Understand lived experience}
    PRA --> OBJ_SOL{Objective: Solve a practical problem}
    SUB --> OBJ_INT{Objective: Interpret signs & meaning}
    CRT --> OBJ_CHG{Objective: Change / Emancipate}

    %% ===== LAYER 3 — Methods & Tools =====

    %% — Positivism branch —
    OBJ_GEN -->|Large-sample inference| M_SURV([Longitudinal Surveys<br>& Structured Scales])
    OBJ_GEN -->|Measure unconscious bias| M_IAT([Implicit Association<br>Tests — IATs])

    %% — Constructivism branch —
    OBJ_UND -->|Deep cultural immersion| M_ETHN([Ethnography<br>& Participant Observation])
    OBJ_UND -->|Group sense-making| M_FGD([Focus Group<br>Discussions — FGDs])

    %% — Pragmatism branch —
    OBJ_SOL -->|Community-driven data| M_PMAP([Participatory Mapping<br>& Co-Design])
    OBJ_SOL -->|Convergent evidence| M_MIX([Mixed-Methods<br>Sequential / Concurrent])

    %% — Subjectivism branch —
    OBJ_INT -->|Semiotic & narrative data| M_NARR([Narrative Analysis<br>& Photo-Elicitation])
    OBJ_INT -->|Perception of landscape| M_IAT2([IATs for<br>Implicit Landscape Values])

    %% — Critical Theory branch —
    OBJ_CHG -->|Action-oriented inquiry| M_PAR([Participatory Action<br>Research — PAR])
    OBJ_CHG -->|Policy & discourse| M_CDA([Critical Discourse<br>Analysis — CDA])

    %% ===== LAYER 4 — Ecological Linkage (The SE Bridge) =====
    BRIDGE{{"How is social data linked<br>to the ecosystem?"}}

    M_SURV  --> BRIDGE
    M_IAT   --> BRIDGE
    M_ETHN  --> BRIDGE
    M_FGD   --> BRIDGE
    M_PMAP  --> BRIDGE
    M_MIX   --> BRIDGE
    M_NARR  --> BRIDGE
    M_IAT2  --> BRIDGE
    M_PAR   --> BRIDGE
    M_CDA   --> BRIDGE

    BRIDGE -->|Spatial overlay of<br>social & biophysical data| ECO_GIS([GIS / Remote-Sensing<br>Overlay])
    BRIDGE -->|Ecological health<br>ground-truthing| ECO_BIO([Bio-Indicators<br>& Field Transects])
    BRIDGE -->|Governance &<br>regulatory analysis| ECO_POL([Policy Critique<br>& Institutional Mapping])

    %% ===== Styling =====
    classDef paradigm fill:#4A6FA5,stroke:#2E4A7A,color:#FFF,font-weight:bold
    classDef objective fill:#F2A154,stroke:#C57830,color:#000,font-weight:bold
    classDef method fill:#6BBF8A,stroke:#3E8A5C,color:#000
    classDef bridge fill:#E86F6F,stroke:#B84545,color:#FFF,font-weight:bold
    classDef eco fill:#9EC5E8,stroke:#5A8DB8,color:#000

    class EP,POS,CON,PRA,SUB,CRT paradigm
    class OBJ_GEN,OBJ_UND,OBJ_SOL,OBJ_INT,OBJ_CHG objective
    class M_SURV,M_IAT,M_ETHN,M_FGD,M_PMAP,M_MIX,M_NARR,M_IAT2,M_PAR,M_CDA method
    class BRIDGE bridge
    class ECO_GIS,ECO_BIO,ECO_POL eco
```

---

## Node-Shape Legend

| Shape | Syntax | Meaning |
|-------|--------|---------|
| `[[ ]]` Subroutine | `[[Positivism]]` | Philosophical / paradigmatic choice |
| `{ }` Diamond | `{Objective: Generalize}` | Decision point (what you want to achieve) |
| `([ ])` Stadium | `([Longitudinal Surveys])` | Concrete data-collection method or tool |
| `{{ }}` Hexagon | `{{"Ecological Linkage?"}}` | Integration checkpoint (the SE bridge) |

---

## Methodological Justification

### Why four layers?

1. **Layer 1 — Epistemology first.**
   Methods are never paradigm-neutral. A longitudinal survey designed under Positivism asks *different* questions (and accepts *different* evidence) than a participatory map produced under Pragmatism. Starting from worldview forces the researcher to make ontological assumptions explicit, which is the single largest source of hidden bias in SES research (Moon & Blackman, 2014).

2. **Layer 2 — Objective as filter.**
   The same paradigm can still serve different goals. Constructivism may aim to *understand* place-attachment **or** to *interpret* semiotic meaning in landscape narratives. Splitting objective from paradigm prevents premature method lock-in and keeps the design coherent with the actual research question.

3. **Layer 3 — SES-specific methods.**
   Standard social-science method menus omit tools that are critical for human–environment coupling:
   - **IATs** capture unconscious environmental attitudes that self-report scales miss (Greenwald et al., 1998). Listing them here reminds the researcher that *implicit* cognition can drive resource-use behavior.
   - **Participatory Mapping** is included under Pragmatism because it generates spatially explicit social data that can be directly overlaid with ecological layers—something neither a survey nor an interview can do on its own.
   - **PAR / CDA** under Critical Theory acknowledge that many SES conflicts are fundamentally about power over resources; methods must surface that power.

4. **Layer 4 — The Ecological Linkage checkpoint.**
   This is the layer most often missing from social-survey guides. In SES work the *social* dataset is only half the story. Forcing every method path through the "How is social data linked to the ecosystem?" node ensures the researcher explicitly chooses an integration strategy:
   - **GIS / Remote-Sensing Overlay** — ties survey or mapping data to land-cover, NDVI, or habitat layers.
   - **Bio-Indicators & Field Transects** — ground-truths perceptions with measurable ecological condition (e.g., water quality, species richness).
   - **Policy Critique & Institutional Mapping** — links discourse or governance data to regulatory structures that shape the SES.

   Without this bridge, a study risks producing social findings that float free of the ecological system they claim to explain.

---

## How to update the SVG

1. Copy the Mermaid code block above.
2. Paste it into the [Mermaid Live Editor](https://mermaid.live/).
3. Export as **SVG** and overwrite `decision_tree.svg` in this folder.
