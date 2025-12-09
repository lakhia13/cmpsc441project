# Song_2024_Causal dynamics of sleep, circadian rhythm, and mood symptoms in patients with major depression and bipolar disorder insights from longitudinal wearable device data.

Articles

Causal dynamics of sleep, circadian rhythm, and mood
symptoms in patients with major depression and bipolar
disorder: insights from longitudinal wearable device data

Yun Min Song,a,b,g Jaegwon Jeong,c,d,g Aurelio A. de los Reyes, Vb,e,g Dongju Lim,a,b Chul-Hyun Cho,c,d Ji Won Yeom,c,d Taek Lee,f Jung-Been Lee,f
Heon-Jeong Lee,c,d,∗

and Jae Kyoung Kima,b,∗∗

aDepartment of Mathematical Sciences, KAIST, Daejeon, 34141, Republic of Korea
bBiomedical Mathematics Group, Pioneer Research Center for Mathematical and Computational Sciences, Institute for Basic Science,
Daejeon, 34126, Republic of Korea
cDepartment of Psychiatry, Korea University College of Medicine, Seoul, 02841, Republic of Korea
dChronobiology Institute, Korea University, Seoul, 02841, Republic of Korea
eInstitute of Mathematics, University of the Philippines Diliman, Quezon City, 1101, Philippines
fDivision of Computer Science and Engineering, Sun Moon University, Asan, 31460, Republic of Korea

Summary
Background Sleep and circadian rhythm disruptions are common in patients with mood disorders. The intricate
relationship between these disruptions and mood has been investigated, but their causal dynamics remain unknown.

Methods We analysed data from 139 patients (76 female, mean age = 23.5 ± 3.64 years) with mood disorders who
participated in a prospective observational study in South Korea. The patients wore wearable devices to monitor sleep
and engaged in smartphone-delivered ecological momentary assessment of mood symptoms. Using a mathematical
model, we estimated their daily circadian phase based on sleep data. Subsequently, we obtained daily time series for
sleep/circadian phase estimates and mood symptoms spanning >40,000 days. We analysed the causal relationship
between the time series using transfer entropy, a non-linear causal inference method.

eBioMedicine
2024;103: 105094

Published Online xxx
https://doi.org/10.
1016/j.ebiom.2024.
105094

Findings The transfer entropy analysis suggested causality from circadian phase disturbance to mood symptoms in
both patients with MDD (n = 45) and BD type I (n = 35), as 66.7% and 85.7% of the patients with a large dataset (>600
days) showed causality, but not in patients with BD type II (n = 59). Surprisingly, no causal relationship was sug-
gested between sleep phase disturbances and mood symptoms.

Interpretation Our ﬁndings suggest that in patients with mood disorders, circadian phase disturbances directly
precede mood symptoms. This underscores the potential of targeting circadian rhythms in digital medicine, such as
sleep or light exposure interventions, to restore circadian phase and thereby manage mood disorders effectively.

Funding Institute for Basic Science, the Human Frontiers Science Program Organization, the National Research
Foundation of Korea, and the Ministry of Health & Welfare of South Korea.

Copyright © 2024 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND
license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

Keywords: Major depressive disorder; Bipolar disorder; Circadian rhythm; Sleep; Mathematical modelling; Causality

Introduction
Sleep and circadian rhythm are tightly intertwined,1 and
their disruptions are commonly observed in patients
with major depressive disorder (MDD) and bipolar dis-
order (BD).2 For instance, during depressive episodes in
both patients with MDD and those with BD, insomnia

or hypersomnia is prevalent,3,4 while a reduced need for
sleep is a prominent feature of manic and hypomanic
episodes.5,6 Patients with MDD typically have lower
amplitude on circadian rhythms of locomotor activity,
body temperature, norepinephrine, thyroid stimulating
hormone,
Furthermore,

and melatonin

levels.7,8

*Corresponding author. Department of Psychiatry, Anam Hospital, Korea University College of Medicine, 73 Goryeodae-ro, Seongbuk-gu, Seoul,
02841, Republic of Korea.
**Corresponding author. Department of Mathematical Sciences, KAIST, 291 Daehak-ro, Yuseong-gu, Daejeon, 34141, Republic of Korea.

E-mail addresses: leehjeong@korea.ac.kr (H.-J. Lee), jaekkim@kaist.ac.kr (J.K. Kim).

gThese authors contributed equally.

www.thelancet.com Vol 103 May, 2024

1

Articles

Research in context

Evidence before this study
We searched PubMed for studies on September 15, 2023,
using the search (“mood disorder” [Title] OR “depression”
[title] OR “bipolar” [title]) AND (“circadian rhythm” OR
“circadian” OR “chronobiology” OR “chronobiological”). While
prior studies suggest a robust association between circadian
rhythms and mood disorders, the precise role of circadian
systems in relation to mood disorders remains unclear.
Among various aspects of circadian rhythms, circadian phase
is notably recognised for its substantial impact on mood
disorders. Earlier research has indicated a strong association
between delayed sleep phases and late chronotype with mood
disorders. Recent investigations have explored individual
sleep-wake patterns and their impact on the course of mood
disorders using wearable devices. However, these studies have
often failed to consider internal circadian rhythms fully. In a
noteworthy study that measured rhythms of circadian gene
expression and salivary cortisol, patients with bipolar disorder
exhibited 4–5 h delayed rhythms during their depressive
episodes and 7 h advanced rhythms (equivocal to 17 h
delayed) during manic episodes. Notably, these rhythms were
normalised following the treatment of mood episodes.
Nevertheless, our understanding of the direction of the causal
relationship between changes in circadian phase and
individual mood at the personal level remains limited.

Added value of this study
We analysed causal relationships between real-world time
series data of sleep/circadian phase estimates and mood
symptoms, encompassing an average of 290 days. The
acquisition of such extensive real-world data was possible by
introducing a mathematical model for circadian phase

estimation, as well as through advancements in wearable
devices and smartphones. This extended dataset enabled
robust causality analysis based on transfer entropy, a method
capable of capturing non-linear relationships overlooked by
conventional approaches like Granger causality. Our ﬁndings
unveiled a crucial distinction: It was not sleep but circadian
phase disruptions that preceded variations in mood
symptoms among individuals with MDD and BDI.
Furthermore, exploring the dynamic disparities between sleep
and circadian phases provided insights into the complex
causal dynamics, thus deepening our comprehension of the
intricate interplay among sleep, circadian rhythms, and mood
disorders.

Implications of all the available evidence
This study explores the complex interplay between sleep
disturbances, circadian rhythms, and mood disorders,
shedding light on the challenging task of establishing
evidence in support of causality. We have elucidated the
evidence supporting a causal relationship, aligning with
the accumulating body of research in this area. Moreover, the
methodology employed to achieve this breakthrough,
harnessing mobile apps, wearable technology, and a
mathematical model, represents a signiﬁcant advancement in
the real-time assessment of mood episode risks. This, in turn,
holds promise for timely interventions focused on regulating
circadian rhythms. Such interventions could usher in an
innovative approach to the treatment of mood disorders,
distinguishing them from conventional digital therapeutics
that primarily offer standardised forms of behavioural
therapy.

abnormalities in the peak time and amount of mela-
tonin secretion have been observed in patients with
BD.9–12 Additionally, genetic evidence points to a strong
relationship between susceptibility to mood disorders
and circadian genes, such as CLOCK and TIM.13,14

Among the various types of sleep and circadian dis-
turbances, phase disturbances are gaining attention in
relation to mood disorders. For instance, social jetlag,
determined by the difference between mid-sleep time
during weekdays and weekends, positively correlated
with depressive symptoms.15 Both patients with MDD
and BD often exhibit a preference for an evening chro-
notype.16,17 Phase angle difference between the circadian
phase and desired bedtime was associated with
depressive severity in individuals with delayed sleep-
wake phase disorder.18 In seasonal affective disorder,
phase delay in circadian rhythms was associated with
depression.19–21 Similar associations between circadian
misalignment and depression severity have been
observed in non-seasonal depression.22 Furthermore,
circadian phase advancement in acute manic episodes

and circadian phase delay in acute mixed and depressive
episodes were reported among patients with BD.23
These circadian phase changes were normalised after
treating the patients with BD. While strong associations
between mood disorders and disturbances in sleep and
circadian phases have been found, the causal relation-
ship between these disturbances and mood remains
elusive24–27
(Fig. 1). For instance, sleep or circadian
phase disruptions could lead to mood disturbances, or it
could be the other way around.

While the causal relationship between circadian/
sleep phase disturbance and mood can be inferred from
their temporal sequences,28
their longitudinal moni-
toring has rarely been performed in existing studies.
Fortunately, the widespread usage of smartphones and
facilitated the collection of
wearable devices has
continuous sleep and mood information over extended
periods during longitudinal studies.29,30 However, unlike
the sleep phase, direct measurement of the circadian
phase in humans is costly and possible only under
limited conditions, making it nearly impossible to

2

www.thelancet.com Vol 103 May, 2024

Articles

mhtyhRnaidacriC

nrettaPekaW-peelS

Mood Disorder

?

?

Fig. 1: Causal relationships between sleep or circadian phase disturbance and mood disorders remain unclear. Sleep and circadian phase
disturbances are associated with feeling depressed, lack of interest, tiredness, poor concentration and irritability, contributing to the devel-
opment of mood disorders such as depression and bipolar disorder. However, the details of the causation between these factors are not yet fully
In particular, sleep-wake cycle disturbance may directly contribute to mood variations of patients with mood disorders or
understood.
contribute indirectly through circadian phase disturbance. Conversely, mood variations themselves may disturb sleep and/or circadian phase.

acquire long-term time series data.31 An alternative
approach is indirectly estimating the circadian phase
with mathematical models and wearable devices.32–35
These models describe how the circadian rhythm
responds to light exposure. Applying these models to
light exposure data continuously obtained or inferred
from wearable devices makes it possible to simulate the
long-term evolution of the circadian rhythm, thereby
generating a time series of the long-term estimates of
circadian phase. Among currently known computational
approaches in ﬁeld settings, such as multiple regression
models and artiﬁcial neural network models,
this
approach is considered the most effective36 and has been
widely accepted in various studies to track circadian
dynamics.32,36–40

Previous studies have explored the temporal associ-
ation and causal relationship between sleep and mood
states using autoregressive models or Granger causal-
ity.41,42 However,
these approaches assume a linear
relationship between the time series,28 which may not be
suitable when considering mood states such as depres-
sive, elevated, and mixed moods. To better understand
their causal dynamics, employing a non-linear causal
inference method such as transfer entropy (TE)
is
essential.43,44 TE quantiﬁes the reduction in uncertainty
when predicting the future state of one process based on
the knowledge of the current and past states of another
process. As a deliberately asymmetric measure, TE is
frequently employed to deduce the directionality of in-
causal
formation

ﬂow and,

consequently,

the

relationship between the two processes.28,45 TE has been
proposed as an effective tool for investigating causality
within complex systems, especially in computational
neuroscience,44,46–48 and in physiological systems such as
cardiorespiratory interactions.49–53 In particular, TE has
also been employed to analyse electroencephalogram
signals in individuals with mood disorders.54–56

In this study, we aimed to elucidate the direction of
causality between circadian/sleep phase disturbances
and mood symptoms in patients with mood disorders.
We collected information on sleep and subjective mood
symptoms over several hundred days using wearable
devices and mobile applications. In addition, using a
mathematical model, we estimated the daily circadian
phase based on the collected sleep data, which indirectly
informs the light exposure of patients. This process
allowed us to extract time series data of circadian and
sleep phase estimates as well as mood symptoms, with
an average length of 290 days, from 139 patients with
mood disorders. Subsequently, we performed causal
inference between these time series using TE, which
enabled us to consider
the non-linear nature of
depressive, elevated, and mixed moods. The analysis
suggested causality from circadian phase disturbance to
mood symptoms in patients with MDD and BD type I
(BDI) but not
in patients with BD type II (BDII).
However, no causal relationship was suggested between
sleep phase disturbance and mood symptoms. Our
ﬁndings propose that in patients with mood disorders, it
is not the sleep phase disturbances but the circadian

www.thelancet.com Vol 103 May, 2024

3

Articles

symptoms.

phase disturbance that directly precedes variations in
mood
circadian phase
Furthermore,
disruption could trigger the relapse of mood episodes
and, therefore, is a potential target of mood disorder
treatment.

Methods
Recruitment
The data used in this study were collected from the
Mood Disorder Cohort
Research Consortium
(MDCRC), a multicenter prospective observational
cohort study on early-onset mood disorders in South
Korea (ClinicalTrials.gov: NCT03088657).57,58 Detailed
study design and protocol information can be found in
a previous publication.57 In the original cohort study,
495 patients were recruited from March 2015 to April
2019, on a convenience basis, from both outpatient
clinics and psychiatric wards. The inclusion criteria
were being of an age <35 years and treated for less than
two years with the diagnosis of mood disorders (MDD,
BDI, and BDII) or age <25 years and diagnosed with
mood disorders. Individuals with evidence of intellec-
tual disabilities, organic brain injury, or difﬁculties
with the Korean language were excluded. Most patients
were on medications, and this study did not affect their
ongoing treatment. Sex identiﬁcation was self-reported
by study participants and eligible patients were all
encouraged to participate without restriction on sex.
The study received approval from the Institutional
Review Boards
hospitals
(2015AN0239) and was
conducted following the
Declaration of Helsinki. All participants provided
written informed consent before enrollment after
receiving a thorough explanation of the study.

participating

all

of

Assessment
The patients were diagnosed by a psychiatrist using the
Mini-International Neuropsychiatric Interview. They
completed clinical scales, including the Montgomery-
Asberg Depression Rating Scale (MADRS) and Young
Mania Rating Scale (YMRS). Furthermore, the patients
were instructed to engage in daily smartphone-delivered
ecological momentary assessment
(EMA) of mood
symptoms. The EMA questionnaire comprised two
types of mood symptoms: depressed and elevated. Pa-
tients recorded their daily mood by rating both
depressed and elevated moods on a scale ranging from
0 (not at all)
to 3 (extremely). The patients were
instructed to check both poles to identify a mixed state
their mood ﬂuctuated frequently
of mood state if
throughout the day or if they felt both elevated and
depressed. The patients were encouraged to complete
the questionnaire at the end of each day to record their
overall daily mood symptoms, with a reminder text
message sent to all patients at 9 pm daily. The patients
were also asked to wear a wearable activity tracker every

day (Fitbit Charge HR, 2 or 3, Fitbit Inc.), which records
their sleep patterns.

Participants
Among 495 patients enrolled in the MDCRC study, 270
patients providing more than 30 days of lifelog data
collected from wearable devices were initially included
in the analysis. We excluded any missing instances after
aligning the extracted estimates of daily sleep/circadian
phase data with the corresponding mood symptoms
data. Subsequently, we excluded 110 patients from the
analysis whose processed data covered fewer than 28
days, excluding the initial 14 days’ data. Additionally, 20
patients were excluded due to their low mood symptom
variation. The exclusions were necessary for ensuring
the reliable estimation of TE (see the following two
sections for details). Finally, one patient was excluded
from the analysis due to a change in diagnosis during
follow-up evaluations of psychotic disorder. As a result,
the ﬁnal analysis was conducted with 139 patients.

to predict

(Forger model)61

Sleep/circadian phase estimates and mood
symptoms extraction
To extract sleep and circadian phase information
from the data collected using wearable devices, we
analysed the sleep duration and timing (Fig. 2a). We
determined the midpoint of each patient’s daily main
sleep period (Midsleep), a valuable measure for assess-
ing the sleep phase.59,60 The main sleep period of each
day was identiﬁed as the most extended continuous
period of sleep that overlapped with that speciﬁc day.
Furthermore, we utilised a light-based circadian pace-
maker model
the daily
DLMO, a widely recognised biomarker of the circadian
phase. Speciﬁcally, the model simulates the core body
temperature rhythm, predicting the core body temper-
ature nadir (CBTmin). As CBTmin is known to occur
7 h after DLMO,62,63 we can predict DLMO using the
model simulations. This approach is substantiated by
ﬁndings from several preceding studies where mathe-
matical models were validated for predicting circadian
phases.32–35 In particular,
the Forger model demon-
strated comparable accuracy to other validated models.35
The applicability of the Forger model to describe circa-
dian rhythm dynamics is further highlighted by its
integration into sleep-cycle models, effectively eluci-
dating the alertness dynamics arising from circadian
rhythm.37,38

To simulate the Forger model, we inferred the light
input based on the sleep-wake pattern, using 250 lux for
wakefulness and 0 lux otherwise, based on previous
studies.35,64 Speciﬁcally, one recent study demonstrated
that a light proxy, which includes ﬁve light intensity
levels (0, 100, 200, 500, and 2000 lux) based on activity
levels, leads to more accurate circadian phase prediction
for shift workers compared to actual data collected from
wearable devices.35 Moreover, another study indicated

4

www.thelancet.com Vol 103 May, 2024

Articles

Fig. 2: A framework for determining the causal relationship between sleep/circadian phase disturbance and mood variation. (a) Sleep
information, including duration and timing, was collected from mood disorder patients via wearable devices. The midpoint of the patient’s daily
sleep period (Midsleep) is used as a measurement of the sleep phase. A mathematical model is applied to the collected data to predict the daily
Dim Light Melatonin Onset (DLMO), a golden standard biomarker of the circadian phase. (b) Self-reported information on the individual’s
emotional state was collected via a mobile survey app. The daily emotional states (Mood) are assessed as feeling low or high on a scale ranging
from 0 to 3 and further classiﬁed into three categories: normal (N; both are 0), depressed (D; only feeling low is >0), and elevated or mixed (E;
otherwise). (c) The causal relationship between the two daily time series (i.e., between Midsleep/DLMO and Mood) was determined via transfer
entropy (TX→Y) (i). TX→Y measures how much the uncertainty of the future state of the target variable (Y) reduces by knowing the past values of
X (i.e., H(Yt+1|Yt) − H(Yt+1|Xt, Yt)). In order to handle biases of transfer entropy due to limited data size, surrogate testing is performed (ii).
Speciﬁcally, X is randomly permuted (Xσ), and a transfer entropy value is computed (TXσ →Y). This is repeated 1000 times to generate a dis-
tribution of transfer entropy and determine the threshold (T∗), making the proportion of TXσ →Y exceeding T∗ by 5%. If the transfer entropy of
the original data (TX→Y) exceeds T∗, causation from X to Y is detected; otherwise, no causation (iii).

that using 250 lux instead of the other positive light
intensities does not signiﬁcantly affect the simulation
results of the Forger model.38 Therefore, employing
such two-level light input can effectively predict circa-
dian phase and applies to data collected with the Fitbit
Charge, known for its comparable accuracy in sleep
evaluation compared to actigraphy.65

The initial conditions of

determined

individually,

the simulations were
each

assuming

that

individual’s average midsleep time during the ﬁrst
seven days corresponded to the initial CBTmin. This
approach is based on a prior study that demonstrated
high accuracy in predicting circadian phase for shift
workers.33 To further mitigate the impact of uncertainty
in the initial conditions, we excluded estimated DLMO
from the ﬁrst two weeks. Additionally, we excluded
Midsleep from the ﬁrst two weeks for pair comparisons
with DLMO.

www.thelancet.com Vol 103 May, 2024

5

Articles

From the collected daily mood symptoms data
(measured by the EMA), we obtained time series data on
daily mood symptoms (Mood) (Fig. 2b). Speciﬁcally, the
quantiﬁed pairs of feeling depressed and elevated on a
scale of 0–3 were classiﬁed into three categories: normal
(N) when both poles are 0, depressed (D) when only
depressed mood is greater than 0, and elevated or mixed
(E) for all other cases.

Each day’s Midsleep or DLMO data was paired with
corresponding Mood data. The days without Midsleep/
DLMO or Mood data due to data missing or absence of
sleep period were excluded from the time series (see
Tables S1–S3 for the time series lengths). Notably,
DLMO can be estimated for the day without any sleep
period, unlike Midsleep. Thus, the lengths of DLMO
and Midsleep can differ, but the difference is at most 11
days.

Causal inference between sleep/circadian phase
estimates and mood symptoms time series
The causal relationship between the two daily time se-
ries, namely Midsleep/DLMO and Mood, was investi-
gated using TE (Fig. 2c (i)), which was found to be more
precise and visually interpretable than Granger causal-
ity.66 TE quantiﬁes the amount by which the uncertainty
of the future state of the target variable (Y) decreases
when the previous day’s value of the source variable (X )
is known. It is computed as the difference between the
two conditional entropies H(Yt+1|Yt) and H(Yt+1|Xt, Yt).
Here, H(Yt+1|Yt) evaluates the amount of information
that remains in the next day’s state of Y (Yt+1) given the
knowledge of its current value (Yt). Intuitively,
this
captures the average uncertainty or surprise linked to
the outcome of Y when its preceding value is available.
If H(Yt+1|Yt) is high and low, knowing the current value
(Yt) provides large and small amounts of information
future value (Yt+1), respectively. Analogously,
about
H(Yt+1|Xt, Yt) measures the amount of
information
remaining in the future state of Y (Yt+1) when the cur-
rent values of both X (Xt) and Y (Yt) are known. A
positive TE indicates that the current value of X con-
tributes valuable information for predicting the future of
Y. Conversely, if it approaches zero, it implies that
knowledge of the current values of X does not sub-
stantially augment the information obtained from the
current values of Y alone. See Supplementary Infor-
mation for a detailed illustrative calculation of TE.

causation.44,67–69 However,

Theoretically, a TE value of 0 indicates the absence of
a causal relationship between two variables. Thus, pre-
vious studies have employed the positivity of TE as a
criterion to detect
this
approach lacks reliability because it disregards conﬁ-
dence or statistical signiﬁcance testing. To address this
limitation, a statistical test for TE has recently been
developed and incorporated into an R package, widely
used for inference.70 This approach, known as the
Markov block bootstrap, requires the reconstruction of

the Markov chain transition matrix for each variable to
generate sample time series of the two variables without
any causality. It is important to note that the reliability of
this statistical test has been questioned due to the need
for a large dataset and high data variability, particularly
when the data has numerous categories or states.44 To
address these concerns, we employed a bin size of three
for both source and target time series to reduce the
number of states, aiming to enhance the robustness of
the analysis. We also considered only 159 patients with
MDD and BD among 495 patients whose data size (i.e.,
length of the time series) was larger than 27, excluding
the initial two weeks’ data (see the sleep/circadian phase
estimates and mood symptom extraction section for
details). The 27-day threshold represents the minimum
data size required to cover all states in the joint proba-
bility of the current target state, the previous day’s target
state, and the previous day’s source state (i.e., (bin
size)3 = 27), which is essential for calculating transfer
entropy. Moreover, 20 patients whose Mood variations
were below 0.05 were excluded when assigning 0 and 1
to the normal and the other states (see Tables S1–S3 for
the mood variation of the included data).

Despite implementing precautions, it was observed
that the current algorithm for predicting causation still
yielded statistically signiﬁcant results when applied to
randomised DLMO time series, which should not
exhibit any causation (Fig. S1 for details). To overcome
this false-positive prediction, we employed an alternative
approach that does not involve the reconstruction of the
Markov chain transition matrix. Speciﬁcally, we per-
formed surrogate testing (Fig. 2c (ii)), which involves
randomly permuting the variable X (X σ), and calculating
the TE value (TX σ →Y ). This process is repeated 1000
times to generate a distribution of TE values. From this
distribution, a threshold value (T ∗) is determined such
that the proportion of TX σ →Y exceeding T ∗ is 5%. To
determine the presence of causation from X to Y, the TE
of the original data (TX →Y ) is compared to T ∗ (Fig. 2c
(iii)). If TX→Y surpasses T ∗, it indicates the detection of
causation from X to Y. Conversely, if TX→Y falls below
T ∗, it suggests the absence of causation between the
variables. When applying this statistical
to the
randomised DLMO data, we observed a signiﬁcantly
reduced number of cases where causation was detected
compared to the previous statistical test method (Fig. S1
for details). This demonstrates the improved accuracy
and reliability of
the alternative approach in dis-
tinguishing between actual causation and random ﬂuc-
tuations in the data.

test

Quantiﬁcation and statistical analysis
Statistical analysis of study patients’ demographic and
clinical characteristics was performed using R software
(version: 4.3.2, http://www.R-project.org). Measurement
data are expressed as the mean ± standard deviation and
compared between three diagnostic groups using

6

www.thelancet.com Vol 103 May, 2024

Articles

analysis of variance. Categorical data are represented as
frequencies and percentages (%) and compared between
three diagnostic groups using the chi-square test and
Fisher’s exact test when the value in any of the cells is
below ﬁve. The annualised relapse rate is calculated with
counts of relapse as the numerator and person-years of
observation as the denominator. Estimated DLMO and
midsleep are expressed as the median and interquartile
range. For sleep and DLMO estimation, the data pre-
processing was performed with MATLAB 2021a software
(Natick, MA, USA). The simulations of the mathematical
model to estimate the DLMO were performed using
ode15s solver in MATLAB. The TE analysis was per-
formed using RTransferEntropy package for R.

Role of the funding sources
The funder played no role in study design, data collec-
tion, analysis and interpretation of data, or the writing of
this manuscript.

Results
Among a total of 139 patients included in the analysis,
45 (32.4%) were diagnosed with MDD, 35 (25.2%) had
BDI, and 59 (42.4%) had BDII. The obtained time series
spanned 29 to 1457 days (mean ± standard deviation
(SD) = 290± 297; see Tables S1–S3 for details). Table 1
presents the patients’ baseline demographic and clin-
ical characteristics, including their baseline symptoms,
comorbidities, and medications. Age, sex, MADRS, and
data size exhibited no differences among the three
groups, whereas YMRS varied between groups, reﬂect-
ing their respective diagnoses. The post-hoc analysis
indicated a signiﬁcantly higher baseline YMRS score in
BDI compared to MDD, with consideration for Bon-
ferroni’s correction. The prevalence of comorbidities,
including anxiety disorder, substance use disorder,
obsessive-compulsive and related disorder, eating dis-
order, and posttraumatic stress disorder, did not show
differences between groups. However, medications
differed between groups, reﬂecting diagnostic differ-
ences, except lithium. Speciﬁcally, pairwise comparison
with Bonferroni correction revealed that patients with
BD used mood-stabilising
anticonvulsants more
frequently and antidepressants less frequently than pa-
tients with MDD. The mean ± SD age of patients with
MDD, BDI, and BDII were 23.3 ± 3.9, 24.7 ± 4.4, and
23.0 ± 2.7 years, respectively. The number (percentage)
of patients whose mood episodes recurred during the
data requisition period were 21 (47%), 23 (66%), and 40
(68%) in MDD, BDI, and BDII, respectively. The mean
± SD durations of data were 266 ± 238, 360 ± 391, and
267 ± 271 days in MDD, BDI, and BDII, respectively.
The annualised relapse rates of mood episode recur-
rence per person-year were as follows: major depressive
episodes, 0.48, 0.53, and 0.73 in MDD, BDI, and
BDII, respectively; manic episodes, 0.28 in BDI, and

hypomanic episodes; 0.15 and 0.33 in BDI and BDII,
respectively.

TE analysis suggests the causality between
circadian phase disturbance and mood symptoms
We examined the percentages of patients demonstrating
causal relationships (% of causality) of each direction
within each diagnostic group of MDD, BDI, and BDII
(Fig. 3). In particular, we investigated how the % of
causality changes as the data size increases, and thus TE
estimation becomes more reliable.44 Thus, the increase
in the % of causality as the data size increases can be
used as the criteria for the reliability of causality.

As the data size grew from 0, 100 to 200, …, and 600
days for patients with MDD (Fig. 3a) and BDI (Fig. 3b),
the % of causality of DLMO to Mood exhibited a pro-
gressive increase. In particular, when considering only
patients with a data size larger than 600 days, the % of
causality reached 66.7% and 85.7% for patients with
MDD and BDI, respectively. However, the opposite di-
rection (Mood to DLMO) showed a consistently low % of
causality (Fig. 3d and e), never exceeding 17% regard-
less of data size. In particular, no causality from Mood to
DLMO was observed for MDD. The % of causality of
Midsleep to Mood also showed a gradual increase with
larger data sizes both for patients with MDD (Fig. 3g)
and those with BDI (Fig. 3h). However, this increase
was not as pronounced as that of DLMO to Mood, with
the % of causality never exceeding 43% in all cases. As
for Mood to Midsleep causality,
it was nearly 0%
regardless of the data size in both patients with MDD
(Fig. 3j) and those with BDI (Fig. 3k). Taken together,
the analysis suggests strong evidence supporting cau-
sality from DLMO to Mood in patients with MDD and
BDI, indicating that the circadian phase exerts a more
inﬂuence on mood symptoms in these
prominent
diagnostic groups. Conversely, Midsleep did not exhibit
such robust evidence supporting a causal relationship
with Mood, suggesting a comparatively weaker impact.
On the other hand, patients with BDII displayed a
different pattern. The % of causality of DLMO to Mood
(Fig. 3c) did not progressively increase with larger data
sizes, never exceeding 37%. Additionally,
the % of
causality from Mood to DLMO (Fig. 3f) was nearly 0%
regardless of the data size. Similarly, the % of causality
of Midsleep to Mood (Fig. 3i) did not show a clear
increasing pattern, with the % of causality never
exceeding 37%, and that of Mood to Midsleep (Fig. 3l)
was 0% for all the data sizes. These ﬁndings suggest a
less pronounced causal relationship between DLMO/
Midsleep and Mood in patients with BDII, possibly
inﬂuenced by other factors (see Discussion for details).
Given the utilisation of estimated DLMO through a
mathematical model, it is crucial to consider the po-
impact of prediction errors on our previous
tential
the causal relationship between DLMO
analysis of
and Mood. To address this concern, we deliberately

www.thelancet.com Vol 103 May, 2024

7

Articles

Characteristics

Demographic characteristics

Diagnosis

MDD n = 45

BDI n = 35

BDII n = 59

Age at baseline, years, mean (SD)

23.3 (3.92)

24.7 (4.37)

23.0 (2.74)

Sex, n (%)

Female

Male

Clinical characteristics

Baseline clinical scales

MADRS

YMRS

Comorbidities

Anxiety disorder

Substance use disorder

OC and related disorder

Eating disorder

PTSD

Somatic symptom and related disorder

Medications

Lithium

Anticonvulsants

SSRIs

Other antidepressants

Annualised relapse rate (person-year)

MDEs

MEs

HMEs

Sleep measures and circadian estimates

Data size, days, mean (SD)

Estimated DLMO, hour, median (IQR)

Midsleep, hour, median (IQR)

18 (40%)

27 (60%)

18.3 (11.1)

1.22 (2.15)

15 (33%)

2 (4.4%)

2 (4.4%)

1 (2.2%)

2 (4.4%)

1 (2.2%)

13 (29%)

10 (22%)

26 (58%)

18 (40%)

0.48

22 (63%)

13 (37%)

10.7 (10.1)

2.37 (3.33)

5 (14%)

3 (8.6%)

2 (5.7%)

1 (2.9%)

0

0

0

19 (54%)

19 (54%)

1 (2.9%)

0.53

0.28

0.15

36 (61%)

23 (39%)

17.4 (10.6)

3.19 (3.64)

21 (36%)

2 (3.4%)

10 (17%)

5 (8.5%)

5 (8.5%)

1 (1.7%)

26 (44%)

31 (53%)

10 (17%)

8 (14%)

0.73

0.33

266 (238)
23.1 (22.0–24.3)
5.02 (3.70–6.97)

360 (391)
22.2 (21.2–23.3)
4.14 (2.92–5.67)

267 (271)
23.0 (21.7–24.6)
4.96 (3.37–7.05)

p

0.62

0.054

0.86

<0.05

0.065

0.54

0.10

0.37

0.22

1

0.065

<0.05

<0.01

<0.01

0.89

Data are expressed as mean (standard deviation), number (%), number per year per person or median (interquartile range). Analysis of variance was applied to test for age
and data size. Categorical variables were compared using the chi-square test and Fisher’s exact test. MDD Major depressive disorder, BDI bipolar I disorder, BDII bipolar II
disorder, MADRS Montgomery-Asberg Depression Rating Scale, YMRS Young Mania Rating Scale, OC obsessive-compulsive, PTSD posttraumatic stress disorder, MDE major
depressive episode, ME manic episode, HME hypomanic episode, DLMO, dim light melatonin onset, IQR, interquartile range.

Table 1: Demographic and clinical characteristics of study participants.

introduced random Gaussian noise into the DLMO time
series, mirroring the level of prediction error encoun-
tered. Subsequently, we applied transfer entropy anal-
ysis to investigate this impact. The magnitude of the
noise was determined based on a prior validation study
of the mathematical modelling approach.33 Speciﬁcally,
the predicted circadian phase shows a linear correlation
with the measured values, while the slope is not pre-
cisely one. As the current transfer entropy analysis is
insensitive to the scaling of the time series, we can re-
gard the residual error of the linear model between
predicted and measured circadian phases as the pre-
diction error. From the previously reported r-squared
values and the SDs of the measured circadian phases in
the previous study,33 we calculated that the SD of the
random noise required to be added to the current
DLMO time series is ∼0.3 h for day shifts and ∼0.6 h for

night shifts. Noise of SD 0.6 h was added to the day with
a night-shift-like sleep phase, where the Midsleep falls
between 10 am and 3 pm, while noise of SD 0.3 h was
added to the other days.

This process was repeated 20 times, and we calcu-
lated the mean and standard deviation of the % of
causality (Fig. S3). Interestingly, as we introduced
random noise, the % of causality from DLMO to Mood
in patients with MDD remained relatively consistent,
while in patients with BDI, it exhibited a signiﬁcant
decrease. However, the overall increasing trend with
increasing thresholds persisted. Moreover, these values
continued to be notably higher than the % of causality
from Mood to DLMO. Importantly, even in this added
random noise, the % of causality from DLMO to Mood
remained comparable to or even exceeded those
observed for Midsleep to Mood (Fig. 3). This suggests

8

www.thelancet.com Vol 103 May, 2024

Articles

b

100

IDB

35

22

19 12 10

9

7

c

100

IIDB

59

37

29 21

11

6

6

# of patients

MDD

45

33

20 15 12

9

6

a

d
o
o
M
→
O
M
L
D

d

O
M
L
D
→
d
o
o
M

g

d
o
o
M
→
p
e
e
s
d
M

i

l

j

l

i

p
e
e
s
d
M
→
d
o
o
M

100

50

0

y
t
i
l

a
s
u
a
C

f
o
%

100

50

0

y
t
i
l

a
s
u
a
C

f
o
%

100

50

0

y
t
i
l

a
s
u
a
C

f
o
%

100

50

0

y
t
i
l

a
s
u
a
C

f

o
%

50

0

6 ×100

0

50

0

6 ×100

0

2

1
5
3
Threshold (days)

4

2

1
5
3
Threshold (days)

4

6 ×100

e
100

35

22

19 12 10

9

7

f
100

59

37

29 21

11

6

6

2

5
1
3
Threshold (days)

4

0

# of patients

45

33

20 15 12

9

6

50

0

6 ×100

0

50

0

6 ×100

0

2

1
5
3
Threshold (days)

4

6 ×100

2

1
5
3
Threshold (days)

4

h
100

35

22

19 12 10

9

7

i
100

59

37

29 21

11

6

6

2

3
1
5
Threshold (days)

4

0

# of patients

45

33

20 14 12

9

6

50

0

6 ×100

0

50

0

6 ×100

0

2

1
5
3
Threshold (days)

4

2

1
5
3
Threshold (days)

4

6 ×100

k
100

35

22

19 12 10

9

7

l
100

59

37

29 21

11

6

6

2

3
1
5
Threshold (days)

4

0

# of patients

45

33

20 14 12

9

6

50

0

6 ×100

0

0

2

3
1
5
Threshold (days)

4

50

0

6 ×100

0

2

1
5
3
Threshold (days)

4

6 ×100

2

1
5
3
Threshold (days)

4

Fig. 3: Only causation from circadian phase disturbance to mood variation is evident. (a–f) The fractions of causality between circadian
phase and mood symptoms among patients with MDD (a, d), BDI (b, e), and BDII (c, f), which were obtained by transfer entropy (TE). In
particular, the fraction of causality was calculated by changing the data inclusion threshold for data length (0, 100, 200, …, 600 days). As more
patients with low data size were excluded, and thus the causation detection with TE became more reliable, the causation from DLMO to Mood
became more evident in patients with major depressive disorder (MDD; (a)) and bipolar disorder I (BDI; (b)), but not BDII (c). (g–l) Unlike DLMO,
there is no apparent causation between Midsleep and Mood for all patients with mood disorders (i.e., MDD, BDI, and BDII).

www.thelancet.com Vol 103 May, 2024

9

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Articles

that, despite the existence of prediction errors, their
impact was sufﬁciently minimal to avoid distorting the
implication of the previous analysis.

The TE analysis in this study examined causality
from a source variable to a target variable by investi-
gating whether knowledge of the previous day’s source
variable can diminish the uncertainty of the present
day’s target variable. As depicted in the results (Fig. 3),
this analysis highlights evidence supporting the causal-
ity of the preceding day’s circadian phase change on
mood symptoms. This prompts the question of whether
the inﬂuence of the circadian phase on mood symptoms
extends beyond a single day. To explore this, we shifted
the source variable time series one day forward and
applied TE analysis. This approach allows us to evaluate
whether awareness of the source variable from two days
prior could reduce the uncertainty of the present day’s
target variable. Upon shifting the source time series by
one day, the overall % of causality decreased compared
to the case without a time series shift (Fig. S2). In
particular, the % of causality from DLMO to Mood of
patients with BDI decreased signiﬁcantly, and that of
patients with MDD no longer shows a progressive in-
crease. This observation suggests that the inﬂuence of
the circadian phase disturbance from one day prior on
mood symptoms is most substantial and diminishes as
the delay increases.

Sleep phase disturbance induces circadian phase
disturbance, which potentially causes mood
episode relapse
Inter-daily circadian phase variations primarily hinge on
sleep-wake patterns, notably dictating the most pivotal
factor in the circadian rhythm—light exposure pattern.
This inﬂuence has become especially pronounced in
modern society due to the prevalence of artiﬁcial light.71
Nevertheless, our TE analysis suggests that the causal
link between circadian phase disruption and mood
symptoms is much stronger than that between sleep
phase disruption and mood symptoms in patients with
MDD and BDI. This raises the question of what speciﬁc
dynamical differences between circadian and sleep
phases contribute to this disparity in causality. To
explore this further, we examined the dynamics of
Midsleep and DLMO in two sample sleep-wake pattern
scenarios: (1) a sudden 4-h delay of sleep periods while
maintaining the overall sleep period (Fig. 4a) and (2) a
gradual variation in sleep durations while keeping the
midpoints of the sleep periods constant (Fig. 4b).

In both scenarios, changes in sleep patterns and the
following change in light exposure pattern resulted in
their change
alterations in the circadian phase, but
tendencies differed. Speciﬁcally, when sleep periods
were suddenly delayed by 4 h, Midsleep also shifted by
4 h immediately, while DLMO exhibited a gradual delay,
taking more than six days to shift by 4 h (Fig. 4a). In
addition, when sleep durations varied while maintaining

a constant Midsleep, DLMO showed variation (Fig. 4b).
These distinctive dynamics between Midsleep and
DLMO may have contributed to the differential identi-
ﬁcation of causal relationships. For instance, a chronic
sleep phase disruption, which induces a large circadian
phase shift, might be more likely to cause mood
symptom variation than acute sleep phase disruptions.
Moreover, irregular sleep durations might induce sig-
niﬁcant circadian shifts and contribute to mood symp-
toms even when the time of midsleep remains almost
the same.

Based on these observations, we can conclude the
following causal relationships between sleep patterns,
circadian phases, and mood disorder: disturbance in the
sleep pattern results in circadian phase disruption
whose dynamics differ from the sleep phase. This
distinct circadian phase disruption ultimately causes
mood symptom variation, which potentially results in
mood episode relapse in patients with mood disorders
(Fig. 4c).

Discussion
Accumulating evidence has shed light on the associa-
tions between sleep/circadian phase disturbance and
mood disorders,23,58,72–74 yet unravelling the direction of
causality remains challenging (Fig. 1).26 Our ﬁndings
based on the application of a mathematical model and
the TE analysis (Fig. 2) demonstrated strong evidence
supporting causality from circadian but not sleep phase
disturbance to mood symptoms for patients with MDD
and BDI, whereas no clear evidence supporting causality
was observed in patients with BDII (Fig. 3). These re-
sults suggest that disturbances in the circadian phase
preceding mood symptom variations may trigger re-
lapses of mood episodes in patients with MDD and BDI.
Furthermore, we explored the dynamics of the circadian
phase estimates, which, although linked to sleep pattern
disturbance, exhibited distinctive characteristics that
might contribute to the different causal relationships
with mood symptoms (Fig. 4a and b). Based on these
ﬁndings, we hypothesise that sleep phase disturbance
indirectly inﬂuences mood symptoms through circadian
phase disturbances (Fig. 4c).

The absence of evidence supporting causality in BDII
may be attributed to several factors. Until recently, it was
believed that BDI and BDII could be classiﬁed along a
spectrum based on the extent, duration, and severity of
manic symptoms. However, recent studies report more
prominent and longer depressions, more cyclothymic
temperament,75 greater likelihood of mixed features,76
and higher risk of mood recurrences77 in BDII than
BDI. These ﬁndings suggest that mood oscillations in
patients with BDII may be more chaotic than in patients
with BDI. Consequently, patients with BDII face difﬁ-
culties accurately assessing their daily mood, which can
in inaccurate mood symptom recordings.
result

10

www.thelancet.com Vol 103 May, 2024

Articles

a

y
a
D

1

2

3

4

5

6

7

8

b

y
a
D

1

2

3

4

5

6

7

8

12:00

00:00

12:00

00:21

00:00

00:21

DLMO

Midsleep

c

nrettaPekaW-peelS

Circadian Rhythm

redrosiDdooM

Fig. 4: Circadian phase disturbance, which results from sleep phase disturbance, causes mood variation, potentially resulting in mood
episode relapse. (a) A sudden delay in the sleep period leads to an abrupt delay in Midsleep (blue triangle) but a gradual delay in DLMO (red
triangle) over time due to altered light exposure. (b) Varying sleep durations does not change the Midsleep but alters DLMO due to altered light
exposure. (c) Due to these different dynamics of Midsleep and DLMO, although DLMO was determined by sleep phase, which determines light
exposure pattern, only the causation from DLMO, not Midsleep to Mood, was detected. Therefore, the accumulation of sleep disruptions and
resulting circadian disruption cause mood variation, potentially contributing to the onset of mood episodes.

Moreover, patients with BDII are more likely to have
comorbidity with borderline personality disorder (BPD)
than BDI.78 However, differentiating BPD from BDII is
a common diagnostic dilemma for clinicians.79 Whether
due to comorbidity or misdiagnosis of BPD, patients
with this disorder can complicate the establishment of a
causal relationship between the circadian phase and
mood symptoms due to their core features, such as af-
fective instability and emotional dysregulation. Inter-
estingly, a recent large study assessing polygenic risk
scores (PRS) for sleep traits in association with BD re-
ported that PRS for morningness was associated with a
reduced relative risk of BDI compared with the control
participants, while the results for BDII compared with
the control were not signiﬁcant.80 This result aligns with
characteristics
the
and may
our
mentioned above of patients with BDII.

reﬂect

results

The suggested causality from circadian phase to
subsequent mood symptoms indicates that disruptions
in circadian phase have the potential to lead to the
recurrence of mood symptoms in patients with mood

disorders. This ﬁnding aligns with previous research
that found that disturbances of circadian phase were
linked to the relapse of mood episodes. For instance, a
12-month prospective study found a signiﬁcant associ-
ation between a later timing of baseline circadian ac-
tivity rhythm and an increased risk of depressive
episode relapses in patients with BD.81 A 48-week pro-
spective study revealed that comorbidity of circadian
rhythm sleep-wake disorders was signiﬁcantly associ-
ated with the time to relapse of mood episodes.74 In
contrast, some longitudinal studies found that chro-
notype was not associated with mood disorders.82,83
However, a meta-analysis that included these longitu-
dinal studies reported a signiﬁcant relationship between
evening chronotype and mood-related disturbances.84
The association of chronotype with mood disorders is
further supported by a recent large-sample genome-
wide association study, which revealed that earlier
diurnal preference is associated with a protective effect
on the risk of MDD.85 It is important to note, however,
studies primarily assessed the
that

the previous

www.thelancet.com Vol 103 May, 2024

11

Articles

inter-individual level effects of circadian rhythm char-
acteristics. Our causality inference framework provides
insights into the within-individual-level
impact of
circadian phase on mood symptoms through gathering
longitudinal data, revealing dynamic intra-individual
variability of estimated sleep/circadian rhythms and its
impact on mood symptoms. Therefore, our framework
addresses the limitations of previous research and
bridges the gap between circadian rhythm characteris-
tics and future mood episodes.

also aligns with prior

The suggested causality from circadian disruption to
mood symptoms
animal
studies.86,87 The studies involved mice carrying mutated
REV-ERB α gene, a circadian clock component, and
these mice exhibited behaviours akin to
found that
elevated, similar to those in BD.86 In particular, the
studies proposed molecular links for this phenomenon
by demonstrating that REV-ERB α regulates dopamine
and serotonin levels in the midbrain and dorsal raphe,
respectively, neurotransmitters known to inﬂuence
mood.86,87 Our study signiﬁcantly supports these prior
inquiries by employing a unique approach to establish
causality between time series data, distinct from previ-
these results
ous animal studies. Taken together,
emphasise the importance of circadian rhythm in MDD
and BD, indicating its potential role in aetiology and
treatment.

with

among

This study utilised sleep onset and offset data
collected through the Fitbit Charge device to estimate
sleep and circadian phases. Previous research has indi-
cated that estimating gross sleep parameters such as
Total Sleep Time (TST) and Wakefulness After Sleep
Onset (WASO) using Fitbit devices can be inaccurate,
especially
psychiatric
individuals
conditions.88–90 However,
it is worth noting that the
Fitbit device model employed in our study was a newer
model than the device used in prior research, and newer
generations have shown improved performance.91–93
Moreover, past studies have primarily noted inaccura-
cies in classifying WASO as sleep, while the estimation
of sleep onset and offsets remained reliable.88–90,94
Hence, the estimated sleep phase (i.e., Midsleep) in
our study can be deemed reliable. Additionally, WASO
typically occurs in low-light or dark conditions, making
it less likely to impact the accuracy of circadian phase
estimation using our methodology signiﬁcantly. Never-
theless, further validation of the current Fitbit model’s
ability to estimate sleep onset and offset in the psychi-
atric population is imperative.

Previous studies have demonstrated the effectiveness
of mathematical models in simulating circadian rhythm
and estimating circadian phase, even in challenging
shift work scenarios where sleep patterns are highly
irregular. Speciﬁcally, while speciﬁc investigations have
reported reduced accuracy in predicting circadian
compared to non-shift
phases
workers,32,34,35
al.33
Stone

shift workers

another

study

for

by

et

demonstrated notably higher accuracy, even among
shift workers; they achieved circadian phase predictions
within ± 1 h for 80% and 68% of individuals on diurnal
and night schedules, respectively. This success was
attributed to their unique approach of setting initial
conditions based on individuals’ midsleep phase, devi-
ating from the uniform initial conditions used in pre-
vious studies.
Inspired by this approach, we also
adopted individualised initial conditions recommended
by Stone et al. to enhance the accuracy of DLMO pre-
diction. Furthermore, acknowledging the lingering un-
certainty associated with initial conditions, we excluded
DLMO data from the ﬁrst two weeks. Taken together,
our study’s circadian phase estimation is expected to be
robust and reliable, even when targeting individuals
with disrupted sleep patterns.

The circadian rhythms simulated with the mathe-
matical models have applications in various domains,
such as predicting appropriate sleep-wake patterns or
daily alertness level variation in shift workers.32,37,38 This
indicates the broad potential of utilising mathematical
model-predicted circadian rhythms to uncover
the
intricate connections between circadian rhythm distur-
bances and the onset or progression of diverse health
conditions, such as neurodegenerative disease.95 This
approach might also be directly applied to data from
previous studies that have explored the temporal asso-
ciation between sleep and mood.41,42,96

Integration of wearable devices and mathematical
models can detect disruptions in circadian rhythms in
real time.35,97,98 This opens up the possibility of assessing
the risk of recurring mood episodes in the patient’s daily
life outside clinical settings. Additionally, it provides an
objective measure of the patient’s condition, which has
been lacking in traditional interview-based psychiatric
approaches to mood disorders. Based on these ﬁndings,
clinicians may be able to intervene early, before daily
mood swings develop into full-blown mood episodes.
This could include correcting the patient’s circadian
rhythm through lifestyle modiﬁcation or administration
of light therapy or melatonin.99–101 In particular, the
timing of melatonin administration or light exposure
could be optimised based on the patient’s calculated
DLMO, considering the phase response curve.101,102
Other zeitgebers, such as mealtime and activity sched-
ules, also have potential as targets for intervention.

In order to make these interventions timely accord-
ing to patients’ dynamic conditions, digital therapeutics
(DTs) may be more appropriate than outpatient
clinics.97,100 DTs, a unique class of software applications
designed to deliver evidence-based treatments through
patients’ smartphones,
tablets, or computers,64 are
emerging treatment options in mental health.103 Some
DTs,
like reSET104 and Somryst,105 digitally provide
standardised versions of behavioural therapies already
employed in traditional clinician-based settings. On the
other hand, a DT focused on modulating circadian

12

www.thelancet.com Vol 103 May, 2024

Articles

potential limitation to the current study. Strengthening
the ﬁndings may require further validation of our
approach by utilising more reliable sleep data. Finally,
while the Forger model has been successfully validated
in diverse populations, including shift workers, its vali-
dation for patients with mood disorders is lacking. Pa-
tients with depression have shown hyposensitivity of the
circadian system to light,113 and supersensitivity to light
has been proposed as a biomarker of BD.106 Given po-
tential variations in physiological properties related to
circadian rhythms in this patient group compared to
non-patients, additional calibration of model parameters
may be necessary to enhance the accuracy of circadian
phase predictions for individuals with mood disorders.

Contributors
H.J.L. and J.K.K. developed the concept and design. H.J.L., C.H.C.,
J.B.L., T.L., and J.W.Y. performed the recruitment of participants and
data collection. A.A.D.L.R.V., Y.M.S., D.L., and J.K.K. developed the al-
gorithm. Y.M.S., A.A.D.L.R.V., J.J., H.J.L., and J.K.K. performed the
analysis of data. Y.M.S., A.A.D.L.R.V., J.J., veriﬁed the underlying data.
Y.M.S., A.A.D.L.R.V., J.J., H.J.L., and J.K.K. wrote the draft of the
manuscript. All authors provided critical feedback on the manuscript for
intellectual content. All authors read and approved the ﬁnal version of
the manuscript.

Data sharing statement
The MDCRC data are not deposited into a public repository due to
multi-site partnership agreements and conditions for Institutional Re-
view Board approval. The MDCRC data are routinely made available
through submission and approval from the cohort executive committee
of a data access form. The access to the data was facilitated by one of the
corresponding authors of this study, HJ Lee, who served as a principal
investigator of the MDCRC study.

Declaration of interests
We declare no competing interests.

Acknowledgements
This study was funded by Institute for Basic Science (IBS-R029-C3)
(J.K.K.),
the Human Frontiers Science Program Organization
(RGY0063/2017) (J.K.K.), the National Research Foundation of Korea
(2019R1A2C2084158) (H.J.L.), and the Ministry of Health & Welfare of
South Korea (HI22C1472) (H.J.L.).

Appendix A. Supplementary data
Supplementary data related to this article can be found at https://doi.
org/10.1016/j.ebiom.2024.105094.

References
1

Lange T, Dimitrov S, Born J. Effects of sleep and circadian rhythm
on the human immune system. Ann N Y Acad Sci. 2010;1193:48–
59.

2 Malhi GS, Kuiper S. Chronobiology of mood disorders. Acta Psy-

3

4

5

6

insomnia, depression,

chiatr Scand Suppl. 2013;444:2–15.
Soehner AM, Kaplan KA, Harvey AG. Insomnia comorbid to severe
psychiatric illness. Sleep Med Clin. 2013;8(3):361–371.
Taylor DJ, Lichstein KL, Durrence HH, Reidel BW, Bush AJ.
and anxiety. Sleep.
Epidemiology of
2005;28(11):1457–1464.
Pancheri C, Verdolini N, Pacchiarotti I, et al. A systematic review
on sleep alterations anticipating the onset of bipolar disorder. Eur
Psychiatry. 2019;58:45–53.
Baglioni C, Battagliese G, Feige B, et al. Insomnia as a predictor of
depression: a meta-analytic evaluation of longitudinal epidemio-
logical studies. J Affect Disord. 2011;135(1-3):10–19.

rhythms in accordance with their daily ﬂuctuations
could offer a distinctive approach to treating mood dis-
orders. However, further clinical trials are imperative to
establish robust
therapeutic
efﬁcacy.

concerning

evidence

While the current study found evidence supporting a
causal
link between circadian phase disturbance and
mood symptoms, further investigation is needed to
determine the exact nature of this relationship. Specif-
ically, it is crucial to explore whether circadian rhythm
delay or advance actively contributes to the development
of depression or (hypo)mania. Moreover,
this study
focused only on phase disturbance, while various types
of circadian disturbances are known to be associated
with mood disorders, such as chronotype, amplitude,
and irregularity of sleep/circadian rhythms.106,107
It
would be interesting to apply the same approach as in
this study to circadian amplitude and mood symptom
variation data. Furthermore, it is essential to acknowl-
like sleep loss,
edge that other sleep-related factors,
which were not considered in this study, could poten-
tially inﬂuence mood symptoms in individuals through
non-circadian mechanisms. These unexplored factors
might actively contribute to mood symptoms in cases
where a causal link between DLMO and mood was not
identiﬁed in this study. It would be intriguing to
conduct further investigations into the causality between
various sleep parameters like sleep duration and mood
symptoms.

Several limitations in our study methodologies war-
rant acknowledgement. Firstly, subjective (self-reported)
mood symptoms may be susceptible to biases. It is
essential to approach the interpretation of subjective
mood symptoms with caution, considering the potential
for miscommunication or misunderstanding,
and
maintain a nuanced understanding when assessing
their implications in mood disorders. Secondly, our
study did not account for the potential effects of medi-
cations and comorbidities. Previous research has indi-
cated that lithium treatment in BD was associated with
shifts towards morningness and a larger circadian
amplitude.108 Other mood stabilisers, such as valproic
acid and even serotonergic antidepressants, are also
known to inﬂuence circadian rhythms.109,110 Further-
more, comorbid psychiatric conditions, such as sub-
stance use disorder with mood disorders, are recognised
for their impact on circadian rhythms.111,112 The rate of
comorbidities in the patient population, except for anx-
iety disorder, mainly was below 10% (Table 1). Thus, the
impact of psychiatric comorbidities on our results is
presumed to be negligible. However, a majority of pa-
tients in this study were using medications, including
lithium, mood-stabilising anticonvulsants, and antide-
pressants (Table 1). This could potentially inﬂuence the
study results. Thirdly, depending on sleep onset and
offset data collected from Fitbit, which may necessitate
further validation in the psychiatric population, poses a

www.thelancet.com Vol 103 May, 2024

13

Articles

7

8

9

Souetre E, Salvati E, Belugou JL, et al. Circadian rhythms in
depression and recovery: evidence for blunted amplitude as the
main chronobiological abnormality. Psychiatry Res. 1989;28(3):263–
278.
Raoux N, Benoit O, Dantchev N, et al. Circadian pattern of motor
activity in major depressed patients undergoing antidepressant
therapy: relationship between actigraphic measures and clinical
course. Psychiatry Res. 1994;52(1):85–98.
Lewy AJ. Circadian misalignment
Psychiatry Rep. 2009;11(6):459–465.

in mood disturbances. Curr

10 Novakova M, Prasko J, Latalova K, Sladek M, Sumova A. The
circadian system of patients with bipolar disorder differs in epi-
sodes of mania and depression. Bipolar Disord. 2015;17(3):303–314.
11 Robillard R, Naismith SL, Rogers NL, et al. Sleep-wake cycle and
melatonin rhythms in adolescents and young adults with mood
disorders: comparison of unipolar and bipolar phenotypes. Eur
Psychiatry. 2013;28(7):412–416.

12 Dallaspezia S, Benedetti F. Melatonin, circadian rhythms, and the
Psychiatry Rep.

disorder. Curr

bipolar

clock
genes
in
2009;11(6):488–493.

13 Etain B, Jamain S, Milhiet V, et al. Association between circadian
Int.

and chronotypes. Chronobiol

genes, bipolar disorders
2014;31(7):807–814.

14 Abreu T, Braganca M. The bipolarity of light and dark: a review on
bipolar disorder and circadian cycles. J Affect Disord. 2015;185:219–
229.

15 Levandovski R, Dantas G, Fernandes LC, et al. Depression scores
associate with chronotype and social jetlag in a rural population.
Chronobiol Int. 2011;28(9):771–778.

16 Melo MCA, Abreu RLC, Linhares Neto VB, de Bruin PFC, de
Bruin VMS. Chronotype and circadian rhythm in bipolar disorder:
a systematic review. Sleep Med Rev. 2017;34:46–58.

17 Au J, Reece J. The relationship between chronotype and depressive
symptoms: a meta-analysis. J Affect Disord. 2017;218:93–104.
18 Murray JM, Phillips AJ, Magee M, et al. Sleep regularity is associ-
ated with sleep-wake and circadian timing, and mediates daytime
function in delayed sleep-wake phase disorder. Sleep Med.
2019;58:93–101.

19 Lewy AJ, Kern HA, Rosenthal NE, Wehr TA. Bright artiﬁcial light
treatment of a manic-depressive patient with a seasonal mood cycle.
Am J Psychiatry. 1982;139(11):1496–1498.

20 Rosenthal NE, Sack DA, Gillin JC, et al. Seasonal affective disorder.
A description of the syndrome and preliminary ﬁndings with light
therapy. Arch Gen Psychiatry. 1984;41(1):72–80.

21 Lee HJ, Rex KM, Nievergelt CM, Kelsoe JR, Kripke DF. Delayed
sleep phase syndrome is related to seasonal affective disorder.
J Affect Disord. 2011;133(3):573–579.

22 Hasler BP, Buysse DJ, Kupfer DJ, Germain A. Phase relationships
between core body temperature, melatonin, and sleep are associ-
further evidence for circadian
ated with depression severity:
misalignment
depression. Psychiatry Res.
2010;178(1):205–207.

in non-seasonal

23 Moon JH, Cho CH, Son GH, et al. Advanced circadian phase in
mania and delayed circadian phase in mixed mania and depression
returned to normal after treatment of bipolar disorder. eBioMedi-
cine. 2016;11:285–295.

24 Zaki NFW, Spence DW, BaHammam AS, Pandi-Perumal SR,
Cardinali DP, Brown GM. Chronobiological theories of mood
disorder. Eur Arch Psychiatry Clin Neurosci. 2018;268(2):107–
118.

25 Findeis H, Oster H, Bauer M, Ritter P. [Chronobiological aspects of

bipolar disorder]. Nervenarzt. 2022;93(9):873–881.

26 Alachkar A, Lee J, Asthana K, et al. The hidden link between
circadian entropy and mental health disorders. Transl Psychiatry.
2022;12(1):281.

27 Lee H-J. Circadian misalignment and bipolar disorder. Chronobiol

Med. 2019;1(4):132–136.

28 Hlaváˇcková-Schindler K, Paluˇs M, Vejmelka M, Bhattacharya J.
Causality detection based on information-theoretic approaches in
time series analysis. Phys Rep. 2007;441(1):1–46.

29 Zhang Y, Folarin AA, Sun S, et al. Relationship between major
depression symptom severity and sleep collected using a wristband
wearable device: multicenter longitudinal observational study.
JMIR Mhealth Uhealth. 2021;9(4):e24604.

30 Robbins R, Affouf M, Seixas A, Beaugris L, Avirappattu G, Jean-
Louis G. Four-year trends in sleep duration and quality: a longitu-
dinal study using data from a commercially available sleep tracker.
J Med Internet Res. 2020;22(2):e14735.

31 Hofstra WA, de Weerd AW. How to assess circadian rhythm in
humans: a review of literature. Epilepsy Behav. 2008;13(3):438–444.
32 Knock SA, Magee M, Stone JE, et al. Prediction of shiftworker
alertness, sleep, and circadian phase using a model of arousal dy-
namics constrained by shift schedules and light exposure. Sleep.
2021;44(11):zsab146.

33 Stone JE, Aubert XL, Maass H, et al. Application of a limit-cycle
oscillator model for prediction of circadian phase in rotating
night shift workers. Sci Rep. 2019;9(1):11032.

34 Cheng P, Walch O, Huang Y, et al. Predicting circadian misalign-
ment with wearable technology: validation of wrist-worn actigraphy
and photometry in night shift workers. Sleep. 2021;44(2):zsaa180.
35 Huang Y, Mayer C, Cheng P, et al. Predicting circadian phase
across populations: a comparison of mathematical models and
wearable devices. Sleep. 2021;44(10):zsab126.

36 Stone JE, Postnova S, Sletten TL, Rajaratnam SMW, Phillips AJK.
Computational approaches for individual circadian phase predic-
tion in ﬁeld settings. Curr Opin Syst Biol. 2020;22:39–51.

37 Song YM, Choi SJ, Park SH, Lee SJ, Joo EY, Kim JK. A real-time,
personalized sleep intervention using mathematical modelling and
wearable devices. Sleep. 2023;46(9):zsad179.

38 Hong J, Choi SJ, Park SH, et al. Personalized sleep-wake patterns
aligned with circadian rhythm relieve daytime sleepiness. iScience.
2021;24(10):103129.

39 Swaminathan K, Klerman EB, Phillips AJK. Are individual differ-
ences in sleep and circadian timing ampliﬁed by use of artiﬁcial
light sources? J Biol Rhythms. 2017;32(2):165–176.

40 Postnova S, Postnov DD, Seneviratne M, Robinson PA. Effects of
rotation interval on sleepiness and circadian dynamics on forward
rotating 3-shift systems. J Biol Rhythms. 2014;29(1):60–70.

41 Zuidersma M, Lugtenburg A, van Zelst W, et al. Temporal dy-
namics of depression, cognitive performance and sleep in older
persons with depressive symptoms and cognitive impairments: a
series
Psychogeriatr.
eight
of
2022;34(1):47–59.

single-subject

studies.

Int

42 Merikangas KR, Swendsen J, Hickie IB, et al. Real-time mobile
monitoring of the dynamic associations among motor activity, en-
ergy, mood, and sleep in adults with bipolar disorder. JAMA Psy-
chiatry. 2019;76(2):190–198.

43 Schreiber T. Measuring information transfer. Phys Rev Lett.

2000;85(2):461–464.

44 Vicente R, Wibral M, Lindner M, Pipa G. Transfer entropy–a
model-free measure of effective connectivity for the neurosciences.
J Comput Neurosci. 2011;30(1):45–67.

45 Vejmelka M, Palus M. Inferring the directionality of coupling with
conditional mutual information. Phys Rev E Stat Nonlin Soft Matter
Phys. 2008;77(2):026214.

46 Timme NM, Lapish C. A tutorial
neuroscience. eNeuro. 2018;5(3).

for information theory in

47 Wibral M, Vicente R, Lizier JT. Directed information measures in

neuroscience. Springer; 2014.

48 Honey CJ, Kotter R, Breakspear M, Sporns O. Network structure of
cerebral cortex shapes functional connectivity on multiple time
scales. Proc Natl Acad Sci U S A. 2007;104(24):10240–10245.
49 Joshi R, Kommers D, Long X, et al. Cardiorespiratory coupling in
preterm infants. J Appl Physiol (1985). 2019;126(1):202–213.
50 Clark MT, Rusin CG, Hudson JL, et al. Breath-by-breath analysis of
cardiorespiratory interaction for quantifying developmental matu-
rity in premature infants. J Appl Physiol (1985). 2012;112(5):859–
867.

51 Mrowka R, Cimponeriu L, Patzak A, Rosenblum MG. Directionality
of coupling of physiological subsystems: age-related changes of
cardiorespiratory interaction during different sleep stages in babies.
Am J Physiol Regul Integr Comp Physiol. 2003;285(6):R1395–R1401.
52 Lucchini M, Burtchen N, Fifer WP, Signorini MG. Multi-para-
metric cardiorespiratory analysis in late-preterm, early-term, and
full-term infants at birth. Med Biol Eng Comput. 2019;57(1):99–106.
53 Rozo A, Morales J, Moeyersons J, et al. Benchmarking transfer
entropy methods for the study of linear and nonlinear cardio-
respiratory interactions. Entropy (Basel). 2021;23(8):939.

54 Demirer RM, Kesebir S. The entropy of chaotic transitions of EEG
phase growth in bipolar disorder with lithium carbonate. Sci Rep.
2021;11(1):11888.

55 Lian J, Luo Y, Zheng M, et al. Sleep-dependent anomalous cortical
information interaction in patients with depression. Front Neurosci.
2021;15:736426.

56 Ravan M, Noroozi A, Sanchez MM, et al. Discriminating between
bipolar and major depressive disorder using a machine learning

14

www.thelancet.com Vol 103 May, 2024

Articles

or II and control participants. JAMA Psychiatry. 2020;77(3):303–
310.

81 Esaki Y, Obayashi K, Saeki K, Fujita K, Iwata N, Kitajima T. As-
sociation between circadian activity rhythms and mood episode
relapse in bipolar disorder: a 12-month prospective cohort study.
Transl Psychiatry. 2021;11(1):525.

82 Karan M, Bai S, Almeida DM, Irwin MR, McCreath H, Fuligni AJ.
Sleep-wake timings in adolescence: chronotype development and
associations with adjustment. J Youth Adolesc. 2021;50(4):628–640.
83 Bai S, Karan M, Gonzales NA, Fuligni AJ. A daily diary study of
sleep chronotype among Mexican-origin adolescents and parents:
implications for adolescent behavioral health. Dev Psychopathol.
2021;33(1):313–322.

84 Cheung FTW, Li X, Hui TK, et al. Circadian preference and mental
health outcomes in youth: a systematic review and meta-analysis.
Sleep Med Rev. 2023;72:101851.

85 Daghlas I, Lane JM, Saxena R, Vetter C. Genetically proxied diurnal
preference, sleep timing, and risk of major depressive disorder.
JAMA Psychiatry. 2021;78(8):903–910.

86 Kim J, Jang S, Choe HK, Chung S, Son GH, Kim K. Implications of
circadian rhythm in dopamine and mood regulation. Mol Cells.
2017;40(7):450–456.

87 Jang S, Park I, Choi M, et al. Impact of the circadian nuclear re-
ceptor REV-ERBalpha in dorsal raphe 5-HT neurons on social
interaction behavior, especially social preference. Exp Mol Med.
2023;55(8):1806–1819.

88 Kawai K, Iwamoto K, Miyata S, et al. Comparison of poly-
somnography, single-channel electroencephalogram, Fitbit, and
sleep logs in patients with psychiatric disorders: cross-sectional
study. J Med Internet Res. 2023;25:e51336.

89 Ogasawara M, Takeshima M, Kosaka S, et al. Exploratory validation
of sleep-tracking devices in patients with psychiatric disorders. Nat
Sci Sleep. 2023;15:301–312.

90 Cook JD, Prairie ML, Plante DT. Utility of the ﬁtbit ﬂex to evaluate
sleep in major depressive disorder: a comparison against poly-
somnography
J Affect Disord.
2017;217:299–305.

and wrist-worn actigraphy.

91 Cook JD, Eftekari SC, Dallmann E, Sippy M, Plante DT. Ability of
the ﬁtbit alta HR to quantify and classify sleep in patients with
suspected central disorders of hypersomnolence: a comparison
against polysomnography. J Sleep Res. 2019;28(4):e12789.

92 Dong X, Yang S, Guo Y, Lv P, Wang M, Li Y. Validation of ﬁtbit
charge 4 for assessing sleep in Chinese patients with chronic
insomnia: a comparison against polysomnography and actigraphy.
PLoS One. 2022;17(10):e0275287.

93 Haghayegh S, Khoshnevis S, Smolensky MH, Diller KR,
Castriotta RJ. Accuracy of wristband Fitbit models in assessing
sleep: systematic review and meta-analysis. J Med Internet Res.
2019;21(11):e16273.

94 Eylon G, Tikotzky L, Dinstein I. Performance evaluation of ﬁtbit
charge 3 and actigraphy vs. polysomnography: sensitivity, speci-
ﬁcity, and reliability across participants and nights. Sleep Health.
2023;9(4):407–416.

95 Leng Y, Musiek ES, Hu K, Cappuccio FP, Yaffe K. Association
between circadian rhythms and neurodegenerative diseases. Lancet
Neurol. 2019;18(3):307–318.

96 Wijbenga RA, Blaauw FJ, Janus SIM, et al. Individual differences in
the temporal relationship between sleep and agitation: a single-
subject study in nursing home residents with dementia experi-
encing sleep disturbance and agitation. Aging Ment Health.
2022;26(8):1669–1677.

97 Kim DW, Zavala E, Kim JK. Wearable technology and systems
modeling for personalized chronotherapy. Curr Opin Syst Biol.
2020;21:9–15.

98 Kim DW, Mayer C, Lee MP, Choi SW, Tewari M, Forger DB.
Efﬁcient assessment of real-world dynamics of circadian rhythms
in heart rate and body temperature from wearable data. J R Soc
Interface. 2023;20(205):20230030.

99 Kim JK, Forger DB, Marconi M, et al. Modeling and validating
chronic pharmacological manipulation of circadian rhythms. CPT
Pharmacometrics Syst Pharmacol. 2013;2(7):e57.

100 Kim DW, Chang C, Chen X, et al. Systems approach reveals
photosensitivity and PER2 level as determinants of clock-modulator
efﬁcacy. Mol Syst Biol. 2019;15(7):e8838.

101 Keijzer H, Smits MG, Duffy JF, Curfs LM. Why the dim light
melatonin onset (DLMO) should be measured before treatment of
patients with circadian rhythm sleep disorders. Sleep Med Rev.
2014;18(4):333–339.

approach and
2023;146:30–39.

resting-state EEG data. Clin Neurophysiol.

57 Cho CH, Ahn YM, Kim SJ, et al. Design and methods of the mood
disorder cohort research consortium (MDCRC) study. Psychiatry
Investig. 2017;14(1):100–106.

58 Lee H-J, Cho C-H, Lee T, et al. Prediction of impending mood
episode recurrence using real-time digital phenotypes in major
depression and bipolar disorders in South Korea: a prospective
nationwide cohort study. Psychol Med. 2022;53:1–9.

59 Tse LA, Wang C, Rangarajan S, et al. Timing and length of
nocturnal sleep and daytime napping and associations with obesity
types in high-, middle-, and low-income countries. JAMA Netw
Open. 2021;4(6):e2113775.

60 Bijlenga D, van der Heijden KB, Breuk M, et al. Associations be-
tween sleep characteristics, seasonal depressive symptoms,
life-
style,
J Atten Disord.
2013;17(3):261–275.

and ADHD symptoms

in adults.

61 Forger DB, Jewett ME, Kronauer RE. A simpler model of the hu-
man circadian pacemaker. J Biol Rhythms. 1999;14(6):532–537.
62 Benloucif S, Guico MJ, Reid KJ, Wolfe LF, L’Hermite-Baleriaux M,
Zee PC. Stability of melatonin and temperature as circadian phase
markers and their relation to sleep times in humans. J Biol
Rhythms. 2005;20(2):178–188.

63 Brown EN, Choe Y, Shanahan TL, Czeisler CA. A mathematical
model of diurnal variations in human plasma melatonin levels. Am
J Physiol. 1997;272(3 Pt 1):E506–E516.

64 Hong JS, Wasden C, Han DH. Introduction of digital therapeutics.

Comput Methods Programs Biomed. 2021;209:106319.

65 Lee HA, Lee HJ, Moon JH, et al. Comparison of wearable activity
tracker with actigraphy for sleep evaluation and circadian rest-
activity rhythm measurement in healthy young adults. Psychiatry
Investig. 2017;14(2):179–185.

66 Lindner B, Auret L, Bauer M, Groenewald JW. Comparative anal-
ysis of granger causality and transfer entropy to present a decision
ﬂow for the application of oscillation diagnosis. J Process Control.
2019;79:72–84.

67 Zhang N, Zhao X. Quantile transfer entropy: measuring the het-
erogeneous information transfer of nonlinear time series. Commun
Nonlinear Sci Numer Simulat. 2022;111:106505.

68 Shorten DP, Spinney RE, Lizier JT. Estimating transfer entropy in
continuous time between neural spike trains or other event-based
data. PLoS Comput Biol. 2021;17(4):e1008054.

69 Ursino M, Ricci G, Magosso E. Transfer entropy as a measure of
brain connectivity: a critical analysis with the help of neural mass
models. Front Comput Neurosci. 2020;14:45.

70 Behrendt S, Dimpﬂ T, Peter FJ, Zimmermann DJ. RTransferEn-
tropy—quantifying information ﬂow between different time series
using effective transfer entropy. SoftwareX. 2019;10:100265.
71 Skeldon AC, Phillips AJ, Dijk DJ. The effects of self-selected light-
dark cycles and social constraints on human sleep and circadian
timing: a modeling approach. Sci Rep. 2017;7:45158.

72 Meyer N, Harvey AG, Lockley SW, Dijk D-J. Circadian rhythms and
disorders of the timing of sleep. Lancet. 2022;400(10357):1061–
1078.

73 Mendoza J, Vanotti G. Circadian neurogenetics of mood disorders.

Cell Tissue Res. 2019;377:81–94.

74 Takaesu Y, Inoue Y, Ono K, et al. Circadian rhythm sleep-wake
disorders predict shorter time to relapse of mood episodes in
euthymic patients with bipolar disorder: a prospective 48-week
study. J Clin Psychiatry. 2017;79(1):2651.

75 Tondo L, Miola A, Pinna M, Contu M, Baldessarini RJ. Differences
between bipolar disorder types 1 and 2 support the DSM two-
syndrome concept. Int J Bipolar Disord. 2022;10(1):21.

76 Frankland A, Cerrillo E, Hadzi-Pavlovic D, et al. Comparing the
phenomenology of depressive episodes in bipolar I and II disorder
and major depressive disorder within bipolar disorder pedigrees.
J Clin Psychiatry. 2015;76(1):32–38. quiz 9.

77 Radua J, Grunze H, Amann BL. Meta-analysis of the risk of sub-
sequent mood episodes in bipolar disorder. Psychother Psychosom.
2017;86(2):90–98.

78 Zimmerman M, Morgan TA. Problematic boundaries in the diag-
nosis of bipolar disorder: the interface with borderline personality
disorder. Curr Psychiatry Rep. 2013;15(12):422.

79 Bayes A, Parker G, Paris J. Differential diagnosis of bipolar II
disorder and borderline personality disorder. Curr Psychiatry Rep.
2019;21(12):125.

80 Lewis KJS, Richards A, Karlsson R, et al. Comparison of genetic
liability for sleep traits among individuals with bipolar disorder I

www.thelancet.com Vol 103 May, 2024

15

Articles

102 Khalsa SB, Jewett ME, Cajochen C, Czeisler CA. A phase response
curve to single bright light pulses in human subjects. J Physiol.
2003;549(Pt 3):945–952.

103 Brezing CA, Brixner DI. The rise of prescription digital therapeu-
tics in behavioral health. Adv Ther. 2022;39(12):5301–5306.
104 Campbell AN, Nunes EV, Matthews AG, et al. Internet-delivered
treatment for substance abuse: a multisite randomized controlled
trial. Am J Psychiatry. 2014;171(6):683–690.

105 Thorndike FP, Berry RB, Gerwien R, Braun S, Maricich YA. Pro-
tocol for digital real-world evidence trial for adults with insomnia
treated via mobile (DREAM): an open-label trial of a prescription
digital therapeutic for treating patients with chronic insomnia.
J Comp Effect Res. 2021;10(7):569–581.

106 McCarthy MJ, Gottlieb JF, Gonzalez R, et al. Neurobiological and
behavioral mechanisms of circadian rhythm disruption in bipolar
disorder: a critical multi-disciplinary literature review and agenda
for future research from the ISBD task force on chronobiology.
Bipolar Disord. 2022;24(3):232–263.

107 Diaz-Morales JF, Randler C, Arrona-Palacios A, Adan A. Validation of
the MESSi among adult workers and young students: general health
and personality correlates. Chronobiol Int. 2017;34(9):1288–1299.

108 Xu N, Shinohara K, Saunders KEA, Geddes JR, Cipriani A. Effect of
lithium on circadian rhythm in bipolar disorder: a systematic re-
view and meta-analysis. Bipolar Disord. 2021;23(5):445–453.
109 Johansson AS, Brask J, Owe-Larsson B, Hetta J, Lundkvist GB.
Valproic acid phase shifts the rhythmic expression of Period2::
Luciferase. J Biol Rhythms. 2011;26(6):541–551.

110 Silva S, Bicker J, Falcao A, Fortuna A. Antidepressants and circa-
interaction for the

dian rhythm: exploring their bidirectional
treatment of depression. Pharmaceutics. 2021;13(11):1975.

111 Serrano-Serrano AB, Marquez-Arrico JE, Navarro JF, Martinez-
Nicolas A, Adan A. Circadian characteristics in patients under
treatment for substance use disorders and severe mental illness
(Schizophrenia, Major Depression and Bipolar Disorder). J Clin
Med. 2021;10(19):4833.

112 Zou H, Zhou H, Yan R, Yao Z, Lu Q. Chronotype, circadian
rhythm, and psychiatric disorders: recent evidence and potential
mechanisms. Front Neurosci. 2022;16:811771.

113 McGlashan EM, Coleman MY, Vidafar P, Phillips AJK,
Cain SW. Decreased sensitivity of the circadian system to light
in current, but not
J Affect Disord.
2019;256:386–392.

remitted depression.

16

www.thelancet.com Vol 103 May, 2024
