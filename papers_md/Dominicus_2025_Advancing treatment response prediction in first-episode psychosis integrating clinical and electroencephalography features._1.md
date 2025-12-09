# Dominicus_2025_Advancing treatment response prediction in first-episode psychosis integrating clinical and electroencephalography features._1

PCNPsychiatry and

Clinical Neurosciences

REGULAR ARTICLE

Advancing treatment response prediction in ﬁrst-episode
psychosis: integrating clinical and
electroencephalography features

Livia Dominicus, MD ,1* Melissa Zandstra, Msc,1 Josephine Franse, Msc,1 Wim Otte, PhD,2
Arjan Hillebrand, PhD ,3,4,5 Simone de Graaf, Msc,1 Karen Ambrosen, PhD,6 Birte Yding Glenthøj, MD, PhD,6,7
Andrew Zalesky, PhD,8,9 Kirsten Borup Bojesen, MD, PhD ,6 Mikkel Sørensen, Msc,6 Floortje Scheepers, MD, PhD,1
Cornelis Stam, MD, PhD,5 Bob Oranje, PhD,6,7 Bjorn Ebdrup, MD, PhD6,7 and Edwin van Dellen, MD, PhD1,10

Aims: Prompt diagnosis and intervention are crucial for ﬁrst-
episode psychosis (FEP) outcomes, but predicting the
response to antipsychotics remains challenging. We studied
whether adding electroencephalography (EEG) characteristics
improves clinical prediction models for treatment response
and whether EEG-based predictors are inﬂuenced by initial
treatment.

Methods: We included 115 antipsychotic-naïve patients
with FEP. Positive and Negative Syndrome Scale (PANSS)
and sociodemographic items were included as clinical
features. Additionally, we analyzed resting-state EEG data
(n = 45) for (relative) power, functional connectivity, and net-
work organization. Treatment
response, measured as
change in PANSS positive subscale scores (ΔPANSS+),
was predicted using a random forest regression model. We
analyzed whether the most predictive EEG characteristics
were inﬂuenced after treatment.

Results: The clinical model explained 12% variance in
symptom reduction in the training set and 32% in the

validation set. Including EEG variables in the model led to a
nonsigniﬁcant increase of 2% (total 34%) explained variance
in symptom reduction. High hallucination symptom scores
and a more hierarchical organization of alpha band networks
(tree hierarchy) were associated with ΔPANSS+ reduction.
The tree hierarchy in the alpha band decreased after medi-
cation. EEG source analysis revealed that this change was
driven by alterations in the degree and centrality of frontal
and parietal nodes in the functional brain network.

Conclusions: Both clinical and EEG characteristics can
inform treatment response prediction in patients with FEP,
but the combined model may not be beneﬁcial over a clinical
model. Nevertheless, adding a more objective marker such
as EEG could be valuable in selected cases.

Keywords: electroencephalography, ﬁrst-episode psychosis, machine
learning, prediction, treatment response.

http://onlinelibrary.wiley.com/doi/10.1111/pcn.13791/full

Psychosis is characterized by clinical symptoms of delusions, halluci-
nations, and disorganized thinking and speech.1 Prompt diagnosis and
effective treatment of ﬁrst-episode psychosis (FEP) are critical for
good outcomes, and reducing the duration between the onset of FEP
and successful intervention can improve the prognosis of affected
patients.2,3 If treatment response to antipsychotics (APs) could be
predicted, this information could facilitate effective treatment selec-
tion. In practice, treatment efﬁcacy only becomes clear after several

weeks of treatment. Consequently, treatment guidelines for FEP are
based on a trial-and-error process.4,5

Clinical prediction and data-driven prediction are two approaches
studied in psychiatry to predict clinical outcomes. Clinical prediction
involves using clinical judgment and experience to make predictions,6
while data-driven prediction is based on statistical models and algo-
rithms informed by objective data.7–9 Data-driven predictions of
human behavior perform as well as, or better than, clinical prediction

1 Department of Psychiatry, University Medical Center Utrecht, Utrecht, The Netherlands
2 Department of Child Neurology, UMC Utrecht Brain Center, University Medical Center Utrecht, and Utrecht University, Utrecht, The Netherlands
3 Amsterdam Neuroscience, Brain Imaging, Amsterdam, The Netherlands
4 Amsterdam Neuroscience, Systems and Network Neurosciences, Amsterdam, The Netherlands
5 Department of Clinical Neurophysiology and MEG Center, Department of Neurology, Amsterdam Neuroscience, Vrije Universiteit Amsterdam, Amsterdam UMC,
Amsterdam, The Netherlands
6 Center for Neuropsychiatric Schizophrenia Research (CNSR) and Center for Clinical Intervention and Neuropsychiatric Schizophrenia Research (CINS), Copenhagen
University Hospital, Mental Health Center Glostrup, Glostrup, Denmark
7 Department of Clinical Medicine, Faculty of Health and Medical Sciences, University of Copenhagen, Copenhagen, Denmark
8 Melbourne Neuropsychiatry Centre, University of Melbourne, Melbourne, Victoria, Australia
9 Department of Biomedical Engineering, University of Melbourne, Melbourne, Victoria, Australia
10 Department of Neurology, UZ Brussel and Vrije Universiteit Brussel, Brussels, Belgium
* Correspondence: Email: l.s.dominicus-2@umcutrecht.nl

© 2025 The Author(s).
Psychiatry and Clinical Neurosciences published by John Wiley & Sons Australia, Ltd on behalf of Japanese Society of Psychiatry and Neurology.
This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any
medium, provided the original work is properly cited, the use is non-commercial and no modiﬁcations or adaptations are made.

187

Psychiatry and Clinical Neurosciences 79: 187–196, 2025

Treatment response prediction in FEP

methods for a wide range of circumstances,7 and clinical judgment of
psychiatrists can sometimes be incorrect.7,10 Decision support sys-
tems utilizing objective data-driven prediction may therefore
improve the predictability of treatment response to AP in FEP. Pre-
cision psychiatry research, utilizing advanced techniques such as
machine learning,
treatment response.
is seeking predictors for
Clinical assessments potentially provide the most cost-effective
predictors of
response given their minimal material
requirements. Symptom scores and sociodemographic items have
some—but not sufﬁcient—predictive value,11–14 and more sophisti-
cated predictive models are therefore needed.

treatment

Electroencephalography (EEG) is of potential added value to
models based on clinical data because it is a relatively cost-effective,
easily accessible, objective measure capable of capturing functional
brain dynamics. Moreover, EEG measures seem to characterize a sub-
group of patients with schizophrenia15 and can identify AP-naïve
patients with FEP from healthy controls in combination with other
modalities.16

Resting-state EEG (rs-EEG), a noninvasive procedure, is com-
monly used to assess the intrinsic activity of brain networks without
any manipulation by task or stimulus presentation.17,18 Several studies
have reported that treatment response to clozapine could be predicted
using EEG connectivity features with accuracies ranging from 85% to
95.8%.19–21 We previously found in AP-naïve patients with FEP that
23% of the variance of the decrease in positive symptoms after treat-
ment could be predicted based on EEG recordings22 and that rs-EEG
can aid in stratifying patients at the onset of illness into clinically
in EEG
also
meaningful
characteristics,24 but the neuroanatomical substrate or localization of
such EEG changes largely remain unstudied. Previous functional
magnetic resonance imaging studies have identiﬁed changes in func-
tional connectivity within several brain areas, particularly between the
striatum and the ventral attention network, as well as between the
default mode network and the striatum.25–28

clusters.23 APs

changes

cause

Here, we aimed to advance treatment response prediction model-
ing for AP treatment of FEP by integrating clinical and EEG-derived
characteristics. Speciﬁcally, we assessed whether a combined model,
utilizing both clinical data and EEG characteristics, offers superior
predictive capability compared with a purely clinical model. Finally,
we studied the most important EEG-based predictors of response to
see whether these characteristics changed after treatment.29

Methods
Study population
The data included in this study were collected in accordance with the
Declaration of Helsinki. All participants provided written informed
consent prior to participation, and the studies were approved by the
Danish National Committee on Biomedical Research Ethics.

The population was recruited from three cohorts with similar
patient characteristics: the PECANS (Pan European Collaboration on
Antipsychotic Naïve Schizophrenia; ClinicalTrials.gov identiﬁer:
NCT01154829),30 PECANSII (Pan European Collaboration on Anti-
II; ClinicalTrials.gov identiﬁer:
psychotic Naïve Schizophrenia
NCT02339844),31 and OPTIMISE (The optimization of treatment
and management of schizophrenia in Europe ClinicalTrials.gov identi-
ﬁer: NCT01555814) studies.4,30,31 These data sets were combined
because participants were included in the same center with matching
inclusion criteria. The patients were referred from inpatient and out-
patient clinics in the Capital Region of Denmark. Inclusion criteria in
all
three studies were being AP-naïve, and age between 18 and
45 years for the PECANS studies, and age between 18 and 40 years
in the OPTIMISE study. Further, patients should fulﬁll a diagnosis of
schizophrenia (PECANS) or schizophreniform disorder (PECANSII
and OPTIMISE). For the OPTIMISE study, the duration of psychosis
was <2 years.

All patients had experienced the initial occurrence of psychotic
symptoms or a psychotic episode and had not previously been treated

188

PCNPsychiatry and

Clinical Neurosciences

with AP medication. Therefore, all patients included in this study
were lifetime AP-naïve at baseline. Patients were treated with either
amisulpride (PECANS 1 and OPTIMISE) or aripiprazole (PECANS
II) according to clinical need balancing effect and side effects. For an
overview of inclusion and exclusion criteria of the different cohorts,
see Supplement S1 in Data S1. The data sets used for this study are
also previous described.15,16,30,31

Study design
We tested three models in our study (for an overview, see Figure 1).
Several methodological steps build upon our previous work.22 First,
we trained a clinical model (Q1a). Subsequently, we tested the perfor-
mance of this model on an unseen data set (Q1b). Patients in the test
set were selected based on the availability of EEG data. We did not
divide the data into subsets based on the different cohorts (namely
PECANS I, PECANS II, and OPTIMISE Degree (k)) because they
were treated with different AP. To address the research question
regarding the added value of EEG, we tested a model in all partici-
pants with EEG data available and incorporated both clinical and
EEG variables (Q2). Although we were unable to test this model in
an independent data set, random forest (RF) models use bootstrapping
for validation to avoid overﬁtting. Last, we tested whether EEG char-
acteristics changed after AP treatment. Anatomical source analyses of
functional network alterations were performed using a beamforming
approach32 to the 68 cortical regions of the Desikan–Killiany atlas
(Q3) (Supplement S2 in Data S1).33

Clinical characteristics
The Positive and Negative Syndrome Scale (PANSS) was used to
assess symptom severity of psychotic symptoms at baseline and
follow-up after 4 to 6 weeks to measure early response, using the
standard PANSS procedure.34 The clinical characteristics included
were individual PANSS items, age, sex (male/female), parents’ socio-
economic status, patients’ education level and the total education in
years for the patient, ICD diagnosis, Clinical Global Impression
(CGI) scores and Global Assessment of Functioning (GAF) scores
(GAF symptoms [GAF-S] and GAF functioning [GAF-F] scores [see
also Supplement S3 and TableS1 in Data S1]).

EEG recordings
Participants underwent 10 min of
rs-EEG eyes-closed recordings
using Biosemi hardware with 64 electrodes at a sampling rate of
2048 Hz, in a soundproof room between 9 AM and 12 AM. Participants
were asked not to smoke in the hour before the recording or consume
any caffeinated drinks, and they were requested not to take benzodiaz-
epines the evening before the recording from 11 PM onwards. Any
other medication use including psychoactive medication was allowed
and documented (see Table 2 for further details). All resting-state
recordings were made after an event-related potential
recording
sequence of ≈45 min, which included paradigms for prepulse inhibi-
tion of the startle reﬂex, P50 suppression, mismatch negativity, and
selective attention.35–37 The EEG data were preprocessed using
BrainWave software version 0.9.152.12.26 (developed by C. J. Stam)
and EEG Utils in Rstudio.38 Eye movement or muscle artifacts were
identiﬁed by trained raters. Interpolation, by spherical spline was used
for artifact-ridden electrodes, and recordings exceeding a threshold of
six problematic channels were discarded.39 The ﬁrst 15 artifact-free
4-s epochs were selected, resulting in 60 s of artifact-free data. To
optimize data preprocessing and analyses, the EEG data were down-
sampled to 1024 Hz and an average reference was applied. Data were
band-pass ﬁltered into four frequency bands: delta (0.5–4 Hz), theta
(4–8 Hz), alpha (8–13 Hz), and beta (13–20 Hz), using the Fast Fou-
rier Transformation. We discarded frequencies >20 Hz, as muscle
activity interferes with neuronal
frequencies above
20 Hz.40,41 EEG follow-up data were recorded at ≈6 weeks after initi-
ation of AP treatment.

responses at

Psychiatry and Clinical Neurosciences 79: 187–196, 2025

PCNPsychiatry and

Clinical Neurosciences

Treatment response prediction in FEP

Clinical model
N = 70

Random forest
regression

Q1a

Best
performing
features

Q1b

Clinical model
validation
N = 45

Clinical and EEG
model
N = 45

Q2

Random forest
regression

Best
performing
features

Change of EEG
characteristics
over time
N = 21

Q3

Group
comparison

Correlation
ΔEEG - ΔPANSS

Source
analyses

Permutation
tests

Fig. 1 Overview of the analyses. Provides a schematic of the various analyses conducted in our research. Initially, we employed a random forest (RF) regression model
focusing on clinical traits (Q1) and later validated this using a separate data set (Q1b). Subsequently, an RF model was used that incorporated both electroencephalog-
raphy (EEG) and clinical data (Q2). We further explored the prominent EEG features from Q2 to determine whether they exhibited alterations after 6 weeks of antipsy-
chotics and whether these shifts correlated with changes in baseline-corrected positive and negative syndrome scale (PANSS) scores (Q3). Our ﬁnal analysis involved
a source-level analysis combined with permutation tests to ascertain how these EEG features evolved over time in distinct brain areas.

EEG characteristics
EEG characteristics included relative spectral power, functional con-
nectivity, and network topology measures.

Power spectrum
Absolute power was calculated using a Fast Fourier Transforma-
tion. Relative power was determined by dividing the absolute
power per frequency band by the total power of the four frequency
bands (delta [0.5–4 Hz], theta [4–8 Hz], alpha [8–13 Hz], and beta
[13–20 Hz]).

Functional connectivity
As mentioned by Aertsen et al.42 functional connectivity (FC) refers
to the statistical interdependence of neural signals, reﬂecting how sig-
nals from different neurons or brain regions vary in relation to one
another. This concept assumes a degree of correlation between neural
activities, which can signify cooperative processing or shared input
sources among neurons. These statistical relationships are central to
all functional connectivity metrics, as they measure associations with-
out implying direct anatomical connections. The statistical depen-
dency between signals can be assessed in various ways, with phase
(PLI)43 and amplitude (amplitude envelope correlation-corrected
[AECc])44,45 emerging as logical candidates for this purpose. Both
measures account for volume conduction and ﬁeld spread in their
calculations.

Network organization
The brain is organized as a complex network of interacting neurons,
or, on a mesoscale, remote brain areas. Network organization refers to
the arrangement and interaction of nodes (such as brain regions or
neurons) and edges (connections) within a network that follows spe-
ciﬁc topological properties. These networks are studied using network
theory, which provides quantitative methods to describe their structure
and dynamics.46 A speciﬁc way to study network organization speciﬁ-
cally is by analyzing characteristics of the minimum spanning tree
(MST), a backbone structure of the full network of (functional) con-
nections between brain areas. This is explained in more detail in
Table 1.

In this study, we included MST characteristics based both on the
PLI and AEC-c47,48 (for an overview, see Table S2 in Data S1).
The MST included the degree (k), the leaf fraction (LF), the diameter
(D), the betweenness centrality (BC), the eccentricity (ECC), and the
tree hierarchy (Th). For the explanation of the different characteris-
tics, see Table 1.

In the prediction models, EEG characteristics were analyzed at
the sensor level. Regarding Q3, source analyses were performed for
the best features of Q2 (Supplement S2 in Data S1).

Statistical analyses
RF regression
We used an RF regression model to explore the predictive power of
EEG/clinical features for symptom reduction after treatment (see also
Supplement S4 in Data S1). It is well established that APs primarily

Psychiatry and Clinical Neurosciences 79: 187–196, 2025

189

Treatment response prediction in FEP

Table 1. Deﬁnitions and descriptions of EEG characteristics

PCNPsychiatry and

Clinical Neurosciences

EEG characteristics

Spectral power

Connectivity

Description

Absolute power was calculated using a Fast Fourier Transformation. Relative power was determined by dividing the absolute
power per frequency band by the total power of the four frequency bands (delta (0.5–4 Hz), theta (4–8 Hz), alpha (8–
13 Hz), and beta (13–20 Hz)

The AEC-c was obtained by estimating the magnitude of the analytic signal. Normalized values range from 0 to 1.
The PLI characterizes consistent phase differences between two signals. Ranges vary from 0 (no synchronization) to 1

(complete phase locking).43–45

Network analyses

The MST was used to reconstruct a backbone of functional connections, and is subsequently characterized with

characteristics derived from graph theory. The MST is an acyclic subnetwork of the brain connecting all nodes, while
minimizing the link weights and reﬂecting most fundamental network properties. A node refers to an electrode or brain
region, and a link/edge is a functional connection between nodes. It avoids limitations of other graph theoretical
approaches such as sensitivity to connection strengths, arbitrary thresholding, or link density effects.48 The MST was
calculated based on connectivity matrices, which here represented the frequency-speciﬁc PLI or AEC-c. The connectivity
matrices consisted of 64 (cid:3) 64 cells (for 64 EEG channels) resulting in 64 nodes with 63 edges.47,48

MST
characteristics

Deﬁnition and description

Degree (k)

Measures the number of edges/links for each node divided by the maximum number of edges possible. The maximum

Leaf fraction

The ratio of leaf nodes is divided by the total number of nodes. A leaf node (L) is a node with only one edge.

degree (kmax), which is the highest degree in the MST, was as a macroscale network characteristic.

(LF)

Diameter (D)

Refers to the largest distance between any two nodes. It can be interpreted as a measure of efﬁciency, where a low

diameter indicates an efﬁcient information ﬂow between brain regions.

BC

ECC

Th

Fraction of all shortest paths that pass through a node. A leaf node has a BC of zero. The central node in a star-like

network is characterized by BC = 1. For the MST global measure, the highest BC (BCmax) is used.

Measure of the maximum distance calculated as the number of edges between a node and any other node in the MST.

Here, we used the mean ECC of all nodes.

Deﬁnes the hierarchy of the MST organization as optimal topology. Th is calculated as Th = L/(2 M BCmax), where

L = leaf number and M = maximum leaf number.

AEC-c, amplitude envelope correlation-corrected; BC, betweenness centrality; ECC, eccentricity; EEG, electroencephalography; MST, minimum
spanning tree; PLI, Phase Lag Index; Th, tree hierarchy.

reduce positive symptoms,49 and, accordingly, our previous research
showed only signiﬁcant predictive power when assessing positive
symptoms.22 In this study, we therefore characterized AP treatment
response based on ΔPANSS for positive symptoms (ΔPANSS+),
deﬁned as:

ΔPANSSþ ¼ PANSS þ follow(cid:2)up – PANSS þ baseline

We included all PANSS items as input features for our RF
regression. We chose to develop tests for explained variance in abso-
lute symptom reduction (as opposed to a percentage change in symp-
tom severity) because APs are more effective in patients with more
severe symptoms; analyzing relative improvement would therefore
potentially mask predictive value.50 The signiﬁcance of the predictive
performance of the models was tested against a random distribution
individual ΔPANSS+ scores,
obtained by 1000 permutations of
aiming to reduce false-positive results, as RF regression is otherwise
not straightforward for interpretation. The 1000 permutations were
selected to minimize computational power while achieving sufﬁ-
ciently stable results.

Change of EEG networks over time
We examined the changes of the EEG characteristics after AP treat-
focusing on those with the highest predictive value for
ment,

treatment response in the RF model (deﬁned as relative variable
importance [VIMP] scores >90; VIMP is a relative score scaled from
1 to 100). To investigate the association between change in these
EEG characteristics and PANSS scores, we utilized a regression-
based approach to account for baseline differences. As baseline
variations can potentially confound follow-up measurements, it is
vital to adjust for them to avoid misinterpretations regarding the
inﬂuence of interventions or the progression of a condition. We
derived residuals by regressing the follow-up scores of both the
EEG characteristics and PANSS onto their respective baseline
scores. These residuals effectively represent the corrected changes
(Δscores), i.e. changes that were unaccounted for by the initial
measurements, and served as our primary variables of interest. We
assessed the relationship between these corrected Δscores of the
best EEG features and PANSS+.51

Analyses for Q2 were based on sensor-level analyses to investi-
gate which macroscale EEG characteristics are related to treatment
response, while regional EEG characteristics were analyzed in source
space for Q3. In essence, although the sensor level is more practical,
the source level gives better insight into the neurophysiological mech-
anisms. Source-level analysis was only performed for
frequency
bands, connectivity measures, and network characteristics with pre-
dictive value for outcomes (deﬁned as VIMP > 90 in Q2), as we
hypothesized changes in these speciﬁc characteristics in relation to
treatment response. We tested whether regional EEG characteristics

190

Psychiatry and Clinical Neurosciences 79: 187–196, 2025

PCNPsychiatry and

Clinical Neurosciences

of all 68 brain regions changed over time using permutation tests over
the different time points (before and after medication). We considered
this an explorative analysis and therefore report ﬁndings uncorrected
for multiple testing. Network-based statistics were used to compare
connectivity pattern changes over time where appropriate (see the
Results section and Supplement S6 in Data S1).

Sensitivity analyses
Since PANSS item scores serve as both input and output variables,
we conducted two sensitivity analyses to assess the model’s perfor-
mance. First, a permutation test was applied to analyze the signiﬁ-
cance of the relationship between the individual PANSS item scores
and ΔPANSS. Second, a noise analysis was performed to allow com-
parison of the performance of the model to its performance when

Treatment response prediction in FEP

applied to noise data. A full description of both sensitivity analyses
can be found in Supplement S5 and Figs. S1 and S2 in Data S1.

Results
Study population
A total of 115 patients were included. From those 115 patients, only
45 underwent rs-EEG. We therefore used 115 patients in total for the
clinical model, and 45 patients for the combined model. Thirty-nine
clinical variables (listed in Table S1, Supplement S3 in Data S1) were
included regarding the clinical models and an additional 60 EEG vari-
ables were included regarding the combined model as input for the
RF regression. Patient characteristics are shown in Table 2. In total,
52 patients were treated with selective dopaminergic AP aripiprazole
(partial D2 and 5-HT1A agonist and 5-HT2A antagonist) and 63 with

Table 2. Patient characteristics

Characteristic

Age (years)
Sex (% male)
Education level (%)

University or similar
Bachelor or similar/skilled worker
No education
Currently active in an education

Education of parents (%)

Highest education and income level
Middle education and income level
Lowest education and income level

Years of education (mean [SD])
GAF symptoms (mean [SD])
GAF functioning (mean [SD])
CGI severity (mean [SD])
ICD-10 diagnosis (N)

Amisulpride (mean dose [SD])
Range (minimum–maximum)
Mean equivalent olanzapine68,69
Aripiprazole (mean dose [SD])
Range (minimum–maximum)
Mean equivalent olanzapine68,69
Psychotropic comedication at baseline

PANSS positive total (mean [SD])
PANSS negative total (mean [SD])
PANSS general total (mean [SD])
PANSS total scores (mean [SD])

Results at baseline

Results at follow-up (6.6 [1.7])

23.5 (5.2)
50% (n = 57 male, n = 58 female)

0.9
8.7
21.7
53.9

24.3
56.5
17.4
12.06 (2.12)
38.73 (8.61)
44.83 (11.49)
4.35 (0.75)
Paranoid schizophrenia: 60
Hebephrenic schizophrenia: 7
Undifferentiated schizophrenia: 11
Simple schizophrenia: 2
Catatonic schizophrenia: 1
Schizophrenia, unspeciﬁed: 12
Other, N = 22†
295 (180.09) mg (N = 59)‡
100–900 mg
7.4 mg
6.43 (3.71) mg (N = 42)‡
5–25 mg
4.3 mg
Zopiclone 7.5 mg N = 3
Codeine 2.5 mg: N = 1
Sertraline 100 mg: N = 1
Disulﬁram: N = 1
Baseline: 19.2 (4.3)
Baseline: 19.8 (6.2)
Baseline: 38.3 (7.6)
Baseline: 77.2 (15.0)

NA
NA

NA
NA
NA
NA

NA
NA
NA
NA
NA
NA
NA
NA

NA

NA

NA

Follow-up: 13.9 (4.0)
Follow-up: 17.5 (5.6)
Follow-up: 30.7 (7.8)
Follow-up: 62.2 (14.4)

CGI, Clinical Global Impression; GAF, Global Assessment of Functioning; NA, not applicable; PANSS, Positive and Negative Syndrome Scale.
†Other diagnoses included (number of patients): unspeciﬁed persistent delusional disorder (two), other nonorganic psychotic disorder with
hallucinations (four), unspeciﬁed nonorganic psychosis (ﬁve), schizoaffective disorder mixed type (two), and not available (eight).
‡Some antipsychotic dosages were unknown.

Psychiatry and Clinical Neurosciences 79: 187–196, 2025

191

Treatment response prediction in FEP

PCNPsychiatry and

Clinical Neurosciences

amisulpride (D2/D3 antagonist). The average follow-up visit was after
6.6 weeks (SD = 1.7).

0.48

Tree hierarchy (Alpha band) over time for individual particpants

RF regression
Model 1 (clinical training model)
The clinical data set included 115 patients. We divided the patient
data into a test set of patients who had only undergone clinical assess-
ments and a validation set of patients who had undergone an EEG
(n = 45). In this way, we were able to consider the added value of EEG
variables when our clinical prediction model was applied to the valida-
tion set. The following clinical features were included in the model (see
Table S1, Supplement S3 in Data S1); age, sex (male/female), parents’
socioeconomic status, patients’ education level and the total education
in years for the patient, ICD diagnosis, CGI scores, and GAF scores
(GAF-S and GAF-F scores). In addition, all PANSS items were
included in the model. This resulted in 39 input features for the clinical
model. Explained variance above the chance level was found for the
regression model with the outcome ΔPANSS+ at 4 to 6 weeks
(R2 = 0.12, P = 0.008). Results are shown in Table 3. The best fea-
tures identiﬁed were PANSS items P3 (hallucinatory behavior), P6
(suspiciousness/persecution), N5 (difﬁculty in abstract thinking), GAF
symptoms, and age at baseline. The clinical test model was validated
on new data of 45 participants. The R2 for this model was 0.32
(Table 3). Sensitivity analysis with permutated individual PANSS items
showed that the model performed above the chance level and that these
results were not just a consequence of phenomena such as regression to
the mean (model R2 = 0.29, permutated R2 = (cid:2)0.12, P = 0.001). Fur-
thermore, the results are not explained by noise (model R2 = 0.23,
noise R2 = 0.025, noise SD = 0.014, P = 0.001) (Supplement S6 and
Tables S3, S4, and S5 in Data S1).

Model 2 (clinical and EEG model)
We then tested a combined EEG and clinical model with 99 input fea-
tures (39 clinical and 60 EEG features). The combined model
included 45 patients. The model signiﬁcantly explained variance in
ΔPANSS+ at 4 to 6 weeks (R2 = 0.34, P = 0.002) (Table 3). Fea-
tures with the highest VIMP were the Th in the alpha band (AEC-c),
the mean phase lag index (beta band), PANSS item P3 hallucinatory
behavior, betweenness centrality in the delta band (PLI-based), and
the degree in the theta band (AEC-c-based). The CI of the clinical
model (1b) (0.04–0.33) and the CI of the combined model (0.03–
0.65) overlapped, showing no signiﬁcant improvement of the com-
bined clinical and EEG model over the clinical model.

Change after AP medication (Q3)
Th in the alpha band and the phase lag index in the beta band were the
most predictive features (VIMP > 90) for our EEG model. Therefore,
we tested whether these characteristics changed after treatment with
APs in follow-up EEG recordings (N = 21). A lower Th (based on
alpha band AEC-c) at baseline was associated with better subsequent
treatment response, and, at the group level, the Th decreased after treat-
ment (mean = 0.391) compared with baseline (mean = 0.444; paired
t test: t = 8.09; d.f = 20; P < 0.01, see also Fig. 2). No correlations

0.44

y
h
c
r
a
r
e
h
e
e
r
T

i

0.40

0.36

Baseline

Follow–up

Fig. 2 Tree hierarchy in the alpha band (based on amplitude envelope
correlation-corrected) for individual patients. The colored lines represent individ-
ual patients.

were found between Th after AP treatment and ΔPANSS+ scores at
follow-up (r = 0.036; d.f. = 19; P = 0.88).

degree

To further investigate whether those changes could be related to
distinct regions in the brain, we applied a source-space analyses atlas-
based beamforming approach.32 The Th deﬁnes the hierarchy of the
MST organization as optimal topology. Given that the Th is a global
measure and incorporates betweenness centrality, we computed this
metric at the source level. Moreover, considering the Th also entails
network organization, we additionally examined alterations at
the
source level in the network’s degree. Results are shown in Figure 3.
Right posterior cingulate BC increased (baseline: 0.066, follow-up;
0.09, P = 0.025) and right frontal pole BC decreased after treatment
(baseline: 0.070, follow-up: 0.037; P = 0.007), while left lingual sul-
cus
0.0283;
P = 0.018) and the degree decreased for the right rostral middle fron-
tal gyrus (baseline: 0.0337, follow-up: 0.0294; P = 0.044) and the
right frontal pole (baseline 0.0279, follow-up: 0.0229; P = 0.006).

follow-up:

(baseline:

increased

The beta band PLI showed no signiﬁcant differences between
different time points (baseline mean: 0.135, follow-up mean: 0.134,
Wilcoxon rank test: V = 140; P = 0.68). No correlation with the
corrected PANSS score was found (r = 0.098; P = 0.67). We
observed nodal changes (i.e. average functional connectivity for a
brain region) in source-space, although their complex pattern proved
challenging for further pathophysiological interpretation. We further
examined differences in source-level functional connections (edges)
using network-based statistics,52 where network-based statistics
showed no signiﬁcant changes in speciﬁc connections after treatment
for beta band PLI. For further details, please refer to Supplement S6
and Table S6 in Data S1.

0.0248,

Table 3. Results of the different RFregression models

Model

Patients, n

Features, n

Clinical model 1a
Validation model 1b
EEG model 2

70
45
45

39
39
99

R2

0.12
0.32
0.34

Conﬁdence interval R2

0–0.33
0.04–0.33
0.03–0.65

P value
0.008*
NA
0.002

mtry

7
7
10

Provided the R2, where an R2 close to 1 means a strong relationship. If R2 is 1, the model accounts for 100% variation. *P < 0.05.
EEG, electroencephalography; NA, not applicable; RF, random forest. mtry is the number of variables considered at each split in the RF model.

192

Psychiatry and Clinical Neurosciences 79: 187–196, 2025

 
PCNPsychiatry and

Clinical Neurosciences

Treatment response prediction in FEP

L

L

0.0371

0.1338

R

L

0.0213

0.0415

BC baseline

R

L

Degree Baseline

BC follow-up

Degree follow-up

R

R

Significant nodes

Significant nodes

Fig. 3 Visualization of alterations in network topology. Left: betweenness centrality (BC) at baseline and follow-up and marked nodes that showed signiﬁcant change
over time regarding the BC. Right: degree at baseline and follow-up and marked nodes that showed signiﬁcant changes over time regarding the degree. The template
brains are viewed from sagittal left and sagittal right. Nodes with a signiﬁcant decrease are depicted in blue, while those with a signiﬁcant increase are shown in red.

Discussion
In this study, we developed a predictive model for treatment response
in AP-naïve patients with FEP combining clinical and EEG data. The
clinical model demonstrated an explained variance of 12% in
the training set and 32% in the validation set for the outcome of
change in ΔPANSS+ scores at follow-up. The clinical feature with
the highest predictive value for treatment response was hallucinatory
behavior. A model combining clinical and EEG information demon-
strated an explained variance of 34%, which showed no signiﬁcant
improvement compared with the clinical model. Lower Th in the
alpha band was the most important EEG characteristic in the model,
which further decreased at a group level after treatment. Regional
analysis in source-space suggests that a less central role for the frontal
pole and increased centrality of the posterior cingulate gyrus in the
alpha band network may contribute to this change in the hierarchical
organization of the functional brain network.

It is noteworthy that the explained variance in the validation set
(1b) was higher than in the training set (1a). For models 1a and 1b,
different numbers of patients deriving from the three different cohorts
were included, based on the availability of EEG data. Compared with
the validation set 1b, the training set 1a included relatively more
patients from the PECANS II study (i.e. 51% vs 36%). Given that
both models consist of different numbers of patients from the differ-
ent cohorts, with slightly different inclusion criteria, this may have
contributed to the observed treatment response differences.

There are previous studies using multimodel neuropsychiatric
data for treatment response,15,53 but we are not aware of previous
studies using a combined model of rs-EEG and clinical features.
Although we found no signiﬁcant added value of EEG to the clinical
prediction model, some clinical decisions might beneﬁt from EEG
information, e.g. patients who have atypical symptoms and therefore
only clinical prediction is less reliable. Previous research, however,

has indicated the potential of either clinical or EEG characteristics as
input for multivariate prediction models of treatment response. Previ-
ous work has found that a higher severity in lack of insight (PANSS
item G12), lack of spontaneity and ﬂow of conversation (PANSS item
N6), and blunted affect (PANSS item N1), alongside a longer dura-
tion of untreated psychosis, were signiﬁcant predictors of patient non-
remission.13 In other work on patients with chronic psychosis rather
than ﬁrst episode, general
items had the most predictive value.54
Notably, both our work and the latter study listed difﬁculties with
abstract thinking (N5 PANSS item) among the top ﬁve features for
predicting treatment response. The primary feature in the clinical
model in our study was hallucinatory behavior, a factor not previously
identiﬁed as a key predictor of treatment response in FEP. However,
unlike our present analysis, previous studies utilized a binary outcome
instead of a continuous one, which might explain the differences in
ﬁndings. The literature on predicting AP treatment response based on
rs-EEG markers, apart from some previous studies,16,22 has mainly
focused on clozapine, which is prescribed in a later stage of the treat-
ment trajectory and therefore clinically incomparable.19–21

Although the literature is limited and inconsistent when investi-
gating speciﬁc cortical brain regions of interest,55–57 the default mode
network and striatum are consistently implicated in relation to AP
treatment response.58 Here, we found increased BC of the posterior
cingulate cortex (PCC) after treatment indicating a more centrale role
the alpha band functional brain network. The PCC is a key compo-
nent of the limbic system and default mode network and has been
implicated in the pathophysiology of schizophrenia.59,60 Similarly, the
lower degree and BC of the frontal pole and lower degree of the ros-
tral middle frontal gyrus, both part of the frontoparietal network, after
treatment, is consistent with previous reports of altered frontoparietal
connectivity in patients with schizophrenia.61–63 Although our ﬁnd-
ings align with certain existing neuroimaging literature, discrepancies

Psychiatry and Clinical Neurosciences 79: 187–196, 2025

193

Treatment response prediction in FEP

persist in the literature concerning alterations in connectivity and net-
work topology characteristics.58,64,65 Our results of the beta band PLI
the source level, where signiﬁcant changes of the
alterations at
PLI beta band over time were located in various different brain
regions point in that direction.

Strengths and limitations
We studied the predictive value of individual PANSS symptoms for
continuous outcomes over psychopathology subset scores related to
binarized outcomes based on arbitrary thresholding. This approach is
considered more methodologically sound66 and is in line with the
for more personalized psychiatry approaches. Our cohort
call
included only AP-naïve patients, and therefore no AP effects on the
baseline EEG interfered with our model. In addition, in contrast to
several previous studies,11–14 we used continuous outcomes, which
avoids arbitrary cutoffs for relative or absolute symptom reductions
to deﬁne treatment response. It was recently suggested that general-
izability of treatment outcome prediction models for patients with
schizophrenia is limited by their context dependency.9 We consider
the strict
inclusion criteria of AP-naïve individuals experiencing
their ﬁrst episode of psychosis, deﬁned medication regimens, and
the addition of EEG characteristics in the prediction model, as used
in the present study, to be potential solutions for some of the prob-
lems addressed by Chekroud and others.9

Our clinical model was tested in an independent validation set,
and sensitivity analyses ensured that
the observed results were
unlikely attributable to phenomena such as regression to the mean.67
However, our study was restricted by the comparatively modest sam-
ple size, especially for
the combined clinical and EEG model,
prohibiting us from validation of this model in new data.

The modest sample size may affect the robustness and generaliz-
ability of our ﬁndings. Consequently, we advise caution in inter-
preting the results and highlight the importance of future studies with
larger sample sizes to validate and expand upon our work.

Future research is also needed to test the generalizability of the
presented models and for application in other types of AP than ami-
sulpride and aripiprazole tested here. Our model needs to be validated
in larger samples to further ensure generalizability of our results.
Importantly, we were unable to test whether implementation of our
model would have led to other treatment decisions with better out-
comes. In addition, future research should add more modalities for
the further improvement of predicting treatment response. The clinical
application we aim for involves using a prediction model as a deci-
sion support system for clinicians. Once the model becomes suitable
for clinical application, the decision concerning the response to a par-
ticular AP medication will vary from patient to patient. Furthermore,
in this study, the follow-up period is limited to ≈6 weeks, whereas in
clinical settings, long-term outcomes hold importance.

Conclusion
Our study underscores the potential of the devised models in forecast-
ing treatment outcomes in FEP. Individual PANSS items such as hal-
lucinatory behavior combined with EEG characteristics of functional
networks, that also changed over time, were found to explain up to
34% of variance in treatment response. Nevertheless, our results sug-
gest that a combined model may not be beneﬁcial over a model
informed only by clinical and demographic characteristics. Further
reﬁnement of these models through simpliﬁcation and broader exter-
nal validation will enhance their clinical utility in predicting
responses in FEP.

Acknowledgment
Support for this study was provided solely from institutional and/or
departmental
funded by The
Netherlands Organization for Health Research and Development
(ZonMW) GGZ fellowship, award ID: 60-63600-98-711. Edwin van

sources. Edwin van Dellen was

194

PCNPsychiatry and

Clinical Neurosciences

Dellen, UMC Utrecht Clinical Research Talent Fellowship,
award ID: NA.

Disclosure statement
B.H.E.
is part of the advisory board of Eli Lilly Denmark A/S,
Janssen-Cilag, Lundbeck Pharma A/S, and Takeda Pharmaceutical
Company Ltd.; and has received lecture fees from Bristol-Myers
Squibb, Boehringer Ingelheim, Otsuka Pharma Scandinavia AB, Eli
Lilly Company, and Lundbeck Pharma A/S. B.Y.G. has been the
leader of a Lundbeck Foundation Centre of Excellence for Clinical
Intervention and Neuropsychiatric Schizophrenia Research (CINS)
(January 2009 – December 2021), which was partially ﬁnanced by an
independent grant from the Lundbeck Foundation based on interna-
tional review and partially ﬁnanced by the Mental Health Services in
the Capital Region of Denmark, the University of Copenhagen, and
other foundations. All grants are the property of the Mental Health
Services in the Capital Region of Denmark and administrated by
them. She has no other conﬂicts to disclose. K.B.B. received lecture
fees from Lundbeck Pharma A/S. All other authors declare no con-
ﬂicts of interest.

Author contributions
L.D.: Design, conceptualization, drafting of the manuscript, data ana-
lyses. M.Z.: Data analysis, drafting of sections of the manuscript.
J.F.: Data analysis, drafting of sections of the manuscript. W.O.:
Supervision of data analyses, editing manuscript, revision of the man-
uscript. A.H.: Supervision of speciﬁc analyses, critical revision of
manuscript. S.G.: Contribution to data analysis. K.A.: Data collection,
conceptualization, critical revision of the manuscript. B.G.: Data col-
lection, critical revision of the manuscript. A.Z.: Analyses software
development, supervision of data analysis, critical revision of the
manuscript. K.B.: Data collection, critical revision of the manuscript.
M.S.: Data collection, critical revision of the manuscript. F.S.: Con-
ceptualization, critical revision of the manuscript. C.S.: Analyses soft-
ware development,
the
manuscript. B.O.: Data collection, design, conceptualization, critical
revision of the manuscript. B.E.: Data collection, design, conceptuali-
zation, critical revision of the manuscript. E.D.: Supervision, design,
conceptualization, critical revision of the manuscript.

conceptualization,

revision of

critical

References
1.

Suvisaari J, Mantere O, Keinänen J et al. Is it possible to predict the
future in ﬁrst-episode psychosis? Front Psychiatry 2018; 9: 580.
Hui CLM, Wong AKH, Ho ECN et al. Effectiveness and optimal dura-
tion of early intervention treatment in adult-onset psychosis: A random-
ized clinical trial. Psychol. Med. 2023; 53: 2339–2351.
Bottlender R, Sato T, Jäger M et al. The impact of the duration of
untreated psychosis prior to ﬁrst psychiatric admission on the 15-year
outcome in schizophrenia. Schizophr. Res. 2003; 62: 37–44.
Kahn RS, Winter van Rossum I, Leucht S et al. Amisulpride and
olanzapine followed by open-label treatment with clozapine in ﬁrst-epi-
sode schizophrenia and schizophreniform disorder (OPTiMiSE): A three-
phase switching study. Lancet Psychiatry 2018; 5: 797–807.
Leucht S, Cipriani A, Spineli L et al. Comparative efﬁcacy and tolerabil-
ity of 15 antipsychotic drugs in schizophrenia: A multiple-treatments
meta-analysis. Lancet 2013; 382: 951–962.
Yakeley J, Hale R, Johnston J, Kirtchuk G, Shoenberg P. Psychiatry,
subjectivity and emotion – Deepening the medical model. Psychiatr.
Bull. 2014; 38: 97–101.
Grove WM, Zald DH, Lebow BS, Snitz BE, Nelson C. Clinical versus
mechanical prediction: A meta-analysis. Psychol. Assess. 2000; 12:
19–30.
Fernandes BS, Williams LM, Steiner J, Leboyer M, Carvalho AF,
Berk M. The new ﬁeld of ‘precision psychiatry’. BMC Med. 2017;
15: 80.
Chekroud AM, Hawrilenko M, Loho H et al. Illusory generalizability of
clinical prediction models. Science 1979. 2024; 383: 164–167.

2.

3.

4.

5.

6.

7.

8.

9.

10. Zellner M, Abbas AE, Budescu DV, Galstyan A. A survey of human
judgement and quantitative forecasting methods. R. Soc. Open Sci. 2021;
8: 201187.

Psychiatry and Clinical Neurosciences 79: 187–196, 2025

PCNPsychiatry and

Clinical Neurosciences

11. Del Fabro L, Bondi E, Serio F, Maggioni E, D’Agostino A, Brambilla P.
Machine learning methods to predict outcomes of pharmacological treat-
ment in psychosis. Transl. Psychiatry 2023; 13: 75.

12. Koutsouleris N, Kahn RS, Chekroud AM et al. Multisite prediction of
4-week and 52-week treatment outcomes in patients with ﬁrst-episode
psychosis: A machine learning approach. Lancet Psychiatry 2016; 3:
935–946.

13. Soldatos RF, Cearns M, Nielsen M et al. Prediction of early symptom
remission in two independent samples of ﬁrst-episode psychosis patients
using machine learning. Schizophr. Bull. 2022; 48: 283.

14. Wu CS, Luedtke AR, Sadikova E et al. Development and validation of a
machine learning individualized treatment rule in ﬁrst-episode schizo-
phrenia. JAMA Netw. Open 2020; 3: e1921660.

15. Bak N, Ebdrup BH, Oranje B et al. Two subgroups of antipsychotic-
naive, ﬁrst-episode schizophrenia patients identiﬁed with a gaussian mix-
ture model on cognition and electrophysiology. Transl. Psychiatry 2017;
7: e1087.

16. Ambrosen KS, Skjerbæk MW, Foldager J et al. A machine-learning
framework for robust and reliable prediction of short- and long-term
treatment response in initially antipsychotic-naïve schizophrenia patients
based on multimodal neuropsychiatric data. Transl. Psychiatry 2020;
10: 276.

17. Koukkou M, Koenig T, Bänninger A et al. Neurobiology of schizophre-
nia: Electrophysiological indices. In: Advances in Psychiatry. Springer
International Publishing, Cham, 2018; 433–459.

18. McCarley RW, Nakamura M, Shenton ME, Salisbury DF. Combining
ERP and structural MRI information in ﬁrst episode schizophrenia and
bipolar disorder. Clin. EEG Neurosci. 2008; 39: 57–60.

19. Khodayari-Rostamabad A, Hasey GM, MacCrimmon DJ, Reilly JP, de
Bruin H. A pilot study to determine whether machine learning methodol-
ogies using pre-treatment electroencephalography can predict the symp-
tomatic response to clozapine therapy. Clin. Neurophysiol. 2010; 121:
1998–2006.

20. Ciprian C, Masychev K, Ravan M, Reilly JP, Maccrimmon D. A
machine learning approach using effective connectivity to predict
response to clozapine treatment. IEEE Trans. Neural. Syst. Rehabil. Eng.
2020; 28: 2598–2607.

21. Masychev K, Ciprian C, Ravan M, Manimaran A, Deshmukh AA. Quan-
titative biomarkers to predict response to clozapine treatment using rest-
ing EEG data. Schizophr. Res. 2020; 223: 289–296.

22. Dominicus LS, Oranje B, Otte WM et al. Macroscale EEG characteris-
tics in antipsychotic-naïve patients with ﬁrst-episode psychosis and
healthy controls. Schizophrenia 2023; 9: 5.

23. Ambrosen KS, Fredriksson F, Anhøj S et al. Clustering of antipsychotic-
naïve patients with schizophrenia based on functional connectivity from
resting-state electroencephalography. Eur. Arch. Psychiatry Clin. Neu-
rosci. 2023; 273: 1785–1796.

24. Zandstra MG, Meijs H, Somers M et al. Associations between psycho-
tropic drugs and rsEEG connectivity and network characteristics: A
cross-sectional study in hospital-admitted psychiatric patients. Front.
Neurosci. 2023; 17: 17.

25. Cadena EJ, White DM, Kraguljac NV et al. Cognitive control network
dysconnectivity and response to antipsychotic treatment in schizophrenia.
Schizophr. Res. 2019; 204: 262–270.

26. Sarpal DK, Robinson DG, Lencz T et al. Antipsychotic treatment and
functional connectivity of the striatum in ﬁrst-episode schizophrenia.
JAMA Psychiatry 2015; 72: 5.

27. Kraguljac NV, White DM, Hadley N et al. Aberrant hippocampal
connectivity in unmedicated patients with schizophrenia and effects of
antipsychotic medication: A longitudinal resting state functional MRI
study. Schizophr. Bull. 2016; 42: 1046–1055.

28. Han S, Becker B, Duan X et al. Distinct striatum pathways connected to
salience network predict symptoms improvement and resilient function-
ing in schizophrenia following risperidone monotherapy. Schizophr. Res.
2020; 215: 89–96.

29. Kazdin AE. Mediators and mechanisms of change in psychotherapy

research. Annu. Rev. Clin. Psychol. 2007; 3: 1–27.

30. Nielsen MO, Rostrup E, Wulff S et al. Improvement of brain reward
abnormalities by antipsychotic monotherapy in schizophrenia. Arch. Gen.
Psychiatry 2012; 69: 1195–1204.

31. Bojesen KB, Ebdrup BH, Jessen K et al. Treatment response after 6 and
26 weeks
in
antipsychotic-naïve patients with psychosis. Psychol. Med. 2020; 50:
2182–2193.

related to baseline glutamate and GABA levels

is

Treatment response prediction in FEP

32. Hillebrand A, Barnes GR. Beamformer analysis of MEG data. Int. Rev.

Neurobiol. 2005; 68: 149–171.

33. Desikan RS, Ségonne F, Fischl B et al. An automated labeling system
for subdividing the human cerebral cortex on MRI scans into gyral based
regions of interest. Neuroimage 2006; 31: 968–980.

34. Kay SR, Fiszbein A, Opler LA. The positive and negative syndrome
scale (PANSS) for schizophrenia. Schizophr. Bull. 1987; 13: 261–276.
35. Düring S, Glenthøj BY, Andersen GS, Oranje B. Effects of dopamine
D2/D3 blockade on human sensory and sensorimotor gating in ini-
antipsychotic-naive, ﬁrst-episode
tially
patients.
Neuropsychopharmacology 2014; 39: 3000–3008.

schizophrenia

36. Düring S, Glenthøj BY, Oranje B. Effects of blocking D2/D3 receptors on
mismatch negativity and P3a amplitude of initially antipsychotic naïve, ﬁrst
episode schizophrenia patients. Int. J. Neuropsychopharmacol. 2015; 19:
pyv109.

37. van Lutterveld R, Oranje B, Kemner C et al. Increased psychophysiolog-
ical parameters of attention in non-psychotic individuals with auditory
verbal hallucinations. Schizophr. Res. 2010; 121: 153–159.

38. Craddock M. EegUtils: Utilities for Electroencephalographic (EEG)
Analysis. [Internet]. 2021. [Cited 8 February 2021.] Available from
URL: https://craddm.github.io/eegUtils.

39. Perrin F, Pernier J, Bertrand O. Spherical splines for scalp potential and
current density mapping. Electroencephalogr. Clin. Neurophysiol. 1989;
72: 72–187.

40. Whitham EM, Lewis T, Pope KJ et al. Thinking activates EMG in scalp
electrical recordings. Clin. Neurophysiol. 2008; 119: 1166–1175.
41. Whitham EM, Pope KJ, Fitzgibbon SP et al. Scalp electrical recording
during paralysis: Quantitative evidence that EEG frequencies above
20 Hz are contaminated by EMG. Clin. Neurophysiol. 2007; 118:
1877–1888.

42. Aertsen AMHJ, Gerstein GL, Habib MK, Palm G. Dynamics of neuronal
ﬁring correlation: Modulation of “effective connectivity”. J. Neurophysiol.
1989; 61: 900–917.

43. Stam CJ, Nolte G, Daffertshofer A. Phase lag index: Assessment of func-
tional connectivity from multi channel EEG and MEG with diminished
bias from common sources. Hum. Brain Mapp. 2007; 28: 1178–1193.
44. Hipp JF, Hawellek DJ, Corbetta M, Siegel M, Engel AK. Large-scale
cortical correlation structure of spontaneous oscillatory activity. Nat.
Neurosci. 2012; 15: 884–890.

45. Fraschini M, Pani SM, Didaci L, Marcialis GL. Robustness of functional
connectivity metrics for EEG-based personal identiﬁcation over task-
induced intra-class and inter-class variations. Pattern Recognit. Lett.
2019; 125: 49–54.

46. Bullmore E, Sporns O. Complex brain networks: Graph theoretical analysis
of structural and functional systems. Nat. Rev. Neurosci. 2009; 10: 186–198.
47. Kruskal JB. On the shortest spanning subtree of a graph and the traveling
salesman problem (1956). In: Ideas that Created the Future. MIT Press,
Cambridge, 2021.

48. Tewarie P, van Dellen E, Hillebrand A, Stam CJ. The minimum span-
ning tree: An unbiased method for brain network analysis. Neuroimage
2015; 104: 177–188.

49. Leucht S, Arbter D, Engel RR, Kissling W, Davis JM. How effective are
second-generation antipsychotic drugs? A meta-analysis of placebo-
controlled trials. Mol. Psychiatry 2009; 14: 429–447.

50. Furukawa TA, Levine SZ, Tanaka S et al. Initial severity of schizophre-
nia and efﬁcacy of antipsychotics: Participant-level meta-analysis of
6 placebo-controlled studies. JAMA Psychiatry 2015; 72: 14.

51. Harrell F. Statistical errors in the medical literature. Stat. Think. 2017.

https://www.fharrell.com/post/errmed/

52. Zalesky A, Fornito A, Bullmore ET. Network-based statistic: Identifying
differences in brain networks. Neuroimage 2010; 53: 1197–1207.
53. Ebdrup BH, Axelsen MC, Bak N et al. Accuracy of diagnostic classiﬁca-
tion algorithms using cognitive-, electrophysiological-, and neuroanatom-
ical data in antipsychotic-naïve schizophrenia patients. Psychol. Med.
2019; 49: 2754–2763.

54. Podichetty JT, Silvola RM, Rodriguez-Romero V et al. Application of
machine learning to predict reduction in total PANSS score and enrich
enrollment in schizophrenia clinical trials. Clin. Transl. Sci. 2021; 14:
1864–1874.

55. Kochunov P, Fan F, Ryan MC et al. Translating ENIGMA schizophrenia
ﬁndings using the regional vulnerability index: Association with cognition,
symptoms, and disease trajectory. Hum. Brain Mapp. 2022; 43: 566–575.
56. Kochunov P, Hong LE, Dennis EL et al. ENIGMA-DTI: Translating
reproducible white matter deﬁcits into personalized vulnerability metrics

Psychiatry and Clinical Neurosciences 79: 187–196, 2025

195

Treatment response prediction in FEP

in cross-diagnostic psychiatric research. Hum. Brain Mapp. 2022; 43:
194–206.

57. Dabiri M, Dehghani Firouzabadi F, Yang K, Barker PB, Lee RR,
Yousem DM. Neuroimaging in schizophrenia: A review article. Front.
Neurosci. 2022; 16: 1042814.

58. Yang C, Tang J, Liu N et al. The effects of antipsychotic treatment on
the brain of patients with ﬁrst-episode schizophrenia: A selective review
of longitudinal MRI studies. Front. Psychiatry 2021; 12: 593703.
59. Wei GX, Ge L, Chen LZ, Cao B, Zhang X. Structural abnormalities of
cingulate cortex in patients with ﬁrst-episode drug-naïve schizophrenia
comorbid with depressive symptoms. Hum. Brain Mapp. 2021; 42:
1617–1625.

60. Newell KA, Zavitsanou K, Jew SK, Huang XF. Alterations of muscarinic
and GABA receptor binding in the posterior cingulate cortex in schizophre-
nia. Prog. Neuropsychopharmacol. Biol. Psychiatry 2007; 31: 225–233.
61. Tu PC, Lee YC, Chen YS, Li CT, Su TP. Schizophrenia and the brain’s con-
trol network: Aberrant within- and between-network connectivity of the
frontoparietal network in schizophrenia. Schizophr. Res. 2013; 147: 339–347.
62. Orellana G, Slachevsky A. Executive functioning in schizophrenia.

Front. Psychiatry 2013; 4: 35.

63. Snelleksz M, Rossell SL, Gibbons A, Nithianantharajah J, Dean B. Evi-
dence that the frontal pole has a signiﬁcant role in the pathophysiology
of schizophrenia. Psychiatry Res. 2022; 317: 114850.

PCNPsychiatry and

Clinical Neurosciences

64. Hadley JA, Kraguljac NV, White DM, Ver Hoef L, Tabora J, Lahti AC.
Change in brain network topology as a function of treatment response in
schizophrenia: A longitudinal resting-state fMRI study using graph the-
ory. NPJ Schizophr. 2016; 2: 16014.

65. Wang LX, Guo F, Zhu YQ et al. Effect of second-generation anti-
psychotics on brain network topology in ﬁrst-episode schizophre-
rs-fMRI study. Schizophr. Res. 2019; 208:
nia: A longitudinal
160–166.

66. van Dellen E. Precision psychiatry: Predicting predictability. 2023.
67. Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: What
it is and how to deal with it. Int. J. Epidemiol. 2005; 34: 215–220.
68. Leucht S, Samara M, Heres S, Davis JM. Dose equivalents for anti-
psychotic drugs: The DDD method. Schizophr. Bull. 2016; 42:
42–S94.

69. World Health Organization Collaborating Centre for Drug Statistics
Methodology. ATC/DDD Methodology and ATC/DDD Index 2020.
WHO Collaborating Centre for Drug Statistics Methodology, Oslo, Nor-
way; 2019.

Supporting Information
Additional supporting information can be found online in the
Supporting Information section at the end of this article.

196

Psychiatry and Clinical Neurosciences 79: 187–196, 2025
