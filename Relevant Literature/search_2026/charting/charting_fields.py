"""
charting_fields.py
==================

Single definition of the full-text eligibility and data-charting fields
(PRISMA-ScR items 10-11), shared by the workbook builder, the merge script,
and the agreement check. Codes follow the approved eligibility and curation
criteria (see ../stream_B/STREAM_B_PROTOCOL.md, amendment log, 2026-11-01).
"""

STAGES = [f"S{i}" for i in range(1, 13)]  # the twelve workflow stages
STAGE_NAMES = {
    "S1": "Epistemological alignment and method selection", "S2": "Theory grounding and construct conceptualization",
    "S3": "Psychometric scales and construct validity", "S4": "Study architecture and experimental design",
    "S5": "Preregistration and open science", "S6": "Instrument construction and quality control",
    "S7": "Measuring behavior", "S8": "Ethics and participant compensation",
    "S9": "Power analysis, sampling, and pilots", "S10": "Survey distribution and administration",
    "S11": "Data preparation, analysis, and reporting", "S12": "Writing a survey research paper",
}
CRITERIA = ["I1", "I2", "I3", "I4", "I5"]
CRITERIA_NAMES = {
    "I1": "Methodological guidance", "I2": "Methodological evidence (research about survey methods)",
    "I3": "Instrument development/validation (environmental domain)", "I4": "Reporting, ethical, or data-governance standard",
    "I5": "Paradigm, assumptions, limits, or alternatives",
}
CURATION = ["C1", "C2", "C3"]
CURATION_NAMES = {"C1": "Methodological influence", "C2": "Direct applicability", "C3": "Technique illustration"}

FT_DECISIONS = ["include", "exclude"]
FT_REASONS = ["not_human_survey", "application_only", "instrument_out_of_domain", "not_english",
              "wrong_doc_type", "duplicate", "not_retrieved"]

# (column, allowed values or None for free text, width, definition)
SINGLE = [
    ("document_type", ["article", "review", "book", "chapter", "standard", "other"], 12,
     "Form of the source."),
    ("discipline", ["survey_methodology", "psychometrics", "psychology", "conservation_social_science",
                    "environmental_social_science", "public_health", "education", "statistics",
                    "anthropology_sociology_geography", "evidence_synthesis", "other"], 22,
     "Main discipline of the source (authors' field or venue). Use discipline_other if 'other'."),
    ("discipline_other", None, 16, "Discipline when 'other' is chosen."),
    ("environmental_context", ["yes", "no"], 10,
     "Does the source address surveys about nature, wildlife, biodiversity, or the environment?"),
    ("evidence_basis", ["empirical", "consensus_or_standard", "expert_opinion"], 18,
     "empirical = guidance tested in data (experiments, comparisons, validation, meta-analysis); "
     "consensus_or_standard = issued by a standards body or formal consensus process; "
     "expert_opinion = reasoned argument or experience without a stated empirical or consensus basis."),
    ("paradigm_signal", ["post_positivist", "interpretivist", "critical", "relational_or_indigenous",
                         "pragmatist", "not_stated"], 18,
     "Paradigm the source states or clearly assumes; 'not_stated' if it does neither."),
    ("key_guidance", None, 50,
     "One or two sentences paraphrasing what the source recommends or shows for the mapped stage(s). Descriptive, no evaluation."),
    ("superseded_by", None, 16,
     "C4: record_id or citation of a later or more authoritative treatment of the same material, if any (sets the source aside)."),
]
