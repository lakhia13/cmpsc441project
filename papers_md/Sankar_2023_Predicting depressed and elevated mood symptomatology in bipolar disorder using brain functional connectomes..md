# Sankar_2023_Predicting depressed and elevated mood symptomatology in bipolar disorder using brain functional connectomes.

Psychological Medicine

cambridge.org/psm

Predicting depressed and elevated mood
symptomatology in bipolar disorder using
brain functional connectomes

Original Article

Cite this article: Sankar A et al (2023).
Predicting depressed and elevated mood
symptomatology in bipolar disorder using
brain functional connectomes. Psychological
Medicine 53, 6656–6665. https://doi.org/
10.1017/S003329172300003X

Received: 14 July 2022
Revised: 7 December 2022
Accepted: 3 January 2023
First published online: 9 March 2023

Keywords:
Bipolar disorder; CPM; functional magnetic
resonance imaging; symptom severity

Author for correspondence:
Anjali Sankar, E-mail: anjali.sankar@yale.edu

© The Author(s), 2023. Published by
Cambridge University Press. This is an Open
Access article, distributed under the terms of
the Creative Commons Attribution licence
(http://creativecommons.org/licenses/by/4.0/),
which permits unrestricted re-use, distribution
and reproduction, provided the original article
is properly cited.

, Xilin Shen3, Lejla Colic1,4,5, Danielle A. Goldman1,6,

Anjali Sankar1,2
Luca M. Villa1,7, Jihoon A. Kim1, Brian Pittman1, Dustin Scheinost3,
R. Todd Constable3 and Hilary P. Blumberg1,3,8

1Department of Psychiatry, Yale School of Medicine, New Haven, CT, USA; 2Neurobiology Research Unit,
Copenhagen University Hospital, Rigshospitalet, Copenhagen, Denmark; 3Department of Radiology and
Biomedical Imaging, Yale School of Medicine, New Haven, CT, USA; 4Department of Psychiatry and Psychotherapy,
Jena University Hospital, Jena, Germany; 5German Center for Mental Health, Halle-Jena-Magdeburg, Magdeburg,
Germany; 6Interdepartmental Neuroscience Program, Yale School of Medicine, New Haven, CT, USA; 7Department
of Psychiatry, University of Oxford, Oxford, UK and 8Child Study Center, Yale School of Medicine, New Haven,
CT, USA

Abstract

Background. The study is aimed to identify brain functional connectomes predictive of
depressed and elevated mood symptomatology in individuals with bipolar disorder (BD)
using the machine learning approach Connectome-based Predictive Modeling (CPM).
Methods. Functional magnetic resonance imaging data were obtained from 81 adults with BD
while they performed an emotion processing task. CPM with 5000 permutations of leave-one-
out cross-validation was applied to identify functional connectomes predictive of depressed
and elevated mood symptom scores on the Hamilton Depression and Young Mania rating
scales. The predictive ability of the identified connectomes was tested in an independent sam-
ple of 43 adults with BD.
Results. CPM predicted the severity of depressed [concordance between actual and predicted
values (r = 0.23, pperm (permutation test) = 0.031) and elevated (r = 0.27, pperm = 0.01) mood.
Functional connectivity of left dorsolateral prefrontal cortex and supplementary motor area
nodes, with inter- and intra-hemispheric connections to other anterior and posterior cortical,
limbic, motor, and cerebellar regions, predicted depressed mood severity. Connectivity of left
fusiform and right visual association area nodes with inter- and intra-hemispheric connec-
tions to the motor, insular, limbic, and posterior cortices predicted elevated mood severity.
These networks were predictive of mood symptomatology in the independent sample (r ⩾
0.45, p = 0.002).
Conclusions. This study identified distributed functional connectomes predictive of depressed
and elevated mood severity in BD. Connectomes subserving emotional, cognitive, and psycho-
motor control predicted depressed mood severity, while those subserving emotional and social
perceptual functions predicted elevated mood severity. Identification of these connectome net-
works may help inform the development of targeted treatments for mood symptoms.

Introduction

Depressed and elevated mood symptom severity underlie the suffering associated with bipolar
disorder (BD) and are among the strongest clinical predictors of functional impairment and
disability in the disorder (Judd et al., 2005). Furthermore, mood symptoms contribute to
the high risk for suicide in the disorder. Elucidation of the brain functional disturbances
that contribute to mood symptoms in individuals with BD could advance our understanding
of the pathophysiology of the disorder and enable the development of more targeted thera-
peutic approaches.

Previous functional magnetic resonance imaging (fMRI) studies investigating brain func-
tional disturbances associated with mood states often used categorical determinations of par-
ticipants meeting criteria for depressed or elevated episodes. Only to a lesser extent was mood
assessed dimensionally by severity scales even though this approach has the benefit of provid-
ing information regarding symptom severity (Sankar et al., 2020). Findings were commonly
observed in the prefrontal cortex (PFC), with patterns of dysfunction suggested to vary by
mood state in their relative hemispheric and ventral v. dorsal distribution. Depressed episodes
of BD, the most common and studied of the acute BD episode types, were associated with dys-
function in the left PFC and dorsolateral PFC (dlPFC) areas (Altshuler et al., 2008; Goldman
et al., 2022). Dysfunctions in the dlPFC have also been associated with depressed symptom

Psychological Medicine

6657

et

et

al.,

al.,

(Bertocci

2020; Brooks

severity
2009;
Fernández-Corcuera et al., 2013; Ketter et al., 2001; Koenigs &
Grafman, 2009). Studies of elevated mood episodes, albeit fewer,
suggest dysfunction particularly in the right hemisphere and in
ventral PFC (vPFC) areas (Blond & Blumberg, 2010; Blumberg
et al., 1999, 2003; Elliott et al., 2004; Liu et al., 2012; Strakowski
et al., 2011). Although there is a convergence of finding in the
PFC, neuroimaging investigations of mood states of BD have
increasingly suggested that dysfunction at the system level, rather
than solely in isolated brain regions, contributes to BD mood epi-
in elevated mood
sodes and symptom severity. For example,
states, in addition to findings in the right vPFC, there is also
some evidence for dysfunction in larger scale networks compris-
ing limbic, predominantly amygdala (Cerullo et al., 2012; Li et al.,
2015), and temporal, particularly fusiform area (Adleman et al.,
2013a, 2013b; Strakowski et al., 2011), parietal (Öngür et al.,
2010; Zhang et al., 2020), and occipital cortical regions (Manelis
et al., 2019). In addition to distributed intrahemispheric findings,
reports also suggest disrupted inter-hemispheric connectivity in
BD (Blumberg et al., 2003; Liu et al., 2012).

Findings from the above fMRI studies are based on examining
average group-level differences or correlations. The effect sizes
from such traditional methods are typically not high enough to
make individual-level inferences (Abi-Dargham & Horga, 2016).
Furthermore, for neuroimaging findings to be defined as biomar-
kers, they need to be replicable when tested in an independent
dataset (Orru, Pettersson-Yeo, Marquand, Sartori, & Mechelli,
2012; Orrù, Monaro, Conversano, Gemignani, & Sartori, 2020).
Machine learning approaches, such as the recently developed
connectome-based predictive modeling (CPM) method (Shen
et al., 2017), are beneficial as they allow the prediction of behavior
or symptom severity at the individual level by determining the
most optimal predictive model using multivariate brain metrics
and involve tests of whether the same model can predict the
same behavior in an independent sample. Thus, machine learning
based analyses (e.g. CPM) permit advances toward providing
foresight with clinical relevance by predicting behavior of individ-
ual subjects (Hahn, Nierenberg, & Whitfield-Gabrieli, 2017;
Walter et al., 2019).

CPM has been previously used to identify functional brain
connectivity matrices, referred to as connectome ‘fingerprints,’
that predict individual differences in traits and behaviors such
as fluid (Finn et al., 2015) and sustained (Rosenberg et al.,
2016; Rosenberg, Hsu, Scheinost, Todd Constable, & Chun,
2018)
intelligence, and neuroticism and extraversion (Hsu,
Rosenberg, Scheinost, Constable, & Chun, 2018). More recently,
CPM was used to identify connectome fingerprints of anxiety
severity (Wang et al., 2021), and treatment response in major
depressive (Fan et al., 2020; Ju et al., 2020) and substance use
(Yip, Scheinost, Potenza, & Carroll, 2019) disorders. Typically,
resting state data have been used in fMRI studies to make
individual-level predictions about network alterations in psychi-
atric disorders. However, recent evidence suggests that salient
tasks can modulate brain functional networks and amplify
disorder-relevant individual differences in patterns of functional
connectivity (Barron et al., 2019; Greene, Gao, Scheinost, &
Constable, 2018), akin to the use of stress tests to identify cardiac
dysfunction. Therefore, prediction models built using salient task
data tend to outperform those built with resting state data (Greene
et al., 2018). In the present fMRI study, participants performed a
task in which they processed emotional face stimuli salient to the
emotional dysfunction characteristic of BD and shown repeatedly

to elicit brain differences between individuals with BD compared
to healthy control individuals (Blumberg et al., 2003; Johnston
et al., 2017; Liu et al., 2012; Wang, Bobrow, Liu, Spencer, &
Blumberg, 2012). In this study, CPM was applied to a dataset
of adults with BD and further tested on an independent dataset
of adults with BD to examine if (a) models built on the emotional
task data can predict severity of depressed and elevated mood
symptomatology in BD at the individual-level, and (b) findings
replicate in an independent dataset of adults with BD.

To our knowledge, this is the first study to use a machine
learning approach to predict individual-level depressed and ele-
vated mood symptomatology in BD. Based on previous literature
exploring group-level differences in brain function, we expected
that whole-brain, intra- and inter-hemispheric functional con-
nectivity alterations in a left dlPFC system would predict individ-
ual differences in depressed mood symptom severity (Altshuler
et al., 2008; Brooks et al., 2009; Fernández-Corcuera et al., 2013;
Ketter et al., 2001; Luo et al., 2018) and in a right vPFC system
would predict individual differences in elevated mood symptom
severity (Blumberg et al., 2003; Liu et al., 2012).

Methods

Participants in the training dataset

(First,

(SCID)

Eighty-one participants met criteria for BD according to the
Diagnostic and Statistical Manual of Mental Disorders (Fourth
ed. Text Revision; DSM-IV-TR) [ages 18–55 years, mean age ±
standard deviation (S.D.) = 29.3 ± 11.1 years; 63.0% female]. The
presence or absence of Axis I diagnoses and mood state for all
confirmed with the Structured Clinical
participants were
Interview for DSM-IV Diagnosis
2014).
Two-thirds of the participants were on psychotropic medications
at the time of scan. Exclusion criteria were major medical disor-
ders (except treated hypothyroidism), central nervous system con-
loss of consciousness ⩾5 min,
ditions including a history of
substance or alcohol abuse or dependence within three months
of MRI scanning, and MRI contraindications. The demographic
and clinical characteristics of the sample are detailed in the online
Supplementary section (Table S1). Written informed consent was
obtained from all participants. The authors assert that all proce-
dures were conducted in accordance with the Yale School of
Medicine (SOM) Human Investigation Committee institutional
review board.

Mood symptom severity of all the participants was assessed
using the Hamilton Depression Rating Scale 29-item version
(HDRS-29)
(Williams, Link, Rosenthal, & Terman, 1988)
(mean ± S.D. = 12.3 ± 10.1; range:0–40) and the Young Mania
Rating Scale (YMRS) (Young, Biggs, Ziegler, & Meyer, 1978)
(mean ± S.D. = 6.5 ± 6.1; range:0–23). However, as the HDRS-29
scale is multifactorial, and measures more than one symptom
cluster which may have different underlying neurobiological
bases, a depressed mood score (HDRS-5) was calculated, as
done in our previous work (11), by summing five items from
the HDRS (HDRS-5) that showed the highest loading for depres-
sion (i.e. depressed mood, work and interests, guilt, psychomotor
retardation, and suicide (12) (HDRS-5 mean ± S.D. = 3.4 ± 3.4;
range:0–13). The YMRS on the other hand, has been found to
have higher validity when used in the one-factor format (i.e.
using total scores) (Serrano, Ezpeleta, Alda, Matalí, & San,
2011; Youngstrom, Kmett Danielson, Findling, Gracious, &
Calabrese, 2002). Furthermore, structures of this scale have not

6658

Anjali Sankar et al.

been well-established as they have been tested only using small
(e.g. n = 17) sample sizes (Double, 1990). Therefore, in the present
study, the YMRS scale, with the total score obtained by summing
all the eleven items of the scale, was used to predict elevated mood
severity.

independently and then combined into a single transformation
by which single participant images (i.e. functional, 2-dimensional
anatomical, and 3-dimensional MPRAGE images of a participant)
were warped into MNI space. This single transformation was per-
formed to reduce interpolation error and was done using
BioImage Suite.

MRI data acquisition

A 3-Tesla Trio scanner was used for MR scanning (Siemens,
Erlangen, Germany). After a localizing scan, a high-resolution
3-dimensional volume was obtained using magnetization-
prepared rapid gradient-echo (MPRAGE) sequence (repetition
time (TR): 1500 ms; echo time (TE): 2.77 ms; flip angle (FA):
15°; matrix: 256 × 256; field of view (FOV): 256 mm × 256 mm;
slice thickness, 1.0 mm without gap; 160 contiguous slices).
Two-dimensional T1-weighted images were also obtained (TR:
300 ms; TE: 2.47 ms; FA: 60°; matrix: 256 × 256; FOV: 256 ×
256 mm2; slice thickness: 3 mm without gap). FMRI data were
collected with a T2*-weighted single-shot echo planar imaging
sequence with Blood Oxygen Level-Dependent contrast, aligned
with the anterior commissure-posterior commissure plane (TR:
2000 ms; TE: 25 ms; FA: 80°; matrix: 64 × 64; FOV: 240 mm ×
240 mm; slice thickness: 3.0 mm without gap; 32 contiguous
slices). FMRI data were obtained while participants performed
an emotional face gender-labeling task, as reported previously,
in which they viewed faces from the Ekman series depicting
happy, fearful, or neutral expressions for 2 s (sec), separated by
4–12 s periods viewing a fixation cross-hair, and pressed a button
to indicate whether the face belonged to a male or a female
(Johnston et al., 2017; Wang et al., 2012). Participants performed
four consecutive runs of the task, each lasting 4 min (min) and 50 s.
FMRI data collection time was 19 min 20 s.

Preprocessing

AFNI’s

six temporal derivatives,

signal, mean gray matter

The first four volumes of each functional run were discarded to
allow for hemodynamic steady state. Slice timing and motion cor-
rection were performed; all participants had an average framewise
displacement of <0.2 mm. Images were iteratively smoothed with
a Gaussian filter of 6 mm full-width at half-maximum (FWHM)
using
3dBlurToFWHM (afni.nimh.nih.gov/afni/)
(Scheinost, Papademetris, & Constable, 2014). Further preproces-
sing steps were performed using BioImage Suite (bioimagesui-
te.org). Covariates of no interest were regressed from the data,
including linear and quadratic drifts, mean cerebrospinal fluid,
mean white matter
signal, and
24-parameter motion variables (including six rigid-body motion
squares).
parameters,
Functional connectivity was calculated based on the ‘raw’ task
time courses,
i.e., without regressing out task-evoked activity.
The data were temporally smoothed with a Gaussian filter (∼cut-
off frequency = 0.12 Hz). Finally, data from the four runs were
variance normalized and concatenated for each participant. To
allow images to be compared across participants, all
images
were warped into MNI (Montreal Neurological Institute) space
using a series of linear and non-linear registrations. The fMRI
data were linearly registered to the 2-dimensional anatomical
images. The 2-dimensional anatomical images were linearly regis-
tered to the 3-dimensional MPRAGE images. The 3-dimensional
MPRAGE images were then non-linearly registered to the MNI
template using a previously validated algorithm (Scheinost
calculated
et

transformation pairs were

2017). All

and their

al.,

Connectivity matrices

(Lacadie,

Fulbright,

Whole brain functional connectivity was assessed using methods
described previously (Finn et al., 2015; Shen et al., 2017). In brief,
network nodes were defined using the Shen 368-node functional
brain atlas (Horien, Shen, Scheinost, & Constable, 2019), which
includes the cortex, subcortex, cerebellum, and brainstem. For
the cortex, Shen et al., applied a group-wise parcellation algorithm
(Shen, Papademetris, & Constable, 2010) and obtained 164 nodes
in the left hemisphere and 163 nodes in the right hemisphere.
This functional parcellation of the cortex was computed based
on resting-state BOLD data from 120 participants. For the subcor-
tical area, Shen et al. adopted anatomical definitions of subcortical
structures
Rajeevan, Constable, &
Papademetris, 2008) with seven nodes in each of the left and
right subcortical regions. For the cerebellum, they adapted the
17 network definition proposed by Buckner et al. (Buckner,
Krienen, Castellanos, Diaz, & Yeo, 2011) eliminating some
nodes of small size, leaving 13 nodes in each of the left and
right cerebellum. They also included one node for the brain
stem area. For each participant, the mean time course for each
of the 368 nodes was extracted to compute node-by-node pairwise
Pearson’s correlation coefficients. The r values were transformed
using Fisher’s z transformation resulting in a symmetric 368 by
368 connectivity matrix of correlation values representing edges.
The edges can be visualized as connections between nodes that
are assigned to one of ten bilateral macroscale brain regions of
the cortex, subcortex, cerebellum, or brainstem. One subject was
excluded from the analysis due to its distribution of edge weights
being an outlier when compared to the rest of the participants.

Connectome-based Predictive Modeling (CPM)

CPM was conducted using previously validated custom MATLAB
scripts (Shen et al., 2017). CPM uses connectivity matrices (edges)
and clinical data as input variables to generate a predictive model
of the clinical data from the edges. Edges and clinical data from
the training data set are correlated to identify positive and nega-
tive predictive networks. The most relevant edges are selected for
further analysis based on the significance of the linear association
between edge and clinical data. Consistent with previous CPM
studies, a threshold of p < 0.001 was set to select edges (Cai,
Zhu, & Yu, 2020; Song et al., 2020). Positive networks are com-
prised of increased edge weights (increased connectivity) asso-
scores, and negative networks of
ciated with the clinical
decreased edge weights (decreased connectivity) associated with
the positive and negative networks
clinical scores. Together,
make up the
the overall network model.
Single-subject summary statistics are then calculated by separately
summing the significant edge weights in the positive and negative
networks which are then used to determine coefficients of the lin-
ear model relating network strength with the clinical data. The
resulting polynomial coefficients, which include the slope and
intercept of the linear model, are then applied to the test data
set to predict clinical scores (cross-validation approach). In this

combined or

Psychological Medicine

6659

study, a leave-one-out cross-validation (LOOCV) was used. The
common edges across the LOOCV iterations are used for model
interpretation.

Results

Prediction of depressed mood severity

Permutation testing

When using LOOCV, analyses in the leave-one-out folds are not
wholly independent, and the number of degrees of freedom is
thus overestimated for parametric p values based on correlation.
Permutation testing was therefore performed instead of parametric
testing. To generate null distributions for significance testing, the
correspondence between clinical scores and edges was randomly
shuffled 5000 times and the CPM analysis was rerun with the
shuffled data. The p values for leave-one-out predictions ( pperm)
were calculated by determining the percentage of permutations
that generated correlation coefficients larger than the correlation
coefficients from the original (unshuffled) leave-one-out predictions.

Predictor and control variables

Clinical data that were used as predictor variables in this study
were HDRS-5 and YMRS total scores. Exploratory analysis
using total HDRS scores (HDRS-29) as predictor variables was
also performed. Partial Pearson correlations of predicted and
observed scores were calculated controlling for age and gender.
It was confirmed that the average framewise displacement did
not correlate with the predictor variables in the sample (i.e.
HDRS-5 and YMRS scores, p > 0.13). Furthermore, the predictor
variables were not correlated ( p = 0.33) in the current sample.

Out-of-sample validation

To determine the generalizability of the findings, the resultant
CPM models from the training dataset were tested in an independ-
ent dataset that had no overlapping participants with the training
dataset. The participants in the validation sample consisted of 43
right-handed individuals with BD [mean ± S.D. (years) = 26.8 ±
8.9; range:18–57 years; 60.5% female]. Scanning for 34 participants
was performed on the same 3-Tesla Trio scanner and with the
same parameters as the training dataset. Scanning for nine partici-
pants was performed using a 3-Tesla Siemens PRISMA scanner
with parameters: 3-dimensional MPRAGE (TR = 2500 ms, TE =
176
2.81 ms, matrix = 256 × 256,
one-mm slices without gap), 2-dimensional T1 image (TR: 400
ms; TE: 2.61 ms; FA: 60°; matrix: 192 × 192; FOV: 220 mm × 220
mm; slice thickness: 2 mm without gap) and fMRI task (TR:
1000 ms, TE: 29.6 ms, matrix = 110 × 110, FOV: 1980mm × 1980
mm, flip angle 60, 72.2 mm slices).

FOV = 256 mm × 256 mm,

There were no significant differences in age (Independent
Samples Mann–Whitney U Test; U = 1610.5, N = 127, p = 0.3) or
gender (Chi-square Test; χ2(2127) = 0.03, p = 0.9) between the
training and the out-of-sample validation datasets. Two partici-
pants in the out-of-sample group did not have YMRS scores;
hence, predictions of YMRS scores were performed in 41 partici-
pants. Of the 43 participants, 11 had current substance abuse (2
alcohol, 1 cannabis, 1 stimulant) and dependence (4 cannabis, 3
alcohol), and 14 had fewer than four (range: 1–3) fMRI task
runs. As above, individual subject summary scores were calculated
by separately summing the significant edge weights in the positive
and negative networks which were extracted from functional con-
nectivity matrices for all participants and then entered into
regression analyses with HDRS-5 and YMRS scores.

to a limbic node (right amygdala),

The overall CPM model predicted the severity of depressed mood
(HDRS-5) (combined positive and negative networks: r = 0.23,
root mean square error (RMSE) = 3.5, pperm = 0.031; online
Supplementary Fig. S1). Investigation of the positive and negative
networks separately showed a greater contribution for the predic-
tion of depressed mood from the negative network (r = 0.36,
RMSE = 3.3, pperm < 0.001). Figure 1a, b displays negative and
positive ‘depressed mood’ networks, defined by the macroscale
regions, that significantly predicted depressed mood severity.
The high degree nodes, i.e., nodes with the most connections
(edges), in the negative network included a left PFC node located
in the dlPFC and a left motor node located in the supplementary
motor area (SMA). In predicting depressed mood severity, the left
dlPFC showed lower inter-hemispheric connections to PFC nodes
(right dlPFC and rostral PFC), lower intra-hemispheric connec-
tions to other PFC (left medial orbitofrontal cortex), limbic (left
ventral anterior cingulate cortex, vACC, and dorsal ACC,
dACC) and temporal (left inferior temporal gyrus) nodes, and
lower inter- and intra-hemispheric connections to cerebellum
nodes. The left SMA node showed lower inter-hemisphere con-
nections
intra-
hemispheric connections to other limbic (left dorsal posterior cin-
gulate cortex, dPCC), and temporal (left superior temporal gyrus)
nodes, and lower inter- and intra-hemispheric connections to
parietal (bilateral supramarginal gyrus) and motor (bilateral pri-
mary motor area) nodes. The high degree nodes in the positive
network also included left PFC and motor nodes, and as expected,
the regions of their connections differed from those of the nega-
tive network. The left prefrontal node (dlPFC) showed increased
inter-hemispheric connections to prefrontal (right ventrolateral
insular, and limbic (including right vACC and dPCC)
PFC),
nodes, increased intra-hemispheric connections to motor node
(left SMA), and increased inter- and intra-hemispheric connec-
tions to parietal nodes (bilateral supramarginal gyrus). The left
motor node (SMA) showed increased inter-hemispheric connec-
tions to the cerebellar node, increased intra-hemispheric connec-
tions to prefrontal (including left dlPFC and rostral PFC) nodes,
and increased inter- and intra-hemispheric connections to tem-
poral nodes (bilateral fusiform). The high degree nodes and
their connections in the negative and positive network, and the
respective macroscale regions they are assigned to, are detailed
in Table 1. Sensitivity analysis when the model was also controlled
for YMRS severity showed the overall CPM model still predicted
HDRS-5 severity (combined positive and negative networks: r =
0.22, pperm = 0.03); furthermore, the analysis showed no add-
itional high degree nodes.

lower

Exploratory investigation with the HDRS-29 scores revealed
that the overall CPM model predicted total HDRS-29 scores
(combined positive and negative networks: r = 0.27, pperm =
0.01). The high degree node in the left dlPFC in the negative net-
work that contributed to prediction of HDRS-5 scores was also a
high degree node that contributed to the prediction of HDRS-29
scores. Other high degree nodes contributing to HDRS-29 score
prediction in the negative and positive networks included a
node in the right dlPFC and another in the right cerebellum.
The high degree nodes and their connections in the negative
and positive network, and the respective macroscale regions
they are assigned to, are detailed in the online Supplementary sec-
tion (Table S2).

6660

Anjali Sankar et al.

Fig. 1. Negative and Positive Networks Predicting Severity of Depressed Mood using Connectome-based Predictive Modeling (CPM). (a) Circle plots in which nodes
are assigned to one of ten bilateral macroscale brain regions. Negative and positive edges (or connections between nodes) are depicted on separate plots at dif-
ferent thresholds for visualization. Threshold values indicate the minimum number of connections emanating from a node. For the negative network (connections
depicted in blue), decreased edge weights (i.e. decreased functional connectivity) predict severity of depressed mood, based on five items on the Hamilton
Depression Rating Scale that showed the highest loading for depression (i.e. depressed mood, work and interests, guilt, psychomotor retardation, and suicide).
For the positive network (in red), increased edge weights (i.e. increased functional connectivity) predict severity of depressed mood. R, right hemisphere; L, left
hemisphere. (b) Glass brain depicting strength of negative and positive networks, depicted in blue and red respectively. Each node is represented as a sphere;
the size of the sphere indicates the number of edges emanating from that node. The highest degree node, i.e., nodes with the most connections (edges), contrib-
uting to the prediction of depressed mood severity was a node located in the left dorsolateral prefrontal cortex in the negative network.

Table 1. Highest degree nodes and their connections in the positive and negative networks predictive of depressed mood severity in adults with bipolar disorder

Connections

Network

Node

Prefrontal

Insula

Limbic

Temporal

Parietal

Cerebellum

Motor

Negative

L Prefrontal (L dlPFC)

R dlPFC

L medial OFC

L/R rostral PFC

L Motor (SMA)

–

Positive

L Motor (SMA)

L dlPFC

–

–

–

–

L rostral PFC

L Fr. Eye Field

L vACC

L ITG

–

L/R Cerebellum

–

L dACC

R Amyg.

L STG

L/R SMG

–

L/R Pri. Motor

L dPCC

–

L/R Fusiform

L Angular Gyrus

R Cerebellum

–

L Prefrontal (L dlPFC)

R vlPFC

R Insula

R vACC

–

L/R SMG

–

L SMA

R dPCC

Abbreviations: L, Left Hemisphere; R, Right Hemisphere; L/R, Bilateral; PFC, Prefrontal Cortex; OFC, Orbitofrontal Cortex; dlPFC, Dorsolateral Prefrontal Cortex; vlPFC, Ventrolateral Prefrontal
Cortex; vACC, Ventral Anterior Cingulate Cortex; dACC, Dorsal Anterior Cingulate Cortex; dPCC, Dorsal Posterior Cingulate Cortex; Amg, Amygdala; Fr. Eye Field, Frontal Eye Field; SMG,
Supramarginal Gyrus, STG, Superior Temporal Gyrus; ITG, Inferior Temporal Gyrus; SMA, Supplementary Motor Area; Pri. Motor, Primary Motor.

Prediction of elevated mood severity

The overall CPM model also predicted the severity of elevated
mood (YMRS) (combined positive and negative networks: r =
0.27, RMSE = 5.8, pperm = 0.01; online Supplementary Fig. S2).
Investigation of the positive and negative networks separately

showed that
the greater contribution for the prediction of
YMRS scores was from the negative network (r = 0.25, RMSE =
5.9, pperm = 0.02). Figure 2a, b display negative and positive
YMRS networks, defined by the macroscale regions, that signifi-
cantly predicted elevated mood severity. The high degree nodes

Psychological Medicine

6661

Fig. 2. Negative and Positive Networks Predicting Severity of Elevated Mood using Connectome-based Predictive Modeling (CPM). (a) Circle plots in which nodes are
assigned to one of ten bilateral macroscale brain regions. Negative and positive edges (or connections between nodes) are depicted on separate plots at different
thresholds for visualization. Threshold values indicate the minimum number of connections emanating from a node. For the negative network (depicted in blue),
decreased edge weights (i.e. decreased functional connectivity) predict severity of elevated mood, based on the Young Mania Rating Scale. For the positive network
(in red), increased edge weights (i.e. increased functional connectivity) predict severity of elevated mood. R, right hemisphere; L, left hemisphere. (b) Glass brain
depicting strength of negative and positive networks, depicted in blue and red respectively. Each node is represented as a sphere; the size of the sphere indicates
the number of edges emanating from that node. The highest degree node, i.e., nodes with the most connections (edges), contributing to the prediction of
depressed mood severity was a node located in the left fusiform gyrus in the negative network.

in the negative network included a left temporal node located in
the fusiform gyrus, and a right occipital node located in the visual
association area. In predicting elevated mood severity, the left
temporal node (fusiform) showed lower inter-hemispheric con-
nections to occipital (right visual association area), lower intra-
hemispheric connections to motor (left SMA), and lower inter-
and intra-hemispheric connections to insular, temporal and par-
ietal nodes. The right occipital node (visual association area)
showed lower inter-hemispheric connections to occipital (left vis-
ual association area), insular, and motor (including left SMA)
nodes, and lower intra-and inter-hemispheric connections to tem-
poral (including left fusiform) and parietal nodes. The high
degree node in the positive network that predicted the severity
of elevated mood was the occipital lobe (right visual association
area), which showed increased inter-hemispheric connection to
occipital (left visual association area), increased intra-hemispheric
connections to parietal, and increased inter- and intra-hemispheric
connections to limbic (including right parahippocampal gyrus)
nodes. The high degree nodes and their connections in the negative
and positive network, and the respective macroscale regions they
are assigned to, are detailed in Table 2. Sensitivity analysis when
the model was also controlled for HDRS-5 showed the overall
CPM model still predicted YMRS severity (combined positive
and negative networks: r = 0.27, pperm = 0.01); furthermore, the
analysis showed no additional high degree nodes.

Out-of-sample validation

The CPM prediction model generated by the training model pre-
dicted HDRS-5 (r = 0.45, df = 42, p = 0.002) and YMRS (r = 0.48,
df = 40, p = 0.002) scores in the non-overlapping independent
dataset. Prediction for HDRS-5 remained significant (r = 0.45,

df = 40, p = 0.004) when the model was re-run after excluding
the two subjects who did not have YMRS scores.

Discussion

The study demonstrated that CPM, a recently developed
connectome-based machine learning approach, predicted individ-
ual differences in severity of both depressed and elevated mood
symptomatology in adults with BD using functional connectivity
networks. The study, importantly, also demonstrated that these
networks were predictive of mood symptomatology in an inde-
pendent sample of adults with BD.

CPM parsed out distributed large scale functional connectivity
networks that were predictive of depressed and elevated mood
symptom severity. The negative and positive networks that con-
tributed to depressed mood severity included dlPFC and SMA
nodes with inter- and intra-hemispheric connections predomin-
limbic, temporo-parietal and
antly to other prefrontal, motor,
cerebellar regions. No connections to nodes in the occipital cortex
were observed from the high degree nodes in either the negative
or the positive network. In contrast, the negative and positive net-
works that contributed to elevated mood severity included
fusiform and visual association area high degree nodes with
inter- and intra-hemispheric connections predominantly also to
temporo-parietal, and motor regions, as well as to insula and
occipital regions. Interestingly, unlike the ‘depressed mood’ net-
work, no connections to nodes in the PFC or cerebellum were
observed from the high degree nodes in the ‘elevated mood’ net-
work. Investigation of the negative and positive networks separ-
ately showed that the greatest contribution for the prediction of
both depressed and elevated mood was from their respective
negative networks, and hence will be the focus of the discussion.

6662

Anjali Sankar et al.

Table 2. Highest degree nodes and their connections in the positive and negative networks predictive of elevated mood severity in adults with bipolar disorder

Connections

Network

Node

Prefrontal

Insula

Limbic

Temporal

Parietal

Cerebellum

Occipital

Motor

Negative

L Temporal (Fusiform)

R Occipital (Visual Ass.)

Positive

R Occipital (Visual Ass.)

–

–

–

L/R Insula

L Insula

–

–

L/R STG

L/R SMG

R ITG

R Pri. Sensory

L/R STG

L SMG

L Fusiform R Pri. Sensory

–

R dPCC

–

R SMG

–

–

–

R Visual Ass.

L SMA

L Visual Ass.

L SMA

L Pri. Motor

L Visual Ass.

–

R Parahipp.

L vPCC

Abbreviations: L, Left Hemisphere; R, Right Hemisphere; L/R, Bilateral; vPCC, Ventral Posterior Cingulate Cortex; dPCC, Dorsal Posterior Cingulate Cortex; Parahipp, Parahippocampal Gyrus;
SMG, Supramarginal Gyrus, STG, Superior Temporal Gyrus; ITG, Inferior Temporal Gyrus; SMA, Supplementary Motor Area; Pri. Motor, Primary Motor; Pri. Sensory, Primary Somato-Sensory
Area; Visual Ass., Visual Association Area.

Depressed mood severity

CPM showed decreased functional connectivity between the left
dlPFC high degree node and the contralateral homologous region
(i.e. right dlPFC) which constituted a part of the negative network
that predicted depression severity (Table 1). The interhemispheric
dysconnectivity in this region may suggest reduced functional
coordination between both sides that could contribute to distur-
bances in the role of dlPFC in cognitive control and flexibility,
especially over affective responses, a core feature in individuals
with either unipolar or bipolar depression. Prior biological evi-
dence for the role of dlPFC in depressed mood symptomatology
has provided support for the use of this region as a target for
stimulation by neuromodulation techniques
for depression
(Beynel et al., 2014; Kazemi et al., 2018; Leyman, De Raedt,
Vanderhasselt, & Baeken, 2011; Tamas, Menkes, & El-Mallakh,
2007), although the interhemispheric observations extend beyond
current models
on intra-hemispheric dlPFC
connections.

focus

that

Also predictive of depressed mood severity was reduced con-
nectivity from the dlPFC to other anterior cortical (ventral and
rostral PFC, ventral and dorsal ACC), posterior cortical (inferior
temporal gyrus), and cerebellar regions that are implicated in vari-
ous emotion regulation processes (Braunstein, Gross, & Ochsner,
2017; Ohira et al., 2006; Phillips, Ladouceur, & Drevets, 2008a;
Schutter & van Honk, 2009; Wager, Davidson, Hughes,
Lindquist, & Ochsner, 2008) (Table 1). This finding suggests
that reduced top-down connectivity from the dlPFC to these
regions may play a role in depressed mood severity in BD.
Clinically, maladaptive regulation of emotions has been shown
to play a major role in the pathophysiology of depression
(Abravanel & Sinha, 2015). In particular, emotion dysregulation
tends to worsen mood, contribute to feelings of excessive guilt,
reduced motivated behavior, and be a risk factor for suicidal
thoughts and behaviors – all features captured by the items in
the HDRS-5 scale.

Despite psychomotor retardation being a common feature dur-
ing the depressed state of BD, very few studies have focused on the
involvement of motor areas in the pathophysiology of the disorder.
Although speculative, the lower connectivity observed between the
SMA and temporoparietal and primary motor regions might help
to explain psychomotor abnormalities of BD depression. The pre-
sent study also showed lower SMA-amygdala connectivity that was

predictive of depressed mood severity. Direct structural connec-
tions between the amygdala and the motor region have been
observed in animal models (Grèzes, Valabrègue, Gholipour, &
Chevallier, 2014) which may suggest a mechanism by which aber-
rant signals from the amygdala may influence complex motor
behavior in BD depression. Further in-depth studies are required
to confirm the involvement of SMA in the psychomotor abnormal-
ities of BD depression. Notwithstanding, the pattern of connections
in the ‘depressed mood symptom network’ suggests that disrup-
tions in brain networks associated with cognitive control and flexi-
bility, emotion regulation, and psychomotor functioning predict
depressed mood severity.

Elevated mood severity

The present study showed that more posterior cortical regions, i.e.,
the left fusiform and the right visual association area comprised
the high degree nodes that predicted elevated mood severity.
While the fusiform and the visual association are both important
for processing visual stimuli, the fusiform has specialized roles in
recognizing faces as well as facial expressions (Ganel, Valyear,
Goshen-Gottstein, & Goodale, 2005; Hadjikhani & de Gelder,
2003). Decreased connectivity between the fusiform and brain
areas such as the insula and somatosensory areas, which are regions
important in the detection of salient stimuli (Uddin, 2015) and
social perceptual processes, respectively, may be suggestive of the
involvement of brain networks that underlie impairments in recog-
nizing salient social cues in elevated mood states. Decreased con-
nectivity was also observed between the fusiform gyrus and motor
areas (primary motor and SMA), regions that are involved in
motor behavior and are influenced by visual cues (Oliveri et al.,
2003; Rodigari & Oliveri, 2014). Although speculative, the pattern
of connections in the ‘elevated mood symptom network’ implies def-
icits in social perceptual functions which may contribute to social
disinhibition, high levels of motor activity, and other disinhibited
behavior typically observed in individuals with elevated mood.
The dysconnectivity between the visual face processing and salient
network nodes in the prediction of elevated mood severity suggests
that the emotional face paradigm may have helped to amplify indi-
vidual differences in predictive networks in the present study. Future
is, however,
work with emotional facial and non-facial stimuli
required to confirm this theory.

Psychological Medicine

6663

The above findings should be considered preliminary as fur-
ther testing using larger samples (∼1000) is needed to reduce
the risk of machine learning performance misestimation (Flint
et al., 2021), and as the predictive networks were tested in an inde-
pendent sample of fewer than 50 individuals. Furthermore, the
concordance rates between the actual and predicted mood severity
scores in our study were modest. This may be because the clinical
and underlying neurobiological heterogeneity in the sample is not
adequately captured by the mood rating scales. The concordance
rates, however, are in line with previous studies using CPM to pre-
individual behaviors (Ju et al., 2020; Lin et al., 2022;
dict
Rutherford, Potenza, Mayes, & Scheinost, 2020; Wang et al.,
2021).The aforementioned clinical heterogeneity in the sample
is another limitation of the study. This sample included partici-
pants who were either BD-I or BD-II,
in different phases of
their illness (including mixed states), and had varied psychiatric
comorbidities. For instance, deficits in brain regions subserving
social perceptual
functions observed in relation to elevated
mood symptom severity have previously been observed in indivi-
duals with post-traumatic stress disorder (PTSD) (Stevens &
Jovanovic, 2019), and 20% of the current sample had comorbid
PTSD. Two-thirds of the BD participants were on different com-
binations of psychiatric medications. There have been reports of
effects of psychiatric medications on the brain regions involved
in this study. Prior reviews support the view that psychotropic
medications have a normalizing effect on brain function, rather
than brain differences observed in BD being the result of psycho-
tropic medications
(Hafeman, Chang, Garrett, Sanders, &
Phillips, 2012; Phillips, Travis, Fagiolini, & Kupfer, 2008b).
Lastly, the predictive networks may be specific to the HDRS-5
and YMRS scales that were used to measure depressed and ele-
vated mood symptom severity in this study. For example, the cere-
bellum appeared as a high degree node in the analyses of
depression severity, when the HDRS 29-item version was used.

Conclusions

The study demonstrates that distributed connectivity networks
could be identified using CPM that predicted individual differ-
ences in depressed and elevated mood severity in adults with
BD. Importantly, these networks were predictive of mood symp-
tomatology in an independent and heterogenous sample of adults
with BD. Data demonstrate that connectivity differences in net-
works subserving emotion regulation, cognitive, and psychomotor
function predict depressed mood severity, while connectivity dif-
ferences in networks subserving social perceptual functions pre-
dict elevated mood severity. These connectome fingerprints may
be biomarkers for targeted therapeutic approaches to reduce
depressed and elevated mood symptoms in individuals with BD.

Supplementary material. The supplementary material for this article can
be found at https://doi.org/10.1017/S003329172300003X

Financial support. This work was supported by grants from the National
Institutes of Mental Health RC1MH088366, R01MH69747, R01MH070902,
R01MH113230, R61MH111929 (HPB), R24MH114805 (DS), R01MH121095
Sciences
(DS, RTC), National Center
TL1TR001864 (DAG, RTC, HPB), AIM Youth Mental Health Foundation,
Klingenstein Third Generation Foundation (AS),
the Interdisciplinary
Center of Clinical Research of the Medical Faculty Jena (LC), American
Foundation for Suicide Prevention, International Bipolar Foundation, MQ
Brighter Futures Program, For the Love of Travis Foundation, the Boehm
Family Foundation and the John and Hope Furth Endowment and the (HPB).

for Advancing Translational

Conflict of interest. Dr Blumberg has consulted to the Milken Institute. All
other authors report no financial relationships with commercial interests.

References

Abi-Dargham, A., & Horga, G. (2016). The search for imaging biomarkers in

psychiatric disorders. Nature Medicine, 22(11), 1248.

Abravanel, B. T., & Sinha, R. (2015). Emotion dysregulation mediates the rela-
tionship between lifetime cumulative adversity and depressive symptom-
atology. Journal of Psychiatric Research, 61, 89–96.

Adleman, N. E., Kayser, R. R., Olsavsky, A. K., Bones, B. L., Muhrer, E. J.,
Fromm, S. J., … Brotman, M. A. (2013a). Abnormal fusiform activation
during emotional-face encoding assessed with functional magnetic reson-
ance imaging. Psychiatry Research: Neuroimaging, 212(2), 161–163.

Adleman, N. E., Kayser, R. R., Olsavsky, A. K., Bones, B. L., Muhrer, E. J.,
Fromm, S. J., … Brotman, M. A. (2013b). Abnormal fusiform activation
during emotional-face encoding in children and adults with bipolar dis-
order. Psychiatry Research, 212(2), 161.

Altshuler, L., Bookheimer, S., Townsend, J., Proenza, M. A., Sabb, F., Mintz, J.,
& Cohen, M. S. (2008). Regional brain changes in bipolar I depression: A
functional magnetic resonance imaging study. Bipolar Disorders, 10(6),
708–717.

Barron, D. S., Gao, S., Dadashkarimi, J., Greene, A. S., Spann, M. N., Noble, S.,
… Scheinost, D. (2019). Task-Based Functional Connectomes Predict
Cognitive Phenotypes Across Psychiatric Disease. bioRxiv, 638825.

Bertocci, M. A., Bergman, J., Santos, J. P. L., Iyengar, S., Bonar, L., Gill, M. K.,
… Lockovich, J. (2020). Emotional regulation neural circuitry abnormalities
in adult bipolar disorder: Dissociating effects of long-term depression his-
tory from relationships with present symptoms. Translational Psychiatry,
10(1), 1–9.

Beynel, L., Chauvin, A., Guyader, N., Harquel, S., Szekely, D., Bougerol, T., &
(2014). What saccadic eye movements tell us about
Marendaz, C.
TMS-induced neuromodulation of the DLPFC and mood changes: A
pilot study in bipolar disorders. Frontiers in Integrative Neuroscience, 8, 65.
Blond, B. N., & Blumberg, H. P. (2010). Functional neuroimaging research in
bipolar disorder. Behavioral Neurobiology of Bipolar Disorder and its
Treatment, 5, 227–245.

Blumberg, H. P., Leung, H.-C., Skudlarski, P., Lacadie, C. M., Fredericks, C. A.,
Harris, B. C., … Peterson, B. S. (2003). A functional magnetic resonance
imaging study of bipolar disorder: State-and trait-related dysfunction in
ventral prefrontal cortices. Archives of General Psychiatry, 60(6), 601–609.
Blumberg, H. P., Stern, E., Ricketts, S., Martinez, D., de Asis, J., White, T., …
Kemperman, I. (1999). Rostral and orbital prefrontal cortex dysfunction in
the manic state of bipolar disorder. American Journal of Psychiatry, 156(12),
1986–1988.

Braunstein, L. M., Gross, J. J., & Ochsner, K. N. (2017). Explicit and implicit
emotion regulation: A multi-level framework. Social Cognitive and Affective
Neuroscience, 12(10), 1545–1557. doi: 10.1093/scan/nsx096

Brooks III, J. O., Wang, P. W., Bonner, J. C., Rosen, A. C., Hoblyn, J. C., Hill, S.
J., & Ketter, T. A. (2009). Decreased prefrontal, anterior cingulate, insula,
and ventral striatal metabolism in medication-free depressed outpatients
with bipolar disorder. Journal of Psychiatric Research, 43(3), 181–188.
Buckner, R. L., Krienen, F. M., Castellanos, A., Diaz, J. C., & Yeo, B. T. (2011).
The organization of the human cerebellum estimated by intrinsic functional
connectivity. Journal of Neurophysiology, 106(5), 2322–2345.

Cai, H., Zhu, J., & Yu, Y. (2020). Robust prediction of individual personality
connectome. Social Cognitive and Affective

from brain functional
Neuroscience, 15(3), 359–369.

Cerullo, M. A., Fleck, D. E., Eliassen, J. C., Smith, M. S., DelBello, M. P., Adler,
C. M., & Strakowski, S. M. (2012). A longitudinal functional connectivity
analysis of the amygdala in bipolar I disorder across mood states. Bipolar
Disorders, 14(2), 175–184. doi: 10.1111/j.1399-5618.2012.01002.x

Double, D. (1990). The factor structure of manic rating scales. Journal of

Affective Disorders, 18(2), 113–119.

Elliott, R., Ogilvie, A., Rubinsztein, J. S., Calderon, G., Dolan, R. J., & Sahakian,
B. J. (2004). Abnormal ventral frontal response during performance of an
affective go/no go task in patients with mania. Biological Psychiatry, 55
(12), 1163–1170.

6664

Anjali Sankar et al.

Fan, S., Nemati, S., Akiki, T. J., Roscoe, J., Averill, C. L., Fouda, S., … Abdallah, C.
G. (2020). Pretreatment brain connectome fingerprint predicts treatment
response in major depressive disorder. Chronic Stress, 4, 2470547020984726.
Fernández-Corcuera, P., Salvador, R., Monté, G. C., Sarró, S. S., Goikolea, J. M.,
Amann, B., … Vieta, E. (2013). Bipolar depressed patients show both failure
to activate and failure to de-activate during performance of a working mem-
ory task. Journal of Affective Disorders, 148(2–3), 170–178.

Finn, E. S., Shen, X., Scheinost, D., Rosenberg, M. D., Huang, J., Chun, M. M.,
… Constable, R. T.
(2015). Functional connectome fingerprinting:
Identifying individuals using patterns of brain connectivity. Nature
Neuroscience, 18(11), 1664.

First, M. B. (2014). Structured clinical interview for the DSM (SCID). The

Encyclopedia of Clinical Psychology, 1–6.

Flint, C., Cearns, M., Opel, N., Redlich, R., Mehler, D. M., Emden, D., …
Kircher, T. (2021). Systematic misestimation of machine learning perform-
ance in neuroimaging studies of depression. Neuropsychopharmacology,
46(8), 1510–1517.

Ganel, T., Valyear, K. F., Goshen-Gottstein, Y., & Goodale, M. A. (2005). The
involvement of the “fusiform face area” in processing facial expression.
Neuropsychologia, 43(11), 1645–1654.

Goldman, D. A., Sankar, A., Rich, A., Kim, J. A., Pittman, B., Constable, R. T.,
… Blumberg, H. P. (2022). A graph theory neuroimaging approach to dis-
tinguish the depression of bipolar disorder from major depressive disorder
in adolescents and young adults. Journal of Affective Disorders, 319, 15–26.
Greene, A. S., Gao, S., Scheinost, D., & Constable, R. T. (2018). Task-induced
brain state manipulation improves prediction of individual traits. Nature
Communications, 9(1), 1–13.

Grèzes, J., Valabrègue, R., Gholipour, B., & Chevallier, C. (2014). A direct
amygdala-motor pathway for emotional displays to influence action: A dif-
fusion tensor imaging study. Human Brain Mapping, 35(12), 5974–5983.
doi: 10.1002/hbm.22598

Hadjikhani, N., & de Gelder, B. (2003). Seeing fearful body expressions
activates the fusiform cortex and amygdala. Current Biology, 13(24),
2201–2205.

Hafeman, D. M., Chang, K. D., Garrett, A. S., Sanders, E. M., & Phillips, M. L.
(2012). Effects of medication on neuroimaging findings in bipolar disorder:
An updated review. Bipolar Disorders, 14(4), 375–410.

Hahn, T., Nierenberg, A. A., & Whitfield-Gabrieli, S. (2017). Predictive analy-
tics in mental health: Applications, guidelines, challenges and perspectives.
Molecular Psychiatry, 22(1), 37–43.

Horien, C., Shen, X., Scheinost, D., & Constable, R. T. (2019). The individual
functional connectome is unique and stable over months to years.
Neuroimage, 189, 676–687.

Hsu, W.-T., Rosenberg, M. D., Scheinost, D., Constable, R. T., & Chun, M. M.
(2018). Resting-state functional connectivity predicts neuroticism and extra-
version in novel individuals. Social Cognitive and Affective Neuroscience, 13
(2), 224–232.

Johnston, J. A. Y., Wang, F., Liu, J., Blond, B. N., Wallace, A., Liu, J., …
Blumberg, H. P. (2017). Multimodal neuroimaging of frontolimbic structure
and function associated with suicide attempts in adolescents and young
adults with bipolar disorder. American Journal of Psychiatry, 174(7), 667–
675. doi: 10.1176/appi.ajp.2016.15050652

Ju, Y., Horien, C., Chen, W., Guo, W., Lu, X., Sun, J., … Yan, D. (2020).
Connectome-based models can predict early symptom improvement in
major depressive disorder. Journal of Affective Disorders, 273, 442–452.
Judd, L. L., Akiskal, H. S., Schettler, P. J., Endicott, J., Leon, A. C., Solomon, D.
A., … Keller, M. B. (2005). Psychosocial disability in the course of bipolar I
and II disorders: A prospective, comparative, longitudinal study. Archives of
General Psychiatry, 62(12), 1322–1330.

Kazemi, R., Rostami, R., Khomami, S., Baghdadi, G., Rezaei, M., Hata, M., …
Fitzgerald, P. B. (2018). Bilateral transcranial magnetic stimulation on
DLPFC changes resting state networks and cognitive function in patients
with bipolar depression. Frontiers in Human Neuroscience, 12, 356.

Ketter, T. A., Kimbrell, T. A., George, M. S., Dunn, R. T., Speer, A. M., Benson,
B. E., … Herscovitch, P. (2001). Effects of mood and subtype on cerebral
glucose metabolism in treatment-resistant bipolar disorder. Biological
Psychiatry, 49(2), 97–109.

Koenigs, M., & Grafman, J. (2009). The functional neuroanatomy of depres-
sion: Distinct roles for ventromedial and dorsolateral prefrontal cortex.
Behavioural Brain Research, 201(2), 239–243.

Lacadie, C. M., Fulbright, R. K., Rajeevan, N., Constable, R. T., &
Papademetris, X. (2008). More accurate Talairach coordinates for neuroi-
maging using non-linear registration. Neuroimage, 42(2), 717–725.

Leyman, L., De Raedt, R., Vanderhasselt, M. A., & Baeken, C. (2011). Effects of
repetitive transcranial magnetic stimulation of the dorsolateral prefrontal
cortex on the attentional processing of emotional information in major
depression: A pilot study. Psychiatry Research, 185(1–2), 102–107. doi:
10.1016/j.psychres.2009.04.008

Li, M., Huang, C., Deng, W., Ma, X., Han, Y., Wang, Q., … Li, T. (2015).
Contrasting and convergent patterns of amygdala connectivity in mania
and depression: A resting-state study. Journal of Affective Disorders, 173,
53–58. doi: 10.1016/j.jad.2014.10.044

Lin, X., Zhu, X., Zhou, W., Zhang, Z., Li, P., Dong, G., … Lu, L. (2022).
Connectome-based predictive modelling of smoking severity in smokers.
Addiction Biology, 27(6), e13242.

Liu, J., Blond, B. N., van Dyck, L. I., Spencer, L., Wang, F., & Blumberg, H. P.
(2012). Trait and state corticostriatal dysfunction in bipolar disorder during
emotional face processing. Bipolar Disorders, 14(4), 432–441. doi: 10.1111/
j.1399-5618.2012.01018.x

Luo, X., Chen, G., Jia, Y., Gong, J., Qiu, S., Zhong, S., … Qi, Z. (2018).
Disrupted cerebellar connectivity with the central executive network and
the default-mode network in unmedicated bipolar II disorder. Frontiers
in Psychiatry, 9, 705.

Manelis, A., Stiffler, R., Lockovich, J. C., Almeida, J. R., Aslam, H. A., &
Phillips, M. L. (2019). Longitudinal changes in brain activation during
anticipation of monetary loss in bipolar disorder. Psychological Medicine,
49(16), 2781–2788.

Ohira, H., Nomura, M., Ichikawa, N., Isowa, T., Iidaka, T., Sato, A., …
Yamada, J. (2006). Association of neural and physiological responses during
voluntary emotion suppression. Neuroimage, 29(3), 721–733.

Oliveri, M., Babiloni, C., Filippi, M., Caltagirone, C., Babiloni, F., Cicinelli, P.,
… Rossini, P. (2003). Influence of the supplementary motor area on pri-
mary motor cortex excitability during movements triggered by neutral or
emotionally unpleasant visual cues. Experimental Brain Research, 149(2),
214–221.

Öngür, D., Lundy, M., Greenhouse, I., Shinn, A. K., Menon, V., Cohen, B. M.,
& Renshaw, P. F. (2010). Default mode network abnormalities in bipolar
disorder and schizophrenia. Psychiatry Research: Neuroimaging, 183(1),
59–68.

Orrù, G., Monaro, M., Conversano, C., Gemignani, A., & Sartori, G. (2020).
Machine learning in psychometrics and psychological research. Frontiers
in Psychology, 10, 2970.

Orru, G., Pettersson-Yeo, W., Marquand, A. F., Sartori, G., & Mechelli, A.
(2012). Using support vector machine to identify imaging biomarkers of
neurological and psychiatric disease: A critical review. Neuroscience &
Biobehavioral Reviews, 36(4), 1140–1152.

Phillips, M. L., Ladouceur, C. D., & Drevets, W. C. (2008a). A neural model of
voluntary and automatic emotion regulation: Implications for understand-
ing the pathophysiology and neurodevelopment of bipolar disorder.
Molecular Psychiatry, 13(9), 833.

Phillips, M. L., Travis, M. J., Fagiolini, A., & Kupfer, D. J. (2008b). Medication
effects in neuroimaging studies of bipolar disorder. American Journal of
Psychiatry, 165(3), 313–320.

Rodigari, A., & Oliveri, M. (2014). Disrupting SMA activity modulates explicit
and implicit emotional responses: An rTMS study. Neuroscience Letters,
579, 30–34.

Rosenberg, M. D., Finn, E. S., Scheinost, D., Papademetris, X., Shen, X.,
Constable, R. T., & Chun, M. M. (2016). A neuromarker of sustained
attention from whole-brain functional connectivity. Nature Neuroscience,
19(1), 165.

Rosenberg, M. D., Hsu, W.-T., Scheinost, D., Todd Constable, R., & Chun, M.
M. (2018). Connectome-based models predict separable components of
attention in novel individuals. Journal of Cognitive Neuroscience, 30(2),
160–173.

Psychological Medicine

6665

Rutherford, H. J., Potenza, M. N., Mayes, L. C., & Scheinost, D. (2020). The
application of connectome-based predictive modeling to the maternal
brain: Implications for mother–infant bonding. Cerebral Cortex, 30(3),
1538–1547.

Sankar, A., Purves, K., Colic, L., Lippard, E. T. C., Millard, H., Fan, S., …
Constable, R. T. (2020). Altered frontal cortex functioning in emotion regula-
tion and hopelessness in bipolar disorder. Bipolar Disorders, 23(2), 152–164.
Scheinost, D., Kwon, S. H., Lacadie, C., Vohr, B. R., Schneider, K. C.,
Papademetris, X., … Ment, L. R. (2017). Alterations in anatomical covari-
ance in the prematurely born. Cerebral Cortex, 27(1), 534–543.

Scheinost, D., Papademetris, X., & Constable, R. T. (2014). The impact of
image smoothness on intrinsic functional connectivity and head motion
confounds. Neuroimage, 95, 13–21.

Serrano, E., Ezpeleta, L., Alda,

Schutter, D. J., & van Honk, J. (2009). The cerebellum in emotion regulation: A
repetitive transcranial magnetic stimulation study. The Cerebellum, 8(1), 28–34.
J. L., & San, L. (2011).
Psychometric properties of the Young Mania Rating Scale for the identifi-
cation of mania symptoms in Spanish children and adolescents with atten-
tion deficit/hyperactivity disorder. Psychopathology, 44(2), 125–132.

J. A., Matalí,

Shen, X., Finn, E. S., Scheinost, D., Rosenberg, M. D., Chun, M. M.,
Papademetris, X., & Constable, R. T. (2017). Using connectome-based pre-
dictive modeling to predict individual behavior from brain connectivity.
Nature Protocols, 12(3), 506.

Tamas, R. L., Menkes, D., & El-Mallakh, R. S. (2007). Stimulating research: A
prospective, randomized, double-blind, sham-controlled study of slow tran-
scranial magnetic stimulation in depressed bipolar patients. The Journal of
Neuropsychiatry and Clinical Neurosciences, 19(2), 198–199.

Uddin, L. Q. (2015). Salience processing and insular cortical function and dys-

function. Nature Reviews Neuroscience, 16(1), 55–61.

Wager, T. D., Davidson, M. L., Hughes, B. L., Lindquist, M. A., & Ochsner, K.
N. (2008). Prefrontal-subcortical pathways mediating successful emotion
regulation. Neuron, 59(6), 1037–1050.

Walter, M., Alizadeh, S., Jamalabadi, H., Lueken, U., Dannlowski, U., Walter,
H., … Koutsouleris, N. (2019). Translational machine learning for psychi-
atric neuroimaging. Progress in Neuro-Psychopharmacology and Biological
Psychiatry, 91, 113–121.

Wang, F., Bobrow, L., Liu, J., Spencer, L., & Blumberg, H. P. (2012).
Corticolimbic functional connectivity in adolescents with bipolar disorder.
PloS one, 7(11), e50177.

Wang, Z., Goerlich, K. S., Ai, H., Aleman, A., Luo, Y.-J., & Xu, P. (2021).
individual anxiety. Cerebral

Connectome-based predictive modeling of
Cortex, 31(6), 3006–3020.

Williams, J., Link, M., Rosenthal, N., & Terman, M. (1988). Structured
Interview Guide for the Hamilton Depression Rating Scale – Seasonal
Affective Disorder Version (SIGH-SAD). In: New York State Psychiatric
Institute, New York.

Shen, X., Papademetris, X., & Constable, R. T. (2010). Graph-theory based par-
cellation of functional subunits in the brain from resting-state fMRI data.
Neuroimage, 50(3), 1027–1035.

Yip, S. W., Scheinost, D., Potenza, M. N., & Carroll, K. M. (2019).
Connectome-based prediction of cocaine abstinence. American Journal of
Psychiatry, 176(2), 156–164.

Song, K. R., Potenza, M. N., Fang, X. Y., Gong, G. L., Yao, Y. W., Wang, Z. L.,
… Lan, J. (2020). Resting-state connectome-based support-vector-machine
predictive modeling of internet gaming disorder. Addiction Biology, 26(4),
e12969.

Stevens, J. S., & Jovanovic, T. (2019). Role of social cognition in post-traumatic
stress disorder: A review and meta-analysis. Genes, Brain and Behavior,
18(1), e12518.

Strakowski, S. M., Eliassen, J. C., Lamy, M., Cerullo, M. A., Allendorfer, J. B.,
Madore, M., … Fleck, D. E. (2011). Functional magnetic resonance imaging
brain activation in bipolar mania: Evidence for disruption of the ventrolateral
prefrontal-amygdala emotional pathway. Biological Psychiatry, 69(4), 381–388.

Young, R., Biggs, J., Ziegler, V., & Meyer, D. (1978). A rating scale for mania:
Reliability, validity and sensitivity. The British Journal of Psychiatry, 133(5),
429–435.

Youngstrom, E. A., Kmett Danielson, C., Findling, R. L., Gracious, B. L., &
Calabrese, J. R. (2002). Factor structure of the Young Mania Rating Scale
for use with youths ages 5 to 17 years. Journal of Clinical Child and
Adolescent Psychology, 31(4), 567–572.

Zhang, L., Li, W., Wang, L., Bai, T., Ji, G.-J., Wang, K., & Tian, Y. (2020).
Altered functional connectivity of right inferior frontal gyrus subregions
in bipolar disorder: A resting state fMRI study.
Journal of Affective
Disorders, 272, 58–65.
