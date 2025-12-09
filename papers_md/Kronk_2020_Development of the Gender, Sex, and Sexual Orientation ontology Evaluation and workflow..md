# Kronk_2020_Development of the Gender, Sex, and Sexual Orientation ontology Evaluation and workflow.

Journal of the American Medical Informatics Association, 27(7), 2020, 1110–1115

doi: 10.1093/jamia/ocaa061
Advance Access Publication Date: 17 June 2020

Brief Communications

Brief Communications

Development of the Gender, Sex, and Sexual Orientation
ontology: Evaluation and workflow

Clair A. Kronk

1 and Judith W. Dexheimer1,2,3

1Department of Biomedical Informatics, University of Cincinnati College of Medicine, Cincinnati, Ohio, USA, 2Division of
Emergency Medicine, Cincinnati Children’s Hospital Medical Center, Cincinnati, Ohio, USA, and 3Department of Pediatrics, Uni-
versity of Cincinnati College of Medicine, Cincinnati, Ohio, USA

Corresponding Author: Clair A. Kronk, BSc, Department of Biomedical Informatics, University of Cincinnati College of
Medicine, 3333 Burnet Avenue, Cincinnati, OH 45229-3026, USA; kronkcj@mail.uc.edu

Received 15 March 2020; Editorial Decision 9 April 2020; Editorial Decision 9 April 2020; Accepted 14 April 2020

ABSTRACT

Objective: The study sought to create an integrated vocabulary system that addresses the lack of standardized
health terminology in gender and sexual orientation.
Materials and Methods: We evaluated computational efﬁciency, coverage, query-based term tagging, ran-
domly selected term tagging, and mappings to existing terminology systems (including ICD (International Clas-
siﬁcation of Diseases), DSM (Diagnostic and Statistical Manual of Mental Disorders ), SNOMED (Systematized
Nomenclature of Medicine), MeSH (Medical Subject Headings), and National Cancer Institute Thesaurus).
Results: We published version 2 of the Gender, Sex, and Sexual Orientation (GSSO) ontology with over 10 000
entries with deﬁnitions, a readable hierarchy system, and over 14 000 database mappings. Over 70% of terms
had no mapping in any other available ontology.
Discussion: We created the GSSO and made it publicly available on the National Center for Biomedical
Ontology BioPortal and on GitHub. It includes clariﬁcations on over 200 slang terms, 190 pronouns with linked
example usages, and over 200 nonbinary and culturally speciﬁc gender identities.
Conclusions: Gender and sexual orientation continue to represent crucial areas of medical practice and
research with evolving terminology. The GSSO helps address this gap by providing a centralized data resource.

Key words: biological ontologies, gender and sexual minorities, sex, gender identity, sexual behavior

INTRODUCTION

Gender, sex, and sexual orientation have expanded significantly as
areas of research in the last 2 decades.1–3 This literature features not
only volume, but also heterogeneity in terminology.2,4 These issues
make knowledge discovery and understanding difficult without exter-
nal modeling.5–7 The Gender, Sex, and Sexual Orientation (GSSO)
ontology was designed as a model to facilitate communication and as-
sist in organizing this literature.8 The GSSO includes more than 1400
external biomedical ontology references, 1000 definitions, and 150
fully cited reference materials. Approximately one-third of its entries
are novel, having no mapping to any of the over 700 ontologies

indexed in the open biomedical ontology repository, the National
Center for Biomedical Ontology (NCBO) BioPortal, in 2019.9,10

An ontology was chosen as the GSSO format to facilitate domain
knowledge reuse, make analysis of that knowledge computationally
efficient, and create explicitness within the domains of gender, sex,
and sexual orientation.11

Since its inception, the GSSO has garnered significant interest, be-
ing in the top 5% of all ontologies visited on the NCBO BioPortal’s
website as of March 2020. As its use cases expand, integration and in-
teroperability have become essential to parse and tag incoming infor-
mation. Despite its size, many entries were incomplete, lacking external

VC The Author(s) 2020. Published by Oxford University Press on behalf of the American Medical Informatics Association.
All rights reserved. For permissions, please email: journals.permissions@oup.com

1110

Journal of the American Medical Informatics Association, 2020, Vol. 27, No. 7

1111

linking, references, or definitions, and its original classification system
was created in a more human- than machine-readable format.

To address the literature and traffic volumes, we sought to in-
crease the ontology’s scope, referencing, internal and external link-
ing, and verification methodologies. We focused on search
capabilities given the diversity and difficult in terminology matching
in the fields of gender, sex, and sexual orientation.1,12–14 Our goal
was to improve the functionality and accessibility of the GSSO
through scalable, iterative improvements.

MATERIALS AND METHODS

Ontology construction
The first version of the GSSO included 6250 terms covering diverse
topics from abstinence to zygosity with synonyms, mappings to
other ontologies, and select translations to additional non-English
languages. It is available via GitHub (https://github.com/Superrap-
tor/GSSO), and a demonstration website with simple search func-
tionality was made available at our institution (https://homepages.
uc.edu/(cid:2)kronkcj/gsso/). We constructed the ontology using the
Prot(cid:2)eg(cid:2)e software.15 Despite its initial wide coverage, only 17% of
initial terms included definitions and referencing, compared with
about 11% of Medical Subject Headings (MeSH) terms or 77% of
National Cancer Institute Thesaurus terms.10

We iteratively scoped all relevant literature for completeness.16
We identified 32 seed terms from the most recent Human Rights
Campaign (HRC) glossary to search titles from the 2019 release of
Medline. HRC is the largest LGBTQIAþ advocacy group in the
United States,17 claiming more than 3 million members,18 about
one-third of the estimated American LGBTQIAþ population.19
These search results were then used to identify the most common n-
grams. The top 200 of 1-, 2-, 3-, 4-, and 5-grams were found and
considered for addition to the GSSO. The 32 seed terms were ally,
androgynous, asexual, biphobia, bisexual, cisgender, closeted, com-
ing out, gay, gender dysphoria, gender-expansive, gender expression,
gender-fluid, gender identity, gender nonconforming, genderqueer,
gender transition, homophobia, intersex, lesbian, LGBTQ, living
openly, nonbinary, outing, pansexual, queer, questioning, same-gen-
der loving, sex assigned at birth, sexual orientation, transgender,
and transphobia.

We searched “LGBTQ terminology” and “LGBTQ slang” on
Google in August 2019, taking the first 2 pages of relevant results and
adding all terms from online glossaries. “LGBTQ” was chosen as the
queried initialism because of its preferred usage in current style
guides.20–23 We evaluated print encyclopedias and vocabularies found
via Google Books, Google Scholar, and the HathiTrust Digital Library
from September 2019 to January 2020. We incorporated feedback on
terms from the GLBT Museum and Archives listserv and the Trans
PhD Network on Facebook for additional terms and usage notes.

To complete the ontology, we parsed each of the original terms
and updated them in a piecewise manner, with reclassifications
based on superclass or subclass and class or individual and class or
individual
journal
articles were moved to instances of “scholarly article” rather than
subclasses of it to facilitate more computationally efficient queries.
We added definitions and references, either a piece of literature or
an external database identifier, where missing.

for computational readability. For instance,

A full mapping was made to the second version of the Homosau-
rus vocabulary24 and to the Library of Congress’ LGBTQIAþ re-
lated vocabulary.25

Table 1. External database mappings from version 1 to version 2

Source

ATC
BFO
ChEBI
DO
DSM
EFO
FMA
GO
GOLD
Homosaurus
HPO
ICD-9-CM
ICD-10-CM
LCC
LCSH
MedDRA
MeSH
NCBI Taxon
NCIT
SCTID
SIO
STY
TA
TE
UBERON
Wikidata
Wikipedia

Mappings in
version 1
(n ¼ 1416)

Mappings
in version 2
(n ¼ 14 193)

NM
19
4
62
NM
35
43
32
13
NM
30
30
28
NM
NM
129
261
11
261
241
116
16
3
30
22
NM
NM

20a
0
213a
193a
21a
0
327a
152a
0
430a
137a
101a
261a
527a
749a
595a
904a
87a
1034a
1084a
3
1
91a
38
169a
2270a
4755a

Only databases with more than 10 mappings are shown. Mappings to
Wikidata and Wikipedia were made in version 1 but were not separately tabu-
lated (they brought the total number of mappings to approximately 3300,
which is still signiﬁcantly less than 14 193).

ATC: Anatomical Therapeutic Chemical Classiﬁcation System; BFO: Basic
Formal Ontology; ChEBI: Chemical Entities of Biological Interest; DO: Dis-
ease Ontology; DSM: Diagnostic and Statistical Manual of Mental Disorders;
EFO: Experimental Factor Ontology; FMA: Foundational Model of Anat-
omy; GO: Gene Ontology; GOLD: General Ontology for Linguistic Descrip-
tion; HPO: Human Phenotype Ontology;
International
Classiﬁcation of Diseases–Ninth Revision–Clinical Modiﬁcation; ICD-10-
CM: International Classiﬁcation of Diseases–Tenth Revision–Clinical Modiﬁ-
cation; LCC: Library of Congress Classiﬁcation; LCSH: Library of Congress
Subject Headings; MeSH: Medical Subject Headings; NCBI: National Center
for Biotechnology Information; NCIT: National Cancer Institute Thesaurus;
NM: no mapping; SIO: Semanticscience Integrated Ontology; STY: Semantic
Types Ontology; TA: Terminologia Anatomica; TE: Terminologia Embryo-
logica.

ICD-9-CM:

aSigniﬁcant increase.

Preliminary ontology evaluation
We used Medline as our evaluation set to evaluate completeness of
mappings. We analyzed recall and precision on chosen queries
revolving around the HRC glossary terms. We tested usage with
plaintext title matching, then added MeSH terms, and finally added
GSSO terms.

We created 2 subgroupings of Medline for testing. The first we
contained a random selection of 1 217 621 entries (of 29 138 438
[4.2%]). In the second, we preselected those entries with plaintext ti-
tle/abstract matches to the HRC glossary terms.

GSSO term matching for titles and abstracts was done piecewise
to decrease false positives.26,27 Pronouns, stop words, and other

1112

Journal of the American Medical Informatics Association, 2020, Vol. 27, No. 7

Figure 1. Sample entries from version 2 (left) and version 1 (right)..

terms 3 characters or shorter were not matched. Matching was done
in a 2-step process. In the first step, a mapping to a label, alternate
name, synonym, exact synonym, broad synonym, narrow synonym,
or demonym was considered a definite match and returned. In the
second step, a mapping to a shortened name, related synonym, or
obsoleted term was considered a probable match. Then,
the
descendants and instances of that term were searched. If there was a
match with any of the descendants or instances, the probable match
was deemed a match. Otherwise, it was deemed a nonmatch.

Recall, precision, and F-scores were tested in the random Med-
line subset and the queried Medline subset using plaintext title map-
ping, MeSH terms, and GSSO terms. Terms had to be present in all
categories and have little to no ambiguity to be considered for
matching. Lack of ambiguity was determined as the term having
only 1 definition as of February 2020 on the online dictionary Wik-
tionary. Alternatively, if all definitions pertained to the same idea
they were included. Terms fitting these criteria included lesbian,
transgender, sexual orientation, gender identity, gender dysphoria,
homophobia, LGBTQ, cisgender, gender expression, transphobia,
gender nonconforming, genderqueer, biphobia, same-gender loving,
gender-expansive, gender-fluid, and sex assigned at birth. MeSH
terms were considered the gold-standard. Precision above 0.265, re-
call above 0.216, and F-score above 0.198 were considered satisfac-
tory based on other work describing ontology-mapped query
systems28; likewise, precision values above 0.56, recall values above
0.42, and F-scores above 0.48 were considered excellent.29

RESULTS

Version 2 of the GSSO features 10 060 entries expanded from 6250
and is available at the NCBO BioPortal (https://bioportal.bioontol-

ogy.org/ontologies/GSSO) and at GitHub (https://github.com/
Superraptor/GSSO). Each class in version 2 (7121 entries) contains
a human-readable definition and is placed in a computer-readable
hierarchy. The number of external database mappings has been in-
creased from 1416 to 14 193 (Table 1). A total of 5273 (74.0%)
classes had no mapping to any class in any of the over 800 ontolo-
gies at the NCBO BioPortal. The average number of annotations
per class increased from 2.6 to 7.4. Sample entries for version 1 and
2 are shown in Figure 1. The number of sources increased from 264
to 823, including 325 scholarly articles and 91 books, including
The Complete Dictionary of Sexology, The Wiley Blackwell Ency-
clopedia of Gender and Sexuality Studies, and LGBTQ America
Today: An Encyclopedia, each being cited in 371, 159, and 121
entries.30–32 Online sources of note included the glbtq Encyclope-
dia Project and the Encyclopedia of Homosexuality, which pro-
vided 125 and 134 citations, respectively.33,34 A total of 310 usage
notes were created.

The GSSO also includes 204 slang terms with definitions and
references, 190 pronouns with linked example usages, and 223
terms related to nonbinary and culturally specific gender identities
ranging from hijra on the Indian subcontinent to ashtime in the
Maale community of Ethiopia.

With plaintext title searching using HRC terms, we identified
14 019 Medline entries. Tagging a Medline entry with GSSO terms
took 7.7 seconds on average (range 1.8-9.9 seconds) when run on a
local machine. Tagging was performed for titles, abstracts, and jour-
nal titles for each entry.

We tagged 13 998 (99.85%) entries with GSSO terms, compared
with the 82.62% covered with MeSH terms. Comparisons between
MeSH headings, Medline keywords, and GSSO terms for the HRC
terms are shown in Table 2. A total of 7022 MeSH terms (2.5% of

Journal of the American Medical Informatics Association, 2020, Vol. 27, No. 7

1113

Table 2. Term frequencies for most common 32 terms across main terminologies for the HRC subset

Word

HRC count

MeSH count

Keyword count

GSSO count

ally
androgynous
asexual
biphobia
bisexual
cisgender
closeted
coming out
gay
gender dysphoria
gender expression
gender identity
gender nonconforming
gender transition
gender-expansive
gender-ﬂuid
genderqueer
homophobia
intersex
lesbian
LGBTQ
living openly
nonbinary
outing
pansexual
queer
questioning
same-gender loving
sex assigned at birth
sexual orientation
transgender
transphobia

289
23
1288
3
2477
39
3
192
4426
277
24
725
11
10
0
0
8
276
598
2195
196
0
31
33
3
369
1219
2
0
1393
2102
17

NM
NM
NM
NM
2021
NM
NM
NM
3257
156
NM
1644
NM
NM
NM
NM
NM
197
561
1891
NM
NM
NM
NM
NM
NM
NM
NM
NM
NM
2078
NM

2
2
5
2
183
8
1
21
208
143
10
164
9
14
1
1
8
58
44
246
58
0
3
0
1
49
12
0
0
358
529
10

304
39
1307
14
3240
176
24
307
2356
394
61
1078
129
48
132
1
19
470
622
3182
271
0
12
0
13
594
1301
2
21
2044
2431
50

Note that because not all terms matched perfectly, the following mappings were made for the GSSO (androgynous ! androgynous gender expression; gender
nonconforming ! gender nonconforming; gender-expansive ! gender variance; sex assigned at birth ! sex at birth; gay ! gay man; nonbinary ! gender nonbi-
nary; gender-ﬂuid ! ﬂuctuating gender identity; same-gender loving ! same gender loving), for MeSH (bisexual ! bisexuality; gay ! homosexuality, male; in-
tersex ! disorders of sex development; lesbian ! homosexuality, female; transgender ! transgender persons þ transsexualism), and for keywords (androgynous
! androgyny). Mappings were made to prioritize MeSH-GSSO comparisons (eg, “gay” to “homosexuality, male” and “gay man”).

GSSO: Gender, Sex, and Sexual Orientation; HRC: Human Rights Campaign; MeSH: Medical Subject Headings; NM ¼ no mapping.

its corpus) were present in our dataset vs 8833 keywords (no defined
corpus) and 2911 GSSO terms (28.9% of its corpus).

lesbian (precision ¼ 0.53,

Of the 17 terms considered nonambiguous, calculating precision,
recall, and F-scores was only possible for 5 that were mappable to
MeSH:
recall ¼ 0.89, F-score ¼ 0.664),
transgender (precision ¼ 0.58, recall ¼ 0.76, F-score ¼ 0.658), gender
identity (precision ¼ 0.60, recall ¼ 0.39, F-score ¼ 0.473), gender
dysphoria (precision ¼ 0.30, recall ¼ 0.76, F-score ¼ 0.430), and
homophobia (precision ¼ 0.19, recall ¼ 0.46, F-score ¼ 0.269). Using
our criteria, 1 of our results was considered excellent (“transgender”)
and 3 were considered satisfactory (“lesbian,” “gender identity,” and
“gender dysphoria”).

With the randomly selected subset, we uploaded 1 217 621 Med-
line entries, of which 628 979 (50.66%) were tagged with GSSO
terms. A total of 1 058 065 (86.89%) had MeSH terms and 201 096
(16.52%) had keywords. A total of 27 813 MeSH terms (10.0% of
its corpus) were present in our dataset vs 306 728 keywords and
2579 GSSO terms (25.6% of its corpus).

The total number of unique GSSO terms utilized in both subsets
was 3733 (37.11%), with an intersection of 1757 terms between
sets. In comparison, MeSH terms had an intersection of 7006 terms.

DISCUSSION

The GSSO clarifies thousands of terms related to gender, sex, and
sexual orientation not present in any other biomedical ontology.
These areas continue to be controversial areas of research,2 with a
constantly evolving terminology. As writer Kyle Taylor Shaughnessy
noted in The Remedy: Queer and Trans Voices on Health and
Health Care: “While the constantly evolving language and concepts
of gender and sexual identity. . . can be overwhelming at times,
if we don’t keep up we lose the ability to connect and therefore
to do effective work.”35 The inclusion of source materials with
date information and usage notes helps provide context for termi-
nology (including derogatory terms) and makes the GSSO easily
updatable.

The lack of gender, sex, and sexual orientation terminology in
MeSH is significant, with only 8 of 32 common terms being directly
mappable to it. Additionally, there was no mapping for intersex,
with only the derogatory term “Disorders of Sex Development” be-
ing available. Assessing the reliability of what was considered a true
positive in our HRC query subset was challenging for this reason.
As a next step, we plan to manually curate a dataset and calculate

1114

Journal of the American Medical Informatics Association, 2020, Vol. 27, No. 7

Figure 2. Screenshots from mock-ups for web applications showcasing the GSSO with version 1 (left) and version 2 (right).

precision and recall values against that grouping as gold standard.
Manual curation will help us better understand the mapping
process.

The GSSO’s tagging system is fast, extensible, and reliable in sit-
uations in which terms are unambiguous. Despite its performance,
some GSSO term matches were missed or imprecise. For example,
gay was not matched at all, owing to it being only 3 characters in
length; likewise, asexual matched most articles relating to asexual
reproduction in nonhuman species, instead of asexuality as a sexual
orientation. Association rule mining or contextual tagging could
help minimize these problems moving forward.

In comparison with MeSH,

the GSSO was more specific,
matching more Medline entries in the HRC query subset with a
larger number of terms. This specificity carried over to the ran-
domly selected subset, in which it matched fewer abstracts but
had a much higher overlap of matched terms with the HRC
query subset.

Future directions include the release of the GSSO website cur-
rently in development (Figure 2) and evaluation and validation with
additional datasets. The website will support GSSO tagging within
text documents and will include a survey component to help track
changes and shifts in terminology usage over time.

The GSSO’s extensibility allows it to be used in a number of
applications including health surveillance of LGBTQIAþ social
media data, which is heavy in slang use; electronic health record
integration for identification of LGBTQIAþ patient groups; us-
age in clinical training programs as a comprehensive resource
for inclusiveness; and semiautomated LGBTQIAþ literature re-
view.

AUTHOR CONTRIBUTIONS

CAK conceived the research idea, designed and completed the ontology, per-
formed ontology analytics, and was the primary author of the manuscript.
JWD oversaw the project, contributed several critical revisions, and provided
feedback on analytical systems crucial to interpreting results. Both authors
agree to be accountable for all aspects of the work in ensuring that questions
related to the accuracy or integrity of any part of the work are appropriately
investigated and resolved.

ACKNOWLEDGMENTS

This document adheres to the principles outlined in the Declaration of Hel-
sinki. Special thanks to the following individuals for their assistance in this
work: Giao Q. Tran, Piper Ranallo, Charles Macquarie, Patti Brennan, K. J.
Rawson, Isaac Fellman, Florence Par(cid:2)e, Amber Billey, Marika Cifor, Walter
Walker, Jack van der Wel, and Brian M. Watson.

CONFLICT OF INTEREST STATEMENT

None declared.

REFERENCES

1. Wanta JW, Unger CA. Review of the transgender literature: where do we

go from here? Transgend Health 2017; 2 (1): 119–28.

2. Madsen TE, Bourjeily G, Hasnain M, et al. Article commentary: sex- and
gender-based medicine: the need for precise terminology. Gender Genome
2017; 1 (3): 122–8.

3. Mitchell M, Howarth C, Kotecha M, et al. Sexual orientation research re-
view 2008. https://www.equalityhumanrights.com/sites/default/ﬁles/re-
search_report_34_sexual_orientation_research_review.pdf
Accessed
January 23, 2020.

4. Moleiro C, Pinto N. Sexual orientation and gender identity: review of
concepts, controversies and their relation to psychopathology classiﬁca-
tion systems. Front Psychol 2015; 6: 1511. doi:10.3389/fpsyg.2015.
01511.

5. Munir K, Sheraz Anjum M. The use of ontologies for effective knowledge
modeling and information retrieval. Appl Comput Inform 2018; 14 (2):
116–26.

6. Harris DR. Modeling integration and reuse of heterogeneous terminolo-
gies in faceted browsing systems. In: 2016 IEEE 17th International Con-
ference on Information Reuse and Integration (IRI). Pittsburgh, PA: IEEE;
2016: 58–66.

7. Ren S, Lu X, Wang T. Application of ontology in medical heterogeneous
data integration. In: 2018 IEEE 3rd International Conference on Big Data
Analysis (ICBDA). Shanghai, China: IEEE; 2018: 150–5.

8. Clair K, Tg Q, Wd TY. Creating a queer ontology: the gender, sex, and
sexual orientation (GSSO) ontology. Stud Health Technol Inform 2019;
264: 208–12.

9. Noy NF, Shah NH, Whetzel PL, et al. BioPortal: ontologies and integrated
data resources at the click of a mouse. Nucleic Acids Res 2009; 37:
W170–3.

Journal of the American Medical Informatics Association, 2020, Vol. 27, No. 7

1115

10. Whetzel PL, Noy NF, Shah NH, et al. BioPortal: enhanced functionality
via new Web services from the National Center for Biomedical Ontology
to access and use ontologies in software applications. Nucleic Acids Res
2011; 39 (suppl): W541–545.

11. Noy NF, McGuinness DL. Ontology development 101: a guide to creating
your ﬁrst ontology. https://protege.stanford.edu/publications/ontology_
development/ontology101.pdf Accessed April 20, 2020.

22. Glossary of Terms. https://www.hrc.org/resources/glossary-of-terms

Accessed April 8, 2020.

23. PFLAG National Glossary of Terms. https://web.archive.org/web/
20180310211422/https://www.pﬂag.org/glossary Accessed March 10,
2018.

24. Billey A, Cifor M, Kronk C, et al. Homosaurus. http://homosaurus.org/

Accessed February 3, 2020.

12. Bosse JD, Chiodo L. It is complicated: gender and sexual orientation iden-

25. Ganin N. QueerLCSH. 2020. http://www.netanelganin.com/projects/

tity in LGBTQ youth. J Clin Nurs 2016; 25 (23–24): 3665–75.

QueerLCSH/QueerLCSH.html Accessed February 3, 2020.

13. Beek TF, Cohen-Kettenis PT, Kreukels B. Gender incongruence/gender dys-

phoria and its classiﬁcation history. Int Rev Psychiatry 2016; 28 (1): 5–12.

14. Song MM, Simonsen CK, Wilson JD, et al. Development of a PubMed
based search tool for identifying sex and gender speciﬁc health literature. J
Womens Health (Larchmt) 2016; 25 (2): 181–7.

15. Musen MA. The prot(cid:2)eg(cid:2)e project: a look back and a look forward. AI Mat-

ters 2015; 1 (4): 4–12.

16. Corcho O, Fern(cid:2)andez-L(cid:2)opez M, G(cid:2)omez-P(cid:2)erez A. Methodologies, tools
and languages for building ontologies. Where is their meeting point. Data
Knowl Eng 2003; 46 (1): 41–64.

17. CNN Politics. Democratic hopefuls pressed on gay issues at forum. 2007.
https://www.cnn.com/2007/POLITICS/08/10/gay.forum/ Accessed Febru-
ary 12, 2020.

18. HRC Story. 2020. https://www.hrc.org/hrc-story Accessed February 12,

2020.

19. Gates GJ. How many people are lesbian, gay, bisexual, and transgender?
http://williamsinstitute.law.ucla.edu/wp-content/uploads/Gates-

2011.
How-Many-People-LGBT-Apr-2011.pdf Accessed April 22, 2019.

20. Gutierrez-Morﬁn N. GLAAD ofﬁcially adds the “Q” to LGBTQ. NBC
News. 2016. https://web.archive.org/web/20161030095844/https://www.
nbcnews.com/feature/nbc-out/glaad-ofﬁcially-adds-q-lgbtq-n673196
Accessed October 30, 2016.

26. Johnson HL, Cohen KB, Baumgartner WA, et al. Evaluation of lexical
methods for detecting relationships between concepts from multiple ontol-
ogies. Pac Symp Biocomput; 2006; 2006: 28–39.

27. Saitwal H, Qing D, Jones S, et al. Cross-terminology mapping challenges:
A demonstration using medication terminological systems. J Biomed In-
form 2012; 45 (4): 613–25.

28. Barros FA, Gonc¸alves PF, Santos T. Providing context to web searches:
the use of ontologies to enhance search engine’s accuracy. J Braz Comp
Soc 1998; 5 (2). doi: 10.1590/S0104-65001998000300005.

29. Thenmalar S, Geetha TV. Enhanced ontology-based indexing and search-

ing. ASLIB J Inf Manage 2014; 66 (6): 678–96.

30. Francoeur RT, ed. The Complete Dictionary of Sexology. New York, NY:

Continuum; 1995.

31. Wong A, Wickramasinghe M, Hoogland R, et al. The Wiley Blackwell En-
cyclopedia of Gender and Sexuality Studies. Singapore: Wiley; 2016.
32. Hawley JC, Nelson ES. LGBTQ America today: an encyclopedia. West-

port, CT: Greenwood; 2008.

33. Summers CJ. glbtq Encyclopedia Project. 2015. http://www.glbtqarchive.

com/ Accessed March 15, 2020.

34. Dynes WR. Encyclopedia of Homosexuality. 1990. http://williamapercy.
title¼Encyclopedia_of_Homosexuality Accessed

com/wiki/index.php?
March 15, 2020.

21. GLAAD Media Reference Guide-10th Edition. 2016. https://web.archive.

35. Cahill S. LGBT experiences with health care. Health Aff (Millwood)

org/web/20180311000209/http://www.glaad.org/sites/default/ﬁles/
GLAAD-Media-Reference-Guide-Tenth-Edition.pdf Accessed March 11,
2018.

2017; 36 (4): 773–4.
