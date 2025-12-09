# Uddin_2017_Progress and roadblocks in the search for brain-based biomarkers of autism and attention-deficit hyperactivity disorder.

OPEN

Citation: Transl Psychiatry (2017) 7, e1218; doi:10.1038/tp.2017.164
www.nature.com/tp

REVIEW
Progress and roadblocks in the search for brain-based
biomarkers of autism and attention-deﬁcit/hyperactivity
disorder
LQ Uddin1,2, DR Dajani1, W Voorhies1, H Bednarz3 and RK Kana3

Children with neurodevelopmental disorders beneﬁt most from early interventions and treatments. The development and
validation of brain-based biomarkers to aid in objective diagnosis can facilitate this important clinical aim. The objective of this
review is to provide an overview of current progress in the use of neuroimaging to identify brain-based biomarkers for autism
spectrum disorder (ASD) and attention-deﬁcit/hyperactivity disorder (ADHD), two prevalent neurodevelopmental disorders. We
summarize empirical work that has laid the foundation for using neuroimaging to objectively quantify brain structure and function
in ways that are beginning to be used in biomarker development, noting limitations of the data currently available. The most
successful machine learning methods that have been developed and applied to date are discussed. Overall, there is increasing
evidence that speciﬁc features (for example, functional connectivity, gray matter volume) of brain regions comprising the salience
and default mode networks can be used to discriminate ASD from typical development. Brain regions contributing to successful
discrimination of ADHD from typical development appear to be more widespread, however there is initial evidence that features
derived from frontal and cerebellar regions are most informative for classiﬁcation. The identiﬁcation of brain-based biomarkers for
ASD and ADHD could potentially assist in objective diagnosis, monitoring of treatment response and prediction of outcomes for
children with these neurodevelopmental disorders. At present, however, the ﬁeld has yet to identify reliable and reproducible
biomarkers for these disorders, and must address issues related to clinical heterogeneity, methodological standardization and
cross-site validation before further progress can be achieved.

Translational Psychiatry (2017) 7, e1218; doi:10.1038/tp.2017.164; published online 22 August 2017

INTRODUCTION
In clinical research, the term ‘biomarker’ or ‘biological marker’
refers to a broad category of medical signs, or objective
indications of medical state, that can be measured accurately
and reproducibly and may inﬂuence and predict the incidence
and outcome of disease.1 Increasingly, clinical neuroscience has
shifted from a focus on identifying neural correlates of psychiatric
conditions to using metrics derived from brain imaging to predict
diagnostic category, disease progression, or response to interven-
tion. Over the past several years, researchers have begun to
integrate sophisticated machine learning approaches into studies
of brain structure and function, with the result that several
candidate ‘brain-based biomarkers’ associated with speciﬁc
disorders have been proposed. The purpose of this review is to
summarize recent progress in identifying brain-based biomarkers
for autism spectrum disorder (ASD) and attention-deﬁcit/hyper-
activity disorder (ADHD), and highlight roadblocks that must be
overcome before further progress can be made. Of note, the term
‘biomarker’ has in some cases been loosely applied in studies that
do not strictly meet the deﬁnition of the term. In the interest of
surveying all potentially relevant contributions to the literature, we
review studies that have used supervised learning approaches to

classify individuals into clinical categories based on neuroimaging
data. As highlighted in other
reviews of brain-based
biomarkers in translational neuroimaging,2,3 we note the sig-
niﬁcant challenges that lie ahead, including the development of
classiﬁers that generalize across studies, sites and heterogeneous
clinical populations.

recent

ASD and ADHD are common disorders affecting youth, and
share a high degree of comorbidity.4 Given their high prevalence
(ASD affects an estimated 1.5% of children,5 and ADHD affects an
estimated 11% of children and adolescents aged 4–17[ref. 6]) and
the cost and consequences of delays in treatment,7 it is imperative
to diagnose and predict outcomes for children with a high degree
of accuracy as early as is feasible.8 Both ASD and ADHD are
currently diagnosed on the basis of parent interview and clinical
observation,9–11 with considerable and sometimes troubling
differences emerging between sites. In the case of ASD, signiﬁcant
site differences have been reported in best-estimate clinical
diagnoses such that even across sites with well-documented
ﬁdelity using standardized diagnostic instruments, clinical distinc-
tions were not reliable.12 The identiﬁcation of objective, reliable
biomarkers is thus a critical yet elusive goal for neuroimaging
researchers investigating these neurodevelopmental disorders.

1Department of Psychology, University of Miami, Coral Gables, FL, USA; 2Neuroscience Program, University of Miami Miller School of Medicine, Miami, FL, USA and 3Department
of Psychology, University of Alabama at Birmingham, Birmingham, AL, USA. Correspondence: Dr LQ Uddin, Department of Psychology, University of Miami, P.O. Box 248185-0751,
Coral Gables, FL 33124, USA.
E-mail: l.uddin@miami.edu
Received 1 June 2017; accepted 7 June 2017

2

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

WHAT SHOULD A BIOMARKER PREDICT?

In order for a biomarker to be developed, it must be demonstrated
that the marker is present before the onset of symptoms, and that
it is speciﬁc to the disorder.13 We proceed with the caveat that
very few of the neuroimaging studies reviewed here would ﬁt this
strict deﬁnition. Few have used prior-onset features to predict
whether a child will later develop ASD or ADHD (but see ref. 14),
and most published classiﬁcation studies only distinguished
patients from controls rather than distinguishing among different
patient groups. Further, in all classiﬁcation studies to date, group
labels (for example, patient vs control) were determined by clinical
diagnosis and reﬂect a binary designation that may not reﬂect the
heterogeneity and dimensionality inherent to complex neurode-
velopmental disorders. Although diagnosis following the Diag-
nostic and Statistical Manual of Mental Disorders (DSM-5)11 has
been the norm in child psychiatry, it is worth noting that there has
been a recent shift towards considering dimensions of behavior,
consistent with the Research Domain Criteria (RDoC) approach.15
Although there has been some push back from the clinical
community
adopting an RDoC
framework,16 there is increasing recognition of the fact that
dimensions of behavior can cut across traditional diagnostic
categories. A few existing studies have focused on dimensions of
symptoms using approaches such as support vector regression
(see ‘Overview of classiﬁers’) that allow one to examine behaviors
in a continuous rather than categorical manner. Here, we aim to
review commonly used classiﬁers in neuroimaging, summarize
current ﬁndings relevant to the development of brain-based
biomarkers for ASD and ADHD, and discuss open challenges.

regarding the utility of

OVERVIEW OF CLASSIFIERS IN NEUROIMAGING

Neuroimaging research in clinical populations has recently begun
testing the potential of the attributes of neuroimaging data sets to
classify participants into a clinical disorder group and a typical
control group. These machine-assisted techniques are often
referred to as classiﬁers. Classiﬁers fall under the broad branch
of machine learning, where computers use algorithms to learn
which patterns account for the differences between two or more
groups. This may involve establishing a rule whereby a given
observation can be classiﬁed or sorted into an existing group.
These rules can be thought of as features that cause the classiﬁer
to distinguish one group from another. By analyzing which features
are driving the decisions of the classiﬁer, the patterns of differences
between groups can be inferred. Thus, pattern classiﬁcation analysis
of neuroimaging data is important in testing the diagnostic utility of
neuroimaging-based markers of psychiatric disorders.

In classifying clinical populations, the classiﬁer searches for
differences in neural patterns between a healthy control group
and a patient group. These patterns can be activation or lack of
activation of a speciﬁc brain area, connectivity of a speciﬁc brain
network, volumetric differences across brain areas, or other
metrics derived from neuroimaging data.
In other words,
classiﬁers use individual features (such as brain activity, brain
morphology or white matter orientation)
to predict group
membership of a given participant. By examining which features
are most important to the classiﬁcation algorithm, researchers can
understand the speciﬁc patterns that account for the largest
variance between clinical populations and controls. A limitation of
is that the classiﬁers are multivariate
this approach, however,
combinations of different features, which can make interpretation
of speciﬁc anatomical contributions difﬁcult. When carefully
constructed, biomarkers have the potential to provide insight
into the neurological mechanisms of the disorder and targets for
future treatment.

Several of the most commonly used classiﬁers in neuroimaging
logistic regression,

support vector machine (SVM),

include:

Translational Psychiatry (2017), 1 – 12

decision tree and random forest
(RF). SVM is a supervised
classiﬁcation method that uses a subset of data for training,
which can then be applied to new data. SVM locates the
hyperplane (a high-dimensional plane) that optimally separates
data into two groups (for example, patients versus controls) based
on features of the data (Figure 1). In the case of neuroimaging
data, each point in feature space corresponds to an individual
Individuals thus become points in a high-dimensional
subject.
space, and a hyperplane can then be used for discrimination
purposes.17 SVMs have been applied successfully in many brain
state and disease state classiﬁcation problems using functional
magnetic resonance imaging (fMRI).18,19 Logistic regression uses
maximum likelihood to estimate the logistic function (an S-shaped
curve); this models the probability that an observation belongs to
a particular category.20 The decision tree method21 is a supervised
learning strategy which builds a classiﬁer from a set of training
samples with a list of features (or attributes) and a class label. RF is
a popular machine learning algorithm22 that is an ensemble
learning method that randomly samples the data with replace-
ment (bootstrapping) to construct many decision trees. Each
decision tree is constructed, or grown, using a random subset of
the input features. The majority vote of the trees makes up the
‘forest’ or the prediction. Although other types of classiﬁers can in
principle be used in neuroimaging research, those reviewed here
have been the most widely used to date.

There are many metrics that measure the performance of
classiﬁers, but the most commonly used metric is accuracy.
Accuracy assesses the percentage of participants that were
correctly classiﬁed as being in the clinical or control group.
In
addition to accuracy, sensitivity and speciﬁcity are commonly
reported measures of classiﬁer performance. Sensitivity measures
the proportion of clinical cases that are correctly identiﬁed, and in
the binary clinical-control classiﬁer,
the
accuracy for the clinical group. Speciﬁcity measures the proportion
of controls that are correctly identiﬁed, and for binary classiﬁers,
indicates accuracy for the control group.

sensitive indicates

Although machine learning algorithms have opened up a new
avenue to neuroimaging research by providing classiﬁcation of
disease states, methodological rigor needs to be ensured for
accurate interpretation and application of ﬁndings. The goal of
machine learning methods is to ﬁt an algorithm to a set of training
data in a way that the algorithm can subsequently be applied to
new data. Fitting an algorithm to training data can be a relatively
simple process, whereas creating a classiﬁer that can generalize
beyond the training data set is quite challenging. One of the
commonly seen effects involves the classiﬁer exhibiting high
accuracy on the training data set but plummeting to chance-level
accuracy when presented with new data. This problem is referred
to as overﬁtting, and it often indicates that the algorithm has been
ﬁt to random noise of the data rather than its truly classifying
features.23 Overﬁtting occurs when the classiﬁer exhibits good
performance on the training data but has poor generalizability to
new data. Under-ﬁtting, on the other hand, occurs when the
classiﬁer exhibits poor performance on both the training data and
the testing data. Under-ﬁtting indicates poor overall ﬁt.

is important

To ensure that a classiﬁer can perform accurately on new data, it
is important to reserve data speciﬁcally for testing. For example, a
classiﬁer could be trained on half of the data and then tested on
the other half. However,
to maximize the
information available for building the classiﬁer, and it can be
detrimental to reserve too much data for testing. To deal with this
dilemma, a procedure referred to as cross-validation, the standard
approach to measure predictive power of a data set, is used. In
cross-validation, the available data are split into a training set,
used to train the model, and a testing set, unseen by the model
during training and used to compute a prediction error.24 One
form of cross-validation, known as the ‘leave-one-out’ method,
involves leaving one example out of the data set, training the

it

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

3

Illustration of support vector machine (SVM). SVM is one machine learning approach that is often used in classiﬁcation studies. If
Figure 1.
there is a population of subjects (x = autism spectrum disorders, o = typically developing) with voxel values (v1 and v2, for example), then
evaluation of one voxel at a time would not differentiate the two groups because there is a substantial amount of overlap between the two
groups on each dimension (as shown by the dashed red and blue lines). A univariate analysis evaluating data one voxel at a time (e.g., either
v1 alone v2) would not be able to detect group differences in such a scenario. However, if v1 and v2 are considered together, a plane separating
the two groups can be constructed, thereby identifying a neighborhood where the two groups differ in spatial patterns of the anatomical or
functional measures of interest.

classiﬁer on the remaining items, and then testing one example.
This is repeated for each example in the set, and the accuracy is
computed from the performance on each of the examples. As this
procedure can be computationally expensive with large data sets,
‘k-fold cross-validation’ can be used instead, which involves
dividing the data into k-parts (for example, 5, 10) that are each
held out for testing.20

In addition, a desirable quality of a machine learning algorithm
is high stability. A classiﬁer is deemed to have higher stability if
modifying the training data does not largely change the resulting
classiﬁcation algorithm. For example, if removing a single example
from the training set results in large perturbations in the resulting
classiﬁcation algorithm,
it reﬂects the relative instability of the
classiﬁer. Stability is an important characteristic of a classiﬁer that
needs to be ensured in studies of classiﬁcation analyses, as
unstable predictions may result in poor reproducibility of ﬁndings.

BRAIN-BASED BIOMARKERS OF ASD
ASD is now thought to affect 1 in 68 children,25 making early
diagnosis an urgent public health concern. The gold standard for
clinical assessment includes administration of the Autism Diag-
nostic Observation Schedule 2 (ADOS-2)26 and the Autism
Diagnostic Interview-Revised (ADI-R),10 which assess behavior by
semi-structured play-based interviews and parent
interviews,
respectively. No objective, biological markers exist for diagnosing
ASD. Although biomarkers can in principle also be derived from

task-based fMRI features, these are less likely to be applied in a
clinical setting where task difﬁculty may preclude some children
from participation. Thus, we limit
the current discussion to
reviewing progress in the development of structural and intrinsic
functional connectivity MRI-based biomarkers (Table 1). Although
structural MRI and resting-state fMRI data are easier to collect from
participants than task fMRI data, it should be noted that one major
limitation of the existing literature is that nearly all studies focus
on those with ASD without intellectual disability (ID) due to the
requirement to stay still for extended periods of time and comply
with verbal instructions in the scanner environment. Most studies
consequently only recruit high-functioning individuals with ASD.

Structural MRI
In one of the ﬁrst detailed analyses of potential brain biomarkers
in adults with ASD, Ecker et al.36 examined ﬁve morphological
parameters including volumetric (cortical thickness and surface
area) and geometric (average convexity or concavity, mean
curvature and metric distortion of cortex) features derived from
structural MRI data. Using SVM and a multiparameter classiﬁcation
approach, they found that all ﬁve parameters together produced
up to 85% accuracy, 90% sensitivity and 80% speciﬁcity for
discriminating individuals with ASD from neurotypical
(NT)
controls. The authors further demonstrated that the classiﬁer built
to discriminate ASD from NT individuals was clinically speciﬁc in
that it somewhat successfully categorized individuals with ADHD

Translational Psychiatry (2017), 1 – 12

4

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

8
6

5
8

:

A
F
L

&
D
T

s
v
A
F
H

:

A
F
H
&
D
T

s
v
A
F
L

3
8

,

5
8

,

R
N

:

D
S
A
s
v
D
T

,

R
N

,

3
7

:

D
S
A

s
v
D
R

R
N

R
N

,

R
N

,

0
9
~

,

V
C
d
o
f
-
9

l

f
o

s
n
o
i
t
a
r
e
t
i

0
1

s
s
e
n
k
c
i
h
t

l

a
c
i
t
r
o
C

i

g
n
m
m
a
r
g
o
r
p

r
a
e
n
L

i

g
n
i
t
s
o
o
b

n
o
i
t
a
d

i
l

a
v

e
m
u
o
v

l

R
L

,

e
e
r
t

n
o
i
s
s
e
r
g
e
r

-
s
s
o
r
c

t
u
o
-
e
n
o
-
e
v
a
e
L

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
t

M
W
d
n
a
M
G

d
n
a

n
o
i
t
a
c
ﬁ
i
s
s
a
C

l

s
i
s
y
R
N

l

0
8

,

0
9

,

0
9

-
s
s
o
r
c

t
u
o
-
o
w

t
-
e
v
a
e
L

s
s
e
n
k
c
i
h
t

l

a
c
i
t
r
o
C

)
l
e
n
r
e
k

r
a
e
n

i
l
(

M
V
S

n
o
i
t
a
d

i
l

a
v

6
8

,

8
8

,

1
8

-
s
s
o
r
c

t
u
o
-
o
w

t
-
e
v
a
e
L

M
W
d
n
a
M
G

)
l
e
n
r
e
k

r
a
e
n

i
l
(

M
V
S

.

3
2
9

,

.

8
5
9

,

R
N

R
N

l

s
e
m
u
o
v
M
W
d
n
a
M
G

a

n
o
i
t
c
n
u
f

t
n
R
N

i

m

i
r
c
s
i
D

t
e
s

i

g
n
n
a
r
t

i

,

n
o
i
t
a
d

i
l

a
v

t
e
s

t
u
o
d
o
h

l

5
7

,

5
9

,

7
8

,

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

l

d
o
f
-
0
1

s
s
e
n
k
c
i
h
t

l

a
c
i
t
r
o
c

l

i

a
n
o
g
e
R

T
M
L

,

T
F

P,
L
M

,

M
V
S

5
7

,

3
8

,

9
7

-
s
s
o
r
c

t
u
o
-
e
n
o
-
e
v
a
e
L

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

r
e
ﬁ
i
s
s
a
l
c

t
u
o
-
e
n
o
-
e
v
a
e
L

t
n
e
d
n
e
p
e
d
n

i

,

n
o
i
t
a
d

i
l

a
v

I

O
R

,

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

R
N

.

2
5
–
7
1

.

)
0
(

5
1
/
)
0
(

2
5

n
a
e
m
D
S
A

n
a
e
m
D
S
A

n
a
e
m
D
T

n
a
e
m
D
T

4
1
7
9

.

4
9
3
1

.

)
0
(

4
2
/
)
0
(

3
3

7
7
,
.
l

a

)

I

Q
P
(

.

2
2
0
0
1

R
N

1
4
1
–
6
7

n
a
e
m
D
T

,

4
0
1

n
a
e
m
D
S
A

n
a
e
m
D
T

,

2
0
1

n
a
e
m
D
S
A

1
1
1

)

Q
V

I

(

0
4
1
–
3
6

.

5
7
0
1

9
2
3
1

.

R
N

8
6
–
0
2

2
4
–
8
1

5
1
–
6

2
4
–
8

)
R
N

(

1
1
/
)
R
N

(

6
1

8
7
,
.
l

a

t
e

h
g
n
S

i

)
0
(

0
2
/
)
0
(

0
2

9
7
,
.
l

a

t
e

r
e
k
c
E

)
0
(

2
2
/
)
0
(

2
2

0
8
,
.
l

a

t
e

r
e
k
c
E

)
3
(

6
1
/
)
3
(

2
2

1
8
o
a
i
J

)
0
(

0
4
/
)
0
(

0
4

n
o
s
r
e
d
n
A

7
2
,
.
l

a

t
e

f
f
o
m
o
o
h
s
k
A

t
e

l

y
e
e
e
N

6
7
,
.
l

a

t
e

t
e
s

t
u
o
d
o
h

l

s
n
o
g
e
r

i

k
r
o
w
t
e
n

)
l
e
n
r
e
k

n
o
i
t
c
n
u
f

D
T

,

.

9
0
0
1

t
e
s

n
o
i
t
a
d

i
l

a
v

R
N

,

R
N

,

0
9

,

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

l

d
o
f
-
0
1

e
d
o
m

t
l
u
a
f
e
d

n

i

M
G

s
i
s
a
b

l

i

a
d
a
r

h
t
i

w

(

M
V
S

n
a
e
m
D
S
A

8
1
–
8

)
2
(

4
2
/
)
2
(

4
2

8
2
,
.
l

a

t
e

i

n
d
d
U

y
c
a
r
u
c
c
a

,

y
t
i
v
i
t
i
s
n
e
s

,

y
c
a
r
u
c
c
a

y
t
i
c
ﬁ
i
c
e
p
s

e
c
n
a
m
r
o
f
r
e
p

p
u
o
r
g
b
u
S

e
c
n
a
m
r
o
f
r
e
p

l

o
r
t
n
o
c
D
S
A

:

e
m
e
h
c
s

n
o
i
t
a
d

i
l

a
V

s
e
r
u
t
a
e
F

d
o
h
t
e
m
n
o
i
t
a
c
ﬁ
i
s
s
a
C

l

)

Q
I
F
(

e
g
n
a
r

Q

I

e
g
n
a
r

e
g
A

s
t
c
e
b
u
s

j

f
o
r
e
b
m
u
N

)
s
r
a
e
y
(

)
F
(

D
T
/
)
F
(
D
S
A

D
S
A

f
o

i

s
e
d
u
t
s

n
o
i
t
a
c
ﬁ
i
s
s
a
l
c

i

d
e
s
a
b
-
g
n
g
a
m
o
r
u
e
N

i

.
1

e
l
b
a
T

y
d
u
t
S

Translational Psychiatry (2017), 1 – 12

R
N

,

R
N

,

.

4
8
8

.
t
e
s

t
u
o
d
o
h

l

,

V
C

l

d
o
f
-
5

m
o
r
f

s
e
r
u
t
a
e
f

l

a
n
o
i
t
c
n
u
F

A
D
L

,
s
r
e
ﬁ
i
s
s
a
l
c

l

e
b
m
e
s
n
E

R
N

R
N

)
R
N

(

2
4
/
)
R
N

(

6
9

r
a
k

0
8
=
C
U
A

,

V
C

t
u
o
-
r
i
a
p
-
e
v
a
e
L

.

p
u
o
r
g

t
u
o
d
o
h

l

s
p
a
m
M
G

e
s
i
w

-
l
e
x
o
V

)
l
e
n
r
e
k

r
a
e
n

i
l
(

M
V
S

.

6
4
0
1

n
a
e
m

4
1
1
–
0
4

8
–
2

)
9
1
(

9
1
/
)
8
3
(

8
3

i

n
o
r
e
d
a
C

l

2
8
,
.
l

a

t
e

i
l

l

a
h
a
g
n

I

3
8
,
.
l

a

t
e

.

8
4
9

,

.

9
6
9

,

.

9
5
9

,

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

l

d
o
f
-
0
1

i

s
t
h
g
e
w
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
s
u
a
C

8
5

,

2
6

,

0
6

g
n
i
s
u

V
C

t
u
o
-
e
n
o
-
e
v
a
e
L

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
t
e
s

t
u
o
d
o
h

l

,

k
s
a
t

d
n
m

i

f
o

y
r
o
e
h
t

g
n
i
r
u
d

l

a
n
o
i
t
c
a
r
f

,
s
e
r
o
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

y
p
o
r
t
o
s
i
n
a

m
o
r
f

s
e
r
u
t
a
e
f

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
r
u
t
c
u
r
t
s

d
n
a
G
E
M

I

T
D

m
e
t
s
y
s

i

g
n
n
n
b

i

I

O
R

,

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

V
C

t
u
o
-
e
n
o
-
e
v
a
e
L

l

a
c
i
t
r
o
c

l

i

a
n
o
g
e
r
-
r
e
t
n

I

l

n
o
i
t
a
e
r
r
o
c
(

2
6
3
0
=

.

r

d
e
t
c
i
d
e
r
p

n
e
e
w
t
e
b

)
S
O
D
A

d
e
v
r
e
s
b
o

d
n
a

0
0
1

,

7
6

,

3
8

n
o
i
t
a
d

i
l

a
v

t
n
e
d
n
e
p
e
d
n

I

.
t
e
s

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

k
r
o
w
t
e
n

,

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

s
t
n
e
n
o
p
m
o
c

l

n
o
i
t
a
e
r
r
o
c

s
s
e
n
k
c
i
h
t

r
e
ﬁ
i
s
s
a
l
c

t
u
o
-
e
n
o
-
e
v
a
e
L

n
a
e
m
D
T

,

5
0
1

n
a
e
m
D
S
A

4
6
–
6

)
1
9
(

7
1
5
/
)
2
5
(

7
4
4

9
2
,
.
l

a

t
e

n
e
s
l
e
N

i

l

i

a
d
a
r

r
o
t
c
e
v

t
r
o
p
p
u
S

n
a
e
m
D
S
A

h
t
i

w
n
o
i
s
s
e
r
g
e
r

n
a
e
m
D
T

,

0
1
1

n
o
i
t
c
n
u
f

s
i
s
a
b

R
L

8
4
1
–
8
7

4
1
1

)

Q
V

I

(

2
1
1

2
4
–
8
1

)
0
(

4
8
/
)
0
(

2
8

5
8
,
.
l

a

t
e

o
t
a
S

2
1
–
7

)
4
(

0
2
/
)
4
(

0
2

0
3
,
.
l

a

t
e

i

n
d
d
U

M
V
S
-
E
C
R

0
4
1
–
0
8

4
3
–
6
1

)
R
N

(

5
1
/
)
R
N

(

5
1

e
d
n
a
h
p
s
e
D

4
8
,
.
l

a

t
e

7
9

,

.

5
5
9

,

7
2
6
9

.

t
e
s

t
u
o
d
o
h

l

,

V
C

l

d
o
f
-
o
w
T

s
v
D
T
2
7
7

.

:

D
S
A
s
v
D
T

.

5
2
8

:
s
g
n

i
l

b
i
s
D
S
A

V
C

l

d
o
f
-
0
1

r
e
t
t
a
m
y
a
r
G

h
c
a
o
r
p
p
a

t
h
g

i
l

h
c
r
a
e
S

6
4
1
–
3
7

6
6
7
1

.

8
1
–
2
1

)
0
2
(

0
4
/
)
7
1
(

2
5

7
8
,
.
l

a

t
e

i

a
v
o
g
e
S

M
V
S

d
n
a

M
V
S

R
N

2
2
–
4

)
3
1
(

8
5

,
)
3
1
(

9
5

1
3
,
.
l

a

t
e

e
e
W

3
3
8
7

.

,

5
7

,

7
6
6
7

.

l

s
e
p
m
a
s

n
o
i
t
a
c
i
l

p
e
r

,

V
C

t
u
o
-
e
n
o
-
e
v
a
e
L

I

O
R

,

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

,

R
L
N
E

,

R
L
2
L

,

R
L
1
L

,

M
V
S

D
T

,

.

6
7
5
1
1

A
D
L

,
)
B
N
G

.

2
0
1
1
1

n
a
e
m

D
T

,

.

3
8
1

n
a
e
m

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

-
f
b
r

,

M
V
S

r
a
e
n

i
l

,

N
N
K

F,
R

n
a
e
m
D
S
A

n
a
e
m
D
S
A

)
0
(

9
5
/
)
0
(

9
5

6
8
,
.
l

a

t
e

t
t
i
l

P

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

5

e
c
n
a
m
r
o
f
r
e
p

p
u
o
r
g
b
u
S

e
c
n
a
m
r
o
f
r
e
p

l

o
r
t
n
o
c
D
S
A

:

e
m
e
h
c
s

n
o
i
t
a
d

i
l

a
V

s
e
r
u
t
a
e
F

d
o
h
t
e
m
n
o
i
t
a
c
ﬁ
i
s
s
a
C

l

)

Q
I
F
(

e
g
n
a
r

Q

I

e
g
n
a
r

e
g
A

s
t
c
e
b
u
s

j

f
o
r
e
b
m
u
N

y
d
u
t
S

)
s
r
a
e
y
(

)
F
(

D
T
/
)
F
(
D
S
A

)

d
e
u
n
i
t
n
o
C

(

.
1

e
l
b
a
T

y
c
a
r
u
c
c
a

,

y
t
i
v
i
t
i
s
n
e
s

,

y
c
a
r
u
c
c
a

y
t
i
c
ﬁ
i
c
e
p
s

0
0
1
~

,

0
0
1
~

,

8
6

s
d
o
f

l

t
n
e
r
e
f
f
i
d

e
g
a
t
n
e
c
r
e
p

r
o

t
u
o
d
o
h

l

,
)
0
9
–
0
1
(

g
n
i
s
u

V
C

)
0
1
–
2
(

s
t
i
l

p
s

.
t
e
s

l

i

a
n
o
g
e
r
-
r
e
t
n

I

d
n
a

l

i

a
n
o
g
e
R

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

d
n
a

l

a
r
u
t
c
u
r
t
s

2
2

l

a
c
i
t
r
o
c
b
u
s

d
n
a

l

a
c
i
t
r
o
c

s
e
r
u
t
a
e
f

s
e
r
u
t
a
e
f

.

3
8
5

,

.

3
1
7

,

5
6

t
e
s

t
u
o
d
o
h

l

,

V
C

l

d
o
f
-
5

t
n
e
d
n
e
p
e
d
n

i

,

g
a
b

t
e
s

n
o
i
t
a
d

i
l

a
v

m
o
r
f

s
e
r
u
t
a
e
f

i

s
t
n
e
d
a
r
g

d
e
t
n
e
i
r
o

f
o
m
a
r
g
o
t
s
i
H

l

a
r
u
t
c
u
r
t
s

d
n
a

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

I

O
R

,

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

3
8

,

9
8

,

1
9

-
f
o
-
t
u
o

i

g
n
p
p
a
r
t
s
t
o
o
B

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

d
e
t
s
e
t

s
r
e
ﬁ
i
s
s
a
l
c

7
6

n
a
e
m
D
S
A

n
a
e
m
D
S
A

3
5
1
/
)
1
4
2
(

.

7
2
1

2
3
,
.
l

a

t
e

u
o
h
Z

.

7
1
1
1

n
a
e
m

.

5
4
1

n
a
e
m

F
R

,

E
F
R

,

O
S
P

,

M
V
S

)

I

Q
P
(

5
5
1
–
7
3

5
3
–
6

)
1
3
(

6
2
1

,
)
8
1
(

6
2
1

3
3
,
.
l

a

t
e

n
e
h
C

D
T

,

.

3
4
0
1

D
T

,

.

5
3
1

.

)
8
4
2
(

n
o
i
t
a
c
ﬁ
i
s
s
a
l
c

i

g
n
n
r
a
e

l

t
n
e
i
t
a
p

)

C
P
H
M

(

n
a
e
m
D
T

,

6
0
1

D
T

,

.

3
7
1

1
1
1

.

1
7
1

n
a
e
m

d
e
s
a
b
-
e
r
u
t
a
e
f
-

G
O
H

I

R
M

f

n
a
e
m
D
S
A

n
a
e
m
D
S
A

)
7
1
(
8

5
4
/
)
1
1
(

0
3
4

9
4
.
l

a
t
e
n
a
i
s
s
a
h
G

i

e
g
a
u
g
n
a

l

r
o
o
p
D
S
A

d
o
o
g
D
S
A

s
v

5
7

,

8
8

,

0
8

:

e
g
a
u
g
n
a

l

R
N

,

R
N

,

4
2
3
8

.

t
e
s

t
u
o
d
o
H

l

M
G

e
v
i
t
i
n
g
o
c
a
t
e
m
d
e
d
n
e
t
x
E

s
e
r
u
s
a
e
m

e
k
a
t
n

i

l

a
c
i
n

i
l
c
d
n
a
n
o
i
t
a
v
i
t
c
a

V
C

l

d
o
f
-
5

l

d
e
t
a
e
r
-
h
c
e
e
p
s

I

R
M

f

A
D
L

s
e
r
a
u
q
s

t
s
a
e

l

l

a
i
t
r
a
P

.

3
2
7

,

1
6

,

.

8
6
6

t
e
s

t
u
o
d
o
h

l

,

V
C

l

d
o
f
-
0
1

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

M
V
S

r
a
e
n
L

i

n
o
i
t
c
n
u
f

s
i
s
a
b

r
e
ﬁ
i
s
s
a
l
c

l

i

a
d
a
r

l

a
r
u
e
n

,

5
7

,
)
7
±
0
8
(

f
o

C
U
A

,

V
C

t
u
o
-
r
i
a
p
-
e
v
a
e
L

e
c
a
f
r
u
s

,
s
s
e
n
k
c
i
h
t

,

e
m
u
o
V

l

7
8

,

2
9

,

0
9

l

d
o
f
-
V

,

V
C

t
u
o
-
e
n
o
-
e
v
a
e
L

0
7

.
t
e
s

t
u
o
d
o
h

l

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

M
G

f
o

s
e
u
a
v

l

l

e
x
o
v

,

a
e
r
a

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

I

O
R

,

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

R
N

,

R
N

,

.

9
1
9

V
C

t
u
o
-
e
n
o
-
e
v
a
e
L

-

H
1

d
n
a

,
I

T
D

,
I

R
M

l

a
r
u
t
c
u
r
t
S

S
R
M

e
e
r
t
-
n
o
i
s
i
c
e
D

n
o
i
t
a
c
ﬁ
i
s
s
a
l
c

M
V
S

N
N
P

I

R
M

m
h
t
i
r
o
g
a

l

.

1
7
1
1

n
a
e
m

R
N

R
N

R
N

D
T

,

.

4
5
1
1

,

.

0
5
8

:
t
r
o
h
o
c

l

i

a
n
g
i
r

O

n
o
i
t
a
d

i
l

a
V

,

.

0
9
8

,

.

0
0
8

I

O
R

,

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

,

V
C

t
u
o
-
e
n
o
-
e
v
a
e
L

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

R
L

e
s
r
a
p
s

,

A
C
C
S
-
1
L

n
a
e
m
D
S
A

,
t
e
s

t
u
o
d
o
h

l

I

O
R

,

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

D
T

,

.

0
0
1
1

R
N

,

R
N

,

.

0
5
7

:
t
r
o
h
o
c

n
o
i
t
a
d

i
l

a
v

t
n
e
d
n
e
p
e
d
n

i

.

3
3
1
1

n
a
e
m

3
2
1
–
2
3

8
4
1
–
1
4

)

I

Q
V
N

(

6
–
2

9
1
–
6

)
1
6
(

8
2
3
/
)
9
3
(

2
1
3

9
8
a
k
a
d

i
I

)
0
(

0
2
/
)
0
(

1
2

8
8
,
.
l

a

t
e

i
r
o
G

n
a
e
m
D
S
A

0
4
–
9
1

)
4
(

8
1
/
)
4
(

9
1

0
9
,
.
l

a

t
e

o
r
e
b
L

i

4
–
1

,
)
R
N

(

4
2
/
)
R
N

(

0
6

9
1

d
e
d
u
l
c
n

i

o
s
l
a

R
N

)
5
9
(

6
4
5
/
)
9
5
(

8
0
5

-
e
g
a
u
g
n
a

l

d
e
y
a
e
d

l

o
d
r
a
b
m
o
L

1
9
,
.
l

a

t
e

u
j
a
r
a
b
b
u
S

2
9
,
.
l

a

t
e

4
6
–
6

4
4
1
(

s
t
c
e
b
u
s

j

1
7
8

0
4
–
8
1

/
)
2
(
4
5

n
o
i
t
a
d

i
l

a
V

,
)
4
3
)
7
0
1
/
)
6
1
(
4
7

)
2
(
2
5

)
F

5
4
,
.
l

a

m
a
h
a
r
b
A

3
9
,
.
l

a

t
e

t
e

a
t
a
h
a
Y

,

B
N
G

;
r
e
t
t
a
m
y
a
r
g

,

M
G

;
s
e
e
r
t

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

,

T
F

;

i

g
n
g
a
m

i

e
c
n
a
n
o
s
e
r

c
i
t
e
n
g
a
m

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

,
I

R
M

f

;
t
n
e
i
t
o
u
q

e
c
n
e
g

i
l
l

e
t
n

i

l

e
a
c
s
-
l
l

u
f

,

Q
F

I

;

l

e
a
m
e
f

,

F

;

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

,

V
C

;
r
e
d
r
o
s
i
d
m
u
r
t
c
e
p
s

m

s
i
t
u
a

,

D
S
A

i

:
s
n
o
i
t
a
v
e
r
b
b
A

.

4
4
1
1

n
a
e
m

-
t
e
n
-
c
i
t
s
a
e

l

,

R
L
N
E

l

s
i
s
y
a
n
a

l

n
o
i
t
a
e
r
r
o
c

l

a
c
i
n
o
n
a
c

e
s
r
a
p
s

d
e
z
i
r
a
u
g
e
r

l

m
r
o
n
-
1
L

,

A
C
C
S
-
1
L

;

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

l

d
e
z
i
r
a
u
g
e
r
-
1
L

,

R
L
1
L

;
r
o
b
h
g
e
n

i

t
s
e
r
a
e
n
-
k

,

N
N
K

;

m

s
i
t
u
a

i

g
n
n
o
i
t
c
n
u
f
-
h
g
h

i

,

A
F
H

;
s
e
y
a
B

i

e
v
a
N

n
a
i
s
s
u
a
G

;
s
n
o
r
t
p
e
c
r
e
p
r
e
y
a

l
i
t
l
u
m
P,
L
M

;

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

,

R
L

;
s
e
e
r
t

l

e
d
o
m
c
i
t
s
i
g
o

l

,

T
M
L

;

m

i

s
i
t
u
a
g
n
n
o
i
t
c
n
u
f

w
o

l

,

A
F
L

l

;
s
i
s
y
a
n
a
t
n
a
n
m

i

i
r
c
s
i
d
r
a
e
n

i
l

,

A
D
L

;

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

l

d
e
z
i
r
a
u
g
e
r
-
2
L

,

R
L
2
L

;

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

d
e
z
i
r
a
u
g
e
r

l

l

e
n
r
e
k

n
a
i
s
s
u
a
G

,

M
V
S
-
f
b
r

;
s
i
s
y
a
n
a

l

t
n
a
n
m

i

i
r
c
s
i
d

c
i
t
a
r
d
a
u
q

,

A
D
Q

;

n
o
i
t
a
z
i
m

i
t
p
o
m
r
a
w
s

e
l
c
i
t
r
a
p

,

O
S
P

;

k
r
o
w
t
e
n

l

a
r
u
e
n

c
i
t
s
i
l
i

b
a
b
o
r
p

,

N
N
P

;

Q

I

e
c
n
a
m
r
o
f
r
e
p

,

Q
P

I

;

Q

I

l

a
b
r
e
v
n
o
n

,

I

Q
V
N

;

d
e
t
r
o
p
e
r

t
o
n

n
o
i
t
a
m
r
o
f
n

i

,

R
N

l

a
c
i
p
y
t

,

D
T

i

;
s
e
n
h
c
a
m

r
o
t
c
e
v

t
r
o
p
p
u
s

,

M
V
S

;
I

R
M

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
r

,
I

R
M

f
-
s
r

;

d
o
h
t
e
m

g
n
i
t
s
o
o
b

i

t
n
e
d
a
r
g

,

n
o
i
t
a
n
m

i

i
l

e

e
r
u
t
a
e
f

e
v
i
s
r
u
c
e
r

,

E
F
R

;
t
s
e
r
o
f

m
o
d
n
a
r

,

F
R

;
r
e
d
r
o
s
i
D

i

g
n
d
a
e
R

,

D
R

i

;
s
e
n
h
c
a
m

r
o
t
c
e
v

t
r
o
p
p
u
s

.
r
e
t
t
a
m
e
t
i
h
w

,

M
W

;

Q

I

l

a
b
r
e
v

,

Q
V

I

;
t
n
e
m
p
o
e
v
e
d

l

6
9
5
7

.

,

3
6
4
7

.

,

.

4
5
7

t
e
s

t
u
o
d
o
h

l

,

V
C

l

d
o
f
-
0
1

l

s
e
m
u
o
v
M
W
d
n
a
M
G

M
V
S

.

8
1
1

n
a
e
m

n
a
e
m
D
S
A

5
1
o

)
7
1
(

7
5
/
)
7
(

4
5

4
9
,
.
l

a

t
e

g
n
a
W

R
N

,

R
N

,

0
6

t
e
s

t
u
o
d
o
h

l

,

V
C

l

d
o
f
-
0
1

m
o
r
f

s
e
r
u
t
a
e
f

c
i
r
t
e
m
o
h
p
r
o
M

M
B
G
F,
R

n
a
e
m
D
S
A

l

s
i
s
y
a
n
a

n
o
i
t
a
z
i
m
o
d
n
a
r

,

V
C

s
s
e
n
k
c
i
h
t

l

a
c
i
t
r
o
c

d
n
a

a
e
r
a

-

D
T

,

6
0
1

d
e
h
c
t
a
m

4
6
–
6

)
0
(

3
7
3
/
)
0
(

1
6
3

5
3
,
.
l

a

t
e

l

a
w
u
t
a
K

I

R
M

l

a
r
u
t
c
u
r
t
s

D
T

,

.

2
5
0
1

D
T

,

.

9
7
0
1

Translational Psychiatry (2017), 1 – 12

R
N

,

R
N

,

0
6
o

t
u
o
-
o
w

t
-
e
v
a
e

l

t
e
s

,

V
C

l

d
o
f
-
0
1

e
c
a
f
r
u
s

,

e
m
u
o
v

l

l

i

a
n
o
g
e
R

A
D
Q

,

A
D
L

n
a
e
m
D
S
A

5
6
–
6

)
0
(

3
7
5
/
)
0
(

9
3
5

4
3
,
.
l

a

t
e

r
a
a
H

6

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

as non-autistic. These results represent an important ﬁrst step
towards identifying structural biomarkers in ASD but are limited in
their clinical utility in that only adults (aged 20–68) were
examined. As ASD is a disorder with early life onset and variable
developmental
individuals are
trajectory, studies of younger
critical for disentangling disorder-speciﬁc neural signatures.

In a study of children and adolescents with autism, gray matter
volume was used as a structural feature for classiﬁcation. Using
SVM searchlight classiﬁcation, this study found that gray matter
within default mode network regions (posterior cingulate cortex
and medial temporal lobes: 92%, medial prefrontal cortex: 88%)
could be used to discriminate between clinical and control groups
with high accuracy.28 The earlier study of adults with ASD also
reported morphometric abnormalities in the posterior cingulate
that contributed to classiﬁcation, suggesting that this cortical
midline region may be a locus of dysfunction throughout the
lifespan.

(morphological

A more recent study of children used a unique approach, multi-
kernal SVM, combining regional (cortical thickness, gray matter
volume) and interregional
change patterns
between pairs of ROIs) features to achieve 96% classiﬁcation
accuracy.31 In this study, the neuroanatomical features contribut-
ing the most to classiﬁcation were subcortical structures including
putamen and accumbens, unlike the studies in older individuals.
Although the studies by Uddin and Wee converge in ﬁnding
that white matter volume was a poor feature for classiﬁcation of
ASD, others have had considerably greater success using features
derived from white matter. Lange et al.37 report high sensitivity
(94%), speciﬁcity (90%) and accuracy (92%) using diffusion tensor
imaging (DTI)-derived metrics in a discovery cohort and a small
replication sample. This region-of-interest-based study speciﬁcally
examined white matter microstructure in the superior temporal
gyrus and temporal stem.

A recent study utilizing 590 6–35-year-old participants from the
Autism Brain Imaging Data Exchange (ABIDE38) data set, however,
was more pessimistic. Using linear and non-linear discriminant
analysis to perform multivariate classiﬁcation based on anatomical
measures (gray matter volume, cortical thickness and cortical
surface area) the authors achieved only 56 and 60% accuracy
based on subcortical volumes and cortical thickness measures,
respectively. The authors take these poor decoding accuracies to
indicate that anatomical differences offer very limited diagnostic
value in ASD.34

Another study also using the ABIDE data set examined
morphometric features from structural MRIs of 361 individuals
with ASD and 373 controls. Using a RF classiﬁer, the authors
demonstrate that only modest classiﬁcation could be achieved
using brain structural properties alone, but that sub-grouping
IQ, autism severity, and age signiﬁcantly
individuals by verbal
improved classiﬁcation accuracy.35 This suggests that to achieve
the highest classiﬁcation accuracies in ASD, multiple different
structural features may need to be combined with behavioral
indices.

Resting-state functional MRI
Resting-state fMRI (rs-fMRI) has been increasingly used over the past
decade to study the development of functional brain circuits, and to
better understand the large-scale organization of the typically and
atypically developing brain.39 Resting-state fMRI entails collecting
functional imaging data from participants as they lay in the MRI
scanner, typically ﬁxating gaze on a cross-hair or with their eyes
closed, and refraining from engaging in any speciﬁc cognitive
task.40 Some of the advantages of using rs-fMRI in pediatric and
clinical populations are that functional brain organization can be
examined independent of task performance, imaging data can be
acquired from otherwise difﬁcult-to-scan populations41 and a full
data set can be collected in as little as 5 min.42

Translational Psychiatry (2017), 1 – 12

In one of

to attempt

the ﬁrst studies to use rs-fMRI
to
discriminate autism from typical development, Anderson and
colleagues used pairwise functional connectivity measures from
regions of interest (ROIs) across the entire brain to demonstrate
that classiﬁcation accuracy of 79% could be obtained using data
from participants aged 8–42. For individuals under the age of 20,
the classiﬁer performed at 89% accuracy. The most informative
connections contributing to successful classiﬁcation were in areas
of the default mode network, anterior insula, fusiform gyrus and
superior parietal lobule.27 This work emphasizes the potential for
classiﬁers to be more accurate and most informative when applied
to subsamples within more restricted age ranges.

Another study examining a younger cohort (age 7–12) using a
logistic regression classiﬁer also found that the salience network,
including the anterior insular cortices, contained information that
could be used to discriminate children with ASD from TD children
with 78% accuracy.30 This study used independent component
analysis (ICA) maps as features for classiﬁcation. Data collected at
another institution could be classiﬁed with 80% accuracy based on
the classiﬁer built by the authors. This type of cross-site validation
of classiﬁers is essential for clinical utility, but has proven to be
difﬁcult. Nielsen et al.29 utilized pairwise connectivity data from
964 subjects collected at 16 different sites to obtain 60%
classiﬁcation accuracy. As in the earlier study from Anderson
et al., connections involving the DMN, parahippocampal and
fusiform gyri, and insula contained the most
information
necessary for accurate classiﬁcation. This study demonstrates the
challenges of building classiﬁers that can perform accurately
across multi-site data sets. Another recent study utilizing data
from ABIDE found that the RF approach produced a classiﬁcation
accuracy of 91% based on a functional connectivity matrix of 220
informative features were
ROIs across the brain.
found to be located in somatosensory, default mode network, and
visual and subcortical regions.33 The most recent study using
resting-state fMRI data from the ABIDE database computed whole-
brain connectomes (functional connectivity matrices between
brain regions of interest) from several atlases to achieve classiﬁ-
cation accuracy (with support vector classiﬁcation approaches) of
67%.43 Connections within the default mode network and parieto-
insular connections contributed most to prediction of diagnostic
category. Finally, a recent study conducted on a large Japanese
cohort achieved 85% accuracy and found that discriminating
features included functional connectivity between regions of the
cingulo-opercular network.44 This rs-fMRI classiﬁcation study used
a unique combination of two machine learning algorithms, L1-
regularized sparse canonical correlation analysis (L1-SCCA) and
sparse logistic regression, and had fair generalizability across
samples, achieving 75% accuracy in an independent validation
cohort.45 Taken together, the emerging picture from rs-fMRI
studies is that discriminating patterns of connectivity in ASD may
reside in DMN and salience/cingulo-opercular network regions.

In this study,

Multimodal MRI
Owing to the sparse nature of the ASD biomarker literature there
is very little information on the use of multimodal MRI to classify
ASD. However, there seems to be potential in combining structural
and resting-state MRI features to discriminate between ASD and
TD groups. A study investigating a wide range of classiﬁers reports
that a random tree classiﬁer using combined cortical thickness
and functional connectivity measures resulted in improved
classiﬁcation and prediction accuracy compared to classiﬁcation
using the single imaging features.32 This study was comprehen-
sive in its inclusion of classiﬁers and features, and the ﬁndings
suggest an integrative model could be fruitful. However, a more
systematic approach to evaluation of classiﬁcation algorithms is
necessary for further progress.

BRAIN-BASED BIOMARKERS OF ADHD

Compared with the ASD biomarker literature,
the biomarker
literature for ADHD has a greater number of studies (Table 2). This
is in part due to the aggregation of a large (N = 973), multi-site,
publicly available data set called ADHD-200 (http://fcon_1000.
projects.nitrc.org/indi/adhd200/)46 with which an orchestrated
global machine learning competition was implemented. The
the
ADHD-200 Global Competition provided a platform for
development of diagnostic classiﬁcation tools for ADHD using
structural and functional MRI data. The best classiﬁer of the 21
competitors in terms of speciﬁcity, or the ability to accurately
classify TD individuals, was from Eloyan et al.,47 who reported 61%
accuracy, 94% speciﬁcity and 21% sensitivity to predict diagnosis
(TD, ADHD-Inattentive or ADHD-Combined). Surprisingly, when
only using phenotypic measures such as site of data collection,
sex, age, handedness and IQ, another study48 achieved higher
classiﬁcation accuracy than any imaging-based classiﬁers (62.52%),
whereas a more recent study demonstrated that combining
phenotypic and functional
imaging data achieved the better
accuracy (65%) than phenotypic data alone (59.6%).49 As this
competition, researchers have continued to test novel classiﬁers to
the most
improve upon these initial
successful classiﬁers below and the features that led to successful
prediction of ADHD diagnosis, focusing on binary (TD vs ADHD)
classiﬁcation.

results. We highlight

Structural MRI
Structural MRI shows promise as a potential biomarker for ADHD.
Several research groups have achieved impressive classiﬁcation
accuracies using predictors such as gray matter volume and
surface area. One of the best-performing classiﬁers for ADHD used
white matter alone to achieve 93% accuracy, with a sensitivity of
100% and speciﬁcity of 85%.56 The researchers reported reduced
white matter in the central pons, which was predictive of ADHD
diagnosis. Similarly, Peng et al.55 reported high classiﬁcation
accuracy (90.18%) using an extreme learning machine (ELM)
features. Discriminative brain
algorithm with multiple cortical
regions included inferior frontal, temporal, occipital and insular
cortices. Another study that used whole-brain gray matter volume
to classify boys with ADHD and TD boys reported 79.3% accuracy,
with 75.9% sensitivity and 82.8% speciﬁcity.54 Similar to the Peng
et al.55 study, Lim and colleagues reported that the ventrolateral
frontal cortex and insula were discriminative.
In addition, this
group also reported that limbic regions such as hippocampus,
amygdala, hypothalamus and ventral striatum were predictive of
ADHD status.54

The structural studies mentioned above were single site studies,
possibly contributing to their high performance. Of note, one
multi-site study using a variety of structural measures obtained
high accuracies for binary classiﬁcation (TD vs ADHD-I: 85.29%, TD
vs ADHD-C: 79.40%), demonstrating that even multi-site studies
have achieved good performance using structural measures.58

Resting-state functional MRI
On one of the largest data sets used to date in ADHD classiﬁcation
(N = 1177)57 achieved 90% accuracy using measures of whole-
brain functional connectivity and an artiﬁcial neural network
algorithm. Of note, these researchers assessed accuracy of binary
classiﬁcation for TD/ADHD-I and TD/ADHD-C separately, which
may have contributed to their
the
researchers regressed out the effects of age, IQ, handedness, sex
and site from each feature set prior to classiﬁcation, indicating that
imaging-speciﬁc features predicted diagnostic status unique from
phenotypic characteristics. They found that OFC-cortical and
cortico-cerebellar functional connectivity was most discriminative.
Similarly, using local and long-distance measures of functional

Interestingly,

success.

7

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

connectivity, Cheng et al.60 found that frontal and cerebellar
regions were most discriminative in classifying ADHD and TD
children. Zhu et al.61 used a measure of local connectivity, regional
homogeneity, to discriminate between ADHD and controls, and
found that the most discriminative brain regions included the PFC,
ACC, and cerebellum. Overall, functional connectivity of frontal
and cerebellar brain regions appear to be good candidates for
future use as features in discriminating individuals with ADHD
from controls.

Multimodal MRI
Few studies have begun to combine structural and rsMRI data to
classify individuals with ADHD from TD individuals. Of those that
have, classiﬁer performance tends to be poorer overall than for
studies utilizing structural or functional data alone.50–53,59 One
exception to this pattern was a study by Qureshi et al.,59 which
for an
used structural and functional data as predictors
impressively high multi-class classiﬁcation (TD, ADHD-I, ADHD-C;
one vs all: 76.19%).59 Their success may have been due to
employing rigorous feature selection in addition to testing more
than one classiﬁer, which demonstrated that the ELM algorithm
outperformed the more traditional SVM.

Comorbidity of ASD and ADHD and cross-diagnostic classiﬁcation
One particularly problematic issue in developing speciﬁc biomar-
kers is the presence of comorbidity across disorders. Rates of
comorbid ADHD symptoms in children with ASD range from 37–
85%,62 with ADHD the second-most common comorbidity in
ASD.63 Conversely, rates of comorbid ASD in children with ADHD
are lower, at about 22%.64,65 Thus, it will be necessary to parse
heterogeneity within these disorders prior
to attempting to
identify biomarkers.

Importantly, the Lim et al.54 study is the only study to date to
test an ADHD-speciﬁc classiﬁer by discriminating adolescents with
ADHD from those with ASD. When classifying these two disorders,
they report even higher accuracy than when discriminating ADHD
from TD (accuracy 85.2 vs 79.3%). To our knowledge, this study is
also the ﬁrst to attempt to discriminate adolescents with ADHD,
ASD, and healthy controls, achieving a balanced accuracy of
68.2%. One other study also considered both ASD and ADHD, but
tested each disorder against healthy controls separately, missing
an opportunity to employ cross-diagnostic classiﬁcation.49 A
recent study applied machine learning to scores derived from
the Social Responsiveness Scale to differentiate between ASD and
ADHD,66 but brain-based features were not evaluated.

LIMITATIONS OF CURRENT APPROACHES
Machine-assisted classiﬁcation of neuroimaging data has provided
a new direction to ASD and ADHD research that has important
implications for diagnosis and treatment. First, the identiﬁcation of
reliable biomarkers can help provide mechanistic explanations of
etiology and behavioral symptomatology. Second, in the long run,
using such markers could better assist behavior-based diagnosis.
This is especially important for complex or borderline cases, where
misdiagnosis is not rare. Third, biomarker screenings could be
risk of
used on infants and young children to assess their
developing a disorder, which is helpful in identifying children at
high risk before they show symptoms.67 Thus, children at high risk
could receive early, targeted treatment and intervention that
would positively impact outcomes of disorders.
Infant sibling
designs aimed at studying high-risk children are among the most
promising avenues for future research. For example, a recent
prospective neuroimaging study found that hyperexpansion of
the cortical surface between 6 and 12 months of age precedes
brain volume overgrowth observed between 12 and 24 months in
high-risk infants diagnosed with ASD at 24 months.14 This type of

Translational Psychiatry (2017), 1 – 12

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

8

a
e
c
n
a
m
r
o
f
r
e
p

s
s
a
l
c
i
t
l
u
M

s
v

C
-
D
H
D
A

D
T

s
v

I
-

D
H
D
A

a
e
c
n
a
m
r
o
f
r
e
p

p
u
o
r
g
b
u
S

l

o
r
t
n
o
c
D
H
D
A

:

a
e
c
n
a
m
r
o
f
r
e
p

)

%

(

y
c
a
r
u
c
c
a

a

)

%

(

,

y
t
i
v
i
t
i
s
n
e
s

y
t
i
c
ﬁ
i
c
e
p
s

,

y
c
a
r
u
c
c
a

e
m
e
h
c
s

n
o
i
t
a
d

i
l

a
V

s
e
r
u
t
a
e
F

d
o
h
t
e
m
n
o
i
t
a
c
ﬁ
i
s
s
a
C

l

)

Q
I
F
(

e
g
n
a
r

Q

I

)
s
r
a
e
y
(

e
g
n
a
r

e
g
A

D
H
D
A

f
o

i

s
e
d
u
t
s

n
o
i
t
a
c
ﬁ
i
s
s
a
l
c

D
T
/
)
F
(

D
H
D
A

f
o

r
e
b
m
u
N

s
t
c
e
b
u
s

j

)
F
(

i

d
e
s
a
b
-
g
n
g
a
m
o
r
u
e
N

i

.
2

e
l
b
a
T

y
d
u
t
S

9
6

R
N

,

R
N

,

5
7

-
s
s
o
r
c

l

d
o
f
-
0
1

c
i
p
y
t
o
n
e
h
p

,
I

R
M

f
-
s
r

t
u
o
d
o
H

l

,

n
o
i
t
a
d

i
l

a
v

b
1
9

,

8
7

,

5
8

-
s
s
o
r
c

t
u
o

n
o

e
v
a
e
L

o
H
e
R

c
R
N

,

R
N

,

6
7

-
s
s
o
r
c

l

d
o
f
-
2

t
e
s

t
u
o
d
o
h

l

,

n
o
i
t
a
d

i
l

a
v

t
e
s

-
g
n
i
t
s
e
r

,
s
e
t
u
b
i
r
t
t
a

l

a
c
i
m
o
t
a
n
a

l

a
c
o
L

s
e
r
u
s
a
e
m
e
t
a
t
s

t
u
o
d
o
h

l

,

n
o
i
t
a
d

i
l

a
v

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

0
8

,

3
3

,

5
5

-
s
s
o
r
c

l

d
o
f
-
0
1

,

e
m
u
o
v

l

,

e
c
a
f
r
u
S

M
V
S

F
B
R

,

E
F
R
M
V
S

t
e
s

M
V
S

F
B
R

d
n
a

,

.

2
4
0
1

n
a
e
m

n
a
e
m
D
T

I
-

D
H
D
A

.

3
4
1
1

R
N

t
u
o
d
o
h

l

,

n
o
i
t
a
d

i
l

a
v

a
t
a
d

,

M
V
S

c
i
b
u
c

,

M
V
S

c
i
t
a
r
d
a
u
q

,

.

5
7
0
1

n
a
e
m

,

M
V
S

r
a
e
n

i
l

,
r
e
ﬁ
i
s
s
a
l
c

c
i
t
s
i
g
o
L

C
-
D
H
D
A

n
a
e
m
C
D
H
D
A

-

I
-

D
H
D
A

,

.

4
1
1

,

.

1
2
1

n
a
e
m

n
a
e
m

l

o
r
t
n
o
C

.

4
2
1

1
4
1

-

C
D
H
D
A

I
-

D
H
D
A

,
)
4
2
(

9
2
4
/
)
6
2
(

8
9

)
4
0
2
(

)
7
2
2
(

8
4
,
.
l

a

t
e

n
w
o
r
B

l

d
n
a
h
o
B

1
5
,
.
l

a

t
e

)
R
N

(

R
N

1
9
4
/
)
R
N

(

5
8
2

2
5
,
.
l

a

t
e

l

y
b
o
C

r
e
ﬁ
i
s
s
a
l
c
M
V
S

r
a
e
n
L

i

R
N

1
2
–
7

2
8
4
/
)
3
5
(

2
7
2

l

s
i
s
y
a
n
a

e
v
i
t
a
n
m

i

i
r
c
s
i
d

r
e
h
s
i
F

d
e
s
a
b
-
A
C
P

0
8
4

.

5
6
1
–
1
1

)
0
(

1
1
/
)
0
(

9

0
5
,
.
l

a

t
e

u
h
Z

Translational Psychiatry (2017), 1 – 12

7
6

.

6
8
6

t
e
s

h
p
a
r
g

,

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

s
c
i
r
t
e
m

.

9
6
5

.

8
9
8

,

.

5
2
2

,

.

9
5
6

-
s
s
o
r
c

d
e
t
s
e
N

,
s
s
e
n
k
c
i
h
t

l

a
c
i
t
r
o
C

l

e
n
r
e
k
-
i
t
l
u
m
F,
B
R
-
M
V
S

R
N

n
a
e
m
C
D
H
D
A

-

2
0
4
/
)
8
4
(

2
2
2

0
8

:

C
-
D
H
D
A

s
v

I
-

D
H
D
A

d
4
9

,

1
2

,

8
7

,
t
e
s

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

t
e
s

t
u
o
d
o
H

l

I

R
M

l

a
r
u
t
c
u
r
t
s

,
I

R
M

f
-
s
r

e
u
a
v

l

l

r
a
u
g
n
S

i

R
N

D
T

m
o
d
n
a
r

,
s
n
o
i
t
i
s
o
p
m
o
c
e
d

,

g
n
i
t
s
o
o
b

i

t
n
e
d
a
r
g

,
t
s
e
r
o
f

R
U
C

,
s
n
o
i
t
i
s
o
p
m
o
c
e
d

,

2
0
2
1

.

7
4
2
1

.

n
a
e
m

n
a
e
m

6
2
–
7

t
u
o
d
o
h

l

,

n
o
i
t
a
d

i
l

a
v

,

o
H
e
R

,

e
m
u
o
v

l

i

g
n
n
r
a
e

l

I
-

D
H
D
A

,

2
3
1
1

.

5
2
1

I
-

D
H
D
A

-

D
H
D
A

,
)
R
N

(

/
)
R
N

(

4
8

H

)
R
N

(

3
6
3

)
4
9
1
(

3
5
,
.
l

a

t
e

i

a
D

7
4
,
.
l

a

t
e

n
a
y
o
E

l

.

2
1
9

,

.

2
6
9

,

4
0
4
9

.

-
s
s
o
r
c

l

d
o
f
-
5

f
o

s
e
r
u
t
a
e
f

l

a
r
u
t
c
u
r
t
S

M
V
S

s

M
V
S

,

i

g
n
g
g
a
b

t
u
o
d
o
h

l

,

n
o
i
t
a
d

i
l

a
v

t
e
s

s
u
e
l
c
u
n

e
t
a
d
u
a
c

n
o
i
t
a
t
n
e
m
g
e
s

R
N

,

R
N

,

.

9
7
5

d
n
a

t
u
o
-
e
n
o
-
e
v
a
e

l

-
g
n
i
t
s
e
r

F,
F
L
A

,

o
H
e
R

,

i

g
n
g
g
a
B

,

1
M

t
s
o
o
B
a
d
A

-
s
s
o
r
c

l

d
o
f
-
K

s
k
r
o
w
t
e
n

e
t
a
t
s

c
i
t
s
i
g
o

l

,

M
V
S

,
t
s
o
o
B
t
i
g
o
L

R
N

n
a
e
m
D
H
D
A

)
2
1
(

9
3
/
)
4
(

9
3

5
9
,
.
l

a

t
e

l

a
u
g

I

n
a
e
m
D
T

,

.

8
0
1

.

7
1
1

R
N

n
a
e
m
D
H
D
A

6
4
5
/
)
7
8
(

3
8
3

n
a
e
m
D
T

,

.

6
1
1

)
0
6
2
(

6
9
,
.
l

a

t
e

o
t
a
S

.

2
5
8

,

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

.

2
8
6

:

D
S
A

s
v
D
H
D
A

e

.

8
2
8

,

.

9
5
7

,

.

3
9
7

t
u
o
-
e
n
o
-
e
v
a
e
L

e
m
u
o
v

l

r
e
t
t
a
m
y
a
r
G

R
N

,

R
N

,

6
7

-
s
s
o
r
c

l

d
o
f
-
0
1

n
o
i
t
a
d

i
l

a
v

t
u
o
d
o
h

l

,

n
o
i
t
a
d

i
l

a
v

t
e
s

d
n
a

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

a
t
a
d

c
i
p
y
t
o
n
e
h
p

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

n
a
i
s
s
u
a
G
y
r
a
n
b

i

n
o
i
t
a
c
ﬁ
i
s
s
a
l
c

s
s
e
c
o
r
p

r
a
e
n
L

i

5
2
1
–
1
8

7
1
–
0
1

/
I
-

D
H
D
A

)
R
N

(

8
9

,

-

C
D
H
D
A

)
0
(

9
2
/
)
0
(

9
2

)
R
N

(

9
2
4

4
5
,
.
l

a

t
e
m
L

i

n
o
i
s
s
e
r
g
e
r

M
V
S

R
N

.

3
2
1

R
N

)
R
N

(

1
4
1

7
9
,
.
l

a

t
e

u
h
d
S

i

t
e
s

t
u
o
d
o
h

l

R
N

,

R
N

,

.

2
0
9

t
u
o
-
e
n
o
-
e
v
a
e
L

d
n
a

s
s
e
n
k
c
i
h
t

l

a
c
i
t
r
o
C

,

i

e
n
h
c
a
m
g
n
n
r
a
e

i

l

e
m
e
r
t
x
E

0
8
4

4
1
–
9

5
5
/
)
R
N

(

5
5

5
5
,
.
l

a

t
e

g
n
e
P

,

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

s
e
r
u
s
a
e
m
e
m
u
o
v

l

F
B
R
-
M
V
S

,

M
V
S

r
a
e
n

i
l

)
R
N

(

e
r
u
t
a
e
f

n
o
i
t
a
d

i
l

a
v

,

p
o
o

l

n
o
i
t
c
e
e
s

l

4
7

,

7
8

,

0
8

.
s
t
s
e
t

n
o
i
t
a
t
u
m
r
e
p

-
s
s
o
r
c

t
u
o
-
e
v
a
e
L

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
r

,

o
H
e
R

r
o
t
c
e
v

t
r
o
p
p
u
s

r
a
e
n
L

i

r
e
ﬁ
i
s
s
a
l
c

n
a
e
m
D
T

,

.

1
5
3

3
4

R
N

n
a
e
m
D
H
D
A

)
5
(

3
2
/
)
5
(

3
2

8
9
,
.
l

a

t
e

g
n
a
W

,

.

6
0
5

.

2
6
7

,

.

8
6
6

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

t
u
o
-
e
n
o
-
e
v
a
e
L

t
e
s

t
u
o
d
o
h

l

h
p
a
r
g

d
n
a

e
r
u
t
c
u
r
t
s

s
c
i
r
t
e
m
y
r
o
e
h
t

e
d
o
m

t
l
u
a
f
e
D

x
i
r
t
a
m
e
v
i
t
a
g
e
n
-
n
o
N

n
o
i
t
a
z
i
r
o
t
c
a
f

R
N

.

8
1
2
–
1
7

.

2
7
4
/
)
5
5
(

6
7
2

)
7
2
2
(

n
o
s
r
e
d
n
A

0
5
,
.
l

a

t
e

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

9

a
e
c
n
a
m
r
o
f
r
e
p

s
s
a
l
c
i
t
l
u
M

s
v

C
-
D
H
D
A

D
T

s
v

I
-

D
H
D
A

)

%

(

y
c
a
r
u
c
c
a

a
)

%

(

,

y
c
a
r
u
c
c
a

,

y
t
i
v
i
t
i
s
n
e
s

y
t
i
c
ﬁ
i
c
e
p
s

.

1
7
5

,

.

8
9
7

,

.

6
9
6

-
s
s
o
r
c

l

d
o
f
-
5

l

a
n
o
s
r
e
P

a
e
c
n
a
m
r
o
f
r
e
p

p
u
o
r
g
b
u
S

l

o
r
t
n
o
c
D
H
D
A

:

a
e
c
n
a
m
r
o
f
r
e
p

e
m
e
h
c
s

n
o
i
t
a
d

i
l

a
V

s
e
r
u
t
a
e
F

d
o
h
t
e
m
n
o
i
t
a
c
ﬁ
i
s
s
a
C

l

)

Q
I
F
(

e
g
n
a
r

Q

I

)
s
r
a
e
y
(

e
g
n
a
r

e
g
A

5
8

,

0
0
1

,

3
9

t
u
o
-
e
n
o
-
e
v
a
e
L

y
a
r
g

,
I

R
M

l

a
r
u
t
c
u
r
t
S

M
V
S

r
a
e
n

i
l
-
n
o
N

n
a
e
m
D
H
D
A

t
u
o
d
o
h

l

,

n
o
i
t
a
d

i
l

a
v

d
n
a

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

)

C
P
H
M

(

n
o
i
t
a
c
ﬁ
i
s
s
a
l
c

t
n
e
i
t
a
p

s
e
r
u
t
a
e
f

t
e
s

i

n
a
r
b

l

a
r
u
t
c
u
r
t
s

m
h
t
i
r
o
g
a

l

i

g
n
n
r
a
e

l

4
1
1

n
a
e
m

D
T

,

7
0
1

.

2
2
1
n
a
e
m

D
T

,

.

6
1
1

d
e
s
a
b
-
e
r
u
t
a
e
f
-

G
O
H

I

R
M

)
f
(

n
a
e
m
D
H
D
A

n
a
e
m
D
H
D
A

0
9
4
/
)
1
2
(

.

7
5
8

:

C
-
D
H
D
A

:

D
T

.

7
5
8

,

.

9
2
9

,

.

9
2
9

:

C
-
D
H
D
A

0
0
1

,

.

7
5
8

;

i

g
n
g
a
m

i

e
c
n
a
n
o
s
e
r

c
i
t
e
n
g
a
m

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

,
I

R
M

f

;
t
n
e
i
t
o
u
q

e
c
n
e
g

i
l
l

e
t
n

i

l

e
a
c
s
-
l
l

u
F

,

Q
F

I

;

l

e
a
m
e
f

,

F

;

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

.

8
0
6

:
I
-

D
H
D
A

,

.

3
5
8

:
I
-

D
H
D
A

.

3
0
8

:

C
-
D
H
D
A

-

D
H
D
A

:

D
T

R
N

:

D
T

,

R
N

i

g
n
n
o
i
t
i
t
r
a
p

0
3
/
0
7

-
s
s
o
r
c

l

d
o
f
-
0
1

d
n
a

s
s
e
n
k
c
i
h
t

l

a
c
i
t
r
o
C

R
N

,

R
N

,

.

4
9
7

:

C

.

n
o
i
t
a
d

i
l

a
v

r
e
ﬁ
i
s
s
a
l
c

i

e
n
h
c
a
m
g
n
n
r
a
e

i

l

e
m
e
r
t
x
e

l

a
c
i
h
c
r
a
r
e
H

i

R
N

,

R
N

,

0
9

:

C

.
t
e
s

t
u
o
d
o
h

l

r
u
t
c
e
t
i
h
c
r
a

)

N
N
A

(

k
r
o
w
t
e
n

0
8

,

1
8

,

1
8

t
u
o
-
e
n
o
-
e
v
a
e

l

s
s
e
n
k
c
i
h
t

l

a
c
i
t
r
o
C

d
e
s
a
b
-
n
o
i
t
a
m
r
o
f
n

i

l

a
u
t
u
M

,

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

t
e
s

t
u
o
d
o
h

l

s
e
r
u
t
a
e
f

-
o
s
s
a
L

d
n
a

i

g
n
k
n
a
r

e
r
u
t
a
e
f

n
o
i
t
c
e
e
s

l

e
r
u
t
a
e
f

d
e
s
a
b

5
9

:

C
-
D
H
D
A

-

D
H
D
A

:

D
T
R
N

,

R
N

:

I
-

D
H
D
A

,

0
9

:
I
-

D
H
D
A

:

D
T

t
u
o
-
e
n
o
-
e
v
a
e
L

.
t
e
s

t
u
o
d
o
h

l

,

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

,

n
o
i
t
a
d

i
l

a
v
-
s
s
o
r
c

r
e
t
t
a
m
e
t
i
h
w
d
n
a

e
m
u
o
v

l

i

n
a
r
b

l

a
n
o
i
t
c
n
u
F

e
d
a
c
s
a
c

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
r
u
e
n

d
e
t
c
e
n
n
o
c

l

a
i
c
ﬁ
i
t
r
a

y

l
l

u
F

)

C
C
F
(

.

2
6
7

:
I
-

D
H
D
A

,

.

3
9
8

:
I
-

D
H
D
A
D
T

:

t
s
e
t

n
o
i
t
a
t
u
m
r
e
P

s
e
r
u
t
a
e
f

l

a
r
u
t
c
u
r
t
S

i

e
n
h
c
a
m
g
n
n
r
a
e

i

l

e
m
e
r
t
x
E

r
e
ﬁ
i
s
s
a
l
c

.

7
3
0
1

n
a
e
m

D
T

,

.

8
9
9

R
N

R
N

R
N

R
N

R
N

4
1
–
7

0
6
2

,
I
-

D
H
D
A

-

D
H
D
A

)
R
N

(

)
R
N

(

4
4
7
/
C

-

D
H
D
A

)
9
(

3
5

3
5

,

-

C
D
H
D
A

)
9
(

3
5

,
I

)
R
N

(

3
7
1

R
N

5
1
/
)
R
N

(

D
T

)
9
(

2
3

)
R
N

(

4
1
–
7

-

D
H
D
A

)
9
(

3
5

3
5

,

-

C
D
H
D
A

)
9
(

3
5

,
I

D
T

)
9
(

.

4
8
1
–
5
8

.

)
0
(
4
3
/
)
0
(

4
3

n
a
i
s
s
a
h
G

i

9
4
,
.
l

a

t
e

n
o
t
s
n
h
o
J

6
5
,
.
l

a

t
e

e
d
n
a
p
h
s
e
D

7
5
,
l

a

t
e

9
9
,
.
l

a

t
e

o
a
X

i

i

h
s
e
r
u
Q

8
5
,
.
l

a

t
e

i

h
s
e
r
u
Q

9
5
,
.
l

a

t
e

e
s
u

s
r
o
h
t
u
a

r
e
v
e
w
o
h

y
c
a
r
u
c
c
a

t
s
e
b
s
t
r
o
p
e
r

l

e
b
a
t

D
S
A
h
t
o
b
d
e
d
u
l
c
n

i

p
u
o
r
g

l

o
r
t
n
o
C
e

.

4

.
s
n
o
i
t
a
c
ﬁ
i
s
s
a
l
c

e
t
o
N
c

.

y
c
a
r
u
c
c
a

f
o

d
a
e
t
s
n

i

d
e
t
r
o
p
e
r

e
t
a
r

n
o
i
t
a
z
i
l

a
r
e
n
e
G
b

.

y
c
a
r
u
c
c
a

t
s
e
t
a
e
r
g

h
t
i

w

r
e
ﬁ
i
s
s
a
l
c

o
t

s
r
e
f
e
R
a

.
r
e
t
t
a
m
e
t
i
h
w

,

M
W

t
c
e
r
r
o
c

f
o
e
g
a
t
n
e
c
r
e
p

l
l

a
r
e
v
o
f
o
n
o
i
t
i
n
ﬁ
e
d
d
r
a
d
n
a
t
s

m
o
r
f
n
o
i
t
c
n
i
t
s
i
d
e
t
o
N

’.
s
t
n
o
p

i

l

a
t
o
t

t
n
e
c
r
e
p

‘

s
a
d
e
n
ﬁ
e
d
y
c
a
r
u
c
c
A
d

r
a
e
n

i
l

,

A
D
L

;

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

l

d
e
z
i
r
a
u
g
e
r
-
2
L

,

R
L
2
L

;

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

l

d
e
z
i
r
a
u
g
e
r
-
1
L

,

R
L
1
L

i

;
r
o
b
h
g
e
n
t
s
e
r
a
e
n
-
k

,

N
N
K

;

d
o
h
t
e
m
g
n
i
t
s
o
o
b
t
n
e
d
a
r
g

i

i

;
s
e
y
a
B
e
v
a
n
n
a
i
s
s
u
a
G

,

B
N
G

;
r
e
t
t
a
m
y
a
r
g

,

M
G

;
s
e
e
r
t

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

,

T
F

;

k
r
o
w
t
e
n

l

a
r
u
e
n

c
i
t
s
i
l
i

b
a
b
o
r
p

,

N
N
P

;

Q

I

e
c
n
a
m
r
o
f
r
e
p

,

Q
P

I

;

Q

I

l

a
b
r
e
v
n
o
n

,

I

Q
V
N

;

d
e
t
r
o
p
e
r

t
o
n

n
o
i
t
a
m
r
o
f
n

i

,

R
N

;
s
n
o
r
t
p
e
c
r
e
p

r
e
y
a

l
i
t
l
u
m
P,
L
M

;

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

,

R
L

;
s
e
e
r
t

l

e
d
o
m
c
i
t
s
i
g
o

l

,

T
M
L

;
s
i
s
y
a
n
a

l

t
n
a
n
m

i

i
r
c
s
i
d

i

;
s
e
n
h
c
a
m

r
o
t
c
e
v

t
r
o
p
p
u
s

,

M
V
S

;
I

R
M

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
r

,
I

R
M

f
-
s
r

;

n
o
i
t
a
n
m

i

i
l

e

e
r
u
t
a
e
f

e
v
i
s
r
u
c
e
r

,

E
F
R

;
t
s
e
r
o
f

m
o
d
n
a
r

,

F
R

;

n
o
i
t
c
n
u
f

s
i
s
a
b

l

i

a
d
a
r
-
F
B
R

;
s
i
s
y
a
n
a

l

t
n
a
n
m

i

i
r
c
s
i
d
c
i
t
a
r
d
a
u
q

,

A
D
Q

;

n
o
i
t
a
z
i
m

i
t
p
o
m
r
a
w
s

e
l
c
i
t
r
a
p

,

O
S
P

;

Q

I

l

a
b
r
e
v

,

Q
V

I

;
t
n
e
m
p
o
e
v
e
d

l

l

a
c
i
p
y
t

,

D
T

.

l

n
o
i
t
a
u
a
v
e
f
o
d
o
h
t
e
m
d
e
r
r
e
f
e
r
p
s
a
C
U
A

j

.
s
t
c
e
b
u
s
D
T

d
n
a

Translational Psychiatry (2017), 1 – 12

l

d
e
z
i
r
a
u
g
e
r
-
t
e
n
-
c
i
t
s
a
e

l

,

R
L
N
E

;
r
e
d
r
o
s
i
d

y
t
i
v

i
t
c
a
r
e
p
y
h
/
t
i
c
ﬁ
e
d
-
n
o
i
t
n
e
t
t
a

,

D
H
D
A

i

:
s
n
o
i
t
a
v
e
r
b
b
A

)
F
(

9
7
2

)
7
4
(

D
T
/
)
F
(

D
H
D
A

f
o

r
e
b
m
u
N

s
t
c
e
b
u
s

j

y
d
u
t
S

)

d
e
u
n
i
t
n
o
C

(

.
2

e
l
b
a
T

10

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

longitudinal work will be necessary to develop true biomarkers for
any neurodevelopmental disorder.

Despite the promise and potential of neuroimaging-based
inconsistency in the current classiﬁcation literature
markers,
suggests that more empirical work must be undertaken. Several
factors including participant age, type of classiﬁer used, and
sample size contribute to these inconsistencies.
In the case of
sample size, it is difﬁcult to compare two studies where one tested
1000 participants (for example) and achieved a classiﬁcation
accuracy of 60% and another tested 40 participants and achieved
a classiﬁcation accuracy of 80%. Furthermore, as most studies
used different classiﬁcation algorithms and included different
it is not possible at present to directly
neuroimaging features,
compare results from various studies. A recent review highlights
these issues, pointing out that almost all studies that have
reported high classiﬁcation accuracies had sample sizes smaller
than 100.3

It is important to note that biomarkers must meet several
criteria before being used clinically. First, a biomarker should be
present before symptoms begin to serve predictive value. All
studies reviewed here were conducted in school-age children and
older individuals. Sampling younger children is necessary to
examine the predictive power of early-identiﬁed brain features.
it is quite possible that features identiﬁed in the
Furthermore,
existing literature might reﬂect either causal or compensatory
differences in brain function and structure, and that these features
may not be the same as those that are most predictive at early
ages. Studies should ideally prospectively screen young children
and longitudinally track the occurrence of symptoms.
It has
already been shown in studies of high-risk infants that develop-
mental trajectories of white matter are most predictive of later
ASD diagnosis.68 This suggests that critical information necessary
for accurate classiﬁcation may be overlooked in cross-sectional
investigations.

Second, a biomarker must be deﬁned independently of
diagnostic symptoms; otherwise, the classiﬁer is validated using
the same features that created it. In other words, the relationship
between the biomarker and neuropathology must be clear.69 So
far, neuroimaging studies have found an array of potential
markers and there is not yet convergence on proposed mechan-
isms. Third, the biomarker must be speciﬁc to the disorder rather
than a hallmark of general pathology. For instance, abnormal DMN
functional connectivity has been associated with both ASD and
schizophrenia.70,71 There are also overlapping biomarkers in
children with autism and their unaffected siblings.72,73 To achieve
speciﬁcity, the classiﬁer must be tested on large samples that
include a variety of disorders. Neuroimaging databases, such
ABIDE and the UCLA Multimodal Connectivity Database, can help
provide these large samples to test classiﬁers on. A classiﬁcation
model should be precisely deﬁned and validated across research-
sites and populations. Further, a biomarker should have high
diagnostic performance in classiﬁcation, as measured by sensitiv-
ity and speciﬁcity.69 One recent study in ASD has demonstrated
that classiﬁcation via behavioral measures (in this case scores on
the Social Responsiveness Scale) outperformed classiﬁcation
rs-fMRI data.74 However, brain-based
based on analysis of
biomarkers are at a clear disadvantage compared with behavioral
measures, as behavioral measures were designed based on
diagnostic
criteria. Once diagnoses are more biologically
grounded rather than relying solely on observation and interview,
it is the hope that early and more objective diagnoses can be
achieved.

Other limitations of current approaches include the practice of
recruitment of equal case and control samples. In almost all of the
studies reviewed here, equal numbers of individuals with ASD or
ADHD were included. However, if one wants to apply a classiﬁer to
the general population where the prevalence of the disorder
ranges from 1.5 to 11%, this can lead to ascertainment bias. For

Translational Psychiatry (2017), 1 – 12

ideal classiﬁer of 95% sensitivity and
example, with a near
speciﬁcity, in 1000 individuals we would accurately identify about
14 of the 15 children with ASD (true positive), but we would
inaccurately identify 49 of the remaining 986 as having ASD (false
positive) if we assume no other disorders are present.
In this
example, only 14/63 (22%) of positive identiﬁcations would be
true cases of ASD.

Biomarkers will not replace clinical assessments, which char-
acterize the extent of speciﬁc deﬁcits, but could potentially
change treatment goals and methods.67 There are ﬁnancial
barriers to this development, however. MRI is an expensive tool
that is unlikely to be used regularly outside of dense urban areas
or major hospitals. In ‘Future directions’, we highlight alternative
neuroimaging approaches that may prove more feasible in the
clinical setting.

In the future, a biomarker could potentially be necessary to
receive treatment or insurance coverage, but this will surely create
issues if a subset of patients has symptoms but no identiﬁable
biomarker. Finally, families should be given accurate information
on what the presence of a biomarker means for their child. It is
important not to develop a deterministic view, as it is likely that a
biomarker only signiﬁes an increased risk of developing the
inﬂuence the choices that parents and
disorder. This will
physicians make regarding treatment.

FUTURE DIRECTIONS: INCREASING SAMPLE HETEROGENEITY

All of the reviewed studies recruited individuals without ID who
could successfully complete MRI scans. Of course, this biases the
studies to high-functioning individuals, and it is not clear how well
the results generalize to the broader population of children with
ASD and ADHD. Even within high-functioning individuals, MRI
success rates can vary.41 There are a few approaches that in
principle could be applied to a greater range of children at varying
levels of intellectual function. Sedation and natural sleep75 have
been used and can facilitate the collection of neuroimaging data
from otherwise inaccessible children. In addition, neuroimaging
approaches such as electroencephalography, magnetoencephalo-
graphy or functional near-infrared spectroscopy (fNIRS), which do
not place as stringent requirements on participants to remain
motionless, are potentially useful tools with which to derive brain
features for classiﬁcation. Though these methods have limited
spatial resolution, making it difﬁcult to assess the contributions of
speciﬁc brain regions, they can in principle be utilized to a greater
extent in future work in biomarker development.

At present, the ﬁeld has not yet reached the point where we can
use brain-based biomarkers to diagnose individuals with a speciﬁc
disorder. However, the studies reviewed here are instrumental in
identifying key dysfunctional brain regions and circuits, moving us
closer to understanding the biological basis of these prevalent
neurodevelopmental disorders.

CONFLICT OF INTEREST
The authors declare no conﬂict of interest.

ACKNOWLEDGMENTS

This work was supported by awards K01MH092288 and R01MH107549 from the
National
Institute of Mental Health, a Slifka/Ritvo Innovation in Autism Research
Award, and a NARSAD Young Investigator Grant to L.Q.U.

REFERENCES
1 Strimbu K, Tavel JA. What are biomarkers?. Curr Opin HIV AIDS 2010; 5: 463–466.
2 Woo CW, Chang LJ, Lindquist MA, Wager TD. Building better biomarkers: brain

models in translational neuroimaging. Nat Neurosci 2017; 20: 365–377.

3 Arbabshirani MR, Plis S, Sui J, Calhoun VD. Single subject prediction of brain
disorders in neuroimaging: promises and pitfalls. NeuroImage. 2017; 145(Pt B):
137–165.

4 Matson JL, Rieske RD, Williams LW. The relationship between autism spectrum
disorders and attention-deﬁcit/hyperactivity disorder: an overview. Res Dev Disabil
2013; 34: 2475–2484.

5 Christensen DL, Baio J, Van Naarden Braun K, Bilder D, Charles J, Constantino JN
et al. Prevalence and characteristics of autism spectrum disorder among children
aged 8 years—autism and developmental disabilities monitoring network, 11
sites, United States, 2012. MMWR Surveill Summ 2016; 65: 1–23.

6 Visser SN, Danielson ML, Bitsko RH, Holbrook JR, Kogan MD, Ghandour RM et al.
Trends in the parent-report of health care provider-diagnosed and medicated
attention-deﬁcit/hyperactivity disorder: United States, 2003-2011. J Am Acad Child
Adoles Psychiatry 2014; 53: 34–46 e2.

7 Horlin C, Falkmer M, Parsons R, Albrecht MA, Falkmer T. The cost of autism

spectrum disorders. PLoS ONE 2014; 9: e106552.

8 Klin A, Klaiman C, Jones W. Reducing age of autism diagnosis: developmental social
neuroscience meets public health challenge. Rev Neurol 2015; 60(Suppl 1): S3–11.
9 Lord C, Risi S, Lambrecht L, Cook EH Jr, Leventhal BL, DiLavore PC et al. The autism
diagnostic observation schedule-generic: a standard measure of social and
communication deﬁcits associated with the spectrum of autism. J Autism Dev
Disord 2000; 30: 205–223.

10 Lord C, Rutter M, Le Couteur A. Autism diagnostic interview-revised: a revised
version of a diagnostic interview for caregivers of individuals with possible per-
vasive developmental disorders. J Autism Dev Disord 1994; 24: 659–685.

11 American Psychiatric Association Diagnostic and Statistical Manual of Mental

Disorders. 5th edn. American Psychiatric Publishing: Arlington, VA, 2013.

12 Lord C, Petkova E, Hus V, Gan W, Lu F, Martin DM et al. A multisite study of the
clinical diagnosis of different autism spectrum disorders. Arch Gen Psychiatry 2012;
69: 306–313.

13 Yerys BE, Pennington BF. How do we establish a biological marker for a beha-
viorally deﬁned disorder? Autism as a test case. Autism Res 2011; 4: 239–241.
14 Hazlett HC, Gu H, Munsell BC, Kim SH, Styner M, Wolff JJ et al. Early brain
development in infants at high risk for autism spectrum disorder. Nature 2017;
542: 348–351.

15 Insel TR. The NIMH Research Domain Criteria (RDoC) Project: precision medicine

for psychiatry. Am J Psychiatry 2014; 171: 395–397.
16 Lilienfeld SO, Treadway MT. Clashing diagnostic
versus RDoC. Ann Rev Clin Psychol 2016; 12: 435–463.

17 Burges CJC. A tutorial on support vector machines for pattern recognition. Data

Min Knowledge Discov 1998; 2: 121–167.

18 Craddock RC, Holtzheimer PE 3rd, Hu XP, Mayberg HS. Disease state prediction
from resting state functional connectivity. Magn Reson Med 2009; 62: 1619–1628.
19 LaConte SM. Decoding fMRI brain states in real-time. NeuroImage 2011; 56:

440–454.

20 Pereira F, Mitchell T, Botvinick M. Machine learning classiﬁers and fMRI: a tutorial

overview. NeuroImage. 2009; 45(1 Suppl): S199–S209.

21 Quinlan J. Induction of decision trees. Mach Learn 1986; 1: 81–106.
22 Breiman L. Random forests. Mach Learn 2001; 45: 4–32.
23 Domingos P. A few useful things to know about machine learning. Commun ACM

2012; 55: 78.

24 Hastie T, Tibshirani R, Friedman J. The Elements of Statistical Learning: Data Mining,

Inference, and Prediction. Springer: New York, NY, USA, 2009.

25 Developmental Disabilities Monitoring Network Surveillance Year Principal
Investigators. Prevalence of autism spectrum disorder among children aged 8
years—autism and developmental disabilities monitoring network, 11 sites,
United States, 2010. MMWR Surveill Summ 2014; 63(Suppl 2): 1–21.

26 Lord C, Rutter M, DiLavore P, Risi S, Gotham K, Bishop S. Autism Diagnostic
Observation Schedule–2nd Edition (ADOS-2). Western Psychological Corporation:
Los Angeles, CA, USA, 2012.

27 Anderson JS, Nielsen JA, Froehlich AL, DuBray MB, Druzgal TJ, Cariello AN et al.
Functional connectivity magnetic resonance imaging classiﬁcation of autism.
Brain 2011; 134(Pt 12): 3742–3754.

28 Uddin LQ, Menon V, Young CB, Ryali S, Chen T, Khouzam A et al. Multivariate
searchlight classiﬁcation of structural magnetic resonance imaging in children
and adolescents with autism. Biol Psychiatry 2011; 70: 833–841.

29 Nielsen JA, Zielinski BA, Fletcher PT, Alexander AL, Lange N, Bigler ED et al.
Multisite functional connectivity MRI classiﬁcation of autism: ABIDE results. Front
Hum Neurosci 2013; 7: 599.

30 Uddin LQ, Supekar K, Lynch CJ, Khouzam A, Phillips J, Feinstein C et al. Salience
network-based classiﬁcation and prediction of symptom severity in children
with autism. JAMA Psychiatry 2013; 70: 869–879.

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

11

32 Zhou Y, Yu F, Duong T. Multiparametric MRI characterization and prediction in
autism spectrum disorder using graph theory and machine learning. PLoS ONE
2014; 9: e90405.

33 Chen CP, Keown CL, Jahedi A, Nair A, Pﬂieger ME, Bailey BA et al. Diagnostic
classiﬁcation of intrinsic functional connectivity highlights somatosensory, default
mode, and visual regions in autism. NeuroImage Clin 2015; 8: 238–245.

34 Haar S, Berman S, Behrmann M, Dinstein I. Anatomical abnormalities in autism?

Cereb Cortex 2016; 26: 1440–1452.

35 Katuwal GJ, Baum SA, Cahill ND, Michael AM. Divide and conquer: sub-grouping
of ASD improves ASD detection based on brain morphometry. PLoS ONE 2016; 11:
e0153331.

36 Ecker C, Marquand A, Mourao-Miranda J, Johnston P, Daly EM, Brammer MJ et al.
Describing the brain in autism in ﬁve dimensions—magnetic resonance imaging-
assisted diagnosis of autism spectrum disorder using a multiparameter classiﬁ-
cation approach. J Neurosci 2010; 30: 10612–10623.

37 Lange N, Dubray MB, Lee JE, Froimowitz MP, Froehlich A, Adluru N et al.
Atypical diffusion tensor hemispheric asymmetry in autism. Autism Res 2010; 3:
350–358.

38 Di Martino A, Yan CG, Li Q, Denio E, Castellanos FX, Alaerts K et al. The autism
brain imaging data exchange: towards a large-scale evaluation of the intrinsic
brain architecture in autism. Mol Psychiatry 2014; 19: 659–667.

39 Uddin LQ, Supekar K, Menon V. Typical and atypical development of functional
human brain networks: insights from resting-state FMRI. Front Syst Neurosci 2010;
4: 21.

40 Biswal B, Yetkin FZ, Haughton VM, Hyde JS. Functional connectivity in the motor
cortex of resting human brain using echo-planar MRI. Magn Reson Med 1995; 34:
537–541.

41 Yerys BE, Jankowski KF, Shook D, Rosenberger LR, Barnes KA, Berl MM et al. The
fMRI success rate of children and adolescents: typical development, epilepsy,
attention deﬁcit/hyperactivity disorder, and autism spectrum disorders. Hum
Brain Map 2009; 30: 3426–3435.

42 Van Dijk KR, Hedden T, Venkataraman A, Evans KC, Lazar SW, Buckner RL. Intrinsic
functional connectivity as a tool for human connectomics: theory, properties, and
optimization. J Neurophysiol 2009; 103: 297–321.

43 Abraham A, Milham MP, Di Martino A, Craddock RC, Samaras D, Thirion B et al.
Deriving reproducible biomarkers from multi-site resting-state data: an autism-
based example. NeuroImage 2017; 147: 736–745.

architecture of top-down control. Trends Cogn Sci 2008; 12: 99–105.

45 Yahata N, Morimoto J, Hashimoto R, Lisi G, Shibata K, Kawakubo Y et al. A small
number of abnormal brain connections predicts adult autism spectrum disorder.
Nat Commun 2016; 7: 11254.

46 The ADHD-200 Consortium. The ADHD-200 Consortium: a model to advance the
translational potential of neuroimaging in clinical neuroscience. Front Syst Neu-
rosci 2012; 6: 62.

47 Eloyan A, Muschelli J, Nebel MB, Liu H, Han F, Zhao T et al. Automated diagnoses
of attention deﬁcit hyperactive disorder using magnetic resonance imaging. Front
Syst Neurosci 2012; 6: 61.

48 Brown MR, Sidhu GS, Greiner R, Asgarian N, Bastani M, Silverstone PH et al.
ADHD-200 Global Competition: diagnosing ADHD using personal characteristic
data can outperform resting state fMRI measurements. Front Syst Neurosci 2012;
6: 69.

49 Ghiassian S, Greiner R, Jin P, Brown MR. Using functional or structural magnetic
resonance images and personal characteristic data to identify ADHD and autism.
PLoS ONE 2016; 11: e0166934.

50 Anderson A, Douglas PK, Kerr WT, Haynes VS, Yuille AL, Xie J et al. Non-negative
matrix factorization of multimodal MRI,
fMRI and phenotypic data reveals
differential changes in default mode subnetworks in ADHD. NeuroImage 2014;
102(Pt 1): 207–219.

51 Bohland JW, Saperstein S, Pereira F, Rapin J, Grady L. Network, anatomical, and
non-imaging measures for the prediction of ADHD diagnosis in individual sub-
jects. Front Syst Neurosci 2012; 6: 78.

52 Colby JB, Rudie JD, Brown JA, Douglas PK, Cohen MS, Shehzad Z. Insights into
multimodal imaging classiﬁcation of ADHD. Front Syst Neurosci 2012; 6: 59.
53 Dai D, Wang J, Hua J, He H. Classiﬁcation of ADHD children through multimodal

magnetic resonance imaging. Front Syst Neurosci 2012; 6: 63.

54 Lim L, Marquand A, Cubillo AA, Smith AB, Chantiluke K, Simmons A et al. Disorder-
speciﬁc predictive classiﬁcation of adolescents with attention deﬁcit hyperactivity
disorder (ADHD) relative to autism using structural magnetic resonance imaging.
PLoS ONE 2013; 8: e63660.

55 Peng X, Lin P, Zhang T, Wang J. Extreme learning machine-based classiﬁcation of

ADHD using brain structural MRI data. PLoS ONE 2013; 8: e79476.

approaches: DSM-ICD

44 Dosenbach NU, Fair DA, Cohen AL, Schlaggar BL, Petersen SE. A dual-networks

31 Wee CY, Wang L, Shi F, Yap PT, Shen D. Diagnosis of autism spectrum disorders
using regional and interregional morphological features. Hum Brain Map 2014; 35:
3414–3430.

56 Johnston BA, Mwangi B, Matthews K, Coghill D, Konrad K, Steele JD. Brainstem
abnormalities in attention deﬁcit hyperactivity disorder support high accuracy
individual diagnostic classiﬁcation. Hum Brain Map 2014; 35: 5179–5189.

Translational Psychiatry (2017), 1 – 12

12

Biomarkers of neurodevelopmental disorders
LQ Uddin et al

57 Deshpande G, Wang P, Rangaprakash D, Wilamowski B. Fully connected cascade
artiﬁcial neural network architecture for attention deﬁcit hyperactivity disorder
classiﬁcation from functional magnetic resonance imaging data.
IEEE Trans
Cybernet 2015; 45: 2668–2679.

58 Qureshi MN, Min B, Jo HJ, Lee B. Multiclass classiﬁcation for the differential diagnosis
on the ADHD subtypes using recursive feature elimination and hierarchical extreme
learning machine: structural MRI study. PLoS ONE 2016; 11: e0160697.

59 Qureshi MNI, Oh J, Min B, Jo HJ, Lee B. Multi-modal, multi-measure, and multi-
class discrimination of ADHD with hierarchical feature extraction and extreme
learning machine using structural and functional brain MRI. Front Hum Neurosci
2017; 11: 157.

60 Cheng W, Ji X, Zhang J, Feng J. Individual classiﬁcation of ADHD patients by
integrating multiscale neuroimaging markers and advanced pattern recognition
techniques. Front Syst Neurosci 2012; 6: 58.

61 Zhu CZ, Zang YF, Cao QJ, Yan CG, He Y, Jiang TZ et al. Fisher discriminative
analysis of resting-state brain function for attention-deﬁcit/hyperactivity disorder.
NeuroImage 2008; 40: 110–120.

62 Leitner Y. The co-occurrence of autism and attention deﬁcit hyperactivity disorder

in children - what do we know? Front Hum Neurosci 2014; 8: 268.

63 Simonoff E, Pickles A, Charman T, Chandler S, Loucas T, Baird G. Psychiatric dis-
orders in children with autism spectrum disorders: prevalence, comorbidity, and
associated factors in a population-derived sample. J Am Acad Child Adolesc Psy-
chiatry 2008; 47: 921–929.

64 van der Meer JM, Oerlemans AM, van Steijn DJ, Lappenschaar MG, de Sonneville
LM, Buitelaar JK et al. Are autism spectrum disorder and attention-deﬁcit/hyper-
activity disorder different manifestations of one overarching disorder? Cognitive
and symptom evidence from a clinical and population-based sample. J Am Acad
Child Adolesc Psychiatry 2012; 51: 1160–72 e3.

65 Ronald A, Simonoff E, Kuntsi J, Asherson P, Plomin R. Evidence for overlapping
genetic inﬂuences on autistic and ADHD behaviours in a community twin sample.
J Child Psychol Psychiatry 2008; 49: 535–542.

66 Duda M, Haber N, Daniels J, Wall DP. Crowdsourced validation of a machine-
learning classiﬁcation system for autism and ADHD. Transl Psychiatry 2017; 7:
e1133.

67 Walsh P, Elsabbagh M, Bolton P, Singh I.

In search of biomarkers for autism:

scientiﬁc, social and ethical challenges. Nat Rev Neurosci 2011; 12: 603–612.
68 Wolff JJ, Gu H, Gerig G, Elison JT, Styner M, Gouttard S et al. Differences in white
from 6 to 24 months in infants

matter ﬁber
with autism. Am J Psychiatry 2012; 169: 589–600.

tract development present

69 Woo CW, Wager TD. Neuroimaging-based biomarker discovery and validation.

Pain 2015; 156: 1379–1381.

80 Ecker C, Rocha-Rego V, Johnston P, Mourao-Miranda J, Marquand A, Daly EM et al.
Investigating the predictive value of whole-brain structural MR scans in autism: a
pattern classiﬁcation approach. Neuroimage 2010b; 49: 44–56.

81 Jiao Y, Chen R, Ke X, Chu K, Lu Z, Herskovits EH. Predictive models of autism
spectrum disorder based on brain regional cortical thickness. Neuroimage 2010;
50: 589–599.

82 Calderoni S, Retico A, Biagi L, Tancredi R, Muratori F, Tosetti M. Female children
with autism spectrum disorder: an insight from mass-univariate and pattern
classiﬁcation analyses. Neuroimage 2012; 59: 1013–1022.

83 Ingalhalikar M1, Parker WA, Bloy L, Roberts TP, Verma R. Using multiparametric
data with missing features for learning patterns of pathology. Med Image Comput
Comput Assist Interv 2012; 15(Pt 3): 468–475.

84 Deshpande G, Libero LE, Sreenivasan KR, Deshpande HD, Kana RK. Identiﬁcation
of neural connectivity signatures of autism using machine learning. Front Hum
Neurosci 2013; 7: 670.

85 Sato JR, Hoexter MQ, Oliveira PP Jr, Brammer MJ, AIMS MRC Consortium, Murphy D,
Inter-regional cortical thickness correlations are associated with autistic

Ecker C.
symptoms: a machine-learning approach. J Psychiatr Res 2013; 47: 453–459.

86 Plitt M, Barnes KA, Martin A. Functional connectivity classiﬁcation of autism
identiﬁes highly predictive brain features but falls short of biomarker standards.
Neuroimage Clin 2014; 7: 359–366.

87 Segovia F, Holt R, Spencer M, Górriz JM, Ramírez J, Puntonet CG et al. Identifying
endophenotypes of autism: a multivariate approach. Front Comput Neurosci 2014;
8: 60.

88 Gori I, Giuliano A, Muratori F, Saviozzi I, Oliva P, Tancredi R et al. Gray matter
alterations in young children with autism spectrum disorders: comparing mor-
phometry at the voxel and regional level. J Neuroimaging 2015; 25: 866–874.
89 Iidaka T. Resting state functional magnetic resonance imaging and neural net-

work classiﬁed autism and control. Cortex 2015; 63: 55–67.

90 Libero LE, DeRamus TP, Lahti AC, Deshpande G, Kana RK. Multimodal neuroi-
maging based classiﬁcation of autism spectrum disorder using anatomical, neu-
rochemical, and white matter correlates. Cortex 2015; 66: 46–59.

91 Lombardo MV, Pierce K, Eyler LT, Carter Barnes C, Ahrens-Barbeau C, Solso S et al.
Different functional neural substrates for good and poor language outcome
in autism. Neuron 2015; 86: 567–577.

92 Subbaraju V, Sundaram S, Narasimham S, Suresh MB. Accurate detection of aut-
ism spectrum disorder from structural MRI using extended metacognitive radial
basis function network. Exp Syst Appl 2015; 42: 8775–8790.

93 Abraham A, Milham MP, Di Martino A, Craddock RC, Samaras D, Thirion B et al.
Deriving reproducible biomarkers from multi-site resting-state data: an autism-
based example. Neuroimage 2017; 147: 736–745.

70 Murdaugh DL, Shinkareva SV, Deshpande HR, Wang J, Pennick MR, Kana RK.
Differential deactivation during mentalizing and classiﬁcation of autism based on
default mode network connectivity. PLoS ONE 2012; 7: e50064.

94 Wang L, Wee CY, Tang X, Yap PT, Shen D. Multi-task feature selection via
supervised canonical graph matching for diagnosis of autism spectrum disorder.
Brain Imaging Behav 2016; 10: 33–40.

71 Garrity AG, Pearlson GD, McKiernan K, Lloyd D, Kiehl KA, Calhoun VD. Aberrant
"default mode" functional connectivity in schizophrenia. Am J Psychiatry 2007;
164: 450–457.

95 Igual L, Soliva JC, Escalera S, Gimeno R, Vilarroya O, Radeva P. Automatic brain
caudate nuclei segmentation and classiﬁcation in diagnostic of attention-deﬁcit/
hyperactivity disorder. Comput Med Imaging Graph 2012; 36: 591–600.

72 Spencer MD, Holt RJ, Chura LR, Suckling J, Calder AJ, Bullmore ET et al. A novel
functional brain imaging endophenotype of autism: the neural response to facial
expression of emotion. Transl Psychiatry 2011; 1: e19.

73 Kaiser MD, Hudac CM, Shultz S, Lee SM, Cheung C, Berken AM et al. Neural

signatures of autism. Proc Natl Acad Sci USA 2010; 107: 21223–21228.

74 Plitt M, Barnes KA, Martin A. Functional connectivity classiﬁcation of autism
identiﬁes highly predictive brain features but falls short of biomarker standards.
NeuroImage Clin 2015; 7: 359–366.

75 Pierce K. Early functional brain development in autism and the promise of

sleep fMRI. Brain Res 2011; 1380: 162–174.

76 Akshoomoff N, Lord C, Lincoln AJ, Courchesne RY, Carper RA, Townsend J et al.
Outcome classiﬁcation of preschool children with autism spectrum disorders using
MRI brain measures. J Am Acad Child Adolesc Psychiatry 2004; 43: 349–357.

77 Neeley ES, Bigler ED, Krasny L, Ozonoff S, McMahon W, Lainhart JE. Quantitative
temporal lobe differences: autism distinguished from controls using classiﬁcation
and regression tree analysis. Brain Dev 2007; 29: 389–399.

78 Singh V, Mukherjee L, Chung MK. Cortical surface thickness as a classiﬁer:
boosting for autism classiﬁcation. Med Image Comput Comput Assist Interv 2008;
11(Pt 1): 999–1007.

79 Ecker C, Marquand A, Mourao-Miranda J, Johnston P, Daly EM, Brammer MJ et al.
Describing the brain in autism in ﬁve dimensions—magnetic resonance
imaging-assisted diagnosis of autism spectrum disorder using a multiparameter
classiﬁcation approach. J Neurosci 2010a; 30: 10612–10623.

96 Sato JR, Hoexter MQ, Fujita A, Rohde LA. Evaluation of pattern recognition and
feature extraction methods in ADHD prediction. Front Syst Neurosci 2012; 6: 68.
97 Sidhu GS, Asgarian N, Greiner R, Brown MR. Kernel principal component analysis
for dimensionality reduction in fMRI-based diagnosis of ADHD. Front Syst Neurosci
2012; 6: 74.

98 Wang X, Jiao Y, Tang T, Wang H, Lu Z. Altered regional homogeneity patterns in
adults with attention-deﬁcit hyperactivity disorder. Eur J Radiol 2013; 82:
1552–1557.

99 Xiao C, Bledsoe J, Wang S, Chaovalitwongse WA, Mehta S, Semrud-Clikeman M
et al. An integrated feature ranking and selection framework for ADHD char-
acterization. Brain Inform 2016; 3: 145–155.

This work is licensed under a Creative Commons Attribution-
NonCommercial-NoDerivs 4.0 International License. The images or
other third party material in this article are included in the article’s Creative Commons
license, unless indicated otherwise in the credit line; if the material is not included under
the Creative Commons license, users will need to obtain permission from the license
holder to reproduce the material. To view a copy of this license, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/

© The Author(s) 2017

Translational Psychiatry (2017), 1 – 12
