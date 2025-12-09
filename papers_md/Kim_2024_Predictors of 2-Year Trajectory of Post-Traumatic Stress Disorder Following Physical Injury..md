# Kim_2024_Predictors of 2-Year Trajectory of Post-Traumatic Stress Disorder Following Physical Injury.

Wiley
Depression and Anxiety
Volume 2024, Article ID 5570405, 12 pages
https://doi.org/10.1155/2024/5570405

Research Article
Predictors of 2-Year Trajectory of Post-Traumatic Stress
Disorder Following Physical Injury

Jae-Min Kim ,1 Ju-Wan Kim ,1 Hee-Ju Kang
Jung-Chul Kim,2 Sung-Wan Kim ,1 Il-Seon Shin ,1 and Robert Stewart

,1 Ye-Jin Kim,1 Hyunseok Jang,2

3,4

1Department of Psychiatry, Chonnam National University Medical School, Gwangju, Republic of Korea
2Division of Trauma, Department of Surgery, Chonnam National University Medical School and Hospital, Gwangju,
Republic of Korea
3King’s College London (Institute of Psychiatry, Psychology and Neuroscience), London, UK
4South London and Maudsley NHS Foundation Trust, London, UK

Correspondence should be addressed to Jae-Min Kim; jmkim@chonnam.ac.kr and Robert Stewart; robert.stewart@iop.kcl.ac.uk

Received 8 February 2024; Revised 7 July 2024; Accepted 26 July 2024

Academic Editor: Lut Tamam

Copyright © 2024 Jae-Min Kim et al. This is an open access article distributed under the Creative Commons Attribution License,
which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

Objectives. This study investigated post-traumatic stress disorder (PTSD) trajectories and their predictors over a 2-year period, in
individuals recovering from physical injuries. Materials and Methods. Between June 2015 and January 2021, 1,142 patients from a
South Korean University Hospital Trauma Center underwent baseline evaluations, including PTSD-related measures and socio-
demographic characteristics. They were subsequently followed up for PTSD using the Clinician-Administered PTSD Scale at 3, 6, 12,
and 24 months. The analyzed sample consisted of 1,014 patients who were followed up at least once after the baseline and 3-month
evaluations. Latent class growth analysis and logistic regression models were used. Results. Five distinctive trajectories were identiﬁed:
resilient, worsening/recovery, worsening, recovery, and chronic groups. The worsening/recovery trajectory was associated with
previous traumatic events and trafﬁc-related injuries, while the worsening trajectory was linked to higher education and elevated
depressive symptoms. The recovery trajectory was characterized by female sex, childhood abuse, trafﬁc-related injuries, dissociative
subtype, and higher levels of anxiety and depressive symptoms. The chronic trajectory was predicted by the dissociative subtype and
heightened anxiety symptoms. Conclusion. These ﬁndings highlighted the heterogeneity of PTSD symptom development and, thus,
the importance of considering individual characteristics when assessing and addressing PTSD following physical injuries.

1. Introduction

Post-traumatic stress disorder (PTSD) is a multifaceted and
incapacitating mental condition that often emerges in the
aftermath of signiﬁcant traumatic experiences. Among these,
traumatic physical injuries resulting from accidents, acts of
violence, or other distressing incidents rank prominently as
triggers for PTSD development. Such injuries are closely
linked to enduring impairments in functioning and a dimin-
ished quality of life [1]. The identiﬁcation of predictors that
contribute to the onset and progression of PTSD is an essen-
tial step toward both the prevention and management of this
debilitating disorder. Therefore, many potential risk factors
have been investigated, including sociodemographic vari-
ables (such as age, gender, education, and socioeconomic

status), pre-existing health conditions (prior mental or physi-
cal disorders, past trauma, childhood adversities, substance
abuse, personality traits), trauma-related attributes (like injury
severity and dissociation), and peri-trauma states (psychological
distress and cognitive symptoms, as well as physiological indi-
cators like heart rate) [2, 3, 4].

Despite extensive investigations, ﬁndings on PTSD predic-
tors have been highly discrepant. A comprehensive systematic
review comprising 44 studies focused on PTSD predictors in
survivors of road trafﬁc accidents highlighted inconsistencies
between studies, with conﬂicting outcomes on nearly all inves-
tigated variables [5]. This heterogeneity in ﬁndings could poten-
tially be attributed not only to the fact that many studies have
assessed PTSD at a single speciﬁc time point following the
traumatic incident, spanning from 1 month to 2 years postevent

2

Depression and Anxiety

[6, 7], but also to variations in the assessment methods
employed across different studies.

Understanding the development of PTSD necessitates inte-
grating predictive factors within a theoretical framework that
accounts for the variability in its trajectories. The diathesis-stress
model posits that PTSD results from the interaction between
pre-existing vulnerabilities and traumatic stress, explaining the
variability in PTSD trajectories—from resilience to chronic
dysfunction—based on individual diatheses. Additionally, the
conservation of resources theory suggests that trauma leads
to PTSD by depleting critical coping resources, inﬂuencing
trajectories of worsening or recovery. Biopsychosocial
models further propose that the interplay of biological, psy-
chological, and social factors determines the onset and course of
PTSD, thereby inﬂuencing the trajectory an individual might
follow [8].

Recent advancements in machine learning and quantita-
tive forecasting have begun to offer new insights into varied
trajectories of PTSD, such as symptom ﬂuctuations, delayed
onsets, and diverse recovery patterns. For instance, studies by
Galatzer-Levy et al. [9, 10] and Tomas et al. [11] have applied
machine learning techniques to forecast PTSD trajectories
from early trauma responses, demonstrating how complex
data-driven approaches can reveal comprehensive patterns
of resilience and dysfunction following trauma. These pat-
terns include distinct groups such as consistently low symp-
tomatology (resilient),
initial high symptoms followed by
gradual improvement (recovery), and persistent high symptom-
atology (chronic). Similarly, Schultebraucks et al. [12, 13, 14]
have contributed signiﬁcant ﬁndings on predicting PTSD trajec-
tories using a variety of biomedical and psychosocial data, which
could potentially reﬁne our understanding of PTSD develop-
ment over time. Specially, Galatzer-Levy et al. [15] identiﬁed
three distinct trajectories (nonremitting, slow remitting, and
rapid remitting) during a 15-month follow-up, evaluating pre-
dictors from emergency room assessments and 10 days poste-
vents between remitters and nonremitters. Furthermore,
subsequent studies have identiﬁed four trajectories (resilient,
delayed-onset, recovery, and nonremitting) over shorter
follow-up periods of 6–12 months [11, 14]. One notable lon-
gitudinal study, spanning a span of 6 years, segmented the
trajectories of PTSD into ﬁve distinct patterns—resilient,
worsening, worsening/recovery, recovery, and chronic—and
highlighted several baseline factors that appeared to predict
poorer trajectories [16]. However, this investigation examined
a limited array of predictive elements, focusing on sociodemo-
graphic factors and a handful of injury-related variables.

A comprehensive assessment of potential predictors, uti-
lizing sociodemographic and clinical proﬁles primarily derived
from self-reports, observer-rating scales, and electronic health
records and encompassing both resilience and vulnerability at
baseline, combined with an investigation of their longitudinal
associations with different PTSD trajectories, could improve
information on factors inﬂuencing the intricate courses of
PTSD and have the potential to address existing gaps in
knowledge. Using data obtained from a prospective 2-year
study involving Korean patients with physical injuries, we
aimed to investigate the associations between baseline factors

and PTSD trajectories. We hypothesize that distinct PTSD
trajectories will emerge and that these trajectories will be
signiﬁcantly associated with speciﬁc sociodemographic and
clinical predictors.

2. Materials and Methods

2.1. Study Overview and Participants. This analysis constitu-
tes an integral component of the biomarker-based diagnostic
algorithm for post-traumatic syndrome (BioPTS) study, aimed
at developing accurate models for the diagnosis and prediction
of PTSD. Study details have been previously published in a
protocol paper [17] and further discussed in relation to differ-
ential predictors of PTSD in a recent study [18]. In summary,
the study’s participants were prospectively enrolled from patients
who had recently undergone hospitalization for physical inju-
ries between June 2015 and January 2021 at the Department
of Trauma Center of Chonnam National University Hospital
(CNUH) in Gwangju, South Korea. The severity of injuries
was assessed using the Injury Severity Score (ISS) [19] and the
Glasgow Coma Scale (GCS) [20]. Study inclusion criteria
comprised the following: (i) individuals aged 18 years or older
at the index injury; (ii) patients hospitalized for more than
24 hr after sustaining a moderate to severe physical injury
(ISS ≥ 9); and (iii) individuals sufﬁciently proﬁcient in the
Korean language to comprehend the study protocol. Exclusion
criteria were as follows: (i) moderate or severe brain injury (GCS
< 10); (ii) physical injuries resulting from suicide attempts; (iii)
conditions hindering comprehensive psychiatric evaluation due
to severe physical ailments; (iv) prior history of psychiatric dis-
orders, including psychotic disorder, bipolar disorder, or alcohol
or substance use disorders other than depressive and anxiety
disorders; (v) signiﬁcant cognitive impairments due to organic
mental or neurocognitive disorders; and (vi) pre-existing con-
vulsive disorders or a history of anticonvulsant use. Participants
satisfying the eligibility criteria and expressing willingness to
partake in the study underwent psychiatric assessments within
1 month of their hospitalization, conducted in person. Subse-
quent follow-up evaluations were conducted via telephone
interviews at 3, 6, 12, and 24 months post the physical injury
event. The culmination of patient visits occurred in January
2023. Ethical clearance for this study was obtained from the
Chonnam National University Hospital Institutional Review
Board (CNUH 2015-148). All participants meticulously
reviewed the consent form, and written informed consent
was duly acquired.

2.2. Baseline Evaluations

2.2.1. Trauma and PTSD-Related Characteristics. To com-
prehensively assess trauma and PTSD-related characteristics
at baseline, several key aspects were evaluated. The type of
accidental injury was evaluated using the life events checklist
(LEC) [21], which aided in identifying the speciﬁc type of
traumatic event that participants had experienced. To stream-
line the analysis, given the number of participants, injury
types were divided into four main categories: (i) trafﬁc-related
injuries, which include those sustained in automobile acci-
dents, motorcycle crashes, and bicycle collisions; (ii) falls,

Depression and Anxiety

3

referring to injuries from falling from heights such as ladders,
stairs, or other elevated platforms; (iii) slips, encompassing
injuries resulting from slipping sideways on wet or uneven
surfaces; and (iv) other types of injuries, which cover a range
of less common mechanisms not included in the aforemen-
tioned categories, such as burns and electric shocks. Injury
severity was evaluated with the ISS and GCS as described
above. The occurrence of surgical procedures related to the
injury was documented. Symptom severity and diagnoses of
PTSD were gauged by the Clinician-Administered PTSD
Scale (CAPS), applying the Diagnostic and Statistical Manual
of Mental Disorders, 5th Edition (DSM-V), criteria (CAPS-5)
[22]. Symptom severity for each of the 20 DSM-V PTSD symp-
toms was determined by multiplying the frequency (Likert Scale,
ranging from 0 to 4) by the intensity (Likert Scale, ranging from
0 to 4) of the assessed symptoms, with the total severity score
representing the overall severity of PTSD symptoms. This struc-
tured clinical interview is among the most widely used tools for
evaluating PTSD and has demonstrated high reliability and
validity [23]. The presence of a dissociative subtype of PTSD
was evaluated within the framework of the CAPS-5 assessment.
Higher scores on ISS and CAPS-5 and lower scores on GCS
indicate more pronounced symptomatology.

2.2.2. Sociodemographic Characteristics. The following base-
line sociodemographic characteristics were collected: age, sex,
duration of education, marital status (currently married or not),
cohabitation status (living alone or not), religion (religious
observance or not), occupational state (current employed or
not), and monthly income (above or below 3,000 USD).

2.2.3. Pre-Trauma Characteristics. Several pre-trauma char-
acteristics were assessed to gain insights into participants’
backgrounds and potential factors that could contribute to
their responses following severe physical injury. Prior histories
of psychiatric disorders were documented, including depres-
sive disorders, panic disorder, agoraphobia, social phobia, and
generalized anxiety disorder. Participants’ experiences of pre-
vious lifetime traumatic events were examined using the LEC
[21], with the occurrence of at least one type of event catego-
rized as present for analysis purposes. Instances of previous
suicidal attempts were identiﬁed, deﬁned as intentional self-
harm with some intention to die, regardless of objective lethal-
ity [24]. A number of physical disorders were assessed using a
questionnaire covering 15 systems or diseases. Personality
traits were evaluated by the Big Five Inventory [25] and were
clustered into resilient and vulnerable types using a standard
approach (detailed in the Supplementary Materials Personality
Assessments section). Childhood abuse experiences were eval-
uated with the Nemesis Childhood Trauma Interview [26],
which encompassed emotional/psychological, physical, and
sexual abuse before the age of 16. A broad deﬁnition of “child-
hood abuse” (having at least one type of abuse) was used for
the analysis. Levels of resilience and social support were mea-
sured by the Connor–Davidson Resilience Scale (CDRS) [27]
and the Multidimensional Scale of Perceived Social Support
(MSPSS), respectively. Smoking status and histories were
evaluated and divided into current smoking or not.

Alcohol-related problems were screened by the Alcohol Use
Disorders Identiﬁcation Test (AUDIT) [28]. Body mass index
was calculated. Lower scores on CDRS and higher scores on
MSPSS and AUDIT indicate higher symptomatology.

2.2.4. Peri-Trauma Characteristics. During the peri-trauma
period (from the index injury to the baseline evaluation),
participants’ symptoms and functional status were assessed
using various evaluation scales. Depressive and anxiety symp-
toms were evaluated by the Hospital Anxiety Depression Scale-
Depression subscale (HADS-D) and Anxiety subscale (HADS-A)
[29], respectively; physical function by the Modiﬁed Barthel
Index (MBI) [30]; subjective cognitive difﬁculties by the Per-
ceived Deﬁcits Questionnaire-Depression (PDQD) [31]; and
hypochondriacal fears by the Illness Attitude Scale (IAS) [32].
Higher scores on HADS-D, HADS-A, PDQD, and IAS and
lower scores on MBI indicate more severe symptomatology.
Vital signs, including systolic and diastolic blood pressures
and heart rate, were measured at the time of baseline evalua-
tion to check physiological status.

2.3. Follow-up Evaluations. CAPS-5 was administered to track
the progression of symptoms and the presence of PTSD over a
2-year period. The interviews were carried out via telephone, a
method that has been demonstrated to be as valid and reliable
as face-to-face interviews [33].

2.4. Statistical Analysis. Since the delayed onset type of PTSD
is deﬁned as PTSD development at least 6 months after the
traumatic events, participants evaluated at least once after
both baseline and 3-month evaluations comprised the ana-
lyzed sample. From a previous longitudinal study on PTSD
following traumatic injury [16], we assumed that there would
be distinct PTSD trajectory groups that could be derived
from CAPS-5 scores across 5 time points over 2 years. Latent
class growth analysis (LCGA) was conducted to identify these
trajectory groups. We selected LCGA over latent growth mix-
linear modeling due to its
ture modeling or hierarchical
robust handling of missing data through maximum likelihood
estimation. This method efﬁciently utilizes all available data
points without the need for imputation, which proved partic-
ularly advantageous given the missing follow-up assessments
in our dataset. This approach ensures the integrity of our class
assignments and the robustness of our ﬁndings. The best-
ﬁtting unconditional model was identiﬁed by comparing the
model ﬁt of progressive numbers of classes (detailed in Sup-
plementary Materials LCGA for PTSD Trajectories section,
Figure S1 and Table S1). Baseline data on sociodemographic
characteristics, the trauma itself, and pre- and peri-trauma
characteristics were compared between the derived trajectory
groups using analysis of variance or χ2 tests. Given that the
sample size for each trajectory group was limited, categorical
variables were collated into binary variables. Speciﬁcally, the
four accidental injury types were categorized as trafﬁc-related
injuries vs. other injuries, considering the distribution of injury
types. Those characteristics signiﬁcantly associated with trajec-
tory groups (P <0:05) were entered into logistic regression
analyses. These models were used both in total, considering
all trajectory groups collectively, and separately for each

4

Depression and Anxiety

4,581 Patients with physical injury screened

3,439 Excluded
2,359 Unsuitable criteria
1,413 In severe physically ill state
468 Inability to complete questionnaires
233 Early discharge before investigation
134 Had significant brain injury
42 Prior history of psychiatric disorder
36 Injury by suicidal attempts
33 Aged under 18
1,080 Refused participation

1,142 Patients completed the baseline evaluation

1,047 Patients completed the 3-month evaluation

1,014 Patients completed the 6-month evaluation

971 Patients completed the 12-month evaluation

918 Patients completed the 24-month evaluation

FIGURE 1: Recruitment and patient ﬂow.

95 Exited from the study
81 Lost to follow-up
14 Refused participation

33 Exited from the study
21 Lost to follow-up
12 Refused participation

43 Exited from the study
33 Lost to follow-up
10 Refused participation

53 Exited from the study
36 Lost to follow-up
17 Refused participation

individual trajectory group to identify and distinguish inde-
pendent predictors that inﬂuence the likelihood of individuals
belonging to speciﬁc PTSD trajectory groups. Corrections for
multiple comparisons were not applied, as the primary goal
of these analyses was to broadly identify potential predictors
across different PTSD trajectory groups. This approach
aims to minimize the risk of overlooking signiﬁcant vari-
ables, thereby reducing the likelihood of Type II errors. All
statistical tests were two-sided with a signiﬁcance level of
0.05. Statistical analyses were carried out using the SPSS
21.0 and STATA 12.0 software.

3. Results

3.1. Recruitment and Patient Flow. The ﬂow of patients from
the baseline assessment to the 24-month follow-up is illus-
trated in Figure 1. Of 4,581 patients screened, 1,142 met the
eligibility criteria and agreed to participate. Of 1,142 patients
evaluated at baseline, 1,047 (91.7%) were successfully fol-
lowed up at the 3-month point, 1,014 (88.8%) at the 6-month
point, 971 (85.0%) at the 12-month point, and 918 (80.4%) at
the 24-month point. The mean follow-up times were 3.4 months
(SD = 0.4), 6.6 months (SD = 0.4), 12.6 months (SD = 0.4), and

Depression and Anxiety

5

5
-
S
P
A
C

f
o
s
e
r
o
c
s
n
a
e

M

60

50

40

30

20

10

0

Baseline

3-Month

6-Month

12-Month 24-Month

Chronic (1.1%)
Worsening (2.7%)
Worsening/recovery (4.2%)

Recovery (5.4%)
Resilient (75.3%)

FIGURE 2: Five trajectories of post-traumatic stress disorder (PTSD)
following physical injury. Data are mean scores of the Clinician
Administered PTSD Scale for Diagnostic and Statistical Manual
of Mental Disorders, 5th edition (CAPS-5).

24.4 months (SD = 0.6), reﬂecting both the scheduled assess-
ment intervals and the actual variability in when these assess-
ments were conducted. Overall, 1,014 patients were followed
up at least once after the baseline and 3-month evaluations,
constituting the analyzed sample. As previously detailed, we
employed LCGA, which utilizes maximum likelihood estima-
tion to handle missing data. This statistical approach allows
for the utilization of all available data points for each individ-
ual, efﬁciently managing missing values without necessitating
imputation. There were no statistical differences in any base-
line characteristic between the 1,014 patients included and the
128 who did not follow-up after the 3-month evaluations (all
P-values > 0.1). The mean (SD) age of participants was 56.8
(17.1) years. Of the participants, 312 (30.8%) were female. The
average (SD) educational attainment was 10.7 (4.1) years.
Additionally, 66.7% of participants were married, 15.0% lived
alone, 41.7% observed a religion, 82.1% were employed, and
42.7% reported a monthly income of at least 3,000 USD.

3.2. PTSD Trajectory Groups. In the baseline assessment, 75
(7.4%) of 1,014 patients were diagnosed as having PTSD using
CAPS-5, and their mean (SD) PTSD severity was 39.5 (10.5)
points. After a 2-year follow-up period, 35 (3.8%) of 918
patients diagnosed using CAPS-5 were identiﬁed, with a
mean (SD) PTSD severity of 40.1 (11.9) points. The LCGA
identiﬁed a ﬁve-cluster model as the best-ﬁtting model char-
acterized by its efﬁciency, parsimony, and capacity to delin-
eate ﬁve distinct PTSD trajectories (detailed in the online
supplement). The mean scores of the CAPS-5 for these tra-
jectory groups are displayed in Figure 2. Of note, at all evalu-
ation points, mean CAPS-5 scores were signiﬁcantly higher
(with all P-values < 0.001) for each of the four PTSD trajec-
tory groups when compared to the resilient group. The shape
of these trajectories closely resembled those observed in
a prior study [16]. Consequently, we opted to employ the

same group names as follows: (i) resilient group (N = 860,
84.8%), exhibiting consistently low levels of PTSD symptoms
from baseline to the last follow-up assessment; (ii) worsening/
recovery group (N = 48, 4.7%): displayed relatively low levels
of PTSD symptoms at baseline, which then increased but
subsequently decreased by the last follow-up; (iii) worsening
group (N = 31, 3.1%) with initially relatively low levels of
PTSD symptoms at baseline then experiencing an increase
in symptoms during the follow-up period; (iv) recovering group
(N = 62, 6.1%), exhibiting relatively high levels of PTSD symp-
toms at baseline, which subsequently decreased during the
follow-up assessments; and (v) chronic group (N = 13; 1.3%),
consistently displaying high levels of PTSD symptoms from
baseline through to the last follow-up assessment.

3.3. Baseline Characteristics by PTSD Trajectory Groups. Table 1
presents a comparison of baseline characteristics among the ﬁve
distinct PTSD trajectory groups. Signiﬁcant group differences
were observed in age, sex, education, previous psychiatric dis-
orders, previous traumatic events, number of physical disorders,
childhood abuse, injury type, dissociative subtype, and scores
on HADS-A, HADS-D, and PDQD.

3.4. Independent Predictors of PTSD Trajectory Groups.
These 12 variables were entered into logistic regression mod-
els, the results of which are presented in Table 2. Being in any
signiﬁcant PTSD trajectory group compared to the resilient
group was predicted by baseline higher education, previous
traumatic events, trafﬁc-related injury type, dissociative PTSD
subtype, and higher scores on HADS-A and HADS-D. The
analysis was then conducted separately for each speciﬁc trajec-
tory group compared to the resilient group, revealing distinct
and varying results for each subgroup. The worsening/recovery
trajectory was predicted by previous traumatic events and
trafﬁc-related injury type; the worsening trajectory by higher
education and higher scores on HADS-D; the recovering tra-
jectory by female sex, childhood abuse, trafﬁc-related injury
type, dissociative subtype, and higher scores on HADS-A and
HADS-D; and chronic trajectory by dissociative subtype and
higher scores on HADS-A.

4. Discussion

The principal ﬁndings of this 2-year prospective longitudinal
study involving patients with severe physical injuries are
twofold. First, the study conﬁrmed the existence of ﬁve dis-
tinct trajectories of PTSD symptoms over the 2-year follow-
up period. Second, it was found that each of these trajectories
was predicted by different baseline characteristics.

Our identiﬁcation of ﬁve trajectory groups and their lon-
gitudinal patterns closely align with the results from a previ-
ous longitudinal study [16]. Both studies shared a similar
research design, in which participants were drawn from indi-
viduals who had experienced physical injuries, and the assess-
ment of PTSD was conducted using the CAPS. The primary
distinction between the two studies lies in the duration of the
follow-up period. In our study, the follow-up period was
2 years, while the previous study extended to 6 years. Despite
this difference in follow-up duration, the number of distinct

 
 
 
6

Depression and Anxiety

.
s
e
i
r
u
n

j

i

l
a
c
i
s
y
h
p

h
t
i

w
s
t
n
e
i
t
a
p

4
1
0
1

,

n

i

s
r
a
e
y

o
w

t

r
o
f

y
r
o
t
c
e
j
a
r
t

r
e
d
r
o
s
i

d

s
s
e
r
t
s

c
i
t
a
m
u
a
r
t
-
t
s
o
p

y
b

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c

e
n

i
l
e
s
a
B

:

1

E
L
B
A
T

a
e
u
l
a
v
-
P

s
t
n
e
i
c
ﬁ
f
e
o
c

l
a
c
i
t
s
i
t
a
t
S

)
3
1
=
N

(

c
i
n
o
r
h
C

)
2
6
=
N

(

y
r
e
v
o
c
e
R

)
1
3
=
N

(

i

g
n
n
e
s
r
o
W

i

/
g
n
n
e
s
r
o
W

)
8
4
=
N

(

y
r
e
v
o
c
e
r

4
1
0

.

0

1
0
0

.

0
<

5
0
0
0

.

7
6
5
0

.

5
7
2
0

.

6
6
0
0

.

9
9
4
0

.

3
0
2
0

.

2
4
0
0

.

1
0
0

.

0
<

0
2
6
0

.

6
3
0
0

.

2
5
7
0

.

7
2
0
0

.

6
5
2
0

.

4
6
3
0

.

0
2
2
0

.

0
7
1
0

.

3
0
4
0

.

5
1
0
0

.

0
6
1
0

.

6
9
9
0

.

8
8
0
0

.

1
0
0

.

0
<

1
0
0
0
<

.

1
0
0

.

0
<

6
9
6
0

.

9
1
1
0

.

1
0
0

.

0

9
5
0
0

.

3
4
3
0

.

4
6
1
0

.

4
7
8
0

.

.

6
5
1
3
=
F

.

2
8
3
0
2
=
2
χ

.

7
9
6
3
=
F

.

6
4
9
2
=
2
χ

.

7
1
1
5
=
2
χ

.

8
2
8
8
=
2
χ

.

4
6
3
3
=
2
χ

.

0
5
9
5
=
2
χ

.

8
0
9
9
=
2
χ

.

8
0
0
9
2
=
2
χ

.

0
4
6
2
=
2
χ

.

5
7
5
2
=
F

.

3
1
9
1
=
2
χ

.

5
4
5
5
=
2
χ

.

1
3
3
1
=
F

.

3
8
0
1
=
F

.

1
3
7
5
=
2
χ

.

7
0
6
1
=
F

.

6
0
0
1
=
F

.

5
8
3
2
1
=
2
χ

.

9
4
6
1
=
F

.

5
4
0
0
=
F

.

2
9
0
8
=
2
χ

.

7
5
4
3
4
1
=
2
χ

.

3
9
3
0
9
=
F

.

4
7
4
0
5
=
F

.

5
5
5
0
=
F

.

8
3
8
1
=
F

.

1
7
9
4
=
F

.

1
8
2
2
=
F

.

5
2
1
1
=
F

.

3
3
6
1
=
F

.

7
0
3
0
=
F

.

)
4
4
1
(

.

0
7
4

.

)
2
6
4
(

6

.

)
3
2
(

.

6
2
1

.

)
2
6
4
(

6

)
0
0
(

.

0

.

)
2
9
6
(

9

)
7
7
(

.

1

.

)
2
6
4
(

6

.

)
4
5
1
(

.

)
8
0
3
(

2

4

.

)
0
0
(

0

.

)
4
1
(

2
1

.

.

)
5
1
6
(

.

)
4
5
1
(

8

2

.

)
5
5
1
(

.

7
9
5

.

)
8
1
1
(

.

4
6
3

.

)
5
8
3
(

5

)
1
7
(

.

.

2
6

.

)
0
3
(

.

6
2
2

.

)
2
6
4
(

6

.

)
3
7
(

.

1
5
1

.

)
4
0
(

.

9
4
1

.

)
2
9
6
(

.

)
5
1
6
(

9

8

)
9
4
(

.

.

5
1
1

.

)
0
5
(

.

4
1
1

)
7
7
(

.

.

5
4
2

.

)
0
5
3
(

.

9
9
5

.

)
3
8
1
(

.

8
2
1

.

)
5
3
2
(

.

3
3
6

.

)
6
0
1
(

.

8
4
1
1

)
0
7
(

.

.

9
9
6

)
9
9
(

.

.

8
0
8

.

)
7
6
1
(

.

7
6
5

.

)
8
4
5
(

4
3

)
4
4
(

.

.

7
0
1

.

)
6
0
3
(

9
1

.

)
5
4
1
(

9

.

)
4
8
4
(

0
3

.

)
6
2
2
(

4
1

.

)
1
8
5
(

6
3

.

)
9
2
1
(

8

)
5
6
(

.

)
2
3
(

.

4

2

)
9
1
(

.

7
1

.

.

)
9
1
4
(

6
2

.

)
3
1
1
(

7

.

)
6
7
1
(

.

0
2
6

)
9
9
(

.

.

2
5
3

.

)
0
1
2
(

3
1

.

)
7
9
(

7
7

.

)
5
3
(

.

.

3
3
2

.

)
7
9
5
(

7
3

)
4
6
(

.

.

3
5
1

)
7
0
(

.

.

8
4
1

.

)
5
9
5
(

7
3

.

)
7
9
5
(

7
3

)
5
4
(

.

9
8

.

)
5
4
(

.

.

5
2
1

)
8
4
(

.

.

1
4
2

.

)
9
0
3
(

.

4
9
4

.

)
5
2
1
(

.

9
1
1

.

)
1
2
2
(

.

6
3
6

.

)
6
2
1
(

.

3
8
1
1

)
8
8
(

.

.

6
0
7

.

)
2
0
1
(

.

9
8
7

.

)
4
3
1
(

.

8
8
4

.

)
5
5
3
(

1
1

)
6
3
(

.

.

1
3
1

.

)
8
5
2
(

8

)
7
9
(

.

3

.

)
6
1
5
(

6
1

.

)
9
2
1
(

4

.

)
8
4
5
(

7
1

.

)
7
9
(

.

)
7
9
(

)
0
0
(

.

3

3

0

)
2
1
(

.

9
0

.

.

)
2
5
4
(

4
1

)
5
6
(

.

2

.

)
6
6
1
(

.

7
7
6

.

)
7
0
1
(

.

4
8
3

.

)
0
9
2
(

9

)
9
9
(

.

.

1
1
1

)
4
3
(

.

.

1
4
2

.

)
2
5
4
(

4
1

)
5
6
(

.

.

9
6
1

)
6
0
(

.

.

8
4
1

.

)
7
7
6
(

1
2

.

)
1
6
1
(

5

)
3
3
(

.

2
4

.

)
8
4
(

.

9
6

.

)
8
3
(

.

.

7
5
2

.

)
2
5
3
(

.

2
6
5

.

)
7
1
1
(

.

6
5

.

)
7
5
1
(

.

8
3
5

.

)
8
0
1
(

.

4
9
1
1

)
6
8
(

.

.

3
3
7

.

)
5
1
1
(

.

2
7
7

.

)
8
3
1
(

.

9
4
5

.

)
2
9
2
(

4
1

.

)
0
3
(

.

1
1
1

.

)
1
7
2
(

3
1

)
3
8
(

.

4

.

)
0
0
5
(

4
2

.

)
5
2
1
(

6

.

)
7
1
4
(

0
2

.

)
6
4
1
(

.

)
4
0
1
(

7

5

)
2
4
(

.

2

)
0
2
(

.

9
1

.

.

)
8
5
4
(

2
2

)
3
6
(

.

3

.

)
1
7
1
(

.

6
6
6

.

)
4
0
1
(

.

8
4
3

.

)
6
9
3
(

9
1

.

)
5
0
1
(

.

5
0
1

.

)
1
3
(

.

3
4
2

.

)
5
2
6
(

0
3

.

)
6
5
(

.

6
4
1

)
6
0
(

.

.

9
4
1

.

)
5
2
6
(

0
3

.

)
7
6
1
(

8

)
7
3
(

.

7
3

.

)
8
4
(

.

0
7

.

)
5
4
(

.

.

1
4
2

.

)
0
3
3
(

.

1
1
5

.

)
1
1
1
(

5
8

.

.

)
0
2
2
(

.

3
5
6

.

)
5
4
1
(

.

6
1
1
1

)
4
9
(

.

.

7
8
6

.

)
1
1
1
(

.

9
7
7

)
0
6
8
=
N

(

t
n
e
i
l
i
s
e
R

.

)
4
7
1
(

.

3
7
5

.

)
7
8
2
(

7
4
2

)
1
4
(

.

.

6
0
1

.

)
0
4
3
(

2
9
2

.

)
8
5
1
(

6
3
1

.

)
0
0
4
(

4
4
3

.

)
1
8
1
(

6
5
1

.

)
4
8
5
(

2
0
5

)
2
6
(

.

3
5

)
5
3
(

.

0
3

)
9
1
(

.

6
1

)
1
2
(

.

0
2

.

.

)
4
3
4
(

3
7
3

)
5
5
(

.

7
4

.

)
5
5
1
(

.

4
5
6

)
9
9
(

.

.

7
4
3

.

)
1
7
2
(

3
3
2

.

)
0
0
1
(

.

4
0
1

)
4
3
(

.

.

6
3
2

.

)
5
3
4
(

4
7
3

)
7
5
(

.

.

5
4
1

)
7
0
(

.

.

8
4
1

.

)
2
1
5
(

0
4
4

)
9
9
(

.

5
8

)
9
2
(

.

.

5
2

)
5
4
(

.

8
4

.

)
3
5
(

.

.

4
4
2

.

)
3
1
3
(

.

7
8
5

.

)
3
1
1
(

2
6

.

.

)
4
0
2
(

.

3
9
5

.

)
7
3
1
(

.

8
9
1
1

)
2
9
(

.

.

3
2
7

.

)
2
1
1
(

.

3
8
7

s
e
r
o
c
s

)

D
S
(
n
a
e
m

,
t
r
o
p
p
u
s

l
a
i
c
o
s
d
e
v
i
e
c
r
e
p
f
o
e
l
a
c
s

l
a
n
o
i
s
n
e
m
i
d
i
t
l
u
M

s
e
r
o
c
s

)

D
S
(

n
a
e
m

,
e
l
a
c
S

e
c
n
e
i
l
i
s
e
R
n
o
s
d
i
v
a
D
–

r
o
n
n
o
C

)

D
S
(

n
a
e
m

,
s
r
e
d
r
o
s
i

d

l
a
c
i
s
y
h
p

f
o

r
e
b
m
u
N

)

%

(

N

,

y
t
i
l
a
n
o
s
r
e
p

e
l
b
a
r
e
n
u
V

l

D
S
U
0
0
0
3
<
)

,

%

(

N

,
e
m
o
c
n

i

y
l
h
t
n
o
M

)

%

(

N

,
s
u
t
a
t
s

d
e
y
o
l
p
m
e
n
U

)

%

(

N

,
s
r
e
d
r
o
s
i
d

c
i
r
t
a
i
h
c
y
s
p

s
u
o
i
v
e
r
P

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c

a
m
u
a
r
t
-
e
r
P

)

%

(

)

%

(

N

,
s
t
n
e
v
e

c
i
t
a
m
u
a
r
t

s
u
o
i
v
e
r
P

N

,
t
p
m
e
t
t
a

l
a
d

i
c
i
u
s

s
u
o
i
v
e
r
P

d
e
i
r
r
a
m
n
u

)

%

(

N

,
s
u
t
a
t
s

l
a
t
i
r
a

M

s
r
a
e
y

)

D
S
(

n
a
e
m

,

n
o
i
t
a
c
u
d
E

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c

c
i
h
p
a
r
g
o
m
e
d
o
i
c
o
S

s
r
a
e
y

)

D
S
(

n
a
e
m

,
e
g
A

e
l
a
m
e
f

)

%

(

N

,

x
e
S

)

%

(

N

,
e
c
n
a
v
r
e
s
b
o

s
u
o
i
g
i
l
e
R

)

%

(

N

,
e
n
o
l
a

g
n
i
v
i
L

)

%

(

N

,
e
s
u
b
a

d
o
o
h
d

l
i

h
c

y
n
A

s
e
r
o
c
s

)

D
S
(

n
a
e
m

,
t
s
e
t

n
o
i
t
a
c
ﬁ
i
t
n
e
d

i

s
r
e
d
r
o
s
i
d

e
s
u

l
o
h
o
c
l
A

)

D
S
(

n
a
e
m

,

x
e
d
n

i

s
s
a
m
y
d
o
B

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c

d
e
t
a
l
e
r
-
a
m
u
a
r
T

s
e
r
o
c
s

)

D
S
(

n
a
e
m

,
e
r
o
c
S

y
t
i
r
e
v
e
S

y
r
u
n
I

j

s
e
r
o
c
s

)

D
S
(

n
a
e
m

,
e
l
a
c
S

a
m
o
C
w
o
g
s
a
l
G

)

%

(

N

,

y
r
u
n

j

i

e
h
t

r
o
f

y
r
e
g
r
u
s

t
o
G

d
e
t
a
l
e
r
-
c
ﬁ
f
a
r
t

)

%

(

N

,
e
p
y
t

y
r
u
n
I

j

)

%

(

N

,
e
p
y
t
b
u
s

e
v
i
t
a
i
c
o
s
s
i

D

s
e
r
o
c
s

e
l
a
c
s
b
u
s

n
o
i
s
s
e
r
p
e
d
-
e
l
a
c
S

n
o
i
s
s
e
r
p
e
D
y
t
e
i
x
n
A

l
a
t
i
p
s
o
H

s
e
r
o
c
s

e
l
a
c
s
b
u
s

y
t
e
i
x
n
a
-
e
l
a
c
S

n
o
i
s
s
e
r
p
e
D
y
t
e
i
x
n
A

l
a
t
i

p
s
o
H

)

D
S
(

n
a
e
m

,
s
t
n
e
m
e
r
u
s
a
e
m
d
n
a

s
e
l
a
c
s

t
n
e
m

s
s
e
s
s
a

a
m
u
a
r
t
-
i
r
e
P

s
e
r
o
c
s

n
o
i
s
s
e
r
p
e
D
-
e
r
i
a
n
n
o
i
t
s
e
u
Q

s
t
i
c
ﬁ
e
D
d
e
v
i
e
c
r
e
P

s
e
r
o
c
s

x
e
d
n
I

l
e
h
t
r
a
B

i

d
e
ﬁ
d
o
M

s
e
r
o
c
s

n
o
i
t
a
n
m
a
x
E

i

e
t
a
t
S

l
a
t
n
e
M

-
i
n
M

i

)
g
H
m
m

(

e
r
u
s
s
e
r
p

d
o
o
l
b

c
i
l
o
t
s
a
i
D

)
g
H
m
m

(

e
r
u
s
s
e
r
p

d
o
o
l
b

c
i
l
o
t
s
y
S

e
t
u
n
m

i

r
e
p

e
t
a
r

t
r
a
e
H

s
e
r
o
c
s

e
l
a
c
S

e
d
u
t
i
t
t

A
s
s
e
n

l
l
I

)

%

(

N

,
r
e
k
o
m

s

t
n
e
r
r
u
C

.
e
c
n
a
c
ﬁ
n
g
i
s

i

l
a
c
i
t
s
i
t
a
t
s

s
e
t
a
c
i
d
n

i

e
l
y
t
s

d
l
o
B

.
e
t
a
i
r
p
o
r
p
p
a

s
a

,
s
t
s
e
t

2
χ

r
o

e
c
n
a
i
r
a
v

f
o

s
i
s
y
l
a
n
A

a

Depression and Anxiety

7

.
s
e
i
r
u
n

j

i

l
a
c
i
s
y
h
p

h
t
i

w
s
t
n
e
i
t
a
p

4
1
0
1

,

n

i

s
r
a
e
y

2

r
o
f

y
r
o
t
c
e
j
a
r
t

r
e
d
r
o
s
i
d

s
s
e
r
t
s

c
i
t
a
m
u
a
r
t
-
t
s
o
p

f
o

s
r
o
t
c
i
d
e
r
p

e
n

i
l
e
s
a
B

:

2

E
L
B
A
T

c
i
n
o
r
h
C

)
3
1
=
N

(

y
r
e
v
o
c
e
R

)
2
6
=
N

(

i

g
n
n
e
s
r
o
W

)
1
3
=
N

(

)
4
0
1

.

–

1
9
0
(

.

7
9
0

.

)
3
0
1

.

–

7
9
0
(

.

9
9
0

.

)
1
9
1
1

.

2
4
0
(

.

–

5
2
2

.

∗

.

)
5
6
4
–
9
0

.

1
(

5
2
2

.

–

–

)
2
0
1

.

6
9
0
(

.

)
3
2
3

.

1
6
0
(

.

9
9
0

.

1
4
1

.

y
r
e
v
o
c
e
r
/
g
n
n
e
s
r
o
W

i

–

–

)
2
0
1

.

7
9
0
(

.

)
8
6
1

.

1
4
0
(

.

)
8
4
=
N

(

9
9
0

.

3
8
0

.

a
y
n
A

)
4
5
1
=
N

(

)
1
0
1

.

)
0
9
1

.

–

8
9
0
(

.

–

4
8
0
(

.

9
9
0

.

6
2
1

.

)
0
2
1

.

–

8
9
0
(

.

8
0
1

.

†

.

)
8
3
1
–
5
0
1
(

.

0
2
.
1

)
6
1
1

.

–

6
9
0
(

.

5
0
1

.

†

)
5
1
.
1
–
2
0
.
1
(

9
0
.
1

–

)
4
5
4
3

.

8
0
0
(

.

8
6
1

.

)
5
2
8

.

–

6
2
0
(

.

5
4
1

.

∗

‡

)
3
4

.

5
2
–
5
1

.

1
(

2
4
5

.

)
4
0

.

2
–
5
2

.

1
(

0
6

.

1

)
7
2
1

.

–

5
8
0
(

.

4
0
1

.

)
0
1
1

.

–

8
9
0
(

.

4
0
1

.

.
)
0
6
8
=
N

(

)
8
7
1

.

–

)
2
4
2

.

–

7
9
0
(

.

1
3
1

.

1
0
0
(

.

4
1
0

.

)
8
4
1

.

–

6
4
0
(

.

2
8
0

.

)
3
1
1

.

–

4
7
0
(

.

2
9
0

.

)
9
3
6
7

.

4
5
0
(

.

–

3
4
6

.

)
5
5
3

.

–

9
0
0
(

.

7
5
0

.

)
7
7
1
1

.

–

9
7
0
(

.

)
2
2
1

.

–

2
1
0
(

.

9
3
0

.

–

)
6
2
2

.

5
1
0
(

.

)
4
0
1

.

–

8
9
0
(

.

1
0
1

.

†

‡

†

‡

†

)
4
4

.

6
1
–
1
6

.

1
(

5
1
5

.

)
7
0

.

6
–
0
4

.

1
(

1
9

.

2

.

)
4
7
3
1
–
4
3

.

3
(

7
7

.

6

)
8
4

.

1
–
9
1

.

1
(

3
3

.

1

.

)
7
2
1
–
5
0

.

1
(

6
1
1

.

∗

–

–

–

–

–

)
2
0
1

.

7
5
0
(

.

)
0
6
4

.

1
2
0
(

.

)
9
7
1

.

7
3
0
(

.

)
2
2
3

.

8
3
0
(

.

)
9
2
1

.

6
9
0
(

.

8
5
0

.

5
0
3

.

6
7
0

.

7
9
0

.

1
8
0

.

0
1
1

.

1
1
1

.

–

)
4
0
1

.

6
9
0
(

.

0
0
1

.

.

)
6
2
1
–
0
0
1
(

.

2
1
.
1

–

)
9
2
4

.

5
6
0
(

.

7
6
1

.

)
8
4
1

.

–

1
4
0
(

.

8
7
0

.

∗

)
6
8
.
7
–
0
0
.
1
(

6
7
.
2

∗

)
6
4
.
5
–
1
1
.
1
(

6
4
.
2

–

–

)
1
2
1

.

5
8
0
(

.

)
2
4
3

.

6
2
0
(

.

1
0
1

.

4
9
0

.

)
3
0
1

.

)
0
8
2

.

–

2
8
0
(

.

–

5
6
0
(

.

2
9
0

.

5
3
1

.

∗

)
9
1
.
4
–
9
1
.
1
(

3
2
.
2

)
6
0
3

.

–

)
8
1
1

.

–

)
7
1
1

.

–

7
5
0
(

.

2
3
1

.

4
9
0
(

.

5
0
1

.

8
9
0
(

.

7
0
1

.

∗

‡

‡

†

)
9
1
.
2
–
0
0
.
1
(

8
4
.
1

)
9
5
.
3
–
4
4
.
1
(

8
2
.
2

)
8
7
2
.
1
–
2
1
.
1
(

0
2
.
1

)
6
1
.
1
–
4
0
.
1
(

1
0
1
.
1

)
4
0
1

.

–

8
9
0
(

.

1
0
1

.

)
2
0
1

.

–

9
9
0
(

.

0
0
1

.

p
u
o
r
g

t
n
e
i
l
i
s
e
r

e
h
t

h
t
i

w
d
e
r
a
p
m
o
c

)
s
l
a
v
r
e
t
n

i

e
c
n
e
d
ﬁ
n
o
c
(

s
o
i
t
a
r

s
d
d
o

e
r
a

a
t
a
D

.
e
c
n
a
c
ﬁ
n
g
i
s

i

l
a
c
i
t
s
i
t
a
t
s

s
e
t
a
c
i
d
n

i

e
l
y
t
s

d
l
o
B

.

1
0
0

:

0
<
P

s
e
r
o
c
s

e
l
a
c
s
b
u
s

n
o
i
s
s
e
r
p
e
d
-
e
l
a
c
S

n
o
i
s
s
e
r
p
e
D
y
t
e
i
x
n
A

l
a
t
i
p
s
o
H

r
e
h
g
i
H

s
e
r
o
c
s

e
l
a
c
s
b
u
s

y
t
e
i
x
n
a
-
e
l
a
c
S

n
o
i
s
s
e
r
p
e
D
y
t
e
i
x
n
A

l
a
t
i
p
s
o
H

r
e
h
g
i
H

s
r
e
d
r
o
s
i
d

c
i
r
t
a
i
h
c
y
s
p

s
u
o
i
v
e
r
p

d
a
H

s
t
n
e
v
e

c
i
t
a
m
u
a
r
t

s
u
o
i
v
e
r
p

d
a
H

s
r
e
d
r
o
s
i
d

l
a
c
i
s
y
h
p

f
o

r
e
b
m
u
n

r
e
h
g
i
H

e
s
u
b
a

d
o
o
h
d

l
i

h
c

y
n
a

d
a
H

e
p
y
t

y
r
u
n

j

i

d
e
t
a
l
e
r
-
c
ﬁ
f
a
r
T

e
p
y
t
b
u
s

e
v
i
t
a
i
c
o
s
s
i

d

t
n
e
s
e
r
P

n
o
i
t
a
c
u
d
e

r
e
h
g
i
H

e
g
a

r
e
h
g
i
H

x
e
s

e
l
a
m
e
F

s
e
r
o
c
s

n
o
i
s
s
e
r
p
e
d
-
e
r
i
a
n
n
o
i
t
s
e
u
Q

s
t
i
c
ﬁ
e
D
d
e
v
i
e
c
r
e
P

r
e
h
g
i
H

‡

;

1
0

:

0
<
P

†

;

5
0

:

0
<
P

∗

.
s
p
u
o
r
g

y
r
o
t
c
e
j
a
r
t

l
l
a

o
t

s
r
e
f
e
r

y
n
A

a

8

Depression and Anxiety

trajectory groups remained consistent at ﬁve in both studies.
These ﬁndings suggest that the longitudinal courses and prog-
noses of PTSD following severe physical injuries may indeed
differ over time, but the fundamental number of trajectory
groups remained the same, regardless of the varying follow-up
periods. This consistency in the number of trajectory groups
emphasizes the robustness of this classiﬁcation system for
understanding the development of PTSD symptoms in this
population.

However, our results differ from those of the previous
study by Galatzer-Levy et al. [9], which identiﬁed three distinct
trajectories (nonremitting, slow remitting, and rapid remit-
ting) over a 15-month follow-up. Foa and Tolin [34] employed
the PTSD Symptom Scale interviewer version, based on DSM-
IV PTSD criteria, whereas we used the CAPS-5 to evaluate
PTSD symptoms. Furthermore, the proportion of participants
involved in trafﬁc accidents was 85% in their study, compared
to 46% in ours. These methodological and demographic dif-
ferences may contribute to the discrepancies between our ﬁnd-
ings. Additionally, two other studies identiﬁed four trajectories
(resilient, delayed-onset, recovery, and nonremitting) [11, 14].
These studies involved fewer participants (400–500) and shorter
follow-up periods (6–12 months) compared to our study, which
included over 1,000 participants and a 2-year follow-up. Such
shorter follow-up periods may capture initial recovery patterns
but could miss later stabilizations or deteriorations.

In the full cohort, the presence of any signiﬁcant PTSD
trajectory was predicted by higher education, previous trau-
matic events, trafﬁc-related injury type, dissociative subtype
of PTSD, and higher scores on HADS-A and HADS-D mea-
sured at baseline. Many of these characteristics have been
previously found to be signiﬁcantly associated with PTSD
when evaluated at speciﬁc time points following the trau-
matic incidents [35, 36, 37]. On the other hand, the associa-
tion with higher education contrasts with the results of most
previous studies, which typically found no signiﬁcant associ-
ation between education level and PTSD [38] or else have
reported associations with lower education levels and have
explained these by more limited coping mechanisms when
dealing with traumatic events [39]. Our ﬁndings might reﬂect
links between higher education, greater self-awareness, and
higher emotional intelligence [40], facilitating the recognition
and reporting of PTSD symptoms, leading to a higher likeli-
hood of diagnosis. However, higher education may also con-
tribute to PTSD in several other ways. Individuals with higher
education levels might experience alterations in their self-view
when faced with trauma, leading to increased psychological
distress [41]. Additionally, difﬁculties in accessing mental
health services due to stigma or lack of time can exacerbate
symptoms [42]. Financial pressures, coupled with emotional
problems, might also play a signiﬁcant role [43].

Our study also sought to conduct separate analyses for
each trajectory group to identify their respective predictors.
As described in Table 2, these predictors differed by trajec-
tory group. For example, the previously mentioned associa-
tion with higher education was signiﬁcant only with the
worsening trajectory group. This might be explained by indi-
viduals with higher levels of education initially coping well

shortly after physical injury, but over time, becoming increas-
ingly aware of potential emotional disturbances linked to their
injuries. These ﬁndings underscore the complexity of the rela-
tionship between education, psychological factors, and the
development of PTSD, and more research is needed to better
understand these dynamics. Furthermore, another predictor
of the worsening trajectory was higher baseline depressive
symptoms. It has been well documented that comorbid depres-
sive symptoms with severe physical disorders have been asso-
ciated with both poorer long-term psychological and physical
prognoses [44, 45]. This supports the importance of recogniz-
ing and addressing depressive symptoms when providing care
for individuals at acute phases following severe physical inju-
ries, even if they do not exhibit overt PTSD symptoms.

Our study also found a speciﬁc association between pre-
vious traumatic events and the worsening/recovery trajectory
of PTSD. While prior trauma has been identiﬁed as a signiﬁcant
predictor of PTSD in certain studies [35], it did not emerge as a
signiﬁcant predictor in other investigations [46]. One potential
explanation for these varying results lies in the timing of assess-
ments following physical injuries. Previous studies have typi-
cally assessed individuals within a relatively short timeframe
after the traumatic event, ranging from 1 to 12 months. Conse-
quently, these studies may not have captured the longer-term
trajectory characterized by worsening/recovery, as observed in
the present 2-year follow-up study and a previous 6-year follow-
up study [16]. In our study, we found that trafﬁc-related injuries,
as opposed to other types such as falls and slips, also emerged as
an independent predictor of the worsening/recovery trajectory
of PTSD. This suggests that there may be speciﬁc factors
associated with trafﬁc accidents that contribute to this trajec-
tory. One potential explanation could lie in the fact that trafﬁc
accidents often involve complex insurance and legal issues.
Other research has shown that trafﬁc-related injuries cause
treatment delays, chronic pain, and require related treatment
during ﬁnancial or legal proceedings [47, 48]. Dealing with
such matters can be emotionally challenging and may con-
tribute to the development or exacerbation of PTSD symp-
toms. Importantly, this aspect of trauma-related emotional
problems, especially in the context of trafﬁc accidents, has
been relatively underexplored in previous research. Further
studies are therefore warranted to better understand the rela-
tionship between the type of injury, including trafﬁc-related
incidents, and the development of PTSD symptoms.

The recovery trajectory in our study was predicted by six
baseline factors: female sex, previous childhood abuse, trafﬁc-
related accident type, dissociative subtype of PTSD, and higher
scores on HADS-A and HADS-D. These factors have previ-
ously been identiﬁed as signiﬁcantly associated with PTSD in
other studies [35, 36, 37]. In our study, we observed that PTSD
symptoms remained considerably elevated until 6 months
after the injuries in the recovery trajectory group (Figure 2).
Most previous PTSD studies following physical injuries typi-
cally assessed PTSD within a 6-month timeframe [6, 38, 46].
Given this overlap in assessment periods, it is plausible that we
have identiﬁed consistent ﬁndings between our study and pre-
vious research, particularly within the context of the recovery
trajectory group. Among the six factors inﬂuencing the

Depression and Anxiety

9

recovery trajectory, two—female sex and previous childhood
abuse—were uniquely associated with this trajectory. It is
widely recognized that women and individuals who have expe-
rienced childhood abuse are at a heightened risk of developing
PTSD [5, 49]. Interestingly, a previous study that identiﬁed
similar trajectories to ours reported that female sex was asso-
ciated not only with the recovery trajectory but also with wors-
ening and chronic trajectories [16]. This discrepancy could be
attributed to differences in the follow-up period and the num-
ber of baseline predictors considered in the studies. Child-
hood abuse may render individuals more vulnerable to
developing PTSD following traumatic injuries, particularly
during the early phases of physical injuries, as indicated by
our ﬁndings of associations exclusively with the recovery
trajectory.

Despite the relatively small number, we identiﬁed a group
with signiﬁcant and persistent PTSD symptoms spanning a
period of 2 years. This chronic trajectory was predicted by
the baseline presence of the dissociative subtype of PTSD
and higher scores on the HADS-A. The role of peri-trauma
dissociation as a strong predictor for subsequent PTSD has
been well-established in numerous studies, even though these
assessments were typically conducted over relatively short per-
iods (1–6 months after traumatic events) [36, 46, 50]. Our
ﬁndings extend this understanding, suggesting that dissocia-
tive symptoms experienced in the early phase of physical
injury can be a potent predictor of PTSD that persists for at
least 2 years. Similarly, peri-trauma anxiety has been recog-
nized as a predictor of PTSD, not only in the acute phase [37]
but also in the chronic phase (3 years) following physical
injuries [51]. Our ﬁndings supported these previous studies,
emphasizing the enduring impact of peri-trauma anxiety on
the development of PTSD. Considering that both dissociative
subtypes and anxiety were also identiﬁed as predictors of the
recovery trajectory, this underscored the importance of care-
fully managing and treating patients who exhibit these factors.
It is also possible that these two symptoms were commonly
associated with early PTSD.

Before drawing a conclusion, several issues should be
considered. In our analysis, the entropy value observed was
lower compared to some prior studies, suggesting a less distinct
separation between classes (see Table S1). This phenomenon is
particularly noted in contexts where one class predominantly
encompasses a large portion of the study population, as was the
case in our study, where over 80% of participants were classiﬁed
within the “resilient” trajectory. Such a distribution can skew the
size and distinctiveness of the remaining classes, occasionally
resulting in smaller class sizes. Despite the presence of classes
containing fewer than 5% of participants, as shown in Figure S1,
these classes were retained due to their distinct clinical proﬁles
and the theoretical relevance to our study aims. The literature
suggests a minimum class size of 5% for statistical robustness
[52]; however, the unique composition of our sample and the
theoretical implications of these smaller classes justiﬁed their
inclusion. This decision underscores the need for a nuanced
interpretation of these results, recognizing the potential limits
in generalizability and the importance of further validation in
more heterogeneous samples. Additionally, in developing our

model to predict PTSD trajectories, we initially considered a
comprehensive range of variables informed by theoretical rele-
vance and empirical evidence. However, to avoid overﬁtting and
ensure the stability of our model, we deliberately balanced com-
plexity with interpretability and robustness. We opted for a
model that integrates the most signiﬁcant predictors, maintain-
ing manageability and clarity in our ﬁn dings. We recognize the
potential for future research to explore more complex models
with additional variables and interactions, especially within
larger datasets where such approaches can be more effectively
evaluated.

Strengths of the study include the consecutive recruitment
of participants at baseline from all eligible patients who had
recently experienced physical injuries, as well as the frequent
follow-up assessments reducing the risk of bias arising from
heterogeneous examination times. Evaluations and data col-
lection were conducted using a structured research protocol
and well-recognized and standardized scales, including the
CAPS-5 for PTSD. A broad range of potential risk factors
for PTSD were comprehensively investigated at baseline. Par-
ticipants were followed up to 2 years after physical injuries,
which allowed a comprehensive understanding of the PTSD
trajectories. Long-term follow-up rates were reasonable, and
no evidence of selective attrition was found.

Limitations were that participants were recruited exclu-
sively from a single trauma center, which may limit the gen-
eralizability, although this approach maximized consistency
in evaluation and follow-up. The number of participants who
declined to participate was high during the screening proce-
dure, which could introduce selection bias, potentially affect-
ing the representativeness of our sample. Future research
could aim to identify and mitigate barriers to participation
to ensure a more representative sample of trauma survivors.
The study focused on patients who were hospitalized for mod-
erate to severe physical injuries, and ﬁndings cannot neces-
sarily be generalized to individuals with more minor physical
injuries. Subsequent studies should consider including a broader
range of injury severities to cover a wider spectrum of trauma
experiences and outcomes. The distribution of patients across
the trajectory groups was uneven, with relatively few partici-
pants, particularly in the chronic trajectory group, which
might attenuate statistical power and reduce generalizability.
However, a similar pattern was observed in a previous study
with a comparable design [16]. The lack of interrater reliability
data for the CAPS could impact the consistency of the PTSD
assessments. Follow-up evaluations were conducted via tele-
phone interview, although this method has proved to be as
valid as face-to-face interviews [33].

In conclusion, ﬁve distinctive PTSD trajectories were
observed over 2 years following severe physical
injuries,
and these were predicted by different baseline characteristics.
These ﬁndings highlighted the heterogeneity of PTSD symp-
tom development and emphasized the importance of consid-
ering individual characteristics when assessing and addressing
PTSD in patients with severe physical injuries. Furthermore,
these observations may help explain the inconsistencies
observed in previous studies that have examined predictive
factors for PTSD from speciﬁc time-point evaluations and

10

Depression and Anxiety

may provide valuable insights that can inform the devel-
opment of tailored preventive and management strategies
for this complex issue. Speciﬁcally, implementing routine
screening for PTSD symptoms in individuals presenting
with identiﬁed risk factors at healthcare centers can lead
to early identiﬁcation and treatment, potentially altering
the trajectory before it worsens. Developing personalized
treatment plans based on an individual’s speciﬁc risk pro-
ﬁle and trajectory is crucial, ensuring that interventions are
responsive to changes in their condition over time. For those
identiﬁed at risk due to factors like previous traumatic events
or childhood abuse, integrating preventive interventions such
as resilience training or stress inoculation training into rou-
tine care could help mitigate the development of severe PTSD.
Future studies are needed to improve generalizability through
multi-center evaluations and include individuals with trau-
matic events beyond physical injuries.

Data Availability

The data that support the ﬁndings of the study are available
from the corresponding author (Jae-Min Kim) upon reason-
able request.

Consent

All participants meticulously reviewed the consent form and
written informed consent was duly acquired.

Conﬂicts of Interest

Robert Stewart declares research support in the last 3 years
from Janssen, GSK, and Takeda. No potential conﬂicts of
interest relevant to this article were reported.

Authors’ Contributions

Jae-Min Kim, Robert Stewart, and Il-Seon Shin designed the
study. Hee-Ju Kang and Ju-Wan Kim constructed and per-
formed the study methodology. Jae-Min Kim and Sung-Wan
Kim contributed project administration. Hyunseok Jang, Jung-
Chul Kim, Sung-Wan Kim, and Il-Seon Shin contributed to
the validation. Jae-Min Kim, Ju-Wan Kim, Hee-Ju Kang, Ye-
Jin Kim, and Sung-Wan Kim acquired and curated the data.
Jae-Min Kim, Robert Stewart, Ju-Wan Kim, and Ye-Jin Kim
contributed to the formal analysis. Jae-Min Kim contributed to
writing—original draft. Jae-Min Kim, Robert Stewart, Hee-Ju
Kang, Ju-Wan Kim, Hyunseok Jang, and Jung-Chul Kim con-
tributed to reviewing and editing the draft. Jae-Min Kim and
Ju-Wan Kim contributed as the co-ﬁrst authors.

Acknowledgments

The study was funded by a grant from the National Research
Foundation of Korea, grant (NRF-2020R1A2C2003472) and
(NRF-2020M3E5D9080733) to Jae-Min Kim. Robert Stewart
is part-funded by (i) the NIHR Maudsley Biomedical
Research Centre at the South London and Maudsley NHS
Foundation Trust and King’s College London; (ii) the National
Institute for Health Research (NIHR) Applied Research

Collaboration South London (NIHR ARC South London) at
King’s College Hospital NHS Foundation Trust; (iii) UKRI—
Medical Research Council through the DATAMIND HDR UK
Mental Health Data Hub (MRC reference: MR/W014386); (iv)
the UK Prevention Research Partnership (Violence, Health and
Society) (MR-VO49879/1), an initiative funded by UK Research
and Innovation Councils, the Department of Health and Social
Care (England) and the UK devolved administrations, and lead-
ing health research charities.

Supplementary Materials

The supplementary material includes information on Per-
sonality assessments and Latent Class Growth Analysis
(LCGA) for post-traumatic stress disorder (PTSD) trajecto-
ries. (Supplementary Materials)

References

[1] T. Wiseman, K. Foster, and K. Curtis, “Mental health
following traumatic physical injury: an integrative literature
review,” Injury-international Journal of The Care of The
Injured, vol. 44, no. 11, pp. 1383–1390, 2013.

[2] I. Pozzato, Y. Tran, B. Gopinath, I. D. Cameron, and A. Craig,
“The contribution of pre-injury vulnerability to risk of
psychiatric morbidity in adults injured in a road trafﬁc crash:
comparisons with non-injury controls,” Journal of Psychiatric
Research, vol. 140, pp. 77–86, 2021.

[3] E. T. Beierl, I. Böllinghaus, D. M. Clark, E. Glucksman, and
A. Ehlers, “Cognitive paths from trauma to posttraumatic
stress disorder: a prospective study of Ehlers and Clark’s
in survivors of assaults or road trafﬁc collisions,”
model
Psychological Medicine, vol. 50, no. 13, pp. 2172–2181, 2020.
[4] R. A. Bryant, M. L. O’Donnell, M. Creamer, A. C. McFarlane,
and D. Silove, “A multisite analysis of the ﬂuctuating course of
posttraumatic stress disorder,” JAMA Psychiatry, vol. 70,
no. 8, pp. 839–846, 2013.

[5] M. Heron-Delaney, J. Kenardy, E. Charlton, and Y. Matsuoka,
“A systematic review of predictors of posttraumatic stress
disorder (PTSD) for adult road trafﬁc crash survivors,” Injury-
international Journal of The Care of The Injured, vol. 44,
no. 11, pp. 1413–1422, 2013.

[6] C. S. Fullerton, R. J. Ursano, R. S. Epstein et al., “Gender
differences in posttraumatic stress disorder after motor vehicle
accidents,” American Journal of Psychiatry, vol. 158, no. 9,
pp. 1486–1491, 2001.

[7] E. B. Blanchard, E. J. Hickling, B. M. Freidenberg, L. S. Malta,
E. Kuhn, and M. A. Sykes, “Two studies of psychiatric
morbidity among motor vehicle accident survivors 1 year after
the crash,” Behaviour Research and Therapy, vol. 42, no. 5,
pp. 569–583, 2004.

[8] C. R. Brewin, B. Andrews, and J. D. Valentine, “Meta-analysis
of risk factors for posttraumatic stress disorder in trauma-
exposed adults,” Journal of Consulting and Clinical Psychology,
vol. 68, no. 5, pp. 748–766, 2000.

[9] I. R. Galatzer-Levy, K.-I. Karstoft, A. Statnikov,

and
A. Y. Shalev, “Quantitative forecasting of PTSD from early
trauma responses: a machine learning application,” Journal of
Psychiatric Research, vol. 59, pp. 68–76, 2014.

[10] I. R. Galatzer-Levy, S. Ma, A. Statnikov, R. Yehuda, and
A. Y. Shalev, “Utilization of machine learning for prediction of
in the
post-traumatic stress: a re-examination of cortisol

Depression and Anxiety

11

[11] C. W. Tomas,

prediction and pathways to non-remitting PTSD,” Transla-
tional Psychiatry, vol. 7, no. 3, Article ID e1070, 2017.

J. M. Fitzgerald, C. Bergner, C. J. Hillard,
C. L. Larson, and T. A. deRoon-Cassini, “Machine learning
prediction of posttraumatic stress disorder trajectories following
traumatic injury: identiﬁcation and validation in two independent
samples,” Journal of Traumatic Stress, vol. 35, no. 6, pp. 1656–
1671, 2022.

[12] K. Schultebraucks and I. R. Galatzer-Levy, “Machine learning
for prediction of posttraumatic stress and resilience following
trauma: an overview of basic concepts and recent advances,”
Journal of Traumatic Stress, vol. 32, no. 2, pp. 215–225, 2019.
[13] K. Schultebraucks, A. Y. Shalev, V. Michopoulos et al., “A
validated predictive algorithm of post-traumatic stress course
following emergency department admission after a traumatic
stressor,” Nature Medicine, vol. 26, no. 7, pp. 1084–1088,
2020.

[14] K. Schultebraucks, M. Sijbrandij, I. Galatzer-Levy, J. Mouthaan,
M. Olff, and M. van Zuiden, “Forecasting individual risk for
long-term posttraumatic stress disorder in emergency medical
settings using biomedical data: a machine learning multicenter
cohort study,” Neurobiology of Stress, vol. 14, Article ID
100297, 2021.

[15] I. R. Galatzer-Levy, S. H. Huang, and G. A. Bonanno,
“Trajectories of resilience and dysfunction following potential
trauma: a review and statistical evaluation,” Clinical Psychology
Review, vol. 63, pp. 41–55, 2018.

[16] R. A. Bryant, A. Nickerson, M. Creamer et al., “Trajectory of
post-traumatic stress following traumatic injury: 6-year follow-
up,” British Journal of Psychiatry, vol. 206, no. 5, pp. 417–423,
2015.

[17] J.-W. Kim, H.-J. Kang, K.-Y. Bae et al., “Development of a
biomarker-based diagnostic algorithm for posttraumatic syn-
injury: design of the BioPTS study,”
drome after physical
Psychiatry Investigation, vol. 14, no. 4, pp. 513–517, 2017.
[18] S.-G. Kang, J.-W. Kim, H.-J. Kang et al., “Differential predictors
of early- and delayed-onset post-traumatic stress disorder
injury: a two-year longitudinal study,”
following physical
Frontiers in Psychiatry, vol. 15, Article ID 1367661, 2024.
[19] S. P. Baker, B. O’Neil, W. Haddon, and W. B. Long, “The
injury severity score: a method for describing patients with
multiple injuries and evaluating emergency care,” Journal of
Trauma-Injury Infection and Critical Care, vol. 14, no. 3,
pp. 187–196, 1974.

[20] G. Teasdale and B. Jennett, “Assessment of coma and impaired
consciousness. A practical scale,” Lancet, vol. 2, no. 7872,
pp. 81–84, 1974.

[21] J. Jenewein, L. Wittmann, H. Moergeli, J. Creutzig, and
U. Schnyder, “Mutual
inﬂuence of posttraumatic stress
disorder symptoms and chronic pain among injured accident
survivors: a longitudinal study,” Journal of Traumatic Stress,
vol. 22, no. 6, pp. 540–548, 2009.

[22] F. W. Weathers, D. D. Blake, P. P. Schnurr et al., “The
clinician-administered PTSD scale for DSM-5 (CAPS-5),” 2017.
[23] F. W. Weathers, T. M. Keane, and J. Davidson, “Clinician-
administered PTSD scale: a review of the ﬁrst ten years of
research,” Depression and Anxiety, vol. 13, pp. 132–156, 2001.
[24] K. Posner, M. A. Oquendo, M. Gould, B. Stanley, and M. Davies,
“Columbia Classiﬁcation Algorithm of Suicide Assessment
(C-CASA): classiﬁcation of suicidal events in the FDA’s pediatric
suicidal risk analysis of antidepressants,” American Journal of
Psychiatry, vol. 164, no. 7, pp. 1035–1043, 2007.

[25] O. P. John and S. Srivastata, “The Big Five Trait taxonomy:
history, measurement, and theoretical perspertives,” in Handbook
of Personality, L. A. Pervin and O. P. John, Eds., pp. 102–138, The
Guilford Press, New York, 2nd edition, 1999.

[26] R. de Graaf, R. V. Bijl, F. Smit, W. A. M. Vollebergh, and
J. Spijker, “Risk factors for 12-month comorbidity of mood,
anxiety, and substance use disorders: ﬁndings from the
Netherlands Mental Health Survey and Incidence Study,”
American Journal of Psychiatry, vol. 159, no. 4, pp. 620–629,
2002.

[27] K. M. Connor and J. R. Davidson, “Development of a new
resilience scale: the connor-davidson resilience scale (CD-
RISC),” Depression and Anxiety, vol. 18, no. 2, pp. 76–82,
2003.

[28] J. B. Saunders, O. G. Aasland, T. F. Babor, la de, J. R. Fuente,
and M. Grant, “Development of the alcohol use disorders
identiﬁcation test (AUDIT): WHO collaborative project on
early detection of persons with harmful alcohol consumption,”
Addiction, vol. 88, no. 6, pp. 791–804, 1993.

[29] A. S. Zigmond and R. P. Snaith, “The hospital anxiety and
depression scale,” Acta Psychiatrica Scandinavica, vol. 67,
pp. 361–370, 1983.

[30] F. I. Mahoney and D. W. Barthel, “Functional evaluation: the
Barthel Index,” Maryland State Medical Journal, vol. 14, pp. 61–
65, 1965.

[31] M. J. L. Sullivan, K. Edgley, and E. Dehoux, “A survey of
multiple sclerosis, part 1: perceived cognitive problems and
compensatory strategy use,” Canadian Journal of Rehabilita-
tion, vol. 4, pp. 99–105, 1990.

[32] R. Kellner, Somatizarion and Hypochondriasis, Praeger Publish-

ers, New York, 1986.

[33] M. Aziz and S. Kenford, “Comparability of telephone and face-
to-face interviews in assessing patients with posttraumatic
stress disorder,” Journal of Psychiatric Practice, vol. 10, no. 5,
pp. 307–313, 2004.

[34] E. B. Foa and D. F. Tolin, “Comparison of the PTSD symptom
scale-interview version and the clinician-administered PTSD
scale,” Journal of Traumatic Stress, vol. 13, no. 2, pp. 181–191,
2000.

[35] G. E. Ryb, P. C. Dischinger, K. M. Read, and J. A. Kufera, “PTSD
after severe vehicular crashes,” Association for the Advancement of
Automotive Medicine, vol. 53, pp. 177–193, 2009.

[36] J. Murray, A. Ehlers, and R. A. Mayou, “Dissociation and post-
traumatic stress disorder: two prospective studies of road trafﬁc
accident survivors,” British Journal of Psychiatry, vol. 180,
no. 4, pp. 363–368, 2002.

[37] D. Nishi, Y. Matsuoka, N. Yonemoto, H. Noguchi, Y. Kim, and
S. Kanba, “Peritraumatic distress inventory as a predictor of
post-traumatic stress disorder after a severe motor vehicle
accident,” Psychiatry and Clinical Neurosciences, vol. 64, no. 2,
pp. 149–156, 2010.

[38] R. Coronas, G. García-Parés, C. Viladrich, J. M. Santos, and
J. M. Menchón, “Clinical and sociodemographic variables
associated with the onset of posttraumatic stress disorder in
road trafﬁc accidents,” Depression and Anxiety, vol. 25, no. 5,
pp. E16–23, 2008.

[39] A. L. Dougall, R. J. Ursano, D. M. Posluszny, C. S. Fullerton,
and A. Baum, “Predictors of posttraumatic stress among
victims of motor vehicle accidents,” Psychosomatic Medicine,
vol. 63, no. 3, pp. 402–411, 2001.

[40] D. W. Klyce, K. Merced, A. Erickson et al., “Perceived care
partner burden at 1-year post-injury and associations with

12

Depression and Anxiety

emotional awareness, functioning, and empathy after TBI: a
TBI model systems study,” NeuroRehabilitation, vol. 52, no. 1,
pp. 59–69, 2023.

[41] J. L. Herman and E. Schatzow, “Recovery and veriﬁcation of
trauma,” Psychoanalytic

memories of
Psychology, vol. 4, no. 1, pp. 1–14, 1987.

childhood sexual

[42] P. S. Wang, O. Demler, and R. C. Kessler, “Adequacy of
treatment for serious mental illness in the United States,”
American Journal of Public Health, vol. 92, no. 1, pp. 92–98,
2002.

[43] J. Sareen, T. O. Aﬁﬁ, K. A. McMillan, and G. J. G. Asmundson,
“Relationship between household income and mental disorders:
ﬁndings from a population-based longitudinal study,” Archives
of General Psychiatry, vol. 68, no. 4, pp. 419–427, 2011.
[44] J.-M. Kim, R. Stewart, K.-Y. Bae et al., “Effects of depression
co-morbidity and treatment on quality of life in patients with
acute coronary syndrome: the Korean depression in ACS
(K-DEPACS) and the escitalopram for depression in ACS
(EsDEPACS) study,” Psychological Medicine, vol. 45, no. 8,
pp. 1641–1652, 2015.

[45] J.-M. Kim, R. Stewart, H.-J. Kang et al., “Long-term cardiac
outcomes of depression screening, diagnosis and treatment in
patients with acute coronary syndrome: the DEPACS study,”
Psychological Medicine, vol. 51, no. 6, pp. 964–974, 2021.
[46] T. Ehring, A. Ehlers, and E. Glucksman, “Do cognitive models
help in predicting the severity of posttraumatic stress disorder,
phobia, and depression after motor vehicle accidents? A
prospective longitudinal study,” Journal of Consulting and
Clinical Psychology, vol. 76, no. 2, pp. 219–230, 2008.
[47] G. T. Jones, B. I. Nicholl, J. McBeth et al., “Role of road trafﬁc
accidents and other traumatic events in the onset of chronic
widespread pain: results from a population-based prospective
study,” Arthritis Care & Research, vol. 63, no. 5, pp. 696–701,
2011.

[48] M. J. Giummarra, L. Ioannou, J. Ponsford et al., “Chronic pain
following motor vehicle collision: a systematic review of
outcomes associated with seeking or receiving compensation,”
The Clinical Journal of Pain, vol. 32, no. 9, pp. 817–827, 2016.
[49] V. Boumpa, A. Papatoukaki, A. Kourti et al., “Sexual abuse
and post-traumatic stress disorder in childhood, adolescence
and young adulthood: a systematic review and meta-analysis,”
European Child & Adolescent Psychiatry, vol. 33, no. 6,
pp. 1653–1673, 2024.

[50] L. A. Irish, B. Fischer, W. Fallon, E. Spoonster, E. M. Sledjeski,
and D. L. Delahanty, “Gender differences in PTSD symptoms:
an exploration of peritraumatic mechanisms,” Journal of
Anxiety Disorders, vol. 25, no. 2, pp. 209–216, 2011.

[51] R. A. Mayou, A. Ehlers, and B. Bryant, “Posttraumatic stress
disorder after motor vehicle accidents: 3-year follow-up of a
prospective longitudinal study,” Behaviour Research and Therapy,
vol. 40, no. 6, pp. 665–675, 2002.

[52] H. L. N. Nguefack, M. G. Pagé, J. Katz et al., “Trajectory
modelling techniques useful to epidemiological research: a
comparative narrative review of approaches,” Clinical Epidemi-
ology, vol. 12, pp. 1205–1222, 2020.
