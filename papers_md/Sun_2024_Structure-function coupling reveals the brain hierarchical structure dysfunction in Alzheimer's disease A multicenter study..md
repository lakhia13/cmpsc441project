# Sun_2024_Structure-function coupling reveals the brain hierarchical structure dysfunction in Alzheimer's disease A multicenter study.

Received: 3 May 2024

Revised: 10 June 2024

Accepted: 13 June 2024

DOI: 10.1002/alz.14123

R E S E A R C H A R T I C L E

Structure–function coupling reveals the brain hierarchical
structure dysfunction in Alzheimer’s disease: A multicenter
study

Yibao Sun1
Zhuangzhuang Li1
Dawei Wang6

Pan Wang2

Kun Zhao1

Suyu Zhong1

Ying Han7,8,9

Bo Zhou4
Hongxiang Yao10

Yong Liu1,3

Pindong Chen3
Jie Lu5

Yida Qu3
Xi Zhang4

1Center for Artificial Intelligence in Medical Imaging, School of Artificial Intelligence, Beijing University of Posts and Telecommunications, Beijing, China

2Department of Neurology, Tianjin Huanhu Hospital, Tianjin, China

3School of Artificial Intelligence, University of Chinese Academy of Sciences & Brainnetome Center, Institute of Automation, Chinese Academy of Sciences, Beijing,
China

4Department of Neurology, the Second Medical Centre, National Clinical Research Centre for Geriatric Diseases, Chinese PLA General Hospital, Beijing, China

5Department of Radiology, Xuanwu Hospital of Capital Medical University, Beijing, China

6Department of Radiology, School of Public Health, Qilu Hospital of Shandong University & Department of Epidemiology and Health Statistics, Jinan, China

7School of Biomedical Engineering, Hainan University, Haikou, China

8Department of Neurology, Xuanwu Hospital of Capital Medical University, Beijing, China

9National Clinical Research Center for Geriatric Diseases, Beijing, China

10Department of Radiology, the Second Medical Centre, National Clinical Research Centre for Geriatric Diseases, Chinese PLA General Hospital, Beijing, China

Correspondence
Yong Liu, Center for Artificial Intelligence in
Medical Imaging, School of Artificial
Intelligence, Beijing University of Posts and
Telecommunications, Beijing, China.
Email: yongliu@bupt.edu.cn

Funding information
the Science and Technology Innovation 2030
Major, Grant/Award Number:
2022ZD0211600; the Beijing Municipal
Natural Science Foundation, Grant/Award
Number: 7244519; Fundamental Research
Funds for the Central Universities,
Grant/Award Number: 2021XD-A03; National
Natural Science Foundation of China,
Grant/Award Numbers: 62333002,
82172018; Beijing Nova Program,
Grant/Award Number: 20220484177; Science
and Technology Project of Tianjin Municipal
Health Committee, Grant/Award Number:

Abstract

BACKGROUND: Alzheimer’s disease (AD) is a neurodegenerative condition character-

ized by cognitive decline. To date, the specific dysfunction in the brain’s hierarchical

structure in AD remains unclear.

METHODS: We introduced the structural decoupling index (SDI), based on a multi-site

data set comprising functional and diffusion-weighted magnetic resonance imaging

data from 793 subjects, to assess their brain hierarchy.

RESULTS: Compared to normal controls (NCs), individuals with AD exhibited increased

SDI within the posterior superior temporal sulcus, insular gyrus, precuneus, hippocam-

pus, amygdala, postcentral gyrus, and cingulate gyrus; meanwhile, the patients with AD

demonstrated decreased SDI in the frontal lobe. The SDI in those regions also showed

a significant correlation with cognitive ability. Moreover, the SDI was a robust AD neu-

roimaging biomarker capable of accurately distinguishing diagnostic status (area under
the curve [AUC] = 0.86).

Yibao Sun, Pan Wang, and Kun Zhao contributed equally to this study.

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial License, which permits use, distribution and reproduction in any
medium, provided the original work is properly cited and is not used for commercial purposes.
© 2024 The Author(s). Alzheimer’s & Dementia published by Wiley Periodicals LLC on behalf of Alzheimer’s Association.

Alzheimer’s Dement. 2024;20:6305–6315.

wileyonlinelibrary.com/journal/alz

6305

6306

TJWJ2022MS032; Tianjin Key Medical
Discipline (Specialty) Construction,
Grant/Award Number: TJYXZDXK-052B

SUN ET AL.

DISCUSSION: Our findings revealed the dysfunction of the brain’s hierarchical struc-

ture in AD. Furthermore, the SDI could serve as a promising neuroimaging biomarker

for AD.

K E Y W O R D S
Alzheimer’s disease, hierarchical structure, multi-modal brain network, multi-site, structural
decoupling index

Highlights
∙ This study utilized multi-center, multi-modal data from East Asian populations.
∙ We found an increased spatial gradient of the structure decoupling index (SDI) from

sensory–motor to higher-order cognitive regions.

∙ Changes in SDI are associated with energy metabolism and mitochondria.
∙ SDI can identify Alzheimer’s disease (AD) and further uncover the disease mecha-

nisms of AD.

1

INTRODUCTION

ment of the relationship between structural and functional activity.

Consequently, the SDI holds promising potential for quantifying the

Alzheimer’s disease (AD) is a neurodegenerative disorder character-

brain’s hierarchical structure, thereby enhancing our comprehension

ized by various impairments including memory, emotional, cognitive,
and behavioral deficits.1-3 The human brain functions as a complex
network and plays a crucial role in constraining brain function.4-6 The

hierarchical structure of the brain network serves as the basic form
of organization for translating and integrating information.7,8 Dys-

of brain communication mechanisms that underpin the diverse behav-
ioral domains and uncovering the potential genetics.11,18 Therefore,

the dysfunction of the brain’s hierarchical structure in AD can be
quantified through the SDI.11

The primary aim of this study is to explore the alteration of the

function of the brain’s hierarchical organization leads to abnormal

brain’s hierarchical structure in AD. For this purpose, we first computed

structural damage and altered functional integration among different
brain regions through disconnection mechanisms.6,9 Understanding

the individual SDIs by combining the resting-state functional magnetic

resonance imaging (rs-fMRI) and diffusion tensor imaging (DTI) in a

these changes in hierarchical structure and functional connectivity is

large multi-site data set encompassing a cohort of 284 patients with

essential for investigating the underlying mechanisms of AD. Better

AD, 254 individuals with mild cognitive impairment (MCI), and 255 cog-

understanding these structure and function alterations will shed light

nitively normal controls (NCs) from seven sites. Then we performed

on the potential targets for therapeutic interventions to mitigate the

a mega-analysis framework to investigate the robust alteration of the

effects of the AD on brain function and cognition.

SDI in AD. In addition, we elucidated the underlying mechanism of SDI

Quantifying the brain’s hierarchical structure is a challenge in
neuroscience.10 Previous studies have demonstrated that the role of

hierarchical organization lies in elucidating how brain structure influ-
ences and constrains brain function.11 Thus the decoupling of function

and structure offers promising insight for exploring the intricate hier-

archical structures of the brain. Several studies have employed a

straightforward regional spatial correlation to investigate the relation-
ship between brain structure and function.12–15 However, the coupling

alterations in AD via gene enrichment analysis. Finally, to evaluate the

potential of SDIs as a neuroimaging biomarker for AD, we employed a

support vector machine (SVM) model for AD classification and clinical

score prediction (Figure 1).

2

MATERIALS AND METHODS

of function and structure exhibits a complex phenotype, which may

2.1

Participants and image acquisition

not comprehensively characterize the complexity of the function–

structure relationship by using only linear statistical methods.

This study included 793 participants (284 individuals with AD, 254 with

To address these challenges, Preti & De Ville have proposed an

MCI, and 255 NCs) with paired fMRI scans, DTI scans, and demographic

innovative measure known as the structural decoupling index (SDI)
to quantify the degree of regional structure–function dependency.11
SDI combines network science16 and graph signal processing17 to

and psychological information from seven sites of the Multi-Center

Alzheimer’s Disease Imaging (MCADI), (Table S1). The MRI scanner

and acquisition protocol information of fMRI and DTI data are listed

link brain activity signals with the underlying white matter topology.

Furthermore, SDI is a novel neuroimaging biomarker for the assess-

in Tables S2 and S3. Detailed information can be found in our previ-
ous studies.19–22 This study was consistent with the Principles of the

SUN ET AL.

6307

Declaration of Helsinki and approved by the medical research ethics

committee and institutional review board (detailed information can be

RESEARCH IN CONTEXT

found in Method S1).

2.2

Data preprocessing

All the rs-fMRI scans were pre-processed using the Brainnetome fMRI

Toolkit (http://brant.brainnetome.org), which included the following

steps: (1) slice-timing correction; (2) realignment to the first volume;

(3) normalization (Montreal Neurological Institute [MNI] space with
2 mm × 2 mm × 2 mm); (4) regression of nuisance signals; and (5)

denoise. Finally, the Brainnetome Atlas was used to parcellate fMRI

volumes and compute regionally averaged fMRI signals. For each par-
ticipant, we obtained an N × T matrix S = [st]t = 1, 2 . . . T (N = 246 regions

of Brainnetome Atlas, T is the time sampling number). W excluded

those subjects with large head motion in any direction corresponding
to >3 mm or any rotation >3. The head motion was also included as the

concomitant variable.

All the DTI scans were pre-processed using the DiffusionKit Toolkit
(http://diffusion.brainnetome.org).23 DTI pre-processing comprised

skull dissection, eddy current correction, registration, and normaliza-

tion. Next the diffusion tensor indices’ fractional anisotropy (FA) and
mean diffusivity (MD) were calculated.19 After that, a brain network

based on the number of fiber connections between brain regions was

constructed using deterministic fiber tracking, and the brain structure
network connection matrix (fiber number network, FN, sized N × N)

was obtained. Structural connectivity (SC) refers to the fiber connec-

tions between brain regions in the Brainnetome Atlas (Table S4). More

detailed information is in Method S2 and Method S3.

2.3

Function–structure coupling

To estimate the coupling of the SC and functional activities, we com-

puted the regional-level SDI using the graph signal processing pipeline
(https://www.github.com/gpreti/GSP_StructuralDecouplingIndex).11

In brief, structural connectome harmonics were obtained by the eigen
decomposition LU = UΛ of the normalized Laplacian of the individ-

ual’s structural connectome (FA, MD, and FN structural matrixes).

This produces the uk Laplace eigenvector, the so-called harmonic
component, where each eigenvector is associated with an eigenvalue
λk that can be interpreted as the graph frequency value. Through
construction, uk with low λk encodes low pattern frequencies that
are more easily expressed on structural connectome, which represent

global brain patterns along major geometric axes. Conversely, uk with
high λk encodes high pattern frequencies, capturing more complex and
localized patterns. Then we projected the individual functional data

1. Systematic review: Authors reviewed the existing liter-

ature via PubMed searches, and found much research

exploring the regions of structural and functional changes

in Alzheimer’s disease (AD). However, there is a lack of

large-sample, multi-center studies investigating the rela-

tionship between structure and function in East Asian AD

populations.

2.

Interpretation: We found alterations in the structural

decoupling index (SDI) of AD populations in the default

mode network, frontal lobe, and subcortical regions, indi-

cating changes in the structural–functional relationship

due to metabolic abnormalities. SDI shows promising

performance in identifying AD.

3. Future directions: These results suggest that SDI could

serve as a biomarker for AD. Further analysis is war-

ranted to explore the causal relationship between struc-

tural and functional changes in AD and to investigate

how metabolic abnormalities lead to the dissociation of

structure and function.

from the structure). The cutoff frequency C of the ideal low/high pass

filter is defined by the equal energy division of the energy spectral

density of each subject. The N square matrix U (low) contains the first

C eigenmodules (columns of U) and complements N-C zero columns.

Conversely, the matrix U (high) includes the first C zero columns,

followed by N-C last eigenmodules. Therefore, the filtered signal is

obtained from the formula (1) and the formula (2):

sC
t

= U(low) UTst

sD
t

= U(high) UTst

)2

)2

(
sD
t2

+

sD
t1

+ ⋯ +

)2

(
sC
t1

(

+

sC
t2

)2

+ ⋯ +

(1)

(2)

(3)

)2

)2

sD
tn

(

(

sC
tn

√

(

SDI =

√

SDI is the ratio between the L2 norms of SD

t across time
and quantifies the absence of function–structure dependency in each

t and SC

region. Using this pipeline, we calculated regional-level individual SDIs

for each metric (FA, MD, and FN; named FA-SDI, MD-SDI, and FN-SDI).
Brain regions with an SDI >1 suggest that their activity signals diverge

of each time point onto individual structural harmonic and applied

more from the underlying structural pathways, resulting in lower cou-

graphic signal filtering to decompose the active signal into two parts:

one is expressed on the low-frequency structural harmonics (so it is

more consistent with the structure) and the other is expressed on

pling between SC and functional activities. Conversely, regions with
an SDI <1 exhibit the opposite relationship, where there is a stronger
coupling between SC and functional activities.24 (More details can be

complementary high-frequency harmonics (therefore, more detached

found in Supplementary Materials.)

6308

SUN ET AL.

F I G U R E 1 Method pipeline. (A) The pipeline for computing SDI. The rs-fMRI time series and structural matric (FA, MD, and FN) were
calculated based on the Brainnetome Atlas, and functional signals were then filtered into two components (coupling and decoupling from the
structure) by applying ideal filters in the graph spectral domain. The SDI was the ratio between the norm of decoupling and coupling signal portions
across time (see 11). (B) Mega-analysis. A two-sample, two-sided t-test was performed to obtain the p-value for SDI metrics in each center after
controlling for age and gender effects. The mega-analysis was applied to integrate results from seven centers, and the significantly altered regions
were identified after multiple comparison corrections. (C) Individual prediction. The classification and prediction tasks are verified by
leave-one-site-out cross-validation. (D) Gene expression. The partial least squares (PLS) regression was used to identify the weighted linear
components of expression patterns for all 15,633 genes correlated with SDI alterations in connectome dynamics. FA, fractional anisotropy; FN,
fiber number; MD, mean diffusivity; rs-fMRI, resting-state functional magnetic resonance imaging; SDI, structural decoupling index.

2.4
NC

Difference analysis for SDI between AD and

multi-site results for each SDI metric (FA-SDI, MD-SDI, and FN-SDI).

Therefore, the statistical results can be obtained more effectively by

reducing the site effect via the mega-analysis framework compared

To reduce the site effects, we first applied two-sample, two-tailed

to direct contrasts among the entire data set. Here, age and gender

t-tests for two groups at each site with the same scanning param-

were controlled using the linear regression model. As suggested in

eters. Then we performed a mega-analysis method to integrate the

previous studies, the Liptak–Stouffer z-score transform was used to

SUN ET AL.

6309

combine p-values across the seven sites, which has optimal power
for combining probabilities in mega-analysis.20,22 Specifically, the

p-values for each data set were transformed into z-scores using the
inverse standard normal distribution. In particular, zi = 𝜑−1 (1 − pi∕2),
where 𝜑−1 is the standard normal cumulative distribution function.
The combined z-score was then computed using the Liptak–Stouffer
formula25:

2.6

Individual diagnostic status prediction

To evaluate whether the SDI can distinguish AD from NCs, we per-

formed a binary classification by the most commonly used SVM model

with features from 255 NCs and 284 ADs for each metric (FA-SDI, MD-

SDI, and FN-SDI) with leave-one-site-out cross-validation framework,
as in our previous studies.19,27 Briefly, one site was selected as the test-

ing set for each time training and testing, and the others served as the

z =

∑k
√

i=1 wizi
∑k
i=1 w2

i

training set. We used the 10-fold cross-validation in the training proce-

(4)

dure to obtain the best parameters via the grid search framework. The

performance of classification was evaluated using accuracy (ACC), sen-

sitivity (SEN), specificity (SPE), and area under the receiver-operating

characteristic (ROC) curve (AUC). To verify the clinical relativity of the

classification model, we performed Pearson’s correlation between indi-

where wi is the square root of the sample size of data set i, and k
is the number of data sets. Under the null hypothesis, the z-scores

follow the standard normal distribution. Therefore, by converting the

vidual risk score (evaluated by the classifier output) and MMSE score

z-scores to p-values, we identified significant regions (FA-SDI, MD-SDI,

(in the ADs and MCIs) in the testing sets.

and FN-SDI) that differed between the two groups. The Bonferroni

We further employed a support vector regression (SVR) model to

correction was used to correct for multiple comparisons across the set
of all 246 regions (p < 0.05/246).

predict the MMSE score for each participant (NC, MCI, and AD) via

the same cross-validation framework as the classification analysis. The

predicted MMSE performance based on the SDI was evaluated using

the Pearson correlation coefficient between the actual and predicted

Associations between clinical scores, gene

2.5
expression, and SDI alterations

MMSE scores.

To explore the biological basis of the SDI, we performed a Pearson’s

3

RESULTS

correlation between the SDI for each metric and cognitive ability, that

is, the Mini-Mental State Examination (MMSE) scores and Montreal

3.1

Demographic and clinical characteristics

Cognitive Assessment (MoCA), in the AD and MCI groups with false
discovery rate (FDR) correction (p < 0.05) after controlling the age,

gender, and site effects.

A gene enrichment analysis was performed in the present study to

Among the NC, MCI, and AD groups there were no statistically signif-

icant differences in the ages and sex ratios.. The MMSE score differed
significantly among the NC, MCI, and AD groups, with p < 0.001 (Table

explore the biological mechanism of the alteration of the SDI in AD.

S1).

The gene expression data were obtained from the Allen Human Brain

atlas (http://human.brain-map.org/) and were projected to the Brain-

netome Atlas using the Abagen toolbox (https://abagen.readthedocs.
io/en/stable/), resulting in a 236 × 15,633 gene expression matrix (10

3.2

Alteration of the SDI in AD

of 246 regions did not identify related genes in the Abagen toolbox).

The visual, sensory, motor, and auditory cortices showed low SDI val-

We first performed a partial least squares (PLS) regression to inves-

ues, whereas the frontal and temporal lobes presented higher SDI

tigate the association between the T-map of FA-SDI in AD versus NC

values. The SDI patterns showed a distinct spatial distribution, rang-

and gene expression. Briefly, the statistical significance of the variance

explained by the PLS components was tested using a permutation anal-
ysis (n = 5000) in which spatial autocorrelation was corrected. Then

ing from sensorimotor to higher-order functional regions (Figure 2A
and Figure S2), which reflect a hierarchical structure of the brain.11

We found that the global SDIs of NC after averaging 246 areas were

the PLS weight of each gene was transformed into a z-score value by

dividing the weight by the standard deviation (SD) of the correspond-

significantly lower than those in AD in all three SDI metrics (Cohen’s
d, FA-SDI = −0.245, MD-SDI = −0.246, FN-SDI = −0.159) (Figure

ing weights derived from 5000 bootstrapping instances. Finally, we

S3). IN addition, the global SDIs were significantly lower in the MCI

effectively ranked 15,633 genes based on their corresponding weight

value. After that, gene-set enrichment analysis was performed based

group than in the AD group in the FA-SDI and MD-SDI (Cohen’s d,
FA-SDI = −0.195, MD-SDI = −0.194), (Table S5).

on the top 1000 genes by the Metascape platform with FDR correction
(p < 0.05) (https://metascape.org/gp/index.html#/main/step1).26 Here,

we provided only the association analysis based on the group differ-

Compared with NCs, the patients with AD showed significant alter-

ation in 27 areas (FA-SDI), 31 areas (MD-SDI), and 42 areas (FN-SDI)
(p < 0.05/N, Bonferroni corrected for N = 246 comparisons), (Table

ence map from the FA-SDI, as the results exhibited high similarity to

S6 and Figure S4). As for FA-SDI, the AD group showed significantly

those obtained from SDI analyses employing different metrics (Figure

higher SDI in the posterior superior temporal sulcus, insular gyrus,

S1).

6310

SUN ET AL.

F I G U R E 2

(A) Left: the FA-SDI pattern of NC; right tables showed the top five large (orange color) and low (blue color) FA-SDI scores with the
associated NC, MCI, and AD groups. Statistically significant differences in FA-SDI between patients with AD versus NC (B) AD versus MCI, (C) and
MCI versus NC. (D) The warmer and colder colors indicate higher and lower SDI measures in patients in the former group than in the latter group,
respectively. The correlation map between altered FA-SDI and MMSE (E) and MoCA scores (F) in the AD and MCI patients with FDR correction
(p < 0.05). AD, Alzheimer’s disease; FA, fractional anisotropy; MCI, mild cognitive impairment; MMSE, Mini-Mental State Examination; MoCA,
Montreal Cognitive Assessment; NC, normal control; SDI, structural decoupling index.

precuneus, hippocampus, amygdala, postcentral gyrus, and cingulate

gyrus, whereas the group showed a significantly lower SDI in the mid-

dle frontal gyrus, and inferior frontal gyrus (Figure 2B). Compared with

Associations between SDI differences and

3.4
gene expression

MCI in the FA-SDI, the AD group showed significantly higher SDI in the

A significant spatial association was found between AD-related

posterior superior temporal sulcus and inferior temporal gyrus, while

changes based on the SDI and nodal gene expression profiles

showing significantly lower SDI in the superior frontal gyrus, middle

(Figure 3A). The first PLS component (PLS1) accounted for a 20%

frontal gyrus, inferior frontal gyrus, and thalamus (Figure 2C). We also

found that compared to NCs, the MCI group only showed significantly

variance in gene expression and significantly correlated with the T-
map of SDI in AD versus NC (r = 0.37, p = 3.6e-8, corrected for Spin

higher FA-SDI in the thalamus (Figure 2D). The similarity-impaired pat-

terns were found in MD-SDI and FN-SDI. (Details can be found in

Figure S5.)

Associations between SDI and clinical scores

3.3
in the AD and MCI

Pearson’s correlation analyses showed that the MMSE scores were sig-

nificantly associated with 11 areas, 17 areas, and 12 areas in FA-SDI,

MD-SDI, and FN-SDI, respectively. As for FA-SDI, significant positive

correlations were found in the frontal lobe (superior frontal gyrus,

middle frontal gyrus, inferior frontal gyrus), thalamus, and inferior pari-

etal lobule, whereas significant negative correlations were found in the

inferior temporal gyrus, postcentral gyrus, cingulate gyrus, hippocam-

pus, posterior superior temporal sulcus, and insular gyrus (Figure 2E).

The FA-SDI of the middle frontal gyrus also correlated significantly

with the MoCA score (Figure 2F). Compared to FA-SDI, similar regions

can also be found in MD-SDI, and part of the above areas were found in

FN-SDI (Figure S6 and Table S6).

test), (Figure 3B and C). We found that the generation of precur-
sor metabolites and energy (GO:0006091, pFDR = 9.26e-14), inorganic
ion transmembrane transport (GO:0098660, pFDR = 6.37e-12), reg-
ulation of monoatomic ion transmembrane transport (GO:0034765,
pFDR = 1.51e-10), and mitochondrion organization (GO:0007005,
pFDR = 2.47e-10), (Figure 3D) are the most significantly correlated bio-
logical process for the alterations of the SDI. (Details can be found in

Table S7).

Multivariate classification and prediction

3.5
based on SDI

The FA-SDI could be a robust neuroimaging biomarker to distinguish
AD from NC with ACC = 0.77 (AUC = 0.864) via leave-one-site-out

cross-validation (Figure 4A, Table 1, and Table S8). More significantly,
we found a significant negative correlations (r = −0.26., p = 6.8e−6 for
AD, r = −0.18, p = 0.005 for MCI, r = −0.35, p = 1.9e−17 for AD plus

MCI) between the individual pseudo-probabilities and cognitive ability

SUN ET AL.

6311

F I G U R E 3 Association between AD-related alterations in module dynamics and gene expression profiles. (A) Gene expression profiles across
brain nodes. Each row denotes the gene expression for each gene at a given brain node. (B) Explained ratios for the first 10 components obtained
from the PLS regression analysis. Each component denotes a weighted linear combination of the expressions of all genes. (C) Spatial association
between case–control differences in modular variability and PLS1 scores. Each dot represents a brain node. (D) Gene enrichment network for PLS1
genes. The circle size represents the number of genes involved in the specific term. AD, Alzheimer’s disease; PLS, partial least squares.

measured by MMSE (Figure 4B). Furthermore, the FA-SDI could also be

4

DISCUSSION

a robust neuroimaging biomarker to predict the clinical cognitive score
(r = 0.45, p < 0.001) via leave-one-site-out cross-validation (Figure 4C).

Based on one of the largest multi-site multi-modal AD databases, the

Similar results can also be found in MD-SDI and FN-SDI compared to

present study demonstrated that the SDI could serve as a neuroimag-

FA-SDI.

ing measure for investigating the abnormal pattern of the brain’s

6312

SUN ET AL.

(A) The ROC and AUC of inter-site cross-validations. (B) Correlation between the AD probability of the test samples and MMSE

F I G U R E 4
scores. MMSE scores were z-scored within each data set and then pooled together. The results showed significant negative correlations (r = −0.26,
p = 6.8e−6 for AD, r = −0.18, p = 0.005 for MCI, r = −0.35, p = 1.9e−17 for AD plus MCI) between the individual pseudoprobabilities of AD and
MCI subjects and the cognitive ability. (C) The correlation between predicted and actual MMSE scores of seven sites using leave-one-site-out
cross-validation. AD, Alzheimer’s disease; AUC, area under the ROC curve; MCI, mild cognitive impairment; MMSE, Mini-Mental State
Examination; ROC, receiver-operating characteristic.

TA B L E 1

Site-averaged performance of classification and regression.

Classification AD from NC

FA-SDI

MD-SDI

FN-SDI

AUC

0.864

0.864

0.857

ACC

0.770

0.749

0.729

Correlation between MMSE and
AD risk score

Correlation between predicted
MMSE and actual MMSE

SEN

0.780

0.738

0.740

SPE

0.773

0.76

0.758

r

−0.346

−0.323

−0.127

p

1.91e-17

1.63e-14

3.27ee-03

R

0.459

0.445

0.272

p

1.79e-42

6.67e-40

6.64e-15

Note: The site-averaged performances of individual prediction (AD vs NC classification and MMSE regression) using the SVM model and leave-one-site-out
cross-validation with SDI features.
Abbreviations: ACC, accuracy; AD, Alzheimer’s disease; AUC, area under the receiver-operating characteristic (ROC) curve; MMSE, Mini-Mental State
Examination; SEN, sensitivity; SPE, specificity.

hierarchical structure in AD. The disease severity–associated regions

be a valuable tool for understanding this relationship. The present

largely overlapped with the altered brain areas, providing a potential

study revealed SDI distribution ranging from sensory-motor regions

biological explanation for cognitive decline in AD. Furthermore, the

most common machine learning models with leave-one-site-out cross-

to higher-order functional areas, indicating a pattern of structural
constraint on function.28 Of interest, it was consistent with brain

validation accurately predicted individual diagnostic status. The classi-

hierarchical organization, that is, brain gradient, which ranged from

fication results further support the clinical utility of SDIs as potential

biomarkers for AD. These findings shed light on the relationship

strongly aligned “unimodal” sensory cortices to weakly aligned “trans-
modal” cortices in several previous studies.15,29–32 This hierarchical

between structural–functional discrepancies, cognitive performance,

organization supports increasing levels of flexibility and dynamic pro-

and genetic pathways in AD.

cessing from primary to high-order in the brain. In sensory-motor

In previous studies, the brain’s hierarchical structure has been

regions, the functional activity could be more directly supported by

defined as the fundamental organizing principle for processing infor-
mation, ranging from the primary cortex to the transmodal cortex.11

the underlying white matter pathways to react quickly to internal or
external stimuli.33 On the contrary, brain areas at the apex of the hier-

Furthermore, it has been demonstrated that hierarchical organiza-

archy may activate more in synchrony, not only as a consequence of

tion elucidates how brain structure influences and constrains brain

function, a concept known as modal decoupling, that is, transmodal

direct signaling between them but also driven by inputs from the rest
of the brain involved in polysynaptic indirect connections.34 Conse-

cortex also occurs in a more separate pattern across multi-modal

quently, the simultaneous functional activation of regions that are not

neuroimaging measures. The SDI has been successful in quantify-

structurally linked leads to a higher SDI. Therefore, the SDI provides

ing and characterizing the relationship between brain structure and

function. Therefore, our study also demonstrated that the SDI could

a promising neuroimaging index to capture the brain’s hierarchical
organization.11

SUN ET AL.

6313

Convergence evidence suggests that the brain is characterized by
a hierarchical organization with functional–structural coupling.10,35,36

involve the structure covariance networks, that is, regional radiomics
similarity network.49,50

However, the divergence from coupling within one region and its
pathological implications are poorly understood.37 The present study

The present study characterized AD dementia–associated changes

in the brain hierarchical structure by combining multisite rs-fMRI

revealed a similar coupling throughout the brain for both AD and NC

and DTI data. The disease-severity–associated pattern of the struc-

groups, which confirmed that the dominant coupling pattern reflects

tural and functional connectivity coupling showed potential related to

a robust organizational principle of the brain. Meanwhile, we found a

energy metabolism and mitochondrial organization pathways, provid-

considerable number of regions with lower coupling in AD in the frontal

ing valuable insights into the neurobiological changes in AD. These

lobe (superior frontal gyrus, middle frontal gyrus, inferior frontal gyrus)

findings contribute to the broader understanding of the disease’s

across three SDI metrics; these regions play a crucial role in executive
function, attention, language, memory, and emotional regulation.38 In

pathophysiology in AD.

addition, our findings showed an abnormally high coupling of patients

ACKNOWLEDGMENTS

with AD in the posterior superior temporal sulcus, insular gyrus, pre-

This work was partially supported by the Science and Technology

cuneus, hippocampus, and amygdala. The hippocampus, in particular, is

Innovation 2030 Major Projects (No. 2022ZD0211600), the Beijing

known for its role in memory processing, and atrophy of the hippocam-
pus is a prominent manifestation of AD.39 These findings provide

Municipal Natural Science Foundation (No. 7244519), the Fundamen-

tal Research Funds for the Central Universities (No. 2021XD-A03), the

valuable insights into the regional variations in functional–structural

National Natural Science Foundation of China (Nos. 62333002 and

coupling in AD, suggesting that alterations in coupling within spe-

82172018), the Beijing Nova Program (20220484177), the Science

cific brain regions may underlie the cognitive decline and memory

and Technology Project of Tianjin Municipal Health Committee (Grant

impairments observed in AD. Understanding these regional differences

No. TJWJ2022MS032), and Tianjin Key Medical Discipline (Specialty)

in coupling can contribute to a deeper understanding of the neuro-

Construction Project (Grant No. TJYXZDXK-052B).

biological mechanisms of AD and potentially offer new targets for

intervention and treatment.

CONFLICT OF INTEREST STATEMENT

The metabolic abnormalities and changes in mitochondrial function
play essential roles in the development and progression of AD.40-43

The authors report no biomedical financial interests or potential con-

flicts of interest. Author disclosures are available in the supporting

Mitochondria are crucial organelles responsible for generating energy

information.

within cells,

including neurons. Any disruptions in mitochondrial

function can profoundly affect the energy supply to neurons and the

transport of materials across the cell membrane. Abnormal energy
metabolism can, in turn, impact the breakdown of the amyloid beta(Aβ)

protein, an essential protein implicated in the formation of brain
changes observed in AD.44,45 The accumulation of Aβ is associated
with the development of AD pathology.46,47 Herein, abnormal energy

metabolism can affect neuronal activity in the brain, leading to the

loss of cognitive abilities, such as memory,
language, and spatial
orientation, in patients with AD.40 These mental changes are then

reflected in the SDI alterations, which reflect the dependence on

brain structure and are highly related to the high-level cognitive

activities of the brain. Abnormalities in this transport process can

have wide-ranging effects on neurons, including signal transmission,

energy metabolism, cell growth, and differentiation. These disruptions

DATA AVAILABILITY STATEMENT

In the current study, all coding has been made publicly avail-

able through the GitHub repository maintained by YongLiuLab

(https://github.com/YongLiuLab). These data sets had conditional

acquisition from the corresponding author.

CONSENT STATEMENT

This study was consistent with the Principles of the Declaration of

Helsinki and approved by the medical research ethics committee and

institutional review board. Written informed consent was obtained

from each enrolled subject or his/her authorized guardian.

ORCID

Yong Liu

https://orcid.org/0000-0002-1862-3121

may contribute to programmed cell death and the overall neurode-
generation process seen in AD.48 Understanding these underlying

REFERENCES

mechanisms is critical for developing therapeutic strategies to slow AD

progression.

Despite the advancements presented herein, there are certain limi-

tations. First, we all have confidence in the clinical diagnosis of patients

diagnosed by experienced doctors from several famous hospitals in

China. We should admit that the AD patients were clinically diagnosed,

lacking biomarkers from cerebrospinal fluid (CSF) or positron emission

tomography (PET), which introduces the possibility of misdiagnosis. In

addition, longitudinal data sets for the MCI and AD groups should be

included in future studies. Moreover, the coupling framework should

1. Lam B, Masellis M, Freedman M, Stuss DT, Black SE. Clinical, imaging,
and pathological heterogeneity of the Alzheimer’s disease syndrome.
Alzheimers Res Ther. 2013;5(1):1. doi:10.1186/alzrt155

2. Masters CL, Bateman R, Blennow K, Rowe CC, Sperling RA, Cummings
JL. Alzheimer’s disease. Nat Rev Dis Primers. 2015;1(1):15056. doi:10.
1038/nrdp.2015.56

3. Scheltens P, De Strooper B, Kivipelto M, et al. Alzheimer’s disease.
Lancet. 2021;397(10284):1577-1590. doi:10.1016/S0140-6736(20)
32205-4

4. Amunts K, Lepage C, Borgeat L, et al. BigBrain: an ultrahigh-resolution
3D human brain model. Science. 2013;340(6139):1472-1475. doi:10.
1126/science.1235381

6314

SUN ET AL.

5. Seguin C, Sporns O, Zalesky A. Brain network communication: con-
cepts, models and applications. Nat Rev Neurosci. 2023;24(9):557-574.
doi:10.1038/s41583-023-00718-5

6. Perovnik M, Rus T, Schindlbeck KA, Eidelberg D. Functional brain net-
works in the evaluation of patients with neurodegenerative disorders.
Nat Rev Neurol. 2023;19(2):73-90. doi:10.1038/s41582-022-00753-
3

7. Park HJ, Friston K. Structural and functional brain networks: from
connections to cognition. Science. 2013;342(6158):1238411. doi:10.
1126/science.1238411

8. Bullmore E, Sporns O. Complex brain networks: graph theoreti-
cal analysis of structural and functional systems. Nat Rev Neurosci.
2009;10(3):186-198. doi:10.1038/nrn2575

9. Dai Z, He Y. Disrupted structural and functional brain connectomes
in mild cognitive impairment and Alzheimer’s disease. Neurosci Bull.
2014;30(2):217-232. doi:10.1007/s12264-013-1421-0

10. Hilgetag CC, Goulas A. ‘Hierarchy’ in the organization of brain net-
works. Philos Trans R Soc Lond B Biol Sci. 2020;375(1796):20190319.
doi:10.1098/rstb.2019.0319

11. Preti MG, Van De Ville D. Decoupling of brain function from struc-
ture reveals regional behavioral specialization in humans. Nat Commun.
2019;10(1):4747. doi:10.1038/s41467-019-12765-7

12. Honey CJ, Thivierge JP, Sporns O. Can structure predict function
in the human brain. Neuroimage. 2010;52(3):766-776. doi:10.1016/j.
neuroimage.2010.01.071

13. Honey CJ, Sporns O, Cammoun L, et al. Predicting human resting-state
functional connectivity from structural connectivity. Proc Natl Acad Sci
U S A. 2009;106(6):2035-2040. doi:10.1073/pnas.0811168106
14. Deco G, Kringelbach ML, Arnatkeviciute A, et al. Dynamical con-
sequences of regional heterogeneity in the brain’s transcriptional
landscape. Sci Adv. 2021;7(29):eabf4752. doi:10.1126/sciadv.abf4752
15. Yu H, Ding Y, Wei Y, et al. Morphological connectivity differences in
Alzheimer’s disease correlate with gene transcription and cell-type.
Hum Brain Mapp. 2023;44:6364-6374. doi:10.1002/hbm.26512
16. Atasoy S, Deco G, Kringelbach ML, Pearson J. Harmonic brain modes: a
unifying framework for linking space and time in brain dynamics. Neu-
roscientist. 2018;24(3):277-293. doi:10.1177/1073858417728032
17. Huang W, Bolton TAW, Medaglia JD, Bassett DS, Ribeiro A, Van De
Ville D. A graph signal processing perspective on functional brain
imaging. Proceedings of the IEEE. IEEE; 2018;106(5):868-885. doi:10.
1109/jproc.2018.2798928

18. Sydnor VJ, Larsen B, Bassett DS, et al. Neurodevelopment of the
association cortices: patterns, mechanisms, and implications for
psychopathology. Neuron. 2021;109(18):2820-2846. doi:10.1016/j.
neuron.2021.06.016

19. Qu Y, Wang P, Yao H, et al. Reproducible abnormalities and diagnostic
generalizability of white matter in Alzheimer’s disease. Neurosci Bull.
2023;39(10):1533-1543. doi:10.1007/s12264-023-01041-w

25. Lipták T. On the combination of independent tests. Magyar Tud Akad

Mat Kutato Int Kozl. 1958;3:171-197.

26. Zhou Y, Zhou B, Pache L, et al. Metascape provides a biologist-oriented
resource for the analysis of systems-level datasets. Nat Commun.
2019;10(1):1523. doi:10.1038/s41467-019-09234-6

27. Zhao K, Ding Y, Han Y, et al. Independent and reproducible hippocam-
pal radiomic biomarkers for multisite Alzheimer’s disease: diagnosis,
longitudinal progress and biological basis. Sci Bull. 2020;65(13):1103-
1113. doi:10.1016/j.scib.2020.04.003

28. Pang JC, Aquino KM, Oldehinkel M, et al. Geometric constraints on
human brain function. Nature. 2023;618(7965):566-574. doi:10.1038/
s41586-023-06098-1

29. Margulies DS, Ghosh SS, Goulas A, et al. Situating the default-mode
network along a principal gradient of macroscale cortical organization.
Proc Natl Acad Sci U S A. 2016;113(44):12574-12579. doi:10.1073/
pnas.1608282113

30. Dong HM, Margulies DS, Zuo XN, Holmes AJ. Shifting gradients of
macroscale cortical organization mark the transition from childhood
to adolescence. Proc Natl Acad Sci U S A. 2021;118(28):e2024448118.
doi:10.1073/pnas.2024448118

31. Vázquez-Rodríguez B, Suárez LE, Markello RD, et al. Gradients of
structure-function tethering across neocortex. Proc Natl Acad Sci U S
A. 2019;116(42):21219-21227. doi:10.1073/pnas.1903403116
32. Baum GL, Cui Z, Roalf DR, et al. Development of structure-function
coupling in human brain networks during youth. Proc Natl Acad Sci U
S A. 2020;117(1):771-778. doi:10.1073/pnas.1912034117

33. Mesulam MM. From sensation to cognition. Brain. 1998;121(Pt

6):1013-1052. doi:10.1093/brain/121.6.1013

34. Buckner RL, Krienen FM. The evolution of distributed association
networks in the human brain. Trends Cogn Sci. 2013;17(12):648-665.
doi:10.1016/j.tics.2013.09.017

35. Kringelbach ML, Cruzat J, Cabral J, et al. Dynamic coupling of whole-
brain neuronal and neurotransmitter systems. Proc Natl Acad Sci U S A.
2020;117(17):9566-9576. doi:10.1073/pnas.1921475117

36. Gordon EM, Laumann TO, Marek S, et al. Default-mode net-
work streams for coupling to language and control systems. Proc
Natl Acad Sci U S A. 2020;117(29):17308-17319. doi:10.1073/pnas.
2005238117

37. Suárez LE, Markello RD, Betzel RF, Misic B. Linking structure and func-
tion in macroscale brain networks. Trends Cogn Sci. 2020;24(4):302-
315. doi:10.1016/j.tics.2020.01.008

38. De Jager PL, Ma Y, McCabe C, et al. A multi-omic atlas of the human
frontal cortex for aging and Alzheimer’s disease research. Sci Data.
2018;5(1):180142. doi:10.1038/sdata.2018.142

39. Mueller SG, Schuff N, Yaffe K, Madison C, Miller B, Weiner MW.
Hippocampal atrophy patterns in mild cognitive impairment and
Alzheimer’s disease. Hum Brain Mapp. 2010;31(9):1339-1347. doi:10.
1002/hbm.20934

20. Chen P, Zhao K, Zhang H, et al. Altered global signal topography
in Alzheimer’s disease. EBioMedicine. 2023;89:104455. doi:10.1016/j.
ebiom.2023.104455

40. de la Monte SM, Tong M. Brain metabolic dysfunction at the core of
Alzheimer’s disease. Biochem Pharmacol. 2014;88(4):548-559. doi:10.
1016/j.bcp.2013.12.012

21. Chen P, Yao H, Tijms BM, et al. Four distinct subtypes of Alzheimer’s
disease based on resting-state connectivity biomarkers. Biol Psychiatry.
2023;93(9):759-769. doi:10.1016/j.biopsych.2022.06.019

22. Jin D, Wang P, Zalesky A, et al. Grab-AD: generalizability and repro-
ducibility of altered brain activity and diagnostic classification in
Alzheimer’s disease. Hum Brain Mapp. 2020;41(12):3379-3391. doi:10.
1002/hbm.25023

23. Xie S, Chen L, Zuo N, Jiang T. DiffusionKit: a light one-stop solution
for diffusion MRI data analysis. J Neurosci Methods. 2016;273:107-119.
doi:10.1016/j.jneumeth.2016.08.011

24. Bortolin K, Delavari F, Preti MG, et al. Neural substrates of psychosis
revealed by altered dependencies between brain activity and white-
matter architecture in individuals with 22q11 deletion syndrome.
Neuroimage Clin. 2022;35:103075. doi:10.1016/j.nicl.2022.103075

41. Zhu X, Perry G, Smith MA, Wang X. Abnormal mitochondrial dynam-
ics in the pathogenesis of Alzheimer’s disease. J Alzheimers Dis.
2013;33(Suppl 1(0)1):S253-S262. doi:10.3233/JAD-2012-129005
42. Zhao K, Zheng Q, Dyrba M, et al. Regional radiomics similarity net-
works reveal distinct subtypes and abnormality patterns in mild
cognitive impairment. Adv Sci. 2022;9(12):e2104538. doi:10.1002/
advs.202104538

43. Zhao K, Chen P, Alexander-Bloch A, et al. A neuroimaging biomarker
for Individual Brain-Related Abnormalities In Neurodegeneration
(IBRAIN): a cross-sectional study. EClinicalMedicine. 2023;65:102276.
doi:10.1016/j.eclinm.2023.102276

44. Wang W, Zhao F, Ma X, Perry G, Zhu X. Mitochondria dysfunc-
tion in the pathogenesis of Alzheimer’s disease: recent advances. Mol
Neurodegener. 2020;15(1):30. doi:10.1186/s13024-020-00376-6

SUN ET AL.

6315

45. Wang X, Su B, Zheng L, Perry G, Smith MA, Zhu X. The role of abnormal
mitochondrial dynamics in the pathogenesis of Alzheimer’s disease.
J Neurochem. 2009;109(Suppl1):153-159. doi:10.1111/j.1471-4159.
2009.05867.x

46. van der Kant R, Goldstein LSB, Ossenkoppele R. Amyloid-beta-
independent regulators of tau pathology in Alzheimer disease. Nat Rev
Neurosci. 2020;21(1):21-35. doi:10.1038/s41583-019-0240-3

47. Chételat G, Arbizu J, Barthel H, et al. Amyloid-PET and (18)F-FDG-
PET in the diagnostic investigation of Alzheimer’s disease and other
dementias. Lancet Neurol. 2020;19(11):951-962. doi:10.1016/S1474-
4422(20)30314-8

48. Jellinger KA. Basic mechanisms of neurodegeneration: a critical
update. J Cell Mol Med. 2010;14(3):457-487. doi:10.1111/j.1582-
4934.2010.01010.x

49. Zhao K, Zheng Q, Che T, et al. Regional radiomics similarity networks
(R2SNs) in the human brain: reproducibility, small-world properties,
and a biological basis. Netw Neurosci. 2021;5(3):783-797. doi:10.1162/
netn_a_00200

50. Zhao K, Lin J, Dyrba M, et al. Coupling of the spatial distributions
between sMRI and PET reveals the progression of Alzheimer’s disease.
Netw Neurosci. 2023;7(1):86-101. doi:10.1162/netn_a_00271

SUPPORTING INFORMATION

Additional supporting information can be found online in the Support-

ing Information section at the end of this article.

How to cite this article: Sun Y, Wang P, Zhao K, et al.

Structure–function coupling reveals the brain hierarchical

structure dysfunction in Alzheimer’s disease: A multicenter

study. Alzheimer’s Dement. 2024;20:6305–6315.

https://doi.org/10.1002/alz.14123
