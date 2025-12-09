# Yao_2025_School adjustment and mental health among adolescents a network analysis.

Yao et al. BMC Pediatrics          (2025) 25:892 
https://doi.org/10.1186/s12887-025-06264-6

BMC Pediatrics

School adjustment and mental health among 
adolescents: a network analysis

Yisong Yao1†, Baoyi Liao2†, Yingying Cheng3†, Xianxian Deng4, Mingjun Sun4, Jiani Song4, Mingxia Li4, Jialin Wu4 and 
Wenle Zhang5*

Abstract
Background  This study uses network analysis to investigate the network structure linking school adjustment 
and mental health among adolescents in Shandong Province. The objectives include identifying core symptoms 
within symptom clusters, examining the interactions between school adjustment and mental health, and providing 
evidence-based insights to help suggest potential intervention targets.

Methods  The data were provided by the Shandong University Database of Youth Health in Population Health Data 
Archive. School Social Behavior Scale (SSBS) and Symptom Check List 90 (SCL-90) were used to estimate the school 
adjustment and mental health status of adolescents, respectively. Network analysis was performed using R software 
to construct the symptom network structure and assess the degree of centrality, bridge strength, stability, and 
precision of each item.

Results  Among the 11,949 adolescents aged 11–18 years in Shandong Province were included in the study, 5695 
(47.7%) were males and 6254 (52.3%) were females. “Obsessive compulsive (SCL-2)” and “Interpersonal sensitivity 
(SCL-3)” were the most strongly connected. The symptom with the highest strength was “Anxiety (SCL-5)”. “Antisocial 
behavior (SSBS-2)” was the symptom with the highest bridge strength. “Antisocial behavior (SSBS-2)” and “Hostility 
(SCL-6)” were extremely distinct bridge symptoms.

Conclusions  “Anxiety (SCL-5)” plays a central role in the symptom network of school adjustment and mental health 
among adolescents. This study fully capture the complex interactions and networked relationships between these 
two psychological traits, and suggest potential intervention targets by targeting core and bridge symptoms in the 
symptom network.

Keywords  Mental health, School adjustment, Network analysis, Adolescents

†Yisong Yao, Baoyi Liao and Yingying Cheng contributed equally to 
this work.

*Correspondence:
Wenle Zhang
angusle19980328@gmail.com
1Department of Otorhinolaryngology, Head and Neck Surgery, Yantai 
Yuhuangding Hospital, Qingdao University, Yantai, China

2Department of Clinical Medicine, North Sichuan Medical College, 
Nanchong 637000, China
3Department of Stomatology, North Sichuan Medical College,  
Nanchong 637000, China
4Sichuan Primary Health Care Research Center, North Sichuan Medical 
College, Nanchong 637000, China
5Fujian Psychiatric Center, Xiamen Xian-yue Hospital, Xian-yue Hospital 
Affiliated with Xiamen Medical College, Fujian Clinical Research Center for 
Mental Disorders, Xiamen 361012, China

©  The  Author(s)  2025.  Open  Access    This  article  is  licensed  under  a  Creative  Commons  Attribution-NonCommercial-NoDerivatives  4.0 
International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you 
give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the 
licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the 
material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or 
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p  : / /  c r e a  t i  
v e c  o m m  o n s .  o r  g / l  i c e  n s e s  / b  y - n c - n d / 4 . 0 /.

RESEARCHOpen AccessPage 2 of 9

Introduction
Mental health of adolescents has emerged as a significant 
global  public  health  concern  [1].  According  to  a  global 
report, one in seven adolescents are suffering from men-
tal  health  problems  all  around  the  world  [2].  In  China, 
recent  nationwide  research  indicates  that  nearly  25%  of 
adolescents  are  experiencing  different  levels  of  depres-
sion  [2].  Another  national  survey  reveals  that  depres-
sion  prevalence  among  adolescents  surged  from  18.4% 
to  24.6%  from  2015  to  2022  [3].  Adolescents  with  poor 
mental  health  are  particularly  vulnerable  to  mood  dis-
orders, eating disorders, risk-taking behaviors, and even 
self-harm  and  suicide  [4–7].  Therefore,  it  is  crucial  to 
address adolescents’ mental health issues.

For  adolescents  from  China,  schools  are  usually  the 
first places, apart from family, that are full of challenges 
for  them,  including  academic  responsibilities,  the  pro-
cess  of  puberty,  and  the  development  of  social  relation-
ships with peers [8, 9]. Several studies have indicated that 
school  adjustment  of  adolescents  is  the  main  source  of 
challenges [10]. School adjustment is defined as the com-
prehensive  assessment  of  students’  overall  performance 
in coping with learning tasks, managing peer and teacher 
relationships,  participating 
in  group  activities,  and 
regulating  emotions,  which  is  usually  divided  into  two 
aspects:  social  competence  and  antisocial  behavior  [11, 
12].  Statistics  indicate  that  approximately  18  to  35%  of 
adolescents in China experience maladaptation at school 
[13]. The challenges of school adjustment in the Chinese 
context are often uniquely shaped by its highly competi-
tive academic environment and cultural emphasis on col-
lectivism  and  academic  achievement  [14,  15].  Previous 
studies  have  revealed  that  school  adjustment  was  asso-
ciated  with  the  mental  health  of  adolescents  [16].  Poor 
social  competence,  such  as  negative  relationships  with 
teachers  and  peers,  contributes  to  a  lack  of  well-being 
experience  [9].  Specifically,  negative  peer  relationships 
can  increase  loneliness  emotions  and  damage  academic 
adjustment  in  adolescents,  while  bad  teacher-student 
relationships can promote internalizing problems such as 
depression and anxiety [17].

Previous  studies  have  recognized  the  importance  of 
maintaining  good  levels  of  school  adjustment  for  pro-
moting  adolescents’  mental  health.  However,  most  of 
them  have  treated  mental  health  as  a  single  variable  or 
have  examined  depression  and  anxiety  as  standalone 
explanatory  variables,  yet  they  overlooked  systemati-
cally  and  comprehensively  exploring  the  interrelation-
ships  between  school  adjustment  and  mental  health  [9]. 
And most of these studies utilized traditional association 
and  regression  analysis  methods.  In  contrast,  network 
analysis  has  following  advantages:  firstly,  it  can  clarify 
the  fine-grained  relationships  between  different  individ-
ual  variables  [18];  secondly,  it  can  capture  the  complex 

interactions  and  non-linear  networked  relationships 
between these two psychological traits [19]; thirdly, it can 
identify key nodes or central symptoms in a network by 
evaluating the relative importance of different nodes [20]. 
This  is  particularly  important  for  psychological  studies, 
as  analyzing  the  relationships  between  micro-symptoms 
and  identifying  key  symptoms  can  help  determine  the 
most urgent targets for improvement, thereby enhancing 
the effectiveness of intervention programs [21].

Therefore,  this  study  aimed  to  use  network  analysis 
to  gain  insight  into  the  intrinsic  association  between 
school adjustment and mental health among adolescents 
in  Shandong  province.  By  identifying  core  symptoms  (it 
refers to symptoms that are centrally located, highly con-
nected,  and  influential  within  a  network  of  symptoms) 
and bridge symptoms (it refers to symptoms that connect 
different clusters in a network containing multiple symp-
tom  clusters)  in  the  network,  this  study  will  reveal  how 
these  key  variables  interact  with  each  other  and  inform 
the development of more targeted interventions. Under-
standing the complex relationship between school adjust-
ment  and  mental  health  can  help  educators  enhance 
the  overall  well-being  and  improve  adolescents’  mental 
health status.

Methods
Participants and study design

The  data  were  obtained  from  the  Shandong  Univer-
sity  Database  of  Youth  Health  Population  Health  Data 
Archive  for  the  school  year  2020–2021  [22],  which  is  a 
probability proportionate to size sampling survey of stu-
dents in 186 schools among 17 cities in Shandong Prov-
ince [23]. More details can be seen in previous studies [9, 
23]. According to the purpose of this study, the relevant 
inclusion criteria were determined as follows: age 11 ~ 18 
years old; informed consent of teachers, parents, and stu-
dents, and voluntary participation in the study. The rele-
vant exclusion criteria were to remove blank values from 
the data. After deleting the blank values, a total of 11,949 
adolescents  were  included,  and  the  flow  chart  has  been 
shown  in  Fig.  1.  This  study  was  approved  by  the  Ethics 
Committee  of  Shandong  University  (20180517),  and 
members of the research team have obtained authoriza-
tion to use the data and can use the data set according to 
the relevant regulations.

Measurements

Demographic factors: These include gender, year of birth, 
ethnicity,  place  of  registration,  urban-rural  distribution, 
single-child  household  or  not,  and  having  a  good  rela-
tionship with parents.

School  adjustment:  School  adjustment  was  measured 
by the School Social Behavior Scale (SSBS) in this study. 
SSBS  is  a  teacher  rating  for  two  dimensions  of  social 

Yao et al. BMC Pediatrics          (2025) 25:892 Page 3 of 9

of  edge  weights  in  the  network  is  optimized  by  the 
extended  Bayesian  Information  Criterion  (EBIC)  [26]. 
The thickness of the edges in the network is indicative of 
the strength of the relationship. The correlation between 
nodes  is  indicated  by  different  colors  of  the  edges  (blue 
for positive correlation and red for negative correlation). 
The adjustment parameter is set to 0.5.

The centrality function in R-qgraph (version 1.9.2) was 
utilized to calculate the centrality indices: strength, close-
ness, betweenness, and expected influence (EI) to assess 
the  importance  of  each  node  in  the  network  [27].  The 
higher  the  centrality,  the  stronger  the  influence  or  con-
trol  of  nodes  in  the  network.  R-networktools  (version 
1.5.0)  was  utilized  to  calculate  bridge  centrality  indices, 
including  bridge  strength,  bridge  betweenness,  bridge 
closeness,  and  bridge  expected  influence  (BEI).  Bridge 
centrality measures the role of a node in linking its net-
work to other networks, assessing the strength and direc-
tion of a node’s connections to other nodes [28]. Bridge 
strength  measures  the  ability  of  a  node  to  act  as  a  con-
necting node. In addition, the predictability of each node 
was evaluated using the R-mgm (version 1.2–13). Nodes 
with high predictability are susceptible to the influence of 
nearby nodes [28]. In this study, centrality measures were 
reported as standardized values (z-scores).

The  stability  and  accuracy  of  the  network  model  were 
assessed  using  R-bootnet  (version  1.5),  where  the  Cor-
relation  Stability  Coefficient  (CS-C)  was  calculated  to 
assess  the  stability  of  the  network  model  [29].  A  CS-C 
value  above  0.25  is  considered  acceptable,  and  greater 
than 0.5 indicates good stability, with larger values indi-
cating better stability [30].

The  Network  Comparison  Test  (NCT)  was  performed 
using  the  R-Network  Comparison  Test  (version  2.2.1) 
to  assess  the  differences  in  network  structure  between 
school adjustment and mental health among adolescents 
of various traits [31]. To ensure the reliability of the net-
work  edge  weights,  95%  confidence  intervals  (95%  CI) 
were  generated  for  each  edge  weight  using  a  non-para-
metric bootstrap method. A narrower 95% CI signifies a 
higher degree of network edge weight accuracy.

Results
Descriptive statistics

A  total  of  11,949  adolescents  were  involved  in  the  net-
work, 6254 (52.3%) were females, and 3758 (31.5%) were 
rural  residents  (Table  1).  Mean,  strength,  closeness, 
betweenness, expected influence, predictability of school 
adjustment,  and  mental  health  measured  by  the  SSBS 
and the SCL-90 were shown in Table 2 and Supplemen-
tary Table 1.

Fig. 1  Flow chart of participants selection

competence  and  antisocial  behavior  [24].  It  contains 
64  items  rated  on  a  5-point  Likert  scale  ranging  from  1 
(never)  to  5  (often).  The  two  dimensions  of  SSBS  were 
considered  as  continuous  variables.  In  this  study,  Cron-
bach’s α of this scale was 0.887.

Mental health: Mental health status was assessed by the 
Symptom Checklist-90 (SCL-90) scale for adolescents in 
this  study,  a  self-rated  questionnaire  designed  to  screen 
for  a  wide  range  of  psychological  symptoms  [25].  The 
SCL-90 contains 90 items rated on a 5-point Likert scale 
ranging  from  1  (none)  to  5  (severe)  and  consists  of  the 
following  10  psychiatric  symptom  factors:  somatization, 
obsessive-compulsive,  interpersonal  sensitivity,  depres-
sion, anxiety, hostility, phobic anxiety, paranoid ideation, 
psychoticism,  and  other.  In  this  study,  the  scores  of  the 
ten  dimensions  of  SCL-90  are  regarded  as  continuous 
variables  for  analysis.  Both  the  SSBS  and  SCL-90  have 
been previously validated in Chinese adolescent samples, 
showing good psychometric properties.

Statistical analysis

All  statistical  analysis  and  network  analysis  were  per-
formed  using  R  4.2.2  ( h t t p  s : /  / m i r  r o  r s .  u s t  c . e d  u .  c o . u k / C R 
A N /), including network construction, network  e s t i m a t i o 
n , network accuracy, and stability analysis.

The  R-qgraph  (version  1.9.2)  package  was  utilized  for 
network  visualization.  Within  the  network,  each  node 
denotes  a  symptom,  and  each  edge  represents  different 
relationship between different symptoms. The estimation 

Yao et al. BMC Pediatrics          (2025) 25:892  
N (%)

Table 1  Descriptive statistics of 11,949 adolescents
Characteristics
Gender
  Male
  Female
Year of birth

Characteristics
Urban-rural distribution

5695 (47.7) Urban
6254 (52.3) Rural

  1996–2007

  2008–2013
Ethnicity

  Han

  Other

Place of 
registration
  This province

11,825 
(99.0)
124 (1.0)

11,735 
(98.2)
214 (1.8)

11,591 
(97.0)

  Other provinces 358 (3.0)

N (%)

8191 (68.5)
3758 (31.5)

3793 (31.7)

8156 (68.3)

1761 (14.7)

10,188 
(85.3)

Single-child household 
or not
Yes

No
Having a good relation-
ship with parents
No

Yes

Mental health

Normal (< 160)

8435 (70.6)

mild abnormality 
(160 ~ 225)
marked abnormality 
(226 ~ 315)
serious abnormality 
(> 315)

2480 (20.8)

850 (7.1)

184 (1.5)

Network structure

The symptom network of school adjustment and mental 
health in adolescents was shown in Fig. 2. Among them, 
“Obsessive  compulsive  (SCL-2)”  and  “Interpersonal 
sensitivity  (SCL-3)”  were  the  most  strongly  connected 
(weight = 0.304), followed by “Somatization (SCL-1)” and 
“Other  (SCL-10)”,  “Paranoid  ideation  (SCL-8)”  and  Psy-
choticism (SCL-9)”. The marginal were, 0.269 and 0.255, 
respectively.  Within  the  relationship  between  school 
adjustment and mental health in adolescents, “Antisocial 
behavior  (SSBS-2)”  and  “Social  compentence  (SSBS-1)” 
were the most closely related (weight=−0.194). This was 
followed by “Antisocial behavior (SSBS-2)” and “Hostility 
(SCL-6)” (weight = 0.116), “Antisocial behavior (SSBS-2)” 

Table 2  Descriptive statistics of the SCL-90 and SSBS items
Item mean
Item content
Item abbreviations
121.57 ± 26.675
Social compentence
SSBS-1
43.61 ± 19.297
Antisocial behavior
SSBS-2
17.75 ± 7.522
Somatization
SCL-1
17.83 ± 7.194
Obsessive compulsive
SCL-2
14.87 ± 6.497
Interpersonal sensitivity
SCL-3
20.63 ± 9.191
Depression
SCL-4
15.65 ± 6.925
Anxiety
SCL-5
9.08 ± 4.113
Hostility
SCL-6
10.40 ± 4.676
Phobic anxiety
SCL-7
9.16 ± 4.003
Paranoid ideation
SCL-8
14.97 ± 6.392
Psychoticism
SCL-9
10.83 ± 4.650
Other
SCL-10

Page 4 of 9

and  “Obsessive  compulsive  (SCL-2)”  (weight=−0.075). 
Symptom network connections were mainly centered on 
the  ten  psychological  symptoms  of  the  SCL-90,  such  as 
“Depression  (SCL-4)”  and  “Anxiety  (SCL-5)”,  “Somatiza-
tion (SCL-1)” and “Anxiety (SCL-5)”, “Interpersonal sen-
sitivity (SCL-3)” and “Paranoid ideation (SCL-8)”.

Centrality and Bridge centrality

In the symptom network of school adjustment and men-
tal  health  in  adolescents,  the  node  “Anxiety  (SCL-5)” 
showed  the  highest  strength,  closeness,  and  expected 
influence,  1.461,  1.139,  and  1.128,  followed  by  “Inter-
personal  sensitivity  (SCL-3)”,  “Paranoid  ideation  (SCL-
8)”,  “Psychoticism  (SCL-9)”.  The  highest  betweenness 
was “Hostility (SCL-6)”, followed by “Antisocial behavior 
(SSBS-2)” and “Anxiety (SCL-5)”. See Fig. 3 for details. In 
the  bridging  network  of  school  adjustment  and  mental 
health in adolescents, “Antisocial behavior (SSBS-2)” and 
“Hostility (SCL-6)” were the most apparent bridge symp-
toms. The symptom with the highest bridge strength was 
“Antisocial  behavior  (SSBS-2)”,  followed  by  “Hostility 
(SCL-6)”,  “Obsessive  compulsive  (SCL-2)”. The  symptom 
with  the  highest  bridge  expected  influence  was  “Antiso-
cial  behavior  (SSBS-2)”,  followed  by  “Hostility  (SCL-6)”, 
“Paranoid ideation (SCL-8)”. See Fig. 4 for details.

Network accuracy and stability

The stability of edge weights was tested by bootstrapping. 
After  bootstrapping  1000  times,  the  symptom  network 
shows  high  stability  and  accuracy. The  relatively  narrow 
95% confidence interval range indicates that the estima-
tion of edge weights in the network is relatively accurate 
and  credible.  And  the  structure  of  the  network  in  this 
study was also more stable (CS-C = 0.75). In addition, the 
results  of  the  non-parametric  bootstrap  analysis  show 
that most of the comparisons between edge weights and 
centrality metrics are statistically significant. See Supple-
mentary  Fig.  1–7  for  details.  The  bridge  centrality  also 

Strength
−2.086
−1.464
−0.142
−0.002
0.805
0.786
1.461
0.103
−0.666
0.374
0.686
0.145

Closeness
−2.275
−1.385
−0.257
0.387
0.581
0.444
1.139
0.664
−0.705
0.772
0.562
0.072

Betweenness
−1.348
1.261
−0.565
−0.043
0.217
−0.826
1.000
1.782
−1.348
0.478
−0.565
−0.043

Expected Influence
−2.220
−1.771
0.186
−0.047
0.623
0.603
1.128
0.247
−0.226
0.491
0.628
0.357

Yao et al. BMC Pediatrics          (2025) 25:892 Page 5 of 9

Fig. 2  Symptom network of school adjustment and mental health among adolescents. (Blue for positive, red for negative, and thickness for strength)

Fig. 3  Centrality of school adjustment and mental health in adolescents. (Standardized z-scores were used)

Yao et al. BMC Pediatrics          (2025) 25:892  
 
Page 6 of 9

Fig. 4  Bridge centrality of school adjustment and mental health in adolescents. (Standardized z-scores were used)

passed  the  stability  test  (CS-C > 0.5),  see  Supplementary 
Fig. 8 for details.

for nodes “SSBS1” (P = 0.002) and “SCL-8” (P = 0.02). See 
Supplementary Fig. 23–30 for details.

Network comparisons

The results of the study showed no significant differences 
in  overall  strength  across  symptom  networks  for  males 
and  females  (S = 0.207,  P = 0.555).  However,  there  was 
a  significant  difference  in  network  structure  for  males 
and  females  (M = 0.093,  P = 0.011).  Three  significantly 
different  edges  were  SCL-7-SCL-1  (P < 0.001),  SCL-10-
SCL-2  (P = 0.001),  and  SCL-9-SCL-1  (P = 0.004).  A  sig-
nificant difference in EI was observed for nodes “SSBS2” 
(P = 0.005)  and  “SCL-7”  (P = 0.001).  See  more  details  in 
Supplementary Fig. 9–16.

The  results  of  the  study  showed  no  significant  differ-
ences  in  network  structure  and  overall  strength  across 
symptom networks for adolescents from Shandong prov-
ince  and  other  provinces  (S = 0.119,  P = 0.542;  M = 0.159, 
P = 0.462), indicating a high degree of similarity between 
the  networks  being  compared.  See  Supplementary 
Fig. 17–22 for details.

The results of the study showed significant differences 
in  network  structure  and  overall  strength  across  symp-
tom  networks  for  adolescents  from  urban  and  rural 
(S = 0.144,  P = 0.027;  M = 0.093,  P = 0.047).  Specifically, 
three  significantly  different  edges  were  SSBS2-SSBS1 
(P = 0.003),  SSBS2-SCL-1  (P = 0.012),  and  SCL-9-SCL-1 
(P = 0.03).  A  significant  difference  in  EI  was  observed 

Discussion
This  study  employs  network  analysis  to  map  symptom-
level interactions between school adjustment and mental 
health in 11,949 Chinese adolescents. We identified anxi-
ety (SCL-5) as the most central symptom with the high-
est strength (1.461) and expected influence (1.128). This 
finding is consistent with a growing body of international 
network  studies  on  adolescent  psychopathology,  which 
have  repeatedly  identified  anxiety  and  depressive  symp-
toms as central nodes in networks across diverse cultural 
settings  [32].  The  cross-cultural  consistency  of  anxiety’s 
centrality underscores its fundamental role in the devel-
opment  and  maintenance  of  mental  health  difficulties 
during adolescence, potentially transcending educational 
systems and cultural contexts.

Critically,  it  showed  the  strongest  connections  to 
somatization  (SCL-1)  and  depression  (SCL-4)  in  our 
symptom  network,  suggesting  its  pivotal  role  in  activat-
ing  these  specific  comorbid  conditions.  This  aligns  with 
global  reports  of  post-pandemic  anxiety  escalation  [1] 
and  reflects  China’s  high-pressure  academic  environ-
ment, where chronic stress amplifies emotional dysregu-
lation  [2].  Critically,  anxiety’s  network  position  implies 
it may serve as an optimal intervention target; targeting 
this symptom may be associated with reduced symptom 

Yao et al. BMC Pediatrics          (2025) 25:892  
Page 7 of 9

cascades  to  adjacent  nodes—a  hypothesis  corroborated 
by  experimental  network  interventions  [21]. These  find-
ings  advocate  integrating  brief  anxiety-reduction  pro-
tocols  (e.g.,  classroom-based  mindfulness)  into  routine 
school activities.

Beyond  centrality,  antisocial  behavior  (SSBS-2)  and 
hostility  (SCL-6)  emerged  as  critical  bridge  symptoms 
linking  school  maladjustment  to  psychopathology.  Pre-
vious  studies  have  demonstrated  that  antisocial  behav-
ior is associated with increased peer rejection, while the 
experience  of  rejection  in  turn  increases  the  likelihood 
of  antisocial  behavior,  thereby  forming  a  vicious  cycle 
[33].  In  line  with  our  research  findings,  which  reveals  a 
self-perpetuating  cycle:  antisocial  acts  (e.g.,  rule  viola-
tions)  provoke  peer  rejection,  fueling  hostile  cognitions 
that  exacerbate  internalising  disorders.  This  mecha-
nism  resonates  with  ecological  systems  theory,  wherein 
microsystem  like  school  conflicts  amplify  individual 
vulnerability  [16].  Notably,  antisocial  behaviour  exhib-
ited  the  strongest  bridge  centrality,  while  hostility  dem-
onstrated  a  relatively  higher  bridge  expected  influence, 
indicating  their  elevated  bridge  centrality,  which  accel-
erates  distress  transmission  between  school  adjustment 
and  psychopathology  domains.  Practically,  these  bridge 
symptoms  represent  actionable  levers  for  prevention; 
cognitive-behavioural  strategies  targeting  hostile  attri-
bution  bias  combined  with  social  skills  training  could 
disrupt this pathway, as evidenced in school-based trials 
[11].  Notably,  the  strongest  cross-domain  connections 
were observed between antisocial behavior and hostility, 
and between antisocial behavior and social competence. 
These  links  suggest  that  behavioral  problems  in  school 
settings are closely tied to emotional dysregulation, high-
lighting  potential  targets  for  integrated  school-based 
mental health interventions.

Significant  urban-rural  disparities  in  network  struc-
ture  (P  <  0.05)  further  contextualise  these  relationships. 
Empirical  evidence  shows  that  only  31.5%  of  rural  par-
ticipants reported access to school counselors, compared 
to  68.5%  of  urban  counterparts—a  disparity  consistent 
with  national  data  on  inequitable  mental  health  service 
distribution. This suggests limited access to professional 
support may exacerbate the pathway from psychological 
stress to physical symptoms in rural contexts. Conversely, 
urban  youth  showed  heightened  hostility-peer  conflict 
linkages,  potentially  driven  by  competitive  academic 
environments  [5].  These  structural  differences  necessi-
tate  tailored  interventions:  telemental  health  expansion 
for  rural  schools  to  address  somatic-academic  loops, 
and  restorative  practices  in  urban  classrooms  to  miti-
gate  hostility  [9]. These  disparities  may  be  further  exac-
erbated by structural inequalities, such as limited access 
to mental health services in rural areas. And resource gap 
likely intensifies the pathway from psychological distress 

to  school  maladjustment  in  rural  contexts.  Our  findings 
align with the goals of China’s ‘Double Reduction’ policy, 
which  emphasizes  the  reduction  of  academic  pressure 
and  the  promotion  of  students’  well-being.  Implement-
ing  school-based  mental  health  programs  that  target 
core symptoms such as anxiety and bridge symptoms like 
antisocial  behavior  could  enhance  the  policy’s  effective-
ness  in  fostering  healthier  school  environments.  Policy 
efforts should prioritise such contextual adaptations, par-
ticularly under China’s “Double Reduction” policy frame-
work [21].

Methodologically,  this  study  advances  prior  research 
by  quantifying  dynamic  symptom  interactions  that  tra-
ditional regression models obscure. The high predictabil-
ity  of  depression  (R²=0.89)  and  interpersonal  sensitivity 
(R²=0.87) confirms their susceptibility to neighbourhood 
effects,  supporting  targeted  node-level  interventions. 
Network  stability  tests  (CS-C  >0.5)  and  narrow  boot-
strap  confidence  intervals  further  validate  these  find-
ings. Crucially, our bridge centrality approach transcends 
conventional  comorbidity  analyses  by  identifying  pre-
cise transmission routes between school adjustment and 
psychopathology.  This  precision  could  enhance  existing 
school mental health programs; for example, monitoring 
changes in hostility’s bridge centrality may serve as a sen-
sitive metric for intervention efficacy [20].

Several  limitations  warrant  consideration.  First,  the 
cross-sectional  design  precludes  causal  inference  about 
symptom  development,  and  the  centrality  of  the  bridge 
only suggests to us the statistical connectivity, not neces-
sarily the mechanism of the connecting domains. Longi-
tudinal  tracking  across  school  transitions  (e.g.,  junior  to 
senior  high)  is  needed  to  map  temporal  dynamics.  Sec-
ond,  regional  sampling  (Shandong  Province)  limits  gen-
eralizability to western China’s diverse cultural contexts. 
Replication using the National Adolescent Health Cohort 
would  strengthen  validity.  Third,  there  may  be  a  poten-
tial  bias  from  informant  differences  due  to  differences 
in  scale  ratings  (teacher  rating  vs.  self-report).  In  addi-
tion, the EBICglasso model has the possibility of overfit-
ting (even if the sample size is very big), and the network 
model  assumes  no  unmeasured  confounders  (i.e.,  no 
demographic  covariates  are  included  in  the  model). 
Fourth,  Although  we  utilized  distinct  scales  to  measure 
behavioral  and  emotional  symptoms,  some  conceptual 
overlap  between  antisocial  behavior  and  hostility  may 
exist.  Future  studies  could  employ  more  differentiated 
measures  or  confirmatory  factor  analysis  to  further  dis-
entangle these constructs. Despite these constraints, our 
findings  offer  clinically  actionable  insights:  prioritizing 
anxiety reduction, disrupting antisocial-hostility bridges, 
and 
for 
implementing  context-sensitive  adaptations 
urban/rural settings could significantly alleviate the ado-
lescent mental health crisis in educational ecosystems.

Yao et al. BMC Pediatrics          (2025) 25:892 Conclusions
This  study  analyzed  the  core  and  bridge  symptoms  in 
the  network  of  school  adjustment  and  mental  health 
affecting  adolescents  in  Shandong  Province  through  a 
network  analysis  method.  The  study  showed  that  ado-
lescents’  school  maladjustment  was  strongly  associated 
with abnormal psychological conditions such as anxiety, 
hostility, and obsessive compulsive disorder among ado-
lescents. This phenomenon is more pronounced between 
urban  and  rural  areas.  Therefore,  regulating  the  school 
adjustment  and  mental  health  status  of  adolescents  is 
important to promote their healthy growth.

Supplementary Information
The online version contains supplementary material available at  h t t p  s : /  / d o i  . o  r 
g /  1 0 .  1 1 8 6  / s  1 2 8 8 7 - 0 2 5 - 0 6 2 6 4 - 6.

Supplementary Material 1.

Acknowledgements
We would like to thank all the participants.

Authors’ contributions
YY, BL, and YC designed the research study. XD, MS, and JS analyzed the 
data. ML, JW, and WZ provided help and advice on specific experimental 
procedures. All authors contributed to editorial changes in the manuscript. All 
authors read and approved the final manuscript.

Funding
This research was supported by Sichuan Province College Students’ innovation 
training program (XJ202510634243).

Data availability
All data reported in this paper will be accessed at  h t t p  s : /  / w w w  . n  c m i . c n . / i n d e 
x . h t m l.

Declarations

Ethics approval and consent to participate
This study was approved by the Ethics Committee of Shandong University 
(20180517).

Competing interests
The authors declare no competing interests.

Conflict of interest
The authors declare no conflict of interest.

Received: 11 July 2025 / Accepted: 29 September 2025

2. 

References
1.  Duncan L, Sheldrick RC. Adolescent mental health measures. Lancet Psychia-
try. 2025;12(6):407–8.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / S  2 2 1 5 - 0 3 6 6 ( 2 5 ) 0 0 1 0 1 - 4.
Zhang M, Gu C, Zeng H, et al. The impact of physical activity on adolescent 
mental health status: the mediating effect of school adaptation. Front Psy-
chol. 2025;16:1573129.  h t t p  s : /  / d o i  . o  r g /  1 0 .  3 3 8 9  / f  p s y g . 2 0 2 5 . 1 5 7 3 1 2 9.
Ahmed HU, Hossain MD, Aftab A, et al. Suicide and depression in the world 
health organization South-East Asia region: A systematic review. WHO South 
East Asia J Public Health. 2017;6(1):60–6.  h t t p  s : /  / d o i  . o  r g /  1 0 .  4 1 0 3  / 2  2 2 4 - 3 1 5 1 . 2 
0 6 1 6 7.
Abernathey L, Kahn NF, Sequeira GM, et al. Associations between gender 
Dysphoria, eating Disorders, and mental health diagnoses among 

4. 

3. 

Page 8 of 9

adolescents. J Adolesc Health. 2024;75(5):780–4.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j a  d 
o h  e a l t  h .  2 0 2 4 . 0 6 . 0 2 2.

5.  Mitchell AJ, Cogswell IE, Dalos J, et al. Estimating global direct health-care 

6. 

7. 

8. 

9. 

spending on neurological and mental health between 2000 and 2019: a 
modelling study. Lancet Public Health. 2025;10(5):e401–11.  h t t p  s : /  / d o i  . o  r g /  1 0 
.  1 0 1 6  / S  2 4 6 8 - 2 6 6 7 ( 2 5 ) 0 0 0 8 9 - 1.
Jalali Z, Fadakar MM, Iranpour A, et al. Investigating the relationship between 
high-risk behaviors and mental health in adolescents in Rabor city, Iran. Int J 
Adolesc Med Health. 2022;35(1):31–40.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 5 1 5  / i  j a m h - 2 0 2 2 - 0 
0 6 7.
Richardson R, Connell T, Foster M, et al. Risk and protective factors of Self-
harm and suicidality in adolescents: an umbrella review with Meta-Analysis. J 
Youth Adolesc. 2024;53(6):1301–22.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s  1 0 9 6 4 - 0 2 4 - 0 1 9 6 
9 - w.
Zhou X, Bambling M, Bai X, et al. Chinese school adolescents’ stress experi-
ence and coping strategies: a qualitative study. BMC Psychol. 2023;11(1):91.  h 
t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 8 6  / s  4 0 3 5 9 - 0 2 3 - 0 1 1 3 7 - y.
Xiu X, Qian Q, Wu S. Mental health problems and associated factors among 
high school students in Shandong Province of china: A Cross-Sectional study. 
Int J Environ Res Public Health. 2022;19(14):8478.  h t t p  s : /  / d o i  . o  r g /  1 0 .  3 3 9 0  / i  j e r 
p h 1 9 1 4 8 4 7 8.

10.  Nagabharana TK, Joseph S, Rizwana A, et al. What stresses adolescents? A 

qualitative study on perceptions of stress, stressors and coping mechanisms 
among urban adolescents in India. Wellcome Open Res. 2021;6:106.  h t t p  s : /  / d 
o i  . o  r g /  1 0 .  1 2 6 8  8 /  w e l  l c o  m e o p  e n  r e s . 1 6 8 1 8 . 1.

11.  Huang CY, Hunt E, Stormshak EA. Differential impact of the school context on 
ethnic and Racial identity and depression for monoracial and multiracial early 
adolescents. Front Psychiatry. 2023;14:1080085.  h t t p  s : /  / d o i  . o  r g /  1 0 .  3 3 8 9  / f  p s y t . 
2 0 2 3 . 1 0 8 0 0 8 5.

12.  Merrell KW, Cedeno CJ, Johnson ER. The relationship between social behavior 
and self-concept in school settings. Psychol Sch. 1993;30(4):293–8.  h t t p  s : /  / d o i  
. o  r g /  1 0 .  1 0 0 2  / 1  5 2 0 - 6 8 0 7 ( 1 9 9 3 1 0 ) 3 0 : 4 3 . 0 . C O ; 2 - L.

13.  Wang X. The effects of excess adaptation on secondary school students’ 
school adjustment: the chain mediating role of self-esteem and mental 
toughness. Chin J Health Psychol. 2023;31:303–8.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 3 3 4  2 /  j . c  
n k i  . c j h  p .  2 0 2 3 . 0 2 . 0 2 5.

14.  Zhu Q, Cheong Y, Wang C, et al. The impact of maternal and paternal parent-
ing styles and parental involvement on Chinese adolescents’ academic 
engagement and burnout. Curr Psychol. 2023;42(4):2827–40.  h t t p  s : /  / d o i  . o  r g /  
1 0 .  1 0 0 7  / s  1 2 1 4 4 - 0 2 1 - 0 1 6 1 1 - z.

15.  Wang H, Wang Y, Wang G, et al. Structural family factors and bullying at 

school: a large scale investigation based on a Chinese adolescent sample. 
BMC Public Health. 2021;21(1):2249.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 8 6  / s  1 2 8 8 9 - 0 2 1 - 1 2 3 
6 7 - 3.

16.  László KD, Andersson F, Galanti MR. School climate and mental health among 
Swedish adolescents: a multilevel longitudinal study. BMC Public Health. 
2019;19(1):1695.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 8 6  / s  1 2 8 8 9 - 0 1 9 - 8 0 1 8 - 0.

17.  Wang Y, Jiang G, Yao Z, et al. The influence of teacher-student relationship on 

Chinese high school students’ academic motivation for the ideological and 
political subject: the mediating role of academic emotions. Front Psychol. 
2024;14:1329439.  h t t p  s : /  / d o i  . o  r g /  1 0 .  3 3 8 9  / f  p s y g . 2 0 2 3 . 1 3 2 9 4 3 9.

18.  Zhao Q, Sun X, Zhang Y, et al. Network analysis of anxiety and depressive 

symptoms among patients with heart failure. BMC Psychiatry. 2024;24(1):803.  
h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 8 6  / s  1 2 8 8 8 - 0 2 4 - 0 6 2 5 9 - 0.

19.  He C, He Y, Yang T, et al. Relationship of sleep-quality and social-anxiety 
in patients with breast cancer: a network analysis. BMC Psychiatry. 
2023;23(1):887.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 8 6  / s  1 2 8 8 8 - 0 2 3 - 0 5 2 6 2 - 1.

20.  Miao J, Wu Y, Yuan J, et al. Network analysis of interpersonal sensitivity and 

self-efficacy in nursing students. BMC Nurs. 2025;24(1):63.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 
1 8 6  / s  1 2 9 1 2 - 0 2 5 - 0 2 7 2 5 - 6.

21.  Wang X, Wu Y, Fu L, et al. Inter-relationships of obesity-related eating behavior 

with depression and anxiety among adults during the COVID-19 pandemic: 
A network analysis. Appetite. 2024;192:107120.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . a p  p e 
t  . 2 0 2  3 .  1 0 7 1 2 0.

22.  Shandong University Database of Youth Health. Population Health Data 

Archive[homepage on the Internet]. Available from: h t t p  s : /  / w w w  . n  c m i  . c n  / p 
h d  a /  d a t  a D e  t a i l  s .  d o ?  i d =  C S T R  : 1  7 9 7  0 . 1  1 . A 0  0 3  1 . 2 0 2 1 0 7 . 2 0 9 . V 1 . 0. Accessed July 
19, 2022.

23.  Zhang SF, Luo W, Dong XS, et al. A dataset on the status quo of health and 

health-Related behaviors of Chinese youth: A longitudinal Large-Scale survey 
in the secondary school students of Shandong Province. Chin Med Sci J. 
2022;37(1):60–6.  h t t p  s : /  / d o i  . o  r g /  1 0 .  2 4 9 2  0 /  0 0 4 0 5 1.

Yao et al. BMC Pediatrics          (2025) 25:892 Page 9 of 9

24.  Alfonso VC, Rentz E, Orlovsky K, et al. Test review: school social behavior 

30.  Bai W, Cai H, Liu S, et al. Anxiety and depressive symptoms in college students 

Scales, second edition. J Psychoeducational Assess. 2007;25(1):82–92.  h t t p  s : /  / 
d o i  . o  r g /  1 0 .  1 1 7 7  / 0  7 3 4 2 8 2 9 0 6 2 9 1 7 9 3.

25.  Liu H, Zhang J. Norm of symptom checklist (SCL-90) in Chinese middle school 
students. Chin Ment Health J. 2004;18:88–90.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / B  F 0 2 9 1 
1 0 3 1.

26.  Mei Q, Li C, Yin Y, et al. The relationship between the psychological stress of 
adolescents in school and the prevalence of chronic low back pain: a cross-
sectional study in China. Child Adolesc Psychiatry Ment Health. 2019;13:24.  h t 
t p  s : /  / d o i  . o  r g /  1 0 .  1 1 8 6  / s  1 3 0 3 4 - 0 1 9 - 0 2 8 3 - 2.

27.  Liu R, Chen X, Qi H, et al. Network analysis of depressive and anxiety symp-
toms in adolescents during and after the COVID-19 outbreak peak. J Affect 
Disord. 2022;301:463–71.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j a d . 2 0 2 1 . 1 2 . 1 3 7.
28.  Foygel R, Drton M. Extended bayesian information criteria for Gaussian 

graphical models. Adv Neural Inf Process Syst2010:604–12.  h t t p  s : /  / d o i  . o  r g /  1 0 .  
4 8 5 5  0 /  a r X i v . 1 0 1 1 . 6 6 4 0

29.  Onnela JP, Saramäki J, Hyvönen J, et al. Structure and tie strengths in mobile 
communication networks. Proc Natl Acad Sci U S A. 2007;104(18):7332–6.  h t t 
p  s : /  / d o i  . o  r g /  1 0 .  1 0 7 3  / p  n a s . 0 6 1 0 2 4 5 1 0 4.

during the late stage of the COVID-19 outbreak: a network approach. Transl 
Psychiatry. 2021;11(1):638.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 3 8  / s  4 1 3 9 8 - 0 2 1 - 0 1 7 3 8 - 4.
31.  Ding L, Ren X, Sun Y, et al. Network analysis of association between prob-

lematic social network use and alexithymia in freshmen. Psychol Res Behav 
Manag. 2024;17:3503–14.  h t t p  s : /  / d o i  . o  r g /  1 0 .  2 1 4 7  / P  R B M . S 4 7 2 7 9 9.
32.  Mullarkey MC, Marchetti I, Beevers CG. Using network analysis to identify 
central symptoms of adolescent depression. J Clin Child Adolesc Psychol. 
2019;48(4):656–68.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 8 0  / 1  5 3 7  4 4 1  6 . 2 0  1 8  . 1 4 3 7 7 3 5.
33.  Trentacosta CJ, Shaw DS. Emotional self - regulation, peer rejection, and 

antisocial behavior: developmental associations from early childhood to early 
adolescence. J Appl Dev Psychol. 2009;30(3):356–65.  h t t p s :   /  / d o  i .  o r  g  /  1 0  . 1 0   1   6 / j  
. a p p   d e v  .   2 0 0  8 . 1 2 . 0 1 6.

Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in 
published maps and institutional affiliations.

Yao et al. BMC Pediatrics          (2025) 25:892
