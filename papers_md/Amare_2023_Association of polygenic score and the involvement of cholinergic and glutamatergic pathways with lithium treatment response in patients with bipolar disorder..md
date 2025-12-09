# Amare_2023_Association of polygenic score and the involvement of cholinergic and glutamatergic pathways with lithium treatment response in patients with bipolar disorder.

Molecular Psychiatry

www.nature.com/mp

OPEN

ARTICLE
Association of polygenic score and the involvement of
cholinergic and glutamatergic pathways with lithium treatment
response in patients with bipolar disorder

Azmeraw T. Amare

1 ✉

et al.

© The Author(s) 2023

:
,
;
)
(
0
9
8
7
6
5
4
3
2
1

Lithium is regarded as the ﬁrst-line treatment for bipolar disorder (BD), a severe and disabling mental health disorder that affects
about 1% of the population worldwide. Nevertheless, lithium is not consistently effective, with only 30% of patients showing a
favorable response to treatment. To provide personalized treatment options for bipolar patients, it is essential to identify prediction
biomarkers such as polygenic scores. In this study, we developed a polygenic score for lithium treatment response (Li+
patients with BD. To gain further insights into lithium’s possible molecular mechanism of action, we performed a genome-wide
gene-based analysis. Using polygenic score modeling, via methods incorporating Bayesian regression and continuous shrinkage
priors, Li+
PGS was developed in the International Consortium of Lithium Genetics cohort (ConLi+Gen: N = 2367) and replicated in
the combined PsyCourse (N = 89) and BipoLife (N = 102) studies. The associations of Li+
PGS and lithium treatment response —
deﬁned in a continuous ALDA scale and a categorical outcome (good response vs. poor response) were tested using regression
models, each adjusted for the covariates: age, sex, and the ﬁrst four genetic principal components. Statistical signiﬁcance was
determined at P < 0.05. Li+
PGS was positively associated with lithium treatment response in the ConLi+Gen cohort, in both the
categorical (P = 9.8 × 10−12, R2 = 1.9%) and continuous (P = 6.4 × 10−9, R2 = 2.6%) outcomes. Compared to bipolar patients in the
1st decile of the risk distribution, individuals in the 10th decile had 3.47-fold (95%CI: 2.22–5.47) higher odds of responding favorably
to lithium. The results were replicated in the independent cohorts for the categorical treatment outcome (P = 3.9 × 10−4,
R2 = 0.9%), but not for the continuous outcome (P = 0.13). Gene-based analyses revealed 36 candidate genes that are enriched in
biological pathways controlled by glutamate and acetylcholine. Li+
PGS may be useful in the development of pharmacogenomic
testing strategies by enabling a classiﬁcation of bipolar patients according to their response to treatment.

PGS) in

Molecular Psychiatry (2023) 28:5251–5261; https://doi.org/10.1038/s41380-023-02149-1

INTRODUCTION
Bipolar disorder (BD) is a severe and often disabling mental health
disorder that affects more than 1% of the population worldwide and
is characterized by recurrent episodes of depression and mania [1]. BD
accounted for 9.3 million disability-adjusted life years (DALYs) in 2017,
and imposes a signiﬁcant social and economic burden on society and
healthcare systems [2, 3]. BD is associated with a signiﬁcant somatic
and psychiatric comorbidity [1] and an increased risk of suicide [4].
Since the discovery of lithium’s mood-stabilizing property in
1949 [5], it has been widely used as a ﬁrst-line therapy for patients
with BD [6, 7]. Lithium is effective in treating acute episodes of
illness and reduces the risk of future recurrences of mania and
depression [8]. It has also been shown to reduce the risk of suicide
[9]. Despite these merits, the efﬁcacy of lithium is highly variable,
with about 30% of treated patients showing a favorable response
while more than 30% of them have no clinical response at all
[8, 10]. Thus far, the causes and predictors of such heterogeneity
in treatment response are insufﬁciently understood.

Genetic factors are thought to contribute, at least in part, to the
large interindividual differences in response to lithium [10–15]. So far,

only a few genetic studies have identiﬁed speciﬁc single nucleotide
polymorphisms (SNPs) and candidate genes associated with patients’
response to lithium or treatment-related side effects [10, 11, 13–16].
Each employing a genome-wide association study (GWAS) approach,
the Taiwan Bipolar Consortium found SNPs in the introns of GADL1
response [17], whereas the
associated with lithium treatment
International Consortium on Lithium Genetics (ConLi+Gen) identiﬁed
a locus on chromosome 21 [10], and a follow-up analysis uncovered
additional variants within the human leukocyte antigen (HLA) region
[14, 16]. Gene expression analysis of ConLi+Gen data also showed
overexpression of genes involved in mitochondrial functioning in
lithium responder patients, highlighting the electron transport chain
as a potential target of lithium [18].

In our recent work, we applied a polygenic score (PGS) modeling
approach and demonstrated associations between a poor response
to lithium and a high genetic loading for schizophrenia (SCZ) [14],
major depression (MD) [13], or a meta-PGS combining both SCZ and
MD [15]. Machine-learning models that combined clinical variables
with the PGS of SCZ and MD has further improved the prediction of
lithium treatment response, explaining 13.7% of the variance [19].

A full list of authors and their afﬁliations appears at the end of the paper.

✉

email: azmeraw.amare@adelaide.edu.au

Received: 12 February 2023 Revised: 31 May 2023 Accepted: 16 June 2023
Published online: 11 July 2023

5252

A.T. Amare et al.

Fig. 1 Overview of input datasets and steps of data analyses. ConLi+Gen = The International Consortium on Lithium Genetics, ALDA =
Retrospective Criteria of Long-Term Treatment Response in Research Subjects with Bipolar Disorder scale, HRC = Haplotype Reference
Consortium, SNPs = Single Nucleotide Polymorphisms, MAF=Minor Allele Frequency, GWAS = Genome Wide Association analysis, Li+
PGS =
Polygenic score for lithium treatment response, LOG = Leave-one-group out procedure; PsyCourse = Pathomechanisms and Signature in the
Longitudinal Course of Psychosis study and BipoLife = German research consortium for the study of bipolar disorder.

Based on these previous results, translation of PGS testing into
clinical practice requires the consideration of three important
learnings. First, the PGS of a single phenotype (e.g., SCZ or MD)
explains only a small proportion (<2%) of the variability to
treatment response in patients with BD [13, 14], providing
insufﬁcient power for clinical use. Second, a meta-PGS from
multiple related phenotypes has better predictive power than a
PGS from a single phenotype [15], suggesting the need to
explore additional biological markers, including additional PGSs,
that can either independently or together with existing PGSs
better predict lithium treatment response. Third, developing
polygenic markers with direct pharmacogenomic implications is
essential, for example, a PGS for lithium treatment response
(Li+
PGS), which is perhaps biologically more related to lithium’s
for other clinical
pharmacological actions than PGSs built
that may indirectly inﬂuence
phenotypes (i.e., SCZ or MD;
treatment response or symptom severity, but do not index
pharmacogenetic signatures per se).
Here, we developed a novel Li+

PGS for lithium treatment
response and applied gene-based pathway analyses to identify
molecular mechanisms
impacted by genetic variation in
response phenotypes. Findings may assist in optimizing and
personalizing the selection of mood stabilizers in patients with
BD, and may point to novel molecular targets for future drug
development.

METHODS AND MATERIALS
Study samples
For this study, we obtained genetic and clinical data from the International
Consortium on Lithium Genetics (ConLi+Gen: N = 2367), Pathomechanisms
and Signature in the Longitudinal Course of Psychosis study (PsyCourse:
N = 89), and BipoLife cohort (N = 102). Figure 1 shows the detailed steps of
data analysis.

Discovery cohort
ConLi+Gen is a global collaboration of scientists established to study the
pharmacogenomics of lithium treatment in patients with BD [10]. In the
current study, we analyzed the genome-wide genotype and clinical data of
2367 lithium-treated bipolar patients of European ancestry collected by 22
including Australia (n = 122), Austria
participating sites in 13 countries,
(n = 43), Czech Republic (n = 45), France (n = 210), Germany (n = 218),
Italy (n = 255), Poland (n = 97), Romania (n = 152), Spain (n = 74), Sweden
(n = 304), Switzerland (n = 57), Canada (n = 353) and the USA (n = 437)
[10, 20].

Replication cohort
PGS associations found in the discovery ConLi+Gen sample,
To replicate Li+
we utilized datasets from PsyCourse and BipoLife where the study
participants were of European ancestry. PsyCourse is a longitudinal
multicenter study conducted from 2012 to 2019 in Germany and Austria,
with up to four assessments at 6 monthly intervals. The study comprises
1320 patients from psychotic-to-affective spectrum, of which, datasets

Molecular Psychiatry (2023) 28:5251 – 5261

from 89 patients with BD who received lithium treatment were obtained
for this study [21]. BipoLife is a multicenter cohort study, established to
investigate the biological basis of BD and patients’ response to treatment
and being conducted across ten university hospitals in Germany (Berlin,
Bochum, Dresden, Frankfurt, Göttingen, Hamburg, Heidelberg, Marburg,
Munich and Tübingen) and the medical
the
University of Göttingen [22].

informatics section of

Target outcome
In both discovery and replication cohorts, patient’s treatment response
was assessed using the “Retrospective Criteria of Long-Term Treatment
Response in Research Subjects with Bipolar Disorder” scale, also called the
ALDA scale [10]. The target outcome “lithium treatment response” was
deﬁned in categorical and continuous scales among patients who had
received lithium for a minimum of 6 months [10]. In both the discovery
ConLi+Gen cohort and the replication cohorts (PsyCourse and BipoLife), a
minimum of 6 months of lithium treatment follow-up was implemented as
an inclusion criterion. This duration was chosen based on previous
analyses of clinical trials, which established that a 6-month follow-up
period is appropriate for assessing the minimum efﬁcacy of lithium in
patients with bipolar disorder [23]. Furthermore, clinical guidelines highly
recommended to regularly monitor lithium levels during the initial six
months of treatment, as this period is characterized by potential variability
in lithium concentrations and an increased likelihood of side effects. After
the six-month mark, stable lithium concentrations are typically achieved,
allowing for an evaluation of the risk of toxicity and patients’ adherence to
treatment. These factors ultimately inﬂuence the effectiveness of the
treatment [24–26]. The detailed procedures of ALDA scale measurement
and its validity are described elsewhere [13, 14, 20]. Brieﬂy, the ALDA scale
consists of two subscales: the A scale and the B scale. The A scale measures
the response to lithium treatment on a continuum ranging from 0 to 10.
Assessors evaluate the change in illness activity while the patient is
receiving lithium, and the response is rated accordingly. The anchor points
for the A scale range from no change or worsening (score = 0) to complete
response, which includes no recurrences during adequate treatment, no
residual symptoms, and full functional recovery (score = 10). On the other
hand, the B scale describes ﬁve factors that could potentially confound the
response to lithium treatment or the interpretation of its magnitude. These
factors are the number and frequency of episodes before starting lithium
(B1 and B2, respectively), the duration of lithium treatment (B3), adherence
to the prescribed lithium regimen (B4), and the use of additional
medications (B5). Each item on the B scale is rated on a scale of 0 to 2,
with a higher B score indicating a lower level of conﬁdence that any
observed clinical
improvement is solely due to lithium [27]. Once we
calculated the total score as ‘A-score minus B-score and setting negative
scores to zero’, the categorical
lithium treatment
response was deﬁned at a cut-off score of 7, where patients with a total
score of 7 or higher were considered as “responders” [10]. The continuous
outcome for lithium treatment response was deﬁned on subscale-A, but
patients with a total B score greater than 4 or who had missing data on the
totals of ALDA subscale-A or B were excluded [10].

(good versus poor)

Genotyping, quality control and imputation. We obtained the genotype
data assayed with different types of commercial SNP arrays across multiple
cohorts [10, 21, 22] and applied a series of quality control (QC) procedures
before and after imputation using PLINK [28]. First, SNPs that had a poor
genotyping rate (<95%), strand ambiguity (A/T and C/G SNPs), a minor
allele frequency (MAF) less than 1% or showed deviation from Hardy-
Weinberg Equilibrium (P < 10−6) were removed. Then, individuals with low
genotype rates (<95%), who had sex inconsistencies (between the
documented and genotype-derived sex), and who were genetically related
were excluded.

(https://imputationserver.sph.umich.edu)

Imputation
The genotype data passing QC were imputed on the Michigan server
[24, 29]
separately for each
genotyping platform, using the Haplotype Reference Consortium (HRC)
reference panel that consists of the largest available set (64,976 human
haplotypes) of broadly European haplotypes at 39,235,157 SNPs [30]. For
each cohort, imputation quality procedures were implemented to exclude
SNPs of low-frequency (MAF < 10%) and low-quality (imputation quality
score R-square < 0.6). From the imputed dosage score, genotype calls for
the ﬁltered SNPs were derived and common sets of 4,652,947 SNPs across
the cohorts were merged using PLINK [28].

Molecular Psychiatry (2023) 28:5251 – 5261

A.T. Amare et al.

5253

Statistical analysis
We implemented polygenic score modeling, genome-wide SNP associa-
tion, gene-based and functional analysis as described below.

Genome-wide SNP association analysis. Genome-wide SNP association
analyses were performed on the binary lithium treatment response and
continuous ALDA total score using logistic and linear regression models as
implemented in PLINK software [28], respectively. Each analysis was
adjusted for the covariates: age, sex, chip type and the ﬁrst four genetic
principal components (PCs). After careful examination of
the Multi-
dimensional (MD) plot, we observed that the ﬁrst four PCs successfully
captured and delineated any underlying population structure that could
potentially inﬂuence the genetic association analyses. Consequently, these
four PCs were incorporated as covariates in all association analyses. This
approach aligns with the methodology employed by previous researchers
who utilized the same dataset [10].

Polygenic score development. Using a polygenic score model constructed
via Bayesian regression framework and continuous shrinkage (CS) prior on
SNP effect sizes implemented in the PRS-CS software [31], we built Li+
PGS
for individuals of European descent who participated in the ConLi+Gen
study and replicated the ﬁndings in the combined PsyCourse and BipoLife
datasets. Polygenic scores were computed using PRS-CS to infer posterior
SNP effect sizes under continuous shrinkage (CS) using GWAS summary
statistics and an external linkage disequilibrium (LD) reference panel. For
the current analysis, the precomputed LD pattern of the 1000 Genomes
European reference panel [32] and the discovery GWAS summary statistics
were used to calculate PGS scores.
For the ConLi+Gen study, Li+

PGS was derived only for the European
ancestry individuals (n = 2367) using a ﬁve-fold leave-one-group out (LOG)
procedure [33] to remove discovery-target circularity. In each fold, 80% of
the sample (n = 1893) was used to generate GWAS summary statistics that
were used as discovery for PGS calculation in the 20% left-out target
sample (n = 474). The procedure was repeated ﬁve times by selecting a
non-overlapping set of 20% left-out samples to calculate PGS for the entire
cohort. Finally, Li+
PGS was computed for the PsyCourse and BipoLife
participants using ConLi+Gen’s GWAS summary statistics (discovery
sample) generated from the full European cohort (n = 2367).

To assess the association of Li+

Polygenic score association analysis.
PGS
with lithium treatment response, a binary logistic regression model was
applied for the binary outcome (good versus poor response to lithium
treatment), and a Tobit analysis model (censored regression) was used for
the continuous outcome (ALDA total) [34].
In addition, we divided the
ConLi+Gen sample into deciles, ranging from the lowest polygenic load
(1st decile, reference group) to the highest polygenic load (10th decile).
Then, we compared BD patients in the higher polygenic load deciles
(2nd–10th deciles) with patients in the lowest polygenic load decile (1st
decile). In both the binary and continuous outcomes, the proportion of
phenotypic variance explained by Li+
PGS was computed as the difference
in R2 of the model ﬁt with Li+
PGS plus covariates, compared to the model ﬁt
with only covariates. Each modeling analysis was adjusted for
the
covariates: age, sex, and the ﬁrst
four genetic PCs, and statistical
signiﬁcance was set at p < 0.05.

Gene-based and functional analysis.
The gene-based analysis was based
on summary statistics generated through genome-wide SNP association
analysis of the full European ConLi+Gen sample (n = 2367) and employed
MAGMA (Multi-marker Analysis of GenoMic Annotation) [35], a tool that
uses a multiple regression approach to incorporate LD between markers
and to detect multi-marker effects.

ANalysis

THrough

Evolutionary

Relationships;

To explore the biological context of the genes discovered from the
gene-based analysis, a pathway analysis was implemented using PANTHER
http://
(Protein
pantherdb.org/) classiﬁcation system. PANTHER is designed to classify
proteins (and their genes) into biological pathways [36]. To prepare the
input genes for PANTHER, we selected genes that showed gene-level
association with lithium treatment response (either with the categorical or
continuous outcome) at MAGMA adjusted p-value < 0.001. This list of
genes was entered into PANTHER version-17 which compares the
proportion of
input genes mapping to a biological pathway to the
reference gene list from its databases. Molecular relationships previously
experimentally observed in Homo sapiens (human) were included. The
signiﬁcance of the overrepresented PANTHER pathways was determined
using Fisher’s exact test and later adjusted for multiple testing using the

5254

Bonferroni correction method. Signiﬁcant associations were deﬁned at
p-value < 0.05.

A.T. Amare et al.

RESULTS
Sample characteristics
The discovery analysis consisted of ConLi+Gen data obtained from
2,367 bipolar patients of European ancestry who had undergone
lithium treatment for at least six months. The mean (sd) age of the
patients was 47.5(13.9) years and 1,369 (57.8%) were female. In all,
660 (27.9%) of patients had a good response to lithium treatment
(ALDA score ≥7). The mean (sd) ALDA score for ConLi+Gen
participants was 4.1 (3.1). Among 2362 patients who underwent
assessment for the type of bipolar diagnosis, the majority (80.0%)
were diagnosed with type 1 bipolar disorder. These patients also
presented with comorbid conditions such as psychosis, alcohol
dependence, panic disorder, and obsessive-compulsive disorder. Of
the 438 patients assessed for possible side effects related to lithium
treatment, 153(34.9%) of them reported experiencing at least one of
the following: nausea, vertigo, polyuria, diarrhea, hypothyroidism,
loss of libido, EEG abnormalities, increased thirst, dermal problems,
weight gain, and strangury. The replication analysis was based on a
combination of the PsyCourse and BipoLife datasets (N = 191),
whose mean (sd) age was 49.1(13.0) years. Of the 191 patients with
BD, 48(25.1%) had a good response to lithium. This replication
cohort exhibits similar characteristics to the discovery sample in
terms of the type of bipolar disorder, comorbidities, and patients’
reports of lithium treatment side effects (Table 1).

PGS with lithium treatment response in

PGS load. Table 2 shows the association results of Li+

Associations of Li+
bipolar patients
Using ConLi+Gen data, we found statistically signiﬁcant associa-
tions between Li+
PGS and lithium treatment response — both in
(P = 9.8 × 10−12, R2 = 1.9%) and continuous
the categorical
(P = 6.4 × 10−9, R2 = 2.6%) outcomes. Li+
PGS was positively asso-
ciated with response to lithium treatment, with an adjusted odds
ratio (OR) [95%CI]) of 1.39 [1.26, 1.54]. In other words, BD patients
who carry a higher genetic loading for lithium responsive genetic
variants, measured using the Li+
PGS, have higher odds of favorable
lithium treatment response, compared to patients carrying a low
Li+
PGS and
lithium treatment response in categorical and continuous out-
comes. The odds of a favorable treatment response increased as
the Li+
PGS increased, ranging from 1.59 fold [95%CI: 1.02–2.49] at
the 2nd decile to 3.47 fold [95%CI: 2.22–5.47] at 10th decile,
compared to the reference Li+
PGS at the 1st decile (Table 2). While
there was an increasing trend in the odds of lithium treatment
the most signiﬁcant prediction
response across the deciles,
contrast was found at the ‘extremes’ (1st and 10th decile) which
comprised of ~20% of the total cohort (Fig. 2). A replication PGS
analysis in the combined PsyCourse and BipoLife samples found a
statistically signiﬁcant association of Li+
PGS with the categorical
lithium treatment response (P = 3.9 × 10−4, R2 = 0.9%), but not
with the continuous outcome (P = 0.13).

Genome-wide association, gene-based and functional analysis
After re-imputing the ConLi+Gen data in reference to the latest HRC
genomes, we conducted GWASs on lithium response, both in
categorical and continuous outcomes. This GWAS analysis identiﬁed
a single locus with lead SNP rs9396756 located near the stathmin
domain containing 1 (STMND1) gene that reached genome-wide
signiﬁcance
outcome
(P = 2.7 × 10−8)
association with
the continuous ALDA score (P = 7.6 × 10−8)
(Fig. 3). A follow-up
gene-based analysis of the newly derived ConLi+Gen GWAS summary
statistics found 36 candidate genes likely associated with lithium
treatment response — assessed in either continuous or categorical
In silico functional analysis of the 36 genes
outcomes (P < 0.001).

the
suggestive

association with

and showed a

categorical

for

Table 1.
outcomes.

The characteristics of patients with BD and lithium treatment

Characteristics BD patients

ConLi+Gen

N = 2558
Good responders to lithium
deﬁned as ALDA total score
≥ 7, N (%)
Mean (se) total ALDA score

Country of origin

Australia

Austria

Canada

Czech Republic

France

Germany

Italy

Poland

Romania

Spain

Sweden

Switzerland

USA

Age at interview, mean (sd)

Sex, Female, N (%)

N = 2,367
660 (27.9%)

4.12 (3.15)
N (%)
122 (5.2)

43 (1.8)

353 (14.9)

45 (1.9)

210 (8.9)

218 (9.2)

255 (10.8)

97 (4.1)

152 (6.4)

74 (3.1)

304 (12.8)

57 (2.4)

437 (18.5)

47.5 (13.9)

1369 (57.8)

PsyCourse and
BipoLife
combined
N = 191
48 (25.1%)

4.3 (2.9)
N (%)

191 (100%)

49.1 (13.0)

84 (44.0%)

Type of bipolar diagnosis, N (%)

2362 (99.8)

89 (46.6)

Bipolar type I

Bipolar type II

Bipolar type III
Bipolar not speciﬁed
Schizoaffective bipolar
disorder

Comorbidity

Psychosis

Alcohol dependence

Panic disorder

Obsessive-compulsive
disorder

Suicidal ideation

Lithium side effects

1890(80.0)

440(18.6)

75(84.3)

14(15.7)

7(0.3)

7(0.3)

18(0.8)

N¥ (% with)
2096 (53.2)

N¥ (% with)
103 (3.9)

933 (18.0)

926 (13.6)

923 (5.2)

-

438 (34.9)

102 (5.9)

102 (8.8)

103 (2.9)

98 (66.3)

102 (83.3)

BD Bipolar disorder, N Number of individuals in each group, sd Standard
deviation, se Standard error.
N¥ refers to the number of individuals assessed for comorbidities, suicidal
ideation or lithium side effects.

revealed enriched biological pathways including the muscarinic
acetylcholine receptors 1 and 3 (P-value corrected for multiple
testing = 0.026) and metabotropic glutamate receptor group III
pathway (P = 0.043). These genes and pathways may have an impact
on clinical response to lithium treatment and be potential molecular
targets for lithium (Supplementary Figure 1 and Table 1).

DISCUSSION
This study presents ﬁndings from a comprehensive analysis of
genetic and clinical data on lithium treatment response that
lithium
involved the development of a polygenic score for

Molecular Psychiatry (2023) 28:5251 – 5261

A.T. Amare et al.

5255

Table 2.

The association of PGS for lithium variants and treatment response to lithium in patients with BD at different sample splits.

Sample split

N

Categorical outcome, OR (95%CI)

Continuous outcome: ALDA total score,
OR (95%CI)

ConLi+Gen
80%/20%
Li+
PGS by decile
First (lowest score)

Second

Third

Fourth

Fifth

Sixth

Seventh

Eighth

Nineth

2367

2083/284
§R/N
44/236

60/237

54/237

70/237

59/236

62/237

76/237

68/237

78/237

unadjusted

1.31(1.19,1.43)

adjusted
1.39(1.26, 1.54) ¥

unadjusted

1.15(1.11, 1.20)

1[Reference]

1.48(0.96, 2.30)

1.29(0.82, 2.02)

1.83(1.19, 2.83)

1.45(0.94, 2.27)

1.55(1.00, 2.40)

2.06(1.35, 3.17)

1.76(1.14, 2.72)

2.14(1.41, 3.29)

1[Reference]¥
1.59(1.02, 2.49)

1.32(0.84, 2.08)

1.87(1.21, 2.91)

1.50(0.96, 2.35)

1.83(1.17, 2.87)

2.27(1.48, 3.53)

1.91(1.23, 2.99)

2.33(1.51, 3.64)

1[Reference]

0.94(0.79,1.12)

1.07(0.90,1.28)

1.09(0.92,1.31)

1.12(0.93,1.34)

1.22(1.02,1.46)

1.15(0.96,1.38)

1.12(0.93,1.34)

1.45(1.21,1.72)

adjusted¥
1.17(1.13, 1.22)

1[Reference]

0.96(0.81,1.15)

1.14(0.95,1.35)

1.14(0.96,1.36)

1.17(0.98,1.40)

1.31(1.09,1.55)

1.23(1.04,1.48)

1.17(0.98,1.39)

1.55(1.31,1.86)

Tenth (highest score)
1.67(1.39,1.99)
The reference decile (1st decile) is the PGS category with the lowest polygenic load for lithium variants. OR (95%CI) for the continuous outcome: ALDA total
score is calculated as the exponent of beta coefﬁcient from the linear regression model.
§R/N: number of lithium responders versus total in that decile; ¥ adjusted for age, sex and 4-genetic principal components, OR: odds ratio.

3.47(2.22, 5.47)

2.64(1.74, 4.05)

1.52(1.27,1.82)

89/236

treatment response (Li+
gene-based and functional analyses.

PGS), genome-wide SNP association and

Since the publication of

the ﬁrst GWAS report by the
ConLi+Gen team [10], two landmark studies that independently
showed the negative association of PGSs for SCZ and MD with
lithium treatment response have been published [13–15]. The
ﬁrst study found that 10% of bipolar patients with the lowest
polygenic load for SCZ were 3.46 times more responsive to
lithium compared to 10% of patients with the highest genetic
load for SCZ [14, 15]. Similarly,
in the second study, 10% of
patients who had the lowest genetic loading for MD were 1.54
times more responsive to lithium than 10% of patients with the
highest genetic loading for MD [13, 15]. Nevertheless, each of
these PGSs accounts for <2% of the total variance to lithium
treatment
response [13], suggesting the need to explore
additional biological traits that can either independently, or in
concert with existing PGSs better predict
lithium response.
Moreover, the previous PGSs for SCZ and MD are difﬁcult to
interpret in a pharmacogenomic context, making the develop-
ment of a speciﬁc lithium response PGS necessary, which is
assumed to be more likely to be associated with lithium
treatment response and perhaps is biologically more related to
lithium’s pharmacological actions.

In this novel study, we constructed a PGS for lithium response-
Li+
PGS, a biological marker of direct pharmacogenomic rele-
vance, and showed a positive relationship between a high
genetic loading for lithium treatment response variants and
long-term therapeutic response to lithium in patients with BD.
We demonstrated that bipolar patients at the extreme tail end of
the distribution have the strongest association,
i.e. 10% of
patients who carry high genetic loading for lithium responsive
variants (10th decile) were 3.47 times more likely to respond to
lithium compared to 10% of those with the lowest Li+
PGS (1st
decile). These results indicated that Li+
PGS has the potential to
help stratify bipolar patients according to predicted lithium
response.

In a GWAS of lithium treatment response, we identiﬁed a locus
near the STMND1 gene, which encodes for proteins known to be
involved in neuron projection development, and active in neuron
junctions and cytoplasm. Previous analysis that employed the
1000 Genomes Project reference panel for imputation reported a

Molecular Psychiatry (2023) 28:5251 – 5261

suggestive association between genetic variants within the
STMND1 gene and lithium treatment response [10].

Using our newly derived ConLi+Gen GWASs summary statistics
as an input, we then carried out a gene-based analysis where
several genetic variations were examined together
their
association with lithium treatment response [35]. This approach
found 36 potential target genes for lithium treatment that are
enriched in the muscarinic acetylcholine receptors (mAChRs) 1
and 3 and the metabotropic glutamate receptor group III signaling
pathways — well characterized biological pathways modulated by
the most abundant neurotransmitters in the brain (glutamate and
acetylcholine).

for

Acetylcholine is the central regulator of the mAChRs signaling
pathways, which are subfamily of G protein-coupled receptor
complexes located in the cell membranes of neurons and other
cells that regulate fundamental functions of the central and
peripheral nervous system including acting as the main end-
receptor stimulated by acetylcholine released from postganglio-
nic ﬁbers in the parasympathetic nervous system [37]. The
muscarinic antagonist scopolamine has antidepressant activity,
while physostigmine, a cholinesterase inhibitor induces depres-
sive symptoms, suggesting muscarinic receptors may play a role,
not only in the pathogenesis of mood disorders, but also as
therapeutic targets [38]. M1 and 3 receptors are localized in the
cortex, hippocampus and substantia nigra and are known to
activate protein kinase C (PKC), causing post-synaptic excitation.
PKC is thought to be central
in the molecular pathogenesis
of BD.

Glutamate,

the primary excitatory neurotransmitter

in the
central nervous system (CNS), exerts neuromodulatory actions
via the activation of metabotropic glutamate (mGlu), a type of
glutamate receptor that modulates synaptic transmission and
neuronal excitability throughout the central nervous system [39].
Group III metabotropic glutamate receptors are largely presynap-
tically localized and downregulate neurotransmitter release from
presynaptic terminals directly or indirectly. These receptors have a
prominent expression in the brain, especially in the region of the
hippocampus, and can lead to the inhibition of the cAMP cascade
which is critical
long-term synaptic
the maintenance of
plasticity [40]. Growing evidence indicates that abnormalities in
the glutamatergic system are implicated in the pathogenesis and

for

5256

A.T. Amare et al.

Fig. 2 Trends in the odds ratios (ORs) for favourable treatment response to lithium for patients with bipolar disorder in the higher
genetic loading for lithium responsive variants, (2nd to 10th deciles) compared with patients in the lowest (1st decile) of genetic loading
for lithium response (n = 2367). The X mark on the line plot indicates that the association is not statistically signiﬁcant at that decile. OR Odds
ratio, CI Conﬁdence interval, Li+

PGS Polygenic score for lithium treatment response.

treatment of mental health disorders [41] including BD [42, 43],
SCZ [44], neurodevelopmental disorders [45], Huntington’s disease
[46] and Alzheimer’s disease [47]. Studies have reported SNPs of
the mGluRs system associated with BD [48], and in animal studies,
lithium was found to alter intracellular calcium by modulating the
activity of the metabotropic glutamatergic receptor system [49].
To summarise, ﬁndings from the genome-wide SNP association,
gene-based and functional analysis highlight the possibility that
mechanisms involving glutamate and acetylcholine signaling
pathways might inﬂuence the therapeutic effects of lithium in
patients with BD. Modulation of these pathways through genetic
variants may disrupt or enhance lithium’s clinical effectiveness.

Our study has some limitations. First, while our ﬁndings were
replicated in an independent small size sample, the fact that it was
replicated in the binary outcome, but not in the continuous
outcome indicates the need for a larger
replication cohort.
Second, because Li+
PGS was developed and evaluated in
European-ancestry populations, the ﬁndings should be replicated
in a multi-ethnic population to gauge generalizability. Further-
more, the risks and beneﬁts of predictive models consisting of
Li+
PGS should be evaluated in prospective studies. Third, Li+
PGS
only explains about 2% of response variance in our cohort, and as
such is comparable to PGSs from other phenotypes (SCZ, MDD)
that have shown an association with treatment outcomes. On
their own, these PGSs are not suited to clinical pharmacogenomic
testing as they would not predict treatment response prospec-
tively in individual patients. Prediction models combining Li+
PGS
with other PGSs [13, 14] and clinical characteristics [19] may
improve the clinical utility of PGSs. Such models would then need
to be tested in prospective studies and clinical trials. Forth, studies
have shown that approaches to phenotyping of lithium treatment
response can be improved using advanced methods such as
machine learning [19]. Employing a more precise phenotype
deﬁnition may result in the identiﬁcation of novel candidate genes

PGS. Fifth,

concomitant medications

response and ultimately the
implicated in lithium treatment
development of more informative Li+
the current
analysis did not include important covariates such as medication
dose, information on lithium blood levels, side effects, and the
(such as Angiotensin-
use of
converting enzyme (ACE)
inhibitors, diuretics, Non-steroidal
anti-inﬂammatory drugs (NSAIDs)), which can potentially inﬂu-
ence lithium clearance and treatment response [50]. Moreover,
maintaining therapeutic blood levels is crucial to achieving
treatment response with limited side effects in lithium therapy
[50]. Lithium possesses a narrow therapeutic index, meaning
that there is a relatively small margin between an effective dose
and a potentially toxic one. Typically, lithium levels are initially
monitored more frequently (weekly or biweekly) during the
initiation or adjustment phase of medication, and then less
frequently (every 3 to 6 months) once stable therapeutic levels
are achieved. While the duration of lithium treatment and the
use of certain psychiatric medications (antidepressants, anti-
psychotics, mood stabilizers) were assessed as part of the B scale
information on the speciﬁc dosage,
measure of ALDA score,
medication blood level and the use of concomitant medications
were not available in the ConLi+Gen dataset, and thus, they
were not considered in our analyses. The inclusion of these
pharmacogenomic covariates could provide stronger evidence
and should be considered in future research.

that

In conclusion, we developed a unique lithium treatment
response polygenic score (Li+
showed a positive
PGS)
association with better lithium treatment response in patients
with BD. Our gene-based and functional analyses build upon the
ﬁndings from existing molecular studies by linking lithium
treatment
response with muscarinic acetylcholine receptor
signaling and metabotropic glutamate receptor pathways. Further
pharmacological evaluation of these pathways in the context of
BD and mood stabilizing treatments may prove fruitful.

Molecular Psychiatry (2023) 28:5251 – 5261

A.T. Amare et al.

5257

Fig. 3 Manhattan plots showing the SNP-based GWAS results of lithium treatment response in patients with bipolar disorder. A In the
categorical outcome and (B) continuous scale, highlighting the loci that showed genome-wide signiﬁcance (orange).The −log10 (p-value) is
plotted against the physical position of each SNP on each chromosome. The threshold for genome-wide signiﬁcance (p-value < 5 × 10–8) is
indicated by the red dotted horizontal line.

Molecular Psychiatry (2023) 28:5251 – 5261

5258

A.T. Amare et al.

REFERENCES
1. Grande I, Berk M, Birmaher B, Vieta E. Bipolar disorder. Lancet. 2016;387:1561–72.
2. DALYs GBD, Collaborators H. Global, regional, and national disability-adjusted
life-years (DALYs) for 359 diseases and injuries and healthy life expectancy (HALE)
for 195 countries and territories, 1990-2017: a systematic analysis for the Global
Burden of Disease Study 2017. Lancet. 2018;392:1859–922.

3. Walker S, Mackay E, Barnett P, Sheridan Rains L, Leverton M, Dalton-Locke C, et al.
Clinical and social factors associated with increased risk for involuntary psy-
chiatric hospitalisation: a systematic review, meta-analysis, and narrative synth-
esis. Lancet Psychiatry. 2019;6:1039–53.

4. Chesney E, Goodwin GM, Fazel S. Risks of all-cause and suicide mortality in

mental disorders: a meta-review. World Psychiatry. 2014;13:153–60.

5. Cade JF. Lithium salts in the treatment of psychotic excitement. Med J Aust.

1949;2:349–52.

6. Malhi GS, Bell E, Bassett D, Boyce P, Bryant R, Hazell P, et al. The 2020 Royal
Australian and New Zealand College of Psychiatrists clinical practice guidelines
for mood disorders. Aust NZ J Psychiatry. 2021;55:7–117.

7. Goodwin GM, Haddad PM, Ferrier IN, Aronson JK, Barnes T, Cipriani A, et al.
Evidence-based guidelines for treating bipolar disorder: Revised third edition
recommendations from the British Association for Psychopharmacology. J Psy-
chopharmacol (Oxf, Engl). 2016;30:495–553.

8. Garnham J, Munro A, Slaney C, Macdougall M, Passmore M, Duffy A, et al. Pro-
phylactic treatment response in bipolar disorder: results of a naturalistic obser-
vation study. J Affect Disord. 2007;104:185–90.

9. Cipriani A, Hawton K, Stockton S, Geddes JR. Lithium in the prevention of suicide
in mood disorders: updated systematic review and meta-analysis. BMJ (Clin Res
ed). 2013;346:f3646.

10. Hou L, Heilbronner U, Degenhardt F, Adli M, Akiyama K, Akula N, et al. Genetic
variants associated with response to lithium treatment in bipolar disorder: a
genome-wide association study. Lancet. 2016;387:1085–93.

11. Amare AT, Schubert KO, Baune BT. Pharmacogenomics in the treatment of mood
disorders: Strategies and opportunities for personalized psychiatry. EPMA J.
2017;8:211–27.

12. Grof P, Duffy A, Cavazzoni P, Grof E, Garnham J, MacDougall M, et al. Is response

to prophylactic lithium a familial trait? J Clin psychiatry. 2002;63:942–7.

14.

13. Amare AT, Schubert KO, Hou L, Clark SR, Papiol S, Cearns M, et al. Association of
polygenic score for major depression with response to lithium in patients with
bipolar disorder. Mol Psychiatry. 2021;26:2457–70.
International Consortium on Lithium G, Amare AT, Schubert KO, Hou L, Clark SR,
Papiol S, et al. Association of polygenic score for schizophrenia and HLA Antigen
and inﬂammation genes with response to lithium in bipolar affective disorder: A
genome-wide association study. JAMA Psychiatry. 2018;75:65–74.

15. Schubert KO, Thalamuthu A, Amare AT, Frank J, Streit F, Adl M, et al. Combining
schizophrenia and depression polygenic risk scores improves the genetic pre-
diction of
lithium response in bipolar disorder patients. Transl Psychiatry.
2021;11:606.

16. Le Clerc S, Lombardi L, Baune BT, Amare AT, Schubert KO, Hou L, et al. HLA-DRB1
and HLA-DQB1 genetic diversity modulates response to lithium in bipolar
affective disorders. Sci Rep. 2021;11:17823.

17. Chen CH, Lee CS, Lee MT, Ouyang WC, Chen CC, Chong MY, et al. Variant GADL1
J Med.

I disorder. N. Engl

and response to lithium therapy in bipolar
2014;370:119–28.

18. Stacey D, Schubert KO, Clark SR, Amare AT, Milanesi E, Maj C, et al. A gene co-
expression module implicating the mitochondrial electron transport chain is
associated with long-term response to lithium treatment in bipolar affective
disorder. Transl Psychiatry. 2018;8:183.

19. Cearns M, Amare AT, Schubert KO, Thalamuthu A, Frank J, Streit F, et al. Using
polygenic scores and clinical data for bipolar disorder patient stratiﬁcation and
J Psychiatry.
lithium response prediction: machine learning approach. Br
2022;220:219–28.

20. Manchia M, Adli M, Akula N, Ardau R, Aubry JM, Backlund L, et al. Assessment of
response to lithium maintenance treatment in bipolar disorder: A consortium on
Lithium Genetics (ConLiGen) Report. PLoS One. 2013;8:e65636.

21. Dwyer DB, Kalman JL, Budde M, Kambeitz J, Ruef A, Antonucci LA, et al. An
Investigation of Psychosis Subgroups With Prognostic Validation and Exploration
of Genetic Underpinnings:
JAMA Psychiatry.
2020;77:523–33.

PsyCourse

Study.

The

22. Ritter PS, Bermpohl F, Gruber O, Hautzinger M, Jansen A, Juckel G, et al. Aims and
structure of the German research consortium bipolife for the study of bipolar
disorder. Int J Bipolar Disord. 2016;4:26.

23. Nierenberg AA, McElroy SL, Friedman ES, Ketter TA, Shelton RC, Deckersbach T,
et al. Bipolar CHOICE (Clinical Health Outcomes Initiative in Comparative Effec-
tiveness): a pragmatic 6-month trial of lithium versus quetiapine for bipolar
disorder. J Clin Psychiatry. 2016;77:90–9.

24. McKnight RF, Adida M, Budge K, Stockton S, Goodwin GM, Geddes JR.
Lithium toxicity proﬁle: A systematic review and meta-analysis. Lancet.
2012;379:721–8.

25. Malhi GS, Tanious M, Das P, Berk M. The science and practice of lithium therapy.

Aust NZ J Psychiatry. 2012;46:192–211.

26. Ng F, Mammen OK, Wilting I, Sachs GS, Ferrier IN, Cassidy F, et al. The Inter-
national Society for Bipolar Disorders (ISBD) consensus guidelines for the
safety monitoring
Bipolar Disord.
2009;11:559–95.

treatments.

disorder

bipolar

of

27. Scott J, Etain B, Manchia M, Brichant-Petitjean C, Geoffroy PA, Schulze T, et al. An
examination of the quality and performance of the Alda scale for classifying
lithium response phenotypes. Bipolar Disord. 2020;22:255–65.

28. Purcell S, Neale B, Todd-Brown K, Thomas L, Ferreira MA, Bender D, et al. PLINK: a
tool set for whole-genome association and population-based linkage analyses.
Am J Hum Genet. 2007;81:559–75.

29. Das S, Forer L, Schonherr S, Sidore C, Locke AE, Kwong A, et al. Next-generation

genotype imputation service and methods. Nat Genet. 2016;48:1284–7.

30. McCarthy S, Das S, Kretzschmar W, Delaneau O, Wood AR, Teumer A, et al. A
reference panel of 64,976 haplotypes for genotype imputation. Nat Genet.
2016;48:1279–83.

31. Ge T, Chen CY, Ni Y, Feng YA, Smoller JW. Polygenic prediction via Bayesian

regression and continuous shrinkage priors. Nat Commun. 2019;10:1776.

32. Southam L, Gilly A, Suveges D, Farmaki AE, Schwartzentruber J, Tachmazidou I,
et al. Whole genome sequencing and imputation in isolated populations identify
genetic associations with medically-relevant complex traits. Nat Commun.
2017;8:15606.

33. Sakaue S, Kanai M, Karjalainen J, Akiyama M, Kurki M, Matoba N, et al. Trans-
biobank analysis with 676,000 individuals elucidates the association of polygenic
risk scores of complex traits with human lifespan. Nat Med. 2020;26:542–8.
34. Yee TW. The VGAM package for categorical data analysis. J Stat Softw.

2010;32:1–34.

35. de Leeuw CA, Mooij JM, Heskes T, Posthuma D. MAGMA: Generalized gene-set

analysis of GWAS data. PLoS Comput Biol. 2015;11:e1004219.

36. Thomas PD, Campbell MJ, Kejariwal A, Mi H, Karlak B, Daverman R, et al. PAN-
THER: A library of protein families and subfamilies indexed by function. Genome
Res. 2003;13:2129–41.

37. Kruse AC, Kobilka BK, Gautam D, Sexton PM, Christopoulos A, Wess J. Muscarinic
acetylcholine receptors: Novel opportunities for drug development. Nat Rev Drug
Discov. 2014;13:549–60.

38. Bymaster FP, Felder CC. Role of the cholinergic muscarinic system in bipolar
disorder and related mechanism of action of antipsychotic agents. Mol Psy-
chiatry. 2002;7:S57–63.

39. Niswender CM, Conn PJ. Metabotropic glutamate receptors: Physiology, phar-

macology, and disease. Annu Rev Pharm Toxicol. 2010;50:295–322.

40. Mercier MS, Lodge D. Group III metabotropic glutamate receptors: Pharmacology,

physiology and therapeutic potential. Neurochem Res. 2014;39:1876–94.

41. Sanacora G, Zarate CA, Krystal JH, Manji HK. Targeting the glutamatergic system
improved therapeutics for mood disorders. Nat Rev Drug

to develop novel,
Discov. 2008;7:426–37.

42. Matosin N, Fernandez-Enright F, Frank E, Deng C, Wong J, Huang XF, et al.
Metabotropic glutamate receptor mGluR2/3 and mGluR5 binding in the anterior
cingulate cortex in psychotic and nonpsychotic depression, bipolar disorder and
implications for novel mGluR-based therapeutics. J Psychiatry
schizophrenia:
Neurosci. 2014;39:407–16.
Itokawa M, Yamada K,
Ishitsuka Y, Detera-Wadleigh S,
Yoshikawa T. Genetic analysis of a functional GRIN2A promoter (GT)n repeat in
bipolar disorder pedigrees in humans. Neurosci Lett. 2003;345:53–56.

Iwayama-Shigeno Y,

43.

44. Tang J, Chen X, Xu X, Wu R, Zhao J, Hu Z, et al. Signiﬁcant linkage and association
(GT)n polymorphism in promoter of the N-methyl-D-
between a functional
aspartate receptor subunit gene (GRIN2A) and schizophrenia. Neurosci Lett.
2006;409:80–2.

45. Endele S, Rosenberger G, Geider K, Popp B, Tamer C, Stefanova I, et al. Mutations
in GRIN2A and GRIN2B encoding regulatory subunits of NMDA receptors cause
variable neurodevelopmental phenotypes. Nat Genet. 2010;42:1021–6.

46. Arning L, Kraus PH, Valentin S, Saft C, Andrich J, Epplen JT. NR2A and NR2B
receptor gene variations modify age at onset in Huntington disease. Neuroge-
netics. 2005;6:25–8.

47. Leuba G, Vernay A, Kraftsik R, Tardif E, Riederer BM, Savioz A. Pathological
reorganization of NMDA receptors subunits and postsynaptic protein PSD-95
distribution in Alzheimer’s disease. Curr Alzheimer Res. 2014;11:86–96.

48. Blacker CJ, Lewis CP, Frye MA, Veldic M. Metabotropic glutamate receptors as
emerging research targets in bipolar disorder. Psychiatry Res. 2017;257:327–37.
49. Khayachi A, Ase A, Liao C, Kamesh A, Kuhlmann N, Schorova L, et al. Chronic
lithium treatment alters the excitatory/ inhibitory balance of synaptic networks

Molecular Psychiatry (2023) 28:5251 – 5261

and reduces mGluR5-PKC signalling in mouse cortical neurons. J Psychiatry
Neurosci. 2021;46:E402–14.

50. Malhi GS, Bell E, Outhred T, Berk M. Lithium therapy and its interactions. Aust

Prescr. 2020;43:91–3.

ACKNOWLEDGEMENTS
The authors are grateful to all patients who participated in the study and we
appreciate the contributions of clinicians, scientists, research assistants and study
staff who helped in the patient recruitment, data collection and biological sample
preparation of the studies. We are also indebted to the members of the ConLi+Gen
Scientiﬁc Advisory Board (http://www.conligen.org/) for critical input over the course
of the project. The analysis of this study was carried out using the high-performance
computational (HPC) capabilities of the University of Adelaide’s Phoenix Super-
computer https://www.adelaide.edu.au/phoenix/.

AUTHOR CONTRIBUTIONS
AT Amare conceived and designed the study hypothesis, as well as secured a
fellowship to lead the study. AT Amare and A Thalamuthu conducted the statistical
analysis and interpreted the ﬁndings. AT Amare, A Thalamuthu, and KO Schubert
drafted the manuscript. BT Baune and SR Clark provided supervision for the study. All
authors contributed genetic and clinical data, and critically revised the manuscript for
important intellectual content.

FUNDING
AT Amare received the 2019–2021 National Alliance for Research on Schizophrenia
and Depression (NARSAD) Young Investigator Grant from the Brain & Behaviour
Research Foundation (BBRF) and is currently supported by National Health and
Medical Research Council (NHMRC) Emerging Leadership (EL1) Investigator Grant
(APP2008000). The primary sources of funding were the Deutsche Forschungsge-
meinschaft (DFG; grant no.RI 908/7-1; grant FOR2107, RI 908/11-1 to Marcella
Rietschel, NO 246/10-1 to Markus M. Nöthen) and the Intramural Research Program of
the National Institute of Mental Health (ZIA-MH00284311; ClinicalTrials.gov identiﬁer:
NCT00001174). The genotyping was in part funded by the German Federal Ministry of
Education and Research (BMBF)
through the Integrated Network IntegraMent
(Integrated Understanding of Causes and Mechanisms in Mental Disorders), under
the auspices of the e:Med Programme (grants awarded to Thomas G. Schulze,
Marcella Rietschel, and Markus M. Nöthen).
Improving Recognition and Care in
Critical Areas of Bipolar Disorders (BipoLife) study was funded by Bundesministerium
für Bildung und Forschung (BMBF): PIs – Felix Bermpohl, Philipp Ritter, Michael Bauer,
Andreas Reif, Sarah Kittel-Schneider, Thomas G. Schulze, Jens Wiltfang, Georg Juckel,
Andreas Fallgatter and Martin Lambert. Urs Heilbronner was supported by European
Union’s Horizon 2020 Research and Innovation Programme (PSY-PGx, grant
agreement No 945151). Some data and biomaterials were collected as part of
eleven projects (Study 40) that participated in the National Institute of Mental Health
the Principal
(NIMH) Bipolar Disorder Genetics
Investigators and Co-Investigators were:
IN, R01
MH59545, John Nurnberger, M.D., Ph.D., Marvin J. Miller, M.D., Elizabeth S. Bowman,
M.D., N. Leela Rau, M.D., P.Ryan Moe, M.D., Nalini Samavedy, M.D., Rif El-Mallakh, M.D.
(at University of Louisville), Husseini Manji, M.D.(at Johnson and Johnson), Debra
A.Glitz, M.D.(at Wayne State University), Eric T.Meyer, Ph.D., M.S.(at Oxford University,
UK), Carrie Smiley, R.N., Tatiana Foroud, Ph.D., Leah Flury, M.S., Danielle M.Dick, Ph.D
(at Virginia Commonwealth University), Howard Edenberg, Ph.D.; Washington
University, St. Louis, MO, R01 MH059534, John Rice, Ph.D, Theodore Reich, M.D.,
Allison Goate, Ph.D., Laura Bierut, M.D.K02 DA21237; Johns Hopkins University,
Baltimore, M.D., R01 MH59533, Melvin McInnis, M.D., J.Raymond DePaulo, Jr., M.D.,
Dean F. MacKinnon, M.D., Francis M. Mondimore, M.D., James B. Potash, M.D., Peter P.
Zandi, Ph.D, Dimitrios Avramopoulos, and Jennifer Payne; University of Pennsylvania,
PA, R01 MH59553, Wade Berrettini, M.D., Ph.D.; University of California at San
Francisco, CA, R01 MH60068, William Byerley, M.D., and Sophia Vinogradov, M.D.;
University of Iowa, IA, R01 MH059548, William Coryell, M.D., and Raymond Crowe,
M.D.; University of Chicago, IL, R01 MH59535, Elliot Gershon, M.D., Judith Badner,
Ph.D., Francis McMahon, M.D., Chunyu Liu, Ph.D., Alan Sanders, M.D., Maria Caserta,
Steven Dinwiddie, M.D., Tu Nguyen, Donna Harakal; University of California at San
Diego, CA, R01 MH59567, John Kelsoe, M.D., Rebecca McKinney, B.A.; Rush University,
IL, R01 MH059556, William Scheftner, M.D., Howard M. Kravitz, D.O., M.P.H., Diana
Marta, B.S., Annette Vaughn-Brown, M.S.N., R.N., and Laurie Bederow, M.A.; NIMH
Intramural Research Program, Bethesda, MD, 1Z01MH002810-01, Francis J. McMahon,
M.D., Layla Kassem, Psy.D., Sevilla Detera-Wadleigh, Ph.D, Lisa Austin, Ph.D, Dennis L.
Murphy, M.D.; Howard University, William B. Lawson, M.D., Ph.D., Evarista Nwulia,
M.D., and Maria Hipolito, M.D. This work was supported by the NIH grants
P50CA89392 from the National Cancer Institute and 5K02DA021237 from the

Initiative. From 2003–2007,
Indiana University,

Indianapolis,

Molecular Psychiatry (2023) 28:5251 – 5261

A.T. Amare et al.

5259

National Institute of Drug Abuse. The Canadian part of the study was supported by
the Canadian Institutes of Health Research grant (#166098), as well as Genome
Canada and Research Nova Scotia grants to MA. Collection and phenotyping of the
Australian UNSW sample, by Philip B. Mitchell, Peter R. Schoﬁeld, Janice M. Fullerton
and Adam Wright, was funded by an Australian NHMRC Program Grant (No.1037196).
The collection of the Barcelona sample was supported by the Centro de Investigación
en Red de Salud Mental
IDIBAPS, and the CERCA Programme /
Generalitat de Catalunya (grant numbers PI080247, PI1200906, PI12/00018,
2014SGR1636, and 2014SGR398). The Swedish Research Council, the Stockholm
County Council, Karolinska Institutet and the Söderström-Königska Foundation
supported this research through grants awarded to Lena Backlund, Louise Frise’n,
Catharina Lavebratt and Martin Schalling. The collection of the Geneva sample was
supported by the Swiss National Foundation (grants Synapsy 51NF40-158776 and
the Romanian sample was supported by
32003B-125469). The collection of
U.E.F.I.S.C.D.I., Romania, grant awarded to Maria Grigoroiu-Serbanescu. Open Access
funding enabled and organized by CAUL and its Member Institutions.

(CIBERSAM),

for

received grants

COMPETING INTERESTS
Eduard Vieta has received grants and served as consultant, advisor or CME speaker
for the following entities: AB-Biotics, Allergan, Angelini, AstraZeneca, Bristol-Myers
Squibb, Dainippon Sumitomo Pharma, Farmindustria, Ferrer, Forest Research
Institute, Gedeon Richter, GlaxoSmith-Kline, Janssen, Lundbeck, Otsuka, Pﬁzer, Roche,
Sanoﬁ-Aventis, Servier, Shire, Sunovion, Takeda, the Brain and Behaviour Foundation,
the Spanish Ministry of Science and Innovation (CIBERSAM), and the Stanley Medical
Research Institute. Michael Bauer has
from the Deutsche
Forschungsgemeinschaft (DFG), and Bundesministeriums für Bildung und Forschung
(BMBF), and served as consultant, advisor or CME speaker for the following entities:
Allergan, Aristo, Janssen, Lilly, Lundbeck, neuraxpharm, Otsuka, Sandoz, Servier and
Sunovion outside the submitted work. Sarah Kittel-Schneider has received grants and
served as consultant, advisor or speaker
the following entities: Medice
Arzneimittel Pütter GmbH and Shire/Takeda. Bernhard Baune has received grants
and served as consultant, advisor or CME speaker
for the following entities:
AstraZeneca, Bristol-Myers Squibb, Janssen, Lundbeck, Otsuka, Servier, the National
Health and Medical Research Council, the Fay Fuller Foundation, the James and Diana
Ramsay Foundation. Scott Clark has received grants and served as consultant, advisor
or CME speaker for the following entities: Otsuka Austalia, Lundbeck Australia,
Janssen-Cilag Australia, Servier Australia. Tadafumi Kato received honoraria for
lectures, manuscripts, and/or consultancy, from Kyowa Hakko Kirin Co, Ltd, Eli Lilly
Japan K.K., Otsuka Pharmaceutical Co, Ltd, GlaxoSmithKline K.K., Taisho Toyama
Pharmaceutical Co, Ltd, Dainippon Sumitomo Pharma Co, Ltd, Meiji Seika Pharma Co,
Ltd, Pﬁzer Japan Inc., Mochida Pharmaceutical Co, Ltd, Shionogi & Co, Ltd, Janssen
Pharmaceutical K.K., Janssen Asia Paciﬁc, Yoshitomiyakuhin, Astellas Pharma Inc,
Wako Pure Chemical
Industries, Ltd, Wiley Publishing Japan, Nippon Boehringer
Ingelheim Co Ltd, Kanae Foundation for the Promotion of Medical Science, MSD K.K.,
Kyowa Pharmaceutical Industry Co, Ltd and Takeda Pharmaceutical Co, Ltd. Tadafumi
Kato also received a research grant from Takeda Pharmaceutical Co, Ltd. Peter Falkai
has received grants and served as consultant, advisor or CME speaker for the
following entities Abbott, GlaxoSmithKline,
Janssen, Essex, Lundbeck, Otsuka,
Gedeon Richter, Servier and Takeda as well as the German Ministry of Science and
the German Ministry of Health. Eva Reininghaus has received grants and served as
consultant, advisor or CME speaker for the following entities: Janssen and Institut
Allergosan. Mikael Landén declares that, over the past 36 months, he has received
lecture honoraria from Lundbeck and served as a scientiﬁc consultant for EPID
Research Oy; no other equity ownership, proﬁt-sharing agreements, royalties or
patent. Kazufumi Akiyama has received consulting honoraria from Taisho Toyama
Pharmaceutical Co, Ltd. In 2021, Jörg Zimmermann served as an advisor for Biogen
concerning Aducanumab (Alzheimer’s Disease).The other authors have no other
conﬂict of interest to disclose.

ADDITIONAL INFORMATION
Supplementary information The online version contains supplementary material
available at https://doi.org/10.1038/s41380-023-02149-1.

Correspondence and requests for materials should be addressed to Azmeraw T.
Amare.

Reprints and permission information is available at http://www.nature.com/
reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims
in published maps and institutional afﬁliations.

A.T. Amare et al.

5260

Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons license, and indicate if changes were made. The images or other third party
material in this article are included in the article’s Creative Commons license, unless
indicated otherwise in a credit line to the material. If material is not included in the

article’s Creative Commons license and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly
license, visit http://
from the copyright holder. To view a copy of
creativecommons.org/licenses/by/4.0/.

this

© The Author(s) 2023

33,

18,

6,7, Urs Heilbronner

1,3, Janice M. Fullerton 4,5, Muktar Ahmed1,

, Anbupalam Thalamuthu2, Klaus Oliver Schubert

6, Franziska Degenhardt8,9, Fasil Tekola-Ayele10, Liping Hou11,

Azmeraw T. Amare 1 ✉
Simon Hartmann 1, Sergi Papiol
Yi-Hsiang Hsu12,13, Tatyana Shekhtman14, Mazda Adli15, Nirmala Akula11, Kazufumi Akiyama16, Raffaella Ardau17, Bárbara Arias
Jean-Michel Aubry19, Roland Hasler19, Hélène Richard-Lepouriel19, Nader Perroud19, Lena Backlund20,21, Abesh Kumar Bhattacharjee14,
Frank Bellivier22, Antonio Benabarre23, Susanne Bengesser24, Joanna M. Biernacka 25,26, Armin Birner24, Cynthia Marie-Claire 22,27,
Pablo Cervantes28, Hsi-Chung Chen 29, Caterina Chillotti17, Sven Cichon 8,30,31, Cristiana Cruceanu 32, Piotr M. Czerski
Nina Dalkner24, Maria Del Zompo 34, J. Raymond DePaulo 35, Bruno Étain 22, Stephane Jamain 36, Peter Falkai7,37,
8,31, Louise Frisen20,21, Mark A. Frye 26, Sébastien Gard38, Julie S. Garnham 39, Fernando S. Goes
Andreas J. Forstner
Maria Grigoroiu-Serbanescu 40, Andreas J. Fallgatter41, Sophia Stegmaier42, Thomas Ethofer42,43, Silvia Biere44, Kristiyana Petrova44,
Ceylan Schuster44, Kristina Adorjan6,7, Monika Budde6, Maria Heilbronner6, Janos L. Kalman 6,7, Mojtaba Oraki Kohshour
Daniela Reich-Erkelenz6, Sabrina K. Schaupp6, Eva C. Schulte 6,7, Fanny Senner6,7, Thomas Vogl6, Ion-George Anghelescu46,
Volker Arolt47, Udo Dannlowski47, Detlef Dietrich48,49, Christian Figge50, Markus Jäger51, Fabian U. Lang51, Georg Juckel52,
Carsten Konrad53, Jens Reimer
Jörg Zimmermann62, Till F. M. Andlauer
Irina Falkenberg65, Cüneyt Yildiz
Ida S. Haussleiter52, Martin Lambert54, Anja C. Rohenkohl54, Vivien Kraft54, Paul Grof67, Ryota Hashimoto68, Joanna Hauser
Stefan Herms8,30, Per Hoffmann8,30, Esther Jiménez23, Jean-Pierre Kahn69, Layla Kassem11, Po-Hsiu Kuo 70, Tadafumi Kato71,
John Kelsoe14, Sarah Kittel-Schneider
Mikael Landén 77,78, Catharina Lavebratt
Lina Martinsson84, Michael J. McCarthy
Francis M. Mondimore35, Palmiero Monteleone 92,93, Caroline M. Nievergelt14, Markus M. Nöthen 8, Tomas Novák
Claire O’Donovan39, Norio Ozaki95, Andrea Pfennig64, Claudia Pisanu 34, James B. Potash35, Andreas Reif
Guy A. Rouleau 96, Janusz K. Rybakowski
Giovanni Severino 34, Paul D. Shilling14, Katzutaka Shimoda 97, Christian Simhandl98, Claire M. Slaney39, Alessio Squassina 34,
Thomas Stamm15,99, Pavla Stopkova 94, Mario Maj93, Gustavo Turecki
100,
Adam Wright101, Peter P. Zandi
Francis J. McMahon 11, Thomas G. Schulze6,35,103, Scott R. Clark

79, Susan G. Leckband80, Alfonso Tortorella 81, Mirko Manchia82,83,
20,21,89, Marina Mitjans88,90,91,
94,

54,55, Max Schmauß56, Andrea Schmitt7,57, Carsten Spitzer58, Martin von Hagen59, Jens Wiltfang 60,61,

102, Philip B. Mitchell101, Michael Bauer64, Martin Alda 39,94, Marcella Rietschel

74, Martin Schalling 20,21, Peter R. Schoﬁeld 4,5, Barbara W. Schweizer35,

72,73, Ewa Ferensztajn-Rochowiak74, Barbara König75, Ichiro Kusumi

14,85, Susan McElroy86, Francesc Colom 87,88, Vincent Millischer

66, Marius Koch 66, Kathrin Gade 60, Sarah Trost60,

32, Eduard Vieta 23, Julia Veeh72, Stephanie H. Witt

63, Andre Fischer61, Felix Bermpohl15, Philipp Ritter

64, Silke Matura44, Anna Gryaznova6,

1 and Bernhard T. Baune104,105,106

65, Tilo Kircher65, Julia Schmidt

20,21, Marion Leboyer

72, Eva Reininghaus

76, Gonzalo Laje11,

6,45,

100,

24,

33,

35,

1Discipline of Psychiatry, School of Medicine, University of Adelaide, Adelaide, SA, Australia. 2Centre for Healthy Brain Ageing (CHeBA), Discipline of Psychiatry and Mental Health,
UNSW Medicine & Health, University of New South Wales, Sydney, Australia. 3Northern Adelaide Local Health Network, Mental Health Services, Adelaide, SA, Australia.
4Neuroscience Research Australia, Sydney, NSW, Australia. 5School of Medical Sciences, University of New South Wales, Sydney, NSW, Australia. 6Institute of Psychiatric Phenomics
and Genomics (IPPG), University Hospital, LMU Munich, Munich, Germany. 7Department of Psychiatry and Psychotherapy, University Hospital, Ludwig-Maximilian-University
Munich, Munich, Germany. 8Institute of Human Genetics, University of Bonn, School of Medicine & University Hospital Bonn, Bonn, Germany. 9Department of Child and
Adolescent Psychiatry, Psychosomatics and Psychotherapy, LVR Klinikum Essen, University of Duisburg-Essen, Rheinische Kliniken, Essen, Germany. 10Epidemiology Branch,
Division of Population Health Research, Division of Intramural Research, Eunice Kennedy Shriver National Institute of Child Health and Human Development, National Institutes of
Health, Bethesda, MD, USA. 11Intramural Research Program, National Institute of Mental Health, National Institutes of Health, US Department of Health & Human Services,
Bethesda, MD, USA. 12HSL Institute for Aging Research, Harvard Medical School, Boston, MA, USA. 13Program for Quantitative Genomics, Harvard School of Public Health, Boston,
MA, USA. 14Department of Psychiatry, University of California San Diego, San Diego, CA, USA. 15Department of Psychiatry and Psychotherapy, Charité - Universitätsmedizin Berlin,
Campus Charité Mitte, Berlin, Germany. 16Department of Biological Psychiatry and Neuroscience, Dokkyo Medical University School of Medicine, Mibu, Tochigi, Japan. 17Unit of
Clinical Pharmacology, Hospital University Agency of Cagliari, Cagliari, Italy. 18Unitat de Zoologia i Antropologia Biològica (Dpt. Biologia Evolutiva, Ecologia i Ciències Ambientals),
Facultat de Biologia and Institut de Biomedicina (IBUB), University of Barcelona, CIBERSAM, Barcelona, Spain. 19Department of Psychiatry, Mood Disorders Unit, HUG - Geneva
University Hospitals, Geneva, Switzerland. 20Department of Molecular Medicine and Surgery, Karolinska Institute, Stockholm, Sweden. 21Center for Molecular Medicine, Karolinska
University Hospital, Stockholm, Sweden. 22INSERM UMR-S 1144, Université Paris Cité, Département de Psychiatrie et de Médecine Addictologique, AP-HP, Groupe Hospitalier
Saint-Louis-Lariboisière-F.Widal, Paris, France. 23Bipolar and Depressive Disorders Program,, Institute of Neuroscience, Hospital Clinic, University of Barcelona, IDIBAPS, CIBERSAM,
Barcelona, Catalonia, Spain. 24Department of Psychiatry and Psychotherapeutic Medicine, Research Unit for bipolar affective disorder, Medical University of Graz, Graz, Austria.
25Department of Quantitative Health Sciences, Mayo Clinic, Rochester, MN, USA. 26Department of Psychiatry and Psychology, Mayo Clinic, Rochester, MN, USA. 27Université Paris
Cité, Inserm, Optimisation Thérapeutique en Neuropsychopharmacologie, F-75006 Paris, France. 28The Neuromodulation Unit, McGill University Health Centre, Montreal, Canada.
29Department of Psychiatry & Center of Sleep Disorders, National Taiwan University Hospital, Taipei, Taiwan. 30Department of Biomedicine, University Hospital Basel, Basel,
Switzerland. 31Institute of Neuroscience and Medicine (INM-1), Research Center Jülich, Jülich, Germany. 32Douglas Mental Health University Institute, McGill University, Montreal,
Canada. 33Psychiatric Genetic Unit, Poznan University of Medical Sciences, Poznan, Poland. 34Department of Biomedical Sciences, University of Cagliari, Cagliari,
Italy.
35Department of Psychiatry and Behavioral Sciences, Johns Hopkins University, Baltimore, MD, USA. 36Inserm U955, Translational Psychiatry laboratory, Fondation FondaMental,
Créteil, France. 37Max Planck Institute of Psychiatry, Munich, Germany. 38Pôle de Psychiatrie Générale Universitaire, Hôpital Charles Perrens, Bordeaux, France. 39Department of
Psychiatry, Dalhousie University, Halifax, Nova Scotia, Canada. 40Biometric Psychiatric Genetics Research Unit, Alexandru Obregia Clinical Psychiatric Hospital, Bucharest, Romania.
41University Department of Psychiatry and Psychotherapy Tuebingen, University of Tübingen, Tuebingen, Germany. 42Department of General Psychiatry, University of Tuebingen,
Tuebingen, Germany. 43Department of Biomedical Resonance, University of Tuebingen, Tuebingen, Germany. 44Department of Psychiatry, Psychotherapy and Psychosomatics,
University Hospital of Frankfurt, Goethe University, Frankfurt, Germany. 45Department of Immunology, Faculty of Medicine, Ahvaz Jundishapur University of Medical Sciences,
Ahvaz, Iran. 46Department of Psychiatry and Psychotherapy, Mental Health Institute Berlin, Berlin, Germany. 47Institute for Translational Psychiatry, University of Münster, Münster,
Germany. 48AMEOS Clinical Center Hildesheim, Hildesheim, Germany. 49Center for Systems Neuroscience (ZSN), Hannover, Germany. 50Karl-Jaspers Clinic, European Medical
School Oldenburg-Groningen, Oldenburg 26160, Germany. 51Department of Psychiatry II, Ulm University, Bezirkskrankenhaus Günzburg, Günzburg, Germany. 52Department of

Molecular Psychiatry (2023) 28:5251 – 5261

A.T. Amare et al.

5261

Psychiatry, Ruhr University Bochum, LWL University Hospital, Bochum, Germany. 53Department of Psychiatry and Psychotherapy, Agaplesion Diakonieklinikum, Rotenburg,
Germany. 54Department of Psychiatry and Psychotherapy, University Medical Center Hamburg-Eppendorf, Hamburg, Germany. 55Department of Psychiatry, Health North Hospital
Group, Bremen, Germany. 56Department of Psychiatry and Psychotherapy, Bezirkskrankenhaus Augsburg, Augsburg, Germany. 57Laboratory of Neuroscience (LIM27), Institute of
Psychiatry, University of Sao Paulo, São Paulo, Brazil. 58Department of Psychosomatic Medicine and Psychotherapy, University Medical Center Rostock, Rostock, Germany. 59Clinic
for Psychiatry and Psychotherapy, Clinical Center Werra-Meißner, Eschwege, Germany. 60Department of Psychiatry and Psychotherapy, University Medical Center Göttingen,
Göttingen, Germany. 61German Center for Neurodegenerative Diseases (DZNE), Göttingen, Germany. 62Psychiatrieverbund Oldenburger Land gGmbH, Karl-Jaspers-Klinik, Bad
Zwischenahn, Germany. 63Department of Neurology, University Hospital rechts der Isar, School of Medicine, Technical University of Munich, Munich, Germany. 64Department of
Psychiatry and Psychotherapy, University Hospital Carl Gustav Carus, Medical Faculty, Technische Universität Dresden, Dresden, Germany. 65Department of Psychiatry and
Psychotherapy, Philipps-University Marburg, Marburg, Germany. 66Institute for Medical Informatics, University Medical Center Göttingen, Göttingen, Germany. 67Mood Disorders
Center of Ottawa, Ontario, Canada. 68Department of Pathology of Mental Diseases, National Institute of Mental Health, National Center of Neurology and Psychiatry, 4-1-1
Ogawahigashi, Kodaira, Tokyo 187-8553, Japan. 69Service de Psychiatrie et Psychologie Clinique, Centre Psychothérapique de Nancy - Université de Lorraine, Nancy, France.
70Department of Public Health & Institute of Epidemiology and Preventive Medicine, College of Public Health, National Taiwan University, Taipei, Taiwan. 71Laboratory for
Molecular Dynamics of Mental Disorders, RIKEN Brain Science Institute, Saitama, Japan. 72Department of Psychiatry, Psychosomatic Medicine and Psychotherapy, University
Hospital Frankfurt, Frankfurt, Germany. 73Department of Psychiatry, Psychotherapy and Psychosomatic Medicine, University Hospital of Würzburg, Wurzburg, Germany.
74Department of Adult Psychiatry, Poznan University of Medical Sciences, Poznan, Poland. 75Department of Psychiatry and Psychotherapeutic Medicine, Landesklinikum
Neunkirchen, Neunkirchen, Austria. 76Department of Psychiatry, Hokkaido University Graduate School of Medicine, Sapporo, Japan. 77Institute of Neuroscience and Physiology,
the Sahlgrenska Academy at the Gothenburg University, Gothenburg, Sweden. 78Department of Medical Epidemiology and Biostatistics, Karolinska Institutet, Stockholm, Sweden.
79Inserm U955, Translational Psychiatry laboratory, Université Paris-Est-Créteil, Department of Psychiatry and Addictology of Mondor University Hospital, AP-HP, Fondation
FondaMental, Créteil, France. 80Ofﬁce of Mental Health, VA San Diego Healthcare System, San Diego, CA, USA. 81Department of Psychiatry, University of Perugia, Perugia, Italy.
82Section of Psychiatry, Department of Medical Sciences and Public Health, University of Cagliari, Cagliari, Italy. 83Department of Pharmacology, Dalhousie University, Halifax, NS,
Canada. 84Department of Clinical Neurosciences, Karolinska Institutet, Stockholm, Sweden. 85Department of Psychiatry, VA San Diego Healthcare System, San Diego, CA, USA.
86Department of Psychiatry, Lindner Center of Hope / University of Cincinnati, Mason, OH, USA. 87Mental Health Research Group, IMIM-Hospital del Mar, Barcelona, Catalonia,
Spain. 88Department of Genetics, Microbiology and Statistics, Faculty of Biology, University of Barcelona, Barcelona, Spain. 89Department of Psychiatry and Psychotherapy,
Medical University of Vienna, Vienna, Austria. 90Institut de Biomedicina de la Universitat de Barcelona (IBUB), Barcelona, Spain. 91Centro de Investigación Biomédica en Salud
Mental (CIBERSAM), Instituto de Salud Carlos III, Madrid, Spain. 92Neurosciences Section, Department of Medicine, Surgery and Dentistry “Scuola Medica Salernitana”, University of
Salerno, Salerno,
Institute of Mental Health, Klecany, Czech Republic.
95Department of Psychiatry & Department of Child and Adolescent Psychiatry, Nagoya University Graduate School of Medicine, Nagoya, Japan. 96Montreal Neurological Institute
and Hospital, McGill University, Montreal, Canada. 97Department of Psychiatry, Dokkyo Medical University School of Medicine, Mibu, Tochigi, Japan. 98Bipolar Center Wiener
Neustadt, Sigmund Freud University, Medical Faculty, Vienna, Austria. 99Department of Clinical Psychiatry and Psychotherapy, Brandenburg Medical School, Brandenburg,
Germany. 100Department of Genetic Epidemiology in Psychiatry, Central Institute of Mental Health, Medical Faculty Mannheim, University of Heidelberg, Mannheim, Germany.
101School of Psychiatry, University of New South Wales, and Black Dog Institute, Sydney, Australia. 102Department of Mental Health, Johns Hopkins Bloomberg School of Public
Health, Baltimore, MD, USA. 103Department of Psychiatry and Behavioral Sciences, SUNY Upstate Medical University, Norton College of Medicine, Syracuse, NY, USA.
104Department of Psychiatry and Psychotherapy, University of Münster, Münster, Germany. 105Department of Psychiatry, Melbourne Medical School, University of Melbourne,
Parkville, VIC, Australia. 106The Florey Institute of Neuroscience and Mental Health, The University of Melbourne, Parkville, VIC, Australia.

Italy. 93Department of Psychiatry, University of Campania “Luigi Vanvitelli”, Naples,

Italy. 94National

Molecular Psychiatry (2023) 28:5251 – 5261
