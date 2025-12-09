# Landvreugd_2024_Connecting the dots using a network approach to study the wellbeing spectrum.

Current Psychology (2024) 43:27365–27376
https://doi.org/10.1007/s12144-024-06363-0

Connecting the dots: using a network approach to study the wellbeing 
spectrum

Anne Landvreugd1,2

 · Margot P. van de Weijer1,2 · Dirk H. M. Pelt1,2 · Meike Bartels1,2

Accepted: 2 July 2024 / Published online: 6 August 2024
© The Author(s) 2024

Abstract
In positive psychology, defining the wellbeing construct has been a challenge. We used the psychometric network approach 
to study the structure of wellbeing. The sample consisted of Dutch adults registered with the Netherlands Twin Register. 
The variables were measured through standardized surveys. The network was estimated using the Mixed Graphical Models 
method and least absolute shrinkage and selection operator (LASSO) regularization to limit the number of spurious edges. 
We estimated a network in a trimming sample (N=1343, 63% females, Mage = 53.18, SDage = 9.45) and in an estimation 
sample (N=726, 75% females, Mage = 45.27, SDage = 11.12) to examine its performance and accuracy. Our final network 
consists  of  a  positive  cluster  including  satisfaction  with  life,  subjective  happiness,  and  flourishing  items,  and  a  negative 
cluster including depressive symptoms, loneliness, and neuroticism items. We identified the four most central nodes: one 
satisfaction  with  life  item,  one  neuroticism  item,  and  two  depression  items. This  suggests  that  to  get  a  general  sense  of 
the  wellbeing  construct,  these  items  would  serve  as  most  informative.    The  network  approach  clearly  demonstrates  the 
different, yet connected positive and negative clusters of wellbeing and therefore re-affirms the complex interconnectivity 
of wellbeing phenotypes. In addition, the network results reject the view of strictly delineated wellbeing domains. Having 
identified the most central nodes in the network, these can be used in futures studies with limited resources, as they are 
likely to be the most representative of the wellbeing spectrum.

Keywords  Wellbeing · Personality · Depression · Network · Flourishing · Happiness

Introduction

Defining  and  delineating  wellbeing  as  a  construct  has 
proven  to  be  a  difficult  challenge  for  the  field  of  positive 
psychology. Wellbeing can be considered an umbrella term 
for many different more or less connected constructs, which 
can  lead  to  difficulties  when  interpreting  and  comparing 
results from positive psychological research (Linton et al., 
2016).

Anne Landvreugd and Margot P. van de Weijer contributed equally to 
this work.

  Anne Landvreugd

a.landvreugd@vu.nl

1  Department of Biological Psychology, Faculty of 

Behavioural and Movement Sciences, Vrije Universiteit 
Amsterdam, Amsterdam, The Netherlands

2  Amsterdam Public Health Research Institute, Amsterdam 
University Medical Centre, Amsterdam, The Netherlands

Diener’s  theory  on  subjective  wellbeing  (SWB)  is 
grounded in the hedonistic tradition of wellbeing and pro-
poses that SWB is comprised of life satisfaction (cognitive 
SWB), high levels of positive affect, and low levels of nega-
tive  affect  (emotional  SWB)  (Diener,  1984).  On  the  other 
hand,  Ryff’s  theory  on  psychological  wellbeing  (PWB)  is 
grounded in the eudaimonic tradition of wellbeing and states 
that PWB is comprised of six dimensions: autonomy, envi-
ronmental mastery, personal growth, positive relationships, 
purpose in life, and self-acceptance (Ryff, 1989). A similar 
influential theory is self-determination theory (SDT) (Ryan 
&  Deci,  2000).  Central  to  SDT  is  an  individual’s  experi-
ence of autonomy, competence, and relatedness, which are 
argued to promote wellbeing. This is slightly different from 
Ryff’s  PWB  theory,  where  these  dimensions  are  believed 
to  be  components  of  wellbeing.  Combining  aspects  from 
both  eudaimonic  and  hedonic  theory,  Keyes  formulated  a 
theory  on  flourishing  that  posits  that  wellbeing  or  mental 
health  is  defined  by  high  levels  of  emotional,  psychologi-
cal,  and  social  wellbeing,  and  an  absence  of  psychopathy 

1 3

27366

(Keyes, 2005). The inclusion of social wellbeing is in line 
with eudaimonic ideology and is well-supported by wellbe-
ing literature (Keyes, 1998). While these theories focus on 
specific aspects of wellbeing, it is also possible to evaluate 
wellbeing in a broader context. Wellbeing is highly (pheno-
typically and genetically) correlated to multiple traits, such 
as depression, neuroticism, loneliness, and self-rated health. 
In previous research, these traits were collectively referred 
to  as  “the  wellbeing  spectrum”  (WBS)  (Baselmans  et  al., 
2019).

While the previously mentioned wellbeing theories have 
very early origins (Ryff, 1989; Keyes, 2005), the definition 
and concept of wellbeing is continuously being studied in 
recent literature. In a paper from 2020, Intelisano, Krasko & 
Luhmann, aimed to create a model to describe similarities 
and  differences  among  existing  wellbeing  and  happiness 
theories. They proposed a two-dimensional taxonomy: the 
degree of stability and psychological processes. Degree of 
stability refers to whether wellbeing is described as a stable 
trait or a temporary state. The psychological process refers 
to  whether  wellbeing  is  described  as  an  affective  process 
or cognitive process. Their model combined theories from 
both philosophy and psychology, allowing for a more inter-
disciplinary definition of wellbeing (Intelisano et al., 2020). 
Coming from a similar point of view, Michell and Alexan-
drova  (2021)  argue  that  there  is  a  strong  methodological 
basis for well-being pluralism. Wellbeing pluralism would 
accommodate the richness and diversity of wellbeing, allow-
ing us to reconcile the philosophic and scientific concept of 
wellbeing. In 2020, Thorsteinen and Vittersø performed fac-
tor analyses for wellbeing, and estimated a pathway model 
to study the convergent and discriminant validity of hedonic 
wellbeing  and  eudaimonic  wellbeing.  Their  models  con-
cluded that wellbeing is most likely to consist of these two 
constructs, that are distinct but closely related at the same 
time (Thorsteinsen & Vittersø, 2020).

One method to study the structure of a concept such as 
wellbeing has emerged from network theory. Network the-
ory advocates that symptoms are all part  of an  interactive 
system and allows us to take a closer look at item-item asso-
ciations without assuming that their correlations stem from 
an underlying factor (Kan et al., 2020). A network consists 
of a set of nodes (i.e. symptoms) along with a set of speci-
fied ties (edges) linking the nodes (Borgatti & Halgin, 2011; 
Epskamp  et  al.,  2018). The  general  aim  is  to  characterize 
the structure of the network and the position of nodes, and 
to use the network to better understand the examined con-
struct. The network is used to reveal which components are 
most “central” using the concept of centrality: components 
with a high degree of centrality are most strongly connected 
to other items (Fried et al., 2017), and are therefore thought 
to  be  most  influential  in  the  network.  Following  this  line 

of  reasoning,  components  that  are  central  to  the  network 
(i.e., high levels of centrality), may serve as targets for the 
development  of  prevention  and  intervention  strategies. At 
the same time, criticism has been expressed on the network 
approach, mainly focused on the stability of centrality indi-
ces and its suitability for psychological constructs (Bring-
mann  et  al.,  2019,  Neal  &  Neal,  2021).  Nevertheless,  the 
network  approach  provides  an  interesting  new  avenue  for 
the investigation of the structure of wellbeing.

There are three studies using networks to investigate the 
underlying structure of wellbeing. Giuntoli and Vidotto esti-
mated a network including measures of both SWB and PWB 
in an Italian adult sample (N = 2392) (Giuntoli & Vidotto, 
2021).  The  authors  conclude  that  the  final  estimated  net-
work was most in line with Diener’s wellbeing definition, 
with life satisfaction, positive and negative experiences, and 
perceived  positive  functioning  as  different  but  connected 
wellbeing  domains. Van Woerkom  et  al.  (2022)  examined 
how  fluctuations  in  specific  components  of  wellbeing  are 
associated with fluctuations in other components of wellbe-
ing by estimating a longitudinal wellbeing (N = 151). Their 
analysis suggests that feeling satisfied is not just a compo-
nent of wellbeing, but also plays an active role in trigger-
ing  other  related  wellbeing  aspects  such  as  cheerfulness. 
Recently, Bjørndal et al. (2024) investigated how the items 
of the Satisfaction with Life Scale (Diener et al., 1985) are 
associated with environmental factors, such as ‘household 
crowding’  and  ‘feeling  safe  when  out  walking’.  The  net-
work showed that the items ‘my living conditions are very 
good’ and ‘I  have gotten the most important things in my 
life’ were most strongly connected to the environmental fac-
tors, e.g. ‘I have trust in the public sector’ and ‘I feel that I 
have  influence  on  the  government’. The  other  two  SWLS 
items were less connected to any of the environmental fac-
tors. All  three  of  these  network  studies  have  provided  us 
with new insights about connections between wellbeing and 
wellbeing related measures.

In line with the works by Giuntoli and Vidotto (2021) and 
Van Woerkom et al. (2022), we aimed to further explore the 
value of network theory for studying wellbeing. However, 
instead of only including wellbeing measures, we estimate 
a broad network that includes different wellbeing measures 
(subjective  happiness,  satisfaction  with  life,  quality  of 
life, and flourishing), as well as the broader WBS depres-
sive  symptoms  (Achenbach  System  of  Empirically  Based 
Assessment),  neuroticism  (NEO  Five  Factor  Inventory), 
self-rated  health,  and  loneliness.  By  estimating  a  broad 
WBS  network,  we  aim  to  get  better  insight  into  wellbe-
ing  in  terms  of  how  clearly  delineated  or  interconnected 
wellbeing items from different domains are. Our study was 
conducted  in  a  sample  of  Dutch  adults.  The  network  was 
estimated  using  the  Mixed  Graphical  Models  method  and 

Current Psychology (2024) 43:27365–273761 327367

The  Subjective  Happiness  Scale  (Lyubomirsky  &  Lep-
per, 1999). Four items were rated on a Likert scale from 
1 (strongly disagree) to 7 (strongly agree). An example 
of an item is: “On the whole, I am a happy person”. We 
recoded  the  items  so  that  for  all  items,  a  higher  score 
meant higher levels of happiness.

The Satisfaction with Life Scale (Diener et al., 1985). Five 
items were rated on a Likert scale from 1 (strongly dis-
agree) to 7 (strongly agree). An example of an item is: 
‘My living conditions are excellent’.

Cantril’s ladder (Cantril, 1965) was used to assess Quality 
of  Life  (QoL).  Participants  were  asked  ‘Where  on  the 
scale would you put your life in general?’, with 0 rep-
resenting the worst possible life and 10 representing the 
best possible life.

The Short Flourishing Scale (Diener et al., 2010). The scale 
contains 8 items that are rated from 1 to 7 using a Likert 
scale. 1 resembles ‘strongly disagree’ and 7 resembles 
‘strongly agree’. An example of an item is: ‘I am com-
petent and capable in the activities that are important to 
me’.

Depressive  symptoms.  The  depressive  problems  subscale 
from the adult self-report (ASR) of The Achenbach Sys-
tem  of  Empirically  Based  Assessment  (ASEBA)  was 
used to assess depressive symptoms (Rescorla & Achen-
bach,  2004).  14  items  were  rated  from  0  to  2  (0 = not 
true,  1 = somewhat  true,  2 = very  true). An  example  of 
an item is: ‘I feel worthless or inferior’.

Loneliness. The three items from the short scale for assess-
ing  loneliness  in  large  epidemiological  studies  were 
used to assess loneliness (Hughes et al., 2004). For each 
item, participants indicated how often they identify with 
a  statement,  rated  as:  0 = almost  never,  1 = sometimes, 
or 2 = often. An example of a statement is: ‘How often 
do you feel isolated from others?’.

Neuroticism.  The  NEO-FFI  (NEO  Five  Factor  Inventory) 
neuroticism  subscale  was  used  to  assess  neuroticism 
(Costa  &  McCrae,  2008).  The  subscale  consists  of  12 
items, and each item was rated on a 5-point scale from 
1 (strongly disagree) to 5 (strongly agree). An example 
of an item is ‘I often feel tense and jittery’. Half of the 
items were reverse-coded so that a higher score indicat-
ed higher levels of neuroticism.

Self-rated health. A single item was used to evaluate self-
rated health: ‘How would you rate your general health?’ 
(Eriksson et al., 2001). This item was rated on a 5-point 
scale ranging from ‘Bad’ to ‘Excellent’.

least  absolute  shrinkage  and  selection  operator  (LASSO) 
regularization  to  limit  the  number  of  spurious  edges.  Our 
study aims to investigate how network theory can enhance 
our understanding of the complex architecture of wellbeing. 
We  conclude  the  study  by  considering  the  added  value  of 
network science as a method for answering questions about 
the nature of wellbeing.

Method

Sample

Study participants are voluntarily registered with the Neth-
erlands  Twin  Register  (NTR)  (Ligthart  et  al.,  2019).  The 
NTR was established by the Department of Biological Psy-
chology,  Vrije  Universiteit  Amsterdam,  and  collects  data 
in  children  (Young  NTR, YNTR)  and  adults  (Adult  NTR, 
ANTR).  For  this  paper  we  included  participants  from  the 
ANTR. Every two/three years, ANTR participants are asked 
to  fill  out  a  survey  about  their  personality,  psychopathol-
ogy,  wellbeing  and  lifestyle.  Written  informed  consent 
was  obtained  from  all  individual  participants  included  in 
the study. Participants in the ANTR generally have a high 
social-economic status and are of Western-European decent. 
For the current project we used four waves: (1) the 8th wave 
of data collection, collected from 2008 to 2010, (2) the 10th 
wave, collected from 2012 to 2014, (3) the 13th wave, col-
lected  in  2017–2018,  (4)  and  the  14th  wave,  collected  in 
2019- February 2020. These waves were selected based on 
availability  of  relevant  wellbeing  variables.  Participants 
were  included  if  they  participated  in  at  least  one  of  these 
surveys. If data on multiple time-points were available, we 
selected the most recent time-point.

Since the NTR collects data in multiples and their fam-
ily  members,  many  individuals  are  genetically  related  to 
each  other,  meaning  that  the  observations  are  not  entirely 
independent. To prevent bias due to these dependencies, we 
selected two samples so that within each sample, all indi-
viduals were genetically unrelated to each other. These sam-
ples were used as a trimming sample (to check for potential 
redundant nodes) and an estimation sample (to estimate the 
network)  (see  Fig.  1).  The  samples  included  only  partici-
pants that had complete data available for all the traits. In 
total, the trimming sample included 1343 individuals (63% 
females, Mage = 53.18, SDage = 9.45). The estimation sam-
ple included 726 participants (75% females, Mage = 45.27, 
SDage = 11.12).

Measures

The following standardized instruments were used:

Current Psychology (2024) 43:27365–273761 327368

Fig. 1  Overview of the analysis 
plan

Statistical analyses

Network analysis

An  overview  of  the  different  steps  of  the  analysis  plan  is 
depicted in Fig. 1.

Item selection

Before  estimating  networks,  we  examined  the  item  distri-
butions. We  excluded  ordinal  variables  having  less  than  2 
observations for any of the observed response categories as 
advised by (Epskamp et al., 2018).

To estimate the most parsimonious network in the esti-
mation  sample,  we  used  the  trimming  sample  to  examine 
item  redundancy  (i.e.,  items  that  are  not  essential  to  the 
network since they correlate highly with other items). The 
goldbricker  function  implemented  in  the  networktools  R 

package  (Jones,  2017)  was  used  to  assess  potential  item 
redundancy.  The  function  operates  by  identifying  pairs 
of  items  that  are  highly  correlated  and  then  flags  those  as 
redundant. With this function, strongly correlated item pairs 
(r ≥ .7) with less than 50% unique combinations with other 
items (i.e. less than 50% of significantly different correla-
tions with other nodes, p = .05) were identified. We opted for 
the slightly strict 50% unique combinations criteria because 
we expected many items to correlate. Next, the net_reduce 
function was used to choose the more unique node of each 
redundant pair and remove the redundant one. Based on the 
network trimming in the trimming sample, we estimated the 
network without redundant nodes in the estimation sample.

Regularized network estimation

We estimated the WBS network using the estimation sam-
ple with all items that remained after the item selection and 
item  trimming  phase. We  included  sex  and  age  as  covari-
ates. The network was estimated using the bootnet package 

Current Psychology (2024) 43:27365–273761 3 
(Epskamp  et  al.,  2018),  and  visualized  using  the  qgraph 
package (Epskamp et al., 2012) in Rstudio (RStudio Team, 
2020). Since mixed variable types (continuous and ordinal) 
were included in the network, the function Mixed Graphical 
Models (MGM) was chosen as the optimal regularized esti-
mation method  for  our  data  (Haslbeck  & Waldorp,  2015). 
Least  absolute  shrinkage  and  selection  operator  (LASSO) 
regularization  with  Extended  Bayesian  Information  Crite-
rion (EBIC) model selection was applied to limit the num-
ber  of  spurious  edges.  Due  to  applying  LASSO,  only  the 
most significant partial correlations are retained, making the 
network less prone to overfitting. This method is preferred 
over  other  regularization  techniques,  because  it  can  lead 
to parameter estimates of exactly zero (Epskamp & Fried, 
2018).  To  avoid  false  positives  and  creating  a  sparse  and 
more  interpretable  network,  To  avoid  false  positives,  we 
set  the  EBIC  tuning  parameter  y  to  the  default  value  (for 
MGM) of 0.5. The network was plotted using multidimen-
sional scaling (MDS), where the distance between the nodes 
is reflective of the strength of the association between two 
nodes,  with  nodes  placed  closer  together  sharing  stronger 
associations.

Centrality and clustering

We examined the centrality index strength (the sum of abso-
lute edge weights connected to each node), which indicates 
how  strongly  a  node  is  directly  connected  to  other  nodes. 
This measure works optimally in a network with exclusively 
positive  edges  as  this  index  does  not  distinguish  between 
positive and negative edges. We, however, expected, due to 
the  WBS  structure,  positive  (wellbeing,  self-rated  health) 
as  well  as  negative  (neuroticism,  depression,  loneliness) 
edges.  In  case  of  a  node  with  both  negative  and  positive 
edges,  expected  influence  (EI)  is  a  preferable  measure 
over strength (Robinaugh et al., 2016). Therefore, we also 
estimated the EI of the nodes (Robinaugh et al., 2016). EI 
assesses a node’s influence while accounting for both nega-
tive and positive edges. Nodes with higher EI would play 
a bigger role in the etiology of wellbeing. For example, if 
the expected influence of the node “On the whole, I am a 
happy person” is higher than of the node “How would you 
rate your general health”, then the first node would be inter-
preted as a more important factor in overall wellbeing than 
the second node.

To  examine  the  network  as  a  whole,  we  estimated  the 
global  clustering  coefficient  and  local  clustering  coeffi-
cients of the network. The global clustering coefficient (i.e. 
transitivity) is an estimate for how often a node’s neighbour-
ing  nodes  are  also  connected  to  each  other  (Costantini  et 
al., 2019). It can range between 0 and 1, with values closer 
to  1  indicating  a  highly  connected  and  clustered  network 

27369

structure,  while  values  closer  to  0  indicating  that  the  net-
work  is  comprised  of  numerous  weak  ties. A  highly  con-
nected network suggests a strong local interconnectedness 
between  the  variables,  while  a  weakly  connected  network 
suggests a branched or hierarchical structure. For example, 
a highly connected wellbeing network would imply that all 
the wellbeing items strongly influence each other. Next, we 
calculated local clustering coefficients (as implemented in 
the qgraph R package) using Zhang & Horvath’s weighted 
clustering coefficient (Zhang & Horvath, 2005). The coef-
ficient  indicates  the  likelihood  that  a  node’s  neighbour-
ing nodes (i.e. the nodes that are connected to a particular 
node) are also connected. A local clustering coefficient of 1 
indicates that the node is at the centre of a fully interlinked 
cluster. This suggests the presence of tightly knit subgroups 
within the network. Contrarily, a coefficient of 0 indicates 
that a node’s neighbouring nodes are not connected at all, 
indicating a more sparse structure around the node.

Edge-weight accuracy

Lastly, we examined how accurately we estimated the edge-
weighs in our network. Assessing the edge-weight accuracy 
is  important  because  the  validity  of  a  number  of  network 
indices (e.g. EI) is based on the edge-weights. In addition, 
the  edges  are  used  for  the  clustering  indices  (e.g.  global 
clustering coefficient) and therefore the accuracy is an indi-
cator  of  the  reliability  of  these  indices.  This  analysis  was 
done by using the non-parametric bootstrapping in bootnet 
(Epskamp et al., 2018). Using this method, observations are 
resampled with replacement to create new plausible datas-
ets  where  the  edge-weights  can  be  re-estimated  in.  Based 
on 1000 bootstraps, a 95% confidence interval (CI) around 
the edge-weights was estimated. These CIs can be used to 
assess accuracy of the edge-weights, with wider CIs reflect-
ing less accurate edges.

Factor analysis

In addition to the network analysis, we also ran exploratory 
(EFA) and confirmatory factor analyses (CFA), to compare 
the wellbeing factor structure with the estimated networks. 
In the EFA, we examined the number of factors to extract 
from  the  data  using  the  “parallel”  function  in  the  psych 
package in R (Revelle, 2022). We examined how the items 
load on that number of factors using the ‘fa’ function, where 
we  used  minimum  residual  factor  extraction  and  oblimin 
rotation (i.e., allowing latent factors to correlate), since we 
expected  the  different  well-being  components  to  be  cor-
related. For the CFA, we used the network-based trimmed 
estimation  sample  to  enable  comparison  with  the  network 
analyses.  Using  the  lavaan  package  (Rosseel,  2012)  we 

Current Psychology (2024) 43:27365–273761 327370

compare the fit of three models: (1) a six factor model with 
correlated factors. This model contains one factor for each 
included construct (excluding quality of life and self-rated 
health since these were removed in the trimming stage), (2) 
a  higher-order  factor  model  where  the  six  factors  load  on 
one  second-order  “well-being  spectrum”  factor,  and  (3)  a 
higher-order factor model where the “positive” traits (satis-
faction with life, subjective happiness, and flourishing) load 
on a positive second-order factor, and all “negative” factors 
(depression, neuroticism, loneliness) load on a negative sec-
ond-order factor (where the higher-order factors are allowed 
to correlate). Detailed methods can be found in Supplemen-
tary Materials I.

Results

Sample descriptives

The sample rated their mean quality of life with a 7.89 out 
of 10 (SD = 1.11). The mean general health was 3.94 out of 
5 (SD = 0.76). The item ‘In general, I consider myself a very 
happy person’ was rated with a mean score of 5.99 out of 
7 (SD = 1.00). Sample descriptives of all the separate items 
can be found in Supplementary Materials II.

Item selection and trimming

Five  items  were  removed  because  they  did  not  meet  the 
threshold  of  at  least  two  observations  in  each  category;  a 
self-rated health item (“How would you rate your general 
health?”),  three  items  from  the  flourishing  scale  (“I  am 
engaged  and  interested  in  my  daily  activities”,  “I  actively 
contribute  to  the  happiness  and  wellbeing  of  others”,  and 
“People respect me”), and one depression item (“I deliber-
ately try to hurt or  kill myself”). After network trimming, 
four  nodes  were  identified  as  redundant,  i.e.  strongly  cor-
related with other nodes (r ≥ .7) with less than 50% unique 
combinations with other items. This way, 41 items were left 
for network estimation. More information on the redundant 
nodes can be found in Supplementary Materials I.

Network structure

The  multidimensional  scaling  (MDS)  layout  of  the  well-
being  network  is  shown  in  Fig.  2. This  graph  reveals  two 
clusters:  a  depression,  loneliness,  and  neuroticism  cluster 
reflecting the more negative aspects of the WBS, and a clus-
ter of the different wellbeing measures, reflecting the posi-
tive aspects of the WBS. Supplementary Table 1 provides 
the  partial  correlation  matrix  that  underlies  the  network 
depicted in Fig. 2 (with item descriptions in Supplementary 

Table 2). The positive and negative cluster are mostly con-
nected  through  depression  nodes  connecting  to  different 
wellbeing nodes. While loneliness and neuroticism are also 
directly connected to flourishing and satisfaction with life, 
respectively, they are mostly indirectly connected to well-
being items through depression nodes. Additionally, we see 
that items of the same questionnaire tend to cluster together. 
Unexpectedly, Sex was barely connected to any of the vari-
ables, and only to variables in the negative cluster. Age was 
not connected to any of the variables.

Centrality and clustering

Standardized  centrality  indices  for  each  item  are  depicted 
in Fig. 3. Lower, negative Z-scores indicate nodes with the 
least strength, while higher, positive Z-scores indicate nodes 
with the highest strength. The nodes that scored relatively 
high on strength were SWL3 (‘I am satisfied with my life’), 
NEU6 (‘I sometimes feel completely worthless’), DEP3 (‘I 
feel worthless or inferior’), and DEP11 (“I am unhappy, sad, 
or depressed”). This indicates that these items play the big-
gest role in the etiology of wellbeing. Also, this is line with 
the  wellbeing  theory  of  Diener  (1984)  because  it  includes 
both  cognitive  wellbeing  (SWL3)  and  affective  wellbe-
ing (NEU6, DEP3, DEP11). Sex, which was included as a 
covariate, scored the lowest, meaning that sex almost plays 
no role in wellbeing. The results for strength and expected 
influence  are  very  similar,  because  there  were  not  many 
negative edges in the network. The global clustering coeffi-
cient of the entire network was 0.32, and the local clustering 
coefficients ranged from 0 to 0.38 (Supplementary Table 3).

Edge weight accuracy

Supplementary Materials I Fig. 1 contains the bootstrapped 
CIs of the edge-weights (edge labels were left out for read-
ability)  that  were  estimated  to  examine  the  edge-weight 
accuracy. To achieve this, new bootstrap samples were cre-
ated by sampling with replacement. For each of these boot-
strap  samples  the  edge  weights  were  calculated.  The  CI’s 
were based on the distribution of edge weights from all the 
bootstrap  samples.  On  the  y-axis  are  all  edges  in  the  net-
work, and on the x-axis it shows the strength of the edge-
weights, with red dots as point estimates, the black dots the 
bootstrap means, and the grey area as 95% confidence inter-
vals. Overall, we find relatively large CIs. These CIs do not 
reflect whether or not an edge should have been set at zero, 
but rather the accuracy of the estimated edge-weights. The 
results  show  that  the  strength  of  the  edges,  and  therefore 
several  network  indices  (e.g.  EI,  global  clustering  coeffi-
cient) should be interpreted with caution.

Current Psychology (2024) 43:27365–273761 3Fig. 2  Multidimensional scaling 
layout network of the wellbeing 
spectrum. Blue lines indicate 
positive associations, red lines 
indicate negative associations. 
RV = reverse coded before the 
analyses

27371

Current Psychology (2024) 43:27365–273761 3 
27372

Fig. 3  Centrality indices of 
all nodes (see Fig. 2 for item 
descriptions)

Factor analysis

factors (see Table 1 for fit indices). Detailed results can be 
found in Supplementary Materials I.

The EFA in our trimming sample suggested a seven-factor 
solution  (variance  explained = 47%).  Within  this  solution 
(see Supplementary Table 4), items from three scales loaded 
exclusively on their own intended factors: neuroticism (fac-
tor 1), flourishing (factor 2), and loneliness (factor 5). Fac-
tor  3  was  a  composite  of  quality  of  life,  self-rated  health, 
SWL,  and  two  SHS  items.  Three  of  the  four  SHS  items 
additionally loaded on Factor 7. The 4th factor included 7 
depression  items,  whereas  the  6th  factor  included  3  other 
depression items and additionally, self-rated health loaded 
on this factor. In our CFA, we compared the fit of three mod-
els. We find that both the model with the single higher-order 
factor and the two higher-order factors fit the data signifi-
cantly worse than the six-factor model without higher-order 

Discussion

In the present study, we set out to study the wellbeing spec-
trum from a network perspective to get better insight into 
the construct’s internal structure. The final network suggests 
two clusters, with on the one hand the “negative” spectrum 
items of depression, loneliness, and neuroticism, and on the 
other hand the “positive” spectrum items from the different 
wellbeing measures.

Visual inspection of the final network in the estimation 
sample suggests the presence of two smaller networks, con-
nected through a few items. One cluster consisted of posi-
tive items for subjective happiness, satisfaction with life and 
flourishing, while the other, more negative, cluster included 

Current Psychology (2024) 43:27365–273761 3 
depressive symptoms, neuroticism, loneliness, and sex. The 
positive and negative cluster were predominantly connected 
by  edges  between  multiple  depression  items  and  multiple 
wellbeing  items,  not  by  one  or  two  “bridge  items”  (see 
Supplementary Tables 1–2). Age was not connected to other 
nodes in the network, i.e., it was independent after condi-
tioning  on  all  other  variables,  indicating  that  the  network 
structure is independent of the age of the participant. Since 
our current sample only included adults, it would be inter-
esting to repeat our current efforts in a sample of children/
adolescents or in a sample of older adults to see if age does 
affect the network in such samples.

With  respect  to  the  wellbeing  items,  we  see  that  items 
belonging to the same measurement instrument tend to clus-
ter together, but there are also several connections between 
wellbeing  items  from  different  instruments.  On  the  one 
hand,  the  clustering  of  wellbeing  items  belonging  to  the 
same measurement instrument (i.e. flourishing, satisfaction 
with life, and subjective happiness) is in line with theories 
such as Keyes’ theory on flourishing or Diener’s theory on 
SWB that distinguish different wellbeing domains such as 
cognitive  wellbeing  and  psychosocial  wellbeing  (Diener, 
1984;  Keyes,  2005).  On  the  other  hand,  it  also  becomes 
clear that all wellbeing items are highly clustered and inter-
connected, suggesting that the different domains are not as 
clearly delineated as may be claimed by different theories/
factor analytic studies. Taken together, these results are very 
similar to previous findings of high phenotypic and genetic 
correlations between WBS measures, and a genomic factor 
model where positive and negative traits loaded on separate, 
but highly correlated factors (Baselmans et al., 2019). This 
is also similar to findings by Giuntoli and Vidotto, who con-
clude  based  on  their  network  analyses  that  different  SWB 
and  flourishing  components  are  closely  related  constructs 
(Giuntoli & Vidotto, 2021). It is also in line with other stud-
ies  emphasizing  that  different  wellbeing  phenotypes  are 
highly interconnected (Bartels & Boomsma, 2009; Kim et 
al., 2016; Kokko et al., 2013).

One of the advantages of network psychometrics is the 
possibility  to  examine  nodes  in  terms  of  their  individual 
strength  in  the  network.  Four  items  scored  relatively  high 
compared  to  all  other  nodes:  SWL3  (‘I  am  satisfied  with 
my life’), NEU6 (‘I sometimes feel completely worthless’), 
DEP3  (‘I  feel  worthless  or  inferior’),  and  DEP11  (“I  am 
unhappy,  sad,  or  depressed”).  This  indicates  that  these 
nodes have stronger connections to other nodes in the net-
work. Similarly to SWL3, Van Woerkom et al. (2022) and 
Giuntoli and Vidotto (2021) identified ‘feeling satisfied’ as a 
item that strongly influences other wellbeing items. NEU6, 
DEP3, and DEP11 had not been identified as highly influen-
tial components of the wellbeing network yet, and therefore 
provide us with new insight in the structure of wellbeing. A 

27373

potential interpretation is that the most central nodes reflect 
the items that are most representative of the WBS. Examin-
ing these items in the factor analytic context, these are also 
items with high communalities compared to the rest of the 
items (see Supplementary Table 5). Thus, to get a general 
idea of an individual’s wellbeing with limited resources, one 
might benefit most from examining these items.

As any approach, the network approach has its limitations. 
A common critique is the validity of the centrality indices 
in  the  context  of  psychological  networks.  Bringmann  and 
colleagues (2019) provide three reasons for why centrality 
indices  might  not  be  suitable  for  psychological  networks. 
First, the indices were originally developed for social net-
works (where connections are direct representations of raw 
data) but these are substantially different from psychologi-
cal  networks  (where  connections  are  coefficients  derived 
from a model). Second, some indices (especially closeness 
and betweenness) have shown to be unstable in psychologi-
cal networks. This instability might occur because the cen-
trality indices are susceptible to which nodes are included 
in  the  network,  and  it  is  unknown  which  nodes  should  be 
included beforehand (Neal & Neal, 2021). Third, there has 
been  little  research  on  the  predictive  power  of  centrality 
indices in psychological networks. Whether centrality indi-
ces can thus point to clinically relevant symptoms as targets 
for intervention is not entirely clear.

Besides being subjected to these general critiques of net-
work analysis, our findings should be interpreted in the con-
text of a number of other limitations. First, we found that 
items that belong to the same questionnaire tend to cluster 
together. While this partly reflects these items successfully 
capturing a particular construct, this likely also reflects par-
ticipants  answering  questions  belonging  to  the  same  mea-
surement  instrument  more  similarly  than  questions  from 
different  instruments  as  these  items  were  presented  with 
the  same  response  format  (Weinberger  et  al.,  2006).  The 
response  format  (e.g.,  scale,  wording)  differ  across  ques-
tionnaires, potentially leading to clustering. Second, items 
in a questionnaire are often designed to load on one certain 
scale and not on another scale, e.g. through factor analysis. 
This way of designing items could be interfering with the 
actual underlying correlations between the items of different 
scales. Third, we were limited by the wellbeing items that 
were previously collected in our sample. For example, we 
did not include Ryff’s different scales or items correspond-
ing to Keyes’ social wellbeing domain. This relates to the 
boundary  specification  problem,  referring  to  the  difficulty 
of deciding which nodes should be included when estimat-
ing  a  network  (Neal  &  Neal,  2021).  Ideally,  all  possible 
nodes should be included in a network, but it is impossible 
to know the boundary of the theoretical network, and so we 
are bounded by what we have measured. Importantly, this 

Current Psychology (2024) 43:27365–273761 327374

issue is not unique to network analyses, but also applies to 
factor analytic studies. Nevertheless, in future research even 
broader wellbeing networks including items based on these 
different  theories  need  to  be  estimated.  In  addition,  future 
research  should  compare  wellbeing  networks  in  different 
ethnic and age groups, to see how the network dynamics is 
different in different populations.

Conclusions

The results described in this study support previous research 
on the WBS that links different items assessing wellbeing, 
depression, neuroticism, and loneliness to form two highly 
interconnected positive and negative clusters (Baselmans et 
al., 2019). Additionally, we identify four nodes most central 
to the network: one life satisfaction item, one neuroticism 
item, and two depression items. This suggests that to get a 
general sense of the WBS, these items would serve as the 
most informative items to evaluate. Wellbeing research with 
limited resources should therefore focus on these four items 
to get the most accurate and comprehensive understanding 
of  wellbeing.  Nevertheless,  taking  a  network  perspective 
re-affirmed  prior  research  that  demonstrates  the  complex 
interconnectivity  of  different  wellbeing  (related)  pheno-
types.  While  several  items  definitely  cluster  with  other 
items  within  the  same  construct,  the  network  results  also 
reject  the  view  of  clearly  delineated  wellbeing  domains. 
To  develop  a  more  complete picture  of  wellbeing,  includ-
ing hedonic and eudaimonic aspects in a network context, 
additional  studies  are  needed  that  include  more  wellbeing 
measures that measure these different aspects of wellbeing. 
Nevertheless, taking a network perspective re-affirmed prior 
research  that  demonstrates  the  complex  interconnectivity 
of  different  wellbeing  (related)  phenotypes. While  several 
items  definitely  cluster  with  other  items  within  the  same 
construct, the network results also reject the view of clearly 
delineated wellbeing domains. To develop a more complete 
picture  of  wellbeing,  including  hedonic  and  eudaimonic 
aspects in a network context, additional studies are needed 
that  include  more  wellbeing  measures  that  measure  these 
different aspects of wellbeing.

Supplementary 
contains 
supplementary  material  available  at  https://doi.org/10.1007/s12144-
024-06363-0.

Information  The 

version 

online 

Acknowledgements  We  would  like  to  thank  the  Netherlands  Twin 
Register participants for their contribution to this study.

Author  contributions  A.L.:  Conceptualization,  Methodology,  For-
mal analysis, Writing – Original, Writing – Review & Editing. M.P.: 
Conceptualization, Methodology, Formal analysis, Writing – Original 
Draft, Writing – Review & Editing D.P.: Writing – Review & Editing. 

M.B.: Conceptualization, Methodology, Writing – Review & Editing, 
Supervision, Funding acquisition.

Funding  This  work  is  supported  by  the  European  Research  Council 
Consolidator Grant (ERC-2017-COG 771057 WELL-BEING PI Bar-
tels), NWO-Groot [480- 15-001/674], and the Addiction programme 
of  The  Netherlands  Organisation  for  Health  Research  and  Develop-
ment (ZonMW) [31160008].

Data availability  The Netherlands Twin Register cohort data may be 
accessed through the Netherlands Twin Register repository (ntr.fgb@
vu.nl) upon approval of the data access committee.

Declarations

Ethics  approval  All  procedures  performed  in  studies  involving  hu-
man participants were in accordance with the ethical standards of the 
institutional  and/or  national  research  committee  and  with  the  1964 
Helsinki declaration and its later amendments or  comparable ethical 
standards. This article does not contain any studies with animals per-
formed by any of the authors. Ethical approval was provided by (1) 
the  Ethical  Review  Board  (VCWE)  of  the  Faculty  of  Behavior  and 
Movement Sciences of the VU University Medical Centre Amsterdam 
(VCWE-2020-083R1)  and,  (2) The  European  Research  Council  Ex-
ecutive Agency Screening Ethics Panel.

Informed consent  Written informed consent was obtained from all in-
dividual participants included in the study.

Competing interest  On behalf of all authors, the corresponding au-
thor states that there is no conflict of interest.

Open  Access    This  article  is  licensed  under  a  Creative  Commons 
Attribution  4.0  International  License,  which  permits  use,  sharing, 
adaptation,  distribution  and  reproduction  in  any  medium  or  format, 
as long as you give appropriate credit to the original author(s) and the 
source, provide a link to the Creative Commons licence, and indicate 
if changes were made. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless 
indicated otherwise in a credit line to the material. If material is not 
included in the article’s Creative Commons licence and your intended 
use is not permitted by statutory regulation or exceeds the permitted 
use,  you  will  need  to  obtain  permission  directly  from  the  copyright 
holder. To view a copy of this licence, visit http://creativecommons.
org/licenses/by/4.0/.

References

Bartels,  M.,  &  Boomsma,  D.  I.  (2009).  Born  to  be  happy?  The  eti-
ology  of  subjective  well-being.  Behavior  Genetics.  https://doi.
org/10.1007/s10519-009-9294-8

Baselmans, B. M. L., van de Weijer, M. P., Abdellaoui, A., Vink, J. M., 
Hottenga, J. J., Willemsen, G., ... Bartels, M. (2019). A genetic 
investigation  of  the  well-being  spectrum.  Behavior  Genetics. 
https://doi.org/10.1007/s10519-019-09951-0

Bjørndal,  L.  D.,  Ebrahimi,  O.  V.,  Lan,  O.,  Nes,  R.  B.,  &  Røysamb, 
E. (2024). Mental health and environmental factors in adults: A 
population-based network analysis. The American Psychologist, 
79(3), 368–383. https://doi.org/10.1037/amp0001208

Borgatti,  S.  P.,  &  Halgin,  D.  S.  (2011).  On  network  theory.  Orga-
nization  Science,  22(5),  1168–1181.  https://doi.org/10.1287/
orsc.1100.0641

Current Psychology (2024) 43:27365–273761 3Bringmann, L. F., Elmer, T., Epskamp, S., Krause, R. W., Schoch, D., 
Wichers, M., ... Snippe, E. (2019). What do centrality measures 
measure  in  psychological  networks?  Journal  of  Abnormal  Psy-
chology, 128(8), 892–903. https://doi.org/10.1037/abn0000446
Cantril, H. (1965). The pattern of human concerns. Rutgers University 

Press.

Costa, P. T. Jr, & McCrae, R. R. (2008). The Revised NEO Personal-
ity Inventory (NEO-PI-R). In The SAGE handbook of personality 
theory and assessment, Vol 2: Personality measurement and test-
ing (pp. 179–198). Thousand Oaks, CA, US: Sage Publications, 
Inc. https://doi.org/10.4135/9781849200479.n9

Costantini, G., Richetin, J., Preti, E., Casini, E., Epskamp, S., & Peru-
gini, M. (2019). Stability and variability of personality networks. 
A  tutorial  on  recent  developments  in  network  psychometrics. 
Personality  and  Individual  Differences,  136,  68–78.  https://doi.
org/10.1016/j.paid.2017.06.011

Diener,  E.  (1984).  Subjective  well-being.  Psychological  Bulletin, 
95(3), 542–575. https://doi.org/10.1037/0033-2909.95.3.542
Diener,  E.,  Emmons,  R. A.,  Larsen,  R.  J.,  &  Griffin,  S.  (1985). The 
satisfaction  with  life  scale.  Journal  of  Personality  Assessment, 
49(1), 71–75. https://doi.org/10.1207/s15327752jpa4901_13
Diener, E., Wirtz, D., Tov, W., Kim-Prieto, C., Choi, D., Oishi, S., & 
Biswas-Diener, R. (2010). New well-being measures: Short scales 
to  assess  flourishing  and  positive  and  negative  feelings.  Social 
Indicators  Research,  97(2),  143–156.  https://doi.org/10.1007/
s11205-009-9493-y

Epskamp,  S.,  &  Fried,  E.  I.  (2018). A  tutorial  on  regularized  partial 
correlation networks. Psychological Methods 23, no. 4 (Decem-
ber 2018): 617–34. https://doi.org/10.1037/met0000167

Epskamp, S., Cramer, A., Waldorp, L., Schmittmann, V., & Borsboom, 
D.  (2012).  qgraph:  Network  visualizations  of  relationships  in 
psychometric data. Journal of Statistical Software, 48. https://doi.
org/10.18637/jss.v048.i04

Epskamp,  S.,  Borsboom,  D.,  &  Fried,  E.  I.  (2018).  Estimating  psy-
chological networks and their accuracy: A tutorial paper. Behav-
ior  Research  Methods,  50(1),  195–212.  https://doi.org/10.3758/
s13428-017-0862-1

Eriksson,  I.,  Undén, A.  L.,  &  Elofsson,  S.  (2001).  Self-rated  health. 
Comparisons  between  three  different  measures.  Results  from  a 
population study. International Journal of Epidemiology, 30(2), 
326–333. https://doi.org/10.1093/ije/30.2.326

  Giuntoli,  L.,  & Vidotto,  G.  (2021).  Exploring  diener’s  multidimen-
sional conceptualization of well-being through network psycho-
metrics.  Psychological  Reports,  124(2),  896–919.  https://doi.
org/10.1177/0033294120916864 

Fried,  E.  I.,  van  Borkulo,  C.  D.,  Cramer,  A.  O.  J.,  Boschloo,  L., 
Schoevers, R. A.,  & Borsboom, D. (2017).  Mental disorders as 
networks  of  problems: A  review  of  recent  insights.  Social  Psy-
chiatry  and  Psychiatric  Epidemiology,  52(1),  1–10.  https://doi.
org/10.1007/s00127-016-1319-z

Haslbeck, J. M. B., & Waldorp, L. J. (2015). Structure estimation for 
mixed graphical models in high-dimensional data. arXiv. https://
doi.org/10.48550/arXiv.1510.05677

Hughes, M. E., Waite, L. J., Hawkley, L. C., & Cacioppo, J. T. (2004). 
A short scale for measuring loneliness in large surveys: Results 
from  two  population-based  studies.  Research  on  Aging,  26(6), 
655–672. https://doi.org/10.1177/0164027504268574

Intelisano, S., Krasko, J., & Luhmann, M. (2020). Integrating philo-
sophical  and  psychological  accounts  of  happiness  and  well-
being. Journal of Happiness Studies, 21(1), 161–200. https://doi.
org/10.1007/s10902-019-00078-x

Jones, P. (2017). networktools: Assorted tools for identifying important 
nodes  in  networks.  R  Package  Version  1.0.0.  https://CRAN.R-
project.org/package=networktools

Kan,  K.  J.,  de  Jonge,  H.,  van  der  Maas,  H.  L.  J.,  Levine,  S.  Z.,  & 
Epskamp,  S.  (2020).  How  to  compare  psychometric  factor  and 

27375

network  models.  Journal  of  Intelligence,  8(4),  35.  https://doi.
org/10.3390/jintelligence8040035

Keyes,  C.  L.  M.  (1998).  —Social  Well-Being.  Social  Psychology 
Quarterly, 121–140.| PDF| Well Being| Correlation And Depen-
dence. (n.d.). Retrieved 28 September 2023, from Scribd website: 
https://www.scribd.com/document/191073958/Keyes-C-L-M-
1998-Social-well-being-Social-psychology-quarterly-121-140
Keyes, C. L. M. (2005). Mental illness and/or mental health? Investi-
gating axioms of the complete state model of health. Journal of 
Consulting and Clinical Psychology, 73(3), 539–548. https://doi.
org/10.1037/0022-006X.73.3.539

Kim, K., Lehning, A. J., & Sacco, P. (2016). Assessing the factor struc-
ture  of  well-being  in  older  adults:  Findings  from  the  National 
Health and Aging trends Study. Aging & Mental Health, 20(8), 
814–822. https://doi.org/10.1080/13607863.2015.1037245
Kokko, K., Korkalainen, A., Lyyra, A. L., & Feldt, T. (2013). Structure 
and  continuity  of  well-being  in  Mid-adulthood:  A  longitudinal 
study.  Journal  of  Happiness  Studies,  14(1),  99–114.  https://doi.
org/10.1007/s10902-011-9318-y

Ligthart, L., van Beijsterveldt, C. E. M., Kevenaar, S. T., de Zeeuw, 
E. L., van Bergen, E., Bruins, S., ... Boomsma, D. I. (2019). The 
Netherlands  twin  register:  Longitudinal  research  based  on  twin 
and  twin-family  designs.  Twin  Research  and  Human  Genetics, 
22(6), 623–636. https://doi.org/10.1017/thg.2019.93

Linton,  M.  J.,  Dieppe,  P.,  &  Medina-Lara, A.  (2016).  Review  of  99 
self-report measures for assessing well-being in adults: Exploring 
dimensions  of  well-being  and  developments  over  time.  British 
Medical  Journal  Open,  6(7),  e010641.  https://doi.org/10.1136/
bmjopen-2015-010641

Lyubomirsky,  S.,  &  Lepper,  H.  S.  (1999).  A  measure  of  subjective 
happiness: Preliminary reliability and construct validation. Social 
Indicators  Research,  46(2),  137–155.  https://doi.org/10.102
3/A:1006824100041

Mitchell,  P.,  &  Alexandrova,  A.  (2021).  Well-being  and  pluralism. 
Journal of Happiness Studies 22, no. 6 (August 1, 2021): 2411–
33. https://doi.org/10.1007/s10902-020-00323-8

Neal, Z. P., & Neal, J. W. (2021). Out of bounds? The boundary speci-
fication  problem  for  centrality  in  psychological  networks.  Psy-
chological  Methods,  28(1),  179–188.  https://doi.org/10.1037/
met0000426

Rescorla, L. A., & Achenbach, T. M. (2004). The Achenbach System 
of  Empirically  Based  Assessment  (ASEBA)  for  ages  18  to  90 
years. In The use of psychological testing for treatment planning 
and outcomes assessment: Instruments for adults, Volume 3, 3rd 
ed (pp. 115–152). Lawrence Erlbaum Associates Publishers.
Revelle,  W.  (2022).  psych:  Procedures  for  psychological,  psycho-
metric, and personality research (2.2.9 ed.) [Computer software 
manual]. psych. (R package version 2.2.9).

Robinaugh,  D.  J.,  Millner, A.  J.,  &  McNally,  R.  J.  (2016).  Identify-
ing  highly  influential  nodes  in  the  complicated  grief  network. 
Journal  of  Abnormal  Psychology,  125(6),  747–757.  https://doi.
org/10.1037/abn0000181

Rosseel,  Y.  (2012).  lavaan:  An  R  Package  for  Structural  Equation 
Modeling.  Journal  of  Statistical  Software,  48(2),  1–36.  https://
doi.org/10.18637/jss.v048.i02

RStudio  Team.  (2020).  RStudio:  Integrated  Development  for  R. 

https://www.rstudio.com/

Ryan,  R.  M.,  &  Deci,  E.  L.  (2000).  Self-determination  theory  and 
the  facilitation  of  intrinsic  motivation,  social  development,  and 
well-being.  American  Psychologist,  55(1),  68–78.  https://doi.
org/10.1037/0003-066X.55.1.68

Ryff,  C.  D.  (1989).  Happiness  is  everything,  or  is  it?  Explorations 
on  the  meaning  of  psychological  well-being.  Journal  of  Per-
sonality  and  Social  Psychology,  57(6),  1069–1081.  https://doi.
org/10.1037/0022-3514.57.6.1069

Current Psychology (2024) 43:27365–273761 327376

Thorsteinsen, K., & Vittersø, J. (2020). Now you see it, now you don’t: 
Solid  and  subtle  differences  between  Hedonic  and  Eudaimonic 
wellbeing. The Journal of Positive Psychology, 15(4), 519–530. 
https://doi.org/10.1080/17439760.2019.1639794

van Woerkom, M., Constantin, M., Janssens, M., Reijnders, J., Jacobs, 
N., & Lataster, J. (2022). Networks of happiness: Applying a net-
work approach to well-being in the general population. Journal 
of Happiness Studies, 23(7), 3215–3231. https://doi.org/10.1007/
s10902-022-00546-x

Weinberger, A., Darkes, J., Boca, F. D., Greenbaum, P., & Goldman, 
M. (2006). Items as context: Effects of item order and ambiguity 

on factor structure. Basic and Applied Social Psychology, 28(1), 
17–26. https://doi.org/10.1207/s15324834basp2801_2

Zhang, B., & Horvath, S. (2005). A general framework for weighted 
gene  co-expression  network  analysis.  Statistical  Applications 
in  Genetics  and  Molecular  Biology,  4,  Article17.  https://doi.
org/10.2202/1544-6115.1128

Publisher’s Note  Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.

Current Psychology (2024) 43:27365–273761 3
