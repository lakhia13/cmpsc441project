#!/usr/bin/env python3
"""
fetch_all_sources.py - UNIFIED Mental Health Content Fetcher

Combines all web sources into one comprehensive script:
- NIMH (National Institute of Mental Health)
- MedlinePlus (NIH Consumer Health)
- Mayo Clinic
- NAMI (National Alliance on Mental Illness)
- Cleveland Clinic
- Verywell Mind
- Psych Central
- WebMD
- Healthline
- Mind UK
- Mental Health Foundation (UK)
- APA (American Psychiatric Association)
- CDC

Usage:
    python fetch_all_sources.py --outdir ./papers_md --source all
    python fetch_all_sources.py --source nimh --source mayo
"""

import argparse
import re
import time
from pathlib import Path
from typing import List, Tuple, Optional

import requests
from bs4 import BeautifulSoup

# ============================================================
# Configuration
# ============================================================

REQUEST_DELAY = 0.4
TIMEOUT = 12
UA = "MentalHealthBot/1.0 (Educational Project)"
HEADERS = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"}

# ============================================================
# Helper Functions
# ============================================================

def sanitize_filename(name: str, maxlen: int = 100) -> str:
    """Clean filename for safe filesystem use."""
    name = re.sub(r"[\\/:*?\"<>|\n\r\t]+", " ", name)
    name = re.sub(r"\s+", "_", name).strip("_")
    return (name[:maxlen].rstrip("_") or "untitled").lower()


def get_page(url: str) -> Optional[BeautifulSoup]:
    """Fetch and parse a webpage."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        if r.status_code != 200:
            return None
        return BeautifulSoup(r.text, "html.parser")
    except:
        return None


def clean_text(text: str) -> str:
    """Clean extracted text."""
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    patterns = [
        r"Skip to (?:main )?content", r"Share (?:on|via) \w+", r"Was this helpful\??",
        r"Medically Reviewed by.*?(?:\n|$)", r"Written by.*?(?:\n|$)",
        r"Last (?:updated|reviewed).*?(?:\n|$)", r"© \d{4}.*?(?:\n|$)",
        r"Subscribe.*?(?:\n|$)", r"Newsletter", r"Advertisement", r"Cookie", r"Privacy Policy",
    ]
    for p in patterns:
        text = re.sub(p, "", text, flags=re.IGNORECASE)
    return text.strip()


def extract_content(soup: BeautifulSoup, selectors: List[str] = None) -> str:
    """Extract main content from a page."""
    if selectors is None:
        selectors = ["article", "main", ".content", "#content", ".article-body"]
    
    content_div = None
    for sel in selectors:
        if sel.startswith("."):
            content_div = soup.find(class_=sel[1:])
        elif sel.startswith("#"):
            content_div = soup.find(id=sel[1:])
        else:
            content_div = soup.find(sel)
        if content_div:
            break
    
    if not content_div:
        content_div = soup.find("article") or soup.find("main") or soup.find("body")
    
    if not content_div:
        return ""
    
    sections = []
    for elem in content_div.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
        text = elem.get_text(strip=True)
        if not text or len(text) < 15:
            continue
        if elem.name == "h1":
            sections.append(f"# {text}\n")
        elif elem.name == "h2":
            sections.append(f"\n## {text}\n")
        elif elem.name in ["h3", "h4"]:
            sections.append(f"\n### {text}\n")
        elif elem.name == "li":
            sections.append(f"- {text}")
        else:
            sections.append(text)
    
    return "\n\n".join(sections)


def save_md(outdir: Path, source: str, title: str, content: str, url: str) -> bool:
    """Save content as markdown file."""
    if len(content) < 300:
        return False
    
    filename = f"{source}_{sanitize_filename(title)}.md"
    outpath = outdir / filename
    counter = 1
    while outpath.exists():
        outpath = outdir / f"{source}_{sanitize_filename(title)}_{counter}.md"
        counter += 1
    
    md = f"# {title}\n\n**Source:** {source.upper()}\n**URL:** {url}\n\n---\n\n{content}\n"
    outpath.write_text(md, encoding="utf-8")
    return True


def fetch_pages(outdir: Path, source: str, pages: List[Tuple[str, str]], 
                base_url: str, selectors: List[str] = None) -> int:
    """Generic page fetcher."""
    saved = 0
    for path, title in pages:
        url = f"{base_url}/{path}" if not path.startswith("http") else path
        print(f"  → {title}...", end=" ", flush=True)
        soup = get_page(url)
        if soup:
            title_elem = soup.find("h1")
            if title_elem:
                title = title_elem.get_text(strip=True)
            content = clean_text(extract_content(soup, selectors))
            if save_md(outdir, source, title, content, url):
                print(f"✓ {len(content):,}")
                saved += 1
            else:
                print("✗ (too short)")
        else:
            print("✗ (fetch failed)")
        time.sleep(REQUEST_DELAY)
    return saved


# ============================================================
# NIMH - National Institute of Mental Health
# ============================================================

NIMH_PAGES = [
    ("health/topics/anxiety-disorders", "Anxiety Disorders"),
    ("health/topics/depression", "Depression"),
    ("health/topics/bipolar-disorder", "Bipolar Disorder"),
    ("health/topics/post-traumatic-stress-disorder-ptsd", "PTSD"),
    ("health/topics/obsessive-compulsive-disorder-ocd", "OCD"),
    ("health/topics/schizophrenia", "Schizophrenia"),
    ("health/topics/eating-disorders", "Eating Disorders"),
    ("health/topics/attention-deficit-hyperactivity-disorder-adhd", "ADHD"),
    ("health/topics/borderline-personality-disorder", "Borderline Personality"),
    ("health/topics/autism-spectrum-disorder-asd", "Autism"),
    ("health/topics/panic-disorder", "Panic Disorder"),
    ("health/topics/social-anxiety-disorder", "Social Anxiety"),
    ("health/topics/generalized-anxiety-disorder", "GAD"),
    ("health/topics/seasonal-affective-disorder", "SAD"),
    ("health/topics/suicide-prevention", "Suicide Prevention"),
    ("health/topics/coping-with-traumatic-events", "Coping with Trauma"),
    ("health/topics/substance-use-and-mental-health", "Substance Use"),
    ("health/topics/psychotherapies", "Psychotherapies"),
    ("health/topics/mental-health-medications", "Mental Health Medications"),
    ("health/topics/caring-for-your-mental-health", "Self Care"),
    ("health/topics/perinatal-depression", "Perinatal Depression"),
    ("health/topics/children-and-mental-health", "Children Mental Health"),
    ("health/topics/dissociative-disorders", "Dissociative Disorders"),
    ("health/topics/specific-phobia", "Specific Phobias"),
    ("health/topics/agoraphobia", "Agoraphobia"),
    ("health/topics/personality-disorders", "Personality Disorders"),
    ("health/topics/chronic-illness-and-mental-health", "Chronic Illness"),
    ("health/topics/older-adults-and-mental-health", "Older Adults"),
    ("health/topics/men-and-mental-health", "Men Mental Health"),
    ("health/topics/women-and-mental-health", "Women Mental Health"),
]

def fetch_nimh(outdir: Path) -> int:
    print("\n📚 NIMH (National Institute of Mental Health)")
    return fetch_pages(outdir, "nimh", NIMH_PAGES, "https://www.nimh.nih.gov",
                      [".content-block", "article", "main"])


# ============================================================
# MedlinePlus - NIH Consumer Health
# ============================================================

MEDLINEPLUS_PAGES = [
    ("anxiety.html", "Anxiety"),
    ("depression.html", "Depression"),
    ("bipolardisorder.html", "Bipolar Disorder"),
    ("ptsd.html", "PTSD"),
    ("obsessivecompulsivedisorder.html", "OCD"),
    ("schizophrenia.html", "Schizophrenia"),
    ("eatingdisorders.html", "Eating Disorders"),
    ("attentiondeficithyperactivitydisorder.html", "ADHD"),
    ("autismspectrumdisorder.html", "Autism"),
    ("mentalhealth.html", "Mental Health"),
    ("teenmentalhealth.html", "Teen Mental Health"),
    ("childmentalhealth.html", "Child Mental Health"),
    ("selfharm.html", "Self Harm"),
    ("suicide.html", "Suicide"),
    ("sleepdisorders.html", "Sleep Disorders"),
    ("insomnia.html", "Insomnia"),
    ("alcoholusedisorder.html", "Alcohol Use Disorder"),
    ("druguse.html", "Drug Use"),
    ("personalitydisorders.html", "Personality Disorders"),
    ("mooddisorders.html", "Mood Disorders"),
    ("postpartumdepression.html", "Postpartum Depression"),
    ("stress.html", "Stress"),
    ("grief.html", "Grief"),
    ("panicdisorder.html", "Panic Disorder"),
    ("phobias.html", "Phobias"),
    ("psychotherapy.html", "Psychotherapy"),
    ("antidepressants.html", "Antidepressants"),
]

def fetch_medlineplus(outdir: Path) -> int:
    print("\n📚 MedlinePlus (NIH Consumer Health)")
    return fetch_pages(outdir, "medlineplus", MEDLINEPLUS_PAGES, "https://medlineplus.gov",
                      ["#topic-content", "article", ".main"])


# ============================================================
# Mayo Clinic
# ============================================================

MAYO_PAGES = [
    ("diseases-conditions/depression/symptoms-causes/syc-20356007", "Depression"),
    ("diseases-conditions/anxiety/symptoms-causes/syc-20350961", "Anxiety"),
    ("diseases-conditions/bipolar-disorder/symptoms-causes/syc-20355955", "Bipolar Disorder"),
    ("diseases-conditions/post-traumatic-stress-disorder/symptoms-causes/syc-20355967", "PTSD"),
    ("diseases-conditions/obsessive-compulsive-disorder/symptoms-causes/syc-20354432", "OCD"),
    ("diseases-conditions/schizophrenia/symptoms-causes/syc-20354443", "Schizophrenia"),
    ("diseases-conditions/generalized-anxiety-disorder/symptoms-causes/syc-20360803", "GAD"),
    ("diseases-conditions/panic-attacks-and-panic-disorder/symptoms-causes/syc-20376021", "Panic Disorder"),
    ("diseases-conditions/social-anxiety-disorder/symptoms-causes/syc-20353561", "Social Anxiety"),
    ("diseases-conditions/anorexia-nervosa/symptoms-causes/syc-20353591", "Anorexia"),
    ("diseases-conditions/bulimia-nervosa/symptoms-causes/syc-20353615", "Bulimia"),
    ("diseases-conditions/binge-eating-disorder/symptoms-causes/syc-20353627", "Binge Eating"),
    ("diseases-conditions/adult-adhd/symptoms-causes/syc-20350878", "Adult ADHD"),
    ("diseases-conditions/adhd/symptoms-causes/syc-20350889", "ADHD Children"),
    ("diseases-conditions/borderline-personality-disorder/symptoms-causes/syc-20370237", "Borderline Personality"),
    ("diseases-conditions/narcissistic-personality-disorder/symptoms-causes/syc-20366662", "Narcissistic Personality"),
    ("diseases-conditions/antisocial-personality-disorder/symptoms-causes/syc-20353928", "Antisocial Personality"),
    ("diseases-conditions/dissociative-disorders/symptoms-causes/syc-20355215", "Dissociative Disorders"),
    ("diseases-conditions/insomnia/symptoms-causes/syc-20355167", "Insomnia"),
    ("diseases-conditions/seasonal-affective-disorder/symptoms-causes/syc-20364651", "SAD"),
    ("diseases-conditions/drug-addiction/symptoms-causes/syc-20365112", "Drug Addiction"),
    ("diseases-conditions/alcohol-use-disorder/symptoms-causes/syc-20369243", "Alcohol Use Disorder"),
    ("diseases-conditions/autism-spectrum-disorder/symptoms-causes/syc-20352928", "Autism"),
    ("diseases-conditions/specific-phobias/symptoms-causes/syc-20355156", "Specific Phobias"),
    ("diseases-conditions/agoraphobia/symptoms-causes/syc-20355987", "Agoraphobia"),
    ("diseases-conditions/hoarding-disorder/symptoms-causes/syc-20356056", "Hoarding Disorder"),
    ("diseases-conditions/postpartum-depression/symptoms-causes/syc-20376617", "Postpartum Depression"),
    ("diseases-conditions/teen-depression/symptoms-causes/syc-20350985", "Teen Depression"),
    # Treatment pages
    ("diseases-conditions/depression/diagnosis-treatment/drc-20356013", "Depression Treatment"),
    ("diseases-conditions/anxiety/diagnosis-treatment/drc-20350967", "Anxiety Treatment"),
    ("diseases-conditions/bipolar-disorder/diagnosis-treatment/drc-20355961", "Bipolar Treatment"),
    ("diseases-conditions/post-traumatic-stress-disorder/diagnosis-treatment/drc-20355973", "PTSD Treatment"),
    ("diseases-conditions/obsessive-compulsive-disorder/diagnosis-treatment/drc-20354438", "OCD Treatment"),
    ("diseases-conditions/schizophrenia/diagnosis-treatment/drc-20354449", "Schizophrenia Treatment"),
]

def fetch_mayo(outdir: Path) -> int:
    print("\n📚 Mayo Clinic")
    return fetch_pages(outdir, "mayoclinic", MAYO_PAGES, "https://www.mayoclinic.org",
                      [".content", "article", "#main-content"])


# ============================================================
# NAMI - National Alliance on Mental Illness
# ============================================================

NAMI_PAGES = [
    ("About-Mental-Illness/Mental-Health-Conditions/Anxiety-Disorders", "Anxiety Disorders"),
    ("About-Mental-Illness/Mental-Health-Conditions/Depression", "Depression"),
    ("About-Mental-Illness/Mental-Health-Conditions/Bipolar-Disorder", "Bipolar Disorder"),
    ("About-Mental-Illness/Mental-Health-Conditions/PTSD", "PTSD"),
    ("About-Mental-Illness/Mental-Health-Conditions/OCD", "OCD"),
    ("About-Mental-Illness/Mental-Health-Conditions/Schizophrenia", "Schizophrenia"),
    ("About-Mental-Illness/Mental-Health-Conditions/Borderline-Personality-Disorder", "BPD"),
    ("About-Mental-Illness/Mental-Health-Conditions/Dissociative-Disorders", "Dissociative"),
    ("About-Mental-Illness/Mental-Health-Conditions/Eating-Disorders", "Eating Disorders"),
    ("About-Mental-Illness/Mental-Health-Conditions/ADHD", "ADHD"),
    ("About-Mental-Illness/Mental-Health-Conditions/Autism", "Autism"),
    ("About-Mental-Illness/Mental-Health-Conditions/Schizoaffective-Disorder", "Schizoaffective"),
    ("About-Mental-Illness/Mental-Health-Conditions/Psychosis", "Psychosis"),
    ("About-Mental-Illness/Treatments/Psychotherapy", "Psychotherapy"),
    ("About-Mental-Illness/Treatments/Mental-Health-Medications", "Medications"),
    ("About-Mental-Illness/Treatments/ECT-TMS-and-Other-Brain-Stimulation-Therapies", "Brain Stimulation"),
    ("About-Mental-Illness/Common-with-Mental-Illness/Self-harm", "Self Harm"),
    ("About-Mental-Illness/Common-with-Mental-Illness/Suicide", "Suicide"),
    ("About-Mental-Illness/Common-with-Mental-Illness/Sleep-Disorders", "Sleep Disorders"),
    ("About-Mental-Illness/Common-with-Mental-Illness/Substance-Use-Disorders", "Substance Use"),
    ("Your-Journey/Family-Members-and-Caregivers", "Caregivers"),
    ("Your-Journey/Teens-Young-Adults", "Teens Young Adults"),
    ("Your-Journey/Veterans-Active-Duty", "Veterans"),
    ("About-Mental-Illness/Warning-Signs-and-Symptoms", "Warning Signs"),
    ("About-Mental-Illness/Recovery", "Recovery"),
]

def fetch_nami(outdir: Path) -> int:
    print("\n📚 NAMI (National Alliance on Mental Illness)")
    return fetch_pages(outdir, "nami", NAMI_PAGES, "https://www.nami.org",
                      [".content-wrapper", "article", ".page-content"])


# ============================================================
# Cleveland Clinic
# ============================================================

CLEVELAND_PAGES = [
    ("health/diseases/depression", "Depression"),
    ("health/diseases/anxiety", "Anxiety"),
    ("health/diseases/bipolar-disorder", "Bipolar Disorder"),
    ("health/diseases/post-traumatic-stress-disorder-ptsd", "PTSD"),
    ("health/diseases/obsessive-compulsive-disorder", "OCD"),
    ("health/diseases/schizophrenia", "Schizophrenia"),
    ("health/diseases/generalized-anxiety-disorder", "GAD"),
    ("health/diseases/panic-disorder", "Panic Disorder"),
    ("health/diseases/social-anxiety-disorder", "Social Anxiety"),
    ("health/diseases/anorexia-nervosa", "Anorexia"),
    ("health/diseases/bulimia", "Bulimia"),
    ("health/diseases/binge-eating-disorder", "Binge Eating"),
    ("health/diseases/attention-deficit-hyperactivity-disorder-adhd", "ADHD"),
    ("health/diseases/borderline-personality-disorder", "BPD"),
    ("health/diseases/narcissistic-personality-disorder", "NPD"),
    ("health/diseases/dissociative-identity-disorder-multiple-personality-disorder", "DID"),
    ("health/diseases/insomnia", "Insomnia"),
    ("health/diseases/seasonal-affective-disorder", "SAD"),
    ("health/diseases/substance-use-disorder-sud-substance-abuse", "Substance Use"),
    ("health/diseases/alcohol-use-disorder", "Alcohol Use Disorder"),
    ("health/diseases/autism-spectrum-disorder", "Autism"),
    ("health/diseases/hoarding-disorder", "Hoarding"),
    ("health/diseases/self-harm", "Self Harm"),
    ("health/diseases/psychosis", "Psychosis"),
]

def fetch_cleveland(outdir: Path) -> int:
    print("\n📚 Cleveland Clinic")
    return fetch_pages(outdir, "clevelandclinic", CLEVELAND_PAGES, "https://my.clevelandclinic.org",
                      [".health-article-content", "article", "main"])


# ============================================================
# WebMD
# ============================================================

WEBMD_PAGES = [
    ("mental-health/mental-health-depression", "Depression"),
    ("anxiety-panic/default", "Anxiety Panic"),
    ("bipolar-disorder/default", "Bipolar Disorder"),
    ("ptsd/default", "PTSD"),
    ("mental-health/obsessive-compulsive-disorder", "OCD"),
    ("schizophrenia/default", "Schizophrenia"),
    ("add-adhd/default", "ADHD"),
    ("mental-health/eating-disorders", "Eating Disorders"),
    ("mental-health/mental-health-borderline-personality-disorder", "BPD"),
    ("mental-health/dissociative-identity-disorder-multiple-personality-disorder", "DID"),
    ("mental-health/mental-health-phobias", "Phobias"),
    ("mental-health/mental-health-social-anxiety-disorder", "Social Anxiety"),
    ("mental-health/mental-health-panic-disorder", "Panic Disorder"),
    ("mental-health/mental-health-generalized-anxiety-disorder", "GAD"),
    ("mental-health/mental-health-seasonal-affective-disorder", "SAD"),
    ("mental-health/postpartum-depression", "Postpartum Depression"),
    ("mental-health/mental-health-psychotherapy", "Psychotherapy"),
    ("mental-health/mental-health-types-of-therapy", "Types of Therapy"),
    ("mental-health/mental-health-antidepressants", "Antidepressants"),
    ("mental-health/mental-health-stress-management", "Stress Management"),
    ("sleep-disorders/default", "Sleep Disorders"),
]

def fetch_webmd(outdir: Path) -> int:
    print("\n📚 WebMD Mental Health")
    return fetch_pages(outdir, "webmd", WEBMD_PAGES, "https://www.webmd.com")


# ============================================================
# Healthline
# ============================================================

HEALTHLINE_PAGES = [
    ("health/depression", "Depression"),
    ("health/anxiety", "Anxiety"),
    ("health/bipolar-disorder", "Bipolar Disorder"),
    ("health/ptsd", "PTSD"),
    ("health/ocd", "OCD"),
    ("health/schizophrenia", "Schizophrenia"),
    ("health/adhd", "ADHD"),
    ("health/eating-disorders", "Eating Disorders"),
    ("health/anorexia-nervosa", "Anorexia"),
    ("health/bulimia-nervosa", "Bulimia"),
    ("health/borderline-personality-disorder", "BPD"),
    ("health/narcissistic-personality-disorder", "NPD"),
    ("health/dissociative-identity-disorder", "DID"),
    ("health/panic-disorder", "Panic Disorder"),
    ("health/social-anxiety-disorder", "Social Anxiety"),
    ("health/generalized-anxiety-disorder", "GAD"),
    ("health/seasonal-affective-disorder", "SAD"),
    ("health/postpartum-depression", "Postpartum Depression"),
    ("health/insomnia", "Insomnia"),
    ("health/alcohol-use-disorder", "Alcohol Use Disorder"),
    ("health/drug-addiction", "Drug Addiction"),
    ("health/autism", "Autism"),
    ("health/psychotherapy", "Psychotherapy"),
    ("health/cognitive-behavioral-therapy", "CBT"),
    ("health/stress", "Stress"),
    ("health/grief", "Grief"),
]

def fetch_healthline(outdir: Path) -> int:
    print("\n📚 Healthline Mental Health")
    return fetch_pages(outdir, "healthline", HEALTHLINE_PAGES, "https://www.healthline.com")


# ============================================================
# Mind UK
# ============================================================

MIND_UK_PAGES = [
    ("information-support/types-of-mental-health-problems/anxiety-and-panic-attacks", "Anxiety"),
    ("information-support/types-of-mental-health-problems/depression", "Depression"),
    ("information-support/types-of-mental-health-problems/bipolar-disorder", "Bipolar"),
    ("information-support/types-of-mental-health-problems/post-traumatic-stress-disorder-ptsd", "PTSD"),
    ("information-support/types-of-mental-health-problems/obsessive-compulsive-disorder-ocd", "OCD"),
    ("information-support/types-of-mental-health-problems/schizophrenia", "Schizophrenia"),
    ("information-support/types-of-mental-health-problems/eating-problems", "Eating Problems"),
    ("information-support/types-of-mental-health-problems/personality-disorders", "Personality Disorders"),
    ("information-support/types-of-mental-health-problems/borderline-personality-disorder-bpd", "BPD"),
    ("information-support/types-of-mental-health-problems/dissociative-disorders", "Dissociative"),
    ("information-support/types-of-mental-health-problems/phobias", "Phobias"),
    ("information-support/types-of-mental-health-problems/self-harm", "Self Harm"),
    ("information-support/types-of-mental-health-problems/suicidal-feelings", "Suicidal Feelings"),
    ("information-support/types-of-mental-health-problems/sleep-problems", "Sleep Problems"),
    ("information-support/types-of-mental-health-problems/stress", "Stress"),
    ("information-support/types-of-mental-health-problems/anger", "Anger"),
    ("information-support/types-of-mental-health-problems/loneliness", "Loneliness"),
    ("information-support/types-of-mental-health-problems/trauma", "Trauma"),
    ("information-support/types-of-mental-health-problems/grief", "Grief"),
    ("information-support/types-of-mental-health-problems/psychosis", "Psychosis"),
    ("information-support/drugs-and-treatments/antidepressants", "Antidepressants"),
    ("information-support/drugs-and-treatments/talking-therapy-and-counselling", "Therapy"),
    ("information-support/drugs-and-treatments/cognitive-behavioural-therapy-cbt", "CBT"),
    ("information-support/drugs-and-treatments/mindfulness", "Mindfulness"),
    ("information-support/tips-for-everyday-living/relaxation", "Relaxation"),
    ("information-support/tips-for-everyday-living/physical-activity-and-your-mental-health", "Physical Activity"),
]

def fetch_mind_uk(outdir: Path) -> int:
    print("\n📚 Mind UK")
    return fetch_pages(outdir, "minduk", MIND_UK_PAGES, "https://www.mind.org.uk")


# ============================================================
# Mental Health Foundation (UK)
# ============================================================

MHF_PAGES = [
    ("explore-mental-health/a-to-z-topics/anxiety", "Anxiety"),
    ("explore-mental-health/a-to-z-topics/depression", "Depression"),
    ("explore-mental-health/a-to-z-topics/stress", "Stress"),
    ("explore-mental-health/a-to-z-topics/sleep", "Sleep"),
    ("explore-mental-health/a-to-z-topics/loneliness", "Loneliness"),
    ("explore-mental-health/a-to-z-topics/body-image", "Body Image"),
    ("explore-mental-health/a-to-z-topics/grief", "Grief"),
    ("explore-mental-health/a-to-z-topics/self-harm", "Self Harm"),
    ("explore-mental-health/a-to-z-topics/eating-disorders", "Eating Disorders"),
    ("explore-mental-health/a-to-z-topics/nature", "Nature"),
    ("explore-mental-health/a-to-z-topics/relationships", "Relationships"),
    ("explore-mental-health/a-to-z-topics/alcohol", "Alcohol"),
    ("explore-mental-health/a-to-z-topics/drugs-and-mental-health", "Drugs"),
    ("explore-mental-health/a-to-z-topics/mindfulness", "Mindfulness"),
    ("explore-mental-health/a-to-z-topics/wellbeing", "Wellbeing"),
    ("explore-mental-health/a-to-z-topics/men-and-mental-health", "Men Mental Health"),
    ("explore-mental-health/a-to-z-topics/women-and-mental-health", "Women Mental Health"),
    ("explore-mental-health/a-to-z-topics/older-people-and-mental-health", "Older Adults"),
]

def fetch_mhf(outdir: Path) -> int:
    print("\n📚 Mental Health Foundation (UK)")
    return fetch_pages(outdir, "mhf", MHF_PAGES, "https://www.mentalhealth.org.uk")


# ============================================================
# APA - American Psychiatric Association
# ============================================================

APA_PAGES = [
    ("patients-families/depression", "Depression"),
    ("patients-families/anxiety-disorders", "Anxiety Disorders"),
    ("patients-families/bipolar-disorders", "Bipolar Disorders"),
    ("patients-families/ptsd", "PTSD"),
    ("patients-families/ocd", "OCD"),
    ("patients-families/schizophrenia", "Schizophrenia"),
    ("patients-families/adhd", "ADHD"),
    ("patients-families/eating-disorders", "Eating Disorders"),
    ("patients-families/addiction-substance-use-disorders", "Addiction"),
    ("patients-families/personality-disorders", "Personality Disorders"),
    ("patients-families/autism-spectrum-disorder", "Autism"),
    ("patients-families/dissociative-disorders", "Dissociative Disorders"),
    ("patients-families/sleep-disorders", "Sleep Disorders"),
    ("patients-families/suicide-prevention", "Suicide Prevention"),
    ("patients-families/what-is-mental-illness", "What is Mental Illness"),
    ("patients-families/what-is-psychotherapy", "Psychotherapy"),
    ("patients-families/warning-signs-of-mental-illness", "Warning Signs"),
]

def fetch_apa(outdir: Path) -> int:
    print("\n📚 APA (American Psychiatric Association)")
    return fetch_pages(outdir, "apa", APA_PAGES, "https://www.psychiatry.org")


# ============================================================
# CDC - Centers for Disease Control
# ============================================================

CDC_PAGES = [
    ("mentalhealth/learn/index.htm", "Mental Health Learn"),
    ("mentalhealth/cope-with-stress/index.htm", "Cope with Stress"),
    ("anxiety/index.html", "Anxiety"),
    ("depression/index.htm", "Depression"),
    ("suicide/facts/index.html", "Suicide Facts"),
    ("childrensmentalhealth/depression.html", "Children Depression"),
    ("childrensmentalhealth/anxiety.html", "Children Anxiety"),
    ("childrensmentalhealth/adhd.html", "Children ADHD"),
    ("sleep/about_sleep/key_disorders.html", "Sleep Disorders"),
]

def fetch_cdc(outdir: Path) -> int:
    print("\n📚 CDC Mental Health")
    return fetch_pages(outdir, "cdc", CDC_PAGES, "https://www.cdc.gov")


# ============================================================
# Verywell Mind
# ============================================================

VERYWELL_PAGES = [
    ("what-is-depression-1066770", "Depression"),
    ("generalized-anxiety-disorder-1066770", "GAD"),
    ("social-anxiety-disorder-4013678", "Social Anxiety"),
    ("panic-disorder-2795419", "Panic Disorder"),
    ("what-is-ptsd-2795405", "PTSD"),
    ("obsessive-compulsive-disorder-ocd-2510676", "OCD"),
    ("bipolar-disorder-overview-378810", "Bipolar"),
    ("schizophrenia-4014032", "Schizophrenia"),
    ("borderline-personality-disorder-425487", "BPD"),
    ("adhd-overview-4013718", "ADHD"),
    ("autism-spectrum-disorder-1066772", "Autism"),
    ("what-is-psychotherapy-2795067", "Psychotherapy"),
    ("cognitive-behavioral-therapy-2795747", "CBT"),
    ("dialectical-behavior-therapy-1067402", "DBT"),
    ("stress-management-4173441", "Stress Management"),
    ("mindfulness-meditation-88369", "Mindfulness"),
]

def fetch_verywell(outdir: Path) -> int:
    print("\n📚 Verywell Mind")
    return fetch_pages(outdir, "verywellmind", VERYWELL_PAGES, "https://www.verywellmind.com",
                      [".article-content", "article", "main"])


# ============================================================
# Main
# ============================================================

ALL_SOURCES = {
    "nimh": fetch_nimh,
    "medlineplus": fetch_medlineplus,
    "mayo": fetch_mayo,
    "nami": fetch_nami,
    "cleveland": fetch_cleveland,
    "webmd": fetch_webmd,
    "healthline": fetch_healthline,
    "minduk": fetch_mind_uk,
    "mhf": fetch_mhf,
    "apa": fetch_apa,
    "cdc": fetch_cdc,
    "verywell": fetch_verywell,
}


def main():
    parser = argparse.ArgumentParser(
        description="Unified Mental Health Content Fetcher",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python fetch_all_sources.py --source all
    python fetch_all_sources.py --source nimh --source mayo --source nami
    python fetch_all_sources.py --outdir ./my_papers --source healthline
        """
    )
    parser.add_argument("--outdir", type=Path, default="./papers_md",
                       help="Output directory (default: ./papers_md)")
    parser.add_argument("--source", action="append", 
                       choices=["all"] + list(ALL_SOURCES.keys()),
                       help="Sources to fetch (can specify multiple, default: all)")
    args = parser.parse_args()
    
    sources = args.source or ["all"]
    outdir = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("🏥 UNIFIED Mental Health Content Fetcher")
    print("=" * 60)
    print(f"Output: {outdir.absolute()}")
    print(f"Sources: {', '.join(sources)}")
    print("=" * 60)
    
    total = 0
    
    if "all" in sources:
        for name, fetch_func in ALL_SOURCES.items():
            total += fetch_func(outdir)
    else:
        for source in sources:
            if source in ALL_SOURCES:
                total += ALL_SOURCES[source](outdir)
    
    print("\n" + "=" * 60)
    print(f"✅ COMPLETE! Saved {total} articles to {outdir}")
    print("=" * 60)


if __name__ == "__main__":
    main()

