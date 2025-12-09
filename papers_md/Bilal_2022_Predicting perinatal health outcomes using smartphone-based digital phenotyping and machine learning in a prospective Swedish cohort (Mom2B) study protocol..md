# Bilal_2022_Predicting perinatal health outcomes using smartphone-based digital phenotyping and machine learning in a prospective Swedish cohort (Mom2B) study protocol.

Open access 

Protocol

Predicting perinatal health outcomes 
using smartphone- based digital 
phenotyping and machine learning in a 
prospective Swedish cohort (Mom2B): 
study protocol

Ayesha M Bilal      ,1,2 Emma Fransson,3,4 Emma Bränn,3 Allison Eriksson,2,3 
Mengyu Zhong,2,5 Karin Gidén,3 Ulf Elofsson,1,3 Cathrine Axfors,3 
Alkistis Skalkidou,3 Fotios C Papadopoulos1

To cite: Bilal AM, Fransson E, 
Bränn E, et al.  Predicting 
perinatal health outcomes 
using smartphone- based digital 
phenotyping and machine 
learning in a prospective 
Swedish cohort (Mom2B): 
study protocol. BMJ Open 
2022;12:e059033. doi:10.1136/
bmjopen-2021-059033

 ► Prepublication history and 
additional supplemental material 
for this paper are available 
online. To view these files, 
please visit the journal online 
(http://dx.doi.org/10.1136/ 
bmjopen-2021-059033).

AS and FCP contributed equally.

Received 12 November 2021
Accepted 12 April 2022

© Author(s) (or their 
employer(s)) 2022. Re- use 
permitted under CC BY. 
Published by BMJ.

For numbered affiliations see 
end of article.

Correspondence to
Ayesha M Bilal;  
 ayesha. bilal@ neuro. uu. se

ABSTRACT
Introduction  Perinatal complications, such as perinatal 
depression and preterm birth, are major causes of 
morbidity and mortality for the mother and the child. 
Prediction of high risk can allow for early delivery of 
existing interventions for prevention. This ongoing 
study aims to use digital phenotyping data from the 
Mom2B smartphone application to develop models 
to predict women at high risk for mental and somatic 
complications.
Methods and analysis  All Swedish- speaking women 
over 18 years, who are either pregnant or within 3 months 
postpartum are eligible to participate by downloading 
the Mom2B smartphone app. We aim to recruit at least 
5000 participants with completed outcome measures. 
Throughout the pregnancy and within the first year 
postpartum, both active and passive data are collected 
via the app in an effort to establish a participant’s digital 
phenotype. Active data collection consists of surveys 
related to participant background information, mental and 
physical health, lifestyle, and social circumstances, as 
well as voice recordings. Participants’ general smartphone 
activity, geographical movement patterns, social media 
activity and cognitive patterns can be estimated through 
passive data collection from smartphone sensors and 
activity logs. The outcomes will be measured using 
surveys, such as the Edinburgh Postnatal Depression 
Scale, and through linkage to national registers, from 
where information on registered clinical diagnoses and 
received care, including prescribed medication, can be 
obtained. Advanced machine learning and deep learning 
techniques will be applied to these multimodal data in 
order to develop accurate algorithms for the prediction of 
perinatal depression and preterm birth. In this way, earlier 
intervention may be possible.
Ethics and dissemination  Ethical approval has been 
obtained from the Swedish Ethical Review Authority 
(dnr: 2019/01170, with amendments), and the project 
fully fulfils the General Data Protection Regulation 
(GDPR) requirements. All participants provide consent to 
participate and can withdraw their participation at any 
time. Results from this project will be disseminated in 

Strengths and limitations of this study

 ► The study collects large- scale, temporally sensitive 
data  regarding  the  user’s  behaviours  in  the  real 
world.

 ► End  users’  feedback  collected  allows  for  app  up-

dates and improvements.

 ► The passive data collection is expected to have low-

er attrition rate.

 ► The active data collection is prone to suffer from a 

higher attrition rate.

 ► There are high costs associated with recruiting par-
ticipants and maintaining frontend and backend for 
the smartphone app.

international peer- reviewed journals and presented in 
relevant conferences.

is 

INTRODUCTION
Optimal  maternal  health 
important 
throughout  pregnancy,  childbirth  and  the 
postpartum  period  to  ensure  the  full  poten-
tial  for  the  mother,  infant  and  family  to  get  a 
good  start.1  Two  health  conditions  that  are 
important to address in order to reach a goal of 
good maternal health are perinatal depression 
(PND) and preterm birth (PTB), both affecting 
about every 10th pregnancy worldwide.2 3

Perinatal depression
PND is an episode of major depression with 
onset  anytime  during  pregnancy  and  up  to 
4  weeks  postpartum,4  although  in  research 
settings, a period of up to 1 year postpartum 
is  often  considered.5  Antenatal  depres-
sion  affects  between  7%  and  13%  of  preg-
nant  women,6  and  postpartum  depression 
(PPD)  is  estimated  to  affect  between  10% 
and  20%  of  all  newly  delivered  mothers,2 

1

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033Open access 

while  many  women  experience  persistent  depression 
throughout  the  perinatal  period.7  PND  is  distinct  from 
‘baby  blues’,  which  are  commonly  experienced  symp-
toms  of  low  mood  and  anxiety  that  subside  within  2 
weeks  postpartum.  PND  is  both  emotionally  and  physi-
cally  debilitating  like  major  depression,  with  additional 
risks  related  to  the  pregnancy  and  birth,  such  as  PTB, 
low birth weight, pre- eclampsia and placental abnormal-
ities.8–10 Moreover, it is associated with retained maternal 
weight postpartum,11 decreased breast feeding,12–14 poor 
maternal sleep15 and poor perinatal quality of life.16 PND 
can also compromise the critical mother–infant bond, as 
it affects the mother’s caregiving abilities and adaptation 
to the maternal role,16 17 and has a long- term impact on 
the  child’s  cognitive,  emotional  and  behavioural  devel-
opment.18 19 Furthermore, PND can be characterised by 
the occurrence of self- harm thoughts, which are linked 
to  long- term  somatic  and  psychiatric  morbidity,20  and 
increased  maternal  mortality  from  suicide  in  the  first 
year postpartum.21

The  aetiology  of  PND  is  multifactorial,  including 
biological,  genetic,  psychological  and  social  factors, 
such  as  stressful  life  events,  social  support,  domestic 
violence,  childhood  adversity,  history  of  depression  and 
anxiety,  low  self- esteem  and  even  personality  traits  like 
resilience.15 22–24 Despite this knowledge, detecting PND 
remains a challenge for the healthcare system, with one 
review  finding  that  around  30%–70%  of  cases  go  unde-
tected and only 15% receive adequate treatment.25 26

Current screening protocols include the Edinburgh Post-
natal Depression Scale (EPDS)27 during postpartum visits to 
assess  risk  of  PND.28  However,  early  detection  of  PND  has 
remained  challenging  for  many  reasons,  including  incon-
sistencies in screening practices,29 and failure to distinguish 
depressive symptoms due to their overlap with typical somatic 
experiences  in  the  early  postpartum  period.30  Further-
more,  women  may  hesitate  to  seek  care  possibly  because 
of  the  depression  itself,  but  also  stigma  and  fear  of  being 
judged  as  an  imperfect  mother,  as  well  as  concerns  about 
antidepressant use during pregnancy and breast feeding.31 
Besides, in- clinic screening frequently relies on retrospective 
self- reports  of  diagnostically  relevant  information,  making 
it  susceptible  to  errors  and  biases  associated  with  autobi-
ographical recollection.32

Unquestionably,  more  efficient  and  effective  methods 
for  predicting  PND  in  mothers  are  needed  to  enable 
early  identification  and  intervention,  thus  improving 
prognosis, and reducing the burden of disease.33 Previous 
studies that have attempted to develop predictive models 
of maternal depression primarily focus on the postpartum 
period  only.34–39  Few  have  used  social  media  finger-
prints40–42  or  biomarkers36  43  in  their  models,  and  these 
studies  largely  depended  on  psychometric  self- reports 
and limited modalities. These drawbacks compromise the 
predictive power of the models and illustrate why multi-
variate,  real- time  and  unobtrusive  approaches  to  data 
collection and symptom monitoring must be encouraged 
to develop better predictive models.

2

Preterm birth
Among somatic pregnancy complications, PTB is a major 
cause  of  neonatal  death,  as  well  as  of  poor  long- term 
health  in  children,  affecting  approximately  15  million 
babies worldwide each year.44 45 In Sweden, the PTB rate 
is about 6%,46 which is a relatively low number compared 
with  the  international  average  of  over  10%.44  Like 
PND,  the  aetiology  of  PTB  is  multifactorial,  including 
previous  PTB,  multifetal  pregnancy,  cervical  insuffi-
ciency,  intrauterine  infections,  vaginal  bleeding  in  the 
second trimester, in- vitro fertilisation, primiparity, as well 
as maternal antenatal stress and depression.47–50 In fact, 
many  risk  factors  overlap  between  PND  and  PTB,  such 
as childhood traumatic events or maltreatment, stressful 
life events, being single or lacking social support, being 
overweight,  smoking  and  low  socioeconomic  status.51  52 
Inflammation  has  been  suggested  as  a  possible  under-
lying pathway for both depression and preterm delivery.53
There are evidence- based interventions for preventing 
or  delaying  PTB  to  optimise  birth  outcomes,  such  as 
smoking  cessation,  progesterone  therapy,  cerclage  in 
women  with  cervical  insufficiency  or  antibiotics.51  54 
However, a major obstacle for the success of these inter-
ventions is the aetiological heterogeneity of PTB, which 
makes it extremely challenging to identify women at high 
risk. In fact, two- thirds of women who experience PTB do 
not present with any risk factors at all.55 Available biolog-
ical  diagnostic  tests  for  PTB  (such  as  fetal  fibronectin) 
lack sufficient positive prediction values.56 Screening for 
cervical length is performed in Sweden for women with a 
history of PTB; however, this is not helpful in primiparous 
women.57

It  can  be  concluded  that  no  single  biomarker  is  suffi-
cient for prediction; multimodal data, including psycho-
social and behavioural factors, should, therefore, be the 
focus of prediction efforts.

Digital phenotyping and big data
Digital  devices  like  smartphones  allow  us  to  capture 
regarding 
moment- by- moment,  objective  data 
the 
in  non- clinical 
patient’s  experiences  and  functions 
settings. This process, known as digital phenotyping,58 allows 
us to collect two kinds of data: active data and passive data. 
Active data refer to data that require user input, such as 
surveys  and  voice  recordings.  Passive  data  refer  to  auto-
matically  collected  data  from  smartphone  sensors  and 
activity logs, which can be used to infer the user’s mobility 
and  sleep  patterns,  digital  social  activity,  smartphone 
usage patterns, and even affective and cognitive changes.
The  Mom2B  smartphone  app  is  developed  using  the 
Beiwe  research  platform  (www.beiwe.org)  from  the 
Harvard  School  of  Public  Health.  It  can  allow  us  to 
capture  digital  phenotyping  data  during  the  perinatal 
period  with  greater  efficiency  and  temporal  sensitivity 
as data collection occurs continuously and in real- world 
contexts, which minimises the risk of recall biases. Such 
apps  could  also  be  integrated  into  the  mother’s  peri-
natal care plan. One drawback of smartphone- based data 

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033collection, in general, is that attrition rate increases with 
longer  follow- up  times59;  however,  this  can  at  least  in 
part be compensated for by the continuous collection of 
passive data.

In  fact,  one  of  the  biggest  advantages  of  smartphone- 
based  digital  phenotyping  is  the  ability  to  collect  multi-
variate, high- volume data, known commonly as big data.60 
Big data are excellent for healthcare research since it can 
facilitate a unique insight into risk factors and the devel-
opment  of  better  diagnostic  frameworks61;  however,  the 
literature  on  big  data  approaches  for  psychiatric  condi-
tions,  particularly  perinatal  mental  health,  is  limited.62 
Nordic  countries  are  in  the  forefront  in  this  respect—
with the Danish National Birth Cohort,63 the Norwegian 
Mother, Father and Child Cohort (MoBa)64 and Autism 
Birth  Cohort  (ABC)65  studies,  and  the  Swedish  Biology, 
Affect,  Stress,  Imaging  and  Cognition  (BASIC)  cohort 
study66—due  to  the  availability  of  nationwide  registers 
with  comprehensive  personal  and  medical  information 
for all pregnant women in these countries. Nonetheless, 
register data, while valuable, lack the multeity, continuity 
and  veracity  offered  by  digital  phenotyping.67  Further-
more,  studies  derived  from  these  cohorts  have  largely 
relied on traditional statistical methods, which are limited 
in their ability to scale to large data sets and identify more 
subtle patterns in data.68

To  date,  few  studies  have  applied  digital  phenotyping 
for prediction of psychiatric conditions, such as relapse in 
schizophrenia69 and severity of mood episodes in bipolar 
disorder.70 In the context of PND, while smartphone apps 
are widely used, their application has been largely focused 
on  screening  and  intervention.71  Only  two  studies  have 
applied digital phenotyping for predicting PPD.34 72 While 
these  studies  have  reported  encouraging  results,  their 
predictive ability is compromised due to limited modali-
ties (using only active data in the form of questionnaires), 
infrequent measurement points and usage of more tradi-
tional  statistical  methods.  The  Mom2B  study  combines 
nationwide health and pregnancy register data with active 
and  passive  data  collected  through  smartphone- based 
digital  phenotyping  to  objectively  monitor  indicators  of 
PND in non- clinical contexts.

In order to harness the full potential of big data, more 
advanced  analytical  methods,  such  as  machine  learning 
(ML) and deep learning (DL), are ideal. ML is an artifi-
cial intelligence approach that refers to various methods 
of  enabling  an  algorithm  to  identify  and  learn  intricate 
patterns  in  data  to  predict  outcomes.73  Modern  ML 
methods,  such  as  deep  neural  networks  (DNNs),  are 
uniquely suited to analysing big data sets as they can detect 
complex,  high- dimensional  interactions  and  structured 
information, without guidance, that can then be used to 
train predictive algorithms. DNN models are comprised 
of multiple ‘hidden’ processing layers, inspired by biolog-
ical  neural  networks,  consisting  of  a  series  of  intercon-
nected nodes that resemble neurons.74 75

Over the last decade, there has been a steady increase 
in  the  use  of  DL  methods  in  medicine.76  However,  few 

Open access

studies have used ML for diagnosis or risk assessment in 
psychiatry, and those that do are often limited by modest 
sample  sizes  and  modalities,  or  from  using  only  tradi-
tional ML techniques.73 77 To our knowledge, Mom2B is 
the first study to adopt a big data approach and use multi-
modal digital phenotyping with advanced ML techniques 
to develop predictive algorithms for PND and PTB.

Objectives
Using large- scale, multimodal data collected through the 
Mom2B smartphone app, together with health and preg-
nancy  information  from  national  registers,  the  primary 
aim of this study is to assess the accuracy of advanced ML 
and DL methods in predicting development of PND (1) 
in the third pregnancy trimester, using data from the first 
trimester, and (2) during the early and late postpartum 
period,  using  data  collected  throughout  pregnancy  and 
childbirth.

A secondary aim of this study is to apply advanced ML 
and  DL  techniques  using  the  multimodal  data  set  to 
predict the risk of PTB.

METHODS AND ANALYSIS
Cohort description
Mom2B  (www.mom2b.se)  is  a  national  ongoing  smart-
phone app- based study; the app was launched at the end 
of  November  2019  to  App  Store  and  Google  Play.  All 
Swedish- speaking  women  above  the  age  of  18  owning 
a  smartphone,  who  are  either  pregnant  or  within  3 
months postpartum, are eligible to participate by regis-
tering and providing consent in the Mom2B app. Partic-
ipating  women  are  also  asked  for  optional  consent  to 
be contacted for additional research studies within and 
from  outside  the  Mom2B  project  (see  online  supple-
mental appendix A). Participant data are then linked to 
psychiatric  and  somatic  health- related  and  pregnancy- 
related  information  available  from  Swedish  national 
registers.

We  aim  to  recruit  at  least  5000  participants  with 
completed  outcome  measures.  Due  to  the  complexity 
of  ML  methods,  it  is  not  possible  to  perform  any  tradi-
tional test of statistical power. However, based on previous 
studies59  78  79,  and  conferring  with  experts  in  artificial 
intelligence, we estimated that this approximate number 
would give us enough material to build robust prediction 
models while accounting for attrition and the prevalence 
rates of the outcomes.

Information about the study is being disseminated on 
social media, and through posters and brochures sent to 
primary  and  maternal  care  centres  across  the  country. 
Figure  1  illustrates  Mom2B  recruitment,  data  collection 
and opt- outs. Table 1 outlines participant characteristics 
of the existing Mom2B cohort based on users who have 
contributed relevant data, along with similar characteris-
tics in the general Swedish population.

3

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033Open access 

Figure 1  From top to bottom, the grey content blocks 
in the main column represent installed apps (downloads 
of the Mom2B app by unique users from either App Store 
(iOS) or Google Play (Android)), registered users (individuals 
who have submitted registration information in the app), 
signed consents (registered users who have consented to 
contributing data, and signed these consents electronically) 
and, finally, data (participants with signed consents who, 
at minimum, have completed the Edinburgh Postnatal 
Depression Scale (EPDS27) at least once). The latter two 
blocks also illustrate the signed consents and available data, 
respectively, by type of data (survey, voice and passive data). 
The intersections of the Venn diagrams are non- exclusive, 
meaning that the number count in the intersection of surveys 
and passive data, for example, can include individuals who 
have also contributed to voice recordings. This flow chart 
reflects data last downloaded on 6 September 2021.

Data collection
The  Mom2B  app  collects  three  types  of  data:  survey 
data, audio recordings, as well as passive data. Data can 
be  collected  from  the  first  week  of  pregnancy,  and  up 
until week 52 after birth. Only data that participants have 
consented for are collected from the time they register to 
the study, and they can change their consent preferences 
anytime in the app if they wish to stop.

questionnaires are used to collect information regarding 
the  participant’s  mental  and  physical  well- being,  and 
history,  personality,  relationships,  as  well  as  perinatal 
and parenthood experiences. They include the EPDS, a 
10- item self- report screening tool with good psychometric 
properties,80 81 used as the primary outcome measure in 
this study to assess depressive symptoms throughout the 
study period. A summary of the timeline of validated and 
self- developed  instruments,  along  with  the  number  of 
occurrences  of  the  survey  throughout  the  study  period, 
can be found in figures 2 and 3, respectively.

Voice recordings
Voice acoustic qualities, such as pitch, speed, timing and 
timbre,  have  been  used  in  previous  research  to  success-
fully  distinguish  depressed  from  non- depressed  individ-
uals.82–85 To collect voice data, the Mom2B app sends out 
a  voice  recording  task  asking  the  participant  to  record 
reading  simple  texts,  numerical  sequences  or  vocalisa-
tions every 2–4 weeks.

Passive data collection
Passive  data  that  the  user  has  provided  consent  for  are 
continuously collected via the Mom2B app throughout the 
study period, and are used to infer the user’s behavioural 
patterns. Some of these features are collected differently 
for  iOS  and  Android  users.  The  feature  modalities  are 
briefly explained below.

Mobility
Correlations have been demonstrated between a patient’s 
geographical movement patterns and changes in depres-
sive  symptoms.86  87  Sixty  seconds  of  Global  Positioning 
System  (GPS)  data  are  continuously  collected  every  10 
min.  Accelerator  data  are  collected  when  the  motion 
exceeds a certain threshold; motion activities, including 
being stationary, walking, running, cycling and movement 
in  a  vehicle,  are  recorded  when  the  state  changes.  For 
iOS,  we  collect  device  motion  to  provide  more  detailed 
motion sensor data.

Data usage
Internet usage is the main feature of data usage. Various 
patterns  of  internet  usage  have  been  identified  in  rela-
tion  to  depression  in  different  populations,88  89  but  not 
among  women  with  PND.  The  Mom2B  app  records  the 
accumulated  upload  and  download  rates  together  with 
timestamps.  Another  feature,  reachability,  records  time-
stamped  smartphone  connectivity—whether  the  phone 
is connected to cellular network, Wi- Fi or neither. It also 
records  a  Wi- Fi  log  for  Android  phone,  which  includes 
anonymised  Media  Access  Control  (MAC)  addresses’ 
frequencies  and  Received  Signal  Strength  Indicator 
(RSSI) of available wireless networks in the area.

Surveys and questionnaires
The Mom2B app delivers a range of both validated and 
self- developed questionnaires two to three times per week 
on average, with a mean of five questions per survey. These 

Smartphone usage
General  smartphone  use  has  been  found  to  correlate 
with sleep quality and depression.90 91 Phone power state, 
combined with mobility parameters, can reflect individual 

4

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033Table 1  Sociodemographic characteristics, pregnancy history and birth outcomes on participants in the Mom2B study and 
the general population of pregnant women in Sweden

Mom2B (2020–2022)
(n=3909)*

Sweden (2019)†

Characteristics

Available data (n) Missing data (n) n (%) or mean±SD Available data (n) n (%) or mean

Open access

Maternal age (years)
Country of origin

3430
3441

479
468

31.2±4.4

3177 (92.3)

40 (1.2)

116 (3.4)

108 (3.1)

744 (21.6)

2700 (78.4)

113 816
112 530

107 711

3444

465

1677

2232

113 147

1626 (97)

51 (3)

441 (14.5)

110 991

25.5±5.3

108 929

70 (2.1)

1815 (54.1)

923 (27.5)

545 (16.3)

1188 (36.4)

238 (17.5)
190 (5.7)

113 816

114 757
116 071

868

556

641

639‡
598

 Sweden

 Nordic countries except 
Sweden

 Europe except Nordic 
countries

 Outside Europe

Education

 ≤12 years

 Post- secondary 
education

Employment before 
pregnancy

 Working/student/
parental leave

 Unemployed/sick leave

Smoking 3 months before 
pregnancy

3041

BMI before pregnancy 
(kg/m2)

3353

 <18.5

 18.5–25

 25–<30

 ≥30

Primiparous

Caesarean section
Preterm delivery (<week 
37)

3268

1356
3311

30.7

78 033 (69.3)

1280 (1.1)

9172 (8.2)

24 045 (21.4)

48 793 (45.3)

58 918 (54.7)

103 967 (91.9)

9180 (8.1)

11 765 (10.6)

2783 (2.5)

59 384 (54.6)

29 636 (27.2)

17 126 (15.7)

48 473 (42.5)

20 312 (17.7)
6502 (5.6)

Percentages are given in relation to available data from women.
*Data downloaded on 1 February 2022.
†Data retrieved from the Swedish Medical Birth Register and Swedish National Board of Health and Welfare from 2019.
‡Calculated using the confirmed number of women in the postpartum period only.
BMI, body mass index.

behaviour like sleep patterns.92 93 To keep track of the use 
of  the  smartphone  device,  data  are  collected  on  screen 
activity, charging status and device reboot.

Social media activity
Social  media  behaviour  has  also  been  proven  useful  in 
detecting  mental  states.  It  has  also  been  shown  that 
reduced social activity on Facebook predicted symptoms 
of  PPD.41  Collected  data  consist  of  simple  behavioural 
measures,  such  as  posting,  commenting  or  liking, 
together with their timestamps. Notably, we only measure 
activity levels, not information related to the text or image 

content of that activity, and participants are made aware 
of this when providing consent.

Survey metadata
App- based  surveys  make  it  possible  to  also  collect  meta-
data. This kind of behavioural metadata may contain clini-
cally relevant information related to attention, processing 
speed and working memory capacity, and even any dete-
rioration  of  psychiatric  symptoms.58  94  We  collect  data 
on  the  time  a  survey  was  opened,  time  taken  to  answer 
each question and fully complete a survey, as well as any 
changes made in survey responses.

5

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033 
 
 
 
 
 
 
 
 
 
 
 
Open access 

Figure 2  Timeline of validated instruments administered in the Mom2B study during pregnancy and postpartum periods, 
and the number of occurrences for each instrument throughout the study period. Surveys become available to users for 
varying periods of time and will disappear once completed or when their period of availability is over. EPDS, Edinburgh 
Postnatal Depression Scale27; WHO- 5, WHO- 5 Well- Being Index106; DSM- screening, Diagnostic and Statistical Manual of 
Mental Disorders, 5th Edition, criterion for depression; DSM- screening short is a shortened version of the DSM- screening with 
selected questions chosen by the research team; HADS, Hospital Anxiety and Depression Scale107; PSS, Perceived Stress 
Scale108; SLE, Stressful Life Events109; LITE, Lifetime Influence of Traumatic Experiences110; FOBS, Fear of Birth Scale111; IPAQ, 
International Physical Activity Questionnaire112; FSFI, Female Sexual Function Index113; ISI, Insomnia Severity Index114; RS- 14, 
Resilience Scale115; SOC, Sense of Coherence116; VPSQ, Vulnerability Personality Style Questionnaire117; ECRS, Experience 
in Close Relationships Scale118; Valentine Scale (relationship with your partner)119; S- MIBS, Swedish Mother to Infant Bonding 
Scale120; PBQ, Postpartum Bonding Questionnaire121; IBQ, Infant Behavior Questionnaire122; SPSQ, Swedish Parenthood Stress 
Questionnaire123; LMUP, London Measure of Unplanned Pregnancy124; ICQ, Infant Characteristics Questionnaire.125

Figure 3  Timeline of self- developed surveys administered in the Mom2B study during pregnancy and postpartum periods, 
and the number of occurrences for each instrument throughout the study period. Surveys become available to users for varying 
periods of time and will disappear once completed or when their period of availability is over.

6

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033Open access

secure,  cloud- based  storage,  where  another  layer  of 
encryption  is  added.  Passive  data  collected  from  the 
phone follow the same path.

 ► From  MinIO,  all  data  are  sent  to  Bianca,  a  private 
offline server, in both encrypted and decrypted forms 
for storage and analysis, respectively.

 ► The  app  provides  weekly  reports  based  on  partici-
pant  activity  and  fetches  health- related  information 
relating to the perinatal period the user is in, as well as 
frequently asked questions about the study and peri-
natal health.

Preliminary data analysis strategy
The  Mom2B  data  set  contains  different  modalities, 
including audio data, sensor data and survey data, which 
will be analysed separately and then combined. We plan 
to use both traditional ML and DL techniques in order 
to  determine  reliable  predictors  of  PND  and  develop 
accurate predictive algorithms, and will report our find-
ings  following  the  best  fit  current  guidelines,  such  as 
the Transparent Reporting of a Multivariable Prediction 
Model for Individual Prognosis or Diagnosis (TRIPOD) 
statement.95

Feature engineering
To handle these multimodal data, we will extract features 
for  these  modalities  separately  using  traditional  feature 
engineering as well as DL techniques.96 97 An example of 
traditional feature engineering uses trajectories,87 which 
use mobility features, such as number of significant places 
visited, maximum distance and SD. However, DL can be 
used  for  extracting  features  in  many  other  modalities, 
such as social media and audio data, which are not inves-
tigated widely in the area.

Feature selection and model selection
To analyse the multimodal Mom2B data set, we will start 
with  each  modality  separately.  To  reduce  the  possibility 
of  potential  overfitting,  given  the  numerous  features  in 
our  data  set,  we  will  use  recursive  feature  elimination 
to  obtain  the  optimal  set  of  variables  for  further  model 
development.

Previously, logistic regression, support vector machine, 
random forests, XGBoost and neural networks have been 
the most commonly used and efficient ML algorithms for 
prediction  of  PND.98  An  advantage  of  using  such  tradi-
tional  ML  methods  is  to  give  us  a  feature  importance 
ranking,  allowing  us  to  identify  stronger  predictors. 
Using  DL  to  analyse  digital  phenotyping  data  for  eval-
uating  risk  of  depression  is  a  relatively  novel  approach 
compared with traditional ML models.73 DL models have 
been shown to outperform traditional ML in various tasks 
involving  complex  data  sets,99  100  and  can  be  combined 
with  traditional  ML  in  multimodal  data  mining  tasks  to 
further  improve  performance.97  We  will  test  and  select 
the  best  performing  ML  models  for  each  modality  and 
determine strong predictors of PND.

7

Figure 4  Flow of data from user to servers for storage and 
analysis. Data pass through secure servers accessible only 
by authorised members of the Mom2B team, and can be 
decrypted for analysis in Bianca when needed.

National register data
Supplementary  information  will  be  accessed  via  the 
following  Swedish  national  health  and  quality  registers: 
the  Medical  Birth  Register,  the  Pregnancy  Register,  the 
National  Patient  Register,  the  Prescribed  Drug  Register 
and  population  censuses  from  Statistics  Sweden.  The 
accessed 
includes  records  of  perinatal 
complications  such  as  PND,  PTB  or  any  other  compli-
cations  considered  important  risk  factors  for  the  study 
outcomes, such as gestational diabetes, gestational hyper-
tension,  pre- eclampsia,  prolonged  delivery,  severe  lacer-
ations,  postpartum  haemorrhage,  induction  of  delivery, 
instrumental vaginal delivery, caesarean section and small 
for gestational age.

information 

Further, the mother’s weight at enrolment in maternity 
care and at aftercare visits; calculated date of birth from 
last menstrual period and from ultrasound; and informa-
tion on previous miscarriages, previous abortions, chronic 
diseases,  fear  of  childbirth,  involuntary  infertility,  gesta-
tional age at enrolment in maternity care and fetal diag-
nostics will be obtained from the Medical Birth Register. 
Retrieved  information  also  includes  variables  regarding 
the  background,  health  and  lifestyle  of  the  participant 
for validation purposes of our self- report questionnaires, 
as well as psychiatric and somatic morbidity for up to 15 
years after childbirth.

Data flow and storage
Figure  4  illustrates  the  data  flow  and  storage  process  as 
follows:
 ► Participants register to the study via the Mom2B app 
using their Swedish Social Security number, which is 
encrypted in the device using a private key provided by 
the Beiwe backend server, and replaced by a random, 
pseudoanonymised code number.

 ► The  decryption  key,  together  with  the  participant 
information  and  electronic  signatures, 
consent 
is  stored  in  a  private,  write- only  server  at  Uppsala 
University.

 ► The  app  fetches  surveys  and  voice  recording  tasks, 
and  uploads  data  from  participants  to  the  backend 
server,  where  it  is  encrypted  and  sent  to  MinIO,  a 

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033Open access 

Figure 5  A multimodal machine learning model for 
peripartum depression (PPD) diagnosis. The extracted 
features can be classified into three categories: acoustic 
signals, time series features and categorical features. 
We can then determine the most suitable model for each 
category. For example, for acoustic signals, we would apply 
convolutional neural network (CNN); for time series data, we 
would apply recurrent neural network (RNN) such as long 
short- term memory (LSTM); and for numerical variables, 
we would apply deep neural networks (DNNs) such as 
transformers, or traditional models like extremely randomised 
trees (XRT), gradient boosted trees, etc. These models can 
yield high- dimension representations of multimodal features. 
After feature fusion, the integrated features will be fed into 
another neural network for prediction.

Multimodal computational model
The  multimodal  data  we  collect  are  in  different  scales, 
dimensions  and  formats,  which  need  to  be  harmon-
ised  before  prediction.101  Different  models  are  better 
suited  to  perform  on  different  modalities.  To  handle 
this complexity in multiple data modalities, we consider 
modality fusion during the development phase.

One  example  of  a  multimodal  ML  model  is  shown 
in  figure  5.  The  model  is  designed  to  detect  potential 
depressive episodes based on multimodal data collected 
in the Mom2B app. Preprocessed data in three modalities 
are fed into models and intermediate representations are 
then fused together and fed in as input features of a clas-
sification model.

Evaluation metrics
Our  data  will  be  split  into  a  training  data  set,  for  anal-
ysis,  and  a  test  data  set,  to  assess  model  performance. 
We consider using multiple evaluation metrics including 
area  under  the  receiver  operating  characteristic  curve, 
specificity,  sensitivity,  positive  predictive  value,  nega-
tive  predictive  value,  balanced  accuracy  and  F1  score, 
as these measurements vary in importance according to 
the setting and goal of the final algorithm. Thereby, we 
can compare the performance of traditional ML with DL, 
and  the  different  assemblies  of  models,  from  different 
perspectives in the context of prediction of PND.

8

Patient and public involvement
A  qualitative  study  is  planned  for  exploring  the  atti-
tudes and concerns of participating women towards the 
Mom2B app. Furthermore, an online survey will be sent 
to  women  who  have  had  no  recent  activity  on  the  app 
or withdrawn participation from the study. Direct contact 
with end users and the ability to make changes to the app 
based  on  their  feedback  can  enhance  user  experience 
and increase engagement. A representative from Mamma 
till Mamma, a non- profit organisation in Sweden focused 
on  perinatal  mental  well- being,  serves  on  our  advisory 
board. The organisation has been involved in the piloting 
of our study and design of questionnaires, and currently 
supports us with recruitment. We plan to involve them in 
the dissemination of study results as well.

Substudies
In  addition  to  predicting  PND  and  PTB,  the  rich  data 
collected  from  the  Mom2B  cohort  will  also  be  used  to 
investigate further questions, mainly regarding the health 
of pregnant and postpartum women. Other planned areas 
of  research  are  regarding  the  impact  of  early  mother–
infant separation and neonatal intensive care of the baby 
on the well- being of the mother; and sexual function and 
its  potential  correlates  to  depression  and  anxiety  in  the 
perinatal period.

Maternal depression and well-being during the COVID-19 
pandemic
In  the  beginning  of  2021,  data  collected  from  1577 
participants  were  used  to  assess  depressive  and  anxiety 
symptoms, as well as well- being and life changes in preg-
nant women in Sweden during the COVID- 19 pandemic 
(from February 2020 to March 2021).102 The Mom2B app 
enabled  gathering  psychiatric  information  at  a  national 
level  during  the  pandemic,  as  well  as  passive  data  on 
mobility. Levels of perinatal affective symptoms and low 
well- being  were  elevated  compared  with  previous  years 
and  to  months  with  fewer  cases.  Similar  apps  can  help 
healthcare providers and governmental bodies to monitor 
high- risk  groups  during  crises  in  real  time,  as  well  as  to 
adjust measures and the support offered.

ETHICS AND DISSEMINATION
Participants are informed about the aims of the study, and 
that the confidentiality and security of their data will be 
assured. All participants provide their consent to partici-
pate while registering to the study, and are informed that 
they can withdraw their participation at any time without 
giving a reason. Ethical approval has been obtained from 
the Swedish Ethical Review Authority (dnr: 2019/01170, 
with  amendments)  and  the  project  fulfils  General  Data 
Protection  Regulation  (GDPR)  requirements,  including 
the processing, storage and protection of all data. Results 
will  be  continuously  disseminated  through  interna-
tional  peer- reviewed  journals,  the  project’s  website  and 
social  media  channels,  and  presented  in  national  and 

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033international  conferences.  All  publications  will  be  open 
access.

DISCUSSION
Strengths and limitations
Besides the utility of digital phenotyping in combination 
with the advanced analytical methods planned to be used, 
other strengths of the Mom2B study include the involve-
ment of participants. Statistics based on the WHO- 5 Well- 
Being  Index  and  behavioural  data  (movement,  internet 
usage,  sleep,  etc)  collected  from  participants  are  sent 
to  the  user,  allowing  them  to  follow  their  well- being 
and  activity  as  an  incentive  for  continued  participation. 
Weekly  informational  reports  regarding  common  expe-
riences and concerns for both the mother and the child 
for  that  particular  week  of  the  perinatal  period,  based 
on  information  taken  from   1177. se  (Swedish  health-
care  service),  are  available  to  users  and  allow  them  to 
easily  stay  informed.  As  per  standard  guidelines,103  if 
participants  receive  a  high  score  on  the  EPDS,  they  are 
prompted to contact their healthcare provider or emer-
gency  support  services  for  support,  and  if  unsure,  they 
can contact the research team, which will help them find 
appropriate support for their needs. Continuous contact 
is maintained with participants until they find support.

The  involvement  of  user  organisations  and  an  inter-
national  advisory  board  further  strengthens  the  study 
by  increasing  the  feasibility,  the  use  of  state- of- the- art 
methods  and  the  potential  for  high  acceptance  by  the 
end  users,  which  is  especially  important  for  future  inte-
gration in regular clinical practice.

However,  there  are  some  limitations  to  acknowledge. 
Weekly reports and statistics are important in supporting 
and incentivising users, but it is possible they may influence 
users’ responses to certain questionnaires. To account for 
this,  we  consider  including  how  often  they  are  checked 
by users as a feature within our models. Furthermore, our 
app is available only in Swedish, which excludes a number 
of otherwise eligible participants, and the high costs for 
maintaining the technical infrastructure in the frontend 
and  backend  of  the  app  require  considerable  funding. 
Attrition is also an issue, especially with data that require 
active input from users. While we can attempt to combat 
this  by  improving  the  app  based  on  user  feedback,  it  is 
important  to  consider  that  attrition  might  also  reflect 
the worsening of symptoms and be a predictor per se of 
clinical deterioration. It will be important to distinguish 
such participants and determine how to use attrition as a 
predictor variable.

Future perspectives
We are at the beginning of the smartphone- based research 
era, and future possibilities seem numerous. We intend to 
develop  the  Mom2B  app  in  other  languages,  including 
English, to expand to a more diverse and wider popula-
tion.  If  the  app  succeeds  in  developing  good  predictive 
models  for  PND,  the  research  team  anticipates  that  the 

Open access

app  could  be  further  developed  to  include  evidence- 
based interventions.104 Furthermore, since PND is much 
less  understood  in  co- parents  and  improving  the  other 
parent’s mental well- being is conducive to the health of 
the  mother  and  the  children  as  well,105  the  app  could 
be  further  developed  to  study  co- parental  PND.  The 
Mom2B research team plans to further adapt the app to 
other research topics such as teenage and student mental 
health,  and  prediction  of  new  episodes  or  self- harm  in 
major depression.

Author affiliations
1Department of Medical Sciences, Uppsala University, Uppsala, Sweden
2Centre for Women's Mental Health during the Reproductive Lifespan (Womher), 
Uppsala University, Uppsala, Sweden
3Department of Women’s and Children’s Health, Uppsala University, Uppsala, 
Sweden
4Centre for Translational Microbiome Research, Department of Microbiology, Tumor 
and Cell Biology, Karolinska Institute, Stockholm, Sweden
5Department of Information Technology, Uppsala University, Uppsala, Sweden

Acknowledgements  We would like to extend our gratitude to Oskar Burman for 
creating and continuously adjusting the smartphone research application Mom2B; 
to Dr Masoumeh Rezapour, the previous head of Department of Obstetrics and 
Gynecology at Uppsala University Hospital, for support and guidance in the first 
steps of this project; to Arvid Marklund and Stavros Iliadis for support at the early 
stages of the app creation; and to Maria Grandahl, Emilia Biskop and Lisa Lindgren 
for their valuable input regarding app content and questionnaires.

Contributors  AS and FCP were involved in the conception and design of the study, 
revised the draft critically for intellectual content and approved the final manuscript. 
EB, EF and CA contributed significantly to the design and launch of the project, and 
revised the draft critically for intellectual content. AE, EB, UE, MZ and KG contributed 
to the drafting of the protocol and the continuation of the project. AMB is the 
coordinator of the study and was primarily responsible for drafting the manuscript 
and revising it critically for intellectual content.

Funding  This work was supported by the Uppsala Region to AS, the Swedish 
Association of Local Authorities and Regions (SKR) to the Department of Obstetrics 
and Gynecology, Uppsala University Hospital, the Swedish Research Council (grant 
number 2020- 01965) to AS, as well as the Swedish Brain Foundation and Uppsala 
University Womher School.

Competing interests  None declared.

Patient and public involvement  Patients and/or the public were involved in the 
design, or conduct, or reporting, or dissemination plans of this research. Refer to 
the Methods section for further details.

Patient consent for publication  Not required.

Provenance and peer review  Not commissioned; externally peer reviewed.

Supplemental material  This content has been supplied by the author(s). It 
has not been vetted by BMJ Publishing Group Limited (BMJ) and may not have 
been peer- reviewed. Any opinions or recommendations discussed are solely 
those of the author(s) and are not endorsed by BMJ. BMJ disclaims all liability 
and responsibility arising from any reliance placed on the content. Where the 
content includes any translated material, BMJ does not warrant the accuracy and 
reliability of the translations (including but not limited to local regulations, clinical 
guidelines, terminology, drug names and drug dosages), and is not responsible 
for any error and/or omissions arising from translation and adaptation or 
otherwise.

Open access  This is an open access article distributed in accordance with the 
Creative Commons Attribution 4.0 Unported (CC BY 4.0) license, which permits 
others to copy, redistribute, remix, transform and build upon this work for any 
purpose, provided the original work is properly cited, a link to the licence is given, 
and indication of whether changes were made. See: https://creativecommons.org/ 
licenses/by/4.0/.

ORCID iD
Ayesha M Bilal http://orcid.org/0000-0002-7349-8765

9

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033Open access 

REFERENCES
  1  WHO. Maternal health World Health organization, 2021. Available: 

https://www.who.int/health-topics/maternal-health

  2  Woody CA, Ferrari AJ, Siskind DJ, et al. A systematic review and 
meta- regression of the prevalence and incidence of perinatal 
depression. J Affect Disord 2017;219:86–92.

  3  WHO. Preterm birth World Health organization, 2018. Available: 
https://www.who.int/news-room/fact-sheets/detail/preterm-birth

  4  Association AP. Diagnostic and statistical manual of mental 

disorders. 5th ed. Washington, DC, 2013.

  5  Moraes GPdeA, Lorenzo L, Pontes GAR, et al. Screening and 

diagnosing postpartum depression: when and how? Trends 
Psychiatry Psychother 2017;39:54–61.

  6  Bennett HA, Einarson A, Taddio A, et al. Prevalence of 

depression during pregnancy: systematic review. Obstet Gynecol 
2004;103:698–709.

  7  Wikman A, Axfors C, Iliadis SI, et al. Characteristics of women 
with different perinatal depression trajectories. J Neurosci Res 
2020;98:1268–82.

  8  Field T, Diego M, Hernandez- Reif M. Prenatal depression 

effects on the fetus and newborn: a review. Infant Behav Dev 
2006;29:445–55.

  9  Grote NK, Bridge JA, Gavin AR, et al. A meta- analysis of 

depression during pregnancy and the risk of preterm birth, low birth 
weight, and intrauterine growth restriction. Arch Gen Psychiatry 
2010;67:1012–24.

  10  Kurki T, Hiilesmaa V, Raitasalo R, et al. Depression and anxiety 

in early pregnancy and risk for preeclampsia. Obstet Gynecol 
2000;95:487–90.

  11  Herring SJ, Rose MZ, Skouteris H, et al. Optimizing weight gain 

in pregnancy to prevent obesity in women and children. Diabetes 
Obes Metab 2012;14:195–203.

  12  Cato K, Sylvén SM, Lindbäck J, et al. Risk factors for exclusive 

breastfeeding lasting less than two months- Identifying 
women in need of targeted breastfeeding support. PLoS One 
2017;12:e0179402.

  13  Dennis C- L, McQueen K. The relationship between infant- feeding 

outcomes and postpartum depression: a qualitative systematic 
review. Pediatrics 2009;123:e736–51.

  14  Figueiredo B, Canário C, Field T. Breastfeeding is negatively 

affected by prenatal depression and reduces postpartum 
depression. Psychol Med 2014;44:927–36.

  15  Field T. Prenatal depression risk factors, developmental effects and 
interventions: a review. J Pregnancy Child Health 2017;4:301.

  16  Slomian J, Honvo G, Emonts P, et al. Consequences of maternal 

postpartum depression: a systematic review of maternal and infant 
outcomes. Womens Health 2019;15:174550651984404.
  17  Brummelte S, Galea LAM. Postpartum depression: etiology, 
treatment and consequences for maternal care. Horm Behav 
2016;77:153–66.

  18  Goodman JH. Perinatal depression and infant mental health. Arch 

Psychiatr Nurs 2019;33:217–24.

  19  Kingston D, Tough S, Whitfield H. Prenatal and postpartum maternal 
psychological distress and infant development: a systematic review. 
Child Psychiatry Hum Dev 2012;43:683–714.

  20  Iliadis SI, Skalkidou A, Ranstrand H, et al. Self- Harm thoughts 

postpartum as a marker for long- term morbidity. Front Public Health 
2018;6:34.

  21  Esscher A, Essén B, Innala E, et al. Suicides during pregnancy 
and 1 year postpartum in Sweden, 1980- 2007. Br J Psychiatry 
2016;208:462–9.

  22  Lancaster CA, Gold KJ, Flynn HA, et al. Risk factors for depressive 

symptoms during pregnancy: a systematic review. Am J Obstet 
Gynecol 2010;202:5–14.

  23  Skalkidou A, Hellgren C, Comasco E, et al. Biological aspects of 

postpartum depression. Womens Health 2012;8:659–72.

  30  Yonkers KA, Smith MV, Gotman N, et al. Typical somatic symptoms 

of pregnancy and their impact on a diagnosis of major depressive 
disorder. Gen Hosp Psychiatry 2009;31:327–33.

  31  Byatt N, Biebel K, Lundquist RS, et al. Patient, provider, and 
system- level barriers and facilitators to addressing perinatal 
depression. J Reprod Infant Psychol 2012;30:436–49.
  32  Shiffman S, Stone AA, Hufford MR. Ecological momentary 

assessment. Annu Rev Clin Psychol 2008;4:1–32.

  33  Halfin A. Depression: the benefits of early and appropriate 

treatment. Am J Manag Care 2007;13:S92–7.

  34  Jiménez- Serrano S, Tortajada S, García- Gómez JM. A mobile health 
application to predict postpartum depression based on machine 
learning. Telemed J E Health 2015;21:567–74.

  35  Dennis C- LE, Janssen PA, Singer J. Identifying women at- risk for 
postpartum depression in the immediate postpartum period. Acta 
Psychiatr Scand 2004;110:338–46.

  36  Ruyak SL, Lowe NK, Corwin EJ, et al. Prepregnancy obesity and a 
Biobehavioral predictive model for postpartum depression. Journal 
of Obstetric, Gynecologic & Neonatal Nursing 2016;45:326–38.
  37  Zhang W, Liu H, Silenzio VMB, et al. Machine learning models 
for the prediction of postpartum depression: application 
and comparison based on a cohort study. JMIR Med Inform 
2020;8:e15516.

  38  Cooper PJ, Murray L, Hooper R, et al. The development and 

validation of a predictive index for postpartum depression. Psychol 
Med 1996;26:627–34.

  39  Andersson S, Bathula DR, Iliadis SI, et al. Predicting women with 

depressive symptoms postpartum with machine learning methods. 
Sci Rep 2021;11:1–15.

  40  De Choudhury M, Counts S, Horvitz E. Predicting postpartum 

changes in emotion and behavior via social media. Conference 
on Human Factors in Computing Systems - Proceedings, 
2013:3267–76.

  41  De Choudhury M, Counts S, Horvitz EJ. Characterizing and 

predicting postpartum depression from shared Facebook data. 
Proceedings of the 17th ACM conference on Computer supported 
cooperative work & social computing, 2014.

  42  Fatima I, Abbasi BUD, Khan S, et al. Prediction of postpartum 

depression using machine learning techniques from social media 
text. Expert Systems 2019;36:e12409–e09.

  43  Mehta D, Newport DJ, Frishman G, et al. Early predictive 

biomarkers for postpartum depression point to a role for estrogen 
receptor signaling. Psychol Med 2014;44:2309–22.

  44  Blencowe H, Cousens S, Chou D, et al. Born too soon: the 

global epidemiology of 15 million preterm births. Reprod Health 
2013;10:S2.

  45  Serenius F, Källén K, Blennow M, et al. Neurodevelopmental 

outcome in extremely preterm infants at 2.5 years after active 
perinatal care in Sweden. JAMA 2013;309:1810–20.

  46  Jacobsson B, Pettersson K, Modzelewska D. Förtidsbörd största 

perinatala problemet. Läkartidningen, 2019.

  47  Räisänen S, Gissler M, Saari J, et al. Contribution of risk factors 

to extremely, very and moderately preterm births - register- based 
analysis of 1,390,742 singleton births. PLoS One 2013;8:e60660.

  48  Staneva A, Bogossian F, Pritchard M, et al. The effects of maternal 

depression, anxiety, and perceived stress during pregnancy on 
preterm birth: a systematic review. Women Birth 2015;28:179–93.

  49  Goldenberg RL, Culhane JF, Iams JD, et al. Epidemiology and 

causes of preterm birth. Lancet 2008;371:75–84.

  50  Fransson E, Örtenstrand A, Hjelmstedt A. Antenatal depressive 
symptoms and preterm birth: a prospective study of a Swedish 
national sample. Birth 2011;38:10–16.

  51  Eklundh A, Grunewald C. Handläggning Vid hotande förtidsbörd. 

Läkartidningen. klinik och vetenskap ED, 2011.

  52  Health NIo. What are the risk factors for preterm labor and birth? 

2019. Available: https://www.nichd.nih.gov/health/topics/preterm/ 
conditioninfo/who_risk [Accessed Oct 2021].

  24  O'Hara MW. Postpartum depression: what we know. J Clin Psychol 

  53  Christian LM. Psychoneuroimmunology in pregnancy: immune 

2009;65:1258–69.

  25  Cox EQ, Sowa NA, Meltzer- Brody SE, et al. The perinatal 

depression treatment cascade. J Clin Psychiatry 2016;77:1189–200.

  26  Bränn E, Fransson E, Wikman A, et al. Who do we miss when 

screening for postpartum depression? A population- based study in 
a Swedish region. J Affect Disord 2021;287:165–73.

  27  Cox JL, Holden JM, Sagovsky R. Detection of postnatal depression. 

development of the 10- item Edinburgh postnatal depression scale. 
Br J Psychiatry 1987;150:782–6.

  28  Socialstyrelsen. Vägledning för barnhälsovården, 2014.
  29  Massoudi P, Wickberg B, Hwang P. Screening for postnatal 
depression in Swedish child health care. Acta Paediatr 
2007;96:897–901.

pathways linking stress with maternal health, adverse birth 
outcomes, and fetal development. Neurosci Biobehav Rev 
2012;36:350–61.

  54  Medley N, Vogel JP, Care A, et al. Interventions during pregnancy to 
prevent preterm birth: an overview of Cochrane systematic reviews. 
Cochrane Database Syst Rev 2018;2018.

  55  Ferrero DM, Larson J, Jacobsson B, et al. Cross- country individual 
participant analysis of 4.1 million singleton births in 5 countries with 
very high human development index confirms known associations 
but provides no biologic explanation for 2/3 of all preterm births. 
PLoS One 2016;11:e0162506.

  56  Jacobsson B. Prediktion, prevention och behandlingsmetoder. 

Läkartidningen, 2019.

10

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033Open access

  57  Varli IH, Wollmann CL, Sandström A. Hotande förtidsbörd/

  85  IEEE. On the relative importance of vocal source, system, and 

prematurbörd/för tidig födsel:  Internetmedicin. se, 2019. Available: 
https://www.internetmedicin.se/behandlingsoversikter/gynekologi- 
obstetrik/prematura-sammandragningar/

  58  Torous J, Kiang MV, Lorme J, et al. New tools for new research in 

psychiatry: a scalable and Customizable platform to empower data 
driven smartphone research. JMIR Ment Health 2016;3:e16.
  59  Meyerowitz- Katz G, Ravi S, Arnolda L, et al. Rates of attrition and 

dropout in App- Based interventions for chronic disease: systematic 
review and meta- analysis. J Med Internet Res 2020;22:e20283.

  60  Press G. 12 Big Data Definitions: What’s Yours? Forbes 2014.
  61  Pastorino R, De Vito C, Migliara G, et al. Benefits and challenges of 
big data in healthcare: an overview of the European initiatives. Eur J 
Public Health 2019;29:23–7.

  62  Torous J, Staples P, Onnela J- P. Realizing the potential of mobile 
mental health: new methods for new data in psychiatry. Curr 
Psychiatry Rep 2015;17:602.

  63  Olsen J, Melbye M, Olsen SF, et al. The Danish National Birth 

Cohort--its background, structure and aim. Scand J Public Health 
2001;29:300–7.

  64  Magnus P, Birke C, Vejrup K, et al. Cohort profile update: the 

Norwegian mother and child cohort study (MobA). Int J Epidemiol 
2016;45:382–8.

  65  Stoltenberg C, Schjølberg S, Bresnahan M, et al. The autism birth 

cohort: a paradigm for gene- environment- timing research. Mol 
Psychiatry 2010;15:676–80.

  66  Axfors C, Bränn E, Henriksson HE, et al. Cohort profile: the biology, 
affect, stress, imaging and cognition (basic) study on perinatal 
depression in a population- based Swedish cohort. BMJ Open 
2019;9:e031514–11.

  67  Onnela JP, Rauch SL. Harnessing smartphone- based digital 

phenotyping to enhance behavioral and mental health. Nature 
Publishing Group, 2016: 1691–6.

  68  Shouval R, Bondi O, Mishan H, et al. Application of machine 

learning algorithms for clinical predictive modeling: a data- mining 
approach in SCT. Bone Marrow Transplant 2014;49:332–7.

  69  Barnett I, Torous J, Staples P, et al. Relapse prediction in 
schizophrenia through digital phenotyping: a pilot study. 
Neuropsychopharmacology 2018;43:1660–6.

  70  Zulueta J, Piscitello A, Rasic M, et al. Predicting mood disturbance 

severity with mobile phone Keystroke metadata: a BiAffect digital 
phenotyping study. J Med Internet Res 2018;20:e241.

prosody in human depression. 2013 IEEE International Conference 
on Body Sensor Networks, 2013.

  86  Saeb S, Zhang M, Karr CJ, et al. Mobile phone sensor correlates of 
depressive symptom severity in Daily- Life behavior: an exploratory 
study. J Med Internet Res 2015;17:e175.

  87  Canzian L, Musolesi M. Trajectories of depression: unobtrusive 

monitoring of depressive states by means of smartphone mobility 
traces analysis. Proceedings of the 2015 ACM international joint 
conference on pervasive and ubiquitous computing, 2015.

  88  Cotten SR, Ford G, Ford S, et al. Internet use and depression 

among older adults. Comput Human Behav 2012;28:496–9.
  89  Katikalapudi R, Chellappan S, Montgomery F, et al. Associating 

Internet usage with depressive behavior among college students. 
IEEE Technology and Society Magazine 2012;31:73–80.

  90  Rozgonjuk D, Levine JC, Hall BJ, et al. The association between 
problematic smartphone use, depression and anxiety symptom 
severity, and objectively measured smartphone use over one week. 
Comput Human Behav 2018;87:10–17.

  91  Elhai JD, Tiamiyu MF, Weeks JW, et al. Depression and emotion 
regulation predict objective smartphone use measured over one 
week. Pers Individ Dif 2018;133:21–8.

  92  Aledavood T, Torous J, Triana Hoyos AM, et al. Smartphone- Based 

tracking of sleep in depression, anxiety, and psychotic disorders. 
Curr Psychiatry Rep 2019;21:49.

  93  DeMasi O, Feygin S, Dembo A, et al. Well- Being tracking via 

Smartphone- Measured activity and sleep: cohort study. JMIR 
Mhealth Uhealth 2017;5:e137.

  94  Torous J, Staples P, Barnett I, et al. Characterizing the clinical 

relevance of digital phenotyping data quality with applications to a 
cohort with schizophrenia. NPJ Digit Med 2018;1:15.

  95  Collins GS, Reitsma JB, Altman DG, et al. Transparent reporting 
of a multivariable prediction model for individual prognosis 
or diagnosis (TRIPOD): the TRIPOD statement. Br J Surg 
2015;102:148–58.

  96  Mehrotra A, Musolesi M. Using autoencoders to automatically 

extract mobility features for predicting depressive states. Proc ACM 
Interact Mob Wearable Ubiquitous Technol 2018;2:1–20.

  97  Joshi DJ, Nabar Y, Makhija M, et al. Mental health analysis using 

deep learning for feature extraction. Proceedings of the ACM India 
Joint International Conference on Data Science and Management of 
Data, 2018.

  71  Hussain- Shamsy N, Shah A, Vigod SN, et al. Mobile health for 

  98  Saqib K, Khan AF, Butt ZA. Machine learning methods for predicting 

perinatal depression and anxiety: Scoping review. J Med Internet 
Res 2020;22:e17011–e11.

postpartum depression: Scoping review. JMIR Ment Health 
2021;8:e29838.

  72  Hahn L, Eickhoff SB, Habel U, et al. Early identification of 

  99  Yang L, Jiang D, Xia X, et al. Multimodal measurement of 

postpartum depression using demographic, clinical, and digital 
phenotyping. Transl Psychiatry 2021;11:1–10.

  73  Graham S, Depp C, Lee EE. Artificial intelligence for mental health 
and mental illnesses: an overview: current medicine group LLC 1, 
2019: 116–16.

  74  Micheli- Tzanakou E. Artificial neural networks: an overview. 

Network: Computation in Neural Systems 2011;22:208–30.

  75  LeCun Y, Bengio Y, Hinton G. Deep learning. Nature 

2015;521:436–44.

  76  Miotto R, Wang F, Wang S, et al. Deep learning for healthcare: review, 
opportunities and challenges. Brief Bioinform 2018;19:1236–46.
  77  Topol EJ. High- Performance medicine: the convergence of human 

and artificial intelligence. Nat Med 2019;25:44–56.

  78  Yahata N, Kasai K, Kawato M. Computational neuroscience 

approach to biomarkers and treatments for mental disorders. 
Psychiatry Clin Neurosci 2017;71:215–37.

  79  Joshi J, Goecke R, Alghowinem S, et al. Multimodal assistive 

technologies for depression diagnosis and monitoring. Journal on 
Multimodal User Interfaces 2013;7:217–28.

  80  SBU. Diagnostik och uppföljning av förstämningssyndrom: en 

systematisk litteraturöversikt. In: Ekselius L, ed. Statens beredning 
för medicinskt utvärdering (SBU, 2012.

depression using deep learning models. Proceedings of the 7th 
Annual Workshop on Audio/Visual Emotion Challenge, 2017.

 100  Mehrotra A, Hendley R, Musolesi M. Towards multi- modal 

anticipatory monitoring of depressive states through the analysis 
of human- smartphone interaction. Proceedings of the 2016 
ACM international joint conference on pervasive and ubiquitous 
computing: adjunct, 2016.

 101  Atrey PK, Hossain MA, El Saddik A, et al. Multimodal fusion for 

multimedia analysis: a survey. Multimed Syst 2010;16:345–79.
 102  Fransson E, Karalexi M, Kimmel M. Mental health among pregnant 
women during the pandemic in Sweden, a mixed methods 
approach using data from the Mom2B mobile application for 
research. MedRxiv2020.

 103  Sheehan AM, McGee H. Screening for depression in medical 

research: ethical challenges and recommendations. BMC Med 
Ethics 2013;14:4.

 104  Zhou C, Hu H, Wang C. The effectiveness of mHealth interventions 
on postpartum depression: a systematic review and meta- analysis. 
J Telemed Telecare 2020:20917816.

 105  Bruno A, Celebre L, Mento C, et al. When fathers begin to falter: 

a comprehensive review on paternal perinatal depression. Int J 
Environ Res Public Health 2020;17:1139.

  81  Levis B, Negeri Z, Sun Y, et al. Accuracy of the Edinburgh postnatal 

 106  Topp CW, Østergaard SD, Søndergaard S, et al. The WHO- 5 

depression scale (EPDS) for screening to detect major depression 
among pregnant and postpartum women: systematic review and meta- 
analysis of individual participant data. BMJ 2020;371:m4022.
  82  France DJ, Shiavi RG, Silverman S, et al. Acoustical properties of 

speech as indicators of depression and suicidal risk. IEEE Trans 
Biomed Eng 2000;47:829–37.

  83  Yang Y, Fairbairn C, Cohn JF. Detecting depression severity from 
vocal prosody. IEEE Trans Affect Comput 2013;4:142–50.
  84  Cummins N, Breakspear M, et al, WIKICFP. An investigation of 

depressed speech detection: features and normalization. Twelfth 
Annual Conference of the International Speech Communication 
Association, 2011.

well- being index: a systematic review of the literature. Psychother 
Psychosom 2015;84:167–76.

 107  Zigmond AS, Snaith RP. The hospital anxiety and depression scale. 

Acta Psychiatr Scand 1983;67:361–70.

 108  Eklund M, Bäckström M, Tuvesson H. Psychometric properties 

and factor structure of the Swedish version of the perceived stress 
scale. Nord J Psychiatry 2014;68:494–9.

 109  Rosengren A, Orth- Gomér K, Wedel H, et al. Stressful life events, social 
support, and mortality in men born in 1933. BMJ 1993;307:1102–5.

 110  Greenwald R, Rubin A. Assessment of posttraumatic symptoms in 

children: development and preliminary validation of parent and child 
scales. Res Soc Work Pract 1999;9:61–75.

11

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033Open access 

 111  Hildingsson I, Rubertsson C, Karlström A, et al. Exploring the fear 

 118  Brennan KA, Clark CL, Shaver P. Self- Report measures of adult 

of birth scale in a mixed population of women of childbearing age- A 
Swedish pilot study. Women Birth 2018;31:407–13.

 112  Craig CL, Marshall AL, Sjöström M, et al. International physical 

activity questionnaire: 12- country reliability and validity. Med Sci 
Sports Exerc 2003;35:1381–95.

 113  Rosen R, Brown C, Heiman J, et al. The female sexual function index 

(FSFI): a multidimensional self- report instrument for the assessment 
of female sexual function. J Sex Marital Ther 2000;26:191–208.
 114  Bastien CH, Vallières A, Morin CM. Validation of the insomnia 

severity index as an outcome measure for insomnia research. Sleep 
Med 2001;2:297–307.

 115  Wagnild GM, Young HM. Development and psychometric evaluation 

of the resilience scale. J Nurs Meas 1993;1:165–78.
 116  Eriksson M, Lindström B. Validity of Antonovsky's sense of 

coherence scale: a systematic review. J Epidemiol Community 
Health 2005;59:460–6.

 117  Dennis CL, Boyce P. Further psychometric testing of a brief 

personality scale to measure vulnerability to postpartum 
depression. J Psychosom Obstet Gynaecol 2004;25:305–11.

romantic attachment. Attachment theory and close relationships, 
1998:46–76.

 119  Burman M, Norlander A- K, Carlbring P. Närmare varandra: Nio 
veckor till en starkare parrelation. Natur & Kultur, 2018.

 120  Mörelius E, Elander A, Saghamre E. A Swedish translation and 

validation of the mother- to- infant bonding scale. Scand J Public 
Health 2021;49:465–70.

 121  Brockington IF, Fraser C, Wilson D. The postpartum bonding 
questionnaire: a validation. Arch Womens Ment Health 
2006;9:233–42.

 122  Putnam SP, Helbig AL, Gartstein MA, et al. Development and 

assessment of short and very short forms of the infant behavior 
questionnaire- revised. J Pers Assess 2014;96:445–58.
 123  Östberg M, Hagekull B. A structural modeling approach to 
the understanding of parenting stress. J Clin Child Psychol 
2000;29:615–25.

 124  Barrett G, Smith SC, Wellings K. Conceptualisation, development, 
and evaluation of a measure of unplanned pregnancy. J Epidemiol 
Community Health 2004;58:426–33.

 125  Bates JE, Freeland CA, Lounsbury ML. Measurement of infant 

difficultness. Child Dev 1979;50:794–803.

12

Bilal AM, et al. BMJ Open 2022;12:e059033. doi:10.1136/bmjopen-2021-059033
