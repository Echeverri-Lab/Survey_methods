import re
text = """Value-Belief-Norm (VBN) Theory (Stern et al., 1999) — arguably the most cited theory in environmental behavior research; links ecological worldviews → beliefs → moral norms → action
Norm Activation Model (NAM) (Schwartz, 1977) — the foundation VBN builds on; models altruistic/moral norm activation
New Ecological Paradigm (NEP) (Dunlap & Van Liere, 1978) — foundational instrument for measuring anthropocentric vs. ecocentric worldviews
Nature Connectedness / Connectedness to Nature (Nisbet et al., 2009; Schultz, 2002) — emotional and cognitive bonds to the natural world as a behavioral predictor
Common-Pool Resource (CPR) Theory (Ostrom, 1990) — the cornerstone of socio-ecological systems science; explains when communities self-govern shared resources
Collective Action Theory (Olson, 1965) — logic of free-riding, a fundamental tension in conservation
Institutional Analysis and Development (IAD) Framework (Ostrom, 2005) — analytical framework for studying rule systems governing social-ecological interactions
Social-Ecological Systems (SES) Framework (Ostrom, 2009) — diagnostic framework for sustainability governance
Resilience Theory / Adaptive Cycle (Holling, 1973; Folke et al., 2004) — how SES persist, adapt, or transform through disturbance
Panarchy Theory (Gunderson & Holling, 2002) — nested adaptive cycles across scales; explains cross-scale dynamics in SES
Complex Adaptive Systems (CAS) — emergence, self-organization, and non-linearity in socio-ecological dynamics
Transtheoretical Model / Stages of Change (Prochaska & DiClemente, 1983) — maps readiness for behavior change across discrete stages
COM-B Model / Behavior Change Wheel (Michie et al., 2011) — systematic framework decomposing behavior into Capability, Opportunity, Motivation
Diffusion of Innovations (Rogers, 1962) — how new conservation practices spread through social systems
Multi-Level Perspective (MLP) (Geels, 2002) — how niches, regimes, and landscapes interact in sustainability transitions
Transformative Learning Theory (Mezirow, 1991) — how disorienting dilemmas shift deep worldview assumptions
Prospect Theory (Kahneman & Tversky, 1979) — loss aversion and framing effects; critical for conservation policy design
Protection Motivation Theory (Rogers, 1975) — threat appraisal and coping appraisal as behavioral drivers
Social Norms Theory (Cialdini et al., 1990) — descriptive vs. injunctive norms; highly relevant for community-based conservation
Environmental Identity Theory (Clayton, 2003) — how self-concept includes nature-related roles
Place Attachment Theory (Scannell & Gifford, 2010) — person-place bonds as drivers of stewardship behavior
Moral Foundations Theory (Haidt, 2012) — how different moral intuitions shape responses to conservation messages
Social Practice Theory (Shove, Pantzar & Watson, 2012) — habits and routines as the unit of analysis rather than individual decisions
Structuration Theory (Giddens, 1984) — the mutual constitution of social structure and human agency"""

print("| Theory / Framework | Main Argument | Constructs / Mechanisms | Citation / File |")
print("| :--- | :--- | :--- | :--- |")
for line in text.splitlines():
   parts = line.split("—")
   if len(parts) >= 2:
      name_cit = parts[0].strip()
      argument = parts[1].strip()
      match = re.search(r'\((.*?)\)$', name_cit)
      if match:
          cit = match.group(1)
          name = name_cit[:match.start()].strip()
      else:
          cit = ""
          name = name_cit
      # Add placeholders for Constructs and File 
      print(f"| **{name}** | {argument} | *Not specified in snippet* | {cit} |")
