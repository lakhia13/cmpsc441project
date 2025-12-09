# Liew_2019_Use of Negative Control Exposure Analysis to Evaluate Confounding An Example of Acetaminophen Exposure and Attention-Deficit Hyperactivity Disorder in Nurses' Health Stud

American Journal of Epidemiology
© The Author(s) 2019. Published by Oxford University Press on behalf of the Johns Hopkins Bloomberg School of
Public Health. All rights reserved. For permissions, please e-mail: journals.permissions@oup.com.

Vol. 188, No. 4
DOI: 10.1093/aje/kwy288
Advance Access publication:
February 14, 2019

Practice of Epidemiology

Use of Negative Control Exposure Analysis to Evaluate Confounding: An Example
of Acetaminophen Exposure and Attention-Deﬁcit/Hyperactivity Disorder in
Nurses’ Health Study II

Zeyan Liew*, Marianthi-Anna Kioumourtzoglou, Andrea L. Roberts, Éilis J. O’Reilly,
Alberto Ascherio, and Marc G. Weisskopf

* Correspondence to Dr. Zeyan Liew, Department of Environmental Health Sciences, Yale School of Public Health, 60 College
Street, New Haven, CT 06510 (e-mail: zeyan.liew@yale.edu).

Initially submitted July 24, 2018; accepted for publication December 12, 2018.

Frequent maternal use of acetaminophen in pregnancy has been linked to attention-deﬁcit/hyperactivity disorder
(ADHD) in children, but concerns regarding uncontrolled confounding remain. In this article, we illustrate use of the
negative control exposure (NCE) approach to evaluate uncontrolled confounding bias in observational studies on
pregnancy drug safety and explain the causal assumptions behind the method. We conducted an NCE analysis
and evaluated the associations between maternal acetaminophen use during different exposure periods and
ADHD among 8,856 children born in 1993–2005 to women enrolled in the Nurses’ Health Study II cohort. Informa-
tion on regular maternal acetaminophen use was collected prospectively in biennial questionnaires. A total of 721
children (8.1%) in the cohort had been diagnosed with ADHD as reported by the mothers. Our NCE analysis sug-
gested that only acetaminophen use at the time of pregnancy was associated with childhood ADHD (odds ratio =
1.34, 95% conﬁdence interval: 1.05, 1.72), and the effect estimates for the 2 NCE periods (about 4 years before
and 4 years after the pregnancy) were null. Our ﬁndings corroborate those of prior reports suggesting that prenatal
acetaminophen exposure may inﬂuence neurodevelopment. The lack of an association between acetaminophen
use in the pre- and postpregnancy exposure periods and ADHD provides assurance that uncontrolled time-
invariant factors do not explain this association.
acetaminophen; attention-deﬁcit/hyperactivity disorder; negative control exposure analysis; neurological
development; pregnancy; prenatal exposure delayed effects; uncontrolled confounding

Abbreviations: ADHD, attention-deﬁcit/hyperactivity disorder; NCE, negative control exposure; NHS II, Nurses’ Health Study II.

Observational studies are useful for drug safety research,
especially when it comes to evaluation of the safety of medi-
cation use during pregnancy (1, 2). Some adverse effects of
medication exposure on the offspring might be hidden from
clinical detection until years after the exposure occurs (3). Con-
founding, however, is a major threat to the validity of ﬁndings
from observational data (4). Newer analytical methods such as
marginal structural models and propensity score calibrations
have been proposed for control of complex confounding (5, 6),
but these methods do not address unmeasured or unknown con-
founding factors. Depending on data structure and availability,
some novel study designs or approaches, such as sibling-controlled
analysis (7), case-crossover and case-time-control designs (8),

and negative control exposures (NCEs) or outcomes (9),
have been utilized to evaluate the inﬂuence of uncontrolled
confounding.

Recently, several reports based on large European birth co-
horts suggested a positive association between frequent acet-
aminophen use during pregnancy and neurobehavioral deﬁcits
in offspring, particularly hyperactivity and conduct disorders
(10–16). Acetaminophen (or paracetamol) is an over-the-counter
medication commonly used to treat pain and fever in pregnancy.
Most previous studies were able to control for maternal fever
and infections in pregnancy that are also suspected to affect
neurological development (17, 18), but possible inﬂuences of
unmeasured factors, such as maternal genetics, illnesses, and

768

Am J Epidemiol. 2019;188(4):768–775

familial and social factors, in the ﬁndings are difﬁcult to address.
In this article, we introduce NCE analysis as a useful approach
with which to evaluate uncontrolled confounding bias in obser-
vational research on pregnancy drug safety. We then demon-
strate NCE analysis using an example from Nurses’ Health Study
II (NHS II)—a large, US-wide cohort study with longitudinally
collected data—and investigate the association between regu-
lar maternal use of acetaminophen and attention-deﬁcit/hyper-
activity disorder (ADHD) in offspring.

METHODS

The Partners Human Research Committee (Partners Health-
Care, Boston, Massachusetts) approved this research and deter-
mined that completion and return of the questionnaires constituted
implied consent.

Causal assumptions of NCE analysis

The use of negative controls to detect suspected and unsus-
pected threats to causal inference from confounding in obser-
vational epidemiology studies have been introduced and discussed
(9, 19–21). In NCE analysis, the effect estimates from vari-
able(s) that do not causally affect the outcome but share a similar
confounding structure with the exposure variable of interest are
evaluated. As illustrated in Figure 1, the basic principle relies on
an NCE variable (N) that does not cause the outcome D (depicted
as no arrow from N to D) but shares the same unmeasured
variables (U) that could potentially introduce confounding to
the exposure (E)-outcome (D) relationship of interest. Such N
variables are referred to as “U-comparable” to E. The variables
C represent variables that can confound either the E-D relation-
ship or the N-D relationship, but these factors are measured and
can be controlled in analyses. In the ﬁgure, the exposure E is
drawn as affecting the outcome D, but this is the unknown rela-
tionship under investigation and so in reality may not be pres-
ent. Because N does not affect D directly, if we ﬁnd an association
between N and D after controlling for C and E, this would then be
evidence that U variables may exist and therefore might also
introduce confounding to the E-D association. In contrast, if

N

[C]

U

E

D

Figure 1. Directed acyclic graph illustrating the basic principles of
negative control exposure analysis. E and D are the exposure and
outcome of interest, respectively. The directed acyclic graph is drawn
under the assumption of a true causal association between E and D,
although there may not be one (this is the question being studied). C
represents a set of measured and controlled confounding variables,
and U represents a set of unknown or unmeasured confounding vari-
ables. The brackets around C suggest that the variable(s) is/are con-
trolled. N is the “negative control” variable.

Am J Epidemiol. 2019;188(4):768–775

NCE Analysis of Acetaminophen and ADHD 769

analyses show no association between N and D, this suggests
that the U variables are not introducing confounding to the N-
D association and therefore are also not confounding the E-D
association.

Some examples of studies that have utilized NCE analysis
to evaluate associations between pregnancy exposure and child
neurodevelopment include studies that have used paternal be-
haviors or exposures in pregnancy as NCEs for maternal beha-
viors or exposures in pregnancy (22, 23) and studies that have
examined exposures before, during, or after pregnancy or ex-
posures in different gestational periods if a critical or sensitive
period of exposure effects is known or assumed (13, 15, 24–27).

Acetaminophen exposure and ADHD in NHS II

NHS II is a longitudinal cohort study of 116,430 female nurses
who were recruited in 1989 at 25–42 years of age, were followed
up biennially every odd calendar year, and are now living in all
US states and territories. Questionnaires are mailed midyear,
and most nurses have returned them before the end of that year.
In the NHS II questionnaires, nurse mothers were asked to report
whether they had used acetaminophen (e.g., Tylenol (Johnson &
Johnson, New Brunswick, New Jersey)) regularly (deﬁned as
≥2 times/week in the 1989 and 1993 questionnaires and ≥1
day/week from 1995 onwards) during the previous 2 years.
Regular maternal acetaminophen use (yes/no) reported on the
questionnaire during the year of the child’s birth was analyzed
as the index exposure variable of interest. We refer to this reg-
ular acetaminophen use as use “at the time of pregnancy.”
Although this question was not about use speciﬁcally during
pregnancy, we considered regular use, which would be more likely
than occasional use to continue through pregnancy, particu-
larly since there was no recommendation against acetamino-
phen use during pregnancy in the study periods.

Importantly, because these data were collected prospectively,
any error in capturing use speciﬁcally during pregnancy should
have been nondifferential and therefore should have introduced
random errors. However, as a sensitivity analysis, in order to
reduce pregnancy-speciﬁc exposure misclassiﬁcation, we also
conducted analyses restricted to the subset of women who re-
ported that they were pregnant when responding to the ques-
tionnaire. For the NCEs, we considered the same maternal regular
use variables from the questionnaires completed 2 cycles (i.e.,
4 years) before and after the one completed at the time of preg-
nancy (the 1991 questionnaire did not ask about acetamino-
phen use; therefore, 1989 use was used as the prepregnancy
NCE for births that took place in 1995). These exposure peri-
ods make good NCE variables because we assume that they
do not affect the offspring’s risks of ADHD in a pregnancy 4
years before or later and that time-invariant variables that could
have introduced confounding in other studies—such as genetic
factors, maternal chronic illnesses, family and social factors,
and/or general medication use behaviors and choices—would
affect these other exposure periods in the same way as they would
during the pregnancy.

On the 2013 questionnaire, nurse mothers were asked, “Have
any of your biological children been diagnosed with attention-
deﬁcit/hyperactivity disorder (ADHD)?” and the year of birth of
any child diagnosed with ADHD. Maternal reports of ADHD
have been found to be reliable (28). In a previous small validation

770 Liew et al.

study, Gao et al. (29) found that 92 children reported as having
ADHD in NHS II also scored high on ADHD Rating Scale-IV
(30), which is an 18-item questionnaire assessing the 2 Diag-
nostic and Statistical Manual of Mental Disorders, Fourth Edi-
tion, Text Revision (31), factors comprising ADHD, including
inattention and hyperactivity-impulsivity. All girls scored above
90%, and 81.1% of boys scored above 80%; 63.8% of boys
scored above 90% (29).

In our main analyses, we included singleton children born
during the years in which the questionnaires were mailed in
order to increase the chance that the acetaminophen reporting
included the pregnancy period. We restricted this to the years
1993 through 2005 (i.e., 1993, 1995, 1997, 1999, 2001, 2003,
and 2005) to have NCE periods both 4 years before and 4
years after all pregnancies and so that all children would be at
least 8 years old when ADHD in children was queried about
in 2013. Multiple births were not included because in these
cases, if the mother reported a child with ADHD, she was not
asked to report whether 1 or more than 1 of the children had
ADHD. These analyses included 8,856 children (see Web
Figure 1, available at https://academic.oup.com/aje, for subject
selection), and the sensitivity analyses carried out among those
nurse mothers who indicated that they were pregnant when
answering the questionnaire (the “pregnancy subset”) included
3,716 children.

Statistical analysis

We used generalized linear models to estimate odds ratios
and 95% conﬁdence intervals for ADHD. Generalized estimat-
ing equations were used to account for potentially correlated
outcomes among children born to the same nurses. We adjusted
analyses for time-varying variables that could possibly intro-
duce confounding, including maternal age at the child’s birth
(<30, 30–34, 35–40, or >40 years), child’s birth order (ﬁrst,
second, third, or fourth or later), child’s birth year (continuous),
maternal gestational diabetes (yes/no), preeclampsia (yes/no),
and self-reported regular maternal use of aspirin or aspirin-
containing medication (Anacin (Pﬁzer Inc., New York, New
York), Bufferin (Novartis Consumer Health, Inc., Parsippany,
New Jersey), Alka-Selzer (Bayer Healthcare LLC, Morristown,
New Jersey), etc.) or other nonsteroidal antiinﬂammatory drugs
(ibuprofen, Advil (Wyeth Consumer HealthCare, Richmond,
Virginia, and other companies), Midol (Bayer Healthcare),
Aleve (Bayer Healthcare and other companies), Naprosyn
(Genentech, Inc., South San Francisco, California; and Hoffman-
La Roche, Basel, Switzerland), Relafen (Glaxo SmithKline
Pharmaceuticals, Memphis, Tennessee), ketoprofen, Anaprox
(Genentech, Hoffman-La Roche, and other companies), etc.).
Information regarding use of aspirin and other nonsteroidal
antiinﬂammatory drugs was collected in a manner similar to
that described above for acetaminophen.

The estimates for maternal acetaminophen use before and
after pregnancy (the negative control periods) might be con-
founded by exposure during pregnancy, which is hypothesized
as the critical window of exposure, and acetaminophen use
during that time is correlated with use during the time periods
before and after pregnancy. Therefore, we estimated the asso-
ciations with exposure in each period alone and additionally

ﬁtted a model that included acetaminophen use in all exposure
periods together.

We conducted sex-stratiﬁed analyses to evaluate potential
effect modiﬁcation by child’s sex (14). In sensitivity analyses,
we also performed analyses restricted to nurses who had never
been diagnosed with depression, rheumatoid arthritis, or migraine
headache, as these conditions might increase use of acetamin-
ophen and, separately, be related to ADHD in the child. We
also performed analyses that adjusted for maternal social fac-
tors, including nurses’ self-reported household income, sub-
jective social standing in the community (32), and education
of the husband/partner, as well as lifestyle factors such as mater-
nal smoking (yes/no) and alcohol drinking (yes/no) during each
pregnancy, which was reported on a separate questionnaire
(33), with information provided by approximately 75% of the
nurses. Lastly, on the 2005 questionnaire, nurses were also
asked whether they had any children diagnosed with ADHD,
but the speciﬁc child(ren) were not identiﬁed. To improve
precision in ADHD diagnosis, we conducted additional analy-
ses using births taking place during 1993–1999 but excluded
ADHD cases that were reported on either the 2005 question-
naire or the 2013 questionnaire but not on both. All analyses
were conducted using SAS 9.4 (SAS Institute, Inc., Cary, North
Carolina).

RESULTS

The demographic characteristics of the study sample are pre-
sented in Table 1 by acetaminophen use. Approximately 14%
of nurse mothers reported using acetaminophen regularly at
the time of the pregnancy. Approximately 8% children in the
cohort had ADHD. The demographic characteristics of chil-
dren with and without ADHD are presented in Table 2.

Regular maternal acetaminophen use during the 3 deﬁned
exposure periods was moderately correlated (Spearman’s r =
0.28–0.32). In models with acetaminophen use in all expo-
sure periods included together, we found that only maternal
acetaminophen use at the time of pregnancy was associated
with elevated odds of ADHD in offspring (odds ratio = 1.34,
95% conﬁdence interval: 1.05, 1.72) (Table 3). The associa-
tions were null for maternal acetaminophen use in the pre- or
postpregnancy periods (Table 3). In the pregnancy subset, the
association with use in the pregnancy period was somewhat
larger (odds ratio = 1.46, 95% conﬁdence interval: 1.01, 2.09),
while use in the other periods remained null (Table 3). The
effect estimates were less precise in sex-stratiﬁed analyses, and
we did not ﬁnd strong evidence to suggest effect measure mod-
iﬁcation by child’s sex (Web Table 1).

Our main results were not materially different in any of the
sensitivity analyses. The positive association between acet-
aminophen use at the time of pregnancy but not in the other
exposure periods and ADHD in offspring remained largely
unchanged in analyses restricted to mothers with no depres-
sion, rheumatoid arthritis, or migraine headache (Web Table 2)
and in analyses excluding mothers who used aspirin and other
nonsteroidal antiinﬂammatory drugs at the time of the preg-
nancy (Web Table 3). The estimates became less precise but
the magnitude of associations also did not change in analysis
of a subset of data in which we further adjusted for maternal

Am J Epidemiol. 2019;188(4):768–775

NCE Analysis of Acetaminophen and ADHD 771

Table 1. Selected Demographic Characteristics (%) of Mothers According to Acetaminophen Use During
Pregnancy in an Analysis of Attention-Deﬁcit/Hyperactivity Disorder in Offspring, Nurses’ Health Study II, 1993–2005

Characteristic

Main Analysis (n = 8,856)

Pregnancy Subset (n = 3,716)

Yes (n = 1,230)

No (n = 7,626)

Yes (n = 513)

No (n = 3,203)

Acetaminophen Use at Time of Pregnancy (Yes/No)

Maternal age at child’s birth, years

<30
30–34
35–40
>40

Child’s birth order

1

2

3
≥4

Pregnancy complications

Gestational diabetes

Preeclampsia

Maternal use of acetaminophen

Before pregnancy

After pregnancy

Maternal medication use at time of pregnancy

Aspirin

Other NSAIDs

Maternal diagnosis of chronic illness

Rheumatoid arthritis

Depression

Migraine

Maternal lifestyle during pregnancya

Cigarette smoking

Alcohol drinking

Annual household incomea

<$50,000
$50,000–$100,000
>$100,000

1.7

28.3

50.2

19.8

23.4

38.0

24.7

13.9

5.9

4.2

41.8

51.0

6.7

37.9

3.2

25.2

29.8

7.1

8.0

15.4

25.3

59.3

2.8

39.0

43.2

15.0

24.8

38.3

24.8

12.2

5.1

2.8

12.2

18.1

2.1

5.2

1.6

16.0

13.6

4.4

6.5

12.6

24.1

63.4

2.3

29.0

47.8

20.9

25.7

33.3

26.1

14.8

7.2

3.9

45.2

52.4

5.3

31.6

3.5

26.1

31.2

7.9

8.7

15.0

28.9

56.1

2.9

40.2

43.9

13.0

25.7

37.4

24.5

12.4

5.6

2.6

11.3

18.1

2.6

3.0

1.4

15.6

12.9

4.2

6.5

12.7

24.0

63.3

Abbreviation: NSAIDs, nonsteroidal antiinﬂammatory drugs.
a Information on these factors was available for approximately 75% of the participants.

social demographic and lifestyle factors (Web Table 4). The
effect estimates were slightly strengthened when we included
the ADHD cases reported on both the 2005 and 2009 ques-
tionnaires (Web Table 5).

DISCUSSION

We found an association between maternal use of acetamin-
ophen at the time of pregnancy and risk of ADHD diagnosis
in offspring using acetaminophen use a few years before preg-
nancy and a few years after pregnancy as NCEs to test for residual
confounding by time-invariant factors. The correlation between

Am J Epidemiol. 2019;188(4):768–775

acetaminophen use in the different time periods was modest,
which suggests only modest U→E and U→N correlations
(Figure 1) that are a ﬁrst indication that confounding by time-
invariant factors is probably weak (since a weak U→E corre-
lation would contribute to weaker E←U→D confounding).
However, the absences of associations with acetaminophen
use in the prepregnancy and postpregnancy periods are the true
NCE tests (9, 21), and they suggest that variables that do not
vary over a few years—such as genetics, maternal chronic dis-
eases, or socioeconomic status—do not explain the association
observed for acetaminophen exposure at the time of pregnancy.
This is because such time-invariant variables would result in
U-comparability between acetaminophen use in pregnancy

772 Liew et al.

Table 2. Selected Demographic Characteristics of Offspring With and Without Attention-Deﬁcit/Hyperactivity
Disorder (n = 8,856), Nurses’ Health Study II, 1993–2005

Characteristic

Yes (n = 721)

No (n = 8,135)

No. of Children

%

No. of Children

%

ADHD Diagnosis

Maternal age at child’s birth, years

<30
30–34
35–40
>40

Child’s birth order

1

2

3
≥4

Pregnancy complications

Gestational diabetes

Preeclampsia

Maternal medication use at time of pregnancy

Aspirin

Other NSAIDs

Maternal diagnosis of chronic illness

Rheumatoid arthritis

Depression

Migraine

Maternal lifestyle during pregnancya

Cigarette smoking

Alcohol drinking

Annual household incomea

<$50,000
$50,000–$100,000
>$100,000

21

268

324

108

209

289

170

53

42

27

24

83

16

201

145

23

41

63

133

374

2.9

37.2

44.9

15.0

29.0

40.1

23.6

7.4

5.8

3.7

3.3

11.5

2.2

27.9

20.1

4.3

7.7

11.1

23.3

65.6

214

3,052

3,587

1,282

1,967

3,096

2,026

1,046

421

236

216

780

143

1,326

1,258

290

401

803

1,482

3,797

2.6

37.5

44.1

15.8

24.2

38.1

24.9

12.9

5.2

2.9

2.7

9.6

1.8

16.3

15.5

4.8

6.6

13.2

24.4

62.4

Abbreviations: ADHD, attention-deﬁcit/hyperactivity disorder; NSAIDs, nonsteroidal antiinﬂammatory drugs.
a Information on these factors was available for approximately 75% of the participants.

and use before and after pregnancy. That is, U→E and U→N
are the same, so the confounding paths N←U→D and E←U→D
would be the same. Thus, not ﬁnding an N→D association
implies that N←U→D is not present, and therefore neither is
E←U→D. Our ﬁndings in this large US cohort are also con-
sistent with the few prior European cohort studies suggesting
that in utero exposure to acetaminophen might affect neuro-
development (10–16).

In contrast to time-invariant variables, our NCE analyses
do not inform possible time-varying confounding that might
differ for the different exposure periods used. This does not
have to be the case in NCE analyses, but it is in the current study
because we assessed exposures during different time periods as
NCEs. We therefore adjusted for several time-varying variables
that might have introduced confounding, such as lifestyle fac-
tors and use of other pain and fever medications during the

pregnancy period. However, we cannot rule out the possibil-
ity of other uncontrolled risk factors for ADHD that are uniquely
correlated with the use of acetaminophen during the pregnancy
period. One possible candidate could be conditions like fever,
infections, or mild pain. However, such conditions should have
led to sporadic use of acetaminophen, if any; our exposure vari-
able was regular use of acetaminophen. Thus, confounding from
this source would seem less likely.

Another important consideration in NCE analysis is expo-
sure measurement error. For a null ﬁnding for the NCEs to imply
an absence of unmeasured confounding, the NCEs must be mea-
sured at least as accurately as the exposure of interest. Otherwise,
larger errors in the measures of the NCEs could possibly account
for an absence of association with the NCEs but not the exposure
of interest. In our study setting, the question on regular acetamin-
ophen use was phrased slightly differently in the 1989 and 1993

Am J Epidemiol. 2019;188(4):768–775

,
I
I
y
d
u
S
h

t

t
l

a
e
H

’

s
e
s
r
u
N

,
s
d
o
i
r
e
P
e
r
u
s
o
p
x
E

t

n
e
r
e

f
f
i

D
g
n
i
r
u
D
n
e
h
p
o
n
m
a
e
c
A

t

i

f

o
e
s
U

l

a
n
r
e
a
M

t

l

r
a
u
g
e
R
o

t

i

g
n
d
r
o
c
c
A
g
n
i
r
p
s
f
f

O
n

i

i

r
e
d
r
o
s
D
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
H

/
t
i
c
ﬁ
e
D
-
n
o

i
t

n
e

t
t

A

r
o

f
s
o

i
t

a
R
s
d
d
O

.

l

3
e
b
a
T

I

C
%
5
9

t

n
e
r
e
e
R

f

9
0
2

.

,

1
0
1

.

t

n
e
r
e
e
R

f

0
5
1

.

,

8
7
0

.

t

n
e
r
e
e
R

f

1
1
1

.

,

0
6
0

.

d
e
t
s
u
d
A

j

b
2
R
O

0
0
1

.

6
4
1

.

0
0
1

.

8
0
1

.

0
0
1

.

2
8
0

.

I

C
%
5
9

t

n
e
r
e
e
R

f

5
9
1

.

,

9
9
0

.

t

n
e
r
e
e
R

f

3
5
1

.

,

2
8
0

.

t

n
e
r
e
e
R

f

0
2
1

.

,

9
6
0

.

d
e
t
s
u
d
A

j

a
1
R
O

0
0
1

.

9
3
1

.

0
0
1

.

2
1
1

.

0
0
1

.

1
9
0

.

f
o

.

o
N

s
e
s
a
C

6
6
2

7
5

6
6
2

7
5

3
5
2

0
7

,

)
6
1
7
3
=
n
(

t
e
s
b
u
S
y
c
n
a
n
g
e
r
P

f
o

.

o
N

n
e
r
d

l
i

h
C

3
1
5

3
0
2
3

,

3
9
5

3
2
1
3

,

9
4
8

7
6
8
2

,

I

C
%
5
9

t

n
e
r
e
e
R

f

2
7
1

.

,

5
0
1

.

t

n
e
r
e
e
R

f

2
3
1

.

,

5
8
0

.

t

n
e
r
e
e
R

f

8
1
1

.

,

0
8
0

.

d
e
t
s
u
d
A

j

b
2
R
O

0
0
1

.

4
3
1

.

0
0
1

.

6
0
1

.

0
0
1

.

7
9
0

.

I

C
%
5
9

t

n
e
r
e
e
R

f

1
7
1

.

,

7
0
1

.

t

n
e
r
e
e
R

f

8
3
1

.

,

1
9
0

.

t

n
e
r
e
e
R

f

6
2
1

.

,

8
8
0

.

d
e
t
s
u
d
A

j

a
1
R
O

0
0
1

.

5
3
1

.

0
0
1

.

2
1
1

.

0
0
1

.

5
0
1

.

f
o

.

o
N

s
e
s
a
C

6
9
5

5
2
1

8
8
5

3
3
1

8
4
5

3
7
1

,

)
6
5
8
8
=
n
(
s
s
y
a
n
A
n
a
M

i

i

l

f
o

.

o
N

n
e
r
d

l
i

h
C

6
2
6
7

,

0
3
2
1

,

0
1
4
7

,

6
4
4
1

,

9
4
8
6

,

7
0
0
2

,

e
s
U
n
e
h
p
o
n
m
a
t
e
c
A

i

l

r
a
u
g
e
5 R
0
0
2
–
3
9
9
1

y
c
n
a
n
g
e
r
p

f

o
e
m

i
t

t

A

c
y
c
n
a
n
g
e
r
p
e
r
o
e
B

f

d
e
s
o
p
x
e
n
U

d
e
s
o
p
x
E

d
y
c
n
a
n
g
e
r
p
r
e

t
f

A

d
e
s
o
p
x
e
n
U

d
e
s
o
p
x
E

d
e
s
o
p
x
e
n
U

d
e
s
o
p
x
E

Am J Epidemiol. 2019;188(4):768–775

NCE Analysis of Acetaminophen and ADHD 773

questionnaires, which might have contributed to some exposure
misclassiﬁcation, especially for the prepregnancy exposure var-
iable, but the postnatal exposure variables were not affected
because the ﬁrst postpregnancy exposure year was 1997. More-
over, it is expected that mothers might have underreported their
over-the-counter medication use in general (34, 35). Any mea-
surement error due to ﬂawed recall of medication use was ex-
pected to be similar in the different study periods, since the
exposure data were collected prospectively before the outcome.
Thus, the ﬁnding of an association speciﬁc to exposure around
the time of pregnancy suggests that maternal reporting bias on
medication use is unlikely to explain the ﬁnding.

Strengths of our NCE analysis included the fact that the infor-
mation on acetaminophen use was prospectively collected in
a large cohort study of nurse mothers and their children across
the United States, and the medical information reported by the
nurses in NHS II is expected to have greater accuracy com-
pared with general population cohorts because the participants
are all medically trained. NHS II has a retention rate greater
than 90% for more than 20 years of follow-up, limiting any
possible inﬂuence of selection bias. Moreover, the wealth of
prospectively collected data in NHS II allowed us to adjust for
many potentially confounding factors in the NCE analyses.
The ﬁndings were also robust in several subgroup and sensi-
tivity analyses we conducted.

There were several important limitations of our study. First,
as mentioned above, although several measured confounders
were accounted for in the analyses, we cannot rule out the pos-
sibility of residual confounding by another unaccounted-for time-
varying factor that is speciﬁc to the pregnancy period. Second,
we did not have detailed information regarding the exact timing
of acetaminophen use or on the frequency and dosage. How-
ever, previous studies have found that the prevalence of acet-
aminophen use is stable across pregnancy trimesters (2, 36).
Thus, we expect that the nurse mothers who indicated regu-
lar acetaminophen use in the questionnaires would likely have
taken acetaminophen during pregnancy, particularly since dur-
ing our study period acetaminophen was largely considered safe
and its use during pregnancy was not contraindicated. Thus,
potential misclassiﬁcation of exposure is likely to have been
nondifferential, which typically leads to underestimation of the
true effect size (37, 38). The NHS II questionnaires only asked
about regular acetaminophen use, and there was no additional
information with which to explore dose-response relationships.
We did not have data with which to evaluate possible con-
founding by prescription medication use in pregnancy. How-
ever, use of prescribed pain medications such as triptans and
opioids was rare (<0.6% in the ﬁrst trimester) among preg-
nant women during the study period and thus less likely to
have confounded the results observed for acetaminophen, for
which the exposure prevalence was much higher (1, 2). Lastly,
ADHD diagnoses were self-reported by the nurse mothers
without clinical veriﬁcation. However, maternal reports of ADHD
have been found to be reliable (28), all of the mothers were
nurses, and the overall ADHD prevalence reported in the study
cohort was comparable to Centers for Disease Control and Pre-
vention estimates (37).

The underlying biological mechanisms that may explain the
increased risk of ADHD with acetaminophen exposure are not
known, but possibilities have been suggested, such as frequent

.

d
e
v
i
r
e
d
s
a
w
e
r
u
s
o
p
x
e
y
c
n
a
n
g
e
r
p
e
h

t

i

h
c
h
w
m
o
r
f

e
n
o
e
h

t

l

f

e
r
o
e
b
s
e
c
y
c
2
d
e
e
p
m
o
c
e
r
i
a
n
n
o

t

l

i
t
s
e
u
q
e
h

t

n
o
d
e
t
r
o
p
e
r
e
s
u
n
e
h
p
o
n
m
a
e
c
a

t

i

.

d
e
v
i
r
e
d
s
a
w
e
r
u
s
o
p
x
e
y
c
n
a
n
g
e
r
p
e
h

t

i

h
c
h
w
m
o
r
f

e
n
o
e
h

t

r
e

t
f

l

t

a
s
e
c
y
c
2
d
e
e
p
m
o
c
e
r
i
a
n
n
o

l

i
t
s
e
u
q
e
h

t

n
o
d
e
t
r
o
p
e
r
e
s
u
n
e
h
p
o
n
m
a
e
c
a

t

i

.
l

e
d
o
m
e
m
a
s
e
h

t

n

i

d
e
d
u
c
n

l

i

s
a
w
s
d
o
i
r
e
p
3

l
l

a
g
n
i
r
u
d
e
s
u
n
e
h
p
o
n
m
a
e
c
a

t

i

,
y

l
l

a
n
o

i
t
i

d
d
a

l

;
s
e
b
a
i
r
a
v
e
v
o
b
a
e
h

t

f

o

l
l

a
r
o

f

d
e
t
s
u
d
A
b

j

l

a
n
r
e
a
M

t

c

l

a
n
r
e
a
M
d

t

.
y
c
n
a
n
g
e
r
p

e
h

t

f

o
e
m

i
t

e
h

t

t

a
s
g
u
r
d
y
r
o
a
m
m
a
ﬂ
n

t

i
i
t

n
a

l

i

a
d
o
r
e
t
s
n
o
n
r
e
h
o
r
o
n
i
r
i
p
s
a

t

f

o
e
s
u

l

a
n
r
e
a
m

t

l

r
a
u
g
e
r
d
n
a

,

i

a
s
p
m
a
c
e
e
r
p

l

t

,
s
e
e
b
a
d

i

l

a
n
o

i
t

a
t
s
e
g

,
r
e
d
r
o
h
t
r
i
b
s
d

’

l
i

h
c
,
r
a
e
y
h
t
r
i
b
s
d

’

l
i

h
c
,

e
g
a

l

a
n
r
e
a
m

t

r
o

f

d
e
t
s
u
d
A
a

j

.

o

i
t

a
r
s
d
d
o

,

R
O

;
l

a
v
r
e
n

t

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
,
I

C

:
s
n
o

i
t

i

a
v
e
r
b
b
A

774 Liew et al.

acetaminophen use in pregnancy affecting maternal-fetal hor-
monal functions (36, 38, 39) or inducing oxidative stress lead-
ing to neuronal death (40, 41). Acetaminophen exposure has
been repeatedly linked to male reproductive outcomes such as
cryptorchidism (24, 42) and reduced anogenital distance (43),
which may be attributable to its endocrine-disrupting effects via
inhibition of androgen or prostaglandin synthesis (36, 38, 39).
Exposure to endocrine disruptors during sensitive periods of
development has been associated with neurobehavioral con-
sequences (44). Future mechanistic studies are needed to
strengthen causal inference for possible effects of acetamino-
phen exposure on neurodevelopmental outcomes.

In conclusion, uncontrolled confounding bias remains a major
challenge in drug safety research using observational data. NCE
analyses can be a useful tool for evaluating whether uncon-
trolled confounding bias contributes to any observed associa-
tion. The success of NCE analyses largely depends on whether
one can ﬁnd negative exposure variable(s) that are expected to
share a similar confounding structure with the index exposure
variable of interest, but the negative exposure variable(s) must
not have a causal effect on the outcome (21). In this example,
the longitudinal data collection waves of NHS II, in which
nurse mothers were repeatedly queried about regular acetamin-
ophen use, provided a unique opportunity allowing the com-
parison of associations with exposures in different time periods.
The ﬁndings of our NCE analyses corroborate those of prior re-
ports suggesting that prenatal acetaminophen exposure may
inﬂuence neurodevelopment (10–17). While several prior stud-
ies based on pregnancy cohort data were better suited to ruling
out potential confounding by time-varying factors speciﬁc to
the pregnancy, using the NHS II data here we obtained further
evidence that this association is also unlikely to be explained
by other time-invariant factors. Future investigations are still
needed, especially studies with improved exposure and outcome
assessment and studies with the ability to address known and
possibly unknown confounding factors in the analyses.

ACKNOWLEDGMENTS

Author afﬁliations: Department of Environmental Health

Sciences, School of Public Health, Yale University, New
Haven, Connecticut (Zeyan Liew); Yale Center for Perinatal,
Pediatric, and Environmental Epidemiology, School of
Public Health, Yale University, New Haven, Connecticut
(Zeyan Liew); Department of Environmental Health
Sciences, Mailman School of Public Health, Columbia
University, New York, New York (Marianthi-Anna
Kioumourtzoglou); Department of Environmental Health,
T.H. Chan School of Public Health, Harvard University,
Boston, Massachusetts (Andrea L. Roberts, Marc G.
Weisskopf); School of Public Health, College of Medicine,
University College Cork, Cork, Ireland (Éilis J. O’Reilly);
Department of Nutrition, T.H. Chan School of Public
Health, Harvard University, Boston, Massachusetts (Éilis J.
O’Reilly, Alberto Ascherio); Channing Division of
Network Medicine, Department of Medicine, Brigham and
Women’s Hospital, Boston, Massachusetts (Alberto
Ascherio); and Department of Epidemiology, T.H. Chan

School of Public Health, Harvard University, Boston,
Massachusetts (Alberto Ascherio, Marc G. Weisskopf).
Nurses’ Health Study II is supported by infrastructure
grant UM1 CA176726 from the National Cancer Institute.
This study was partially supported by the National Institute
of Environmental Health Sciences (NIEHS) (grant P30
ES000002). Z.L. was partly supported by a National
Institutes of Health/NIEHS career development award
(K99ES026729 and R00ES026729), and M.-A.K. was
partially supported by the National Institutes of Health
(training grant T32 ES 007069 and NIEHS center grant P30
ES09089).

The funders played no role in the design and conduct of

the study; the collection, management, analysis, and
interpretation of the data; the preparation, review, and
approval of the manuscript; or the decision to submit the
manuscript for publication.

Conﬂict of interest: none declared.

REFERENCES

1. Mitchell AA, Gilboa SM, Werler MM, et al. Medication use

during pregnancy, with particular focus on prescription drugs:
1976–2008. Am J Obstet Gynecol. 2011;205(1):51.e1–51.e8.

2. Werler MM, Mitchell AA, Hernandez-Diaz S, et al. Use of

over-the-counter medications during pregnancy. Am J Obstet
Gynecol. 2005;193(3):771–777.

3. Savitz DA, Hertz-Picciotto I, Poole C, et al. Epidemiologic

measures of the course and outcome of pregnancy. Epidemiol
Rev. 2002;24(2):91–101.

4. Wood ME, Lapane KL, van Gelder MMHJ, et al. Making fair
comparisons in pregnancy medication safety studies: an
overview of advanced methods for confounding control.
Pharmacoepidemiol Drug Saf. 2018;27(2):140–147.

5. Little RJ, Rubin DB. Causal effects in clinical and

epidemiological studies via potential outcomes: concepts and
analytical approaches. Annu Rev Public Health. 2000;21:
121–145.

6. Robins JM, Hernán MA, Brumback B. Marginal structural

models and causal inference in epidemiology. Epidemiology.
2000;11(5):550–560.

7. Frisell T, Öberg S, Kuja-Halkola R, et al. Sibling comparison
designs: bias from non-shared confounders and measurement
error. Epidemiology. 2012;23(5):713–720.

8. Schneeweiss S, Sturmer T, Maclure M. Case-crossover and

case-time-control designs as alternatives in
pharmacoepidemiologic research. Pharmacoepidemiol Drug
Saf. 1997;6(suppl 3):S51–S59.

9. Lipsitch M, Tchetgen Tchetgen E, Cohen T. Negative controls:
a tool for detecting confounding and bias in observational
studies. Epidemiology. 2010;21(3):383–388.

10. Liew Z, Ritz B, Rebordosa C, et al. Acetaminophen use during

pregnancy, behavioral problems, and hyperkinetic disorders.
JAMA Pediatr. 2014;168(4):313–320.

11. Brandlistuen RE, Ystrom E, Nulman I, et al. Prenatal

paracetamol exposure and child neurodevelopment: a sibling-
controlled cohort study. Int J Epidemiol. 2013;42(6):
1702–1713.

12. Liew Z, Ritz B, Virk J, et al. Maternal use of acetaminophen

during pregnancy and risk of autism spectrum disorders in
childhood: a Danish National Birth Cohort study. Autism Res.
2016;9(9):951–958.

Am J Epidemiol. 2019;188(4):768–775

NCE Analysis of Acetaminophen and ADHD 775

29. Gao XA, Lyall K, Palacios N, et al. RLS in middle aged

women and attention deﬁcit/hyperactivity disorder in their
offspring. Sleep Med. 2011;12(1):89–91.

30. DuPaul GJ, Power TJ, Anastopoulos AD, et al. ADHD Rating
Scale-IV: Checklists, Norms, and Clinical Interpretation. New
York, NY: The Guilford Press; 1998.

31. American Psychiatric Association. Diagnostic and Statistical
Manual of Mental Disorders, Fourth Edition, Text Revision.
Arlington, VA: American Psychiatric Publishing, Inc.; 2000.
32. Singh-Manoux A, Adler NE, Marmot MG. Subjective social

status: its determinants and its association with measures of ill-
health in the Whitehall II study. Soc Sci Med. 2003;56(6):
1321–1333.

33. Roberts AL, Liew Z, Lyall K, et al. Association of maternal
exposure to childhood abuse with elevated risk for attention
deﬁcit hyperactivity disorder in offspring. Am J Epidemiol.
2018;187(9):1896–1906.

34. Olesen C, Sondergaard C, Thrane N, et al. Do pregnant women
report use of dispensed medications? Epidemiology. 2001;
12(5):497–501.

35. van Gelder MMHJ, Vorstenbosch S, te Winkel B, et al. Using
Web-based questionnaires to assess medication use during
pregnancy: a validation study in two prospectively enrolled
cohorts. Am J Epidemiol. 2018;187(2):326–336.
36. Kristensen DM, Mazaud-Guittot S, Gaudriault P, et al.

Analgesic use—prevalence, biomonitoring and endocrine and
reproductive effects. Nat Rev Endocrinol. 2016;12(7):
381–393.

37. Visser SN, Danielson ML, Bitsko RH, et al. Trends in the

parent-report of health care provider-diagnosed and medicated
attention-deﬁcit/hyperactivity disorder: United States,
2003–2011. J Am Acad Child Adolesc Psychiatry. 2014;53(1):
34–46.e2.

38. Albert O, Desdoits-Lethimonier C, Lesné L, et al. Paracetamol,

aspirin and indomethacin display endocrine disrupting
properties in the adult human testis in vitro. Hum Reprod.
2013;28(7):1890–1898.

39. Mazaud-Guittot S, Nicolas Nicolaz C, Desdoits-Lethimonier
C, et al. Paracetamol, aspirin, and indomethacin induce
endocrine disturbances in the human fetal testis capable of
interfering with testicular descent. J Clin Endocrinol Metab.
2013;98(11):E1757–E1767.

40. Nuttall SL, Khan JN, Thorpe GH, et al. The impact of

therapeutic doses of paracetamol on serum total antioxidant
capacity. J Clin Pharm Ther. 2003;28(4):289–294.

41. Posadas I, Santos P, Blanco A, et al. Acetaminophen induces
apoptosis in rat cortical neurons. PLoS One. 2010;5(12):
e15360.

42. Snijder CA, Kortenkamp A, Steegers EA, et al. Intrauterine
exposure to mild analgesics during pregnancy and the
occurrence of cryptorchidism and hypospadia in the offspring:
the Generation R Study. Hum Reprod. 2012;27(4):1191–1201.

43. Lind DV, Main KM, Kyhl HB, et al. Maternal use of mild
analgesics during pregnancy associated with reduced
anogenital distance in sons: a cohort study of 1027 mother-
child pairs. Hum Reprod. 2017;32(1):223–231.

44. Braun JM. Early-life exposure to EDCs: role in childhood
obesity and neurodevelopment. Nat Rev Endocrinol. 2017;
13(3):161–173.

13. Stergiakouli E, Thapar A, Davey Smith G. Association of
acetaminophen use during pregnancy with behavioral
problems in childhood evidence against confounding. JAMA
Pediatr. 2016;170(10):964–970.

14. Avella-Garcia CB, Julvez J, Fortuny J, et al. Acetaminophen
use in pregnancy and neurodevelopment: attention function
and autism spectrum symptoms. Int J Epidemiol. 2016;45(6):
1987–1996.

15. Ystrom E, Gustavson K, Brandlistuen RE, et al. Prenatal

exposure to acetaminophen and risk of ADHD. Pediatrics.
2017;140(5):e20163840.

16. Gervin K, Nordeng H, Ystrom E, et al. Long-term prenatal

exposure to paracetamol is associated with DNA methylation
differences in children diagnosed with ADHD. Clin
Epigenetics. 2017;9:Article 77.

17. Liew Z, Ritz B, Virk J, et al. Prenatal use of acetaminophen and
child IQ: a Danish cohort study. Epidemiology. 2016;27(6):
912–918.

18. Zerbo O, Iosif AM, Walker C, et al. Is maternal inﬂuenza or

fever during pregnancy associated with autism or
developmental delays? Results from the CHARGE
(CHildhood Autism Risks from Genetics and Environment)
study. J Autism Dev Disord. 2013;43(1):25–33.

19. Flanders WD, Klein M, Darrow LA, et al. A method for

detection of residual confounding in time-series and other
observational studies. Epidemiology. 2011;22(1):59–67.
20. Flanders WD, Klein M, Darrow LA, et al. A method to detect

residual confounding in spatial and other observational studies.
Epidemiology. 2011;22(6):823–826.

21. Weisskopf MG, Tchetgen-Tchetgen EJ, Raz R. On the use of
imperfect negative control exposures in epidemiological
studies. Epidemiology. 2016;27(3):365–367.

22. Mikkelsen SH, Hohwü L, Olsen J, et al. Parental body mass
index and behavioral problems in their offspring: a Danish
National Birth Cohort study. Am J Epidemiol. 2017;186(5):
593–602.

23. Zhu JL, Olsen J, Liew Z, et al. Parental smoking during

pregnancy and ADHD in children: the Danish National Birth
Cohort. Pediatrics. 2014;134(2):e382–e388.

24. Jensen MS, Rebordosa C, Thulstrup AM, et al. Maternal use of
acetaminophen, ibuprofen, and acetylsalicylic acid during
pregnancy and risk of cryptorchidism. Epidemiology. 2010;
21(6):779–785.

25. Kalkbrenner AE, Windham GC, Serre ML, et al. Particulate

matter exposure, prenatal and postnatal windows of
susceptibility, and autism spectrum disorders. Epidemiology.
2015;26(1):30–42.

26. Raz R, Levine H, Pinto O, et al. Trafﬁc related air pollution and
autism spectrum disorder: a population based nested case-
control study in Israel. Am J Epidemiol. 2018;187(4):717–725.

27. Raz R, Roberts AL, Lyall K, et al. Autism spectrum disorder
and particulate matter air pollution before, during, and after
pregnancy: a nested case-control analysis within the Nurses’
Health Study II cohort. Environ Health Perspect. 2015;123(3):
264–270.

28. Faraone SV, Biederman J, Milberger S. How reliable are

maternal reports of their children’s psychopathology? One-
year recall of psychiatric diagnoses of ADHD children. J Am
Acad Child Adolesc Psychiatry. 1995;34(8):1001–1008.

Am J Epidemiol. 2019;188(4):768–775
