# Koppe_2019_Recurrent Neural Networks in Mobile Sampling and Intervention.

Schizophrenia Bulletin vol. 45. no. 2 pp. 272–276, 2019 
doi:10.1093/schbul/sby171
Advance Access publication 28 November 2018

ENVIRONMENT AND SCHIZOPHRENIA

Recurrent Neural Networks in Mobile Sampling and Intervention

Georgia Koppe*,1,2, Sinan Guloksuz3,4, Ulrich Reininghaus,3,5–7, and Daniel Durstewitz1,7 

1Department of Theoretical Neuroscience, Central Institute of Mental Health, Medical Faculty Mannheim, Heidelberg University, 
Mannheim, Germany; 2Department of Psychiatry and Psychotherapy, Central Institute of Mental Health, Medical Faculty Mannheim, 
Heidelberg University, Mannheim, Germany; 3Department of Psychiatry and Psychology, School for Mental Health and Neuroscience, 
Maastricht University, Maastricht, The Netherlands; 4Department of Psychiatry, Yale University School of Medicine, New Haven, 
CT; 5Department of Public Mental Health, Central Institute of Mental Health, Medical Faculty Mannheim, University of Heidelberg, 
Mannheim, Germany; 6Centre for Epidemiology and Public Health, Health Service and Population Research Department, Institute of 
Psychiatry, Psychology and Neuroscience, King’s College London, London, UK

7These authors contributed to this work as joint senior authors.

*To whom correspondence should be addressed; J 5, 68159 Mannheim, Germany; tel: 621-1703-2364, e-mail: georgia.koppe@
zi-mannheim.de

The rapid rise and now widespread distribution of handheld 
and wearable devices, such as smartphones, fitness trackers, 
or  smartwatches,  has  opened  a  new  universe  of  possibili-
ties for monitoring emotion and cognition in everyday-life 
context, and for applying experience- and context-specific 
interventions in psychosis. These devices are equipped with 
multiple sensors, recording channels, and app-based oppor-
tunities  for  assessment  using  experience  sampling  meth-
odology (ESM), which enables to collect vast amounts of 
temporally highly resolved and ecologically valid personal 
data from various domains in daily life. In psychosis, this 
allows  to  elucidate  intermediate  and  clinical  phenotypes, 
psychological  processes  and  mechanisms,  and  their  inter-
play with socioenvironmental factors, as well as to evalu-
ate  the  effects  of  treatments  for  psychosis  on  important 
clinical  and  social  outcomes.  Although  these  data  offer 
immense  opportunities,  they  also  pose  tremendous  chal-
lenges for data analysis. These challenges include the sheer 
amount of time series data generated and the many differ-
ent data modalities and their specific properties and sam-
pling rates. After a brief review of studies and approaches 
to ESM and ecological momentary interventions in psycho-
sis,  we  will  discuss  recurrent  neural  networks  (RNNs)  as 
a powerful statistical machine learning approach for time 
series analysis and prediction in this context. RNNs can be 
trained on multiple data modalities simultaneously to learn 
a dynamical model that could be used to forecast individual 
trajectories and schedule online feedback and intervention 
accordingly.  Future  research  using  this  approach  is  likely 
going  to  offer  new  avenues  to  further  our  understanding 
and treatments of psychosis.

Key  words:  mobile  health  (mHealth)/deep  neural  net-
works/machine  learning/ecological  momentary  assess-
ment/ecological 
intervention/digital 
phenotyping and schizophrenia

momentary 

Introduction

In recent years, the use of behavioral, physiological, and 
other  digital  data  collected  in  the  context  of  daily  life 
using wearable technologies to improve understanding of 
various  mental  health  outcomes  has  received  increasing 
attention. Recent work applying machine learning meth-
ods  to  experience  sampling  methodology  (ESM)  data 
showed  that  patterns  differentiating  patients  with  psy-
chosis  spectrum  disorder  from  controls  could  be  recog-
nized with up to 82% accuracy.1 This article explores the 
potential  of  (deep)  recurrent  neural  networks  (RNNs), 
a machine learning method, which has been successfully 
applied for many types of time series data with sequential 
structure,  like  language  and  text  processing2  or  motion 
data,3  for  harnessing  digital  data  from  wearable  devices 
to  further  our  understanding  and  optimizing  treatment 
of psychosis.

Understanding Psychosis in Context

Over  the  past  decade,  there  has  been  a  growing  num-
ber of studies using ESM4 (or synonymously, ecological 
momentary assessment5–7) to investigate the phenomenol-
ogy, onset, course, and outcome of psychosis in daily life, 
outside the research laboratory. ESM is a structured diary 

272

© The Author(s) 2018. Published by Oxford University Press on behalf of the Maryland Psychiatric Research Center. All rights reserved. For permissions, please email: journals.permissions@oup.comtechnique that allows us to assess variation in thoughts, 
feelings,  and  behaviors  from  one  moment  to  the  next 
using repeated, naturalistic sampling several times a day 
over  a  number  of  (often  consecutive)  days.4–7  Data  col-
lected using the ESM are now often referred to as active 
or explicit data, more generally,8 and there is a long tra-
dition  of  collecting  data  other  than  self-report  requir-
ing  active  participation  of  the  participant  in  experience 
sampling research such as taking cortisol samples.9 ESM 
is  more  than  just  a  data  collection  method.  As  pointed 
out  in  a  recent  review  by  Myin-Germeys  et  al,7  ESM 
has  its  origins  in  ecological  psychology  and  emerged 
from  the  idea  that  experience  and  behavior  are  situated 
in  context  and  vary  over  time,  and  thus,  should  always 
be  assessed  and  investigated  in  relation  to  this  context, 
and in the moment.7 This is nowadays typically achieved 
through using mobile devices, primarily applications on 
smartphones, and, although a number of methodological 
challenges and ethical issues remain,7 over 2 decades of 
experience sampling research in psychosis10,11 make ESM 
the  most  widely  used  and  methodologically  grounded 
mobile Health (mHealth) assessment method in the field. 
The  most  promising  use  of  ESM  in  psychosis  research 
has been in identifying intermediate and clinical pheno-
types,  investigating  psychological  processes  and  mecha-
nisms  (including  cognitive  variables  using  experimental 
ESM  tasks12),  and  studying  the  interplay  with  socioen-
vironmental  contexts  in  daily  life,  as  well  as  evaluating 
treatment effects for psychosis on important clinical and 
social outcomes.

Further,  although  ESM  has  long  entailed  collecting 
data in the context of daily life requiring no active par-
ticipation of the participant (eg, data on time, allowing 
to examine timing and calculate time budgets), triangu-
lation with additional, so-called passive or implicit data 
has become more common. This includes the use of GPS 
tracking  (as  another  proxy  for  context),  accelerometers, 
physiological  sensors,  keyboard  interaction  (on  mobile 
devices),  and  data  from  other  smartphone  applications 
(eg, social media) and wearable technologies. This offers 
an  opportunity  to  elucidate  more  fully  how  experience 
and  behavior  of  people  with  psychosis  interact  with 
socioenvironmental  context,  physiological  parameters, 
and  other  proxies  over  time  using  data  from  various 
modalities.  This  may  help  to  approximate  even  better 
ecological  psychology’s  central  posit  of  experience  and 
behavior being situated in context.

Delivering Treatments for Psychosis in Context

Another recent development has extended the principles 
of ESM to the delivery of treatments for psychosis using 
mobile devices as part of what is now commonly referred 
to  as  ecological  momentary  interventions  (EMIs).5,13,14 
EMIs are mHealth interventions that extend beyond pre-
vious ESM research by assuming that, if experience and 

RNNs in Mobile Sampling and Intervention

behavior are situated in context and vary over time, they 
are best targeted and most amenable to change in a given 
moment  and  context.13  More  generally  speaking,  EMIs 
therefore are consistent with, and broaden the scope of, 
community  mental  health  service  delivery  models,  as 
they  aim  to  translate  treatments  for  psychosis  beyond 
clinical settings to patients’ daily life. Examples of EMIs 
for psychosis are FOCUS, an automated intervention to 
provide  illness  management  support  for  psychosis;15,16 
Mobile  Assessment  and  Treatment  for  Schizophrenia,  
a  text-messaging  approach  to  targeting  maladaptive 
beliefs corresponding to outcomes of socialization, med-
ication adherence, and voices in people with psychosis;17 
and  Acceptance  and  Commitment  Therapy  in  Daily 
Life (ACT-DL), which complements ACT sessions with 
3 days of exercises in daily life using an ESM app.

Despite  these  promising  developments,  the  challenge 
that remains at this point is to identify key parameters in 
ESM and other digital data that reflect (1) risk markers 
for  individuals  in  a  given  moment  and  context,  and  (2) 
targets  for  interventions  (that  may  or  may  not  coincide 
with risk markers) that optimize timing and effect on out-
comes in the context of daily life.

Time Series Models and Mobile Data

t

−

∆

,

,

)



=

u
t

x
t

…−
1

θ (
F x
t

x
−…1
t
−

Data from mobile and wearable devices all come as time 
series (or longitudinal data). Time series, ie, the consecu-
tive repeated sampling of data points in time, need special 
attention  and  treatment  from  a  statistical  and  machine 
learning perspective as they are usually (highly) temporally 
dependent and violate the common statistical assumption 
of independent samples. Time series models often express 
temporal dependencies in the data by some time-recursive 
, ie, 
function of the general form  x
t
the current observation  xt  is assumed to depend on the 
∆   of  preceding  observations  up  to  some 
values  x
t
time lag  ∆ , as well as on current external inputs (regres-
sor variables)  ut . θ  denotes parameters of the system (like 
regression weights), and  t  is a noise term (ie, a random 
variable).  To  make  this  concrete,  we  can  consider,  eg, 
the  process  of  sensitization.  Here,  repeated  exposure  to 
an  environmental  risk  factor  results  in  a  progressive  in-
crease of the stress response, such that individuals expe-
rience  a  strong  stress  response  even  to  minor  stressors 
in daily life. It has been hypothesized that this enhanced 
stress response may facilitate the transition to psychosis.18 
In this example, the  xt  may constitute consecutive stress 
responses  (frequently  operationalized  as  stronger  emo-
tional reactions assessed as negative affect ESM ratings), 
∆  
which are related to previous stress responses  x
t
and to minor stressors  ut  (eg, ratings of unpleasant and 
taxing events, activities, and social situations) by a set of 
regression  weights  inferred  from  the  data.  Once  such  a 
model has been trained on the data, it can be used to sta-
tistically test various assumptions about the influence of 

x
−…1
t
−

273

G. Koppe et al

external regressors  ut  or the nature of the dependencies 
in time, and most importantly perhaps, to produce predic-
tions about future states by running it forward in time.

The  most  popular  and  commonly  employed  class  of 
time  series  models  is  “auto-regressive  moving  average 
(ARMA)”  models,  where  Fθ   is  assumed  to  be  a  linear 
function  for  simplicity,  and  temporal  relationships  are 
expressed directly between observations  xt  (ie, in our ex-
ample  the  individual’s  future  stress  response  is  directly 
predicted  from  previous  stress  responses  and  external 
stressors via the estimated regression weights).

t

t

−

|

)

=

1,

,

u
t

More  powerful  and  perhaps  interesting  are  so-called 
latent  variable  (“generative”  or  “state  space”)  models, 
which  assume  that  there  is  some  underlying  but  itself 
(
 that generates the 
unobserved process  z
F z
t
t
θ
observations  xt  according to some probability distribu-
) .19 Time series are usually generated by some 
(
tion p x zt
underlying dynamical system that evolves in time,20 and 
it  is  this  underlying  system  that  we  are  often  ultimately 
interested in. Coming back to our example, we may not 
be so much interested in the subjective ESM ratings per 
se, but only because these hint to some underlying psy-
chological or biological dynamical process we would like 
to tap into. In this specific case, we would be interested in 
the underlying sensitization process (or even concomitant 
changes in the dopaminergic transmitter system posited to 
be involved in this process in the development of psycho-
sis18). Thus,  zt  would model some not directly observed, 
underlying affective, cognitive, or neural process such as 
sensitization  that  gives  rise  to  the  changes  in  subjective 
stress reactivity ratings  xt . Hence latent variable models 

enable us, to some degree, to reveal the true processes of 
interest  from  some  “surface  measurements”  that  are  a 
reflection  of  this  underlying  process.  Although  we  have 
outlined this for just a single observation modality (stress 
reactivity  ratings),  generative  models,  if  designed  prop-
erly, can combine and integrate information from many 
diverse sources, such as different sensor readings on top 
of  ESM  ratings,  or  different  classes  of  environmental 
factors.

RNNs may be seen or cast as such latent variable time 
series  models  where  the  transition  function  Fθ   is  highly 
nonlinear,21,22  a  decisive  difference  to  the  former  more 
common  statistical  models.22,23  It  is  well  known  that 
purely linear systems like ARMA models can only cap-
ture  or  produce  a  very  limited  class  of  dynamical  phe-
nomena,24  eg,  may  not  be  able  to  properly  model  the 
pattern  of  reoccurring  episodes  of  psychotic  symptoms 
with relatively sudden onsets and slower offsets. RNNs, 
on the other hand, which, in theory, can be used to ap-
proximate  (almost)  any  other  dynamical  system,25,26  are 
very powerful devices for modeling and predicting  even 
complex multivariate time series, as they arise from mo-
bile sampling (see figure 1 for details).

Opportunities and Challenges of RNNs for Digital 
Data in Psychosis Research

RNNs  as  latent  variable  models,  when  trained  on  a  set 
of  time  series  data,  come  to  represent  the  underlying 
dynamical  process.  In  this  sense,  they  build  a  dynami-
cal  systems  model  of  the  person  that  could  be  used  for 
predicting  the  individual’s  behavior  and  for  suggesting 

Fig.  1.  (A)  Schema  of  a  state  space  model,  unwrapped  in  time,  where  the  latent  process  is  represented  by  a  recurrent  neural  network 
(RNN). The latent states zt represent the activations of “neural units” that are connected and interact through “synaptic” weights (con-
necting black lines). “Recurrent” means that both forward and backward connections among units are present, in contrast to the much 
more common pure feedforward networks. These recurrent connections are what make these models true time series or dynamical system 
models that express recursive relationships in time. In the graphical representation here, stimulus inputs ut (in this case minor stressors in 
daily life and ecological momentary interventions) exert their effects directly onto the latent states (the underlying dynamical model of a 
person). These in turn generate observations xt, in this case stress response ratings and psychotic experiences, as assessed through ESM and 
other sensors on mobile and wearable devices. (B) Particular RNN architectures, or particular forms of the nonlinearities  Fθ , enable the 
network to detect, represent, and predict very long-term (“deep”) temporal dependencies. By simulating the RNN model forward in time, 
longer-term predictions on future observations can be produced, as for instance depicted here for the example of symptom severity as a 
function of fictive potential stressors and an EMI at future time points.

274

suitable  interventions  ahead  of  time,  to  change  that 
predicted  behavioral  course.  For  instance,  the  models 
could warn individuals about upcoming risks and signal 
critical  periods  for  EMIs  and  other  interventions.  Vice 
versa, by incorporating those EMIs as model inputs, the 
same  RNN  could  be  leveraged  for  predicting  treatment 
response, paving the way for context-dependent and cus-
tomized  interventions.  Ultimately,  a  feedback  loop  that 
optimizes ESMs and EMIs iteratively and subject-specif-
ically could be realized.

This generative aspect of RNNs also enables us to pre-
dict the influence of environmental factors by simulation. 
The model can “generate” new behavior when forwarded 
in time such that model inputs for instance could be emu-
lated  to  assess  the  effect  of  specific  interventions  and 
their (hypothetical) interaction with other variables and 
the dynamical process itself. RNNs may also give insights 
into aberrant mechanisms underlying psychosis or other 
conditions,  and  by  integrating  many  different  features 
and inputs, unravel new types of relations between envi-
ronmental  factors  and  behavior  that  were  previously 
not  known  or  hypothesized  to  exist.  As  these  relations 
may  be rather complex and involve long-term  temporal 
dependencies,21  hard  to  assess  intuitively,  merely  raising 
awareness by feedback could already prove useful from a 
psychoeducative perspective.

Of  course, although very powerful, such models also 
come with major challenges. These include the compu-
tational and data aspects of  model training, ethical and 
data safety issues,27 as well as the selection of  appropri-
ate  model  inputs  and  features  (both  of   which  may  be 
sampled at different frequencies and may follow differ-
ent  distributions).  For  instance,  efficient  RNN  models 
may  often  require  large  amounts  of   data  for  deriving 
their  many  parameters.  A  potential  solution  to  this  is 
“transfer  learning”22,28  where  one  uses  data  obtained 
from a larger group of  individuals for model pretrain-
ing, and data from the single individual for fine-tuning 
the model.29 Especially in such ecological contexts where 
each individual shapes their very own and unique expe-
riences,  integrating  data  across  many  subjects  may  be 
particularly beneficial, as it may enable to piece together 
separate  bits  of   the  same  puzzle.  This  would  also  give 
us  more  powerful  ways  to  study  rare  events  such  as 
when  several  risk  factors  come  together  in  a  specific 
combination.

Conclusion

Recent  years  have  seen  rapid  progress  in  the  use  of 
behavioral,  physiological,  and  other  mobile  data  col-
lected in context of daily life using wearable technologies 
to improve understanding of psychosis. We have argued 
here that RNNs, a powerful statistical machine learning 
approach for time series analysis and prediction, can be 
trained  on  multiple  data  modalities  simultaneously  to 

RNNs in Mobile Sampling and Intervention

learn  a  dynamical  model  to  forecast  individual  trajec-
tories,  and  schedule  online  feedback  and  intervention 
accordingly. Future research using this approach is likely 
going to offer new avenues to further our understanding 
of, and treatments for, psychosis.

Funding

S.G.  was  supported  by  the  European  Community’s 
Seventh  Framework  Program  (grant  agreement  no. 
HEALTH-F2-2009–241909) 
EU-GEI). 
U.R. was supported by a Heisenberg professorship from 
the German Research Foundation (grant no. 389624707). 
D.D. was supported by grants from the German Federal 
Ministry  of  Education  and  Research  within  the  e:Med 
program  (01ZX1311A  [SP7]  and  01ZX1314G  [SP10]) 
and the German Science Foundation (Du 354/8-2).

(project 

Acknowledgment

The authors have declared that there are no conflicts of 
interest in relation to the subject of this study.

References

  1.  Katrineez  A,  Stamate  D,  Alghamdi  W,  et  al.  Predicting  psy-
chosis  using  the  Experience  Sampling  Method  with  mobile 
apps.  2017  16th  IEEE  International  Conference  on  Machine 
Learning and Applications (ICMLA), Cancun, Mexico, 18–21 
December 2017. Los Alamitos, CA: IEEE Computer Society, 
Conference Publishing Services; 2018:667–673.

  2.  Graves A, Mohamed A-R, Hinton G. Speech recognition with 
deep recurrent neural networks. Paper presented at: 2013 IEEE 
International  Conference  on  Acoustics,  Speech  and  Signal 
Processing (ICASSP), 26–31 May 2013; Vancouver, BC.

  3.  Chen  C,  Lu  X,  Markham  A,  Trigoni  N.  IONet:  learning  to 
cure  the  curse  of  drift  in  inertial  odometry.  arXiv  preprint 
arXiv.180202209. 2018.

  4.  Myin-Germeys  I,  Oorschot  M,  Collip  D,  et  al.  Experience 
sampling research in psychopathology: opening the black box 
of daily life. Psychol Med. 2009;39:1533–1547.

  5.  Myin-Germeys I, Birchwood M, Kwapil T. From environment 
to  therapy  in  psychosis:  a  real-world  momentary  assessment 
approach. Schizophr Bull. 2011;37:244–247.

  6.  Shiffman  S,  Stone  AA,  Hufford  MR.  Ecological  momentary 

assessment. Annu Rev Clin Psychol. 2008;4:1–32.

  7.  Myin-Germeys I, Kasanova Z, Vaessen T, et al. Experience sam-
pling methodology in mental health research: new insights and 
technical developments. World Psychiatry. 2018;17:123–132.
  8.  Torous  J,  Larsen  ME,  Depp  C,  et  al.  Smartphones,  sensors, 
and  machine  learning  to  advance  real-time  prediction  and 
interventions for suicide prevention: a review of current pro-
gress and next steps. Curr Psychiatry Rep. 2018;20:51.

  9.  Collip  D,  Nicolson  NA,  Lardinois  M,  Lataster  T,  van  Os  J, 
Myin-Germeys  I;  G.R.O.U.P.  Daily  cortisol,  stress  reactiv-
ity  and  psychotic  experiences  in  individuals  at  above average 
genetic risk for psychosis. Psychol Med. 2011;41:2305–2315.

275

G. Koppe et al

 10.  Delespaul  P.  Assessing  Schizophrenia  in  Daily  Life:  The 
Experience  Sampling  Method.  Maastricht,  the  Netherlands: 
Datawyse/Universitaire Pers Maastricht; 1995.

 11.  Myin-Germeys I, van Os J, Schwartz JE, Stone AA, Delespaul 
PA. Emotional reactivity to daily life stress in psychosis. Arch 
Gen Psychiatry. 2001;58:1137–1144.

 12.  Reininghaus U, Oorschot M, Moritz S, et al. Liberal accept-
ance  bias,  momentary  aberrant  salience,  and  psychosis:  an 
experimental experience sampling study. Schizophr Bull.  2018.
 13.  Reininghaus  U.  [Ecological  momentary  interventions  in  psy-
chiatry:  the  momentum  for  change  in  daily  social  context]. 
Psychiatr Prax. 2018;45:59–61.

 14.  Myin-Germeys  I,  Klippel  A,  Steinhart  H,  Reininghaus  U. 
Ecological momentary interventions in psychiatry. Curr Opin 
Psychiatry. 2016;29:258–263.

 15.  Ben-Zeev  D,  Brenner  CJ,  Begale  M,  Duffecy  J,  Mohr  DC, 
Mueser KT. Feasibility, acceptability, and preliminary efficacy 
of  a  smartphone  intervention  for  schizophrenia.  Schizophr 
Bull. 2014;40:1244–1253.

 16.  Ben-Zeev  D,  Kaiser  SM,  Brenner  CJ,  Begale  M,  Duffecy  J, 
Mohr  DC.  Development  and  usability  testing  of  FOCUS:  a 
smartphone  system  for  self-management  of  schizophrenia. 
Psychiatr Rehabil J. 2013;36:289–296.

 17.  Granholm  E,  Ben-Zeev  D,  Link  PC,  Bradshaw  KR,  Holden 
JL.  Mobile  Assessment  and  Treatment  for  Schizophrenia 
(MATS):  a  pilot  trial  of  an  interactive  text-messaging  inter-
vention for medication adherence, socialization, and auditory 
hallucinations. Schizophr Bull. 2012;38:414–425.

 18.  Collip  D,  Myin-Germeys  I,  Van  Os  J.  Does  the  concept  of 
“sensitization” provide a plausible mechanism for the putative 
link  between  the  environment  and  schizophrenia?  Schizophr 
Bull. 2008;34:220–225.

 19.  Durbin  J,  Koopman  SJ.  Time  Series  Analysis  by  State  Space 

Methods. Vol 38. Oxford University Press; 2012.

 20.  Durstewitz D, Huys QJ, Koppe G. Psychiatric illnesses as dis-
orders of network dynamics. arXiv preprint arXiv.180906303. 
2018.

 21.  Schmidhuber J. Deep learning in neural networks: an overview. 

Neural Netw. 2015;61:85–117.

 22.  Goodfellow  I,  Bengio  Y,  Courville  A.  Deep  Learning.  Vol  1. 

Cambridge, MA: MIT Press; 2016.

 23.  Durstewitz  D.  A  state  space  approach  for  piecewise-linear 
identifying  computational 
recurrent  neural  networks  for 
dynamics  from  neural  measurements.  PLoS  Comput  Biol. 
2017;13:e1005542.

 24.  Strogatz SH. Nonlinear Dynamics and Chaos: With Applications 
to Physics, Biology, Chemistry, and Engineering. Boca Raton, 
FL: CRC Press; 2018.

 25.  Funahashi  K-I,  Nakamura  Y.  Approximation  of  dynamical 
systems by continuous time recurrent neural networks. Neural 
Netw. 1993;6:801–806.

 26.  Kimura  M,  Nakano  R.  Learning  dynamical  systems 
by  recurrent  neural  networks  from  orbits.  Neural  Netw. 
1998;11:1589–1599.

 27.  Dehling  T,  Gao  F,  Schneider  S,  Sunyaev  A.  Exploring  the 
far  side  of  mobile  health:  information  security  and  privacy 
of  mobile  health  apps  on  iOS  and  android.  JMIR  Mhealth 
Uhealth. 2015;3:e8.

 28.  Caruana  R.  Multitask 

learning.  Machine  Learning. 

1997;28:41–75.

 29.  Thodoroff P, Pineau J, Lim A. Learning robust features using 
deep learning for automatic seizure detection. Paper presented 
at  2016  Machine  Learning  for  Healthcare  Conference,  Los 
Angeles, CA. 2016.

276
