# Jiang_2020_Distinct structural brain circuits indicate mood and apathy profiles in bipolar disorder.

NeuroImage: Clinical 26 (2020) 101989

Contents lists available at ScienceDirect

NeuroImage: Clinical

journal homepage: www.elsevier.com/locate/ynicl

Distinct structural brain circuits indicate mood and apathy profiles in
bipolar disorder

T

Wenhao Jianga, Ole A. Andreassenb,i, Ingrid Agartzc,d,e, Trine V. Lagerbergb,i, Lars T. Westlyeb,c,i,
Vince D. Calhouna,f,g,h, Jessica A. Turnera,⁎
a Department of Psychology, Georgia State University, USA
b NORMENT, Institute of Clinical Medicine, University of Oslo, Norway
c Department of Psychology, University of Oslo, Oslo, Norway
d Department of Psychiatry, Diakonhjemmet Hospital, Oslo, Norway
e Department of Clinical Neuroscience, Centre for Psychiatric Research, Karolinska Institutet, Stockholm, Sweden
f Department of Electrical and Computer Engineering, The University of New Mexico, USA
g The Mind Research Network and Lovelace Biomedical and Environmental Research Institute, USA
h Tri-institutional Center for Translational Research in Neuroimaging and Data Science (TReNDS), Georgia State University, Georgia Institute of Technology, Emory
University, Atlanta, GA, USA
i Division of Mental Health and Addiction, Oslo University Hospital, Norway

A B S T R A C T

Bipolar disorder (BD) is a severe manic-depressive illness. Patients with BD have been shown to have gray matter (GM) deficits in prefrontal, frontal, parietal, and
temporal regions; however, the relationship between structural effects and clinical profiles has proved elusive when considered on a region by region or voxel by
voxel basis. In this study, we applied parallel independent component analysis (pICA) to structural neuroimaging measures and the positive and negative syndrome
scale (PANSS) in 110 patients (mean age 34.9 ± 11.65) with bipolar disorder, to examine networks of brain regions that relate to symptom profiles. The pICA
revealed two distinct symptom profiles and associated GM concentration alteration circuits. The first PANSS pICA profile mainly involved anxiety, depression and
guilty feelings, reflecting mood symptoms. Reduced GM concentration in right temporal regions predicted worse mood symptoms in this profile. The second PANSS
pICA profile generally covered blunted affect, emotional withdrawal, passive/apathetic social withdrawal, depression and active social avoidance, exhibiting a
withdrawal or apathy dominating component. Lower GM concentration in bilateral parietal and frontal regions showed worse symptom severity in this profile. In
summary, a pICA decomposition suggested BD patients showed distinct mood and apathy profiles differing from the original PANSS subscales, relating to distinct
brain structural networks.

1. Introduction

Bipolar disorder (BD) is a debilitating psychiatric disorder that
causes morbidity and disability worldwide throughout the lifespan
(Grande et al., 2016; Merikangas et al., 2011). Despite continuous re-
search efforts, the neurobiological mechanism of BD remains unclear
(Dunner, 2003; Lawrie et al., 2016). However, noninvasive brain ima-
ging such as structural magnetic resonance imaging (sMRI) has suc-
cessfully characterized BD with wide range brain abnormalities (Hibar
et al., 2018).

In the recent large cohort meta-analysis of sMRI studies, the
ENIGMA (Enhancing Neuro Imaging Genetics Through Meta-Analysis)
bipolar working group identified consistent and robust subcortical vo-
lume differences including smaller hippocampus, thalamus and en-
larged lateral ventricles (Hibar et al., 2016), and thinner frontal, tem-
poral and parietal cortex (Hibar et al., 2018) in patients compared to

controls. These differences show overlap with volumetric differences
also found in schizophrenia (SZ) but are not as marked (Rimol et al.,
2010; Rimol et al., 2012; van Erp et al., 2018); they are also similar but
not identical to differences found in major depressive disorders (MDD)
(Wise et al., 2017).

BD patients can exhibit a wide range of cognitive deficits and
symptoms, which overlap with other psychiatric disorders (Hozer and
Houenou, 2016; Whalley et al., 2012). Various cognitive domain defi-
cits have been related to corresponding brain regions in BD (Fears et al.,
2015; Gutierrez-Galve et al., 2012; Kieseppa et al., 2014; Killgore et al.,
2009; Shepherd et al., 2015). The clinically observed behaviors and
symptoms are even more difficult to explore, and yield inconsistent
findings (Sharma et al., 2017; Wise et al., 2017). BD are often studied
together with MDD for mood symptoms or together with the schizo-
phrenia spectrum for psychosis symptoms. Though BD along with MDD
commonly show reductions in prefrontal, frontal, temporal and anterior

⁎

Corresponding author at: Psychology and Neuroscience, Georgia State University, Atlanta, GA, USA.
E-mail address: jturner63@gsu.edu (J.A. Turner).

https://doi.org/10.1016/j.nicl.2019.101989
Received 17 April 2019; Received in revised form 1 August 2019; Accepted 16 August 2019
Available online 19 August 2019
2213-1582/ © 2019 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license 
(http://creativecommons.org/licenses/BY-NC-ND/4.0/).

W. Jiang, et al.

NeuroImage: Clinical 26 (2020) 101989

cingulate cortex (Han et al., 2019), the relationship with depression
severity is unclear and inconsistent (Wise et al., 2017). Mania, however,
shows a close relationship with prefrontal regions, and the onset times
of mania leading to reduction of GM (Abe et al., 2015). Anhedonia
severity relates to some shared deficits in the reward system in BD,
MDD, and SZ (Nusslock and Alloy, 2017; Redlich et al., 2015; Sharma
et al., 2017). Similar to SZ, BD subjects show cortical deficits in frontal
and temporal regions associated with positive symptoms, and frontal
regions also with negative symptoms
(Hartberg et al., 2011;
Padmanabhan et al., 2015; Strauss et al., 2019). However, many of
these associations are inconsistent due to the disorders' heterogeneity,
both in terms of brain structural underpinnings (Wolfers et al., 2018)
and clinical symptoms (Nunes et al., 2018). Considering the complexity,
it is important to study the patients' symptoms from a multivariate
profile point of view, and the aggregation of regional brain alterations
may help to reveal the brain mechanism behind specific symptom
profiles (Liu and Calhoun, 2014; Xu et al., 2009).

To comprehensively assess and create a clinical profile on hetero-
geneous BD patients and clinical observations, the positive and negative
syndrome scale (PANSS) (Kay et al., 1987) can be an appropriate tool.
The PANSS provides a wide range assessment including positive, ne-
gative and general symptoms, and it is useful to detect psychotic
symptom groups and behavioral traits. In PANSS, the positive symp-
toms score includes delusions, conceptual disorganization, hallucina-
tions, excitement, grandiosity, suspiciousness, and hostility. The nega-
tive scores include blunted affect, emotional withdrawal, poor rapport,
passive/apathetic social withdrawal, difficulty in abstract thinking, lack
of spontaneity and flow of conversation, and stereotyped thinking.
Importantly, PANSS has already proved its usefulness in discovering the
potential relationship between clinical dimensions and brain alterations
(Koutsouleris et al., 2008; Wang et al., 2018). The PANSS positive
symptom severity has been associated with GM concentrations in left
perisylvian regions and thalamus, and negative symptom severity with
orbitofrontal, prefrontal,
in SZ
(Koutsouleris et al., 2008). However, a study using the functional
connectome identified the fronto-parietal control network and sensor-
imotor regions to be associated with PANSS positive in SZ, while in BD
it is the visual and default mode network (Wang et al., 2018). The in-
clusion of PANSS in previous studies, however, are often still limited to
the originally designed positive, negative and general subscales (Walton
et al., 2017; Walton et al., 2018).

and limbic

temporal

regions

Here, we employ parallel independent component analysis (pICA) to
reveal the relationship between clinical profiles and the structural brain
patterns of BD patients. pICA is a higher order statistical method which
can be used to establish association between different data modalities
(Calhoun et al., 2009; Chen et al., 2013; Liu et al., 2009; Meda et al.,
2012; Pearlson et al., 2015). Single-modality ICA identifies maximally
independent components through blind source separation in one data
modality. pICA performs individual ICA on two data modalities si-
multaneously, and it aims to maximize independence in each modality
while optimizing the correlation between the components from both
modalities. The output of pICA provides the correlation between two
modalities, and loading coefficients of both modalities are calculated
for each subject which indicate the contribution of the generated pat-
tern to the subject's original data. This blind source separation proceeds
automatically, and no prior knowledge and intervention needs be taken
into account for this analytical method (Gupta et al., 2015). Previous
pICA analysis in SZ has provided a mapping of symptom profiles onto
the brain structures, and a distinct PANSS profile characterized by de-
lusions, suspiciousness, hallucinations, and anxiety was associated with
GM concentration patterns including inferior temporal gyrus, fusiform
gyrus and the sensorimotor cortex (Mennigen et al., 2019).

In this study, pICA was performed on GM concentration and PANSS
items scores obtained from 110 BD patients. We hypothesized that pICA
would identify multimodal components reflecting the joint variance
between specific PANSS profiles and distinct structural brain patterns.

Specifically, based on the studies reviewed above, we hypothesized that
pICA would reveal patterns implicating persistent behavioral deficits
and fronto-parietal brain networks.

2. Materials and methods

2.1. Participants

This study used data from 110 patients with bipolar I (n = 69) or II
(n = 41) diagnoses from the Thematically Organized Psychosis (TOP)
study at
the Norwegian Centre for Mental Disorders Research
(NORMENT) in Oslo, Norway (Rimol et al., 2012; Ringen et al., 2008).
All data were collected with approval from the local institutional re-
view board, and all participants signed informed consent. Patients met
following criteria to be included in the study: 1) aged from 18 to
65 years; 2) understood and spoke a Scandinavian language; 3) had no
history of severe head trauma; 4) had IQ over 70. The diagnosis of bi-
polar I (DSM-IV 296.0-7) and bipolar 2 (DSM-IV 296.89) was estab-
lished by the Structured Clinical Interview for DSM-IV Axis I Disorders.
At the stage of enrollment, the mood status of the patients was identi-
fied as depressive (n = 60), manic (n = 5), euthymic (n = 40), mixed
(n = 2) and unspecified (n = 3). In addition, 54 patients (approxi-
mately 50%) experienced at least one lifetime psychotic episode.
PANSS scores and structural MRI data were available for all the parti-
cipants, and detailed demographic and scanning information are pre-
sented in Table 1.

2.2. Positive and negative symptom scores (PANSS)

All participants provided complete PANSS item scores, which in-
cluded all 30 items of PANSS with positive, negative and general
symptom dimensions.

2.3. Neuroimaging acquisition and preprocessing

All patients were scanned on a 1.5 T Siemens Magnetom Sonata
scanner (Siemens Medical Solutions, Erlangen, Germany) scanner. T1-
weighted structural MRI data were collected using a MPRAGE se-
quence. T1-weighted images were normalized to the standard Montreal
Neurological Institute (MNI) template using a 12-parameter affine
model, resliced to a voxel size of 2 × 2 × 2 mm and segmented into
GM, white matter, and cerebro-spinal fluid using Statistical Parametric
Mapping 12 (SPM12, http://www.fil.ion.ucl.ac.uk/spm/software/
spm12/). To identify possible outliers, individual scans were corre-
lated with group GM template, and the correlation was computed. One
showing low correlation with the group GM template
subject
(ρ < 0.98) was excluded. 109 participants were included in following
analysis. Voxel-wise regression of age and gender was performed to
remove their possible effects. Structural MRI data were smoothed with
a 10 mm full width at half maximum Gaussian kernel (Gupta et al.,

Table 1
Demographic and scanning information, N = 110.

Age(years)
Females (N/%)
Duration of illness(years)
PANSS positive score
PANSS negative score
PANSS general score
PANSS total score
Field strength (T)
Sequence
Voxel size (mm)
Scanning orientation

SD

11.65

10.09
3.28
3.54
5.82
10.33

Mean

34.87
72 (65%)
12.13
9.81
9.75
25.42
44.96
1.5
MPRAGE
1.33 × 0.94 × 1
Sagittal

PANSS: Positive and Negative Syndrome Scale.

2

W. Jiang, et al.

2015).

2.4. Parallel independent component analysis (pICA)

Fusion ICA Toolbox (FIT, http://mialab.mrn.org/software/fit/) was
employed to perform pICA on the preprocessed structural images and
PANSS item scores. The optimal component number of structural MRI
data was estimated to be 25 by the minimum description length (MDL)
algorithm (Rissanen, 1978). The components for PANSS items was set
to three according to its inner structure (positive, negative and general
symptom dimensions). A GM mask was applied on structural images
before ICA was performed. To ensure stability of component estimation,
infomax ICA was run 20 times, and the central point of 20 runs was
selected as the final component using ICASSO (Himberg et al., 2004).
Using the default setting of pICA, three components in each modality
were constrained to be optimized (Liu et al., 2009). More specifically,
the correlation between the loading coefficients of sMRI and PANSS was
optimized through pICA while independence within each modality was
further maximized.

2.5. Validations

After the original pICA analysis, 10-fold cross-validation was per-
formed to ensure that the pICA estimation was not driven by a subset of
participants or potential outliers. Each validation run included 90% of
the individuals of the sample. Parameter settings of 10-fold validation
were essentially the same as the original analysis. The results from each
fold were examined for overlap with the original pICA.

2.6. Additional analysis

To control possible confounders, duration of illness (DOI) and cur-
rent medication status were assessed in this study. The current medi-
cation status was included as a binary variable according to whether or
not the patient was currently on antipsychotic, antiepileptic or lithium
treatment (Hartberg et al., 2015; Jorgensen et al., 2016). The medica-
tion effect was tested on GM concentrations and PANSS loading coef-
ficients.

The relations of original PANSS subscale scores (positive, negative
and general symptoms), PANSS loading coefficients and sMRI loading
coefficients from pICA were also assessed.

3. Results

3.1. Parallel independent component analysis

Two pairs of sMRI and PANSS components showed significant cor-
relations, passing the Bonferroni correction threshold of 6.67 × 10−04
(determined by 25 sMRI components and 3 PANSS components). In the
first pair of components, the correlation between the structural MRI and
PANSS components was Pearson's r = −0.41 (p = 7.67 × 10−06)
(Fig. 1). In the second pair, the correlation was Pearson's r = −0.35
(p = 1.80 × 10−04)(Fig. 3). The negative correlation indicated that
greater loading coefficients of sMRI correlated with lower loadings of
symptom profile represented by PANSS.

In the first pair, the sMRI component showed positively contributing
GM concentration mainly in right middle/superior temporal gyrus in
the more medial aspect (extended to inferior frontal gyrus, see Fig. 2a
and Table 2). The corresponding PANSS component was positively
weighted strongly on anxiety (G2), guilty feelings (G3) and depression
(G6); the lack of spontaneity and flow of conversation (N6) was nega-
tively associated with this component (Fig. 2b). Participants with
higher preserved GM concentration in right superior/middle temporal
gyrus exhibited reduced severity in these symptoms consisting of an-
xiety, guilty feelings and depression.

In the second pair, positively contributing GM concentration was

NeuroImage: Clinical 26 (2020) 101989

Fig. 1. Negative correlation between loading coefficients of the first PANSS
component and sMRI component.
Pearson's
= 6.67−04).

r = −0.41, P = 7.67 × 10−06

(Bonferroni-corrected threshold

mainly located in bilateral middle frontal gyrus, bilateral parietal lo-
bule including postcentral gyrus with temporal regions on the left side
(left inferior, middle and superior temporal gyrus), and negatively
contributing GM concentration was located in left supramarginal gyrus
for the sMRI component (see Fig. 4a and Table 2). The PANSS com-
ponent was positively weighted strongly on blunted affect (N1), emo-
tional withdrawal (N2), passive/apathetic social withdrawal (N4), de-
pression (G6) and active social avoidance (G16), and excitement (P4)
and guilty feeling (G3) was negatively associated with this component
(Fig. 4b). In summary, participants with higher preserved GMC in bi-
lateral frontal, parietal and left temporal regions show milder severity
for these symptoms.

3.2. 10-Fold validation

The 10-fold validation showed high correlation with the original
pICA results in both of the pairs of components. For the first pair, 7 out
of 10 validation runs showed similar results to the original output, with
one of run showing an inverted direction of sMRI and PANSS correla-
tion to the other runs. The first pair presented a mean correlation of
Pearson's r = 0.75 of above replicated runs. The second pair also pre-
sented similar stability, with 7 out of 10 validation runs showing similar
results to the original output and two of the runs showing inverted
direction of sMRI and PANSS correlation to the other runs. The second
pair presented a mean correlation of Pearson's r = 0.67 of its replicated
runs.

3.3. Additional analysis

In the regression model including loadings coefficients of sMRI
components as dependent variable and DOI values as predictors, there
was no significant association between the DOI and component 1
(β = −0.10,
t = −1.06, p = .29) or component 2 (β = −0.004,
t = −0.043, p = .97). The regression model including loadings coeffi-
cients of PANSS components as dependent variable and DOIs as pre-
dictors also showed no significant association in component 1
(β = 0.01, t = 0.08, p = .94) or component 2 (β = −0.05, t = −0.49,
p = .63).

There was no significant correlation between medication status and
the sMRI loading coefficients in component 1 (Spearman's ρ = 0.10,
p = .33) or component 2 (Spearman's ρ = −0.06, p = .56). In addition,

3

W. Jiang, et al.

NeuroImage: Clinical 26 (2020) 101989

Fig. 2. Parallel ICA results - the first pair – ‘mood’ component a) structural MRI and b) PANSS components.
PANSS items with |Z| > 1: N6 – Lack of spontaneity and flow of conversation; G2 – Anxiety; G3 – Guilty feelings; G6 – Depression.

there was no significant correlation between medication status and the
PANSS loading coefficients in component 1 (Spearman's ρ = −0.06,
p = .57) or component 2 (Spearman's ρ = −0.14, p = .88).

In the first pair, the correlation between the original PANSS subscale
scores and the pICA derived PANSS loading coefficients revealed no
association with PANSS positive (Pearson's r = 0.017, p = .86), nega-
tive (Pearson's r = 0.15, p = .88), or general (Pearson's r = 0.062,
p = .53) scores. In addition, sMRI component loading coefficients were
not significantly correlated with PANSS positive (Pearson's r = 0.023,
r = −0.039, p = .69), and general
p = .82), negative (Pearson's
(Pearson's r = −0.031, p = .75) scores.

In the second pair, there was also no significant correlation found
between the pICA PANSS component loading and PANSS positive
(Pearson's r = 0.074, p = .45), negative (Pearson's r = 0.11, p = .27),
or general (Pearson's r = 0.11, p = .26) scores. In the sMRI, the loading
coefficients were not significantly correlated with PANSS positive
(Pearson's
r = −0.031,
p = .75) and general (Pearson's r = −0.061, p = .53) scores.

r = 0.072, p = .45), negative (Pearson's

4. Discussion

In this study, we find two gray matter networks that relate to two
different patterns of
symptom severity in a large BP sample.
Importantly, the PANSS profiles highlighted here were not constructed
according to the typical PANSS subscales, but were driven by the

4

Fig. 3. Negative correlation between loading coefficients of the second pair of
PANSS component and the sMRI component.
Pearson's r = −0. 35, P = 1.80 × 10−04 (Bonferroni-corrected threshold
= 6.67−04).

a)Structural MRI component b)PANSS component W. Jiang, et al.

NeuroImage: Clinical 26 (2020) 101989

Table 2
Brain regions, peak coordinates and volumes of component 1 and 2.

Brain regions

Brodmann area

Volumes (cc3)

Peak coordinates (Z and coordinates)

Component 1
Cluster 1
Cluster 2
Component 2
Cluster 1/2
Cluster 3/4
Cluster 5
Cluster 6
Cluster 7
Cluster 8

R superior temporal gyrus (extended to inferior frontal gyrus & insula)
R middle temporal gyrus

L/R parietal lobe (postcentral gyrus)
L/R frontal lobe (middle frontal gyrus)
L inferior middle temporal gyrus, posterior
L inferior parietal lobule
L parietal lobe (L angular gyrus)
L supramarginal gyrus

48
39

3,3
9,8
37
41
7
40

3.6
2.7

5.7/5.5
5.4/3.0
3.4
2.9
2.7
4.6

6.0 (48, 14, −6)
7.8 (38, −62, 22)

3.3(−40,-26, 40)/5.5(46, −26, 36)
5.4(−26,32,32)/6.4(22, 12, 46)
7.6(−46,-58,-6)
7.6(−46,-46,22)
7.3(−30,-60,38)
−7.3(−42,-46,38)

Note: For both components, Z score was set > 3, and cluster volumes were set > 2 cc3 to retain their most significant results. Brodmann areas are listed for the peak
coordinates. The directions of peak Z scores indicate whether the brain region contributed positively or negatively to the component as red for positive and blue for
negative in brain maps.

underlying relationships with gray matter patterns. The mood profile
was correlated with reductions in the right temporal gyrus, while the
apathy/asocial profile correlated with a more widespread network in-
cluding frontal, temporal and parietal regions. It implicated the GM
deficits in regional temporal lobe and frontal-temporal-parietal circuits
that were separately related to clinical profiles as mood and apathy.

The PANSS component for the first pair mainly included anxiety,

guilty feelings and depression (all Z-scores > 1.5), with the lack of
spontaneity and flow of conversation contrasting with those symptoms
but less strongly (Z-score = −1.08). This represents a generally nega-
tive mood component, differing from the original design of the PANSS
of positive, negative and general symptom dimensions. This mood
component showed similar affective items emphasized in affective
affective
temperaments

In addition,

al., 2010).

(Rihmer

et

Fig. 4. Parallel ICA results - the second pair – ‘apathy’ component a) structural MRI and b) PANSS components.
PANSS items with |Z| > 1: P4 – Excitement; N1 – Blunted affect; N2 – Emotional withdrawal; N4 – Passive/apathetic social withdrawal; G3 – Guilty feelings; G6 –
Depression;G16 – Active social avoidance.

5

a)Structural MRI component b)PANSS component W. Jiang, et al.

NeuroImage: Clinical 26 (2020) 101989

temperaments patterns (the relative balance of hyperthymic vs cy-
clothymic-irritable-anxious-dysthymic) has been significantly asso-
ciated with hopelessness, negative outcomes, and potential psycho-
pathology (Pompili et al., 2012). The structural brain component for
this profile was mainly located in right temporal regions (including
middle and superior temporal gyrus extended to inferior frontal gyrus).
The negative correlation between components indicated that higher GM
temporal regions exhibited milder mood
concentrations in right
symptoms, or lower concentrations exhibited worse mood.

The temporal regions' deficits are common in BD and other psy-
chiatric disorder (Abe et al., 2016; Hanford et al., 2016; Whalley et al.,
2012), though its relationship with mood symptoms can be elusive, and
few studies have formed a direct association between the mood symp-
toms and brain structure alterations (Busatto, 2013; Hozer and
Houenou, 2016; Padmanabhan et al., 2015; Palaniyappan and Cousins,
2010; Selvaraj et al., 2012). Among psychiatric symptoms, temporal
regions (mostly in superior temporal gyrus) are believed to be im-
portant in thought disorders, auditory verbal hallucinations and across
the positive symptom domains in psychosis (Cavelti et al., 2018; Morch-
Johnsen et al., 2018; Morch-Johnsen et al., 2017; Padmanabhan et al.,
2015; Strik et al., 2017), while mood symptoms are usually believed to
be centered in the large regions including frontal, temporal and limbic
regions (Garety and Freeman, 2013; Lebow and Chen, 2016; Ramirez
et al., 2015). The structural brain studies emphasize the important role
of multiple involvement of temporal regions especially superior tem-
poral gyrus (Hanford et al., 2016). Cortical thickness in right superior
frontal and superior temporal has been negatively correlated with Ha-
milton Depression Rating Scale (Maller et al., 2014). In addition, cor-
tical thickness reduction in middle temporal gyrus has been negatively
correlated with the global assessment of functioning, which indicated
worse overall symptoms. However, it must be pointed out that, despite
these significant structure/mood symptom studies, there has been even
more structural imaging research in BD which reported no correlation
between structural alterations and mood symptom severity (Doan et al.,
2017; Elvsashagen et al., 2013; Hanford et al., 2016; Lan et al., 2014;
Ratnanather et al., 2014). Functional studies have provided some evi-
dence to support the role of superior/middle temporal gyrus in mood
regulations (Whalley et al., 2012). An emotional prosody task indicated
BD patients exhibited stronger activation in bilateral superior temporal
gyrus and right inferior frontal gyrus compared to controls (Mitchell
et al., 2004). Also, in an emotional memory task, the role of left su-
perior temporal gyrus was highlighted (Whalley et al., 2009). The exact
role of the discovered middle/superior temporal gyrus in modulating
such mood components clearly needs to be further investigated.

The PANSS component for the second pair was strongly weighted on
blunted affect, emotional withdrawal, passive/apathetic social with-
drawal, depression and active social avoidance, while excitement along
with guilty feeling was contributing negatively. In addition to negative
symptoms, this PANSS component also included all the withdrawal/
avoidance items along with depression. The PANSS component here
was a combination of negative and general symptoms highlighting
behavioral deficits involving asociality. From SZ research, a two-factor
model of the PANSS has identified anhedonia-asociality-avolition as a
general motivation and pleasure (MAP) factor while alogia/blunted
affect as an expressive (EXP) factor. However, asociality was not in-
cluded in this model (Jang et al., 2016). In addition, when negative
symptoms were observed across different psychiatric disorders, apathy
was another common term to describe such motivational deficits.
Moreover, previous studies using subsets of
the TOP sample in-
vestigated apathy comparing Apathy Evaluation Scale (AES) and PANSS
(Faerden et al., 2009; Faerden et al., 2008; Morch-Johnsen et al., 2015).
In these studies, emotional withdrawal (N2), passive/apathetic social
withdrawal (N4), and lack of spontaneity and flow of conversation (N6)
were chosen to form the apathy score from PANSS to compare with
AES, while N2 and N4 were chosen according to Marin's definition of
apathy (Marin et al., 1991). They found the apathy items from PANSS

significantly correlated with AES.

In this pICA approach we find emotional withdrawal (N2) and
passive/apathetic social withdrawal (N4) along with blunted affect
(N1) and depression (G6, considering depression's relationship with
anhedonia) included in the ‘apathy’ or withdrawal profile. The role of
active social avoidance is more complicated. Active social avoidance
refers to the social avoidance caused by unwarranted fear, hostility, or
distrust (Hansen et al., 2009). Some studies argue it is weighted on
positive symptoms (van der Gaag et al., 2006), while others that it is
weighted on depression or anxiety (Bell et al., 1994) or not related to
the preset factors of PANSS items (White et al., 1997). We suggest ac-
tive social avoidance, regardless of its cause, should be seen as part of
asociality while grouped into this ‘apathy’ component. In addition, si-
milar to the mood component, this ‘apathy’ component was also con-
structed beyond the original PANSS structure. In this automatic data
reduction process, active social avoidance survived and weighted
heavily in this component. All the PANSS items are relating to with-
drawal and avoidance at the clinical observation level. This withdrawal
component describes another unique clinical aspect of BD patients in
TOP research. The sMRI component associated with this ‘apathy’
component was largely located in frontal-parietal-temporal regions
with an isolated region in left supramarginal gyrus (contributing ne-
gatively).

Apathy is commonly observed in mood and psychotic disorders
(Grande et al., 2016). This frontal-parietal-temporal circuit is also the
important deficits in BD brain abnormalities (Dusi et al., 2019; Han
et al., 2019; Shahab et al., 2018). Regarding its connection to symp-
toms, one recent connectome study suggested the frontal-parietal cir-
cuit was able to track the positive and negative symptoms assess by
PANSS, though structural connectivity was not able to predict symptom
dimensions (Wang et al., 2018). Another interesting comparison was
suggested by the BSNIP research (Clementz et al., 2016; Ivleva et al.,
2016; Meda et al., 2015). GM concentration was checked in these three
biotypes of BSNIP study, and the concentration loss followed the same
order as cognitive decline: biotype 1 showed whole brain gray matter
density loss, while type 2 showed largely overlapping results with type
1, and the largest effects were found in fronto-temporal circuits, par-
ietal cortex and cerebellum. Type 3 only showed small reductions in
frontal, cingulate, and temporal regions despite their similar DSM di-
agnoses (Ivleva et al., 2016). Our findings show similar brain circuits as
type 2, and in addition we find this pattern potentially connected with
apathy symptoms in a BD sample.

Excitement, mania or aggressive are the typical positive symptoms
expected in BD patients with potential behavioral effects (Dell'osso
et al., 2009). These positive profiles did not emerge through PANSS in
this analysis. However, this result does not weaken the importance of
such positive symptoms; it reflects that these symptoms might not show
the strongest relationships with brain structure components as seen for
negative mood or apathy. Similarly, we did not find any medication or
DOI effects on PANSS or brain structures in the highlighted sMRI
components. Previous studies exhibited commonly prescribed medica-
tions positively affecting brain structure through various pathways
(Dell'Osso et al., 2016; Di Sero et al., 2019; Hartberg et al., 2015;
Jorgensen et al., 2016), and large scale studies found medication effects
on both cortical and subcortical regions (Hibar et al., 2018; Hibar et al.,
2016). The situation was similar for DOI though the strongest effect was
found in cortical thickness (Hibar et al., 2018). The pICA method
prioritized the correlation of the PANSS and sMRI during the data re-
duction process of both modalities, so the components do not ne-
cessarily reflect brain regions most significantly affected by medication
or DOI.

These findings have some limitations. This study employed parti-
cipants with the diagnosis of bipolar spectrum disorders including bi-
polar I and II, and around half of patients experienced at least one
lifetime psychotic episode. We made the effort to enhance the stability
of the results. 10-fold validations were applied to pICA to avoid results

6

W. Jiang, et al.

NeuroImage: Clinical 26 (2020) 101989

being driven by outliners, and pICA itself was running with ICASSO to
ensure stability. A final
limitation is that by introducing 10 mm
smoothing kernel (Gupta et al., 2015; Segall et al., 2009; Silver et al.,
2011), and using a relatively strict Z score, and cluster size to filter the
structural brain, the main findings were restricted to the cortical re-
gions.

In summary, our finding suggested BD patients showed negative
mood symptom and apathy profile differing from the original PANSS
subscales. Importantly, localized temporal deficits and fronto-parietal
circuits were found associated with these profiles.

Author contributions

J.T. and W.J. contributed to idea generation, experiment design and
writing; W.J. conducted the analyses and wrote the manuscript. The
remaining authors contributed to the participant recruitment and data
collection and ideas. All authors critically reviewed the content and
approved the final version for publication.

Acknowledgments

This study was supported by the National Institutes of Health grant
R01-MH094524-01A1 to Turner & Calhoun. The TOP study was sup-
ported by the Research Council of Norway (#160181, 190311, 223273,
213837, 249711), the South-East Norway Health Authority (2014114,
2014097, 2017-112), and the Kristian Gerhard Jebsen Stiftelsen (SKGJ-
MED- 008) and the European Community's Seventh Framework
Programme
602450
(IMAGEMEND).

(FP7/2007–2013),

agreement

grant

no.

Appendix A. Supplementary data

Supplementary data to this article can be found online at https://

doi.org/10.1016/j.nicl.2019.101989.

References

Abe, C., Ekman, C.J., Sellgren, C., Petrovic, P., Ingvar, M., Landen, M., 2015. Manic

episodes are related to changes in frontal cortex: a longitudinal neuroimaging study
of bipolar disorder 1. Brain 138 (Pt 11), 3440–3448. https://doi.org/10.1093/brain/
awv266.

Abe, C., Ekman, C.J., Sellgren, C., Petrovic, P., Ingvar, M., Landen, M., 2016. Cortical

thickness, volume and surface area in patients with bipolar disorder types I and II. J.
Psychiatry Neurosci. 41 (4), 240–250.

Bell, M.D., Lysaker, P.H., Beam-Goulet, J.L., Milstein, R.M., Lindenmayer, J.P., 1994.
Five-component model of schizophrenia: assessing the factorial invariance of the
positive and negative syndrome scale. Psychiatry Res. 52 (3), 295–303.

Busatto, G.F., 2013. Structural and functional neuroimaging studies in major depressive
disorder with psychotic features: a critical review. Schizophr. Bull. 39 (4), 776–786.
https://doi.org/10.1093/schbul/sbt054.

Calhoun, V.D., Liu, J., Adali, T., 2009. A review of group ICA for fMRI data and ICA for

joint inference of imaging, genetic, and ERP data. NeuroImage 45 (1 Suppl),
S163–S172. https://doi.org/10.1016/j.neuroimage.2008.10.057.

Cavelti, M., Kircher, T., Nagels, A., Strik, W., Homan, P., 2018. Is formal thought disorder
in schizophrenia related to structural and functional aberrations in the language
network? A systematic review of neuroimaging findings. Schizophr. Res. 199, 2–16.
https://doi.org/10.1016/j.schres.2018.02.051.

Chen, J., Calhoun, V.D., Pearlson, G.D., Perrone-Bizzozero, N., Sui, J., Turner, J.A., ... Liu,
J., 2013. Guided exploration of genomic risk for gray matter abnormalities in schi-
zophrenia using parallel independent component analysis with reference.
Neuroimage 83, 384–396. https://doi.org/10.1016/j.neuroimage.2013.05.073.
Clementz, B.A., Sweeney, J.A., Hamm, J.P., Ivleva, E.I., Ethridge, L.E., Pearlson, G.D., ...
Tamminga, C.A., 2016. Identification of distinct psychosis biotypes using brain-based
biomarkers. Am. J. Psychiatry 173 (4), 373–384. https://doi.org/10.1176/appi.ajp.
2015.14091200.

Dell'osso, L., Carmassi, C., Rucci, P., Ciapparelli, A., Paggini, R., Ramacciotti, C.E., ...
Marazziti, D., 2009. Lifetime subthreshold mania is related to suicidality in post-
traumatic stress disorder. CNS Spectr. 14 (5), 262–266.

Dell'Osso, L., Del Grande, C., Gesi, C., Carmassi, C., Musetti, L., 2016. A new look at an old

drug: neuroprotective effects and therapeutic potentials of lithium salts.
Neuropsychiatr. Dis. Treat. 12, 1687–1703. https://doi.org/10.2147/NDT.S106479.
Di Sero, A., Jorgensen, K.N., Nerland, S., Melle, I., Andreassen, O.A., Jovicich, J., Agartz,

I., 2019. Antipsychotic treatment and basal ganglia volumes: exploring the role of
receptor occupancy, dosage and remission status. Schizophr. Res. 208, 114–123.

7

https://doi.org/10.1016/j.schres.2019.04.002.

Doan, N.T., Kaufmann, T., Bettella, F., Jorgensen, K.N., Brandt, C.L., Moberget, T., ...
Westlye, L.T., 2017. Distinct multivariate brain morphological patterns and their
added predictive value with cognitive and polygenic risk scores in mental disorders.
Neuroimage Clin. 15, 719–731. https://doi.org/10.1016/j.nicl.2017.06.014.

Dunner, D.L., 2003. Clinical consequences of under-recognized bipolar spectrum disorder.

Bipolar Disord. 5 (6), 456–463.

Dusi, N., De Carlo, V., Delvecchio, G., Bellani, M., Soares, J.C., Brambilla, P., 2019. MRI
features of clinical outcome in bipolar disorder: a selected review: special section on
"Translational and Neuroscience Studies in Affective Disorders". Section Editor, Maria
Nobile MD, PhD. This section of JAD focuses on the relevance of translational and
neuroscience studies in providing a better understanding of the neural basis of af-
fective disorders. The main aim is to briefly summaries relevant research findings in
clinical neuroscience with particular regards to specific innovative topics in mood
and anxiety disorders. J. Affect. Disord. 243, 559–563. https://doi.org/10.1016/j.
jad.2018.05.066.

Elvsashagen, T., Westlye, L.T., Boen, E., Hol, P.K., Andreassen, O.A., Boye, B., Malt, U.F.,
2013. Bipolar II disorder is associated with thinning of prefrontal and temporal
cortices involved in affect regulation. Bipolar Disord. 15 (8), 855–864. https://doi.
org/10.1111/bdi.12117.

Faerden, A., Nesvag, R., Barrett, E.A., Agartz, I., Finset, A., Friis, S., ... Melle, I., 2008.
Assessing apathy: the use of the Apathy Evaluation Scale in first episode psychosis.
Eur. Psychiatry 23 (1), 33–39. https://doi.org/10.1016/j.eurpsy.2007.09.002.

Faerden, A., Friis, S., Agartz, I., Barrett, E.A., Nesvag, R., Finset, A., Melle, I., 2009.
Apathy and functioning in first-episode psychosis. Psychiatr. Serv. 60 (11),
1495–1503. https://doi.org/10.1176/appi.ps.60.11.1495.

Fears, S.C., Schur, R., Sjouwerman, R., Service, S.K., Araya, C., Araya, X., ... Bearden, C.E.,
2015. Brain structure-function associations in multi-generational families genetically
enriched for bipolar disorder. Brain 138 (Pt 7), 2087–2102. https://doi.org/10.1093/
brain/awv106.

Garety, P.A., Freeman, D., 2013. The past and future of delusions research: from the

inexplicable to the treatable. Br. J. Psychiatry 203 (5), 327–333. https://doi.org/10.
1192/bjp.bp.113.126953.

Grande, I., Berk, M., Birmaher, B., Vieta, E., 2016. Bipolar disorder. Lancet 387 (10027),

1561–1572. https://doi.org/10.1016/S0140-6736(15)00241-X.

Gupta, C.N., Calhoun, V.D., Rachakonda, S., Chen, J., Patel, V., Liu, J., ... Turner, J.A.,
2015. Patterns of gray matter abnormalities in schizophrenia based on an interna-
tional mega-analysis. Schizophr. Bull. 41 (5), 1133–1142. https://doi.org/10.1093/
schbul/sbu177.

Gutierrez-Galve, L., Bruno, S., Wheeler-Kingshott, C.A., Summers, M., Cipolotti, L., Ron,

M.A., 2012. IQ and the fronto-temporal cortex in bipolar disorder. J. Int.
Neuropsychol. Soc. 18 (2), 370–374. https://doi.org/10.1017/S1355617711001706.
Han, K.M., De Berardis, D., Fornaro, M., Kim, Y.K., 2019. Differentiating between bipolar
and unipolar depression in functional and structural MRI studies. Prog. Neuro-
Psychopharmacol. Biol. Psychiatry 91, 20–27. https://doi.org/10.1016/j.pnpbp.
2018.03.022.

Hanford, L.C., Nazarov, A., Hall, G.B., Sassi, R.B., 2016. Cortical thickness in bipolar

disorder: a systematic review. Bipolar Disord. 18 (1), 4–18. https://doi.org/10.1111/
bdi.12362.

Hansen, C.F., Torgalsboen, A.K., Melle, I., Bell, M.D., 2009. Passive/apathetic social

withdrawal and active social avoidance in schizophrenia: difference in underlying
psychological processes. J. Nerv. Ment. Dis. 197 (4), 274–277. https://doi.org/10.
1097/NMD.0b013e31819dbd36.

Hartberg, C.B., Sundet, K., Rimol, L.M., Haukvik, U.K., Lange, E.H., Nesvag, R., ... Agartz,
I., 2011. Brain cortical thickness and surface area correlates of neurocognitive per-
formance in patients with schizophrenia, bipolar disorder, and healthy adults. J. Int.
Neuropsychol. Soc. 17 (6), 1080–1093. https://doi.org/10.1017/
S1355617711001081.

Hartberg, C.B., Jorgensen, K.N., Haukvik, U.K., Westlye, L.T., Melle, I., Andreassen, O.A.,
Agartz, I., 2015. Lithium treatment and hippocampal subfields and amygdala vo-
lumes in bipolar disorder. Bipolar Disord. 17 (5), 496–506. https://doi.org/10.1111/
bdi.12295.

Hibar, D.P., Westlye, L.T., van Erp, T.G., Rasmussen, J., Leonardo, C.D., Faskowitz, J., ...
Andreassen, O.A., 2016. Subcortical volumetric abnormalities in bipolar disorder.
Mol. Psychiatry 21 (12), 1710–1716. https://doi.org/10.1038/mp.2015.227.
Hibar, D.P., Westlye, L.T., Doan, N.T., Jahanshad, N., Cheung, J.W., Ching, C.R.K., ...

Andreassen, O.A., 2018. Cortical abnormalities in bipolar disorder: an MRI analysis of
6503 individuals from the ENIGMA bipolar disorder working group. Mol. Psychiatry
23 (4), 932–942. https://doi.org/10.1038/mp.2017.73.

Himberg, J., Hyvarinen, A., Esposito, F., 2004. Validating the independent components of
neuroimaging time series via clustering and visualization. Neuroimage 22 (3),
1214–1222. https://doi.org/10.1016/j.neuroimage.2004.03.027.

Hozer, F., Houenou, J., 2016. Can neuroimaging disentangle bipolar disorder? J. Affect.

Disord. 195, 199–214. https://doi.org/10.1016/j.jad.2016.01.039.

Ivleva, E.I., Clementz, B.A., Dutcher, A.M., Arnold, S.J., Jeon-Slaughter, H., Aslan, S., ...
Tamminga, C.A., 2016. Brain structure biomarkers in the psychosis biotypes: findings
from the bipolar-schizophrenia network for intermediate phenotypes. Biol.
Psychiatry. https://doi.org/10.1016/j.biopsych.2016.08.030.

Jang, S.K., Choi, H.I., Park, S., Jaekal, E., Lee, G.Y., Cho, Y.I., Choi, K.H., 2016. A two-
factor model better explains heterogeneity in negative symptoms: evidence from the
positive and negative syndrome scale. Front. Psychol. 7, 707. https://doi.org/10.
3389/fpsyg.2016.00707.

Jorgensen, K.N., Nesvag, R., Gunleiksrud, S., Raballo, A., Jonsson, E.G., Agartz, I., 2016.
First- and second-generation antipsychotic drug treatment and subcortical brain
morphology in schizophrenia. Eur. Arch. Psychiatry Clin. Neurosci. 266 (5), 451–460.
https://doi.org/10.1007/s00406-015-0650-9.

W. Jiang, et al.

NeuroImage: Clinical 26 (2020) 101989

Kay, S.R., Fiszbein, A., Opler, L.A., 1987. The positive and negative syndrome scale

fgene.2015.00276.

(PANSS) for schizophrenia. Schizophr. Bull. 13 (2), 261–276.

Kieseppa, T., Mantyla, R., Tuulio-Henriksson, A., Luoma, K., Mantere, O., Ketokivi, M., ...
Isometsa, E., 2014. White matter hyperintensities and cognitive performance in adult
patients with bipolar I, bipolar II, and major depressive disorders. Eur. Psychiatry 29
(4), 226–232. https://doi.org/10.1016/j.eurpsy.2013.08.002.

Killgore, W.D., Rosso, I.M., Gruber, S.A., Yurgelun-Todd, D.A., 2009. Amygdala volume
and verbal memory performance in schizophrenia and bipolar disorder. Cogn. Behav.
Neurol. 22 (1), 28–37. https://doi.org/10.1097/WNN.0b013e318192cc67.
Koutsouleris, N., Gaser, C., Jager, M., Bottlender, R., Frodl, T., Holzinger, S., ...

Meisenzahl, E.M., 2008. Structural correlates of psychopathological symptom di-
mensions in schizophrenia: a voxel-based morphometric study. NeuroImage 39 (4),
1600–1612. https://doi.org/10.1016/j.neuroimage.2007.10.029.

Lan, M.J., Chhetry, B.T., Oquendo, M.A., Sublette, M.E., Sullivan, G., Mann, J.J., Parsey,
R.V., 2014. Cortical thickness differences between bipolar depression and major
depressive disorder. Bipolar Disord. 16 (4), 378–388. https://doi.org/10.1111/bdi.
12175.

Lawrie, S.M., O'Donovan, M.C., Saks, E., Burns, T., Lieberman, J.A., 2016. Towards di-
agnostic markers for the psychoses. Lancet Psychiatry 3 (4), 375–385. https://doi.
org/10.1016/S2215-0366(16)00021-3.

Lebow, M.A., Chen, A., 2016. Overshadowed by the amygdala: the bed nucleus of the stria
terminalis emerges as key to psychiatric disorders. Mol. Psychiatry 21 (4), 450–463.
https://doi.org/10.1038/mp.2016.1.

Liu, J., Calhoun, V.D., 2014. A review of multivariate analyses in imaging genetics. Front.

Neuroinform. 8, 29. https://doi.org/10.3389/fninf.2014.00029.

Liu, J., Pearlson, G., Windemuth, A., Ruano, G., Perrone-Bizzozero, N.I., Calhoun, V.,
2009. Combining fMRI and SNP data to investigate connections between brain
function and genetics using parallel ICA. Hum. Brain Mapp. 30 (1), 241–255. https://
doi.org/10.1002/hbm.20508.

Maller, J.J., Thaveenthiran, P., Thomson, R.H., McQueen, S., Fitzgerald, P.B., 2014.

Volumetric, cortical thickness and white matter integrity alterations in bipolar dis-
order type I and II. J. Affect. Disord. 169, 118–127. https://doi.org/10.1016/j.jad.
2014.08.016.

Marin, R.S., Biedrzycki, R.C., Firinciogullari, S., 1991. Reliability and validity of the

apathy evaluation scale. Psychiatry Res. 38 (2), 143–162.

Meda, S.A., Narayanan, B., Liu, J., Perrone-Bizzozero, N.I., Stevens, M.C., Calhoun, V.D.,
... Pearlson, G.D., 2012. A large scale multivariate parallel ICA method reveals novel
imaging-genetic relationships for Alzheimer's disease in the ADNI cohort.
NeuroImage 60 (3), 1608–1621. https://doi.org/10.1016/j.neuroimage.2011.12.
076.

Pompili, M., Rihmer, Z., Akiskal, H., Amore, M., Gonda, X., Innamorati, M., ... Girardi, P.,
2012. Temperaments mediate suicide risk and psychopathology among patients with
bipolar disorders. Compr. Psychiatry 53 (3), 280–285. https://doi.org/10.1016/j.
comppsych.2011.04.004.

Ramirez, F., Moscarello, J.M., LeDoux, J.E., Sears, R.M., 2015. Active avoidance requires
a serial basal amygdala to nucleus accumbens shell circuit. J. Neurosci. 35 (8),
3470–3477. https://doi.org/10.1523/JNEUROSCI.1331-14.2015.

Ratnanather, J.T., Cebron, S., Ceyhan, E., Postell, E., Pisano, D.V., Poynton, C.B., ... Barta,
P.E., 2014. Morphometric differences in planum temporale in schizophrenia and
bipolar disorder revealed by statistical analysis of labeled cortical depth maps. Front.
Psychiatry 5, 94. https://doi.org/10.3389/fpsyt.2014.00094.

Redlich, R., Dohm, K., Grotegerd, D., Opel, N., Zwitserlood, P., Heindel, W., ...

Dannlowski, U., 2015. Reward processing in unipolar and bipolar depression: a
functional MRI study. Neuropsychopharmacology 40 (11), 2623–2631. https://doi.
org/10.1038/npp.2015.110.

Rihmer, Z., Akiskal, K.K., Rihmer, A., Akiskal, H.S., 2010. Current research on affective
temperaments. Curr. Opin. Psychiatry 23 (1), 12–18. https://doi.org/10.1097/YCO.
0b013e32833299d4.

Rimol, L.M., Hartberg, C.B., Nesvag, R., Fennema-Notestine, C., Hagler Jr., D.J., Pung,

C.J., ... Agartz, I., 2010. Cortical thickness and subcortical volumes in schizophrenia
and bipolar disorder. Biol. Psychiatry 68 (1), 41–50. https://doi.org/10.1016/j.
biopsych.2010.03.036.

Rimol, L.M., Nesvag, R., Hagler Jr., D.J., Bergmann, O., Fennema-Notestine, C., Hartberg,
C.B., ... Dale, A.M., 2012. Cortical volume, surface area, and thickness in schizo-
phrenia and bipolar disorder. Biol. Psychiatry 71 (6), 552–560. https://doi.org/10.
1016/j.biopsych.2011.11.026.

Ringen, P.A., Lagerberg, T.V., Birkenaes, A.B., Engn, J., Faerden, A., Jonsdottir, H., ...
Andreassen, O.A., 2008. Differences in prevalence and patterns of substance use in
schizophrenia and bipolar disorder. Psychol. Med. 38 (9), 1241–1249. https://doi.
org/10.1017/S003329170700236X.

Rissanen, J., 1978. Modeling by shortest data description. Automatica 14, 465–471.
Segall, J.M., Turner, J.A., van Erp, T.G., White, T., Bockholt, H.J., Gollub, R.L., ...

Calhoun, V.D., 2009. Voxel-based morphometric multisite collaborative study on
schizophrenia. Schizophr. Bull. 35 (1), 82–95. https://doi.org/10.1093/schbul/
sbn150.

Selvaraj, S., Arnone, D., Job, D., Stanfield, A., Farrow, T.F., Nugent, A.C., ... McIntosh,
A.M., 2012. Grey matter differences in bipolar disorder: a meta-analysis of voxel-
based morphometry studies. Bipolar Disord. 14 (2), 135–145. https://doi.org/10.
1111/j.1399-5618.2012.01000.x.

Meda, S.A., Wang, Z., Ivleva, E.I., Poudyal, G., Keshavan, M.S., Tamminga, C.A., ...

Shahab, S., Mulsant, B.H., Levesque, M.L., Calarco, N., Nazeri, A., Wheeler, A.L., ...

Pearlson, G.D., 2015. Frequency-specific neural signatures of spontaneous low-fre-
quency resting state fluctuations in psychosis: evidence from bipolar-schizophrenia
network on intermediate phenotypes (B-SNIP) consortium. Schizophr. Bull. 41 (6),
1336–1348. https://doi.org/10.1093/schbul/sbv064.

Mennigen, E., Jiang, W., Calhoun, V.D., van Erp, T.G.M., Agartz, I., Ford, J.M., ... Turner,
J.A., 2019. Positive and general psychopathology associated with specific gray matter
reductions in inferior temporal regions in patients with schizophrenia. Schizophr.
Res. https://doi.org/10.1016/j.schres.2019.02.010.

Merikangas, K.R., Jin, R., He, J.P., Kessler, R.C., Lee, S., Sampson, N.A., ... Zarkov, Z.,
2011. Prevalence and correlates of bipolar spectrum disorder in the world mental
health survey initiative. Arch. Gen. Psychiatry 68 (3), 241–251. https://doi.org/10.
1001/archgenpsychiatry.2011.12.

Mitchell, R.L., Elliott, R., Barry, M., Cruttenden, A., Woodruff, P.W., 2004. Neural re-

sponse to emotional prosody in schizophrenia and in bipolar affective disorder. Br. J.
Psychiatry 184, 223–230.

Morch-Johnsen, L., Nesvag, R., Faerden, A., Haukvik, U.K., Jorgensen, K.N., Lange, E.H.,
... Agartz, I., 2015. Brain structure abnormalities in first-episode psychosis patients
with persistent apathy. Schizophr. Res. 164 (1–3), 59–64. https://doi.org/10.1016/j.
schres.2015.03.001.

Morch-Johnsen, L., Nesvag, R., Jorgensen, K.N., Lange, E.H., Hartberg, C.B., Haukvik,
U.K., ... Agartz, I., 2017. Auditory cortex characteristics in schizophrenia: associa-
tions with auditory hallucinations. Schizophr. Bull. 43 (1), 75–83. https://doi.org/
10.1093/schbul/sbw130.

Morch-Johnsen, L., Nerland, S., Jorgensen, K.N., Osnes, K., Hartberg, C.B., Andreassen,
O.A., ... Agartz, I., 2018. Cortical thickness abnormalities in bipolar disorder patients
with a lifetime history of auditory hallucinations. Bipolar Disord. 20 (7), 647–657.
https://doi.org/10.1111/bdi.12627.

Nunes, A., Schnack, H.G., Ching, C.R.K., Agartz, I., Akudjedu, T.N., Alda, M., ... Group,
E.B.D.W., 2018. Using structural MRI to identify bipolar disorders - 13 site machine
learning study in 3020 individuals from the ENIGMA Bipolar Disorders Working
Group. Mol. Psychiatry. https://doi.org/10.1038/s41380-018-0228-9.

Nusslock, R., Alloy, L.B., 2017. Reward processing and mood-related symptoms: an RDoC
and translational neuroscience perspective. J. Affect. Disord. 216, 3–16. https://doi.
org/10.1016/j.jad.2017.02.001.

Padmanabhan, J.L., Tandon, N., Haller, C.S., Mathew, I.T., Eack, S.M., Clementz, B.A., ...
Keshavan, M.S., 2015. Correlations between brain structure and symptom dimensions
of psychosis in schizophrenia, schizoaffective, and psychotic bipolar I disorders.
Schizophr. Bull. 41 (1), 154–162. https://doi.org/10.1093/schbul/sbu075.

Palaniyappan, L., Cousins, D.A., 2010. Brain networks: foundations and futures in bipolar

disorder. J. Ment. Health 19 (2), 157–167. https://doi.org/10.3109/
09638230903469129.

Pearlson, G.D., Liu, J., Calhoun, V.D., 2015. An introductory review of parallel in-

dependent component analysis (p-ICA) and a guide to applying p-ICA to genetic data
and imaging phenotypes to identify disease-associated biological pathways and sys-
tems in common complex disorders. Front. Genet. 6, 276. https://doi.org/10.3389/

Voineskos, A.N., 2018. Brain structure, cognition, and brain age in schizophrenia,
bipolar disorder, and healthy controls. Neuropsychopharmacology. https://doi.org/
10.1038/s41386-018-0298-z.

Sharma, A., Wolf, D.H., Ciric, R., Kable, J.W., Moore, T.M., Vandekar, S.N., ...

Satterthwaite, T.D., 2017. Common dimensional reward deficits across mood and
psychotic disorders: a connectome-wide association study. Am. J. Psychiatry 174 (7),
657–666. https://doi.org/10.1176/appi.ajp.2016.16070774.

Shepherd, A.M., Quide, Y., Laurens, K.R., O'Reilly, N., Rowland, J.E., Mitchell, P.B., ...
Green, M.J., 2015. Shared intermediate phenotypes for schizophrenia and bipolar
disorder: neuroanatomical features of subtypes distinguished by executive dysfunc-
tion. J. Psychiatry Neurosci. 40 (1), 58–68.

Silver, M., Montana, G., Nichols, T.E., Alzheimer's Disease Neuroimaging, I, 2011. False

positives in neuroimaging genetics using voxel-based morphometry data.
NeuroImage 54 (2), 992–1000. https://doi.org/10.1016/j.neuroimage.2010.08.049.
Strauss, G.P., Esfahlani, F.Z., Kirkpatrick, B., Allen, D.N., Gold, J.M., Visser, K.F., Sayama,
H., 2019. Network analysis reveals which negative symptom domains are most
central in schizophrenia vs bipolar disorder. Schizophr. Bull. https://doi.org/10.
1093/schbul/sby168.

Strik, W., Stegmayer, K., Walther, S., Dierks, T., 2017. Systems neuroscience of psychosis:

mapping schizophrenia symptoms onto brain systems. Neuropsychobiology 75 (3),
100–116. https://doi.org/10.1159/000485221.

van der Gaag, M., Cuijpers, A., Hoffman, T., Remijsen, M., Hijman, R., de Haan, L., ...
Wiersma, D., 2006. The five-factor model of the Positive and Negative Syndrome
Scale I: confirmatory factor analysis fails to confirm 25 published five-factor solu-
tions. Schizophr. Res. 85 (1–3), 273–279. https://doi.org/10.1016/j.schres.2006.04.
001.

van Erp, T.G.M., Walton, E., Hibar, D.P., Schmaal, L., Jiang, W., Glahn, D.C., ... Turner,
J.A., 2018. Cortical brain abnormalities in 4474 individuals with schizophrenia and
5098 control subjects via the enhancing neuro imaging genetics through meta ana-
lysis (ENIGMA) consortium. Biol. Psychiatry 84 (9), 644–654. https://doi.org/10.
1016/j.biopsych.2018.04.023.

Walton, E., Hibar, D.P., van Erp, T.G., Potkin, S.G., Roiz-Santianez, R., Crespo-Facorro, B.,
... Ehrlich, S., 2017. Positive symptoms associate with cortical thinning in the su-
perior temporal gyrus via the ENIGMA schizophrenia consortium. Acta Psychiatr.
Scand. 135 (5), 439–447. https://doi.org/10.1111/acps.12718.

Walton, E., Hibar, D.P., van Erp, T.G.M., Potkin, S.G., Roiz-Santianez, R., Crespo-Facorro,

B., ... Ehrlich, S., 2018. Prefrontal cortical thinning links to negative symptoms in
schizophrenia via the ENIGMA consortium. Psychol. Med. 48 (1), 82–94. https://doi.
org/10.1017/S0033291717001283.

Wang, D., Li, M., Wang, M., Schoeppe, F., Ren, J., Chen, H., ... Liu, H., 2018. Individual-
specific functional connectivity markers track dimensional and categorical features of
psychotic illness. Mol. Psychiatry. https://doi.org/10.1038/s41380-018-0276-1.
Whalley, H.C., McKirdy, J., Romaniuk, L., Sussmann, J., Johnstone, E.C., Wan, H.I., ...

Hall, J., 2009. Functional imaging of emotional memory in bipolar disorder and
schizophrenia. Bipolar Disord. 11 (8), 840–856. https://doi.org/10.1111/j.1399-

8

W. Jiang, et al.

5618.2009.00768.x.

Whalley, H.C., Papmeyer, M., Sprooten, E., Lawrie, S.M., Sussmann, J.E., McIntosh, A.M.,
2012. Review of functional magnetic resonance imaging studies comparing bipolar
disorder and schizophrenia. Bipolar Disord. 14 (4), 411–431. https://doi.org/10.
1111/j.1399-5618.2012.01016.x.

White, L., Harvey, P.D., Opler, L., Lindenmayer, J.P., 1997. Empirical assessment of the
factorial structure of clinical symptoms in schizophrenia. A multisite, multimodel
evaluation of the factorial structure of the Positive and Negative Syndrome Scale. The
PANSS Study Group. Psychopathology 30 (5), 263–274. https://doi.org/10.1159/
000285058.

Wise, T., Radua, J., Via, E., Cardoner, N., Abe, O., Adams, T.M., ... Arnone, D., 2017.

NeuroImage: Clinical 26 (2020) 101989

Common and distinct patterns of grey-matter volume alteration in major depression
and bipolar disorder: evidence from voxel-based meta-analysis. Mol. Psychiatry 22
(10), 1455–1463. https://doi.org/10.1038/mp.2016.72.

Wolfers, T., Doan, N.T., Kaufmann, T., Alnaes, D., Moberget, T., Agartz, I., ... Marquand,
A.F., 2018. Mapping the heterogeneous phenotype of schizophrenia and bipolar
disorder using normative models. JAMA Psychiatry 75 (11), 1146–1155. https://doi.
org/10.1001/jamapsychiatry.2018.2467.

Xu, L., Groth, K.M., Pearlson, G., Schretlen, D.J., Calhoun, V.D., 2009. Source-based

morphometry: the use of independent component analysis to identify gray matter
differences with application to schizophrenia. Hum. Brain Mapp. 30 (3), 711–724.
https://doi.org/10.1002/hbm.20540.

9
