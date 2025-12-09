# Cerit_2025_Person-Specific Analyses of Smartphone Use and Mental Health Intensive Longitudinal Study.

JMIR FORMATIVE RESEARCH

Original Paper

Cerit et al

Person-Specific Analyses of Smartphone Use and Mental Health:
Intensive Longitudinal Study

Merve Cerit1, MS; Angela Y Lee2, MA; Jeffrey Hancock2,3, PhD; Adam Miner4, MS, PsyD; Mu-Jung Cho5, PhD;
Daniel  Muise6,  PhD;  Anna-Angelina  Garròn  Torres2,  BA;  Nick  Haber1,7,  PhD;  Nilam  Ram2,8,  PhD;  Thomas  N
Robinson9, MD, MPH; Byron Reeves2, PhD
1Graduate School of Education, Stanford University, Stanford, CA, United States
2Department of Communication, Stanford University, Stanford, CA, United States
3Cyber Policy Center, Stanford University, Stanford, CA, United States
4Department of Psychiatry and Behavioral Science, Stanford University, Stanford, CA, United States
5Center for Survey Research, Research Center for Humanities and Social Sciences, Academia Sinica, Taipei, Taiwan
6Screenlake Inc, San Mateo, CA, United States
7Department of Computer Science, Stanford University, Stanford, CA, United States
8Department of Psychology, Stanford University, Stanford, CA, United States
9Departments of Pediatrics, Medicine and Epidemiology & Population Health, Stanford University, Stanford, CA, United States

Corresponding Author:
Merve Cerit, MS
Graduate School of Education
Stanford University
520 Galvez Mall
Stanford, CA, 94305
United States
Phone: 1 650 723 21 46
Email: mervecer@stanford.edu

Abstract

Background:  Contrary to popular concerns about the harmful effects of media use on mental health, research on this relationship
is ambiguous, stalling advances in theory, interventions, and policy. Scientific explorations of the relationship between media
and mental health have mostly been found null or have small associations, with the results often blamed on the use of cross-sectional
study designs or imprecise measures of media use and mental health.

Objective:  This exploratory empirical demonstration aims to answer whether mental health effects are associated with media
use experiences by (1) redirecting research investments to granular and intensive longitudinal recordings of digital experiences
to build models of media use and mental health for single individuals over the course of 1 year, (2) using new metrics of fragmented
media use to propose explanations of mental health effects that will advance person-specific theorizing in media psychology, and
(3) identifying combinations of media behaviors and mental health symptoms that may be more useful for studying media effects
than single measures of dosage and affect or assessments of clinical symptoms related to specific disorders.

Methods:  The activity on individuals’ smartphone screens was recorded every 5 seconds when devices were in use over 1 year,
resulting in a dataset of 6,744,013 screenshots and 123 fortnightly surveys from 5 adult participants. Each participant contributed
between 0.8 and 2.7 million screens. Six media use metrics were derived from smartphone metadata. Fortnightly surveys captured
symptoms  of  depression,  attention-deficit/hyperactivity  disorder,  state  anxiety,  and  positive  affect.  Idiographic  filter  models
(p-technique canonical correlation analyses) were applied to explore person-specific associations.

Results:  Canonical correlations revealed substantial person-specific associations between media use and mental health, ranging
from r=0.82 (P=.008) to r=0.92 (P=.03). The specific combinations of media use metrics and mental health dimensions were
different for each person, reflecting significant individual variability. For instance, the media use canonical variate for 1 participant
was characterized by higher loadings for app-switching, which, in combination with other behaviors, correlated strongly with a
mental health variate emphasizing anxiety symptoms. For another, prolonged screen time, alongside other media use behaviors,
contributed to a mental health variate weighted more heavily toward depression symptoms. These within-person correlations are
among the strongest reported in this literature.

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 1
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

Conclusions:  Results  suggest  that  the  relationships  between  media  use  and  mental  health  are  highly  individualized,  with
implications for the development of personalized models and precision smartphone-informed interventions in mental health. We
discuss how our approach can be extended generally, while still emphasizing the importance of idiographic approaches. This
study highlights the potential for granular, longitudinal data to reveal person-specific patterns that can inform theory development,
personalized screening, diagnosis, and interventions in mental health.

(JMIR Form Res 2025;9:e59875)  doi: 10.2196/59875

KEYWORDS

media use; mental health; mHealth; uHealth; digital health; precision mental health; idiographic analysis; person-specific modeling;
p-technique; longitudinal study; precision interventions; smartphones; idiosyncrasy; psychological well-being; canonical correlation
analysis; United States

Introduction

Over  the  last  decade,  researchers  have  conducted  extensive
studies  involving  hundreds  of  thousands  of  participants  to
understand  the  relationship  between  media  use  and  mental
health.  Despite  significant  investments,  findings  remain
ambiguous, often reporting null or small associations [1-5]. This
lack  of  clarity  undermines  progress  in  theory  development,
public  policy,  and  clinical  interventions.  Researchers  have
proposed solutions, including granular tracking of media use
[6-8], longitudinal study designs [9,10], the inclusion of at-risk
populations [11-13], and person-specific analytics to account
for individual differences [14,15].

A  central  challenge  in  this  research  is  the  problem  of
idiosyncrasy—the substantial variability in how individuals use
media  and  how  it  affects  their  mental  health  [16,17].  In
psychology, the opportunity to reclaim idiosyncratic variance
has  been  defined  as  one  of  identifying  idiographic  filters  for
nomothetic  interests  [18].  The  core  argument  is  that  the
conventional practice of averaging out idiosyncrasy is neither
theoretically satisfactory nor practically useful. We explore if
and  how  an  idiographic  filter  approach  might  enhance  this
research about media use and mental health. While researchers
often seek universal rules to inform public policies or clinical
interventions,  such  generalizations  obscure  the  reality  that
individuals’ media  experiences  are  inherently  personal  and
shaped  by  unique  combinations  of  content  and  context.
Aggregate analyses, which average out these differences, are
insufficient  and  often  misleading.  Similarly,  mental  health
symptom clusters frequently cut across traditional diagnostic
boundaries,  further  emphasizing  the  need  for  individualized
approaches. Addressing this challenge requires an idiographic
perspective, which preserves individual variability and analyzes
person-specific patterns rather than treating them as noise. By
adopting  an  idiographic  approach,  research  can  uncover
meaningful insights into the unique configurations of media use
and mental health for each person.

To  address  this  challenge,  we  used  p-technique  canonical
correlation analysis (pCCA) [19], a method designed to analyze
within-person  relationships  over  time.  This  approach  creates
idiographic filters [20] that highlight how core constructs, such
as  media  use  and  mental  health  metrics,  manifest  differently
for  each  participant.  Unlike  traditional  methods  that  assume
consistency  across  individuals,  pCCA  uncovers  the  specific
patterns  and  dynamics  unique  to  each  person  based  on  the

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

common  set  of  variables.  For  example,  media  use  heavily
characterized  by  frequent  app-switching  may  correlate  with
symptoms  of  hyperactivity  for  1  individual,  while  prolonged
social  screen  time  may  have  significant  weight  in  describing
the  changes  in  symptoms  of  depression  for  another.  By
prioritizing  individual-level  insights,  this  method  provides  a
pathway  to  more  personalized  interventions  (Multimedia
Appendix 1 [2-4,7,15-19,21-50]).

This study uses granular longitudinal data collected through the
Human Screenome Project [21,51], which recorded smartphone
activity every 5 seconds for 1 year, resulting in over 6.7 million
screenshots and 123 surveys across 5 participants. Mental health
[52],
metrics, 
attention-deficit/hyperactivity  disorder  (ADHD)  [22],  state
anxiety [53], and positive affect were assessed fortnightly. Using
pCCA, we explored person-specific associations between media
use and mental health to address the following questions.

depression 

symptoms 

including 

of 

• Can  granular  longitudinal  recordings  reveal  associations
between media use and mental health that differ from the
null or small effects reported in aggregated studies?
• Can  new  metrics,  such  as  fragmentation  of  media  use,
explain person-specific mental health effects and advance
media psychology theory?

• Can combinations of mental health symptoms provide better
insights into media effects than single measures of dosage
or individual clinical symptoms?

By focusing on individual experiences and variability over time,
this  study  offers  a  novel  approach  to  understanding  the
relationship between media use and mental health, emphasizing
the  potential  of  person-specific  data  to  inform  theory
development and precision interventions.

Methods

to  assess  smartphone  use  and 

Procedure and Participants
This  study  was  conducted  in  the  United  States,  leveraging  a
its
longitudinal  design 
relationships  with  mental  health.  Data  were  collected  via  a
custom  smartphone  app  and  biweekly  participant  surveys,
enabling the integration of behavioral data with mental health
measures. Participants were recruited via the Qualtrics research
panel as part of a larger research project on assessing digital
experiences  with  smartphone  data  [51].  Eligibility  criteria
included residing in the United States, being the sole user of an
Android  phone,  and  providing  informed  consent  and  Health

JMIR Form Res 2025 | vol. 9 | e59875 | p. 2
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

Insurance  Portability  and  Accountability  Act  (HIPAA)
authorization.

Participants installed a custom study app on their smartphones,
enabling an unobtrusive collection of smartphone screens. The
app  required  no  active  user  management  and  operated
transparently,  with  a  status  bar  icon  indicating  its  activity.
Screenshots, along with operating system metadata like phone
battery state and foreground app were captured and recorded
automatically every 5 seconds when the screen was active.

Our study selected a focused sample that satisfied the minimum
requirements for robust within-person analysis and allowed for
a  demonstration  of  our  methodology,  prioritizing  long  time
series from a small number of participants over larger aggregate
datasets  so  that  we  might  uncover  detailed  person-specific
insights  and  enable  future  scalability  through  computational
methods  [7,21,23].  We  conducted  a  detailed  analysis  of  5
participants, randomly chosen from a group of 36 individuals
that  met  several  eligibility  requirements.  First,  they  had
contributed at least 800,000 screenshots, reflecting an average
of at least 3 hours of daily smartphone use over the year. This
measure  was  chosen  to  capture  use  data  that  is  close  to  the
national  average  [54-56].  The  goal  was  to  ensure  that
participants  had  sufficient  smartphone  use  to  demonstrate
relationships  with  mental  health.  Second, 
the  selected
participants had completed at least 20 biweekly surveys, creating
a sufficient longitudinal record for each participant that exceeded
the number of variables in the pCCA [57]. Finally, the selected
participants had reported at least 1 biweekly period where their
mental health symptoms reached clinically significant thresholds
[22,52,58,59].

Ethical Considerations
This  study  adhered  to  national  regulations  and  institutional
policies, including the Declaration of Helsinki (2013), and was
approved  by  Stanford  University’s  institutional  review  board
under  protocol  (#56430).  All  procedures  were  reviewed  and
classified as minimal risk.

Participants provided electronic informed consent and HIPAA
authorization before enrollment. The consent process included
detailed information about the study’s goals, procedures, and
privacy  protections,  and  participants  confirmed  their  consent
using  an  e-signature  interface.  To  ensure  privacy  and
confidentiality,  all  data  were  encrypted  during  transfer  and
securely  stored  on  Stanford’s  high-risk  personal  identifiable
information and protected health information–compliant servers.
Screenshots and metadata were deidentified prior to analysis,
with access to raw screenshots restricted to a small subset of
researchers under strict institutional protocols. Only aggregated,
deidentified  data  were  analyzed  and  reported  to  prevent  the
identification  of  individual  participants.  Participants  were
compensated  US  $15  for  each  fortnightly  survey  and  data
submission,  with  potential  earnings  of  up  to  US  $390  for
completing the 1-year study.

Data were collected unobtrusively using a custom Screenomics
app that captured screenshots every 5 seconds when the device
was active. The app included an icon on the status bar to ensure

transparency. Although nearly all screenshots were processed
through automated methods, a small subset could be viewed by
researchers in specific analyses. To mitigate risks, research staff
were trained as mandated reporters under Stanford University
and  California  guidelines.  Any  concerning  content  signaling
potential  legal,  medical,  or  social  risks  was  escalated  to  the
Principal Investigators for appropriate action. Protocols were
in  place  to  refer  participants  to  professionals  or  services  as
needed, ensuring their privacy while addressing potential risks
to their well-being.

No images or supplementary materials in this manuscript include
identifiable  participant  information.  All  visual  data  were
anonymized to ensure privacy, and no consent was required for
image inclusion as all images were deidentified.

All  research  staff  completed  mandatory  HIPAA  and  human
subjects  training.  Data  security  measures  included  strong
passwords, restricted database access, and frequent reminders
of privacy policies. These procedures ensured the highest level
of data integrity and participant confidentiality.

Measures

Mental Health Measures
Participants completed fortnightly surveys over a year to assess
symptoms of depression, and ADHD, in addition to state anxiety
and positive affect. This extended time frame allowed the study
of fluctuations across weeks or months [24-29].

Depression symptoms were measured using the 10-item Center
for Epidemiologic Studies Depression scale [52]. Participants
rated the frequency of symptoms (eg, “I felt I could not shake
off the blues”) on a 4-point Likert scale. Scores range from 0
to 60, with scores above 16 indicating clinical risk [59]. These
scores were used to calculate the number of fortnight participants
who were at clinical risk for depression (Table 1). The CES-D
scale is in the public domain.

State  anxiety  was  assessed  with  the  20-item  State  Anxiety
subscale of the State-Trait Anxiety Inventory [60]. Items (eg,
“I am tense; I am worried”) were rated on a 4-point Likert scale.
Scores  range  from  20  to  80,  with  scores  over  40  indicating
moderate  to  high  anxiety  [58].  This  threshold  was  used  to
calculate  fortnights  at  clinical  risk  (Table  1).  A  license  was
obtained from Mind Garden, Inc.

Positive  affect  was  measured  using  a  single  item:  “Looking
back over the last two weeks, I felt happy,” rated on a 100-point
slider scale from “strongly disagree” to “strongly agree.”

Hyperactivity  and  inattention  symptoms  were  measured
fortnightly using the 18-item Adult ADHD Self-Report Scale
[22,61].  Participants  rated  hyperactivity  and  inattention  on  a
5-point Likert scale. Subscale scores range from 0 to 36. A score
of  9  or  more  on  the  first  6  items  (4  inattention  and  2
hyperactivity) indicates clinical risk for adult ADHD [62]. These
thresholds were used to calculate risk fortnights (Table 1). A
license  was  obtained  from  NYU  TOV  Licensing,  New  York
University.

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 3
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Table 1.  Participant data and demographicsa.

Cerit et al

Participant A (n=26)

Participant B (n=25)

Participant C (n=20)

Participant D (n=25)

Participant E (n=27)

Total screens

824,111

1,191,958

Age (year)

Sex

Race

Region

62

Female

White

Midwest

Residence type

Rural

22

Female

White

Midwest

Suburban

897,514

37

Female

20

Female

Multiracial Hispanic

White

Northeast

Suburban

Pacific

Suburban

24

Female

Black

Northeast

Urban

1,106,164

2,724,266

Highest educational
level

2-year college

High school or GEDb

Some college

Some college

Some College

Marital status

Divorced or separated

Single or never married

Married

Single or never married

Married

Income level (US $)

15,000-24,999

14,999 or less

25,000-29,999

75,000-99,999

14,999 or less

aThe table presents the demographic characteristics of participants in the study, as collected through an initial onboarding survey. The survey was
administered before the commencement of the study to gather pertinent information regarding participant backgrounds. “n” is the count of fortnightly
surveys completed by each participant throughout the study year, while “Total screens” is the cumulative number of screenshots recorded from each
participant’s smartphone during the study year.
bGED: General Educational De velopment.

system  metadata 

Media Use Metrics
Six metrics for smartphone media use were derived from the
screenshots  and  operating 
recorded
continuously at 5-second intervals over the study year. Metadata
enabled us to map app names and categories using Google Play
Market classifications [63,64]. All metrics were averaged daily
within biweekly periods, defined as the 14 days preceding each
survey,  except  session  duration  calculated  as  the  average
screen-on  interval.  Missing  data  were  addressed  under  the
“missing at random” assumption.

Screen  time  was  measured  as  the  daily  average  number  of
screenshots  captured  during  screen-on  periods.  The  data
collection app captured screenshots every 5 seconds when the
screen was on. For each fortnight, the total screenshots were
divided by the number of active data collection days.

Social  screen  time  was  measured  as  the  daily  average  of
screenshots recorded while using social apps. Social apps were
those  classified  as  “social”  by  Google  Play  Market
categorization  [63,64].  Social  apps  included  common  social
media apps (eg, TikTok and Instagram), certain messaging apps
(eg, Telegram and Text Free), and social network or dating apps
(eg, Tagged and Grindr). Similar to the screen time measure,
we calculated this metric by dividing the total number of social
app screenshots by the number of active data collection days.

The number of sessions of smartphone use indicated average
daily  sessions,  defined  as  intervals  between  screen  on  or  off
events.  For  each  fortnight,  we  calculated  the  daily  average
number of sessions by dividing the total number of sessions by
the number of days the participant actively used their phone. A
higher number of sessions (eg, ten 30-second sessions) relative
to  the  duration  of  each  session  (eg,  one  5-minute  session)
indicates a more fragmented digital experience.

Session duration was calculated as the time interval between
the initiation of a session and its termination. For each fortnight,
we summed the duration of all sessions that occurred within

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

that  period  and  then  computed  the  mean.  This  provided  an
average session duration metric for the specified time frame.

The number of unique apps was calculated as the daily average
of distinct apps used, calculated by dividing the count of unique
apps within a period by the number of active days.

The number of app switches indicated the daily average number
of times individuals switched between apps and was calculated
as a measure of fragmentation. For each biweekly period, we
counted how many times individuals moved from app to app
(ie, from Facebook to Zoom=1 switch) and divided that number
by the number of active smartphone data collection days. Please
see  Multimedia  Appendix  1 [2-4,7,15-19,21-50]  for  more
discussion on theories and measures examining media use and
mental health over time and the origins of our measures.

Data Analysis
Canonical correlation analysis (CCA) is a classical technique
used to obtain the maximal correlation between objects that are
represented by 2 sets of variables [65]. Adopting the Nesselroade
et al idiographic filter approach [18], we use pCCA to model
each  individual’s  multivariate  repeated  measures  data.  The
observed  correlation  between  an  individual’s  media  use  and
mental  health  is  not  static;  rather,  it  depends  on  the  chosen
coordinate system, that is, how observed variables are projected
onto latent constructs of media use and mental health. Unlike
traditional  factorial  analyses  that  assume  a  uniform  variable
projection  across  individuals,  the  idiographic  filter  approach
allows person-specific rotations of the coordinate system.

pCCA does this by locating the specific rotation where the linear
correlation  between  the  latent  media  use  and  mental  health
canonical  variates  is  mutually  maximized.  The  size  and
significance of the maximum correlation (ρ) are used to answer
our  first  research  question:  Does  the  analysis  of  single
individuals  offer  different  conclusions  than  the  small  or  null
effects  reported  in  the  across-individual  analyses  dominating
the literature? The configurations of the basis vectors x and y

JMIR Form Res 2025 | vol. 9 | e59875 | p. 4
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

are interpreted to address our second and third questions: Can
we identify combinations of media use metrics and mental health
metrics that might advance theories about media effects?

Given  Ax (27  occasions  ×  6  media  use  variables)  and  Ay (27
occasions  ×  5  mental  health  variables)  for  an  individual,  the
data are projected onto canonical variates, zx = Axx and zy =
Ayy, the correlation of which is given by the following equation.

mental health. This process generates a null distribution for ρ,
representing the range of chance correlations expected in the
absence of a systematic relationship. Comparing the observed
ρ to this null distribution provides an exact P value based on
the  empirical  data,  thereby  avoiding  reliance  on  theoretical
distributions that could inflate P values. Histograms of these
permutations  are  presented  in  Multimedia  Appendix  2.  All
pCCA and permutation test analyses were done using the cca
package [67] in R (R Foundation for Statistical Computing).

Results

where x and y are chosen to maximize ρ, achieved via singular
value decomposition [19,66]. We use permutation tests to ensure
observed correlations are not simply artifacts of random chance.
Specifically, for each participant, we perform 1000 permutations
by randomly shuffling the values within the columns of Ax or
Ay, disrupting any temporal ordering between media use and

The following results include an analysis of a full year of media
use  and  mental  health  data  (6,744,013  screenshots  and  123
fortnightly surveys) provided by 5 individuals. The background
of each participant and descriptive statistics about media use
and mental health are in Tables 1-3.

Table 2.  Descriptive statistics for participants' mental health measures throughout 1 yeara.

Partici-
pants

Depression symptoms (0-60)

State anxiety (20-80)

ADHDb symptoms (0-72)

Positive affect (0-
100), mean (SD)

Mean (SD)

9.23 (5.31)

24.80 (5.07)

12.40 (4.77)

12.80 (6.10)

14.78 (7.06)

Clinical
risk peri-
ods, n

Mean (SD)

Clinical
risk peri-
ods, n

Inattention (0-
36), mean (SD)

Hyperactivity (0-
36), mean (SD)

Clinical
risk peri-
ods, n

1

24

4

7

4

44.23 (4.43)

51.84
(10.15)

45.05
(14.25)

45.84 (8.76)

55.00 (8.98)

22

21

13

17

27

1.88 (3.24)

2.04 (3.32)

12.72 (1.99)

8.72 (1.79)

10.10 (2.25)

5.70 (0.80)

5.36 (2.27)

2.76 (1.39)

4.52 (4.37)

4.34 (4.36)

0

13

3

0

0

53.85 (17.54)

62.12 (19.81)

65.35 (5.43)

57.00 (15.21)

16.85 (27.98)

A

B

C

D

E

aThe table shows the means and SD for each mental health measure, as well as the clinical risk associated with symptomatology exceeding certain
thresholds. Clinical risk periods are calculated as the number of fortnightly surveys in which participants’ responses exceeded the clinical threshold for
each measure.
bADHD: attention-deficit/hyperactivity disorder.

Table 3.  Descriptive statistics for participants' media use measures throughout 1 year.

Participant

Screen time

(hours per day),
mean (SD)

Social screen time
(hours per day),
mean (SD)

Number of sessions
(per fortnight), mean
(SD)

Session duration
(minutes per day),
mean (SD)

Number of unique
apps (per day), mean
(SD)

Number of app switch-
es (per day), mean (SD)

A

B

C

D

E

2.99 (0.51)

0.41 (0.17)

57.84 (8.12)

4.15 (1.10)

0.37 (0.12)

32.76 (3.18)

4.18 (0.95)

0.15 (0.23)

57.81 (8.89)

3.10 (0.49)

7.59 (1.86)

4.33 (0.85)

90.90 (25.28)

2.87 (0.89)

4.18 (1.05)

9.55 (2.03)

0 (0)

0 (0)

4.08 (0.39)

3.64 (0.37

7.29 (2.50)

4.54 (0.61)

210.27 (32.79)

206.87 (18.96)

324.88 (52.73)

273.22 (54.38)

9.45 (2.10)

62.62 (14.75)

1.50 (0.59)

39.51 (14.48)

The main objective of this study was to assess whether analysis
of media use metrics derived from super-intensive observational
data passively collected from the smartphones individuals use
in their daily lives could unearth relationships between media
use and mental health within individuals that have previously
been  difficult  to  observe  using  analyses  aggregated  across
individuals.  Related  to  that  objective,  we  first  report  the

within-person associations between the media use and mental
health latent variables that were obtained separately for each
participant using pCCA.

The main results of this study are reported in Figure 1, which
shows correlations and plots of the fortnightly media use and
mental health variables across 1 year for each participant. The

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 5
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

observed p-technique canonical correlations are large, ranging
from 0.78 to 0.92. These values provide a compelling answer
to our primary research question: for 4 of the 5 participants in
this  study,  fluctuations  in  canonical  media  use  variate  were

significantly and tightly coupled with fluctuations in a canonical
mental health variate, more so than for any previous associations
observed in this literature [3,5].

Figure 1.  Canonical variate plot for each participant (A-E). This figure presents the results of pCCA, highlighting within-person associations between
media use and mental health metrics for five female Android phone users in the United States. The data were collected longitudinally as part of the
Human Screenome Project, spanning 1 year (from July 2020 to October 2021). For each participant, the figure shows the temporal alignment of canonical
media use variate (red solid line) and mental health variate (blue solid line), derived from granular measures recorded fortnightly. Individual metrics
of media use (dotted red lines, eg, app-switching frequency, social screen time) and mental health (dotted blue lines, eg, depression, state anxiety) are
also plotted in the background for comparison. Canonical correlations (r) for each participant range from 0.78 to 0.92, indicating strong covariation.
Wilks statistic (Λ), P values, and sample size (n) are displayed for statistical significance. Permutation tests were conducted to validate correlations by
generating null distributions based on shuffled data. Participant A shows a strong positive association between mental health and media use, with both
variates generally moving together over time. Participant B exhibits a similar pattern, though with more pronounced fluctuations. Participant C has the
highest correlation, indicating tightly coupled trends in media use and mental health across the year. Participant D also shows a strong association,
though with some deviations at certain time points. In contrast, Participant E presents a weaker and statistically non-significant correlation, suggesting
that media use and mental health follow more independent patterns in this case. These findings illustrate the unique within-person dynamics of media
use and mental health over time, emphasizing the importance of person-specific models in understanding this relationship.

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 6
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

for  each  participant, 

The composition of media use and mental health variates was
unique 
reflecting  person-specific
relationships and highlighting the heterogeneity in how media
use  impacts  mental  health.  While  individual  metrics  (eg,
app-switching, screen time) varied considerably over time, the
canonical variates showed consistent and strong covariation for
four of the 5 participants. These findings underscore the use of
pCCA in identifying tightly coupled, within-person associations
that are otherwise obscured in aggregated analyses, paving the
insights  and
way 
interventions.

individualized 

theoretical 

for  more 

The  figures  below  highlight  the  unique  person-specific
relationships  between  media  use  metrics  and  mental  health
measures.  These  findings  demonstrate  the  variability  in  how
media use correlates with mental health for each participant,
emphasizing the value of individualized approaches.

For participant A (Figure 2), the media use behavior most related
to  greater  mental  health  symptoms  over  time  was  primarily
shorter sessions (–0.93), and secondarily a higher number of
sessions (0.51) and shorter screen time (–0.48). This suggests
that the fluctuations in media use most related to mental health
for this person are quick-checking behaviors on the smartphone.
In complement, the configuration of mental health symptoms
and positive affect that was most related to fluctuations in media
use was characterized by lower state anxiety (–0.85) and lower
levels  of  ADHD  symptoms  for  both  inattention  (–0.59)  and
hyperactivity  (–0.52),  and  lower  positive  affect  (–0.71).
Generally, for participant A, quick checking on the smartphone
was  associated  with  lower  positive  affect,  and  lower  state
anxiety and ADHD symptoms.

Figure 2.  Canonical correlation analysis of participant A’s media use and mental health. This figure illustrates the results of pCCA for participant A,
based on 1 year of longitudinal data. Media use (left column) includes 6 variables (eg, session duration, number of sessions, and screen time), while
mental health (right column) includes 5 variables (eg, state anxiety, depression symptoms, and positive affect). Arrows from the canonical variates
(center) to observed variables indicate the direction (positive or negative) and strength of associations, with values closer to ±1.0 indicating stronger
relationships. The canonical correlation (r=0.82; P=.01) highlights a significant within-person relationship, showing that quick-checking behaviors (eg,
shorter session duration and more frequent sessions) were associated with reduced anxiety and ADHD symptoms but also diminished positive affect.

Figure 3 shows that for participant B, the media use behaviors
most related to greater mental health symptoms over time were
characterized by longer sessions (0.66) and secondarily by more
screen  time  (0.53)  and  little  app  switching  (–0.55).  We
characterize this combination as focused smartphone use. The
mental  health  symptoms  most  related  to  media  use  were
characterized by depression symptoms (0.61) and lower positive

affect (–0.53). It is also notable that this participant’s mental
health changes, especially true for depression symptoms, had
a  stronger  association  with  media  use  changes  than  for  state
anxiety. The media use canonical variate for participant B was
driven by fluctuations in total screen time rather than social app
use, specifically.

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 7
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

Figure 3.  Canonical correlation analysis of participant B’s media use and mental health. This figure illustrates the results of pCCA for participant B,
based on 1 year of longitudinal data. Media use (left column) includes 6 variables (eg, session duration, screen time, and app-switching intensity), while
mental health (right column) includes 5 variables (eg, depression symptoms, state anxiety, and positive affect). Arrows from the canonical variates
(center) to observed variables indicate the direction (positive or negative) and strength of associations, with values closer to ±1.0 indicating stronger
relationships.  The  canonical  correlation  (r=0.82;  P=.02)  highlights  a  significant  within-person  relationship,  showing  that  focused  smartphone
use—characterized by longer session duration, higher screen time, and minimal app-switching—was associated with increased depression symptoms
and reduced positive affect.

For participant C (Figure 4), the media use canonical variate
shows the strongest loadings for the number of social screen
time (distinct from total screen time) at 0.79. Secondarily, there
is a high loading for the use of unique apps (0.53). The mental
health canonical variate shows a strong loading associated with
depression symptoms (0.75). Additionally, there is a noteworthy
negative loading in relation to hyperactivity symptoms (–0.60).

The much larger loading for social screen time in comparison
to total screen time shows the value of separating these uses
when  examining  relationships  with  mental  health.  This
distinction is often part of discussions about media effects (ie,
more worry about intensive social app use and depression than
about the effects of all media use). As for many media effects,
however, the value of the distinction is person-specific.

Figure 4.  Canonical correlation analysis of participant C’s media use and mental health. This figure illustrates the results of pCCA for participant C,
based on 1 year of longitudinal data. Media use (left column) includes 6 variables (eg, social screen time, number of unique apps, session duration),
while  mental  health  (right  column)  includes  5  variables  (eg,  depression  symptoms,  hyperactivity  symptoms,  and  positive  affect).  Arrows  from  the
canonical variates (center) to the observed variables indicate the direction (positive or negative) and strength of associations, with values closer to ±1.0
reflecting stronger relationships. The canonical correlation (r=0.92; P=.03) underscores a significant within-person relationship, with social screen time
(0.79) emerging as the strongest media use factor, closely tied to increased depressive symptoms (0.75) and reduced hyperactivity symptoms (–0.60).

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 8
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

Participant D (Figure 5) did not use any social apps during the
entire year (ie, there are no screens from any of the hundreds
of  social  apps  in  the  Google  Play  store).  Their  media  use
canonical variate is characterized by fewer app switches (–0.77),
extended  session  durations  (0.71),  and  a  reduced  number  of
sessions overall (–0.57). This pattern indicates longer, focused
interactions.  The  mental  health  canonical  variate  was
characterized primarily by reduced positive affect (–0.58), with
no  large  loadings  associated  with  any  of  the  mental  health

symptoms.  For  participant  D,  longer  and  more  focused
smartphone sessions had a more singular definition (diminished
positive  affect).  However,  the  number  and  duration  of  the
sessions  were  still  highly  correlated  with  smartphone  use
features (r=0.82; P=.008).

There was no statistically significant association between the
media  and  mental  health  canonical  variates  for  Participant  E
(Figure 6).

Figure 5.  Canonical correlation analysis of participant D’s media use and mental health. This figure presents the results of pCCA for participant D,
based  on  longitudinal  data  collected  over  1  year.  Media  use  (left  column)  includes  6  variables  (eg,  session  duration,  number  of  sessions,  and  app
switching), while mental health (right column) includes 5 variables (eg, positive affect, state anxiety, and ADHD symptoms). The arrows between latent
canonical variates (center) and observed variables represent the direction (positive or negative) and strength of associations, with values closer to ±1.0
indicating  stronger  relationships.  The  canonical  correlation  (r=0.82;  P=.008)  underscores  a  significant  within-person  association,  highlighting  that
longer session durations and reduced app-switching behaviors were most associated with lower positive affect for participant D.

Figure 6.  Canonical correlation analysis of participant E’s media use and mental health. This figure illustrates the results of pCCA for participant E,
based on 1 year of longitudinal data. Media use (left column) is represented by 6 variables, such as screen time, session duration, and number of app
switches, while mental health (right column) is represented by 5 variables, including depression symptoms, state anxiety, and positive affect. Arrows
connecting latent canonical variates (center) to observed variables indicate the direction (positive or negative) and strength of associations, with values
closer to ±1.0 reflecting stronger associations. The canonical correlation (r=0.78; P=.35) indicates a nonsignificant association.

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 9
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

Discussion

Principal Findings
The results highlight the person-specific associations between
media use and mental health. Canonical correlations revealed
substantial covariation (0.82 to 0.92) over time for 4 out of 5
individuals.  Simultaneously,  as  hypothesized,  the  specific
combinations of media dosage metrics and dimensions of mental
health  that  defined  this  covariation  were  different  for  each
person  (Multimedia  Appendix  1 [2-4,7,15-19,21-50].  The
approach supports the idea of a common association between
media use and mental health while accommodating idiosyncrasy
in how that association manifests for individuals. The couplings
between  media  use  and  mental  health  for  each  person  offer
insights  into  the  complexity  of  this  relationship,  directly
addressing the research questions posed in the introduction.

In summary, our conclusions are the following.

•

• As  research  investments  shift  toward  intensive,  granular
longitudinal  data  about  individuals’ digital  experiences,
this study demonstrates the potential to construct distinct,
person-specific  models  of  media  use  and  mental  health,
revealing  insights  that  transcend  traditional  aggregated
analyses.
The study’s innovative approach, combining various dosage
metrics of fragmented media use, advances person-specific
theorizing 
in  media  psychology,  offering  potential
explanations  for  the  impact  on  mental  health  and
emphasizing the significance of tailored approaches.
• By identifying individualized combinations of mental health
symptoms, 
the  necessity  of
the  study  underscores 
considering  nuanced  factors  beyond  single  measures  of
dosage  and  affect  or  clinical  symptoms  associated  with
specific disorders.

Causality and Theory
The substantial p-technique canonical correlations observed in
this study reflect within-person associations between media use
and  mental  health  but  do  not  establish  causality.  Media  use
metrics may act as markers responding to mental health changes,
antecedents  influencing  mental  health,  or  reflections  of
confounding  variables.  A  causal  explanation  likely  involves
complex mechanisms interacting over different time domains
and  individual  histories,  which  this  analysis  does  not  aim  to
disentangle.

Past research has explored single mechanisms over varying time
frames,  such  as  the  introduction  of  Facebook  on  campuses
(months/years) [68], ecological momentary assessment studies
linking self-reported media use with mental health (days/weeks)
[69],  and  cohort  analyses  over  decades  [70].  Additionally,
momentary exposures, like a single unflattering social media
post, might amplify depression symptoms, particularly during
periods of heightened vulnerability. Interactions between short-
and long-term domains—for example, a negative social media
post  during  an  extended  depressive  episode—could  further
complicate causal pathways.

Combining  mechanisms  into  a  single  causal  conclusion  for
media use and mental health is beyond the scope of this project

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

and likely any single study, given the heterogeneity observed
across individuals. The participants in this study suggest that
no universal explanation applies across diverse media behaviors,
content, and time domains. Instead, multiple mechanisms, each
tailored  to  specific  contexts,  are  likely  needed.  Controlled
experiments targeting distinct media experiences [71,72] and
idiographic approaches like ours can help identify mechanisms
for further exploration.

The  within-person  associations  in  this  project  emphasize  the
need for new theories addressing the accumulation of similar
media  experiences  over  time,  regardless  of  specific  content.
Such mechanisms echo the concept of resonance in social reality
theory  [73,74],  where  outcomes  arise  from  the  alignment  of
digital and real-life environments. For instance, increased screen
use during a depressive episode may reinforce social isolation,
creating a feedback loop that intensifies mental health symptoms
[75]. These findings highlight the importance of reexamining
how repetitive media experiences influence mental health over
extended periods.

Interventions
The p-technique canonical correlations observed in this project
(Figure 1) suggest that results obtained for a participant over 1
year may generalize to future months. Acute changes in media
use  could  serve  as  markers  for  triggering  mental  health
interventions  without  requiring  frequent  or  intrusive  direct
assessments. Interventions could integrate patient and clinician
access to data through dashboards alerting users to mental health
risks  and  offering  tailored  recommendations.  For  instance,
systems might limit social app usage for some individuals or
promote it for others based on identified risks. Person-specific
thresholds for intervention provide a more accurate approach
than generalized thresholds derived from population averages
[76].

to 

information  designed 

The key to these interventions is precision timing and targeted
actions that connect continuous monitoring of screen activity
with 
improve  mental  health.
Screen-based  systems  might  rival  the  diagnostic  accuracy  of
traditional  methods  for  some  disorders.  Studies  estimate,  for
example, that up to 60% of people with depression are never
diagnosed [77,78], and even those connected to care often face
delays in appointments, diagnosis, and treatment initiation [79].
Screen summaries might accelerate care by offering behavioral
insights  prior  to  intake  or  as  indicators  of  treatment
effectiveness.

Determining the clinical use of idiographic tracking will require
research to establish optimal baseline collection periods, which
may  vary  by  individual.  While  longer  data  collection  can
enhance  accuracy,  even  shorter  periods  could  yield  valuable
insights. For example, smartphone monitoring during the weeks
between initial clinician contact and the first appointment, or
in  critical  postdischarge  periods,  could  inform  preliminary
evaluations  and  adaptive  interventions.  These  monitoring
systems could feed data into clinician dashboards and support
the implementation of just-in-time adaptive interventions [80].
Importantly,  such  tools  are  intended  to  augment  rather  than
replace direct patient-clinician interactions, which require robust
support resources.

JMIR Form Res 2025 | vol. 9 | e59875 | p. 10
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

Limitations of the Study
This  longitudinal  study,  conducted  with  a  small,  nonclinical
sample  of  female  Android  phone  users,  was  not  intended  to
provide population-level conclusions about the prevalence of
media  and  mental  health  relationships  nationally  or  within
subgroups.  Avoiding  generalization  at 
this  stage  helps
circumvent the small sample fallacy [81]. Our intent was to first
understand the unique media dosage and mental health indicators
important  for  individuals  without  prematurely  investing  in  a
research strategy aimed at extensive between-subject variability
that we believe has resulted in considerable ambiguity in this
literature.  This  bottom-up  inductive  approach  celebrates
idiosyncrasy  and  prioritizes  individual  models  as  a  first  step
toward  building  models  that  might  apply  to  larger  groups  of
people. We have successfully demonstrated that it is possible
to  find  strong,  individualized  relationships  with  granular
measures and longitudinal data.

Our analysis focused on a limited set of variables: 6 media use
metrics and 5 mental health measures. Many additional factors
could influence within-person associations between media use
and mental health. Notably, data collection coincided with the
height  of  the  COVID-19  pandemic.  Although  none  of  the
participants contracted the virus, the pandemic’s broader effects
may have shaped their mental health and media use behaviors.
Future analyses could examine how contextual factors, such as
global or personal life events, moderate these relationships. For
example,  exploring  interactions  between  media  use,  sleep
patterns,  and  mental  health  outcomes  [82,83],  or  identifying
whether media use acts as a supportive resource [84,85] or an
additional stressor [86,87] could inform context-aware models
that better capture individual contingencies.

Future Work and Conclusions
While  new  computational  methods  enable  the  collection  and
analysis  of  large  datasets,  they  often  focus  on  aggregated
measures, obscuring person-specific longitudinal insights and
yielding ambiguous population-level conclusions. Our method
emphasizes  the  importance  of  a  person-specific  approach
applicable to new datasets. A key recommendation for extending
this  investigation  is  to  maintain  this  individual  focus  and
compare people based on similarities between models derived
for  single  individuals,  rather  than  relying  solely  on  priori

groupings  based  on  demographics  or  other  psychosocial
characteristics. When idiographic models are available for many
individuals,  researchers  can  use  clustering,  latent  class,  and
mixture  models  to  quantify  and  examine  between-person
similarities and differences [88-90]. One such method suggested
by  Ram  et  al  [88]  involves  calculating  Tucker  congruence
coefficients  [91]  that  compare  parameter  estimates  (eg,  the
canonical  variates)  for  each  pair  of  individuals  in  a  larger
sample.  Importantly,  this  approach  entails  specifying  and
modeling each person’s data separately, as done in this study,
before identifying shared patterns. Rather than assuming a priori
commonalities (eg, based on sex or personality), this bottom-up
paradigm uncovers the full range of person-specific solutions,
which  can  then  inform  theory,  policy,  and  interventions
[18,88,92,93].

Future  work  will  expand  on  the  metrics  presented  here,
integrating  richer  variables  through  our  computational  assay
[20]  and  identifying  screen  content  characteristics—such  as
words,  objects,  emotional  arousal,  and  environmental
features—using advanced artificial intelligence models. These
granular data can help refine our understanding of how different
media use patterns related to mental health. While traditional
screen  time  measures,  often  derived  from  self-reports,  have
been criticized for their imprecision [94], this study suggests
that accurate, granular recordings of screen behavior can reveal
strong associations for some individuals. Similar increments in
the precision of assessing media use have paid off in the study
of  other  media  effects;  for  example,  exposure  to  political
information [95], advertising [94], and food content in digital
media [30]. Our ongoing work also includes open-sourcing the
most up-to-date Screenomics app and toolset [96].

The idiographic filter approach, producing individual models
1 person at a time, may initially seem to risk overfocusing on
small samples. However, there may not be a shorter route to
useful  answers  about  media  use  and  mental  health.  This  is
especially true if we want to retain media use and mental health
as important and psychologically complex categories of digital
and non-digital life. The present results suggest that to advance
research  addressing  media  use  and  mental  health  problems
generally, we may need to seek answers applicable to one person
at a time; that is, we must embrace idiosyncrasy, not ignore it.

Acknowledgments
This project was partially funded by an internal Stanford University seed grant from the Stanford Medical School (Spectrum
SPADA).

Data Availability
All deidentified data used and reported in this study, along with the code for analysis and visualizations, are available from the
corresponding author upon reasonable request.

Authors' Contributions
TNR, NR, and BR did the inception and design of the study; MC, AYL, and BR drafted the manuscript and did data interpretation;
NR,  MC,  and  NH  did  data  analysis  and  strategy;  AM  and  JH  advised  on  literature  review,  mental  health  assessments,  and
interpretations;  DM  and  AAGT  organized  data  acquisition  and  data  management.  All  authors  have  edited  the  manuscript  in
multiple versions and accept responsibility for the entire content of this manuscript.

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 11
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

Conflicts of Interest
DM is a founder of Screenlake Inc, a startup company focusing on smartphone data collection and analysis for the purpose of
market intelligence. His involvement in the present study was the design and management of data collection during his doctoral
studies, which took place prior to the founding of the company. JH consults for YouTube and Google on issues related to social
media and receives compensation for these services. However, his contribution to this paper is solely his own work. The other
authors declare no competing interests.

Multimedia Appendix 1
Supplementary Information.
[DOCX File , 31 KB-Multimedia Appendix 1]

Multimedia Appendix 2
Permutation distribution histograms. This figure displays histograms of the permutation distributions of 1,000 permuted canonical
correlations for each participant (A to E). To assess the statistical significance of the observed canonical correlations, we conducted
permutation  tests  using  Wilks'  lambda  by  randomly  permuting  each  individual’s  data,  creating  a  null  distribution.  This  null
distribution represents correlations expected by chance—meaning the values that would arise if there were no systematic relationship
between media use and mental health variables and any observed associations were purely random. The histograms display these
chance-based distributions under the null hypothesis, with observed canonical correlations indicated by red dashed lines to evaluate
their statistical significance. The test statistic shown in each histogram is Wilks' lambda. For Participant E, the result is nonsignificant
(P> 0.05), suggesting that the observed correlation cannot be confirmed as statistically significant. For the other participants, the
observed correlations are confirmed by the permutation test.
[PNG File , 5001 KB-Multimedia Appendix 2]

References

1.

2.

3.

Sohn SY, Rees P, Wildridge B, Kalk NJ, Carter B. Prevalence of problematic smartphone usage and associated mental
health outcomes amongst children and young people: a systematic review, meta-analysis and GRADE of the evidence.
BMC Psychiatry. 2019;19(1):356. [FREE Full text] [doi: 10.1186/s12888-019-2350-x] [Medline: 31779637]
Kushlev K, Leitao MR. The effects of smartphones on well-being: theoretical integration and research agenda. Curr Opin
Psychol. 2020;36:77-82. [doi: 10.1016/j.copsyc.2020.05.001] [Medline: 32563707]
Hancock J, Liu SX, Luo M, Mieczkowski H. Psychological well-being and social media use: a meta-analysis of associations
between social media use and depression, anxiety, loneliness, eudaimonic, hedonic and social well-being. SSRN J. 2022:84.
[doi: 10.2139/ssrn.4053961]

4. Marciano L, Ostroumova M, Schulz PJ, Camerini AL. Digital media use and adolescents' mental health during the Covid-19

5.

6.

7.

pandemic: a systematic review and meta-analysis. Front Public Health. 2021;9:793868. [FREE Full text] [doi:
10.3389/fpubh.2021.793868] [Medline: 35186872]
Nawi A, Zameran FA. Exploring the relationship between smartphone use and adolescent well-being: a systematic literature
review. In: Rajakumar G, Du KL, Vuppalapati C, Beligiannis GN, editors. Intelligent Communication Technologies and
Virtual Mobile Networks. Singapore. Springer; 2023.
Harari GM, Müller SR, Aung MS, Rentfrow PJ. Smartphone sensing methods for studying behavior in everyday life. Curr
Opin Behav Sci. 2017;18:83-90. [doi: 10.1016/j.cobeha.2017.07.018]
Brinberg M, Bodie GD, Solomon DH, Jones SM, Ram N. Examining individual differences in how interaction behaviors
change over time: a dyadic multinomial logistic growth modeling approach. Psychol Methods. 2023. [doi:
10.1037/met0000605] [Medline: 37561491]

8. Mao C, Bayer JB, Ross MQ, Rhee L, Le HTK, Mount J, et al. Perceived vs. observed mHealth behavior: a naturalistic

9.

investigation of tracking apps and daily movement. Mobile Media Commun. 2023;11(3):526-548. [doi:
10.1177/20501579221149823]
Barnett ML, Gonzalez A, Miranda J, Chavira DA, Lau AS. Mobilizing community health workers to address mental health
disparities for underserved populations: a systematic review. Adm Policy Ment Health. 2018;45(2):195-211. [FREE Full
text] [doi: 10.1007/s10488-017-0815-0] [Medline: 28730278]

10. Chancellor S, De Choudhury M. Methods in predictive techniques for mental health status on social media: a critical review.

NPJ Digit Med. 2020;3:43. [FREE Full text] [doi: 10.1038/s41746-020-0233-7] [Medline: 32219184]

11. Torous J, Choudhury T, Barnett I, Keshavan M, Kane J. Smartphone relapse prediction in serious mental illness: a pathway
towards personalized preventive care. World Psychiatry. 2020;19(3):308-309. [FREE Full text] [doi: 10.1002/wps.20805]
[Medline: 32931109]

12. Orben A, Przybylski AK, Blakemore SJ, Kievit RA. Windows of developmental sensitivity to social media. Nat Commun.

2022;13(1):1649. [FREE Full text] [doi: 10.1038/s41467-022-29296-3] [Medline: 35347142]

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 12
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

13. Orben A, Blakemore SJ. How social media affects teen mental health: a missing link. Nature. 2023;614(7948):410-412.

[doi: 10.1038/d41586-023-00402-9] [Medline: 36788371]

14. Beyens I, Pouwels JL, van Driel II, Keijsers L, Valkenburg PM. Social media use and adolescents’ well-being: developing
a typology of person-specific effect patterns. Commun Res. 2021;51(6):691-716. [doi: 10.1177/00936502211038196]

15. Valkenburg PM, Meier A, Beyens I. Social media use and its impact on adolescent mental health: an umbrella review of

the evidence. Curr Opin Psychol. 2022;44:58-68. [FREE Full text] [doi: 10.1016/j.copsyc.2021.08.017] [Medline: 34563980]

16. Bryant J, Oliver MB. Media Effects: Advances in Theory and Research. New York, NY. Routledge; 2009.
17. McLeod JM, Reeves B. On the nature of mass media effects. In: Withey SB, Abeles RP, editors. Television and Social

Behavior: Beyond Violence and Children/A Report of the Committee on Television and Social Behavior, Social Science
Research Council. Oxfordshire, United Kingdom. Routledge; 2013.

18. Nesselroade JR, Gerstorf D, Hardy SA, Ram N. Focus article: idiographic filters for psychological constructs. Meas

Interdiscip Res Perspect. 2007;5(4):217-235. [doi: 10.1080/15366360701741807]

19. Thompson B. Canonical Correlation Analysis: Uses and Interpretation. Washington, DC. Sage Publications; 1984.
20. Ram N, Haber N, Robinson TN, Reeves B. Binding the person-specific approach to modern AI in the human screenome

project: moving past generalizability to transferability. Multivariate Behav Res. 2024;59(6):1211-1219. [doi:
10.1080/00273171.2023.2229305] [Medline: 37439508]

21. Reeves B, Robinson T, Ram N. Time for the Human Screenome Project. Nature. 2020;577(7790):314-317. [doi:

10.1038/d41586-020-00032-5] [Medline: 31942062]

22. Kessler RC, Adler L, Ames M, Demler O, Faraone S, Hiripi E, et al. The World Health Organization Adult ADHD

Self-Report Scale (ASRS): a short screening scale for use in the general population. Psychol Med. 2005;35(2):245-256.
[doi: 10.1017/s0033291704002892] [Medline: 15841682]

23. Chen R, Mias GI, Li-Pook-Than J, Jiang L, Lam HYK, Chen R, et al. Personal omics profiling reveals dynamic molecular
and medical phenotypes. Cell. 2012;148(6):1293-1307. [FREE Full text] [doi: 10.1016/j.cell.2012.02.009] [Medline:
22424236]

24. Rozgonjuk D, Levine JC, Hall BJ, Elhai JD. The association between problematic smartphone use, depression and anxiety

symptom severity, and objectively measured smartphone use over one week. Comput Hum Behav. 2018;87:10-17. [doi:
10.1016/j.chb.2018.05.019]

25. Alloy LB, Urošević S, Abramson LY, Jager-Hyman S, Nusslock R, Whitehouse WG, et al. Progression along the bipolar
spectrum: a longitudinal study of predictors of conversion from bipolar spectrum conditions to bipolar I and II disorders.
J Abnorm Psychol. 2012;121(1):16-27. [FREE Full text] [doi: 10.1037/a0023973] [Medline: 21668080]

26. McInnis MG, Andreassen OA, Andreazza AC, Alon U, Berk M, Brister T, et al. Strategies and foundations for scientific
discovery in longitudinal studies of bipolar disorder. Bipolar Disord. 2022;24(5):499-508. [FREE Full text] [doi:
10.1111/bdi.13198] [Medline: 35244317]

27. Keller MB, Lavori PW, Mueller TI, Endicott J, Coryell W, Hirschfeld RM, et al. Time to recovery, chronicity, and levels

of psychopathology in major depression. a 5-year prospective follow-up of 431 subjects. Arch Gen Psychiatry.
1992;49(10):809-816. [doi: 10.1001/archpsyc.1992.01820100053010] [Medline: 1417434]

28. Crocetti E, Klimstra T, Keijsers L, Hale WW, Meeus W. Anxiety trajectories and identity development in adolescence: a

five-wave longitudinal study. J Youth Adolesc. 2009;38(6):839-849. [doi: 10.1007/s10964-008-9302-y] [Medline: 19636785]

29. Buecker S, Luhmann M, Haehner P, Bühler JL, Dapp LC, Luciano EC, et al. The development of subjective well-being
across the life span: a meta-analytic review of longitudinal studies. Psychol Bull. 2023;149(7-8):418-446. [doi:
10.1037/bul0000401]

30. Ram N, Yang X, Cho MJ, Brinberg M, Muirhead F, Reeves B, et al. Screenomics: a new approach for observing and

studying individuals' digital lives. J Adolesc Res. 2020;35(1):16-50. [FREE Full text] [doi: 10.1177/0743558419883362]
[Medline: 32161431]

31. Humphreys L. The Qualified Self: Social Media and the Accounting of Everyday Life. Cambridge, MA. MIT Press; 2018.
32. Conway CC, Forbes MK, Forbush KT, Fried EI, Hallquist MN, Kotov R, et al. A hierarchical taxonomy of psychopathology

can transform mental health research. Perspect Psychol Sci. 2019;14(3):419-436. [FREE Full text] [doi:
10.1177/1745691618810696] [Medline: 30844330]

33. Nock MK, Kessler RC, Franklin JC. Risk factors for suicide ideation differ from those for the transition to suicide attempt:
the importance of creativity, rigor, and urgency in suicide research. Clin Psychol Sci Pract. 2016;23(1):31-34. [doi:
10.1037/h0101734]

34. Nock MK, Banaji MR. Prediction of suicide ideation and attempts among adolescents using a brief performance-based test.
J Consult Clin Psychol. 2007;75(5):707-715. [FREE Full text] [doi: 10.1037/0022-006X.75.5.707] [Medline: 17907852]
35. Robinaugh DJ, Brown ML, Losiewicz OM, Jones PJ, Marques L, Baker AW. Towards a precision psychiatry approach to
anxiety disorders with ecological momentary assessment: the example of panic disorder. Gen Psychiatr. 2020;33(1):e100161.
[FREE Full text] [doi: 10.1136/gpsych-2019-100161] [Medline: 32175524]

36. Chahal R, Ho TC, Miller JG, Borchers LR, Gotlib IH. Sex-specific vulnerability to depressive symptoms across adolescence
and during the COVID-19 pandemic: the role of the cingulum bundle. JCPP Adv. 2022;2(1):e12061. [FREE Full text] [doi:
10.1002/jcv2.12061] [Medline: 35572852]

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 13
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

37. Hardoon DR, Szedmak S, Shawe-Taylor J. Canonical correlation analysis: an overview with application to learning methods.

Neural Comput. 2004;16(12):2639-2664. [doi: 10.1162/0899766042321814] [Medline: 15516276]

38. Orben A. Teenagers, screens and social media: a narrative review of reviews and key studies. Soc Psychiatry Psychiatr

39.

Epidemiol. 2020;55(4):407-414. [doi: 10.1007/s00127-019-01825-4] [Medline: 31925481]
Schimmack U, Krause P, Wagner GG, Schupp J. Stability and change of well being: an experimentally enhanced latent
state-trait-error analysis. Soc Indic Res. 2009;95(1):19-31. [doi: 10.1007/s11205-009-9443-8]

40. Liu X, Ping S, Gao W. Changes in undergraduate students' psychological well-being as they experience university life. Int

J Environ Res Public Health. 2019;16(16):2864. [FREE Full text] [doi: 10.3390/ijerph16162864] [Medline: 31405114]

41. Odgers CL, Jensen MR. Annual research review: adolescent mental health in the digital age: facts, fears, and future directions.
J Child Psychol Psychiatry. 2020;61(3):336-348. [FREE Full text] [doi: 10.1111/jcpp.13190] [Medline: 31951670]
42. Yoon S, Kleinman M, Mertz J, Brannick M. Is social network site usage related to depression? A meta-analysis of

Facebook-depression relations. J Affect Disord. 2019;248:65-72. [doi: 10.1016/j.jad.2019.01.026] [Medline: 30711871]

43. Houben M, Van Den Noortgate W, Kuppens P. The relation between short-term emotion dynamics and psychological
well-being: a meta-analysis. Psychol Bull. 2015;141(4):901-930. [doi: 10.1037/a0038822] [Medline: 25822133]
44. Meier A, Reinecke L. Computer-mediated communication, social media, and mental health: a conceptual and empirical

meta-review. Commun Res. 2020;48(8):1182-1209. [doi: 10.1177/0093650220958224]

45. Vanden Abeele MMP, Halfmann A, Lee EWJ. Drug, demon, or donut? Theorizing the relationship between social media
use, digital well-being and digital disconnection. Curr Opin Psychol. 2022;45:101295. [doi: 10.1016/j.copsyc.2021.12.007]
[Medline: 35123383]

46. Goodman LS, Gilman A. Brunton LL, Knollman BC, editors. Goodman and Gilman's The Pharmacological Basis of

47.

Therapeutics. New York, NY. McGraw Hill; 2022.
Schleidgen S, Friedrich O, Gerlek S, Assadi G, Seifert J. The concept of “interaction” in debates on human-machine
interaction. Humanit Soc Sci Commun. 2023;10(1). [doi: 10.1057/s41599-023-02060-8]

48. Orben A, Meier A, Dalgleish T, Blakemore SJ. Mechanisms linking social media use to adolescent mental health vulnerability.

Nat Rev Psychol. 2024;3(6):407-423. [doi: 10.1038/s44159-024-00307-y]

49. Lee AY, Katz R, Hancock J. The role of subjective construals on reporting and reasoning about social media use. Soc Media

Soc. 2021;7(3):205630512110353. [doi: 10.1177/20563051211035350]

50. Yeykelis L, Cummings JJ, Reeves B. The fragmentation of work, entertainment, e-mail, and news on a personal computer:

motivational predictors of switching between media content. Media Psychol. 2017;21(3):377-402. [doi:
10.1080/15213269.2017.1406805]

51. Reeves B, Ram N, Robinson TN, Cummings JJ, Giles CL, Pan J, et al. Screenomics: A framework to capture and analyze
personal life experiences and the ways that technology shapes them. Hum Comput Interact. 2021;36(2):150-201. [FREE
Full text] [doi: 10.1080/07370024.2019.1578652] [Medline: 33867652]

52. Radloff L. The CES-D Scale: A self-report depression scale for research in the general population. Appl Psychol Meas.

1977;1(3):385-401. [FREE Full text] [doi: 10.1177/014662167700100306]

53. Marteau TM, Bekker H. The development of a six-item short-form of the state scale of the Spielberger State-Trait Anxiety
Inventory (STAI). Br J Clin Psychol. 1992;31(3):301-306. [doi: 10.1111/j.2044-8260.1992.tb00997.x] [Medline: 1393159]

54. Wilkinson D. Screen time trends in the age of COVID-19. SimpleTexting. 2021. URL: https://simpletexting.com/blog/

55.

screen-time-survey [accessed 2023-10-22]
Flynn J. 20 Vital Smartphone Usage Statistics (2023): facts, data, and trends on mobile use in the U.S. Zippia.com. Zippia.
2023. URL: https://www.zippia.com/advice/smartphone-usage-statistics/ [accessed 2024-02-03]

56. Kerai A. Cell phone usage statistics: mornings are for notifications. Reviews.org. URL: https://www.reviews.org/mobile/

57.

58.

cell-phone-addiction/ [accessed 2024-02-03]
Pezeshki A, Scharf LL, Azimi-Sadjadi MR, Lundberg M. Empirical canonical correlation analysis in subspaces. 2004.
Presented at: Conference Record of the Thirty-Eighth Asilomar Conference on Signals, Systems and Computers,; November
7-10, 2004:994-997; Pacific Grove, CA. [doi: 10.1109/acssc.2004.1399288]
Julian LJ. Measures of anxiety: State-Trait Anxiety Inventory (STAI), Beck Anxiety Inventory (BAI), and Hospital Anxiety
and Depression Scale-Anxiety (HADS-A). Arthritis Care Res. 2011;63:S467-S472. [FREE Full text] [doi: 10.1002/acr.20561]
[Medline: 22588767]

59. Vargas-Terrones M, Nagpal TS, Perales M, Prapavessis H, Mottola MF, Barakat R. Physical activity and prenatal depression:
going beyond statistical significance by assessing the impact of reliable and clinical significant change. Psychol Med.
2021;51(4):688-693. [doi: 10.1017/S0033291719003714] [Medline: 32102723]
Spielberger CD, Gorsuch RL, Lushene RE. State-Trait Anxiety Inventory (STAI): Test Manual for Form X. Washington,
DC. Consulting Psychologists Press; 1968.

60.

61. Adler L, Cohen J. Diagnosis and evaluation of adults with attention-deficit/hyperactivity disorder. Psychiatr Clin North

Am. 2004;27(2):187-201. [doi: 10.1016/j.psc.2003.12.003] [Medline: 15063992]

62. Kessler RC, Berglund P, Demler O, Jin R, Merikangas KR, Walters EE. Lifetime prevalence and age-of-onset distributions
of DSM-IV disorders in the national comorbidity survey replication. Arch Gen Psychiatry. 2005;62(6):593-602. [doi:
10.1001/archpsyc.62.6.593] [Medline: 15939837]

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 14
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

JoMingyu. Google Play scraper. Github. URL: https://github.com/JoMingyu/google-play-scraper [accessed 2024-02-05]

63.
64. Rhee L, Bayer JB, Lee DS, Kuru O. Social by definition: how users define social platforms and why it matters. Telematics

Inform. 2021;59:101538. [doi: 10.1016/j.tele.2020.101538]

65. Hotelling H. Relations Between Two Sets of Variates. In: Kotz S, Johnson NL, editors. Breakthroughs in Statistics:

Methodology and Distribution. New York, NY. Springer; 1992.

66. Weenink D. Canonical correlation analysis. 2003. Presented at: Proceedings of the Institute of Phonetic Sciences of the
University of Amsterdam ;25?99; 2003:81-99; University of Amsterdam. URL: https://uvafon.hum.uva.nl/archive/2003/
2003-ifaproc25-Weenink.pdf

67. González I, Déjean S. Package CCA: Canonical correlation analysis. R Foundation for Statistical Computing. 2021. URL:

https://cran.r-project.org/package=CCA [accessed 2024-04-04]

68. Braghieri L, Levy R, Makarin A. Social media and mental health. Am Econ Rev. 2022;112(11):3660-3693. [doi:

10.1257/aer.20211218]

69. Müller SR, Peters H, Matz SC, Wang W, Harari GM. Investigating the relationships between mobility behaviours and
indicators of subjective well–being using smartphone–based experience sampling and GPS tracking. Eur J Pers.
2020;34(5):714-732. [doi: 10.1002/per.2262]
Johnson AL. Changes in mental health and treatment, 1997-2017. J Health Soc Behav. 2021;62(1):53-68. [doi:
10.1177/0022146520984136] [Medline: 33480305]

70.

71. Bailey ER, Matz SC, Youyou W, Iyengar SS. Authentic self-expression on social media is associated with greater subjective
well-being. Nat Commun. 2020;11(1):4889. [FREE Full text] [doi: 10.1038/s41467-020-18539-w] [Medline: 33024115]
72. Brailovskaia J, Delveaux J, John J, Wicker V, Noveski A, Kim S, et al. Finding the "sweet spot" of smartphone use: reduction
or abstinence to increase well-being and healthy lifestyle?! An experimental intervention study. J Exp Psychol Appl.
2023;29(1):149-161. [doi: 10.1037/xap0000430] [Medline: 35389685]

73. Gerbner G, Gross L, Signorielli N, Morgan M. Aging with television: images on television drama and conceptions of social

reality. J Commun. 1980;30(1):37-47. [doi: 10.1111/j.1460-2466.1980.tb01766.x] [Medline: 7372841]

74. Clark JL, Green MC. Self-fulfilling prophecies: perceived reality of online interaction drives expected outcomes of online

communication. Personal Individual Differ. 2018;133:73-76. [doi: 10.1016/j.paid.2017.08.031]

75. Boers E, Afzali MH, Newton N, Conrod P. Association of screen time and depression in adolescence. JAMA Pediatr.

2019;173(9):853-859. [FREE Full text] [doi: 10.1001/jamapediatrics.2019.1759] [Medline: 31305878]

76. Molenaar PCM, Campbell CG. The new person-specific paradigm in psychology. Curr Dir Psychol Sci. 2009;18(2):112-117.

[doi: 10.1111/j.1467-8721.2009.01619.x]

77. Williams SZ, Chung GS, Muennig PA. Undiagnosed depression: a community diagnosis. SSM Popul Health. 2017;3:633-638.

[FREE Full text] [doi: 10.1016/j.ssmph.2017.07.012] [Medline: 29349251]

78. Handy A, Mangal R, Stead TS, Coffee RL, Ganti L. Prevalence and impact of diagnosed and undiagnosed depression in
the United States. Cureus. 2022;14(8):e28011. [FREE Full text] [doi: 10.7759/cureus.28011] [Medline: 36134073]
79. Boerema AM, Ten Have M, Kleiboer A, de Graaf R, Nuyen J, Cuijpers P, et al. Demographic and need factors of early,

delayed and no mental health care use in major depression: a prospective study. BMC Psychiatry. 2017;17(1):367. [FREE
Full text] [doi: 10.1186/s12888-017-1531-8] [Medline: 29145820]

80. Nahum-Shani I, Smith SN, Spring BJ, Collins LM, Witkiewitz K, Tewari A, et al. Just-in-time adaptive interventions

(JITAIs) in mobile health: key components and design principles for ongoing health behavior support. Ann Behav Med.
2018;52(6):446-462. [FREE Full text] [doi: 10.1007/s12160-016-9830-8] [Medline: 27663578]
Poulton EC. Small sample fallacy. In: Behavioral Decision Theory: A New Approach. Cambridge, MA. Cambridge
University Press; 1994.

81.

82. Li X, Buxton OM, Lee S, Chang AM, Berger LM, Hale L. Sleep mediates the association between adolescent screen time
and depressive symptoms. Sleep Med. 2019;57:51-60. [FREE Full text] [doi: 10.1016/j.sleep.2019.01.029] [Medline:
30897456]

83. Guerrero MD, Barnes JD, Chaput JP, Tremblay MS. Screen time and problem behaviors in children: exploring the mediating

role of sleep duration. Int J Behav Nutr Phys Act. 2019;16(1):105. [FREE Full text] [doi: 10.1186/s12966-019-0862-x]
[Medline: 31727084]

84. Zhang K, Kim K, Silverstein NM, Song Q, Burr JA. Social media communication and loneliness among older adults: the

mediating roles of social support and social contact. Gerontologist. 2021;61(6):888-896. [doi: 10.1093/geront/gnaa197]
[Medline: 33284972]

85. Lisitsa E, Benjamin KS, Chun SK, Skalisky J, Hammond LE, Mezulis AH. Loneliness among young adults during COVID-19
pandemic: the mediational rolea of social media use and social support seeking. J Soc Clin Psychol. 2020;39(8):708-726.
[doi: 10.1521/jscp.2020.39.8.708]

86. Zhao N, Zhou G. Social media use and mental health during the COVID-19 pandemic: moderator role of disaster stressor
and mediator role of negative affect. Appl Psychol Health Well Being. 2020;12(4):1019-1038. [FREE Full text] [doi:
10.1111/aphw.12226] [Medline: 32945123]

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 15
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Cerit et al

87.

Seo J, Lee CS, Lee YJ, Bhang SY, Lee D. The type of daily life stressors associated with social media use in adolescents
with problematic internet/smartphone use. Psychiatry Investig. 2021;18(3):241-248. [FREE Full text] [doi:
10.30773/pi.2020.0060] [Medline: 33735548]

88. Ram N, Brose A, Molenaar PCM. Dynamic factor analysis: modeling person-specific process. In: The Oxford Handbook

89.

of Quantitative Methods. New York, NY. Oxford University Press; 2013:441.
van der Nest G, Lima Passos V, Candel MJJM, van Breukelen GJP. An overview of mixture modelling for latent evolutions
in longitudinal data: modelling approaches, fit statistics and software. Adv Life Course Res. 2020;43:100323. [doi:
10.1016/j.alcr.2019.100323] [Medline: 36726256]

90. Gates KM, Lane ST, Varangis E, Giovanello K, Guskiewicz K. Unsupervised classification during time-series model

building. Multivariate Behav Res. 2017;52(2):129-148. [FREE Full text] [doi: 10.1080/00273171.2016.1256187] [Medline:
27925768]

91. Lorenzo-Seva U, ten Berge JMF. Tucker's congruence coefficient as a meaningful index of factor similarity. Methodology.

2006;2(2):57-64. [doi: 10.1027/1614-2241.2.2.57]

92. Brose A, Ram N. Within-person factor analysis: Modeling how the individual fluctuates changes across time. In: Mehl
MR, editor. Handbook of Research Methods for Studying Daily Life. New York, NY. Guilford Press; 2012:459.
93. Yang X, Ram N, Lougheed JP, Molenaar PCM, Hollenstein T. Adolescents' emotion system dynamics: network-based
analysis of physiological and emotional experience. Dev Psychol. 2019;55(9):1982-1993. [FREE Full text] [doi:
10.1037/dev0000690] [Medline: 31464499]

94. Lee J, Hamilton JT, Ram N, Roehrick K, Reeves B. The psychology of poverty and life online: natural experiments on the

effects of smartphone payday loan ads on psychological stress. Inf Commun Soc. 2022;26(14):2775-2796. [doi:
10.1080/1369118x.2022.2109982]

95. Muise D, Hosseinmardi H, Howland B, Mobius M, Rothschild D, Watts DJ. Quantifying partisan news diets in web and

TV audiences. Sci Adv. 2022;8(28):eabn0083. [FREE Full text] [doi: 10.1126/sciadv.abn0083] [Medline: 35857498]
96. Yee AZH, Yu R, Lim SS, Lim KH, Dinh TTA, Loh L, et al. ScreenLife Capture: an open-source and user-friendly framework
for collecting screenomes from android smartphones. Behav Res Methods. 2023;55(8):4068-4085. [FREE Full text] [doi:
10.3758/s13428-022-02006-z] [Medline: 36289177]

Abbreviations

ADHD:  attention-deficit/hyperactivity disorder
CCA:  canonical correlation analysis
HIPAA:  Health Insurance Portability and Accountability Act
pCCA:  p-technique canonical correlation analysis

Edited by A Mavragani; submitted 24.04.24; peer-reviewed by A AL-Asadi, T Seibers; comments to author 20.08.24; revised version
received 15.10.24; accepted 17.12.24; published 26.02.25

Please cite as:
Cerit M, Lee AY, Hancock J, Miner A, Cho M-J, Muise D, Garròn Torres A-A, Haber N, Ram N, Robinson TN, Reeves B
Person-Specific Analyses of Smartphone Use and Mental Health: Intensive Longitudinal Study
JMIR Form Res 2025;9:e59875
URL: https://formative.jmir.org/2025/1/e59875
doi: 10.2196/59875
PMID: 39808832

©Merve Cerit, Angela Y Lee, Jeffrey Hancock, Adam Miner, Mu-Jung Cho, Daniel Muise, Anna-Angelina Garròn Torres, Nick
Haber,  Nilam  Ram,  Thomas  N  Robinson,  Byron  Reeves.  Originally  published 
in  JMIR  Formative  Research
(https://formative.jmir.org),  26.02.2025.  This  is  an  open-access  article  distributed  under  the  terms  of  the  Creative  Commons
Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction
in  any  medium,  provided  the  original  work,  first  published  in  JMIR  Formative  Research,  is  properly  cited.  The  complete
bibliographic information, a link to the original publication on https://formative.jmir.org, as well as this copyright and license
information must be included.

https://formative.jmir.org/2025/1/e59875

XSL•FO
RenderX

JMIR Form Res 2025 | vol. 9 | e59875 | p. 16
(page number not for citation purposes)
