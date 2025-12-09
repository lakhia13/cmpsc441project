# Dils_2024_The efficacy of cognitive behavioral therapy for mental health and quality of life among individuals diagnosed with cancer A systematic review and meta-analysis.

Received: 9 November 2023 

DOI: 10.1002/cam4.70063  

|  Revised: 12 July 2024 

|  Accepted: 20 July 2024

R E V I E W

The efficacy of cognitive behavioral therapy for mental 
health and quality of life among individuals diagnosed with 
cancer: A systematic review and meta- analysis

Alexander T. Dils1  |   Kathryn O'Keefe1  |   Nada Dakka1  |   Michelle Azar1  |   
Meiyan Chen2  |   Anao Zhang2,3,4

1Central Michigan University College 
of Medicine, Saginaw, Michigan, USA
2The University of Texas at Austin Steve 
Hicks School of Social Work, Austin, 
Texas, USA
3University of Michigan Health, 
Adolescent and Young Adult Oncology 
Program, Ann Arbor, Michigan, USA
4University of Michigan School of 
Social Work, Ann Arbor, Michigan, 
USA

Correspondence
Anao Zhang, University of Michigan 
School of Social Work and University 
of Michigan Health AYA Oncology 
Program, 1080 S University Avenue 
Office, (734) 647–6787, Ann Arbor, MI, 
USA.
Email: zhangan@med.umich.edu

Abstract
Objective: It has long been documented that cognitive behavioral therapy (CBT) 
has positive impacts on improving mental health (MH) and quality of life (QoL) 

in the general population, but investigations on its effect on cancer survivors re-

main limited, especially for QoL outcomes. The purpose of this meta- analysis is 

to investigate the effects of CBT as compared to control on cancer patients' MH 

and QoL outcomes. Control is defined in this study as standard therapy, waitlist 

control, and active/alternative therapy.
Methods: In total, 154 clinical trials creating a sample size of 1627 individuals 
were collected. Analysis focusing on MH and QoL excluded 29 clinical trials re-

sulting in a final analysis of 132 clinical trials (and 1030 effect sizes). R Statistical 

Software  (version  4.2.2)  and  the  robumeta  package  were  utilized  to  complete 

analysis,  which  entailed  robust  variance  estimation  (RVE)  in  intercept- only 

meta- regression, and univariate meta- regression (for moderator analysis).
Results:  Across  132  clinical  trials  and  1030  effect  size  estimates,  we  identified 
that CBT moderately improves MH and QoL in cancer patients d = 0.388, 95% CI 
0.294–0.483,  p < 0.001.  Additionally,  age  and  delivery  format  can  influence  the 
efficacy of CBT in this patient population.
Conclusions:  CBT  statistically  improves  the  MH  and  QoL  psychosocial  pa-
rameters in cancer patients with greater efficacy in younger patients. Important 

clinical and intervention- related factors, that is, age and delivery, should be con-

sidered when oncologists consider CBT as a psychotherapeutic intervention for 

individuals with cancer.

K E Y W O R D S

cancer survivor, cognitive behavioral therapy, meta- analysis, patient- reported outcome, 
supportive care

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided 
the original work is properly cited.
© 2024 The Author(s). Cancer Medicine published by John Wiley & Sons Ltd.

Cancer Medicine. 2024;13:e70063. 
https://doi.org/10.1002/cam4.70063

wileyonlinelibrary.com/journal/cam4

|  1 of 10

  
  
2 of 10 

| 

1 

|  INTRODU CT ION

Cancer is a debilitating disease that affects millions of in-
dividuals  each  year  around  the  globe.  While  treatments 
have  advanced  in  recent  decades  improving  longevity 
and  survival  rates,  treatment  regimens  have  serious  im-
pacts on the physical, psychological, and social well- being 
of oncology patients.1,2 These patients are prone to many 
psychological  and  mental  health  (MH)  disturbances,  in-
cluding  depression,  anxiety,  and  decreased  general  well-
ness,  due  to  these  psychosocial  burdens  associated  with 
cancer treatment.3 This effect can persist after treatment 
has  ended,  and  cohort  studies  report  higher  incidences 
of anxiety and depression in long- term cancer survivors, 
with  symptoms  lasting  for  roughly  2 years  or  more  after 
diagnosis.4 Addressing the issues that pertain to MH and 
general wellness is imperative for the long- term wellbeing 
of these patients. One common and effective intervention 
utilized  in  the  treatment  of  MH  and  general  wellness  is 
cognitive behavioral therapy (CBT).5

CBT has classically been utilized for the treatment of 
many  MH  disorders.  Literature  has  shown  that  CBT  in 
the general population is effective in the treatment of MH 
disorders,  among  them  depression  and  anxiety,  as  well 
as  improvements  in  quality  of  life  (QoL).6  In  a  most  re-
cent  meta- review  of  systematic  reviews  and  panoramic 
meta- analysis by Fordham et al.7 a total of 494 systematic 
reviews  and  meta- analyses  were  identified,  reporting  an 
overall statistically significant and moderate treatment ef-
fect of CBT for QoL outcomes as well as for MH outcomes 
such  as  depression  and/or  anxiety.  In  addition,  CBT  has 
been  shown  to  not  only  adequately  treat  MH  disorders, 
but to reduce relapse and recurrence as well, a feature that 
is  particularly  noteworthy  when  treating  chronic  condi-
tions such as those oncology patients face.8 In fact, studies 
have  shown  that  CBT  use  is  effective  in  cancer  patients 
when  treating  distress  and  pain.9  Besides,  CBT  has  also 
been  shown  to  be  effective  in  the  context  of  insomnia,10 
PTSD,11 fatigue,12 fear,13 anxiety and depression14 in can-
cer  patients.  However,  whether  CBT  is  more  effective 
than standard care in the treatment of combined MH and 
general wellness in cancer patients remains unanswered 
and is an investigation point of this project. While these 
studies  have  shown  CBT  is  effective  in  treating  MH  and 
general  wellness  in  cancer  patients,  they  do  not  address 
which outcome is better benefitted in response to CBT and 
little is known about other factors that may influence the 
efficacy of CBT.

Recent work has illustrated the efficacy of CBT on MH 
in  breast  cancer  patients.15,16  While  these  studies  have 
shed  light  on  the  importance  of  CBT  in  treating  cancer 
patients with MH disorders, they leave gaps in our under-
standing of CBT as an adjunct to treatment. Furthermore, 

there are a limited number of trials included in these re-
cent works, and most were limited to nonmetastatic Stage 
3 breast cancer patients, excluding cases with more wide-
spread aggressive disease.17 Given all that is left to explore, 
we believe an updated analysis is warranted.

Herein, we discuss the effect of CBT on MH and QoL 
and  analyze  two  potential  moderators  of  the  efficacy  of 
CBT  in  patients  in  these  two  aspects  of  care:  age  of  pa-
tients and the treatment delivery of CBT. We focused on 
age  and  treatment  delivery  of  CBT  as  potentially  signif-
icant factors impacting CBT's treatment effect for a cou-
ple  of  reasons.  First,  studies  have  reported  a  differential 
treatment  effect  of  CBT  across  the  age  spectrum.  For 
example,  Zhang  et  al.18  systematically  reviewed  existing 
psychosocial, behavioral, and supportive interventions for 
pediatric,  adolescent  and  young  adult  cancer  survivors. 
Findings  of  the  study  suggested  that  supportive  inter-
ventions, including CBT, were only effective for pediatric 
cancer patients but not for adolescents and young adults 
with  cancer.  Similarly,  Mirosevic  et  al.19  found  a  signifi-
cant treatment effect of CBT on cancer patients' survival 
only among middle-  to older- adult patients but not among 
younger (< 40 years old) patients. Second, with recent ad-
vancement in technology, the delivery of CBT has become 
increasingly  diverse  with  CBT  delivery  formats  ranging 
from in- person to interpersonal CBT via technology (e.g., 
Zoom), or even a mixture of multiple methods. The effi-
cacy of CBT in oncology patients may vary depending on 
delivery method and setting.20,21 Specifically, a systematic 
review and meta- analysis of internet- delivered CBT for de-
pression and anxiety among patients with chronic health 
conditions  revealed  overall  significant  and  moderate 
treatment effect sizes for depression and anxiety, d = 0.31 
and d = 0.45, respectively.22 On one hand, these point es-
timates  seemed  smaller  than  in- person  CBT's  treatment 
effect  for  cancer  patients,  for  example,  d = 0.57  for  QoL 
or  d = 1.10  for  anxiety.23  On  the  other  hand,  in  a  recent 
meta- analysis, Carlbring et al.24 found that internet- based 
CBT  for  psychiatric  and  somatic  disorders  is  equally  ef-
fective  as  in- person  CBT,  indicating  the  need  to  further 
clarify the possible differential treatment effect of CBT for 
cancer  patients'  MH  and  QoL  outcomes  across  different 
delivery  formats.  Performing  this  analysis  is  critical  for 
understanding how to further provide all- encompassing, 
comprehensive  treatment  of  cancer  patients  by  not  only 
addressing the disease, but also the psychosocial compli-
cations associated with treatments.

2 

|   METH ODS

This  study  followed  the  Methodological  Expectations  of 
Cochrane  Intervention  Reviews  (MECIR)  and  reported 

DILS et al. 
 
|  3 of 10

findings in accordance with the Preferred Reporting Items 
for Systematic Review and Meta- Analysis (PRISMA). Our 
team  included  an  interdisciplinary  team  of  medical  stu-
dents, behavioral health therapist, psycho- oncologist, and 
research synthesis expert. We followed the protocol pre- 
registered  at  PROSPERO:  CRD42020200987  but  adopted 
an updated search date from inception to July 2023.

|  Search procedures and inclusion 

2.1 
criteria

We searched all literature from inception to July 2023. We 
searched  for  controlled  trials,  including  both  randomized 
and non- randomized controlled trial studies. We searched 
across 11 electronic databases, 4 professional websites, plus 
a manual search of reference lists from relevant published 
studies.  A  detailed  description  of  the  key  search  words, 

specific databases, and others are outline in Data S1. Two re-
search assistants independent screened all articles based on 
title/abstract, and then full text articles, using the Cochrane 
recommended  systematic  review  platform,  Covidence. 
Any  decision  inconsistency  between  the  two  independent 
screeners was first discussed by the two screeners for con-
sensus  building,  and,  if  unsuccessful,  resolved  by  a  senior 
scholar on the team to make a final vote. A full record of the 
literature search is outlined in Figure 1.

|  Population, intervention, and 

2.2 
outcome measures

We focused on the cancer survivor population, which, ac-
cording to the National Cancer Institute definition, refers to 
an  individual  from  the  time  of  diagnosis  through  the  bal-
ance of life. For intervention consideration, any intervention 

n
o
i
t
a
c
i
f
i
t
n
e
d
I

g
n
i
n
e
e
r
c
S

d
e
d
u
l
c
n
I

Records identified from:
- Databases (n = 2412)
- Existing reviews (n = 229) 
- Grey literature (n = 8)

Records removed before screening:
- Duplication (n = 800)
- Records marked as ineligible by 
automation tools (n = 9) 

Records screened based on 
title and abstract (n = 1840)

Records excluded (n = 1407)

Records screened based on 
full text articles (n = 433)

Records excluded 
- Not CBT (186)
- No control condition (57)

Full text records eligible for 
statistical extraction (n = 
190)

Records excluded due to missing 
statistical information (n = 36)

Number of records included 
in the original dataset (n = 
154)

Records excluded due to not 
focusing on MH or QoL (n = 29)

Number of records included 
in the final analysis (n = 125)

F I G U R E   1  PRISMA 2020 Flow 
diagram for literature search.

DILS et al. 
   
4 of 10 

| 

that was medical or pharmaceutical only were not eligible 
for  inclusion.  With  the  focus  on  CBT,  this  project  consid-
ered traditionally- defined CBT and several important CBT 
variations. This paper adheres to Beck's CBT definition that 
CBT is a structured, present- focused psychotherapeutic ap-
proach that is informed by the cognitive behavioral model, 
and often include the following core components: cognitive 
restructuring, behavioral activation, problem- solving skills, 
and exposure. We considered including third waves of CBT, 
such as acceptance and commitment- based CBT or dialectic 
behavioral therapy. Unfortunately, that would significantly 
expand  the  scope  of  this  review  and  reduce  its  feasibility. 
Specifically, by including keywords representing acceptance 
commitment therapy or dialect behavioral therapy or meta- 
cognitive therapy, our initial screening pool expanded from 
1840  to  28,191,  making  the  scope  too  broad  to  complete 
given our team's resources available. This decision should be 
viewed as a limitation of this paper. However, we decided to 
include mindfulness- based CBT because mindfulness- based 
interventions are very common among cancer survivors and 
should be included as part of the evidence synthesis. Given 
the nature and scope of this project, the primary outcomes 
are cancer survivors' MH and QoL.

2.3 

|  Data extraction

The research team developed a data extraction sheet to ob-
tain key information to facilitate data analysis. In addition 
to  bibliographic  information,  we  also  extracted  study  de-
sign information (e.g., randomization, type of comparison, 
sample size), participant characteristics (e.g., average age, 
%female, %non- Hispanic White) intervention characteris-
tics (e.g., intervention theory, core CBT component, deliv-
ery format, etc.), and other factors (e.g., if supervision was 
provided  or  if  training  was  provided).  We  also  extracted 
necessary statistical information to calculate effect size for 
meta- analysis.

2.4 

|  Risk of bias assessment

Given  the  inclusion  of  both  randomized  controlled  tri-
als  and  non- randomized  controlled  trials,  we  used  the 
Cochrane  Collaboration's  Risk  of  Bias  tool  2nd  version 
(RoB  2)  for  randomized  trials,  and  the  Risk  of  Bias  in 
Non- randomized  Studies  –  of  Interventions  (ROBINS- I) 
tool for non- randomized controlled trials. Both the RoB 2 
and ROBINS- I evaluate key aspect of studies using a con-
trolled  trial  design,  for  example,  bias  due  to  randomiza-
tion, or bias due to selected outcome reporting.

|  Data synthesis and statistical 

2.5 
analysis

We  performed  all  data  analyses  using  the  R  Statistical 
Software.  Specifically,  we  used  the  meta- regression 
analytical  framework  with  robust  variance  estima-
tion (RVE) to facilitate meta- analysis. All our outcome 
measures were standardized mean differences, and we 
calculated the small sample size corrected Hedges' gas 
measures of effect size.25 We chose the meta- regression 
with  RVE  because  it  is  a  method  that  effectively  ad-
dresses  the  issues  of  dependency  among  effect  sizes 
from the same study. Additionally, the meta- regression 
with RVE method is also an advantageous method be-
cause  it  produces  robust  estimation  of  the  variance 
component  regardless  of  the  model  selection,  that  is, 
fixed-  versus random- effects models. Therefore, the se-
lection between a fixed-  versus a random- effects model 
is no longer necessary.

In  addition  to  an  intercept- only  meta- regression 
model to evaluate the overall treatment effect of CBT for 
cancer survivors' MH and QoL outcomes, we conducted 
important  subgroup  analyses  and  univariate  meta- 
regression  moderator  analysis.  We  considered  three 
important  moderators:  (1)  outcome  type,  that  is,  MH 
versus QoL; (2) age, categorized to <40 years old which 
represents pediatric, adolescent and young adult cancer 
survivors,  40–64 years  old  which  represents  the  middle 
aged cancer survivors and ≥65 years old which represents 
older cancer survivors; and (3) delivery format, defined 
as  in- person,  tech- only  interpersonal  where  CBT  deliv-
ered  person  to  person  virtually,  mixed  in- person  and 
tech,  pre- programmed  only  where  CBT  was  delivered 
over a programmed software without a person, and tech- 
only interpersonal and pre- programmed. While we also 
collected other important demographic, clinical, and in-
tervention  related  variables,  we  were  unable  to  include 
many  of  them  due  to  significant  amount  of  missing  to 
allow meaningful analysis.

To evaluate publication bias, plotting of individual ef-
fect size estimates against corresponding standard errors 
was performed using the funnel plot for visual inspection 
(Figure 2).26 Symmetry within the funnel plot is indicative 
of  absent  publication  bias  and  in  contrast  asymmetry  is 
suggestive of publication bias.27 In addition, the publica-
tion  bias  was  further  evaluated  with  sensitivity  analysis 
using  a  priori  weight  functions.  This  method  represents 
an  observed  overall  treatment  effect  and  a  theoretical 
treatment  effect  (assuming  the  funnel  plot  is  symmetri-
cal)  and  evaluates  the  difference  between  the  two  lines/
observations.

DILS et al. 
 
|  5 of 10

21.21%  (n = 28)  to  an  active  control  group,  and  37.88% 
(n = 50)  to  a  waitlist  or  attention  control  group.  Looking 
at  patient  treatment  phase,  of  the  116  trials  document-
ing  this  factor,  41.67%  (n = 55)  had  patients  undergoing 
current curative treatment, 32.76% (n = 38) were in post- 
treatment  survivorship,  12.93%  (n = 15)  were  in  a  mixed 
phase, 4.31% (n = 5) were newly diagnosed without initi-
ated treatment, one study was in end- of- life care, and one 
focused on palliative treatment (including transition from 
curative  to  palliative).  Details  of  individuals  studies  are 
presented in Data S2.

3.2 

|  Risk of bias assessment

The  Revised  Cochrane  Risk- of- Bias  tool  second  ver-
sion  and  the  Non- Randomized  Studies  of  the  Effects  of 
Interventions  (ROBINS- I)  was  used  in  this  review  to  as-
sess  the  risk  of  bias  for  both  randomized  controlled  tri-
als (122/132) and controlled trials without randomization 
(10/132), respectively. In general, studies included in this 
review identified a low risk of bias in selection of the re-
ported  results  (129/132),  appropriate  reporting  in  the 
measurement of the outcome (126/132), deviations from 
the  intended  interventions  (122/132),  and  reporting  of 
missing outcome data (103/132). Besides, 10 randomized 
controlled  trials  reported  moderate  risk  of  bias  arising 
from the randomization process and two non- randomized 
controlled trials indicated moderate risk of bias in the se-
lection of participants into the study. In controlled trials 
without  random  assignment,  one  study  had  a  moderate 
risk of bias due to confounding. Collectively, the included 
studies revealed a low risk of bias (Data S3).

|  Overall meta- analytic and subgroup 

3.2.1 
findings

Across  132  studies  inclusive  of  1030  effect  sizes,  CBT 
reported  an  overall  small  to  moderate  and  statistically 
significant  treatment  effect  size  for  cancer  survivors' 
MH  and  QoL  outcomes,  d = 0.388,  95%  CI  0.294–0.483, 
p < 0.001  (Table  1).  Subgroup  analysis  across  119  stud-
ies and 796 effect sizes revealed an overall moderate and 
statistically  significant  treatment  effect  size  of  CBT  for 
cancer survivors' MH outcomes, d = 0.406, 95% CI 0.299–
0.512,  p < 0.001.  Similarly,  subgroup  analysis  across  63 
studies and 234 effect sizes reported an overall small and 
statistically  significant  treatment  effect  size  of  CBT  for 
cancer survivors' QoL outcomes, d = 0.254, 95% CI 0.14–
0.368, p < 0.001.

Subgroup  analysis  evaluating  CBT's  treatment  effect 
on MH and QoL outcomes by age group revealed that CBT 

F I G U R E   2  Funnel plot for publication bias.

3 

|  RESULT S

3.1 

|  Study characteristics

The  present  meta- analysis  included  132  trials  compris-
ing 1030 effect size estimates and a total sample of 13,226 
participants  undergoing  CBT  intervention  published  be-
tween 1986 and 2023. Among the 129 trials reporting par-
ticipants' age, the average age ranged from 4.2 to 76 years, 
with  a  mean  of  53.38 years.  Regarding  participant  sex, 
78.85%  of  patients  were  female  (n = 10,303)  among  the 
131  trials  reporting  this  demographic.  With  the  excep-
tion of 10 trials, all study utilized a randomized controlled 
trial (RCT) design, while the remaining 10 studies imple-
mented  a  non- randomized  controlled  methodology.  In 
terms  of  treatment  delivery  format,  76  studies  (57.58%) 
utilized  in- person  intervention,  28  studies  (21.21%)  em-
ployed  a  combined  in- person  and  technology- assisted 
approach,  13  studies  (9.85%)  used  pre- programmed 
technology- only  intervention,  12  studies  (9.09%)  utilized 
interpersonal  technology- only  intervention,  and  three 
studies (2.27%) conducted pre- programmed and interper-
sonal technology.

Concerning  primary  intervention  modality,  65  trials 
(51.59%)  utilized  individual- based  methods,  while  53 
studies (42.06%) employed small- group- based techniques; 
additionally,  four  trials  used  a  family- based  approach, 
one  used  couple- based  intervention,  and  two  combined 
individual  and  small- group  modalities.  Training  proto-
cols  were  implemented  in  56%  (n = 70)  of  the  125  trails, 
compared to 56% (n = 70) that did not. Among the clini-
cal trials, 53.97% (n = 68) incorporated supervision during 
the  intervention,  whereas  46.06%  (n = 58)  did  not.  With 
respect  to  comparison  groups,  30.30%  (n = 40)  of  stud-
ies compared the treatment group to treatment- as- usual, 

DILS et al. 
   
6 of 10 

| 

T A B L E   1  Overall treatment effect and subgroup analysis.

Overall

Subgroup analysis with outcome categories

Mental health outcomes

Quality of Life

Subgroup analysis with age categories

<40 years old

40–64 years old
≥65 years old

Subgroup analysis with the delivery format

In- person therapy

Mixed in- person and tech

Tech- only interpersonal

Pre- programmed only

Tech- only interpersonal and pre- programmed

T A B L E   2  Univariate moderator analyses.

Estimate

N/K

0.388

132/1030

0.406

0.254

0.773

0.384

0.092

0.391

0.307

0.323

0.483

0.991

119/796

63/234

8/50

115/929

6/43

77/658

28/203

12/87

13/75

3/7

95% CI

0.294–0.483

p- value

<0.001

df

128

115

60.9

0.299–0.512

0.140–0.368

6.92

0.204–1.340

112

0.281–0.486

4.24

−0.094 – 0.278

74.5

26.4

10.8

11.9

0.255–0.526

0.133–0.481

−0.323–0.684

0.225–0.741

1.98

−1.140–3.120

<0.001

<0.001

=0.015

<0.001

=0.245

<0.001

=0.001

=0.074

=0.002

=0.182

Moderator analysis for mental health and quality of life outcomes combined

Estimate

N/K

df

95% CI

p value

Outcome (ref: mental health)

Quality of life

Age (intercept)

Age (slope)

Delivery format (ref: In- person)

Mixed in- person and tech

Tech- only interpersonal

Pre- programmed only

Tech- only interpersonal and pre- programmed

0.417

−0.122

0.983

−0.011

0.3891

−0.069

−0.058

0.094

0.591

132/1030

132/1030

129/1022

129/1022

132/1030

132/1030

132/1030

132/1030

132/1030

109.2

65.2

10.9

12.0

74.02

48.62

14.81

16.28

2.06

0.307–0.526

−0.286–0.041

0.395–1.570

−0.022–0.001

0.255–0.524

−0.290–0.151

−0.438–0.322

−0.195–0.383

−1.591–2.773

<0.001

=0.140

=0.003

=0.037

<0.001

=0.530

=0.750

=0.500

=0.371

has an overall large and statistically significant treatment 
effect  size  for  pediatric  and  adolescent  and  young  adult 
cancer survivors (<40 years old), d = 0.773, 95% CI 0.204–
1.340, p = 0.015. Interestingly, while CBT was overall sta-
tistically  significant  for  middle- aged  adults  (40–64 years 
old)  on  their  MH  and  QoL  outcomes,  d = 0.384,  95%  CI 
0.281–0.486, p < 0.001, its treatment effect for older cancer 
survivors (≥65 years old) was statistically non- significant, 
d = 0.092,  95%  CI  −0.094  to  0.278,  p = 0.245.  Subgroup 
analysis investigating CBT's treatment effect on MH and 
QoL outcomes by delivery format revealed that CBT has 
a statistically significant treatment effect size for patients 
receiving  in- person  therapy,  d = 0.391,  95%  CI  0.225–
0.526,  p = <0.001,  mixed  in- person  and  tech,  d = 0.307, 
95% CI 0.133–0.481 p = 0.001, and pre- programmed only, 
d = 0.483,  95%  CI  0.225–0.741,  p = 0.002.  Surprisingly, 
while  in- person  and  tech  were  statistically  significant, 
tech- only  interpersonal,  d = 0.323,  95%  CI  −0.323  to 

0.684,  p = 0.074  and  tech- only  interpersonal  and  pre- 
programmed d = 0.991, 95% CI −1.140 to 3.120, p = 0.182 
were not statistically significant.

3.2.2 

|  Moderator analysis findings

Univariate moderator analyses evaluated possible mod-
erators  in  relation  to  CBT's  treatment  effect  for  cancer 
survivors (Table 2). Specifically, the difference in treat-
ment  effect  sizes  was  statistically  non- significant  be-
tween CBT for cancer survivors' QoL outcomes and MH 
outcomes, b = −0.122, 95% CI −0.286 to 0.041, p = 0.140. 
In  addition,  cancer  survivors'  age  significantly  moder-
ated CBT's treatment effect on MH and QoL outcomes, 
b = −0.011,  95%  CI  −0.022  to  −0.001,  p = 0.037.  For 
each unit increase in a study's participant average age, 
that study is expected to report 0.011 smaller treatment 

DILS et al. 
 
effect  sizes.  The  delivery  format  was  not  a  significant 
moderator.

4 

|  DISCUSSIO N

CBT is a research- supported treatment for individuals liv-
ing  with  a  cancer  diagnosis  across  a  broad  spectrum  of 
outcomes, with the strongest support for its effect for MH 
outcomes.28  Given  the  established  relationship  between 
MH and QoL,29 it is reasonable to expect that CBT would 
benefit cancer survivors' QoL life outcomes. To that end, 
the  purpose  of  this  study  is  to  empirically  evaluate  the 
treatment effect of CBT for MH and QoL among individu-
als with cancer.

Consistent  with  the  existing  literature,  when  com-
bining CBT's treatment effect for both MH and QoL out-
comes, an overall statistically significant treatment effect 
was identified.23,30 Importantly, however, subgroup analy-
sis suggested a moderate versus small overall treatment ef-
fect of CBT for MH and QoL outcomes, respectively. While 
CBT's overall treatment effect was statistically significant 
for  both  outcome  domains,  findings  of  this  study  sug-
gested a relatively greater overall treatment effect size of 
CBT for MH (moderate) versus QoL (small). It is import-
ant to note that moderator analysis revealed the difference 
in  the  effect  size  for  MH  versus  QoL  outcomes  was  sta-
tistically  non- significant.  This  particular  finding  renders 
several important clinical implications. First, oncological 
providers  should  continue  to  view  CBT  as  a  research- 
supported intervention for both MH and QoL outcomes. 
Second,  individuals  with  cancer  may  benefit  more  from 
CBT  for  their  MH  outcomes  than  QoL  outcomes. Third, 
researchers  and  oncological  providers  are  encouraged  to 
further consider how to maximize the benefit of CBT for 
MH to have a stronger connection with cancer patients/
survivors QoL outcomes. For example, existing literature 
have suggested that MH combined with improvement in 
social relationship and self- efficacy will lead to improve-
ment in cancer patients/survivors QoL.30,31

In addition to our main meta- analytical findings, our 
selection  of  age  and  delivery  format  for  subgroup  and 
moderator analysis revealed a couple of clinically signif-
icant  findings.  First,  subgroup  analysis  of  CBT's  treat-
ment effect across cancer patients/survivors age spectrum 
revealed  CBT  being  overall  statistically  significant  for 
pediatric,  adolescent  and  young  adult  cancer  patients/
survivors (<40 years old), middle adults with cancer (40–
64 years old), but ineffective for older cancer patients/sur-
vivors (>65 years old). This reveals a significant gap in the 
psychosocial oncology literature of CBT for MH and QoL 
outcomes.  Given  the  majority  of  individuals  diagnosed 
with  cancer  are  those  who  are  of  older  age,32  an  overall 

|  7 of 10

statistically non- significant treatment of CBT for this age 
group's MH and QoL outcome is concerning and warrant 
further investigation. Notably, this finding seemed consis-
tent with the existing CBT literature that has found older 
adults benefiting less than their middle adult counterpart 
from receiving CBT.33,34

Second, in addition to age, we have evaluated treat-
ment  delivery  as  a  factor  for  subgroup  and  moderator 
analysis.  Notably,  subgroup  analysis  revealed  that  the 
overall treatment effects of CBT were statistically non- 
significant  when  being  delivered  as  an  interpersonal 
modality  only  via  technology,  that  is,  having  a  human 
therapist/clinician  delivering  care  via  tech  platforms, 
or  technology- only  intervention  combined  with  pre- 
programmed  content.  This  is  an  interesting  finding  as 
it seemed to suggest that when there is an interpersonal 
component  involved  in  the  treatment  delivery,  an  in- 
person  modality  seemed  to  be  critical  to  ensure  treat-
ment effectiveness. One possible explanation is that, for 
patients  choose  to  receive  interpersonal  therapy,  they 
are  expect  some  level  of  human- to- human  in- person 
connection, that can be difficult to be replaced any tech-
nological format, for example, having a live human ther-
apist  on  the  other  end  of  Zoom.  Future  investigations 
should focus on how delivery format impacts interper-
sonal  supportive  care  for  cancer  patients/survivors.  It 
was, however, encouraging to reveal that other formats 
of delivering CBT have been equally beneficial for indi-
viduals living with a cancer diagnosis, suggesting CBT's 
dexterity for large- scale uptake.

An  important  context  to  understanding  the  study's 
findings is the proportion of studies with a relatively small 
sample size. Due to the state of the science/published lit-
erature, many studies included in this meta- analysis were 
considered  “preliminary  efficacy  trials.”  To  a  certain  ex-
tent, this feature of the existing literature reflected a lack 
of high- quality clinical trials that are well conceptualized 
and have a large sample size of CBT for individuals with 
cancer. Despite the relatively well- established clinical effi-
cacy of CBT for individuals with cancer, future studies of 
CBT in cancer should prioritize CBT intervention fidelity, 
maturity, and large sample size.

Overall,  our  findings  indicate  that  CBT  is  associated 
with marked improvement in MH and QoL for all types 
of  cancer  patients  including  those  actively  in  treatment 
and post treatment. A notable implication of this study's 
findings  suggests  that  CBT  seemed  to  have  benefits  for 
cancer patients/survivors beyond MH outcomes but also 
their QoL. The broad scope of CBT benefits suggests that 
CBT  being  made  available  to  cancer  patients/survivors, 
even when a formal MH diagnosis is not imminently pres-
ent, could be warranted. Further, our findings support the 
need for further investigation into psychosocial treatment 

DILS et al. 
   
8 of 10 

| 

modalities that may better serve those in the older adult 
population.  These  findings  are  informative  to  clinical 
practice  and how best to  treat the psychosocial realm of 
cancer treatment.

|  STRENGTH S  AN D 

5 
LIMITATIONS

The  findings  of  this  project  should  be  contextualized 
in  some  limitations  of  the  study.  First,  there  is  always  a 
chance that we may have missed some articles despite a 
comprehensive search strategy we have followed. Such a 
concern, however, is relatively low given the large number 
of articles and very large number of effect sizes included 
in  the  analysis.  Second,  it  is  possible  that  we  may  have 
missed  other  important  factors  for  subgroup  and  mod-
erator analyses. However, multiple statistical tests would 
result in an inflated Type I error rate, and therefore, we se-
lected two theoretically and clinically meaningful factors 
to consider in this paper. Finally, for this study's modera-
tor analysis, we used univariate moderator analysis, that 
is to enter the moderators in meta- regression once a time. 
Given meta- regression uses case wise deletion for missing 
value,  that  is,  if  missing  in  one  variable,  the  entire  case 
is deleted, we chose to use univariate meta- regression to 
reduce the impact of missingness, though multi- variable 
meta- regression may offer a more nuanced understanding 
of CBT's treatment effect. This should be the focus of fu-
ture investigations when more data (with minimal miss-
ing) becomes available.

Notwithstanding the above- mentioned limitations, this 
study represents one of the most comprehensive and larg-
est systematic review and meta- analysis study that evalu-
ated CBT's treatment effect for cancer patients, and one of 
the first that included both MH and QoL outcomes. This 
study benefited from a large sample size with an advanced 
statistical analysis framework that facilitates rigorous and 
flexible modeling needs. Finally, findings of the study pro-
vides important clinical implications, especially the focus 
on  CBT's  differential  treatment  effect  across  age  groups 
and delivery format among cancer patients/survivors.

6 

|  CONCLU SIO N

Based  on  previous  literature,  cancer  patients  suffer  from 
impaired MH and QoL, and integration of CBT into treat-
ment regiments has been a useful tool in assisting with these 
psychosocial challenges. In this study, we noted a mild to 
moderate improvement in MH and QoL in cancer patients 
receiving  CBT  as  a  form  of  treatment.  Additionally,  we 
found that age and treatment delivery setting can influence 

the efficacy of CBT in cancer patients. These results have 
implications  in  effectively  treating  the  psychosocial  com-
plications associated with cancer treatment. Further work 
will  need  to  be  performed  investigating  other  factors  in-
volved in CBT treatment in cancer patients.

AUT HOR CON TRIBUT IONS
Alexander T. Dils: Formal analysis (equal); investiga-
tion (equal); project administration (equal); supervision 
(equal); writing – original draft (equal); writing – review 
and  editing  (equal).  Kathryn  O'Keefe:  Data  curation 
(equal);  investigation  (equal);  methodology  (equal); 
writing  –  original  draft  (equal);  writing  –  review  and 
editing  (equal).  Nada  Dakka:  Data  curation  (equal); 
methodology  (equal);  validation  (equal);  writing  –  re-
view  and  editing  (equal).  Michelle  Azar:  Data  cura-
tion  (equal);  methodology  (equal);  validation  (equal); 
writing  –  original  draft  (equal);  writing  –  review  and 
editing  (equal).  Meiyan  Chen:  Data  curation  (equal); 
formal  analysis  (equal);  writing  –  review  and  editing 
(equal).  Anao  Zhang:  Conceptualization  (equal);  data 
curation  (equal);  formal  analysis  (equal);  investigation 
(equal); methodology (equal); supervision (equal); writ-
ing – original draft (equal); writing – review and editing 
(equal).

FUNDING  INFORMAT ION
No funding to report.

CONFLICT OF IN TEREST STAT EMENT
All  authors  of  this  paper  have  no  conflict  of  interest  to 
disclose.

DATA AVAILABILIT Y STAT EM EN T
Data  can  be  made  available  upon  reasonable  request  to 
the corresponding author.

ET HICS STAT EM ENT
Given  the  nature  of  this  paper,  ethics  approval  is  not 
relevant.

ORCID
Anao Zhang 

 https://orcid.org/0000-0002-3199-1113 

R E F E R E N C E S
  1.  Van Der Kruk SR, Butow P, Mesters I, et al. Psychosocial well- 
being and supportive care needs of cancer patients and survi-
vors living in rural or regional areas: a systematic review from 
2010 to 2021. Support Care Cancer. 2022;1:1-44.

  2.  Ellis  SJ,  Wakefield  CE,  Antill  G,  Burns  M,  Patterson  P. 
Supporting  children  facing  a  parent's  cancer  diagnosis:  a  sys-
tematic  review  of  children's  psychosocial  needs  and  existing 
interventions. Eur J Cancer Care. 2017;26(1):e12432.

DILS et al. 
 
  3.  Grassi  L,  Spiegel  D,  Riba  M.  Advancing  psychosocial  care  in 

cancer patients. F1000Research. 2017;6:6.

  4.  Mitchell AJ, Ferguson DW, Gill J, Paul J, Symonds P. Depression 
and  anxiety  in  long- term  cancer  survivors  compared  with 
spouses  and  healthy  controls:  a  systematic  review  and  meta- 
analysis. Lancet Oncol. 2013;14(8):721-732.

  5.  Zhang  A, Weaver  A, Walling  E,  et  al.  Evaluating  an  engaging 
and coach- assisted online cognitive behavioral therapy for de-
pression among adolescent and young adult cancer survivors: a 
pilot feasibility trial. J Psychosoc Oncol. 2023;41(1):20-42.
  6.  Hofmann SG, Asnaani A, Vonk IJ, Sawyer AT, Fang A. The effi-
cacy of cognitive behavioral therapy: a review of meta- analyses. 
Cognit Ther Res. 2012;36:427-440.

  7.  Fordham B, Sugavanam T, Edwards K, et al. The evidence for 
cognitive behavioural therapy in any condition, population or 
context:  a  meta- review  of  systematic  reviews  and  panoramic 
meta- analysis. Psychol Med. 2021;51(1):21-29.

  8.  Driessen E, Hollon SD. Cognitive behavioral therapy for mood 
disorders:  efficacy,  moderators  and  mediators.  Psychiatr  Clin. 
2010;33(3):537-555.

  9.  Tatrow K, Montgomery GH. Cognitive behavioral therapy tech-
niques for distress and pain in breast cancer patients: a meta- 
analysis. J Behav Med. 2006;29:17-27.

 10.  Garland  SN,  Johnson  JA,  Savard  J,  et  al.  Sleeping  well  with 
cancer:  a  systematic  review  of  cognitive  behavioral  therapy 
for  insomnia  in  cancer  patients.  Neuropsychiatr  Dis  Treat. 
2014;18:1113-1124.

 11.  Capezzani L, Ostacoli L, Cavallo M, et al. EMDR and CBT for 
cancer patients: comparative study of effects on PTSD, anxiety, 
and depression. JEMDR. 2013;7(3):134-143.

 12.  Mendoza ME, Capafons A, Gralow JR, et al. Randomized con-
trolled trial of the Valencia model of waking hypnosis plus CBT 
for pain, fatigue, and sleep management in patients with cancer 
and cancer survivors. Psychooncology. 2017;26(11):1832-1838.

 13.  Montel S. Fear of recurrence: a case report of a woman breast 
cancer  survivor  with  GAD  treated  successfully  by  CBT.  Clin 
Psychol Psychother. 2010;17(4):346-353.

 14.  Nguyen P, Heisey R, Quenneville C, et al. An examination of 
depression, anxiety, and fear of recurrence among cancer sur-
vivors who participated in a virtual cognitive behavioral ther-
apy  (CBT)- based  telephone  coaching  program.  Support  Care 
Cancer. 2022;30(9):7323-7332.

 15.  Jassim GA, Doherty S, Whitford DL, Khashan AS. Psychological 
interventions  for  women  with  non- metastatic  breast  cancer. 
Cochrane Database Syst Rev. 2023;1:1-151.

|  9 of 10

psychosocial treatment effect on cancer survival. Cancer Med. 
2019;8(1):363-373.

 20.  Abrahams  HJ,  Gielissen  MF,  Donders  RR,  et  al.  The  ef-
ficacy  of  internet- based  cognitive  behavioral  therapy  for 
severely  fatigued  survivors  of  breast  cancer  compared 
with  care  as  usual:  a  randomized  controlled  trial.  Cancer. 
2017;123(19):3825-3834.

 21.  Everts FZ, Van Der Lee ML, de Jager ME. Web- based individ-
ual mindfulness- based cognitive therapy for cancer- related fa-
tigue—a pilot study. Internet Interv. 2015;2(2):200-213.

 22.  Mehta  S,  Peynenburg  VA,  Hadjistavropoulos  HD.  Internet- 
delivered cognitive behaviour therapy for chronic health con-
ditions:  a  systematic  review  and  meta- analysis.  J  Behav  Med. 
2019;15(42):169-187.

 23.  Ye  M,  Du  K,  Zhou  J,  et  al.  A  meta- analysis  of  the  efficacy  of 
cognitive behavior therapy on quality of life and psychological 
health of breast cancer survivors and patients. Psychooncology. 
2018;27(7):1695-1703.

 24.  Carlbring  P,  Andersson  G,  Cuijpers  P,  Riper  H,  Hedman- 
Lagerlöf  E.  Internet- based  vs.  face- to- face  cognitive  behav-
ior  therapy  for  psychiatric  and  somatic  disorders:  an  updated 
systematic  review  and  meta- analysis.  Cogn  Behav  Ther. 
2018;47(1):1-8.

 25.  Hedges LV, Tipton E, Johnson MC. Robust variance estimation 
in  meta- regression  with  dependent  effect  size  estimates.  Res 
Synth Methods. 2010;1(1):39-65.

 26.  Sedgwick P, Marston L. How to read a funnel plot in a meta- 

analysis. BMJ. 2015;16:351.

 27.  Sterne JA, Sutton AJ, Ioannidis JP, et al. Recommendations for 
examining  and  interpreting  funnel  plot  asymmetry  in  meta- 
analyses of randomised controlled trials. BMJ. 2011;22:343.
 28.  Daniels S. Cognitive behavior therapy for patients with cancer. 

J Adv Pract Oncol. 2015;6(1):54-56.

 29.  Zhang A, Wang K, Blumenstein K, et al. For whom and what 
outcomes does cognitive- behavioral- therapy work among can-
cer  survivors:  a  systematic  review  and  meta- analysis.  Support 
Care Cancer. 2022;30(11):8625-8636.

 30.  Hopko DR, Bell JL, Armento M, et al. Cognitive- behavior ther-
apy  for  depressed  cancer  patients  in  a  medical  care  setting. 
Behav Ther. 2008;39(2):126-136.

 31.  Shelby  RA,  Edmond  SN,  Wren  AA,  et  al.  Self- efficacy  for 
coping  with  symptoms  moderates  the  relationship  between 
physical  symptoms  and  well- being  in  breast  cancer  survivors 
taking  adjuvant  endocrine  therapy.  Support  Care  Cancer. 
2014;22:2851-2859.

 16.  Mustafa  M,  Carson- Stevens  A,  Gillespie  D,  Edwards  AG. 
Psychological interventions for women with metastatic breast 
cancer. Cochrane Database Syst Rev. 2013;6:1-61.

 32.  White MC, Holman DM, Boehm JE, Peipins LA, Grossman M, 
Henley SJ. Age and cancer risk: a potentially modifiable rela-
tionship. Am J Prev Med. 2014;46(3):S7-S15.

 17.  Sun H, Huang H, Ji S, et al. The efficacy of cognitive behavioral 
therapy  to  treat  depression  and  anxiety  and  improve  quality 
of life among early- stage breast cancer patients. Integr Cancer 
Ther. 2019;18:1534735419829573.

 33.  Kishita  N,  Laidlaw  K.  Cognitive  behaviour  therapy  for  gen-
eralized  anxiety  disorder:  is  CBT  equally  efficacious  in 
adults  of  working  age  and  older  adults?  Clin  Psychol  Rev. 
2017;1(52):124-136.

 18.  Zhang  A,  Wang  K,  Zebrack  B,  Tan  CY,  Walling  E,  Chugh  R. 
Psychosocial, behavioral, and supportive interventions for pe-
diatric,  adolescent,  and  young  adult  cancer  survivors:  a  sys-
tematic  review  and  meta- analysis.  Crit  Rev  Oncol  Hematol. 
2021;1(160):103291.

 19.  Mirosevic S, Jo B, Kraemer HC, Ershadi M, Neri E, Spiegel D. 
“Not  just  another  meta- analysis”:  sources  of  heterogeneity  in 

 34.  Chand  SP,  Grossberg  GT.  How  to  adapt  cognitive- behavioral 
therapy for older adults. Curr Psychiatr Ther. 2013;12(3):10-15.

FO U R   P RO F E S S I O NA L  W E B S I T E S
  1.  Association  for  Behavioral  and  Cognitive  Therapies  https:// 

www. abct. org/ 

DILS et al. 
   
10 of 10 

| 

  2.  Association for Clinical Oncology: https:// www. asco. org/ about 

-  asco/ about -  asco-  assoc iation

  3.  International  Psycho- Oncology  Society:  https:// www. ipos-  

socie ty. org/ 

  4.  Association of Oncology Social Work: https:// aosw. org/ 

SUPPORTI NG INFORMATION
Additional  supporting  information  can  be  found  online 
in  the  Supporting  Information  section  at  the  end  of  this 
article.

How to cite this article: Dils AT, O’Keefe K, Dakka 
N, Azar M, Chen M, Zhang A. The efficacy of 
cognitive behavioral therapy for mental health and 
quality of life among individuals diagnosed with 
cancer: A systematic review and meta- analysis. 
Cancer Med. 2024;13:e70063. doi:10.1002/cam4.70063

DILS et al.
