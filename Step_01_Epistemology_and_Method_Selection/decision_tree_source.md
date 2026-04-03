# SES Method-Selection Decision Tree

> A four-layer decision aid for choosing research methods in **Socio-Ecological Systems (SES)** fieldwork.
> Edit the [Mermaid](https://mermaid.js.org/) graph below and preview it in GitHub, VS Code, or the [Mermaid Live Editor](https://mermaid.live/).

---

## Decision Tree

```mermaid
flowchart LR

    EP[["What is your philosophical worldview?"]] -- Reality is objective<br>and measurable --> POS[["Positivism"]]
    EP -- Reality is socially<br>constructed --> CON[["Constructivism"]]
    EP -- What works is<br>what matters --> PRA[["Pragmatism"]]
    EP -- Reality is shaped by<br>individual perspective --> SUB[["Subjectivism"]]
    EP -- Knowledge must expose<br>power and oppression --> CRT[["Critical Theory"]]
    POS --> OBJ_GEN{"Objective: Find universal truths and mechanisms/ Generalize"}
    CON --> OBJ_UND{"Objective: Understand lived experience"}
    PRA --> OBJ_SOL{"Objective: Solve a practical problem"}
    SUB --> OBJ_INT{"Objective: Interpret signs and meaning"}
    CRT --> OBJ_CHG{"Objective: Change / Emancipate"}
    OBJ_GEN -- "Large-sample inference" --> M_SURV(["Longitudinal surveys,<br> experiments and structured psychometric scales"])
    OBJ_GEN -- Measure unconscious bias --> M_IAT(["Implicit Association<br>Tests — IATs"])
    OBJ_UND -- Deep cultural immersion --> M_ETHN(["Ethnography<br> and participant observation"])
    OBJ_UND -- "Group sense-making" --> M_FGD(["Focus group<br> discussions"])
    OBJ_SOL -- "Community-driven data" --> M_PMAP(["Participatory mapping<br> and community-based methods"])
    OBJ_SOL -- Convergent evidence --> M_MIX(["Mixed-methods<br>sequential / concurrent"])
    OBJ_INT -- Semiotic & narrative data --> M_NARR(["Narrative analysis<br> and photo-elicitation"])
    OBJ_INT -- Perception of landscape --> M_IAT2(["IATs for<br>Implicit landscape values"])
    OBJ_CHG -- "Action-oriented inquiry" --> M_PAR(["Participatory action<br>research"])
    OBJ_CHG -- Policy & discourse --> M_CDA(["Critical discourse<br>analysis"])
    M_SURV --> BRIDGE{{"How is social data linked<br>to the ecosystem?"}}
    M_IAT --> BRIDGE
    M_ETHN --> BRIDGE
    M_FGD --> BRIDGE
    M_PMAP --> BRIDGE
    M_MIX --> BRIDGE
    M_NARR --> BRIDGE
    M_IAT2 --> BRIDGE
    M_PAR --> BRIDGE
    M_CDA --> BRIDGE
    BRIDGE -- Spatial overlay of<br>social &amp; biophysical data --> ECO_GIS(["GIS / Remote-Sensing<br>Overlay"])
    BRIDGE -- "Ecological health<br>ground-truthing" --> ECO_BIO(["Bio-indicators<br> and field transects, surveys, point counts, "])
    BRIDGE -- Governance &amp;<br>regulatory analysis --> ECO_POL(["Policy Critique<br>&amp; Institutional Mapping"])

     EP:::paradigm
     POS:::paradigm
     CON:::paradigm
     PRA:::paradigm
     SUB:::paradigm
     CRT:::paradigm
     OBJ_GEN:::objective
     OBJ_UND:::objective
     OBJ_SOL:::objective
     OBJ_INT:::objective
     OBJ_CHG:::objective
     M_SURV:::method
     M_IAT:::method
     M_ETHN:::method
     M_FGD:::method
     M_PMAP:::method
     M_MIX:::method
     M_NARR:::method
     M_IAT2:::method
     M_PAR:::method
     M_CDA:::method
     BRIDGE:::bridge
     ECO_GIS:::eco
     ECO_BIO:::eco
     ECO_POL:::eco
    classDef paradigm fill:#4A6FA5,stroke:#2E4A7A,color:#FFF,font-weight:bold
    classDef objective fill:#F2A154,stroke:#C57830,color:#000,font-weight:bold
    classDef method fill:#6BBF8A,stroke:#3E8A5C,color:#000
    classDef bridge fill:#E86F6F,stroke:#B84545,color:#FFF,font-weight:bold
    classDef eco fill:#9EC5E8,stroke:#5A8DB8,color:#000
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
