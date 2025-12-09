# Shi_2021_Network-based functional connectivity predicts response to exposure therapy in unmedicated adults with obsessive-compulsive disorder.

www.nature.com/npp

ARTICLE
Network-based functional connectivity predicts response
to exposure therapy in unmedicated adults with
obsessive–compulsive disorder

Tracey C. Shi

1,2, David Pagliaccio 1, Marilyn Cyr

1, H. Blair Simpson1,2 and Rachel Marsh 1,2

Obsessive–compulsive disorder (OCD) is associated with alterations in cortico-striato-thalamo-cortical brain networks, but some
resting-state functional magnetic resonance imaging studies report more diffuse alterations in brain connectivity. Few studies have
assessed functional connectivity within or between networks across the whole brain in unmedicated OCD patients or how patterns
of connectivity predict response to exposure and ritual prevention (EX/RP) therapy, a ﬁrst-line treatment for OCD. Herein, multiband
resting-state functional MRI scans were collected from unmedicated, adult patients with OCD (n = 41) and healthy participants (n =
36); OCD patients were then offered twice weekly EX/RP (17 sessions). A whole-brain-network-based statistic approach was used to
identify group differences in resting-state connectivity. We detected altered pre-treatment functional connectivity between task-
positive regions in the temporal gyri (middle and superior) and regions of the cingulo-opercular and default networks in individuals
with OCD. Signal extraction was performed using a reconstruction independent components analysis and isolated two
independent subcomponents (IC1 and IC2) within this altered connectivity. In the OCD group, linear mixed-effects models tested
whether IC1 or IC2 values predicted the slope of change in Yale–Brown Obsessive–Compulsive Scale (Y-BOCS) scores across EX/RP
treatment. Lower (more different from controls) IC2 score signiﬁcantly predicted greater symptom reduction with EX/RP
(Bonferroni-corrected p = 0.002). Collectively, these ﬁndings suggest that an altered balance between task-positive and task-
negative regions centered around temporal gyri may contribute to difﬁculty controlling intrusive thoughts or urges to perform
ritualistic behaviors.

Neuropsychopharmacology (2021) 46:1035–1044; https://doi.org/10.1038/s41386-020-00929-9

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

are

the

and

hallmarks

compulsions

INTRODUCTION
Obsessions
of
obsessive–compulsive disorder (OCD) and are thought to result
from disruption of cortico-striato-thalamo-cortical (CSTC) feedback
loops, speciﬁcally involving the anterior cingulate cortex, orbito-
frontal cortex, and other frontoparietal regions [1–7]. The CSTC
model has been investigated using resting-state functional
magnetic resonance imaging (rsfMRI), which delineates brain
connection-level or network-level functioning independent from a
speciﬁc task. Most rsfMRI studies of OCD have focused on a priori
subcortical (striatal) seed regions of interest (ROIs) and report
alterations in frontal-subcortical connectivity in adults with OCD,
consistent with the CSTC model [8–11]. These studies, however,
differ in their speciﬁc ﬁndings (i.e.,
increased versus decreased
connectivity in OCD) and many included medicated participants.
Few studies have assessed functional connectivity within or
between networks across the whole brain in unmedicated adults
with OCD or examined how patterns of connectivity predict
response to exposure and ritual prevention therapy (EX/RP), a ﬁrst-
line treatment for OCD.

Neuroimaging studies have begun examining disruptions
in OCD [12–16].

extending beyond traditional CSTC loops

rsfMRI connectivity across large-scale
Whole-brain studies of
intrinsic brain networks in unmedicated OCD participants have
revealed broader alterations across task-positive and task-negative
networks [17, 18]. “Task-positive” networks, including the fronto-
parietal (FPN), cingulo-opercular (CO), and ventral attention (VAN)
networks, are typically engaged during goal-directed tasks
requiring cognitive control and attention [19–21]. Of these task-
positive networks, the CO functions to arbitrate how attention is
divided among tasks and is alternatively referred to as a “salience”
is a “task-
network [22]. The default-mode network (DMN)
negative” network, typically engaged during rest, self-referential
processes, and mind wandering [23–29]. Findings from rsfMRI
studies using seeds in or analyses restricted to the DMN, FPN, and
salience/CO also suggest abnormal connectivity in OCD within
and among these networks [30, 31]. Notably, previous whole-brain
reported decreased
studies of adults [17] and children [18]
connectivity between and within these networks in OCD, while
studies that
focused exclusively on these networks [30, 31]
reported increased connectivity across them. Also notable is that
these prior studies included small samples ranging from 17 [17] to
35 [30] participants with OCD. Such ﬁndings suggest that OCD
pathology may involve an impaired functional balance among

1Department of Psychiatry, New York State Psychiatric Institute, 1051 Riverside Drive, Unit 74, New York, NY 10032, USA and 2Department of Psychiatry, Columbia University
Irving Medical Center, 1051 Riverside Drive, Unit 74, New York, NY 10032, USA
Correspondence: Tracey C. Shi (ts2928@cumc.columbia.edu)
These authors contributed equally: H. Blair Simpson, Rachel Marsh

Received: 12 August 2020 Revised: 30 October 2020 Accepted: 20 November 2020
Published online: 14 January 2021

© The Author(s), under exclusive licence to American College of Neuropsychopharmacology 2021

Network-based functional connectivity predicts response to exposure. . .
TC Shi et al.

1036

task-positive and task-negative networks. For example, pediatric
OCD ﬁndings from our lab [18] and meta-analytic ﬁndings from
adults [6] suggest that the “triple network” model of psycho-
pathology might apply to OCD, wherein the salience/CO might
inappropriately “switch” or modulate between task-positive net-
works and the task-negative DMN [6, 18].

Probing whole-brain rsfMRI connectivity in adults may thus
expand our understanding of the neurobiology of OCD beyond
the CSTC model. However, the different methods used across
previous studies complicate drawing conclusions about functional
abnormalities in OCD, in part because ﬁndings from studies that
analyze different brain regions are difﬁcult to reconcile. For
example, a study that does not include a particular ROI in analyses
cannot be compared to studies with ﬁndings in that ROI. While a
priori ROI selection can provide evidence for speciﬁc hypotheses
such as the CSTC model, whole-brain approaches with good
statistical power are necessary to search for more broad neural
dysfunction across the brain.

RsfMRI studies have also begun to examine neural predictors of
OCD treatment
therapy (CBT)
response. Cognitive-behavioral
consisting of EX/RP is an evidence-based treatment for OCD.
Although EX/RP has proven highly effective in randomized
controlled trials, individual patients range in the degree of their
response [32, 33]. Given the substantial investment of time and
cost associated with EX/RP, the ability to predict which patients
are likely to respond best could substantially improve clinical
efﬁciency [34]. Prior rsfMRI ﬁndings suggest that EX/RP response
can be predicted by changes in multiple brain areas, including the
ventromedial prefrontal cortex [35] and DMN regions [36].
However, these studies included medicated patients despite data
indicating that medication may affect neural activity in OCD [37].
Moreover, both studies focused on speciﬁc brain regions or
networks deﬁned a priori based on their established association
with OCD, thereby precluding detection of abnormalities that do
not overlap with regions identiﬁed in previous work. Two
additional studies used whole-brain graph theoretical approaches
to address the latter problem, but both used relatively small
sample sizes [38, 39] (both n = 17) and the former also included
medicated patients. As with the rsfMRI literature regarding neural
changes in OCD, the heterogeneity in methods employed and in
the OCD samples studied limits the ability to draw conclusions
across studies about EX/RP response prediction.

sample of unmedicated patients

To address this gap in the literature, we used a whole-brain
approach in a larger
to
investigate patterns of functional connectivity that differ between
adults with OCD and healthy controls (HC) and also predict EX/RP
response in OCD patients. We used state-of-the-art multiband MRI
acquisition sequences, taking advantage of recent advances in
spatial and temporal resolution, and a whole-brain network-based
statistic (NBS) technique to identify abnormalities in resting-state
functional connectivity (rs-FC) in unmedicated adults with OCD.
We then used these group differences to predict response to EX/
RP in the OCD group. Based on previous ﬁndings
from
unmedicated participants with OCD, we hypothesized that the
functional balance across task-positive and task-negative regions
would be altered in OCD, and that such alterations would predict
EX/RP response.

METHODS AND MATERIALS
Participants
Details of participant
recruitment and data collection are
published elsewhere [40]. Brieﬂy, unmedicated adults with OCD
and age-, sex-, and race/ethnicity-matched HC were recruited from
the New York City area. All patients met Diagnostic and Statistical
Manual of Mental Disorders, Fifth Edition [41] criteria for OCD as
conﬁrmed by trained raters using the Structured Clinical Interview
for Diagnostic and Statistical Manual-IV-TR Axis I Disorders [42].

Healthy participants had no lifetime psychiatric disorders.
Participants were excluded for MRI contraindications, history of
illness or seizures, head trauma with loss of
neurological
consciousness, pervasive developmental disorder, any current
psychiatric diagnosis (other than OCD or phobias [if secondary] for
the OCD group), or an estimated IQ < 80. The study was approved
by the Institutional Review Board of the New York State Psychiatric
Institute (NYSPI). All participants provided written informed
consent.

Treatment
Patients received a standardized protocol of EX/RP [43] that
included 17 sessions (2 introductory and 15 exposure sessions,
each 90-min long) delivered twice weekly by a clinical psychol-
ogist. Exposure sessions consisted of therapist-aided exposures,
ritual prevention, and education about relapse prevention.

Clinical measures
Severity of OCD symptoms was assessed pre-, mid-, and post-
treatment by a trained rater (independent from the treating
clinician) using the Yale–Brown Obsessive Compulsive Scale (Y-
BOCS) [44].

MRI acquisition
High-resolution MRI scans were conducted at NYSPI using
sequences adapted from the Human Connectome Project (HCP)
[45] for a GE Signa 3T MR750 scanner (details in Supplement).
Brieﬂy, each participant completed T1- and T2-weighted structural
images and 2 runs of multiband resting-state functional MRI
(repetition time = 850 ms, multiband factor = 6, 2 mm isotropic
voxels = 7 min and 32 s per run). For the resting-state scans,
participants were instructed to relax with their eyes open and
remain awake.

MRI pre- and post-processing
Functional data were preprocessed using the HCP pipelines v3.4
[46] (details in Supplement and Fig. S1). First-level analyses were
performed in “grayordinate” space (“91k” CIFTI format), which
combines cortical surface and subcortical volume representations.
Post-processing was performed in Matlab R2019a (Mathworks,
2019). Nuisance regression was performed with 24 motion
parameters (bandpass ﬁltered [47]) and four average global
including squared terms, tem-
grayordinate signal parameters,
poral derivatives, and squared temporal derivatives for all motion
and global mean regressors [48]. Motion censoring [49, 50] based
on framewise displacement (FD; >0.25 mm) and DVARS (z-score >
3) was also performed. All participants had at least 495 frames (7
min) of data remaining after censoring.

The brain was divided into 352 cortical and subcortical regions
using a publicly available CIFTI-space segmentation (https://balsa.
wustl.edu/ﬁle/show/JX5V) using HCP Connectome Workbench
[51]. This segmentation included 333 cortical parcels from the
Cortical Area Parcellation atlas deﬁned by homogeneity of rs-FC
[52] and 19 anatomically deﬁned subcortical ROIs from the
Freesurfer Subcortical Atlas: left and right amygdala, hippocam-
pus, accumbens, caudate, pallidum, putamen, thalamus, ventral
diencephalon, cerebellum, and brain stem. Next,
the BOLD
timeseries from each of the 352 regions/parcels (“nodes”) was
extracted and correlated with all other nodes. These correlations
(“edges”) were Fisher r-to-z transformed, resulting in a 352 × 352
connectivity matrix for each participant.

A growing consensus suggests that whole-brain analyses are
sensitive to how the brain is parcellated and the granularity of
these parcels [53, 54]. To test robustness of our NBS analyses
(described below), we conducted a sensitivity analysis aimed to
replicate ﬁndings using a coarser 100-parcel segmentation [55]
(Supplement).
In addition to having a substantially different
number and granularity of ROIs, this parcellation was created

Neuropsychopharmacology (2021) 46:1035 – 1044

using a different reference dataset, modeled using an algorithm
accounting for both homogeneity and local gradient changes, and
trained on both task and resting-state fMRI data.

Statistical analysis
Participant characteristics. Group differences in participant char-
acteristics were tested using t-tests for continuous variables and χ2
tests for categorical variables in Matlab.

Group differences in functional connectivity. Whole-brain correla-
tion matrices were examined for group differences between OCD
patients and controls using the Network Based Statistic (NBS
Connectome v1.2 [56]). NBS uses permutation testing to identify
signiﬁcant components or “clusters” of contiguous region-to-
region connections and to correct
for multiple comparisons
(10,000 permutations), which can control the family-wise error rate
with more power than mass univariate testing in cases where the
brain connectivity features of interest are interconnected [56] (see
Supplement).

Group differences were tested using an F-test to examine both
OCD > HC and OCD < HC differences parsimoniously in one test
(rather than two unidirectional t-tests), controlling for age, sex,
and mean FD to control for residual effects of head motion during
the MRI scan. Extent thresholding and an f-statistic threshold of 14
(p = 0.0004) were used for primary analyses. Findings from NBS
with extent and intensity thresholding across a range of f-statistic
thresholds are reported in the supplement. Signiﬁcant compo-
nents were visualized using the BrainNet Viewer [57].

As NBS deﬁnes components based on their interconnectedness
and we examined an F-test (rather than directional t-tests), a given
component identiﬁed in our analysis may include functionally
distinct subcomponents that may even show different direction of
effects. Therefore, we used reconstruction independent compo-
nents analysis (RICA) [58] to isolate distinct independent (sub)
components (IC) within the NBS results (details in Supplement).
For each participant, a value for each IC was calculated as a
weighted average across all edges, weighted by their RICA
loadings. Two-sample t-tests were used to test the signiﬁcance
of group differences in resultant ICs. Critically, this allowed for
more parsimonious follow-up testing rather than running analyses
for each identiﬁed edge.

NBS is designed to identify components that are signiﬁcant in
the aggregate, but the individual edges cannot be interpreted in
isolation from the component [56]. Following our prior work with
youth with OCD [18], we performed a supplemental group analysis
using an FDR-corrected mass univariate approach. This approach
has less power (than NBS) to detect interconnected signiﬁcant
edges but permits the investigation of individual edges (detailed
in Supplement).

Response to treatment. Analyses examined associations between
the functional connectivity that was identiﬁed as different across
groups (ICs, described above) and response to treatment in
patients with OCD. For each IC, a linear mixed-effect (LME) model
(“lme4” package [59]) was conducted in R v3.6.1 (R Core Team,
2019) with Y-BOCS scores as a repeated-measure dependent
variable; a random effect for participant; and ﬁxed effects for age,
sex, mean head motion (FD), time of assessment (week 0, 4, or 8),
component score for the IC, and the interaction between time and
IC score. The main effect of time indicated the slope of Y-BOCS
change across pre-, mid-, and post-treatment. A main effect of IC
score would indicate an association with pre-treatment (week 0) Y-
BOCS scores. The IC × time interaction was the predictor of
interest, indicating that the slope of change in Y-BOCS scores over
treatment differed as a function of baseline rs-FC. This interaction
effect was Bonferroni-corrected for multiple
comparisons
across ICs.

Neuropsychopharmacology (2021) 46:1035 – 1044

Network-based functional connectivity predicts response to exposure. . .
TC Shi et al.

1037

RESULTS
Participant characteristics
Eighty-eight adult participants (47 with OCD and 41 HCs) provided
consent for and were enrolled in the study. Six participants (n = 3
OCD; n = 3 HC) did not complete the MRI scan and ﬁve (n = 3
OCD; n = 2 HC) were excluded from analysis due to incidental
anatomical ﬁndings, excessive head motion during the structural
scan, or technical issue with the scanner. Two HC participants had
only one run of resting-state data; the remaining participants
completed two runs.

Demographic and clinical characteristics of the 77 participants
(n = 41 OCD; n = 36 HC) included in the ﬁnal analyses are shown
in Table 1. All patients were either psychotropic medication naïve
(34 out of 41 patients) or free from psychotropic medication for an
average of 126 weeks (range 9–676 weeks) prior to the MRI scan.

Treatment outcomes
The majority of patients (76%) completed at least 14 sessions of
EX/RP, with 25 out of 41 patients (61%) completing all 17
(median = 17 sessions, mean = 14.1, SD = 5.1, range = 1–17). Of
the 41 patients included in analyses, 1 did not complete the mid-
treatment evaluation (week 4), 2 did not complete the post-
treatment evaluation (week 8), and 3 did not complete either the
mid-treatment or post-treatment evaluations (all female). The
number of EX/RP sessions completed was not associated with
age, baseline Y-BOCS severity, or head motion, though males
tended to complete more treatment sessions. Y-BOCS scores
(mean
declined substantially over
decrease = 11.5 points, SD = 8.0).

the course of

treatment

Resting-state functional connectivity (rs-FC)
Group differences. NBS revealed one component with signiﬁ-
cantly altered connectivity in patients relative to controls (p =
0.027). This component consisted of 23 edges, primarily between
parcels in the right VAN, the salience/CO and the DMN (Table 2
and Fig. 1). Speciﬁcally, the right middle and superior temporal
gyri formed a hub in this component, with three nodes in these
gyri (all mapped to the VAN) that collectively appeared in 21 of
the 23 edges. These edges primarily showed reduced connectivity

Table 1. Demographic and clinical characteristics.

Healthy
(n = 36)

OCD
(n = 41)

Group difference
test statistic

Age

Sex, male
Race, white

Handedness, right
Education, years

IQ

Y-BOCS score pretreatment
Y-BOCS score posttreatmenta
Resting-state fMRI
Frames cut, %

Mean FD

29.7 (7.5)

29.1 (7.3)

18 (50%)
26 (72%)

32 (89%)

21 (51%)
30 (73%)

33 (80%)

16.6 (1.7)

16.1 (2.0)

111.7 (12.0)
–
–

106.0 (13.1)

24.8 (3.5)
12.9 (7.9)

t = −0.37
χ2 = 0.01
χ2 = 0.01
χ2 = 1.30
t = −1.03
t = −1.96
–
–

4.9% (1.2%)

4.9% (1.3%)

0.03 (0.02)

0.03 (0.02)

t = 0.06
t = 0.31

There were no signiﬁcant group differences in demographic characteristics
or head motion during resting-state acquisition. Parentheses after
numbers contain standard deviation for continuous variables or percen-
tage of total for discrete variables. Percentage of frames cut indicates the
average percentage of frames regressed as motion or timeseries outliers,
and mean framewise displacement (FD) indicates average head motion
only among runs included in analyses.
aValues for n = 36 patients who completed post-treatment follow-up
session.

Network-based functional connectivity predicts response to exposure. . .
TC Shi et al.

1038

s
l
o
r
t
n
o
C

5
0
0

.

5
2
0

.

0
2
0

.

0
2
0

.

5
1
0

.

3
1
0

.

.

6
0
0
−

4
5
0

.

.

6
0
0
−

0
0
0

.

0
0
0

.

1
0
0

.

1
0
0

.

.

1
0
0
−

7
0
0

.

5
0
0

.

1
0
0

.

.

3
0
0
−

.

1
0
0
−

0
0
0

.

2
0
0

.

0
2
0

.

8
1
0

.

.

8
1
0
−

7
0
0

.

.

3
0
0
−

.

6
0
0
−

.

4
0
0
−

.

6
0
0
−

9
1
0

.

9
7
0

.

.

8
2
0
−

.

8
2
0
−

.

4
2
0
−

.

1
2
0
−

.

5
2
0
−

.

6
2
0
−

.

8
1
0
−

.

1
2
0
−

.

0
2
0
−

.

6
2
0
−

.

0
2
0
−

.

2
2
0
−

.

8
1
0
−

.

2
0
0
−

.

2
0
0
−

D
C
O

.

.

9
6
2
−
1
4
1
−
5
0
4
−

.

l

a
r
y
g
-
b
u
s

,

e
b
o

l

l

a
r
o
p
m
e
T

8
1
_
e
n
o
N
_
L

s
e
u
a
v

l

e
g
d
e

n
a
e
M

a
2

l

e
c
r
a
P

a
1

l

e
c
r
a
P

.
s
e
c
n
e
r
e
f
f
i
d

p
u
o
r
g

y
t
i
v
i
t
c
e
n
n
o
c

l

a
n
o
i
t
c
n
u
f

e
t
a
t
s
-
g
n
i
t
s
e
R

.
2

e
l
b
a
T

)
I

N
M

(

r
e
t
n
e
C

n
o
i
t
p
i
r
c
s
e
D

e
m
a
n

l

e
c
r
a
P

)
I

N
M

(

r
e
t
n
e
C

n
o
i
t
p
i
r
c
s
e
D

e
m
a
n

l

e
c
r
a
P

.

2
4
4

.

0
5
−
4
8
−

.

.

1
6
1

.

4
7
1

.

7
3
3

.

1
4
1
−
5
4
5

.

.

4
6
1
−
2
0
5
−

.

.

0
6
7
−
0
1
4
−

.

.

.

8
7
−
7
5
2
−
9
0
6

.

.

2
4
4

.

0
5
−
4
8
−

.

.

1
0
1

3
6

.

1
6

.

.

0
3
2

.

0
8
3
−

.

0
1
3
−

.

0
3
6

.

5
1
−
2
8

.

.

5
9
2

.

8
7
2
−
3
5
5

.

.

0
3
1

7
4

.

.

4
7
3

3
7

.

.

0
4
2

.

7
5
3

4
6

.

2
2

.

.

2
8
4

.

0
3
1

7
4

.

.

4
7
3

.

1
0
1

.

3
6

.

0
8
3
−

.

4
8
2

.

8
4
4

.

2
8
4

.

2
5
4

.

5
3
3

.

5
9
2

.

8
7
7
−
5
6

.

.

0
0
7
−
0
2
1
−

.

.

6
1
1
−
6
0
4
−

.

.

1
1
1
−
5
3
4

.

.

8
7
2
−
3
5
5

.

.

4
3
2
−
0
9
5
−

.

.

6
0
−
9
9

.

.

5
8
3

s
u
r
y
g

l

a
t
i
p
i
c
c
o

r
o
i
r
e
p
u
S

s
u
r
y
g

l

a
r
t
n
e
c
t
s
o
P

s
u
r
y
g

l

a
r
t
n
e
c
t
s
o
P

l

a
u
s
n

I

l

a
u
s
n

I

s
u
r
y
g

l

a
r
o
p
m
e
t

l

e
d
d
M

i

l

e
u
b
o

l

l

a
t
e
i
r
a
p

r
o
i
r
e
f
n

I

s
u
r
y
g

l

a
t
n
o
r
f

l

i

a
d
e
M

a
l
u
s
n

I

l

a
u
s
n

I

s
u
e
n
u
c
e
r
P

s
u
e
n
u
C

a
l
u
s
n

I

l

a
u
s
n

I

l

a
u
s
n

I

l

e
u
b
o

l

l

a
t
e
i
r
a
p

r
o
i
r
e
f
n

I

l

e
u
b
o

l

l

a
t
e
i
r
a
p

r
o
i
r
e
f
n

I

m
u
r
t
s
u
a
C

l

s
u
r
y
g

l

a
r
t
n
e
c
e
r
P

s
u
r
y
g

l

a
r
t
n
e
c
e
r
P

s
u
r
y
g

l

e
t
a
u
g
n
C

i

s
u
r
y
g

l

e
t
a
u
g
n
C

i

0
1
_
c
r
e
p
O
o
u
g
n
C
_
L

i

l

3
3
_
c
r
e
p
O
o
u
g
n
C
_
R

l

i

0
1
_
y
r
o
t
i
d
u
A
_
L

2
2
_
y
r
o
t
i
d
u
A
_
R

7
2
_
t
l
u
a
f
e
D
_
R

7
_
t
l
u
a
f
e
D
_
L

2
_
c
r
e
p
O
o
u
g
n
C
_
L

i

l

2
_
c
r
e
p
O
o
u
g
n
C
_
L

l

i

.

4
5
1

.

1
3
4

.

1
0
1

3
6

.

.

0
8
3
−

.

8
6
3
−

2
4

.

2
4

.

2
4

.

2
4

.

.

0
0
4
−
8
9
5

.

.

0
0
4
−
8
9
5

.

.

0
0
4
−
8
9
5

.

.

0
0
4
−
8
9
5

.

.

.

4
2
−
2
4
3
−
2
7
5

.

.

.

4
2
−
2
4
3
−
2
7
5

.

.

.

4
2
−
2
4
3
−
2
7
5

.

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
t
n
o
r
f

l

a
u
s
n

I

l

e
d
d
M

i

l

e
d
d
M

i

l

e
d
d
M

i

l

e
d
d
M

i

l

e
d
d
M

i

l

e
d
d
M

i

l

e
d
d
M

i

l

e
d
d
M

i

0
1
_
c
r
e
p
O
o
u
g
n
C
_
L

l

i

l

7
1
_
n
t
t
A
a
s
r
o
D
_
L

l

2
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

2
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

2
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

2
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

0
1
_
c
r
e
p
O
o
u
g
n
C
_
L

l

i

.

.

4
2
−
2
4
3
−
2
7
5

.

s
u
r
y
g

l
a
r
o
p
m
e
t

e
l
d
d
M

i

3
1
_
n
t
t
A
l
a
r
t
n
e
V
_
R

3
1
_
c
r
e
p
O
o
u
g
n
C
_
L

l

i

7
2
_
c
r
e
p
O
o
u
g
n
C
_
R

l

i

0
3
_
c
r
e
p
O
o
u
g
n
C
_
R

i

l

.

.

4
2
−
2
4
3
−
2
7
5

.

.

.

4
2
−
2
4
3
−
2
7
5

.

.

.

4
2
−
2
4
3
−
2
7
5

.

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

l

e
d
d
M

i

l

e
d
d
M

i

l

e
d
d
M

i

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

3
3
_
c
r
e
p
O
o
u
g
n
C
_
R

i

l

.

.

4
2
−
2
4
3
−
2
7
5

.

s
u
r
y
g

l
a
r
o
p
m
e
t

e
l
d
d
M

i

3
1
_
n
t
t
A
l
a
r
t
n
e
V
_
R

7
3
_
c
r
e
p
O
o
u
g
n
C
_
R

i

l

8
3
_
c
r
e
p
O
o
u
g
n
C
_
R

l

i

l

3
_
a
t
e
i
r
a
P
a
d
e
M
_
L

i

l

2
_
h
t
u
o
m
M
S
_
L

6
_
h
t
u
o
m
M
S
_
R

8
3
_
l
a
u
s
i
V
_
R

6
1
_
c
r
e
p
O
o
u
g
n
C
_
L

l

i

0
3
_
c
r
e
p
O
o
u
g
n
C
_
R

l

i

4
3
_
c
r
e
p
O
o
u
g
n
C
_
R

l

i

.

.

4
2
−
2
4
3
−
2
7
5

.

.

.

4
2
−
2
4
3
−
2
7
5

.

.

.

4
2
−
2
4
3
−
2
7
5

.

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

l

e
d
d
M

i

l

e
d
d
M

i

l

e
d
d
M

i

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

.

.

4
2
−
2
4
3
−
2
7
5

.

s
u
r
y
g

l
a
r
o
p
m
e
t

e
l
d
d
M

i

3
1
_
n
t
t
A
l
a
r
t
n
e
V
_
R

.

.

4
2
−
2
4
3
−
2
7
5

.

.

.

4
2
−
2
4
3
−
2
7
5

.

3
2

.

3
2

.

.

3
2

.

7
4
3
−
3
7
4

.

.

7
4
3
−
3
7
4

.

.

7
4
3
−
3
7
4

.

s
u
r
y
g

l

a
r
o
p
m
e
t

s
u
r
y
g

l

a
r
o
p
m
e
t

l

e
d
d
M

i

l

e
d
d
M

i

s
u
r
y
g

l

a
r
o
p
m
e
t

r
o
i
r
e
p
u
S

s
u
r
y
g

l

a
r
o
p
m
e
t

r
o
i
r
e
p
u
S

s
u
r
y
g

l

a
r
o
p
m
e
t

r
o
i
r
e
p
u
S

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

3
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

6
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

6
1
_
n
t
t
A
a
r
t
n
e
V
_
R

l

6
1
_
n
t
t
A
a
r
t
n
e
V
_
R

s
e
d
o
n
e
h
t

y
b
d
e
ﬁ
i
t
n
e
d

i

e
r
a

s
e
g
d
E

.
)
1

.

i

g
F
n

i

n
w
o
h
s
o
s
l
a
(

s
l
o
r
t
n
o
c

y
h
t
l
a
e
h
d
n
a
D
C
O
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
n
e
e
w
t
e
b
e
c
n
e
r
e
f
f
i
d
p
u
o
r
g
t
n
a
c
ﬁ
n
g
i
s

i

a
h
t
i

w

t
n
e
n
o
p
m
o
c

S
B
N
e
h
t
d
e
s
i
r
p
m
o
c

t
a
h
t

s
e
g
d
e

3
2

e
h
t

s
l
i

a
t
e
d
e
b
a
t

l

s
i
h
T

l

e
c
r
a
P

.
l

e
c
r
a
p

h
c
a
e

r
o
f

s
s
a
m

f
o

r
e
t
n
e
c

e
h
t

f
o

i

s
e
t
a
n
d
r
o
o
c

e
h
t

e
r
a

s
e
u
a
v

l

)
I

N
M

(

r
e
t
n
e
C

.
)

V
5
X
J
/
w
o
h
s
/
e
ﬁ
/
u
d
e

l

.

.
l
t
s
u
w
a
s
l
a
b
/
/
:
s
p
t
t
h

(

e
s
a
b
a
t
a
d

A
S
L
A
B

e
h
t

y
b

d
e
s
u

e
s
o
h
t

e
r
a

s
e
m
a
n

l

e
c
r
a
P

.
t
c
e
n
n
o
c

y
e
h
t

)
s
l
e
c
r
a
p

(

.
)
3
S

l

e
b
a
T
(

h
c
a
o
r
p
p
a

e
t
a
i
r
a
v
n
u

i

s
s
a
m
d
e
t
c
e
r
r
o
c
-
R
D
F

e
h
t

g
n
i
s
u

t
n
a
c
ﬁ
n
g
i
s

i

.

n
o
i
t
c
e
n
n
o
c

e
h
t

f
o

y
t
i
l

a
n
o
i
t
c
e
r
i
d

e
t
a
c
i
d
n

i

t
o
n

s
e
o
d

s
i
h
t

;

e
c
n
e
r
e
f
e
r

r
o
f

l

y
p
m

i
s

2

d
n
a

1

s
a

d
e
r
e
b
m
u
n

e
r
a

s
l
e
c
r
a
P

.

d
e
t
c
e
r
i
d
n
u

e
r
a

s
e
g
d
e

l
l

A
a

o
s
l
a

e
r
e
w

t
a
h
t

s
e
g
d
e

s
e
t
a
c
i
d
n

i

l

d
o
B

.
]
6
8

,

5
8
[

)
l

.

m
t
h
n
o
m
e
a
d
/
g
r
o
h
c
a
r
i
a
a
t
/
/
:
p
t
t
h

l

.

(

n
o
m
e
a
D
h
c
a
r
i
a
a
T

l

e
h
t

g
n
i
s
u

d
e
n
g
i
s
s
a

e
r
a

s
n
o
i
t
p
i
r
c
s
e
d

Neuropsychopharmacology (2021) 46:1035 – 1044

Network-based functional connectivity predicts response to exposure. . .
TC Shi et al.

1039

Fig. 1 Resting-state functional connectivity group differences. Visualization of the 23 edges comprising the NBS component that differed
signiﬁcantly across patients with OCD and healthy controls (details in Table 2). Nodes (endpoints of edges) are plotted by center of mass.
Edges (21) with greater average connectivity in healthy controls (HC) compared to the OCD group are represented in blue. Edges (2) with
greater average connectivity in the OCD group are represented in red.

in OCD relative to HC participants with negative connectivity in
OCD and near zero connectivity in HC. The remaining two edges
connecting the middle temporal gyrus (MTG, mapped to VAN) to
DMN nodes showed greater connectivity in the OCD group
(Table 2). NBS with the contrasting Schaefer parcellation similarly
revealed one signiﬁcant component with a hub in the right
lobe (p = 0.017, Supplement). The mass univariate
temporal
analysis revealed seven edges that differed signiﬁcantly across
groups after FDR-correction (see Supplemental text and Table S3);
these edges overlapped with the signiﬁcant NBS
three of
component (bolded in Table 2).

To address heterogeneity in the identiﬁed NBS component,
characterize these group differences parsimoniously, and avoid
conducting 23 separate post hoc analyses, we used a standard
signal extraction method (RICA, see “Methods and materials”) to
reduce the 23 edges into two independent subcomponents
(Table 3 and Fig. 2). Both independent subcomponent 1 (IC1) and
independent subcomponent 2 (IC2) were signiﬁcantly lower in the
OCD relative to HC group (IC1: t = −6.9, p < 10−8; IC2: t = −5.8,
p < 10−6).

(more different

Predicting treatment response. Among participants with OCD,
LME analyses revealed that only IC2 signiﬁcantly predicted Y-BOCS
the course of EX/RP. Speciﬁcally, a model
trajectory over
predicting Y-BOCS as a repeated-measure dependent variable
revealed a signiﬁcant IC × time interaction for IC2 (p = 0.002 after
Bonferroni correction; Table 4), but not IC1 (corrected p = 0.84),
such that participants with lower
from HC)
IC2 showed greater improvement in symptoms. None of the
three edges that were identiﬁed by both NBS and the mass
univariate analysis predicted treatment response individually (see
Supplement). In the subsets of subjects who completed at least 14
or all 17 of the EX/RP treatment sessions, LME analyses replicated
IC2 (p = 0.001 after Bonferroni
the full sample results that
correction for 14-session subset; p = 0.002 for 17-session subset),
but not IC1 (corrected p = 0.54 for 14 sessions; p = 0.10 for
17 sessions), signiﬁcantly predicted Y-BOCS trajectory over the
course of EX/RP. These results were similar with and without
inclusion of the number of CBT sessions as a covariate.

Neuropsychopharmacology (2021) 46:1035 – 1044

Sensitivity analyses using Schaefer parcellation. NBS with the
contrasting Schaefer parcellation revealed one signiﬁcant compo-
nent with a hub in the right temporal lobe (p = 0.017, Supple-
ment). Since all of these edges had decreased rs-FC on average in
OCD relative to HC, we performed RICA with 1 subcomponent.
This subcomponent did not signiﬁcantly predict Y-BOCS change
over
(FDR-
corrected F tests) using the Schaefer parcellation revealed two
edges that signiﬁcantly differed across groups, neither of which
overlapped with the signiﬁcant NBS component (Supplement).

the mass univariate analysis

treatment. Finally,

DISCUSSION
Using a data-driven, whole-brain approach, we detected altered
functional connections between middle and superior temporal
gyri nodes within the VAN and regions within the salience/CO and
DMN in unmedicated patients with OCD. Moreover,
these
alterations positively predicted response to EX/RP. These data
suggest
in unmedicated individuals with OCD, altered
communication between task-positive and task-negative regions
may contribute to the impaired control over intrusive thoughts
and urges to perform rituals instead of more adaptive goal-
directed behaviors.

that

Group differences between OCD and HC
Our ﬁndings of altered connectivity between nodes in task-
positive (i.e., VAN and salience/CO) and task-negative (i.e., DMN)
networks in OCD seem to conform with ﬁndings from previous
resting-state studies of unmedicated adults [17, 30, 31] and youth
[18] with OCD reporting aberrant connectivity between task-
positive and task-negative regions. Of note, only two of the edges
in our signiﬁcant NBS component involved the DMN, and other
edges varied in the patterns of connectivity (i.e., negative or
positive across groups; greater or reduced in OCD). Thus, future
research with larger samples is required to conﬁrm any network-
based interpretation of altered functional connectivity in OCD.
Prior ﬁndings suggest both increased [60, 61] and decreased
[17, 18, 62] connectivity across task-positive and -negative
networks in OCD, possibly due to the use of different analysis

Network-based functional connectivity predicts response to exposure. . .
TC Shi et al.

1040

Table 3.

Edge weights for each independent subcomponent.

Parcel 1a name

Parcel 2a name

Weight in independent
component 1

Weight in independent
component 2

L_CinguloOperc_10

L_DorsalAttn_17

R_VentralAttn_12

R_VentralAttn_12

R_VentralAttn_12

R_VentralAttn_12

R_VentralAttn_13
R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_13
R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_13

R_VentralAttn_16

R_VentralAttn_16

R_VentralAttn_16

L_None_18

L_CinguloOperc_2

L_CinguloOperc_10

R_CinguloOperc_33

L_Auditory_10

R_Auditory_22

L_Default_7
R_Default_27

L_CinguloOperc_2

L_CinguloOperc_10

L_CinguloOperc_13

R_CinguloOperc_27

R_CinguloOperc_30

R_CinguloOperc_33

R_CinguloOperc_37
R_CinguloOperc_38

L_MedialParietal_3

R_Visual_38

L_SMmouth_2

R_SMmouth_6

L_CinguloOperc_16

R_CinguloOperc_30

R_CinguloOperc_34

0.14
−0.06
0.08

0.10

0.05

0.08
−0.19
−0.53
0.26

0.28

0.25

0.22

0.25

0.26

0.22
0.25

0.10

0.20

0.16

0.20

0.14

0.08

0.05

0.12

0.16

0.32

0.30

0.20

0.16
−0.16
0.57
−0.04
0.09

0.12

0.06

0.10

0.10

0.26
0.18
−0.02
−0.05
−0.08
−0.04
0.11

0.32

0.27

Weights (loadings) calculated by reconstruction independent components analysis (also shown in Fig. 2).
aAll edges are undirected. Parcels are numbered as 1 and 2 simply for reference; this does not indicate directionality of the connection.

Fig. 2 Visualization of the largest weights (loadings) generated by reconstruction independent components analysis (RICA) for
independent subcomponents 1 and 2 (see also Table 3). Nodes (endpoints of edges) are plotted by center of mass. Edges are color-coded
according to the subcomponent(s) for which they have a suprathreshold RICA weighting. An edge is deﬁned as “suprathreshold” for a
subcomponent(s) if the absolute value of its RICA weight in the subcomponent is >0.2. A auditory, CO cingulo-opercular, DM default mode, V
visual, VA ventral attention.

Neuropsychopharmacology (2021) 46:1035 – 1044

Fitted coefﬁcients for LME model predicting Y-BOCS as a

Table 4.
repeated dependent measure.

Fixed effects

Coefﬁcient

T value

P value
(uncorrected)

(Intercept)

Timepoint

IC2 strength

Timepoint × IC2 strength
interaction

Age

Male
Mean FD

23.1
−1.7
0.5

1.2

0.04
−2.4
48.6

6.6
−11.9
0.19

3.4

<10−7
<10−15*
0.85
0.0011*

0.38
−1.5
0.97

0.71

0.15
0.34

Mean framewise displacement (FD) is used to control for residual head
motion in the scanner. P values are displayed uncorrected for multiple
comparisons.
*Signiﬁcant at p = 0.05 threshold after Bonferroni correction for two
comparisons (0.05/2 = 0.025).

methods across studies. Our data-driven results are consistent
with prior whole-brain analyses that revealed primarily decreased
connectivity in OCD [17, 18, 62]. Importantly, naming conventions
for and divisions between task-positive networks are inconsistent
across studies: different parcellation schemes combine these
networks (e.g., as a single FPN, usually in older literature [63]) or
label the same regions as part of the ventral attention [64], CO
[22], or salience [65] networks. Such differences in nomenclature
complicate comparison of ﬁndings across this literature. For
example, the “FPN” referenced by one particular study may be the
“CO” of another study, distinguishable only by the speciﬁc ROIs
being studied rather than the network label. For this reason, we
discuss and interpret our ﬁndings from anatomical ROIs rather
than relying solely on network labeling.

Our signiﬁcant NBS component included nodes in the insula,
inferior parietal lobule (IPL), and cingulate, labeled as part of the CO
network in the parcellation scheme used herein [52] but sometimes
included more broadly in an overall FPN [63, 66] or referred to as the
salience network [67]. Previous ﬁndings suggest altered insula
[6, 17, 66, 68, 69], IPL [66], and cingulate [6, 60, 68–70] connectivity in
OCD patients. For example, a meta-analysis of seed-based rsfMRI
studies revealed reduced connectivity in OCD compared to control
participants from insular seeds and general dysconnectivity from the
DMN to anterior cingulate cortex [6]. Differences in the particular
connections identiﬁed across the previous studies and ours are likely
due to methodological differences. For example, all previous rs-FC
studies of adult OCD except for one [71] used singleband acquisition
sequences and processed images in volume space, whereas we
used multiband acquisition and processed in CIFTI
to
represent cortical regions as a surface. Studies also differ in the size
and shape of ROIs (e.g., the 160-ROI Dosenbach atlas [12, 72] or ROIs
derived from prior rsfMRI or task-based fMRI studies [66, 68]) and in
whether resting-state data were acquired with participants’ eyes
open [17, 66] or closed [8, 12, 60, 68–70]. Despite these
methodological variations, the high degree of convergence between
our whole-brain results and earlier seed-based ﬁndings indeed
suggests diffuse alterations in connectivity across the insula, IPL, and
cingulate in OCD. Such dysconnectivity could contribute to the
cognitive control deﬁcits observed in OCD patients [73, 74] and their
difﬁculty controlling or attending away from intrusive thoughts.

format

Our NBS analysis revealed reduced rs-FC in the OCD group
particularly from right MTG to left cingulate, bilateral insula, IPL,
and precentral gyrus. This functional connection is consistent with
human anatomical connections (i.e., white matter tracts identiﬁed
through diffusion-weighted imaging) between the MTG and IPL,
lateral frontal areas, and other MTG subregions [75]. Previous

Neuropsychopharmacology (2021) 46:1035 – 1044

Network-based functional connectivity predicts response to exposure. . .
TC Shi et al.

1041

functional ﬁndings
including medicated and unmedicated
patients suggest abnormal spontaneous resting-state activity
(amplitude of low-frequency ﬂuctuations) in the MTG in OCD
[76]. Other seed-based analyses from unmedicated patients point
to increased rs-FC between the MTG and raphe nucleus that
associated with baseline symptoms and predicted poorer
response to SSRIs [77]. We did not examine the raphe nucleus
speciﬁcally since the subcortical parcellation used herein included
one region for the entire brain stem. However, we detected
reduced connectivity of MTG with several task-positive regions
(cingulate,
IPL) and increased connectivity between the
MTG’s task-positive and task-negative subregions. Since multiple
atlases parcellate MTG subregions into both task-positive and
task-negative networks [52, 55, 78], our ﬁndings suggest that the
imbalance between these networks may be centered around MTG
abnormalities that should be explored further in future research
with larger samples of unmedicated patients.

insula,

We did not detect rs-FC abnormalities in CSTC circuitry, and
speciﬁcally had no subcortical ﬁndings. This could be due, in part,
to methodology. First, while multiband sequences offer excellent
cortical spatio-temporal resolution, they have lower signal-to-
noise ratios for subcortical (compared to cortical) structures [79].
Second, we included only unmedicated patients, whereas most rs-
FC ﬁndings of CSTC alterations come from studies that included
medicated patients, many receiving serotonin reuptake inhibitors
(SRIs). Although the direct effects of SRIs on BOLD signal
in
individuals with OCD are incompletely understood, SRIs inﬂuence
BOLD signal in healthy volunteers [80, 81], and patients with OCD
exhibit differing rs-FC patterns based on medication status [37].
Furthermore, a large multi-site study of OCD showed that
psychotropic medication use exerted signiﬁcant effects on all
measures of brain structure evaluated, and that medication status
often had a greater effect size than clinical diagnosis [82]. Thus,
medication usage confounds reports of altered connectivity from
previous studies of OCD. While some of these studies attempted
to identify effect of medication or SRI-refractory disease on
ﬁndings by including medication status as a covariate or
performed post hoc analyses of unmedicated subsamples, these
subsamples were small (fewer than 30 patients [12, 36, 39, 71]).
Our ﬁndings from a larger sample of unmedicated patients,
in
which rs-FC abnormalities were detected in VAN, salience/CO, and
DMN networks but not CSTC circuitry, underscore the importance
of separating effects due to medication and those due to the
underlying disorder.

Prediction of EX/RP treatment response
Reduced connectivity in the rs-FC component connecting the
MTG to task-positive networks (i.e., VAN, salience/CO) predicted
greater response to EX/RP in OCD patients. This component was
identiﬁed and deﬁned based on group (OCD vs. HC) differences.
That it also predicted treatment response in patients provides
converging evidence that this identiﬁed component may play an
important role in OCD pathophysiology. However, our prediction
ﬁndings should be interpreted with caution since they did not
replicate when we used an alternate parcellation. We suspect that
some of the edges that emerged from our a priori analyses using
the Gordon parcellation were between two nodes that are
and
anatomically
R_Default_27, both subregions of the MTG) and likely grouped
into the same ROI
in the much coarser Schaefer parcellation.
Further, we did not have an independent validation sample of
participants that would have allowed us to test out-of-sample
prediction. Thus, these treatment prediction ﬁndings should be
interpreted with caution.

R_VentralAttn_13

together

close

(e.g.,

Prior work using rsfMRI to predict treatment response has
generated mixed results [35, 36], but it is difﬁcult to compare
these ﬁndings to ours since they did not use whole-brain
approaches. Only one prior study employed a whole-brain

Network-based functional connectivity predicts response to exposure. . .
TC Shi et al.

1042

approach in 17 unmedicated adults with OCD, reporting that
overall connectivity of a subregion of
the right basolateral
amygdala with the rest of the brain predicted response to EX/RP
[38]. The NBS approach used in our study cannot detect ﬁndings
that affect only portions of a region. Furthermore, the method
used in the prior study was designed to detect regions with
diffusely altered connectivity with the rest of the brain, rather than
strongly altered connectivity with speciﬁc regions. In contrast, the
NBS approach we employed is sensitive to multiple, overlapping
edges that signiﬁcantly differ between groups.

Strengths
Our study had several strengths. First, we used multiband
acquisition sequences and state-of-the-art
image processing
pipelines (e.g., the HCP pipeline [46]). Second, to address concerns
of the impact of head motion on rs-FC data, we conducted motion
denoising via nuisance regression with squared terms, temporal
derivatives, and squared temporal derivatives for each of six
realignment parameters (translation and rotation in each of the x, y,
and z planes) based on a recent benchmarking study showing that
this 24-parameter method outperformed alternatives with fewer
motion-related regressors [48]. We additionally performed motion
censoring [49] using relatively strict cutoffs based on FD and DVARS
and included FD as a covariate in analyses to further reduce the
residual effects of head motion on results. Third, we reproduced our
analyses of group differences using two contrasting parcellations,
one ﬁner [52] and one coarser [55], suggesting that our results are
robust and not an artifact of parcellation scheme. Finally, we
enrolled only unmedicated patients with minimal comorbidities,
and 34 out of 41 patients (83%) were drug-naïve, minimizing the
confound of medication use on our brain ﬁndings.

Limitations
Our sample, although comparable to or larger than previous rs-
FC studies of unmedicated adults with OCD, was still relatively
small and 73% non-Hispanic white. In addition, our study design
compared OCD patients undergoing EX/RP therapy with HC
participants, but did not have a positive control arm (e.g., an
OCD group undergoing placebo or an alternative treatment).
Future work should explore neural predictors of
treatment
response in a large,
trial with EX/RP,
medication, and placebo arms to examine speciﬁcity. Finally,
response
our
prediction in an independent validation sample [83], but does
set the stage for future studies to examine whether baseline rs-
FC centered around the MTG/STG predicts EX/RP response in an
independent sample.

study was not powered to test

randomized control

treatment

Future directions
Comparing ﬁndings across neuroimaging studies are difﬁcult due,
in part, to differences in methods. To address this challenge, we
recommend future rs-FC studies in OCD standardize preproces-
sing to help with transparency and replication [84] and use whole-
brain approaches to expand our understanding of OCD beyond
existing models.
In addition, we recommend that researchers
report ROIs and ﬁndings by coordinates rather than just by name
or description, make imaging (e.g., NIFTI or CIFTI format) ﬁles
containing masks of these regions freely available online, and
highlight in manuscripts when a network being studied has
multiple names. Sensitivity analyses can be used to test if ﬁndings
replicate across different atlases, as choice of parcellation can
inﬂuence functional connectivity-based results [53, 54]. Finally,
future studies that assess the comparability of multiband rs-FC
measurements to those from traditional singleband sequences
would be helpful in understanding how newer imaging results
compare to prior ﬁndings.

CONCLUSIONS
Our study is the ﬁrst to combine multiband rs-FC with a whole-
brain network-based approach to assess rs-FC abnormalities in
unmedicated adults with OCD and rs-FC predictors of response to
EX/RP. Functional connectivity in a component dominated by
edges connecting task-positive temporal gyri regions to other
task-positive (salience/CO) and task-negative (DMN) regions was
altered in patients with OCD. Furthermore, those patients with
lower functional connectivity across these regions showed better
response to EX/RP. These ﬁndings suggest that altered connectiv-
ity across task-positive and task-negative temporal gyri regions
may be central to OCD pathophysiology. Since rs-FC is relatively
easy to acquire consistently across sites and scanners, this work
highlights the need for future rs-FC studies of EX/RP response in
unmedicated OCD patients to validate the predictive value of
these ﬁndings in an independent sample.

FUNDING AND DISCLOSURE
This work was supported by grants from the National Institute of
Mental Health (R01MH104648; Principal
Investigators: RM and
HBS) and the National Institutes of Health (MSTP Training Grant to
Columbia University T32GM007367, supporting TCS). In the last 3
years, HBS has received research funds from Biohaven (2018 to
present), royalties from Cambridge University Press and UpToDate,
Inc., and a stipend for serving as associate editor of JAMA
Psychiatry (2019 to present). The remaining authors declare no
competing interests.

ACKNOWLEDGEMENTS
We acknowledge and thank Martine Fontaine and all members of the Center for OCD
research assistants, data
and Related Disorders (e.g.,
managers) who worked on this study as well as all research participants. This study
has been registered as a clinical trial (Control and Reward Circuits in Obsessive
Compulsive Disorder, NCT02221518); additional information is provided at https://
clinicaltrials.gov/ct2/show/NCT02221518.

therapists, clinical

raters,

AUTHOR CONTRIBUTIONS
RM and HBS designed the study; TCS, DP, and RM analyzed the data; and all authors
contributed to writing and/or editing the manuscript.

ADDITIONAL INFORMATION
Supplementary Information accompanies this paper at (https://doi.org/10.1038/
s41386-020-00929-9).

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims
in published maps and institutional afﬁliations.

REFERENCES
1. Maia TV, Cooney RE, Peterson BS. The neural bases of obsessive-compulsive

disorder in children and adults. Dev Psychopathol. 2008;20:1251–83.

2. Ahmari SE, Risbrough VB, Geyer MA, Simpson HB. Impaired sensorimotor gating
in unmedicated adults with obsessive-compulsive disorder. Neuropsycho-
pharmacology. 2012;37:1216–23.

3. Marsh R, Maia TV, Peterson BS. Functional disturbances within frontostriatal cir-
childhood psychopathologies. Am J Psychiatry.

across multiple

cuits
2009;166:664–74.

4. Graybiel AM, Rauch SL. Toward a neurobiology of obsessive-compulsive disorder.

Neuron 2000;28:343–7.

5. Stein DJ, Costa DLC, Lochner C, Miguel EC, Reddy YCJ, Shavitt RG, et al. Obsessive-

compulsive disorder. Nat Rev Dis Prim. 2019;5:52.

6. Gursel DA, Avram M, Sorg C, Brandl F, Koch K. Frontoparietal areas link impair-
ments of large-scale intrinsic brain networks with aberrant fronto-striatal inter-
actions in OCD: a meta-analysis of resting-state functional connectivity. Neurosci
Biobehav Rev. 2018;87:151–60.

Neuropsychopharmacology (2021) 46:1035 – 1044

7. Marsh R, Horga G, Parashar N, Wang Z, Peterson BS, Simpson HB. Altered acti-
vation in fronto-striatal circuits during sequential processing of conﬂict in
unmedicated adults with obsessive-compulsive disorder. Biol Psychiatry.
2014;75:615–22.

8. Harrison BJ, Soriano-Mas C, Pujol J, Ortiz H, Lopez-Sola M, Hernandez-Ribas R,
et al. Altered corticostriatal functional connectivity in obsessive-compulsive dis-
order. Arch Gen Psychiatry. 2009;66:1189–200.

9. Posner J, Marsh R, Maia TV, Peterson BS, Gruber A, Simpson HB. Reduced func-
loop in
tional connectivity within the limbic cortico-striato-thalamo-cortical
unmedicated adults with obsessive-compulsive disorder. Hum Brain Mapp.
2014;35:2852–60.

10. Sakai Y, Narumoto J, Nishida S, Nakamae T, Yamada K, Nishimura T, et al. Corti-
functional connectivity in non-medicated patients with obsessive-

costriatal
compulsive disorder. Eur Psychiatry. 2011;26:463–9.

11. Zhao Q, Xu T, Wang Y, Chen D, Liu Q, Yang Z, et al. Limbic cortico-striato-thalamo-
cortical functional connectivity in drug-naive patients of obsessive-compulsive
disorder. Psychol Med. 2019:1–13.

12. Moody TD, Morﬁni F, Cheng G, Sheen C, Tadayonnejad R, Reggente N, et al.
Mechanisms of cognitive-behavioral therapy for obsessive-compulsive disorder
involve robust and extensive increases in brain network connectivity. Transl
Psychiatry. 2017;7:e1230.

13. Milad MR, Rauch SL. Obsessive-compulsive disorder: beyond segregated cortico-

striatal pathways. Trends Cogn Sci. 2012;16:43–51.

14. Cocchi L, Harrison BJ, Pujol J, Harding IH, Fornito A, Pantelis C, et al. Functional
alterations of large-scale brain networks related to cognitive control in obsessive-
compulsive disorder. Hum Brain Mapp. 2012;33:1089–106.

15. Norman LJ, Carlisi C, Lukito S, Hart H, Mataix-Cols D, Radua J, et al. Structural and
functional brain abnormalities in attention-deﬁcit/hyperactivity disorder and
obsessive-compulsive disorder: a comparative meta-analysis. JAMA Psychiatry.
2016;73:815–25.

16. Norman LJ, Taylor SF, Liu Y, Radua J, Chye Y, De Wit SJ, et al. Error processing and
inhibitory control in obsessive-compulsive disorder: a meta-analysis using sta-
tistical parametric maps. Biol Psychiatry. 2019;85:713–25.

17. Gottlich M, Kramer UM, Kordon A, Hohagen F, Zurowski B. Decreased limbic and
increased fronto-parietal connectivity in unmedicated patients with obsessive-
compulsive disorder. Hum Brain Mapp. 2014;35:5617–32.

18. Cyr M, Pagliaccio D, Yanes-Lukin P, Fontaine M, Rynn MA, Marsh R. Altered network
therapy in pediatric

connectivity predicts response to cognitive-behavioral
obsessive-compulsive disorder. Neuropsychopharmacology. 2020,45:1232–40.
19. Kerns JG, Cohen JD, MacDonald AW 3rd, Cho RY, Stenger VA, Carter CS. Anterior
Science.
and

conﬂict monitoring

adjustments

control.

in

cingulate
2004;303:1023–6.

20. Menon V, Adleman NE, White CD, Glover GH, Reiss AL. Error-related brain acti-
vation during a Go/NoGo response inhibition task. Hum Brain Mapp.
2001;12:131–43.

21. Ridderinkhof KR, Ullsperger M, Crone EA, Nieuwenhuis S. The role of the medial

frontal cortex in cognitive control. Science. 2004;306:443–7.

22. Dosenbach NU, Fair DA, Miezin FM, Cohen AL, Wenger KK, Dosenbach RA, et al.
Distinct brain networks for adaptive and stable task control in humans. Proc Natl
Acad Sci U S A. 2007;104:11073–8.

23. Beckmann CF, DeLuca M, Devlin JT, Smith SM. Investigations into resting-state
connectivity using independent component analysis. Philos Trans R Soc Lond B
Biol Sci. 2005;360:1001–13.

24. Biswal BB, Van Kylen J, Hyde JS. Simultaneous assessment of ﬂow and BOLD
Biomed.

connectivity maps. NMR

resting-state

functional

signals
1997;10:165–70.

in

25. Fox MD, Snyder AZ, Vincent JL, Corbetta M, Van Essen DC, Raichle ME. The human
brain is intrinsically organized into dynamic, anticorrelated functional networks.
Proc Natl Acad Sci USA. 2005;102:9673–8.

26. Greicius MD, Krasnow B, Reiss AL, Menon V. Functional connectivity in the resting
brain: a network analysis of the default mode hypothesis. Proc Natl Acad Sci USA.
2003;100:253–8.

27. Raichle ME, MacLeod AM, Snyder AZ, Powers WJ, Gusnard DA, Shulman GL. A

default mode of brain function. Proc Natl Acad Sci USA. 2001;98:676–82.

28. Harrison BJ, Pujol J, Lopez-Sola M, Hernandez-Ribas R, Deus J, Ortiz H, et al.
Consistency and functional specialization in the default mode brain network.
Proc Natl Acad Sci U S A. 2008;105:9781–6.

29. Mason MF, Norton MI, Van Horn JD, Wegner DM, Grafton ST, Macrae CN. Wan-
dering minds: the default network and stimulus-independent thought. Science
2007;315:393–5.

30. Fan J, Zhong M, Gan J, Liu W, Niu C, Liao H, et al. Altered connectivity within and
between the default mode, central executive, and salience networks in
obsessive-compulsive disorder. J Affect Disord. 2017;223:106–14.
31. Posner J, Song I, Lee S, Rodriguez CI, Moore H, Marsh R, et al.

Increased
functional connectivity between the default mode and salience networks in

Neuropsychopharmacology (2021) 46:1035 – 1044

Network-based functional connectivity predicts response to exposure. . .
TC Shi et al.

1043

unmedicated adults with obsessive-compulsive disorder. Hum Brain Mapp.
2017;38:678–87.

32. Foa EB, Liebowitz MR, Kozak MJ, Davies S, Campeas R, Franklin ME, et al. Ran-
domized, placebo-controlled trial of exposure and ritual prevention, clomipra-
mine, and their combination in the treatment of obsessive-compulsive disorder.
Am J Psychiatry. 2005;162:151–61.

33. Simpson HB, Huppert JD, Petkova E, Foa EB, Liebowitz MR. Response versus
remission in obsessive-compulsive disorder. J Clin Psychiatry. 2006;67:269–76.
34. O’Neill J, Feusner JD. Cognitive-behavioral therapy for obsessive-compulsive
disorder: access to treatment, prediction of long-term outcome with neuroima-
ging. Psychol Res Behav Manag. 2015;8:211–23.

35. Fullana MA, Zhu X, Alonso P, Cardoner N, Real E, Lopez-Sola C, et al. Basolateral
amygdala-ventromedial prefrontal cortex connectivity predicts cognitive beha-
vioural therapy outcome in adults with obsessive-compulsive disorder. J Psy-
chiatry Neurosci. 2017;42:378–85.

36. Reggente N, Moody TD, Morﬁni F, Sheen C, Rissman J, O’Neill J, et al. Multivariate
resting-state functional connectivity predicts response to cognitive behavioral
therapy
in obsessive-compulsive disorder. Proc Natl Acad Sci USA.
2018;115:2222–27.

37. Beucke JC, Sepulcre J, Talukdar T, Linnman C, Zschenderlein K, Endrass T, et al.
Abnormally high degree connectivity of the orbitofrontal cortex in obsessive-
compulsive disorder. JAMA Psychiatry. 2013;70:619–29.

38. Gottlich M, Kramer UM, Kordon A, Hohagen F, Zurowski B. Resting-state con-
nectivity of the amygdala predicts response to cognitive behavioral therapy in
obsessive compulsive disorder. Biol Psychol. 2015;111:100–9.

39. Feusner JD, Moody T, Lai TM, Sheen C, Khalsa S, Brown J, et al. Brain connectivity
therapy in obsessive-
relapse after cognitive-behavioral

and prediction of
compulsive disorder. Front Psychiatry. 2015;6:74.

40. Pagliaccio D, Middleton R, Hezel D, Steinman S, Snorrason I, Gershkovich M, et al.
Task-based fMRI predicts response and remission to exposure therapy in
obsessive-compulsive disorder. Proc Natl Acad Sci USA. 2019;116:20346–53.
41. American Psychiatric Association. Diagnostic and statistical manual of mental

disorders (DSM-5®). American Psychiatric Pub: Philadelphia; 2013.

42. First MB, Spitzer RL, Gibbon M, Williams JB. SCID-I/P. Biometrics Research, New

York State Psychiatric Institute: New York; 2002.

43. Foa EB, Yadin E, Lichner TK. Exposure and response (ritual) prevention for obsessive
compulsive disorder: therapist guide. Oxford University Press: New York; 2012.
44. Goodman WK, Price LH, Rasmussen SA, Mazure C, Fleischmann RL, Hill CL, et al.
The Yale-Brown Obsessive Compulsive Scale. I. Development, use, and reliability.
Arch Gen Psychiatry. 1989;46:1006–11.

45. Van Essen DC, Ugurbil K, Auerbach E, Barch D, Behrens TE, Bucholz R, et al. The
Human Connectome Project: a data acquisition perspective. Neuroimage
2012;62:2222–31.

46. Glasser MF, Sotiropoulos SN, Wilson JA, Coalson TS, Fischl B, Andersson JL, et al.
The minimal preprocessing pipelines for the Human Connectome Project. Neu-
roimage 2013;80:105–24.

47. Fair DA, Miranda-Dominguez O, Snyder AZ, Perrone A, Earl EA, Van AN, et al.
Correction of respiratory artifacts in MRI head motion estimates. Neuroimage
2020;208:116400.

48. Ciric R, Wolf DH, Power JD, Roalf DR, Baum GL, Ruparel K, et al. Benchmarking of
participant-level confound regression strategies for the control of motion artifact
in studies of functional connectivity. Neuroimage 2017;154:174–87.

49. Power JD, Barnes KA, Snyder AZ, Schlaggar BL, Petersen SE. Spurious but sys-
tematic correlations in functional connectivity MRI networks arise from subject
motion. Neuroimage 2012;59:2142–54.

50. Power JD, Schlaggar BL, Petersen SE. Recent progress and outstanding issues in

motion correction in resting state fMRI. Neuroimage 2015;105:536–51.

51. Marcus DS, Harwell J, Olsen T, Hodge M, Glasser MF, Prior F, et al. Informatics and
data mining tools and strategies for the human connectome project. Front
Neuroinform. 2011;5:4.

52. Gordon EM, Laumann TO, Adeyemo B, Huckins JF, Kelley WM, Petersen SE.
Generation and evaluation of a cortical area parcellation from resting-state cor-
relations. Cereb Cortex. 2016;26:288–303.

53. Messe A. Parcellation inﬂuence on the connectivity-based structure-function

relationship in the human brain. Hum Brain Mapp. 2020;41:1167–80.

54. Zalesky A, Fornito A, Harding IH, Cocchi L, Yucel M, Pantelis C, et al. Whole-brain
the choice of nodes matter? Neuroimage

anatomical networks: does
2010;50:970–83.

55. Schaefer A, Kong R, Gordon EM, Laumann TO, Zuo XN, Holmes AJ, et al. Local-
global parcellation of the human cerebral cortex from intrinsic functional con-
nectivity MRI. Cereb Cortex. 2018;28:3095–114.

56. Zalesky A, Fornito A, Bullmore ET. Network-based statistic: identifying differences

in brain networks. Neuroimage 2010;53:1197–207.

57. Xia M, Wang J, He Y. BrainNet Viewer: a network visualization tool for human

brain connectomics. PLoS ONE. 2013;8:e68910.

Network-based functional connectivity predicts response to exposure. . .
TC Shi et al.

1044

58. Le QV, Karpenko A, Ngiam J, Ng AY. ICA with reconstruction cost for efﬁcient
overcomplete feature learning. Proceedings of the 24th International Conference
on Neural Information Processing Systems. 2011:1017–25.

59. Bates D, Maechler M, Bolker B, Walker S, Christensen RHB, Singmann H, et al.

Package ‘lme4’. Convergence. 2015;12:2.

60. Beucke JC, Sepulcre J, Eldaief MC, Sebold M, Kathmann N, Kaufmann C. Default
mode network subsystem alterations in obsessive-compulsive disorder. Br J
Psychiatry. 2014;205:376–82.

61. Chen Y, Meng X, Hu Q, Cui H, Ding Y, Kang L, et al. Altered resting-state functional
organization within the central executive network in obsessive-compulsive dis-
order. Psychiatry Clin Neurosci. 2016;70:448–56.

62. Anticevic A, Hu S, Zhang S, Savic A, Billingslea E, Wasylink S, et al. Global resting-
state functional magnetic resonance imaging analysis identiﬁes frontal cortex,
striatal, and cerebellar dysconnectivity in obsessive-compulsive disorder. Biol
Psychiatry. 2014;75:595–605.

63. Vincent JL, Kahn I, Snyder AZ, Raichle ME, Buckner RL. Evidence for a fronto-
parietal control system revealed by intrinsic functional connectivity. J Neuro-
physiol. 2008;100:3328–42.

64. Yeo BT, Krienen FM, Sepulcre J, Sabuncu MR, Lashkari D, Hollinshead M, et al. The
organization of the human cerebral cortex estimated by intrinsic functional
connectivity. J Neurophysiol. 2011;106:1125–65.

65. Seeley WW, Menon V, Schatzberg AF, Keller J, Glover GH, Kenna H, et al. Dis-
sociable intrinsic connectivity networks for salience processing and executive
control. J Neurosci. 2007;27:2349–56.

66. Stern ER, Fitzgerald KD, Welsh RC, Abelson JL, Taylor SF. Resting-state functional
connectivity between fronto-parietal and default mode networks in obsessive-
compulsive disorder. PLoS ONE. 2012;7:e36356.

67. Power JD, Cohen AL, Nelson SM, Wig GS, Barnes KA, Church JA, et al. Functional

network organization of the human brain. Neuron. 2011;72:665–78.

68. Zhang T, Wang J, Yang Y, Wu Q, Li B, Chen L, et al. Abnormal small-world
architecture of top-down control networks in obsessive-compulsive disorder. J
Psychiatry Neurosci. 2011;36:23–31.

69. Hou JM, Zhao M, Zhang W, Song LH, Wu WJ, Wang J, et al. Resting-state
functional connectivity abnormalities in patients with obsessive-compulsive
disorder and their healthy ﬁrst-degree relatives.
J Psychiatry Neurosci.
2014;39:304–11.

70. Jang JH, Kim JH, Jung WH, Choi JS, Jung MH, Lee JM, et al. Functional connectivity
in fronto-subcortical circuitry during the resting state in obsessive-compulsive
disorder. Neurosci Lett. 2010;474:158–62.

71. Sha Z, Edmiston EK, Versace A, Fournier JC, Graur S, Greenberg T, et al. Functional
disruption of cerebello-thalamo-cortical networks in obsessive-compulsive dis-
order. Biol Psychiatry Cogn Neurosci Neuroimaging. 2020;5:438–47.

72. Dosenbach NU, Nardos B, Cohen AL, Fair DA, Power JD, Church JA, et al. Pre-
diction of individual brain maturity using fMRI. Science 2010;329:1358–61.
73. Shin NY, Lee TY, Kim E, Kwon JS. Cognitive functioning in obsessive-compulsive

disorder: a meta-analysis. Psychol Med. 2014;44:1121–30.

74. Kalanthroff E, Henik A, Simpson HB, Todder D, Anholt GE. To do or not to do? Task
control deﬁcit in obsessive-compulsive disorder. Behav Ther. 2017;48:603–13.
75. Jung J, Cloutman LL, Binney RJ, Lambon, Ralph MA. The structural connectivity of
higher order association cortices reﬂects human functional brain networks.
Cortex 2017;97:221–39.

76. Fan J, Zhong M, Gan J, Liu W, Niu C, Liao H, et al. Spontaneous neural activity in
the right superior temporal gyrus and left middle temporal gyrus is associated
with insight
J Affect Disord.
in obsessive-compulsive disorder.
2017;207:203–11.

level

77. Kim M, Kwak S, Yoon YB, Kwak YB, Kim T, Cho KIK, et al. Functional connectivity of
the raphe nucleus as a predictor of the response to selective serotonin reuptake
inhibitors
disorder. Neuropsychopharmacology
2019;44:2073–81.

obsessive-compulsive

in

78. Glasser MF, Coalson TS, Robinson EC, Hacker CD, Harwell J, Yacoub E, et al. A
multi-modal parcellation of human cerebral cortex. Nature 2016;536:171–78.
79. Barch DM, Burgess GC, Harms MP, Petersen SE, Schlaggar BL, Corbetta M, et al.
Function in the human connectome: task-fMRI and individual differences in
behavior. Neuroimage 2013;80:169–89.

80. McCabe C, Mishor Z, Filippini N, Cowen PJ, Taylor MJ, Harmer CJ. SSRI adminis-
tration reduces resting state functional connectivity in dorso-medial prefrontal
cortex. Mol Psychiatry. 2011;16:592–4.

81. Simmons AN, Arce E, Lovero KL, Stein MB, Paulus MP. Subchronic SSRI admin-
istration reduces insula response during affective anticipation in healthy volun-
teers. Int J Neuropsychopharmacol. 2009;12:1009–20.

82. van den Heuvel OA, Boedhoe PSW, Bertolin S, Bruin WB, Francks C, Ivanov I, et al.
An overview of the ﬁrst 5 years of the ENIGMA obsessive-compulsive disorder
working group: the power of worldwide collaboration. Hum Brain Mapp. 2020.
83. Poldrack RA, Huckins G, Varoquaux G. Establishment of best practices for evi-

dence for prediction: a review. JAMA Psychiatry. 2020;77:534–40.

84. Simmons JP, Nelson LD, Simonsohn U. False-positive psychology: undisclosed
ﬂexibility in data collection and analysis allows presenting anything as signiﬁcant.
Psychol Sci. 2011;22:1359–66.

85. Lancaster JL, Rainey LH, Summerlin JL, Freitas CS, Fox PT, Evans AC, et al. Auto-
mated labeling of the human brain: a preliminary report on the development and
evaluation of a forward-transform method. Hum Brain Mapp. 1997;5:238–42.
86. Lancaster JL, Woldorff MG, Parsons LM, Liotti M, Freitas CS, Rainey L, et al.
Automated Talairach atlas labels for functional brain mapping. Hum Brain Mapp.
2000;10:120–31.

Neuropsychopharmacology (2021) 46:1035 – 1044
