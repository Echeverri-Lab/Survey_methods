# Editable Decision Tree

You can edit this [Mermaid](https://mermaid.js.org/) graph and preview it directly in GitHub or text editors that support Mermaid rendering.

```mermaid
graph TD
    A[Research Goal] -->|Exploratory / Local Meaning<br>Power dynamics & context| B(Qualitative Methods)
    B --> B1[Interviews, Ethnography, FGDs]
    
    A -->|Hypothesis testing / Prevalence| C{Are constructs well-defined & measurable?}
    
    C -->|No| D[Formative Qualitative Work]
    D --> D1[Cognitive interviews, FGDs]
    D1 -->|Pilot| E
    
    C -->|Yes| E[Quantitative Survey]
    E --> E1[Scales, sampling design, power analysis]
    
    A -->|Need both depth & breadth?| F(Mixed Methods)
    F --> F1[Sequential or Concurrent designs]
    
    E --> G{Behavioral outcomes available?}
    G -->|Yes| H[Add behavioral tasks / objective data]
    G -->|No| I[Proceed with self-report & strong quality control]
```

To update the SVG image in this folder:
1. Copy the code above.
2. Paste it into the [Mermaid Live Editor](https://mermaid.live/).
3. Export as SVG and overwrite `decision_tree.svg`.
