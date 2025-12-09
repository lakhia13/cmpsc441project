# Lee_2025_Exploring novel determinants of exercise behavior a lagged exposure-wide approach.

Annals of Behavioral Medicine, 2025, 59, 1–15
https://doi.org/10.1093/abm/kaae082
Advance access publication 4 January 2025
Regular Article

Exploring novel determinants of exercise behavior:  
a lagged exposure-wide approach
Harold H. Lee, PhD1,* · Eric S. Kim, PhD2,3,4 · Younseo Kim5 · David E. Conroy, PhD6 ·  
Tyler J. VanderWeele, PhD4,7,8

1Department of Biobehavioral Health, The Pennsylvania State University, University Park, PA 16802, United States, 
2Department of Psychology, University of British Columbia, BC V6T 1Z4, United States, 
3Lee Kum Sheung Center for Health and Happiness, Harvard T.H. Chan School of Public Health, Boston, MA 02115, United States, 
4Human Flourishing Program, Institute for Quantitative Social Science, Harvard University, Cambridge, MA 02138, United States, 
5Department of Statistics, The Pennsylvania State University, University Park, PA 16802, United States, 
6Department of Kinesiology, University of Michigan, Ann Arbor, MI 48109, United States, 
7Department of Epidemiology, Harvard T.H. Chan School of Public Health, Boston, MA 02115, United States, 
8Department of Biostatistics, Harvard T.H. Chan School of Public Health, Boston, MA 02115, United States
*Corresponding author: Harold H. Lee, PhD, Department of Biobehavioral Health, College of Health and Human Development, The Pennsylvania State 
University, State College, 124 Biobehavioral Health Building, University Park, PA 16802, United States (hkl5425@psu.edu).
H.H. Lee and E.S. Kim are co-first authors.

Abstract 
Many middle-aged to older adults do not engage in regular exercise at all, despite its importance for healthy aging. Extensive research grounded 
in behavioral and social science theories has identified numerous determinants of exercise. However, few studies used an exposure-wide ap-
proach, a data-driven exploratory method particularly useful for identifying novel determinants.

Methods:  We used data from 13 771 participants in the Health and Retirement Study, a diverse, national panel study of adults aged >50 years 
in the United States, to evaluate 62 candidate determinants of exercise participation. Candidate predictors were drawn from the following do-
mains: health behaviors, physical health, psychological well-being, psychological distress, social factors, and work. We used Poisson regression 
with robust error variance to individually regress exercise in the outcome wave (t2: 2014/2016) on baseline candidate predictors (at t1: 2010/2012) 
controlling for all covariates in the previous wave (t0: 2006/2008).
Results:  Some physical health conditions (eg, physical functioning limitations and lung disease), psychological factors (eg, health mastery, pur-
pose in life, and positive affect), and social factors (eg, helping others, religious service attendance, and volunteering) were robustly associated 
with increased subsequent exercise. Among factors related to psychological distress, perceived constraints stood out as a factor in reducing 
exercise.

Conclusions:    We  identified  potentially  novel  exercise  determinants,  such  as  helping  friends/neighbors/relatives,  religious  attendance,  and 
volunteering, that have not been captured using a theory-driven approach. Future studies validating these findings experimentally in midlife and 
older adults are needed.

Lay Summary 
Regular exercise is crucial for healthy aging, yet many older adults remain inactive. This study explored factors influencing exercise participation 
in adults over 50 using data from a large national survey. Researchers examined 62 potential predictors across health, psychological, and social 
domains. Physical health issues such as lung and heart diseases were strongly associated with not exercising. Unexpectedly, social activities 
such  as  helping  others,  church  attendance,  and  volunteering  were  the  strongest  predictors  of  exercise  participation.  Similarly,  psychological 
well-being factors such as having a sense of purpose and positive emotions were linked to increased exercise. Many of these strong predictors 
are  not  typically  considered  in  traditional  behavioral  and  social  science  theories,  making  these  findings  novel. The  study  also  confirmed  the 
widely accepted view among behavioral scientists that exercise behavior is influenced by numerous factors, each with modest effects. While 
these results suggest potential targets for interventions to promote exercise, further experimental studies are needed to confirm cause-and-
effect relationships. Understanding these diverse influences on exercise behavior could lead to more effective strategies for encouraging phys-
ical activity in aging populations, ultimately contributing to better health outcomes for older adults.

Key words: exercise; physical activity; lagged exposure-wide analysis; midlife.

Introduction
Numerous  systematic  reviews  spanning  various  age  groups 
consistently underscore the vital role of exercise in promoting 
healthy aging.1–6 Unfortunately, a progressive decline in phys-
ical activity is observed after age 45-50,7,8 a period in which 

the  health  benefits  of  exercise  on  aging  become  more  pro-
nounced considering the large increase in the incidence of pre-
ventable  chronic  diseases  after  age  45-50.9  This  paradox  is 
of paramount concern given the aging population. There are 
now 46.3 million Americans aged over 65, and this number 

© The Author(s) 2025. Published by Oxford University Press on behalf of the Society of Behavioral Medicine.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), 
which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

2

ann. behav. med. (2025) 59:1–15

is projected to increase by almost 50% in the next 15 years.10 
Health  organizations  used  to  recommend  150-300  minutes 
of weekly moderate-to-vigorous physical activity until 2018, 
after which the guidelines eliminated the minimum duration 
for  exercise  sessions.11–13  The  utility  of  engaging  in  at  least 
some  exercise  was  further  corroborated  by  more  recent  ro-
bust  epidemiological  studies  demonstrating  that  even  brief 
bouts of exercise, lasting as little as 1 minute, can significantly 
reduce  the  risk  of  mortality  and  heart  disease.14,15 Thus,  as-
sisting  physically  inactive  older  adults  to  start  engaging  in 
at least some regular exercise carries increasingly substantial 
public health significance.

For discerning the factors that elucidate exercise determin-
ants, both induction and deduction serve as valuable epistemo-
logical tools.16,17 However, the empirical research of the past 
4 decades has predominantly embraced a deductive method-
ology, anchored in the tenets of behavioral and social science 
theories. Notably, the investigation of exercise determinants 
began with atheoretical literature reviews,18–20 which evolved 
to the socioecological model, an expansive and multifaceted 
framework that extends beyond intra- and interindividual in-
fluences, such as the built environment and policy. Within the 
scope  of  intra-  and  interindividual  determinants,  behavioral 
science  theories—initially  focused  on  cognitive  and  social 
factors  in  the  late  20th  century,  with  a  recent  emphasis  on 
affective  determinants  in  the  early  21st  century—have  pro-
liferated  a  substantial  body  of  empirical  evidence  clarifying 
why certain individuals refrain from engaging in exercise.21–25 
While  valuable  for  guiding  our  research,  these  theoretical 
models  may  constrict  our  investigative  scope,  inadvertently 
overlooking  causal  factors  that  do  not  fit  neatly  within  es-
tablished  theoretical  lenses.  To  complement  this  theoretical 
approach  (ie,  deduction),  agnostically  scrutinizing  a  large 
number  of  factors,  including  those  not  traditionally  viewed 
as  causal  (ie,  induction),  may  uncover  new  and  unexpected 
insights.  Such  an  approach  may  be  particularly  relevant  for 
the  putative  causal  factors  that  exert  weak  or  no  effect  in 
younger age groups but becomes more salient as individuals 
reach middle age and older adulthood, a period characterized 
by  physiological  deterioration  (eg,  muscle  loss  and  physical 
ailment)  and  shifts  in  social  dynamics  (eg,  family  structure) 
in which classic exercise determinants (eg, self-efficacy, social 
support,  affect,  and  socioeconomic  status)  exert  weaker  or 
stronger effects on exercise participation.26–28

An innovative approach that may be able to identify novel 
targets  of  intervention  is  an  exposure-wide  approach,  in 
which a large number of candidate predictors are examined 
with no a priori hypotheses,29 which can be refined to more 
principled approaches with respect to confounding control by 
focusing on exposures at a single point in time.30,31 We used 
such an exposure-wide approach to explore the determinants 
of changes in participation in at least some exercise (ie, from 
inactivity to some activity) among older US adults to help en-
rich the existing empirical literature in this area. We applied a 
lagged exposure-wide epidemiologic design, which is a data-
driven  approach  aimed  at  elucidating  promising  predictors 
of  a  particular  outcome  that  can  then  be  examined  further 
in subsequent research. This analytic approach includes steps 
that  rigorously  control  for  potential  confounding  and  miti-
gate  concerns  about  reverse  causation,30  thereby  strength-
ening causal inference. Using a nationwide sample of ~13 000 
adults aged >50 years in the United States, we examined 62 
candidate predictors of exercise participation drawn from the 

following domains: health behaviors, physical health, psycho-
logical  well-being,  psychological  distress,  social  factors,  and 
work. These predictors were selected to align with our prior 
studies using the same sample.32–34

Methods
Study population
We used data from the Health and Retirement Study (HRS), 
a  nationwide  panel  study  of  people  aged  >50  in  the  United 
States.35  In  2006,  HRS  first  assessed  psychosocial  data  in  a 
random 50% of participants who were selected to complete 
an enhanced face-to-face interview. The other 50% were as-
sessed  in  the  next  wave  (2008). After  the  interview,  partici-
pants completed a psychosocial questionnaire which they then 
mailed back to the University of Michigan. The response rates 
were  88%  in  2006  and  84%  in  2008.36  Each  HRS  partici-
pant completes this psychosocial questionnaire every 4 years. 
Data from the 2006 and 2008 sub-cohorts were combined to 
increase sample size and statistical power. Participants were 
excluded if they did not report psychosocial data in this pre-
baseline  wave  (since  over  half  of  the  study  predictors  were 
psychosocial  factors)  resulting  in  a  final  sample  of  13 771 
participants.

We  used  data  from  3  time  points,  each  spaced  4  years 
apart:  (1)  covariates  were  assessed  in  the  pre-baseline  wave 
(t0:  2006/2008),  (2)  candidate  predictors  were  assessed  in 
the baseline wave (t1: 2010/2012), and (3) our outcome (ever 
exercise) was assessed in the outcome wave (t2: 2014/2016).

Measures
Ever exercise
Exercise  behavior  was  operationalized  using  the  HRS  item 
series  denoting  vigorous  activity  (vgactx)  and  moderate  ac-
tivity  (mdactx).  Participants  indicated  the  frequency  with 
which they engaged in vigorous (eg, running, swimming, and 
aerobics) and moderate (eg, gardening, dancing, and walking 
at  a  moderate  pace)  exercise  over  the  past  12  months.  For 
both vigorous and moderate activities, participants could se-
lect  from  5  frequency  options,  including:  (1)  daily,  (2)  >1×/
week,  (3)  1×/week,  (4)  1-3×/month,  or  (5)  never.  Given  our 
focus  on  engaging  in  at  least  some  exercise  versus  no  exer-
cise at all, this variable was dichotomized as never versus all 
else for each intensity. That is, those who reported engaging 
in  either  vigorous  or  moderate  activities  with  a  frequency 
ranging from daily to 1-3×/month were classified as “at least 
some  exercisers.”  Duration  data  were  not  available  in  the 
HRS dataset.

[continuous],  gender 

Covariates
We adjusted for a substantial number of covariates in the pre-
baseline wave (t0: 2006/2008), including sociodemographics 
(age 
[male/female],  race/ethnicity 
[White,  African-American,  Hispanic,  and  Other],  marital 
status  [married/not  married],  income  [<$50 000,  $50 000-
$74 999,  $75 000-$99 999,  and  ≥$100 000],  total  wealth 
[based on quintiles of the score distribution for total wealth 
in this sample], educational attainment [no degree, GED/high 
school diploma, and ≥college degree], employment status [yes/
no], health insurance [yes/no], geographic region [Northeast, 
Midwest,  South,  and  West],  religious  service  attendance 
[none,  <1×/week,  and  ≥1×/week],  personality  [openness, 

ann. behav. med. (2025) 59:1–15

3

conscientiousness,  extraversion,  agreeableness,  and  neuroti-
cism;  continuous],  and  childhood  abuse  [yes/no]).  We  ad-
justed  for  prior  values  of  all  predictors  to  evaluate  change 
in each predictor.30 To reduce the possibility of reverse caus-
ation, we also adjusted for pre-baseline exercise.

We evaluated 62 candidate predictors in the baseline wave 
(t1:  2010/2012)  including  measures  of:  (1)  health  behaviors 
(ever exercise, smoking, heavy drinking, and sleep problems); 
(2)  physical  health  (number  of  chronic  conditions,  diabetes, 
hypertension, stroke, cancer, heart disease, lung disease, arth-
ritis,  overweight/obesity,  physical  functioning  limitations, 
cognitive impairment, chronic pain, self-rated health, hearing, 
and  eyesight);  (3)  psychological  well-being  (positive  affect, 
life  satisfaction,  optimism,  purpose  in  life,  mastery,  health 
mastery, and financial mastery); (4) psychological distress (de-
pression, depressive symptoms, hopelessness, negative affect, 
perceived constraints, anxiety, trait anger, state anger, cynical 
hostility,  stressful  life  events,  financial  strain,  daily  discrim-
ination,  and  major  discrimination);  (5)  social  factors  (lone-
liness, living with spouse, frequency of contact in 3 separate 
relationship categories: (i) children, (ii) other family, and (iii) 
friends,  closeness  with  spouse,  number  of  close  (i)  children, 
(ii) other family, and (iii) friends, positive social support from 
(i)  spouse,  (ii)  children,  (iii)  other  family,  and  (iv)  friends, 
negative social strain from (i) spouse, (ii) children, (iii) other 
family,  and  (iv)  friends,  volunteer  activity,  helping  friends, 
neighbors,  and  relatives,  religious  service  attendance,  so-
cial status ladder ranking, and change in social status ladder 
ranking); and (6) employment (in the labor force). HRS ma-
terials provide further details about each variable.37–39

Multiple imputation
All missing exposures, covariates, and outcome variables were 
imputed using multiple imputations by chained equations; 5 
imputed datasets were created. This method was used because 
it  is  more  flexible  than  other  methods  of  handling  missing 
data and helps address problems that arise from attrition.40–42

Statistical analysis
We  used  a  lagged  exposure-wide  approach30  and  ran  sep-
arate models for each exposure. In our primary analyses, ever 
exercise was a binary outcome that was common (>10% in 
our  sample).  Thus,  we  used  Poisson  regression  with  robust 
error  variance  to  individually  regress  exercise  in  the  out-
come wave (t2: 2014/2016) on baseline candidate predictors 
(at t1: 2010/2012), that is residualized changes in the likeli-
hood of ever exercising 4 years later, after controlling for all 
covariates in the previous wave (t0: 2006/2008). Adjusting for 
pre-baseline  levels  of  exposure  helps  us  evaluate  the  associ-
ation  between “changes”  in  exposure  and  subsequent  exer-
cise behavior. As detailed in Appendix Text #1, this method 
isolates  the  impact  of  exposure  changes  over  time  on  sub-
sequent exercise outcomes. Because behavioral interventions 
target  factors  that  drive  changes  in  physical  activity,  rather 
than just predicting higher activity levels, analyzing changes 
in  exposure  is  more  relevant  for  developing  effective  inter-
ventions  than  simply  evaluating  exercise  outcomes  without 
accounting for baseline levels. Each predictor was examined 
one at a time in separate models. Continuous predictors were 
standardized (mean = 0, SD = 1) so their effect sizes could be 
interpreted as an SD change in the exposure. For categorical 
exposures, the effect estimate corresponds to associations be-
tween  the  exposure  at  baseline  (at  t1:  2010/2012),  and  ever 

exercising at the outcome wave (t2: 2014/2016), conditional 
on the exposure and covariates in the pre-baseline wave (at t0: 
2006/2008). We  marked  multiple  P-value  cutoffs  (including 
Bonferroni-corrected)  and  provided  exact  CIs,  since  mul-
tiple  testing  practices  vary  widely  and  are  continuously 
evolving.43,44

Additional analyses
Unlike  experimental  studies  with  randomization,  observa-
tional studies inherently provide weaker causal inferences re-
garding  the  hypothesized  relationship  between  an  exposure 
and  an  outcome. This  limitation  arises  because  it  is  impos-
sible  to  completely  rule  out  the  influence  of  unmeasured 
confounders (ie, a covariate that has a causal influence on the 
independent  variable  and  the  outcome  variable).  Regardless 
of the size of the dataset, these unmeasured confounders can 
introduce  bias. To  evaluate  the  robustness  of  our  results  to 
potential  unmeasured  confounding,  we  calculated  E-values 
to assess the minimum strength of unmeasured confounding 
on the risk ratio (RR) scale (with both the exposure and the 
outcome) needed to explain away the association between the 
exposure and outcome.45 As such, a higher E-value indicates 
that stronger unmeasured confounding would be required to 
overturn the association, suggesting greater confidence in the 
observed  relationship.  Conversely,  a  lower  E-value  suggests 
that even relatively weak unmeasured confounding could po-
tentially alter the findings, highlighting the need for caution in 
interpreting the results.

Results
In the pre-baseline wave (t0: 2006/2008), when all covariates 
were  assessed,  the  average  age  of  participants  was  69  years 
old (SD = 10), more likely women (58%) and married (62%). 
Table  1  summarizes  participant  characteristics.  Table  2  de-
scribes  the  changes  in  exercise  from  the  pre-baseline  wave 
(t0)  to  the  outcome  wave  (t2).  Among  participants  who  re-
ported ever exercising at t0, 75% continued to exercise at t2, 
while 25% no longer exercised. Conversely, of those who did 
not exercise at t0, 33% began exercising by t2, whereas 66% 
remained non-exercisers. Figure 1 and Table 3 show the as-
sociations between the candidate predictors and subsequent 
exercise.

When considering health behaviors, 1 out of 4 predictors 
were significantly associated with an increased likelihood of 
subsequent  exercise.  Not  surprisingly,  ever  exercising  in  the 
past  was  associated  with  an  increased  likelihood  of  subse-
quent  exercise  with  the  highest  effect  size  (RR = 1.86,  95% 
CI = 1.73-2.01).  For  physical  health  indicators,  9  out  of  15 
candidate predictors were associated with an increased like-
lihood  of  subsequent  exercise.  Among  physical  health  indi-
cators,  physical  functioning  limitations  (RR = 0.75,  95% 
CI = 0.70-0.80),  stroke  (RR = 0.78,  95%  CI = 0.64-0.96), 
and lung disease (RR = 0.85, 95% CI = 0.76-0.96) were most 
strongly  associated  with  decreased  likelihood  of  subsequent 
exercise.

There was evidence that several psychological factors (11 
out of 20 predictors) were associated with an increased likeli-
hood of subsequent exercise. Among psychological well-being 
factors,  health  mastery  (RR = 1.09,  95%  CI = 1.07-1.12), 
purpose in life (RR = 1.08, 95% CI = 1.05-1.10), and positive 
affect (RR = 1.07, 95% CI = 1.04-1.10), were most strongly 
associated  with  increased  likelihood  of  subsequent  exercise. 

4

ann. behav. med. (2025) 59:1–15

Table 1. Characteristics of participants at pre-baseline (N = 13 757).a,b,c

Participant characteristics

No exercise (n = 2743)

Some exercise (n = 11 014)

No. (%)

Mean (SD)

No. (%)

Mean (SD)

Sociodemographic factors

 Age (y; range: 52-104)

 Female (%)

 Race/ethnicity (%)

 White

 Black

 Hispanic

 Other

 Married (%)

 Annual household income (%)

 <$50 000

 $50 000-$74 999

 $75 000-$99 999

 ≥$100 000

 Total wealth (%)

 1st quintile

 2nd quintile

 3rd quintile

 4th quintile

 5th quintile

 Education (%)

 <High school

 High school

 ≥College

 Employment

 In labor force

 Health insurance (%)

 Geographic region (%)

 Northeast

 Midwest

 South

 West

 Childhood abuse (%)

Health behaviors

 Frequent physical activity (%)

 Smoking (%)

 Heavy drinking (%)

 Sleep problems (%)

Physical health

72.7 (10.4)

68.4 (9.2)

1852 (67.5)

1999 (72.88)

443 (16.15)

251 (9.15)

50 (1.82)

1408 (51.33)

2086 (76.05)

309 (11.27)

143 (5.21)

205 (7.47)

912 (33.25)

642 (23.41)

534 (19.47)

348 (12.69)

307 (11.19)

875 (31.93)

1464 (53.43)

401 (14.64)

493 (17.97)

2651 (96.68)

385 (14.08)

700 (25.59)

1230 (44.97)

420 (15.36)

166 (6.24)

0 (0)

452 (16.56)

119 (5.09)

780 (54.97)

6183 (56.1)

8632 (78.38)

1315 (11.94)

837 (7.60)

229 (2.08)

7172 (65.12)

6268 (56.91)

1814 (16.47)

1032 (9.37)

1900 (17.25)

1856 (16.85)

2098 (19.05)

2213 (20.09)

2407 (21.85)

2440 (22.15)

1838 (16.73)

6039 (54.95)

3112 (28.32)

4285 (38.91)

10 519 (95.57)

1706 (15.51)

2889 (26.27)

4262 (38.75)

2142 (19.47)

682 (6.28)

9869 (89.60)

1272 (11.64)

672 (7.48)

2272 (38.96)

 Number of physical conditions (range: 0-8)

3.29 (1.51)

2.46 (1.39)

 Diabetes (%)

 Hypertension (%)

 Stroke (%)

 Cancer (%)

 Heart disease (%)

 Lung disease (%)

 Arthritis (%)

 Overweight/obese (%)

 Physical functioning limitations (%)

 Cognitive impairment (%)

 Chronic pain (%)

825 (30.08)

1897 (69.16)

409 (14.91)

497 (18.12)

989 (36.06)

476 (17.35)

1998 (72.84)

1948 (72.63)

1541 (56.18)

868 (32.59)

1405 (51.22)

1897 (17.22)

5941 (53.94)

696 (6.32)

1576 (14.31)

2362 (21.45)

822 (7.46)

6285 (57.06)

7534 (69.04)

1786 (16.22)

1833 (16.86)

3346 (30.39)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
ann. behav. med. (2025) 59:1–15

Table 1. Continued

5

Participant characteristics

No exercise (n = 2743)

Some exercise (n = 11 014)

 Self-rated health (range: 1-5)

 Hearing (range: 1-5)

 Eyesight (range: 1-6)

Psychological well-being

 Positive affect (range: 1-5)

 Life satisfaction (range: 1-7)

 Optimism (range: 1-6)

 Purpose in life (range: 1-6)

 Mastery (range: 1-6)

 Health mastery (range: 0-10)

 Financial mastery (range: 0-10)

Psychological distress

 Depression (%)

 Depressive symptoms (range: 0-8)

 Hopelessness (range: 1-6)

 Negative affect (range: 1-5)

 Perceived constraints (range: 1-6)

 Anxiety (range: 1-4)

 Trait anger (range: 1-4)

 State anger (range: 1-4)

 Cynical hostility (range: 1-6)

 Stressful life events (range: 0-5)

 Financial strain (range: 1-5)

 Daily discrimination (range: 1-6)

 Major discrimination (range: 0-6)

Social factors

 Loneliness (range: 1-3)

 Living with spouse/partner (%)

 Contact children (%)

 <very few months

 1-2×/mo

 1-2×/wk

 ≥3×/wk

 Contact other family (%)

 <Every few months

 1-2×/mo

 1-2×/wk

 ≥3×/wk

 Contact friends (%)

 <Every few months

 1-2×/mo

 1-2×/wk

 ≥3×/wk

 Closeness with spouse (range: 1-4)

 Number of close children

 Number of close other family

 Number of close friends

 Positive social support from spouse (range: 1-4)

 Positive social support from children (range: 1-4)

 Positive social support from other family (range: 1-4)

 Positive social support from friends (range: 1-4)

No. (%)

Mean (SD)

No. (%)

2.45 (1.07)

3.09 (1.13)

3.82 (1.04)

3.28 (.80)

4.55 (1.61)

4.19 (.97)

4.15 (.97)

4.3 (1.21)

6.23 (2.82)

6.83 (3.15)

720 (27.05)

1160 (10.67)

2.37 (2.32)

2.85 (1.39)

1.91 (.77)

2.72 (1.32)

1.75 (.67)

2.20 (.71)

1.54 (.58)

3.10 (1.16)

.216 (.53)

2.15 (1.11)

1.63 (.83)

.431 (.87)

1.62 (.60)

3.36 (.83)

2.94 (4.27)

3.94 (4.99)

4.04 (4.74)

3.33 (.74)

3.23 (.77)

2.86 (.90)

2.99 (.78)

1427 (53.93)

401 (15.18)

280 (10.60)

693 (26.23)

1268 (47.99)

715 (26.88)

529 (19.89)

666 (25.04)

750 (28.20)

665 (24.87)

441 (16.49)

800 (29.92)

768 (28.72)

7359 (68.65)

1442 (13.41)

1227 (11.41)

3437 (31.97)

4646 (43.21)

2552 (23.72)

2592 (24.09)

3011 (27.98)

2606 (24.22)

1600 (14.78)

2037 (18.82)

4007 (37.02)

3179 (29.37)

Mean (SD)

3.32 (1.02)

3.37 (1.07)

4.27 (.959)

3.65 (.70)

5.15 (1.40)

4.53 (.94)

4.68 (.89)

4.85 (1.06)

7.47 (2.20)

7.46 (2.49)

1.16 (1.74)

2.28 (1.24)

1.62 (.59)

2.10 (1.13)

1.52 (.55)

2.15 (.66)

1.48 (.49)

2.91 (1.12)

.231 (.55)

1.91 (.96)

1.62 (.71)

.469 (.88)

1.44 (.51)

3.50 (.71)

2.77 (3.58)

3.85 (5.69)

4.65 (6.28)

3.48 (.62)

3.28 (.70)

2.89 (.86)

3.06 (.73)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
6

Table 1. Continued

ann. behav. med. (2025) 59:1–15

Participant characteristics

No exercise (n = 2743)

Some exercise (n = 11 014)

No. (%)

Mean (SD)

No. (%)

Mean (SD)

 Social strain from spouse (range: 1-4)

 Social strain from children (range: 1-4)

 Social strain from other family (range: 1-4)

 Social strain from friends (range: 1-4)

 Religious service attendance (%)

 Not at all

 <1×/wk

 ≥1×/wk

 Volunteering (%)

 0 h/y

 1-49 h/y

 50-99 h/y

 100-199 h/y

 ≥200 h/y

 Helping friends/neighbors/relatives (%)

 0 h/y

 1-49 h/y

 50-99 h/y

 100-199 h/y

 ≥200 h/y

 Social status ladder (range: 1-10)

 Change in social status ladder (%)

 Moved down

 No change

 Moved up

Personality

 Openness (range: 1-4)

 Conscientiousness (range: 1-4)

 Extraversion (range: 1-4)

 Agreeableness (range: 1-4)

 Neuroticism (range: 1-4)

966 (35.26)

787 (28.72)

987 (36.02)

2257 (82.34)

177 (6.46)

112 (4.09)

105 (3.83)

90 (3.28)

2049 (74.84)

336 (12.27)

166 (6.06)

102 (3.73)

85 (3.10)

305 (11.84)

1987 (77.14)

284 (11.02)

2.01 (.72)

1.74 (.69)

1.58 (.65)

1.82 (.46)

1.9 (.66)

1.68 (.62)

1.56 (.60)

1.84 (.41)

2485 (22.57)

3512 (31.90)

5011 (45.52)

6660 (60.55)

1352 (12.29)

973 (8.85)

1085 (9.86)

930 (8.45)

4573 (41.66)

2875 (26.19)

1669 (15.20)

1087 (9.90)

774 (7.05)

6.05 (1.94)

6.64 (1.68)

962 (9.04)

8296 (77.94)

1386 (13.02)

2.77 (.58)

3.19 (.53)

3.01 (.59)

3.48 (.51)

2.16 (.66)

2.97 (.53)

3.39 (.45)

3.24 (.52)

3.53 (.46)

2.01 (.59)

aThis table was created based on non-imputed data.
bAll variables in this table were used as covariates, and assessed in the pre-baseline wave (t0: 2006/2008).
cThe percentages in some sections may not add up to 100% due to rounding.

Table 2. Changes in ever exercising from the pre-baseline wave (t0) to 
the outcome wave (t2).a

Pre-baseline wave (t0) Outcome wave (t2)

Ever exercise (%) Do not ever exercise (%)

Ever exercise

Do not ever exercise

75

33

25

66

aThe correlation coefficient for ever exercising between the pre-baseline 
wave (t0) and the outcome wave (t2) was 0.35.

Among  psychological  distress  factors,  perceived  constraints 
(RR = 0.94,  95%  CI = 0.92-0.98)  were  most  strongly  asso-
ciated  with  a  lower  likelihood  of  subsequent  exercise;  fur-
ther depressive symptoms, hopelessness, negative affect, and 
anxiety all had RRs = 0.96 in relation to ever exercising. For 
social  factors,  there  was  notable  evidence  that  9  out  of  22 
predictors were associated with subsequent exercise. Helping 

friends/neighbors/relatives  100-199  hours/year  (RR = 1.18, 
95% CI = 1.13-1.23) and ≥200 hours/year (RR = 1.15, 95% 
CI = 1.10-1.21),  religious  service  attendance  (>1×/week) 
(RR = 1.16, 95% CI = 1.08-1.24), and volunteering 100-199 
hours/year (RR = 1.13, 95% CI = 1.07-1.20) and ≥200 hours/
year  (RR = 1.13,  95%  CI = 1.07-1.19)  were  most  strongly 
associated  with  increased  likelihood  of  subsequent  exercise. 
Finally,  being  in  the  labor  force  was  not  notably  associated 
with subsequent exercise.

Additional analyses
E-values indicated that many of the observed associations were 
potentially  moderately  robust  to  unmeasured  confounding 
(Table  4).  For  example,  for  purpose  in  life,  an  unmeasured 
confounder that was associated with both ever exercising and 
purpose in life by RRs of 1.36 each (above and beyond the 
covariates already adjusted for) could explain away the asso-
ciation, but weaker joint confounder associations could not. 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
ann. behav. med. (2025) 59:1–15

7

Figure 1. Likelihood of exercise participation based on candidate predictors. Values greater than 1 indicate a higher likelihood of participating in at least 
some exercise, and vice versa. CIs that include 1.0 indicate that a predictor is not statistically significant at the 5% level. Exercise was not included as a 
predictor (2010/2012), but they can be found in Table 2, which also includes a detailed explanation of the analyses.

Furthermore, to shift the CI to include the null, an unmeas-
ured  confounder  associated  with  both  ever  exercising  and 
purpose in life by RRs of 1.25 each could explain away the 
association, but weaker joint confounder associations could 
not. This particular association is thus at least moderately ro-
bust to potential unmeasured confounding. However, in other 
cases,  a  combination  of  unmeasured  confounding  and  stat-
istical uncertainty might suffice to explain away the results.

Discussion
In  this  study,  we  investigated  putative  determinants  of 
engaging  in  at  least  some  exercise  among  adults  aged  over 

50 in the United States by examining 62 candidate predictors 
spanning  health  behaviors,  physical  health,  psychological 
factors,  social  factors,  and  employment.  Some  factors  were 
robustly  associated  with  subsequent  physical  activity.  The 
factors  that  most  strongly  predicted  decreased  likelihoods 
of subsequent exercise were physical functioning limitations, 
stroke, and lung disease. The factors that most strongly pre-
dicted an increased likelihood of subsequent exercise were re-
ligious service attendance, volunteering, and helping friends, 
neighbors, and relatives.

Our findings align with previous research, which has con-
sistently demonstrated that exercise participation (eg, volume 
or  frequency)  is  influenced  by  higher  positive  psychological 

8

ann. behav. med. (2025) 59:1–15

Table 3. Candidate predictors of exercise (Health and Retirement Study [HRS]: N = 13 771).a,b,c

Candidate predictor

Health behaviors
 Ever exercise
 Smoking
 Heavy drinking
 Sleep problems

Physical health

 Number of physical conditions

 Diabetes
 Hypertension
 Stroke
 Cancer
 Heart disease
 Lung disease
 Arthritis
 Overweight/obese

 Physical functioning limitations
 Cognitive impairment
 Chronic pain
 Self-rated health
 Hearing
 Eyesight

Psychological well-being

 Positive affect
 Life satisfaction
 Optimism
 Purpose in life
 Mastery
 Health mastery
 Financial mastery
Psychological distress

 Depression
 Depressive symptoms
 Hopelessness
 Negative affect
 Perceived constraints
 Anxiety
 Trait anger
 State anger
 Cynical hostility
 Stressful life events
 Financial strain
 Daily discrimination
 Major discrimination

Social factors
 Loneliness
 Living with spouse
 Contact children

 <Every few months
 1-2×/mo
 1-2×/wk

 ≥3×/wk

 Contact other family
 <Every few months
 1-2×/mo
 1-2×/wk
 ≥3×/wk

RR

1.86
1.04
1.00
1.00

0.93
0.98
0.96
0.78
0.94
0.93
0.85
0.99
0.99
0.75
0.88
0.93
1.13
1.02
1.02

1.07
1.05
1.02
1.08
1.06
1.09
1.04

0.93
0.96
0.96
0.96
0.94
0.96
1.00
0.98
0.98
1.00
1.00
1.00
1.00

0.97
0.99

Reference
1.01
1.08
1211wdq
1.06

Reference
1.05
1.03
1.02

95% CI

1.73-2.01***
0.95-1.13
0.94-1.07
0.93-1.06

0.89-0.97**
0.90-1.07
0.91-1.01
0.64-0.96*
0.87-1.00
0.87-0.99*
0.76-0.96**
0.93-1.05
0.94-1.04
0.70-0.80***
0.83-0.94**
0.90-0.95***
1.11-1.16***
1.01-1.04
1.01-1.04**

1.04-1.10***
1.03-1.07***
1.00-1.05
1.05-1.10***
1.04-1.08***
1.07-1.12***
1.01-1.07*

0.84-1.04
0.92-0.99*
0.93-0.99*
0.93-0.99**
0.92-0.98**
0.94-0.98**
0.98-1.02
0.95-1.00
0.96-1.00
0.98-1.02
0.98-1.01
0.98-1.03
0.98-1.02

0.95-0.99**
0.94-1.05

Reference
0.95-1.07
1.00-1.15*

0.98-1.15

Reference
1.01-1.09*
1.00-1.07
0.98-1.07

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
ann. behav. med. (2025) 59:1–15

Table 3. Continued

Candidate predictor

 Contact friends

 <Every few months

 1-2×/mo

 1-2×/wk

 ≥3×/wk

 Closeness with spouse

 Number of close children

 Number of close other family

 Number of close friends

 Positive social support from spouse

 Positive social support from children

 Positive social support from other family

 Positive social support from friends

 Social strain from spouse

 Social strain from children

 Social strain from other family

 Social strain from friends

 Volunteer

 0 h/y

 0-49 h/y

 50-99 h/y

 100-199 h/y

 ≥200 h/y

 Helping friends/neighbors/relatives

 0 h/y

 1-49 h/y

 50-99 h/y

 100-199 h/y

 ≥200 h

 Religious service attendance

 Not at all

 <1×/wk

 ≥1×/wk

 Social status ladder

 Change in social status ladder

 Moved down

 No change

 Moved up

Work

 In labor force

RR

Reference

1.04

1.08

1.07

0.99

1.01

1.01

1.01

1.01

1.01

1.02

1.00

1.01

0.99

1.00

1.01

Reference

1.05

1.10

1.13

1.13

Reference

1.14

1.16

1.18

1.15

Reference

1.09

1.16

1.00

Reference

1.04

1.02

1.01

9

95% CI

Reference

0.98-1.12

1.02-1.15*

1.00-1.14

0.95-1.03

1.00-1.03

0.99-1.02

0.99-1.03

0.98-1.05

0.99-1.03

1.00-1.03*

0.98-1.04

0.98-1.03

0.97-1.01

0.98-1.02

0.99-1.03

Reference

1.01-1.09**

1.05-1.14***

1.07-1.20***

1.07-1.19***

Reference

1.10-1.17***

1.11-1.20***

1.13-1.23***

1.10-1.21***

Reference

1.05-1.13***

1.08-1.24***

0.99-1.02

Reference

1.00-1.08*

0.96-1.08

0.99-1.04

Abbreviation: RR, risk ratio.
aThe analytic sample was restricted to those who had participated in the pre-baseline wave (2006 or 2008). Multiple imputation was performed to impute 
missing data on the exposures, covariates, and outcomes. Candidate antecedents were assessed, one at a time, in wave 2 (2010/2012), and the outcome 
(ever exercise) was assessed in wave 3 (2014/2016). The following covariates were controlled for at wave 1 (2006/2008): sociodemographic characteristics 
(age, sex, race/ethnicity, marital status, income, total wealth, level of education, employment status, health insurance, and geographic region), childhood 
abuse, personality factors (openness, conscientiousness, extraversion, agreeableness, and neuroticism), and all of the predictor variables, including health 
behaviors (ever exercise, smoking, heavy drinking, and sleep problems), physical health (heart disease, cancer, stroke, arthritis, hypertension, overweight/
obese, diabetes, lung disease, chronic pain, hearing, eyesight, self-rated health, physical functioning limitations, and cognitive impairment), social factors 
(living with spouse, frequency of contact with children, frequency of contact with other family, frequency of contact with friends, loneliness, closeness 
with spouse, number of close children, number of close other family, number of close friends, positive social support from spouse, positive social support 
from children, positive social support from friends, positive social support from other family, social strain from spouse, social strain from children, social 
strain from other family, social strain from friends, religious service attendance, volunteering, helping friends/neighbors/relatives, perceived social status, 
and change in perceived social status), psychological well-being factors (life satisfaction, positive affect, purpose in life, optimism, health mastery, financial 
mastery, and mastery), psychological distress (depressive symptoms, hopelessness, negative affect, perceived constraints, anxiety, trait anger, state anger, 
daily discrimination, major discrimination, cynical hostility, stressful life events, and financial strain), work (in labor force), and baseline values of the 
outcome (ever exercise).
bAll continuous candidate antecedents were standardized (mean = 0; SD = 1).
cAn exposure-wide analytic approach was used, and a separate model for each exposure was run.
*P < .05 before Bonferroni correction;
**P < .01 before Bonferroni correction;
***P < .05 after Bonferroni correction (the P value cutoff for Bonferroni correction is P = .05/62 predictors = P < .0.00080645161).

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
10

ann. behav. med. (2025) 59:1–15

Table 4. Robustness to unmeasured confounding (E-values) for the 
associations between candidate predictors and subsequent exercise 
(N = 13 771).a

Table 4. Continued

Effect estimateb

CI limitc

 1-2×/mo
 1-2×/wk
 ≥3×/wk

 Contact friends

Effect estimateb

CI limitc

1.28
1.22
1.18

1
1
1

Health behaviors

 Frequent physical activity
 Smoking
 Heavy drinking
 Sleep problems

Physical health

3.13
1.23
1.06
1.07

 Number of physical conditions

 Diabetes
 Hypertension
 Stroke
 Cancer
 Heart disease
 Lung disease
 Arthritis
 Overweight/obese

1.37
1.16
1.26
1.87
1.34
1.37
1.62
1.10
1.12
 Physical functioning limitations 2.00
1.52
 Cognitive impairment
1.38
 Chronic pain
1.52
 Self-rated health
1.18
 Hearing
1.18
 Eyesight

1.35
1.28
1.17
1.36
1.30
1.41
1.23

1.34
1.27
1.24
1.25
1.30
1.25
1.03
1.18
1.14
1.02
1.07
1.05
1.05

1.20
1.11

Psychological well-being

 Positive affect
 Life satisfaction
 Optimism
 Purpose in life
 Mastery
 Health mastery
 Financial mastery
Psychological distress

 Depression
 Depressive symptoms
 Hopelessness
 Negative affect
 Perceived constraints
 Anxiety
 Trait anger
 State anger
 Cynical hostility
 Stressful life events
 Financial strain
 Daily discrimination
 Major discrimination

Social factors
 Loneliness
 Living with spouse
 Contact children

 <Every few months
 1-2×/mo
 1-2×/wk
 ≥3×/wk

 Contact other family
 <Every few months

2.81
1
1
1

1.15
1
1
1.19
1
1
1.10
1
1
1.76
1.26
1.18
1.43
1
1

1.23
1.15
1
1.25
1.19
1.31
1.06

1
1.07
1.05
1.08
1.15
1.12
1
1
1
1
1
1
1

1
1

 <Every few months

Reference

Reference

 1-2×/mo

 1-2×/wk

 ≥3×/wk

 Closeness with spouse

 Number of close children

 Number of close other family

 Number of close friends

 Positive social support from 
spouse

 Positive social support from 
children

 Positive social support from 
other family

 Positive social support from 
friends

 Social strain from spouse

 Social strain from children

 Social strain from other family

 Social strain from friends

1.26

1.37

1.34

1.11

1.14

1.08

1.11

1.12

1.12

1.15

1.10

1.08

1.10

1.09

1.04

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

 Volunteer

 0 h/y

 0-49 h/y

 50-99 h/y

 100-199 h/y

 ≥200 h/y

Reference

Reference

1.28

1.43

1.52

1.51

1

1.12

1.22

1.15

 Helping friends/neighbors/relatives

 0 h/y

 1-49 h/y

 50-99 h/y

 100-199 h/y

 ≥200 h

 Religious service attendance

 Not at all

 <×/wk

 ≥1×/wk

 Social status ladder

 Change in social status ladder

 Moved down

 No change

 Moved up

Work

 In labor force

Reference

Reference

1.53

1.58

1.63

1.58

1.35

1.36

1.37

1.25

Reference

Reference

1.40

1.59

1.07

1.17

1.31

1

Reference

Reference

1.25

1.16

1.11

1

1

1

Reference
1.11
1.36
1.31

Reference
1
1
1

Reference

Reference

aSee VanderWeele and Ding45 for the formula for calculating E-values.
bThe E-values for effect estimates are the minimum strength of association 
on the risk ratio scale that an unmeasured confounder would need to have 
with both the exposure and the outcome to fully explain away the observed 
association between the exposure and outcome, conditional on the measured 
covariates.
cThe E-values for the limit of the 95% CI closest to the null denote the 
minimum strength of association on the risk ratio scale that an unmeasured 
confounder would need to have with both the exposure and the outcome to 
shift the CI to include the null value, conditional on the measured covariates.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
ann. behav. med. (2025) 59:1–15

11

well-being46,47  and  social  factors,48  as  well  as  reduced  psy-
chological  stress.49  Regarding  potentially  novel  exercise 
determinants, it is worth highlighting that some of the eude-
monic psychological well-being factors (eg, sense of purpose, 
volunteering,  and  religious  service  attendance)  were  associ-
ated  with  higher  exercise  levels.  A  predominant  human  in-
clination is to pursue pleasure and avoid pain as proposed by 
Epicurus,  reiterated  by  Bentham,  and  empirically  confirmed 
by Kahneman et al.50,51 The reluctance of most individuals to 
engage in exercise can be attributed to the fact that the ex-
perience of exercising is typically perceived as less pleasurable 
during (vs after) the activity.24,52,53 In this light, a common un-
measured factor that may increase exercise level—as well as 
purpose in life, volunteering, and religious activities—may be 
one’s  willingness  or  behavioral  tendency  to  engage  in  som-
atically  unpleasant  but  meaningful  activities.  Potentially  re-
lated, in our results, behavioral (vs psychological) phenotypes 
tend  to  show  higher  effect  sizes.  For  instance,  subfactors  of 
psychological  well-being  predict  exercise  participation  with 
small effect sizes (RR = 1.02-1.09), while behavioral pheno-
types like helping others, volunteering, and religious attend-
ance show effect sizes around RR = 1.09-1.18. Older adults 
who have lower neural conflict when making eudaimonically 
(vs  hedonically)  good  decisions  may  succeed  in  practicing 
their ideas (eg, knowledge and beliefs) behaviorally. For ex-
ample,  in  a  functional  magnetic  resonance  imaging  study 
with 220 sedentary and overweight young adults, those with 
a higher sense of purpose had reduced cognitive conflict when 
exposed to health messages about physical activity.54 It is im-
portant to note that eudemonic psychological well-being and 
exercise appear to have a reciprocal relationship,55,56 and un-
measured  third  variables  could  account  for  some  of  the  re-
lations  between  eudaimonic  psychological  well-being  and 
physical  activity. A  prior  randomized  controlled  experiment 
has shown that those whose gym attendance was incentivized 
by  charitable  donations  on  their  behalf  made  12  additional 
visits to the YMCA over a month, compared with those in the 
control  condition  who  only  received  reminder  emails  about 
their gym attendance.57 This suggests that enhancing meaning 
and purpose may have a causal impact on enhanced exercise 
behavior.

It  is  important  to  emphasize  that  our  exposure-wide  ap-
proach aims to generate hypotheses rather than conduct formal 
hypothesis testing. This method has proven highly successful 
in human genetics, particularly in the context of genome-wide 
association  studies,  leading  to  transformative  advancements 
in  the  past  decade.  Notably,  because  one’s  genetic  profile  is 
determined before all behavioral phenotypes, genetics enjoys 
an  advantage  of  aligned  temporality  between  exposure  and 
outcome. Moreover, except for ancestral history, there is no 
conceptual  confounder  that  can  have  a  causal  influence  on 
both genotype (ie, allele frequency within a population) and 
phenotype.  However,  in  non-genetic  research,  these  condi-
tions are seldom met.31 Thus, despite our efforts to mitigate 
confounding  through  robust  covariate  adjustment,  longitu-
dinal design, and E-value analyses, our exposure-wide results 
should be considered hypothesis-generating. Therefore, newly 
identified factors warrant further investigation in studies pro-
viding stronger causal inferences (eg, randomized controlled 
trials); and then, studies examining the feasibility of engaging 
the intervention target.58 Finally, an exposure-wide approach 
for  understanding  exercise  determinants  can  be  applied  to 
other  populations  with  different  sociodemographic  back-
grounds (eg, age and country).

One  crucial  aspect  often  overlooked  within  our  theoret-
ical framework of exercise determinants is health condition. 
Physical  and  mental  capabilities  are  posited  as  an  influence 
in  some  models  of  behavior  change such  as  COM-B  model 
(Capability,  Motivation,  Opportunity-Behavior),59  but  cap-
abilities  are  not  addressed  in  widely  used  explanatory  the-
oretical  models  of  health  behavior  motivation.  Indeed,  we 
found  that  medical  conditions,  such  as  physical  functioning 
limitations, stroke, and lung disease were strong determinants 
of subsequent exercise behavior. As the global population of 
older adults continues to grow, an increasing number of indi-
viduals will be grappling with a spectrum of underlying health 
issues. This demographic shift underscores the escalating need 
to place greater emphasis on tertiary prevention efforts among 
older populations who tend to have underlying illnesses. For 
example,  studies  aimed  at  enhancing  exercise  levels  after 
treating underlying illnesses using pharmaceutical or surgical 
treatment may become increasingly pertinent. Future studies 
may  aim  to  integrate  treatment  with  subsequent  rehabilita-
tion  efforts,  such  as  physical  therapy  and  personal  training, 
particularly  for  older  adults.  This  approach  not  only  pro-
motes  physical  recovery  but  also  improves  overall  health 
outcomes  by  ensuring  that  treatment  transitions  seamlessly 
into  effective  rehabilitation. Additionally,  exploring  innova-
tive strategies to integrate exercise promotion programs into 
hospitals and rehabilitation programs for older adults may be 
a promising avenue for maximizing the utility of exercise for 
the  population’s  health.  For  instance,  wearable  technologies 
and AI-driven systems offer the potential for highly personal-
ized exercise regimens for the elderly, going beyond biological 
factors (eg, age, weight, and blood pressure) to consider older 
adults’ behavioral patterns (eg, hospital visit schedule, mood 
fluctuations,  daily  routines,  and  seasonal  variations).60–62 
Connecting  these  technologies  to  the  hospital’s  web  portal 
may  enrich  the  physician–patient  experience  and  ultimately 
improve tertiary prevention efforts among older populations 
with underlying illnesses.

All the effect sizes in this study are considered small. For 
reference,  in  epidemiologic  studies,  relative  risk  values  of 
1.22,  1.86,  and  3.00  are  interpreted  as  small,  medium,  and 
large  effect  sizes,  respectively.63  Moreover,  exercise  partici-
pation  was  influenced  by  a  multitude  of  factors,  each  with 
modest  effects,  in  line  with  a  common  pattern  observed  in 
other exposure-wide approaches, such as genome association 
studies. Moreover, in line with the socioecological model, our 
findings ascertained that exercise behavior in older adults is 
influenced by numerous determinants, highlighting the com-
plexity of this relationship. Relatedly, recent advances in poly-
exposure  scores,  which  combine  numerous  small  effects  of 
each exposure into a cumulative score, may enable researchers 
to  more  effectively  and  confidently  identify  subpopulations 
predisposed  to  low  levels  of  exercise,  especially  when  these 
scores  include  factors  that  are  difficult  or  impossible  to 
change,  such  as  genetics  and  the  built  environment.  While, 
poly-approaches,  such  as  poly-exposure  scores  or  genetic 
risk  scores,  are  effective  in  predicting  behaviors,  they  have 
limited utility for changing behaviors. Thus, the factors that 
are  fixed  or  unmodifiable  may  be  used  to  identify  high-risk 
populations for targeted interventions, while modifiable fac-
tors  may  be  further  examined  as  the  target  of  an  interven-
tion. Future intervention studies aimed at changing behaviors 
among high-risk populations based on a poly-exposure score 
approach  could  explore  strategies  for  integrating  multiple 
intervention  targets  within  a  single  trial.  Such  interventions 

12

ann. behav. med. (2025) 59:1–15

may encompass the targeting of psychological and social de-
terminants,  the  attenuation  of  risk  factors  (eg,  depression), 
the enhancement of health assets (eg, social engagement and 
volunteering),  and  the  integration  of  pharmaceutical  treat-
ments.  Notably,  advanced  intervention  frameworks  such  as 
Multiphase  Optimization  Strategy64  and  Behavior  Change 
Taxonomy65  may  serve  as  effective  guidance  for  translating 
big-data-driven  poly-exposure  approaches  into  personalized 
behavioral interventions.

Our study has some limitations. First, exercise phenotype 
was self-reported, which is susceptible to bias. While the ac-
curacy may be low in assessing the exact volume of exercise, 
it  is  likely  accurate  in  distinguishing  whether  someone  en-
gages  in  exercise  or  not.  Relatedly,  we  lacked  a  measure  of 
duration,  which  is  expected  to  vary  across  individuals  who 
exercise,  and  the  factors  that  distinguish  no  activity  from 
some activity may not be the same as those that predict ac-
tivity duration. Second, our study did not address how pre-
dictors of exercise differ by key factors, such as age, gender, 
or  socioeconomic  status  that  often  modify  exposure’s  effect 
on  physical  activity.26,66  Third,  although  the  analyses  were 
conducted  systematically  using  an  exposure-wide  approach, 
the  selection  of  candidate  predictors,  covariates,  outcome, 
and their operationalizations was informed by our expertise 
in social epidemiology, exercise science, and behavioral medi-
cine, thereby introducing a degree of subjectivity. Related, the 
present study was not pre-registered. However, our team has 
consistently  published  exposure-wide  studies  using  nearly 
identical predictors and covariates.32–34 Fourth, while we as-
sumed that covariates measured at pre-baseline would remain 
stable, this assumption may not be warranted, and could af-
fect the effect sizes observed. Finally, each exposure examined 
can be correlated. Despite potential collinearity, we intention-
ally analyzed individual exposures separately (while control-
ling  for  numerous  other  potential  confounders  in  the  prior 
wave) as we sought to understand each factor’s independent 
contribution,  aligning  with  the  goal  of  generating  hypoth-
eses for potential intervention in exposure-wide approaches. 
However,  future  research  aimed  at  building  a  predictive 
model  may  incorporate  additional  multivariate  or  machine 
learning methods, such as random forest or lasso regression, 
to  further  address  variable  correlations  and  refine  predictor 
selection.67–70 Finally, the majority of HRS participants were 
White. Future research should validate these predictors in a 
more  diverse  population  and  incorporate  additional  expos-
ures  related  to  social  determinants  of  health,  such  as  food 
and  housing  insecurity,  neighborhood  safety,  and  financial 
stress. The  current  study  also  has  several  notable  strengths. 
First, to our knowledge, this is the first exposure-wide study 
to  examine  determinants  of  exercise  behavior.  We  investi-
gated  many  novel  predictors  that  are  understudied  or  not 
previously  studied,  and  also  evaluated  all  predictors  within 
the same study, allowing us to compare effect sizes. Second, 
our study has high generalizability from using a nationwide 
dataset of older adults in the United States.

Conclusion
Using  an  exposure-wide  approach  in  a  prospective  cohort 
study  of  older  US  adults,  we  have  identified  a  critical  over-
sight  within  our  theoretical  framework  of  exercise  deter-
minants: physical health conditions, such as stroke and lung 
disease.  Given  the  growing  population  of  older  adults,  it  is 

prudent for funding agencies to allocate increased resources 
for tertiary prevention related to exercise. Furthermore, aca-
demic societies may foster discussions on tertiary prevention 
initiatives,  particularly  in  the  context  of  exercise,  to  stimu-
late greater research endeavors aimed at promoting exercise 
among older adults with health challenges.

We  have  identified  potentially  novel  exercise  determin-
ants  that  do  not  align  neatly  with  existing  theories  of  exer-
cise  behavior,  namely  helping  friends/neighbors/relatives, 
volunteering,  religious  attendance,  and  purpose  in  life.  A 
common underlying factor that enables exercise participation 
as  well  as  these  eudemonic  elements  may  be  one’s  willing-
ness  or  behavioral  tendency  to  engage  in  somatically  un-
pleasant  but  meaningful  activities.  Putting  this  observation 
into a broader context, modern humans enjoy unprecedented 
somatic comfort (eg, entertainment at our fingertips, modern 
climate  control  technologies,  labor-saving  household  appli-
ances, online shopping, and food delivery services), thanks to 
scientific  advancements  and  technological  innovations,  with 
even more advancements on the horizon. With this prospect, 
the  significance  of  eudemonic  elements  and  their  impact  on 
public health might gain greater importance.

Finally,  while  the  aforementioned  eudemonic  elements 
need  to  be  further  scrutinized  with  study  designs  with 
stronger  causal  inferences,  we  demonstrate  the  potential 
of the exposure-wide approach for uncovering novel deter-
minants  of  exercise  behavior  within  specific  populations. 
Thus,  adopting  similar  exposure-wide  methodologies  in 
diverse large-scale cohorts with varying sociodemographic 
characteristics  holds  promise  for  identifying  additional 
yet  unexplored  factors  influencing  exercise  behavior.  In 
translating  exposure-wide  studies  to  intervention  devel-
opment, the factors that are fixed or unmodifiable may be 
used  to  identify  high-risk  populations  for  targeted  inter-
ventions,  while  modifiable  factors  may  be  further  exam-
ined  as  the  target  of  an  intervention.  Such  a  data-driven 
approach could further refine existing health behavior the-
ories,  similar  to  how  theoretical  research  in  exercise  mo-
tivation  in  the  past  later  contributed  to  the  development 
of the socioecological framework. In particular, considering 
the  contemporary  landscape  of  behavioral  and  social  sci-
ences, in which most research participants are Eurocentric 
and  over-represent  well-educated,  high-income  people  on 
a  global  scale,71  nationally  representative  survey  data,  es-
pecially  from  non-Western  countries,  can  make  valuable 
contributions to theoretical frameworks in behavioral and 
social  sciences.  Future  exposure-wide  studies  in  more  di-
verse  and  representative  samples  will  enhance  the  gen-
eralizability  of  findings  and  can  lead  to  a  more  nuanced 
refinement  of  theories  of  human  behavior  across  different 
cultural and socioeconomic contexts worldwide.

Acknowledgments
We extend our appreciation to Brianna Sutara and Geoffrey 
Sandhanamudi  for  their  contributions  in  developing  the 
tables for this study.

Funding
Health and Retirement Study is conducted by the Institute for 
Social  Research  at  the  University  of  Michigan,  with  grants 

ann. behav. med. (2025) 59:1–15

13

from the National Institute on Aging (U01AG09740) and the 
Social Security Administration.

posure of A1 = a0 in 2010/2012, will give rise to an effect on 
the risk ratio scale of:

Author contributions
Harold  H.  Lee  (Conceptualization  [lead],  Writing—ori-
ginal  draft  [equal],  Writing—review  &  editing  [lead]),  Eric 
S.  Kim  (Formal  analysis  [lead],  Writing—original  draft 
[equal],  Writing—review  &  editing  [equal]),  Younseo  Kim 
(Visualization  [lead],  Writing—review  &  editing  [sup-
porting]), David E. Conroy (Conceptualization [supporting], 
Writing—review  &  editing  [supporting]),  and  Tyler  J. 
VanderWeele 
[lead],  Writing—review  & 
editing [supporting])

(Methodology 

Conflicts of interest
Tyler  J.  VanderWeele  reports  receiving  personal  fees  from 
Flerish Inc. and Flourishing Metrics. Others have no conflicts 
of interest to report.

Ethical standards
The ethics board at Penn State University exempted our study 
from review because it used de-identified and publicly avail-
able data.

Study registration
This study was not formally registered.

Analytic plan pre-registration
The analysis plan was not formally pre-registered.

Data availability
Data are publicly available through the Health and Retirement 
Study (http://hrsonline.isr.umich.edu/). Documentation, code, 
and other materials are available upon request.

Appendix Text 1
Proof illustrating how adjusting for pre-baseline levels of ex-
posure can help us evaluate how “changes” in exposure are 
associated with subsequent ever exercising over time

Let Y be the ever exercising outcome in 2014/2016, A1 the 
exposure  under  consideration  in  2010/2012,  A0  the  prior 
level  of  exposure  in  2006/2008,  and  C  the  set  of  all  other 
covariates in 2006/2008.

|

|

}

{

{

P [Y = 1

P [Y = 1

a0, a1, c]

the  regression  model 

For  a  binary  outcome, 
a0, a1, c]

is: 
= v + b0a0 + b1a1 + b(cid:31)2c, which, if the 
log
outcome is rare can be approximated by a logistic regression 
= v + b0a0 + b1a1 + b(cid:31)2c,  or, 
model,  logit
}
if the outcome is common, by a modified Poisson model. Let 
Ya  denote  the  potential  outcome  Y  for  an  individual  under 
an  intervention  to  set  A1  to  a.  For  an  individual  with  base-
line exposure A0 = a0 and covariates c in 2006/2008, under 
the  no-confounding  (and  positivity  and  consistency)  and 
modeling assumptions, a change in exposure of d points A0 
= a0 to A1 = a0 + d in 2010/2012, rather than maintaining ex-

A0 = a0, c]

A0 = a0, c] /P [Ya0 = 1
|
A1 = a0 + d, A0 = a0, c] /P [Ya0 = 1

P [Ya0+d = 1
|
= P [Ya0+d = 1
= P [Y = 1
A1 = a0, A0 = a0, c]
= exp [v + b0a0 + b1 (a0 + d) +b (cid:31)2c] /exp [v + b0a0 + b1a0 + b(cid:31)2c]
= exp (b1d)

A1 = a0 + d, A0 = a0, c] /P [Y = 1

|

|

|

|

A1 = a0, A0 = a0, c]

where the first equality follows by the no-confounding as-
sumption, the second by consistency, and the third by the stat-
istical model.

References
1.  Vagetti GC, Barbosa Filho VC, Moreira NB, Oliveira V, Mazzardo 
O,  Campos W. Association  between  physical  activity  and  quality 
of life in the elderly: a systematic review, 2000–2012. Braz J Psy-
chiatry  2014;36:76-88.  https://doi.org/10.1590/1516-4446-2012-
0895

2.  Heyn P, Abreu BC, Ottenbacher KJ. The effects of exercise training 
on  elderly  persons  with  cognitive  impairment  and  dementia:  a 
meta-analysis.  Arch  Phys  Med  Rehabil.  2004;85:1694-1704. 
https://doi.org/10.1016/j.apmr.2004.03.019

3.  Paterson DH, Jones GR, Rice CL. Ageing and physical activity: ev-
idence to develop exercise recommendations for older adults. Appl 
Physiol  Nutr  Metab.  2007;32:S69-S108.  https://doi.org/10.1139/
h07-111

4.  DiPietro L. Physical activity in aging: changes in patterns and their 
relationship  to  health  and  function.  J  Gerontol  A  Biol  Sci  Med 
Sci. 2001;56 Spec No 2:13-22. https://doi.org/10.1093/gerona/56.
suppl_2.13

5.  King  AC,  King  DK.  Physical  activity  for  an  aging  population. 
Public  Health  Rev.  2010;32:401-426.  https://doi.org/10.1007/
bf03391609

6.  Committee  PAGA.  2018  Physical  Activity  Guidelines  Advisory 
Committee Scientific Report. US Department of Health and Human 
Services; 2018.

7.  Luke A, Dugas LR, Durazo-Arvizu RA, Cao G, Cooper RS. Assessing 
physical activity and its relationship to cardiovascular risk factors: 
NHANES 2003-2006. BMC Public Health. 2011;11:1-11.

8.  Troiano RP, Berrigan D, Dodd KW, Masse LC, Tilert T, McDowell 
M. Physical activity in the United States measured by accelerometer. 
Med  Sci  Sports  Exerc.  2008;40:181-188.  https://doi.org/10.1249/
mss.0b013e31815a51b3

9.  Ansah JP, Chiu C-T, Chiu C-T. Projecting the chronic disease burden 
among the adult population in the United States using a multi-state 
population model. Front Public Health. 2023;10:1082183. https://
doi.org/10.3389/fpubh.2022.1082183

10.  Colby  SL,  Ortman  JM.  Projections  of  the  Size  and  Composition 
of  the  US  Population:  2014  to  2060.  Population  Estimates  and 
Projections.  Current  Population  Reports.  P25-1143.  US  Census 
Bureau; 2015.

11.  Bull  FC,  Al-Ansari  SS,  Biddle  S,  et  al.  World  Health  Organiza-
tion  2020  guidelines  on  physical  activity  and  sedentary  behaviour. 
Br  J  Sports  Med.  2020;54:1451-1462.  https://doi.org/10.1136/
bjsports-2020-102955

12.  U.S. Department of Health and Human Services. Physical Activity 
Guidelines  for  Americans. 2nd  ed.  Washinton,  DC: U.S.  Depart-
ment of Health and Human Services; 2018.

13.  Liguori  G.  ACSM’s  Guidelines  for  Exercise Testing  and  Prescrip-

tion. Lippincott Williams & Wilkins; 2020.

14.  Stamatakis E, Ahmadi MN, Friedenreich CM, et al. Vigorous intermit-
tent lifestyle physical activity and cancer incidence among nonexercising 
adults:  the  UK  Biobank  Accelerometry  Study.  JAMA  Oncol. 
2023;9:1255-1259. https://doi.org/10.1001/jamaoncol.2023.1830
15.  Wengström  Y,  Fornander  T,  Lindström  LS.  Short  bouts  of  phys-
ical  activity—good  for  health?  JAMA  Oncol.  2023;9:1199-1201. 
https://doi.org/10.1001/jamaoncol.2023.1810

14

ann. behav. med. (2025) 59:1–15

16.  Plato. Plato’s Parmenides. Oxford University Press; 360 BCE/1991.
17.  Bacon F. Novum Organum. Clarendon Press; 1878.
18.  Sallis JF, Simons-Morton BG, Stone EJ, et al. Determinants of phys-
ical  activity  and  interventions  in  youth.  Med  Sci  Sports  Exerc. 
1992;24:248-257.

19.  Dishman RK, Sallis JF, Orenstein DR. The determinants of physical 

activity and exercise. Public Health Rep. 1985;100:158-171.

20.  Sallis  JF,  Hovell  MF,  Hofstetter  CR.  Predictors  of  adoption  and 
maintenance of vigorous physical activity in men and women. Prev 
Med. 1992;21:237-251. https://doi.org/10.1016/0091-7435(92)90 
022-a

21.  Marcus BH, Williams DM, Dubbert PM, et al.; American Heart As-
sociation Council on Nutrition, Physical Activity, and Metabolism 
(Subcommittee on Physical Activity). Physical activity intervention 
studies:  what  we  know  and  what  we  need  to  know:  a  scientific 
statement  from  the American  Heart Association  Council  on  Nu-
trition, Physical Activity, and Metabolism (Subcommittee on Phys-
ical  Activity);  Council  on  Cardiovascular  Disease  in  the  Young; 
and the Interdisciplinary Working Group on Quality of Care and 
Outcomes  Research.  Circulation.  2006;114:2739-2752.  https://
doi.org/10.1161/CIRCULATIONAHA.106.179683

22.  Williams DM, Marcus BH. Theoretical approaches to exercise pro-
motion.  In: Acevedo  EO,  ed.  The  Oxford  Handbook  of  Exercise 
Psychology. Oxford University Press; 2012:241:chap 13.

23.  Liao Y, Shonkoff ET, Dunton GF. The acute relationships between 
affect, physical feeling states, and physical activity in daily life: a re-
view of current evidence. Front Psychol. 2015;6:1975. https://doi.
org/10.3389/fpsyg.2015.01975

24.  Lee HH, Emerson JA, Williams DM. The exercise–affect–adherence 
pathway: an evolutionary perspective. Front Psychol. 2016;7:1285. 
https://doi.org/10.3389/fpsyg.2016.01285

25.  Conroy DE, Hyde AL, Doerksen SE, Ribeiro NF. Implicit attitudes 
and explicit motivation prospectively predict physical activity. Ann 
Behav  Med.  2010;39:112-118.  https://doi.org/10.1007/s12160-
010-9161-0

26.  Lee HH, Pérez AE, Operario D. Age moderates the effect of soci-
oeconomic  status  on  physical  activity  level  among  south  Korean 
adults: cross-sectional analysis of nationally representative sample. 
BMC Public Health. 2019;19:1-8.

27. Anderson-Bill  ES,  Winett  RA,  Wojcik  JR,  Williams  DM. 
Aging  and  the  social  cognitive  determinants  of  physical  ac-
tivity  behavior  and  behavior  change:  evidence  from  the  guide 
to  health  trial.  J  Aging  Res.  2011;2011:505928.  https://doi.
org/10.4061/2011/505928

28.  Lee  HH,  Dunsiger  S,  Connell  Bohlen  L,  Boyle  HK,  Emerson  JA, 
Williams  DM. Age  moderates  the  effect  of  self-paced  exercise  on 
exercise  adherence  among  overweight  adults.  J  Aging  Health. 
2020;32:154-161. https://doi.org/10.1177/0898264318812139
29.  Ioannidis  JP.  Exposure‐wide  epidemiology:  revisiting  Bradford 
Hill.  Stat  Med.  2016;35:1749-1762.  https://doi.org/10.1002/
sim.6825

30.  VanderWeele TJ, Mathur MB, Chen Y. Outcome-wide longitudinal 
designs for causal inference: a new template for empirical studies. 
Statist Sci. 2020;35: 437-466.

31. VanderWeele  TJ.  Outcome-wide  epidemiology.  Epidemiology. 
2017;28:399-402.  https://doi.org/10.1097/EDE.000000000000 
0641

32.  Chen Y, Kim ES, Shields AE, VanderWeele TJ. Antecedents of pur-
pose in life: evidence from a lagged exposure-wide analysis. Cogent 
Psychol.  2020;7:1825043.  https://doi.org/10.1080/23311908.202
0.1825043

33.  Hong JH, Nakamura JS, Sahakari SS, et al. The silent epidemic of 
loneliness: identifying the antecedents of loneliness using a lagged 
exposure-wide  approach.  Psychol  Med.  2024;54:1519-1532. 
https://doi.org/10.1017/S0033291723002581

34.  Cowden RG, Nakamura JS, Chen ZJ, Case B, Kim ES, VanderWeele 
TJ.  Identifying  pathways  to  religious  service  attendance  among 
lagged  exposure-wide  analysis.  PLoS  One. 
older  adults:  a 
2022;17:e0278178. https://doi.org/10.1371/journal.pone.0278178

35.  Sonnega A,  Faul  JD,  Ofstedal  MB,  Langa  KM,  Phillips  JW, Weir 
DR. Cohort profile: the Health and Retirement Study (HRS). Int J 
Epidemiol. 2014;43:576-585. https://doi.org/10.1093/ije/dyu067
36.  Smith J, Fisher G, Ryan L, Clarke P, House J, Weir D. Psychosocial 
and Lifestyle Questionnaire. Survey Research Center, Institute for 
Social Research; 2013.

37.  Smith J, Ryan LH, Fisher GG, Sonnega A, Weir DR. HRS Psycho-
social  and  Lifestyle  Questionnaire  2006–2016.  Survey  Research 
Center,  Institute  for  Social  Research,  University  of  Michigan; 
2017:202006-2016.

38.  Fisher  G,  Faul  J, Weir  D, Wallace  R.  Documentation  of  Chronic 
Disease  Measures  in  the  Health  and  Retirement  Study  (HRS/
AHEAD). 2005.

39.  Jenkins  K,  Ofstedal  MB,  Weir  D.  Documentation  of  Health 
Behaviors  and  Risk  Factors  Measured  in  the  Health  and  Retire-
ment Study (HRS/AHEAD). 2008.

40.  Asendorpf  JB,  Van  De  Schoot  R,  Denissen  JJ,  Hutteman  R.  Re-
ducing bias due to systematic attrition in longitudinal studies: the 
benefits of multiple imputation. Int J Behav Dev. 2014;38:453-460.
41.  Harel  O,  Mitchell  EM,  Perkins  NJ,  et  al.  Multiple  imputation 
for  incomplete  data  in  epidemiologic  studies.  Am  J  Epidemiol. 
2018;187:576-584. https://doi.org/10.1093/aje/kwx349

42.  Van Ginkel JR, Linting M, Rippe RC, Van Der Voort A. Rebutting 
existing misconceptions about multiple imputation as a method for 
handling missing data. J Pers Assess. 2020;102:297-308.

43.  Dunn OJ. Multiple comparisons among means. J Am Stat Assoc. 

1961;56:52-64. https://doi.org/10.2307/2282330

44.  VanderWeele  TJ,  Mathur  MB.  Some  desirable  properties  of  the 
Bonferroni correction: is the Bonferroni correction really so bad? Am 
J Epidemiol. 2019;188:617-618. https://doi.org/10.1093/aje/kwy250
45.  VanderWeele  TJ,  Ding  P.  Sensitivity  analysis  in  observational  re-
search:  introducing  the  E-value.  Ann  Intern  Med.  2017;167:268-
274. https://doi.org/10.7326/M16-2607

46.  Kim  ES,  Kubzansky  LD,  Soo  J,  Boehm  JK.  Maintaining  healthy 
behavior:  a  prospective  study  of  psychological  well-being  and 
physical  activity.  Ann  Behav  Med.  2017;51:337-347.  https://doi.
org/10.1007/s12160-016-9856-y

47.  Feig EH, Madva EN, Millstein RA, et al. Can positive psychological 
interventions improve health behaviors? A systematic review of the 
literature. Prev Med. 2022;163:107214. https://doi.org/10.1016/j.
ypmed.2022.107214

48.  Lindsay Smith G, Banting L, Eime R, O’Sullivan G, Van Uffelen JG. 
The association between social support and physical activity in older 
adults: a systematic review. Int J Behav Nutr Phys Act. 2017;14:1-21.
49.  Stults-Kolehmainen  MA,  Sinha  R.  The  effects  of  stress  on  phys-
ical activity and exercise. Sports Med. 2014;44:81-121. https://doi.
org/10.1007/s40279-013-0090-5

50.  Williams  DM.  Darwinian  Hedonism  and  the  Epidemic  of  Un-

healthy Behavior. Cambridge University Press; 2019.

51.  Kahneman D, Wakker PP, Sarin R. Back to Bentham? Explorations 
of  experienced  utility.  Q  J  Econ.  1997;112:375-406.  https://doi.
org/10.1162/003355397555235

52.  Ekkekakis P, Parfitt G, Petruzzello SJ. The pleasure and displeasure 
people  feel  when  they  exercise  at  different  intensities:  decennial 
update  and  progress  towards  a  tripartite  rationale  for  exercise 
intensity  prescription.  Sports  Med.  2011;41:641-671.  https://doi.
org/10.2165/11590680-000000000-00000

53.  Rhodes RE, Kates A. Can the affective response to exercise predict 
future motives and physical activity behavior? A systematic review 
of published evidence. Ann Behav Med. 2015;49:715-731. https://
doi.org/10.1007/s12160-015-9704-5

54.  Kang Y, Strecher VJ, Kim E, Falk EB. Purpose in life and conflict-
related  neural  responses  during  health  decision-making.  Health 
Psychol. 2019;38:545-552. https://doi.org/10.1037/hea0000729
55.  Nakamura  JS,  Lee  MT,  Chen  FS,  et  al.  Identifying  pathways  to 
increased volunteering in older US adults. Sci Rep. 2022;12:12825. 
https://doi.org/10.1038/s41598-022-16912-x

56.  Nakamura JS, Chen Y, VanderWeele TJ, Kim ES. What makes life 
purposeful?  Identifying  the  antecedents  of  a  sense  of  purpose  in 

ann. behav. med. (2025) 59:1–15

15

life  using  a  lagged  exposure-wide  approach.  SSM  Popul  Health. 
2022;19:101235. https://doi.org/10.1016/j.ssmph.2022.101235
57.  Galárraga  O,  Bohlen  LC,  Dunsiger  SI,  et  al.  Small  sustainable 
monetary donation-based incentives to promote physical activity: 
a  randomized  controlled  trial.  Health  Psychol.  2020;39:265-268. 
https://doi.org/10.1037/hea0000818

58.  Nielsen  L,  Riddle  M,  King  JW,  et  al.;  NIH  Science  of  Behavior 
Change  Implementation  Team.  The  NIH  science  of  behavior 
change  program:  transforming  the  science  through  a  focus  on 
mechanisms  of  change.  Behav  Res  Ther.  2018;101:3-11.  https://
doi.org/10.1016/j.brat.2017.07.002

59.  Michie S, Van Stralen MM, West R. The behaviour change wheel: 
a new method for characterising and designing behaviour change 
interventions. Implement Sci. 2011;6:1-12.

60.  Conroy DE, Lagoa CM, Hekler E, Rivera DE. Engineering person-
specific  behavioral  interventions  to  promote  physical  activity. 
Exerc  Sport  Sci  Rev.  2020;48:170-179.  https://doi.org/10.1249/
JES.0000000000000232

61.  Dunton GF, Rothman AJ, Leventhal AM, Intille SS. How intensive 
longitudinal data can stimulate advances in health behavior mainte-
nance theories and interventions. Transl Behav Med. 2021;11:281-
286. https://doi.org/10.1093/tbm/ibz165

62.  Spruijt-Metz D, Hekler E, Saranummi N, et al. Building new com-
putational  models  to  support  health  behavior  change  and  main-
tenance:  new  opportunities  in  behavioral  research.  Transl  Behav 
Med.  2015;5:335-346.  https://doi.org/10.1007/s13142-015-0324-
1

63.  Olivier J, May WL, Bell ML. Relative effect sizes for measures of 
risk. Commun Stat - Theory Methods. 2017;46:6774-6781. https://
doi.org/10.1080/03610926.2015.1134575

64.  Collins  LM,  Murphy  SA,  Strecher  V.  The  multiphase  optimiza-
tion  strategy  (MOST)  and  the  sequential  multiple  assignment 

randomized trial (SMART): new methods for more potent eHealth 
interventions.  Am  J  Prev  Med.  2007;32:S112-S118.  https://doi.
org/10.1016/j.amepre.2007.01.022

65.  Michie S, Richardson M, Johnston M, et al. The behavior change 
technique taxonomy (v1) of 93 hierarchically clustered techniques: 
building an international consensus for the reporting of behavior 
change interventions. Ann Behav Med. 2013;46:81-95. https://doi.
org/10.1007/s12160-013-9486-6

66.  Bauman  AE,  Reis  RS,  Sallis  JF,  Wells  JC,  Loos  RJ,  Martin  BW; 
Lancet Physical Activity Series Working Group. Correlates of phys-
ical  activity:  why  are  some  people  physically  active  and  others 
not?  Lancet.  2012;380:258-271.  https://doi.org/10.1016/S0140-
6736(12)60735-1

67.  Puterman E, Weiss J, Hives BA, et al. Predicting mortality from 57 
economic, behavioral, social, and psychological factors. Proc Natl 
Acad  Sci  USA.  2020;117:16273-16282.  https://doi.org/10.1073/
pnas.1918455117

68.  Aichele S, Rabbitt P, Ghisletta P. Think fast, feel fine, live long: a 
29-year  study  of  cognition,  health,  and  survival  in  middle-aged 
and  older  adults.  Psychol  Sci.  2016;27:518-529.  https://doi.
org/10.1177/0956797615626906

69.  Ganna  A,  Ingelsson  E.  5  year  mortality  predictors  in  498 103 
UK  Biobank  participants:  a  prospective  population-based  study. 
Lancet. 
https://doi.org/10.1016/s0140-
6736(15)60175-1

2015;386:533-540. 

70.  Patel CJ, Rehkopf DH, Leppert JT, et al. Systematic evaluation of 
environmental  and  behavioural  factors  associated  with  all-cause 
mortality in the United States National Health and Nutrition Ex-
amination  Survey.  Int  J  Epidemiol.  2013;42:1795-1810.  https://
doi.org/10.1093/ije/dyt208

71.  Henrich J, Heine SJ, Norenzayan A. Most people are not WEIRD. 

Nature. 2010;466:29. https://doi.org/10.1038/466029a
