# Casanova_2023_Effects of physical activity and sedentary time on depression, anxiety and well-being a bidirectional Mendelian randomisation study.

Casanova et al. BMC Medicine          (2023) 21:501  
https://doi.org/10.1186/s12916-023-03211-z

RESEARCH ARTICLE

BMC Medicine

Open Access

Effects of physical activity and sedentary 
time on depression, anxiety and well-being: 
a bidirectional Mendelian randomisation study
Francesco Casanova1, Jessica O’Loughlin1, Vasilis Karageorgiou1, Robin N. Beaumont1, Jack Bowden1, 
Andrew R. Wood1 and Jessica Tyrrell1* 

Abstract 
Background  Mental health conditions represent one of the major groups of non-transmissible diseases. Physical 
activity (PA) and sedentary time (ST) have been shown to affect mental health outcomes in opposite directions. In 
this study, we use accelerometery-derived measures of PA and ST from the UK Biobank (UKB) and depression, anxi-
ety and well-being data from the UKB mental health questionnaire as well as published summary statistics to explore 
the causal associations between these phenotypes.

Methods  We used MRlap to test if objectively measured PA and ST associate with mental health outcomes using 
UKB data and summary statistics from published genome-wide association studies. We also tested for bidirectional 
associations. We performed sex stratified as well as sensitivity analyses.

Results  Genetically instrumented higher PA was associated with lower odds of depression (OR = 0.92; 95% CI: 0.88, 
0.97) and depression severity (beta =  − 0.11; 95% CI: − 0.18, − 0.04), Genetically instrumented higher ST was associ-
ated higher odds of anxiety (OR = 2.59; 95% CI: 1.10, 4.60). PA was associated with higher well-being (beta = 0.11, 
95% CI: 0.04; 0.18) and ST with lower well-being (beta =  − 0.18; 95% CI: − 0.32, − 0.03). Similar findings were observed 
when stratifying by sex. There was evidence for a bidirectional relationship, with higher genetic liability to depres-
sion associated with lower PA (beta =  − 0.25, 95% CI: − 0.42; − 0.08) and higher well-being associated with higher PA 
(beta = 0.15; 95% CI: 0.05, 0.25).

Conclusions  We have demonstrated the bidirectional effects of both PA and ST on a range of mental health out-
comes using objectively measured predictors and MR methods for causal inference. Our findings support a causal role 
for PA and ST in the development of mental health problems and in affecting well-being.

Keywords  Mental health, Well-being, Physical activity, Mendelian randomisation

*Correspondence:
Jessica Tyrrell
j.tyrrell@exeter.ac.uk
1 Genetics of Complex Traits, Department of Biomedical & Clinical 
Science, University of Exeter Medical School, Exeter, UK

Background
Mental  health  conditions  are  a  significant  contributor 
to  the  burden  of  non-transmissible  diseases  worldwide. 
They pose a significant challenge to patients and health-
care  systems,  with  a  considerable  impact  on  the  global 
economy,  costing  trillions  of  dollars  per  year  [1].  In 
1946, the World Health Organisation (WHO) re-defined 
“health”  as  a  state  of  complete  physical,  mental,  and 
social well-being and not merely the absence of disease or 

© The Author(s) 2023. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which 
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory 
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this 
licence, visit http://creativecommons.org/licenses/by/4.0/. The Creative Commons Public Domain Dedication waiver (http://creativecom-
mons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.

  
Casanova et al. BMC Medicine          (2023) 21:501 

Page 2 of 13

infirmity. The concept of health is, therefore, extended to 
quality of life with emphasis on a person’s mental health 
and  general  well-being.  Understanding  factors  that  con-
tribute  to  poorer  mental  health  and  lower  well-being  is 
crucial  to  ensure  appropriate  public  health  prevention 
strategies and messaging.

Higher levels of physical activity (PA) have been found 
to  be  associated  with  improved  mental  health  and  well-
being [2–7] whilst sedentary time (ST) increases the risk 
of depression and anxiety [8, 9] and contributes to lower 
emotional  well-being  [10,  11].  ST,  defined  as  time  spent 
performing  activities  of  less  than  1.5  metabolic  equiva-
lent units such as sitting or lying down while awake [12], 
has  received  increasing  attention  in  recent  years  as  an 
independent  predictive  risk  factor  for  disease  [13–15] 
and  it  is  believed  to  be  conceptually  different  from  low 
PA [16].

Most  evidence  for  the  effects  of  PA  and  ST  on  men-
tal  health  and  well-being  comes  from  small  to  medium 
size  exercise  intervention  trials  or  observational  studies 
that suffer from potential unmeasured biases, even when 
well-designed. Randomised control trials (RCTs) are the 
gold  standard  for  exploring  causality.  However,  large-
scale  RCTs  cannot  always  be  performed  because  they 
can  be  costly,  impractical,  or  even  unethical  [17].  Men-
delian  randomisation  (MR)  is  a  genetic  approach  that 
is  similar  to  RCTs  in  terms  of  study  design.  It  is  exten-
sively described elsewhere [17]; briefly, it utilises the ran-
dom distribution of alleles at birth [17] to infer causality. 
MR  uses  genetic  variants  as  instrumental  variables  for 
modifiable risk factors that affect population health. The 
method  can  overcome  some  of  the  limitations  of  con-
ventional  observational  studies  including  confounding 
and reverse causation [18]. A recent MR study in the UK 
Biobank  (UKB)  utilised  genetic  variants  that  were  asso-
ciated  with  accelerometery-derived  PA  to  infer  a  causal 
relationship  between  PA  and  depression  [19]  but  pro-
vided  no  evidence  of  a  causal  association  of  depression 
on PA (i.e. no bidirectionality). Exploring bidirectionality 
is important to tease apart the relationships between PA, 
ST and mental health and well-being [20].

To  the  best  of  our  knowledge,  no  MR  studies  have 
investigated the association between PA and other men-
tal  health  phenotypes  such  as  anxiety  and  well-being. 
Similarly,  no  previous  MR  study  has  investigated  the 
association between ST and mental health and well-being 
outcomes.  Until  recently  there  was  no  suitable  ST  data-
set for MR. Using a machine learning algorithm Doherty 
et al. [21] analysed accelerometery data in approximately 
100,000  participants  from  UKB  and  classified  activity 
into overall PA, sleep and ST. These data allow us to con-
sider  objectively  measured  ST,  as  well  as  PA,  and  men-
tal  health  outcomes  using  MR  techniques  providing  the 

advantage  of  homogeneity  in  data  collection  and  out-
come  definitions,  as  well  as  the  ability  to  explore  casual 
associations at the population level.

In this study, we used MR to investigate the effects the 
accelerometery-derived measures of PA and ST from the 
UKB as exposures and data from the UKB mental health 
questionnaire  (MHQ)  as  well  as  published  GWAS  of 
depression, anxiety and well-being as outcomes [22–24]. 
We accounted for several potential sources of bias, tested 
for  bidirectional  associations  (i.e.  mental  health  is  caus-
ally associated with PA and ST), and performed sex-strat-
ified  analyses  due  to  the  different  incidence  of  mental 
health problems between males and females [25].

Methods
Population

We  used  451,025  individuals  of  European  ancestry 
(defined  through  principal  component  analyses  [26]) 
from  the  UKB  study  [27].  UKB  recruited  over  500,000 
individuals  and  collected  detailed  information  from 
all  participants,  via  questionnaires, 
interviews  and 
measurements.

Exposures and outcomes
Physical activity (PA) and sedentary time (ST)

In  UKB  PA  was  objectively  measured  using  accelerom-
etery  data  in  95,776  European  individuals.  We  derived 
overall  PA  as  described  by  Doherty  et  al.  [21],  we  used 
the mean average vector magnitude for each 30-s epoch 
over the 7 days wear time.

We  derived  ST  from  accelerometery  data  using  a 
machine  learning  algorithm  (https:// github. com/ activ 
as 
ityMo nitor ing/ bioba nkAcc elero meter Analy sis) 
described  elsewhere  [21,  28].  Briefly,  for  every  non-
overlapping  30-s  time  window,  the  algorithm  extracts 
126-dimensional  feature  vectors  representing  a  range  of 
time  and  frequency  domain  features.  These  vectors  are 
then used to classify activities in each 30-s window into 
sedentary (used here to perform the ST GWAS analysis) 
and other activities (not used here) using a random for-
est nonparametric discrimination model. The predictions 
are then smoothed using a hidden Markov model.

Genetic associations for inverse-normalised PA and ST 
were  tested  using  a  linear  mixed  model  approach  with 
BOLT-LMM [29]. These were adjusted for age, sex, study 
centre,  and  genotyping  array.  Variants  with  imputation 
quality  (INFO) < 0.3  or  minor  allele  frequency < 1%  were 
excluded.

As  no  genome-wide  (p < 5 × E − 08)  SNPs  were  found 
for ST and only three were below this threshold for PA, 
the p-value threshold for SNPs used in our analysis was 
relaxed to 1 × E − 05 to maximise the number of SNPs in 
our  instruments.  Sensitivity  analysis  at  different  P-value 

Casanova et al. BMC Medicine          (2023) 21:501 

Page 3 of 13

thresholds  was  also  performed  (see  below).  To  obtain 
independent  SNPs  to  use  as  genetic  instruments  in  the 
MR analyses, the full summary statistics from the GWAS 
analyses were clumped using a distance of 1 Mb and an 
 R2 threshold of 0.001 (Additional file 1: Table S1 and S2).

Depression, anxiety and well‑being

For  mental  health  metrics,  we  first  focused  on  using 
published  summary  statistics  from  the  largest  avail-
able GWAS as genetic instruments and we then used the 
mental health questionnaire (MHQ) data in UK Biobank, 
to enable sex-specific analyses.

Firstly,  we  used  genome-wide  significant  SNPs  from 
published  mental  health  GWAS  [22–24]  as  instruments 
for  the  exposures  (Additional  file  1:  Tables  S3–5).  For 
depression, we used summary statistics from the Psychi-
atric  Genomic  Consortium  (PGC)  [22]  (n = 1,306,354; 
414,055  cases),  excluding  23andMe  (these  data  are  not 
shared  by  PGC  because  of  transfer  agreement  restric-
tions; Additional file 1: Table S3). We did not have access 
to  summary  statistics  from  the  most  recent  depression 
GWAS [30].

For anxiety, we also used PGC summary statistics [23] 
(n = 21,761;  7016  cases;  Additional  file  1:  Table  S4).  For 
well-being, we used summary statistics from Okbay et al. 
[24]  which  measured  subjective  well-being  as  life  satis-
faction, and positive affect in 298,420 individuals (Addi-
tional file 1: Table S5).

Secondly, we derived the mental health outcomes from 
the UKB MHQ. A total of 145,668 individuals completed 
the  MHQ  and  we  derived  depression,  anxiety  and  well-
being  using  freely  available  R  code  (https:// data. mende 
ley. com/ datas ets/ kv677 c2th4/3),  as  described  elsewhere 
[31].  More  information  on  the  mental  health  variables 
derived  is  briefly  below  and  in  the  supplement  (Addi-
tional file 1: Methods).

Depression

Depression  was  assessed  using  the  Composite  Interna-
tional  Diagnostic  Interview  Short  Form  (CIDI-SF)  and 
the  Patient  Health  Questionnaire-9  (PHQ9)  question-
naires.  From  the  CIDI-SF  we  derived  a  binary  measure 
of  lifetime  major  depression  and  a  continuous  variable 
for  the  severity  of  lifetime  depression.  Using  PHQ9  we 
derived both a binary measure of current depression and 
a continuous variable for the severity of current depres-
sion [22, 30].

Anxiety

Anxiety  was  assessed  using  the  Generalised  Anxiety 
Disorder  7  (GAD-7)  item  questionnaire.  Based  on  this 
assessment,  we  derived  two  binary  anxiety  variables: 

current GAD and lifetime GAD. Additionally, we created 
a continuous variable to represent GAD severity[23].

Well‑being

A well-being score was derived from three variables that 
made up part of the MHQ [31]. Two questions assessed 
the subjective, or hedonic, aspect of well-being: “general 
happiness” (20,458) and “happiness with health” (20,459). 
The third question, taken from the WHO-Quality of Life, 
measured  the  eudaimonic,  or  psychological  aspect  of 
well-being: “belief that my life is meaningful” (20,460).

Each  of  the  three  variables  was  assessed  individually 
and  summed  to  provide  an  overall  ‘well-being  score’  for 
141,829 participants.

Analysing associations between exposures and outcomes
Observational association analysis in the UK Biobank

Linear (continuous) and logistic (binary) regression mod-
els were used to test observational associations between 
PA,  ST  and  our  mental  health  metrics.  Models  were 
adjusted  for  age  and  sex,  and  further  adjusted  for  body 
mass  index  (BMI)  and  socioeconomic  status  (Townsend 
deprivation index, TDI). Sex stratified analyses were also 
performed.

Mendelian randomisation analysis

For  our  MR  analyses,  we  used  MRlap  (https:// github. 
com/n- mouni er/ MRlap)  [32].  This  is  a  relatively  new 
method,  that  considers  a  number  of  biases  that  MR 
analyses  can  be  subject  to.  MRlap  corrects  for  weak 
instrument  bias  and  winner’s  curse,  whilst  accounting 
for sample overlap and its effect as a modifier of these 
biases.  The  authors  introduced  an  analytical  deriva-
tion of the expected value of the standard IVW causal 
effect  estimate,  assuming  a  spike-and-slab  genomic 
architecture for the exposure. The standard IVW esti-
mate is equivalent to a weighted regression of the SNP-
outcome  association  estimates  on  the  SNP-exposure 
association  estimates  constraining  the  intercept  to 
zero.  The  estimated  regression  coefficient  represents 
the standard deviation (SD) change in the outcome per 
SD change in the exposure variable, with the exception 
of binary outcomes where it represents log(odds ratio). 
The IVW causal effect expectation relies solely on the 
true  underlying  causal  effect  and  parameters  that  can 
be  estimated  from  GWAS  summary  statistics.  These 
parameters include the cross-trait LD-score intercept, 
which  is  proportionate  to  the  degree  of  sample  over-
lap,  as  well  as  the  heritability  and  polygenicity  of  the 
exposure.  Consequently,  it  becomes  feasible  to  adjust 
the IVW estimate and propose a corrected effect esti-
mate that remains robust against weak instrument bias 

 Casanova et al. BMC Medicine          (2023) 21:501 

Page 4 of 13

and winner’s curse, regardless of the degree of sample 
overlap between the exposure and outcome samples.

MRlap  calculates  a  test  statistic  to  highlight  if  the 
corrected effect estimate significantly differs from the 
IVW  observed  effect.  If  there  is  no  difference,  then 
the  IVW-MR  estimate  can  be  safely  used.  However, 
when there is a significant difference, corrected effects 
should  be  preferred  as  they  should  be  less  biased, 
independently  of  the  sample  overlap.  This  method 
relies  on  the  same  instrumental  variable  assumptions 
(relevance,  exclusion  restriction  and  independence 
assumptions)  that  IVW  and  therefore  could  be  biased 
in  the  presence  of  correlated  pleiotropy.  Moreover,  to 
be  able  to  correctly  estimate  the  genomic  architec-
ture  parameters,  the  spike-and-slab  assumption  must 
hold,  and  the  approach  does  not  work  well  for  traits 
that are not heritable or not polygenic enough. Finally, 
when  working  with  case–control  data,  the  sample 
overlap  between  the  exposure  and  the  outcome  data 
is  assumed  to  be  the  same  for  both  cases  and  con-
trols.  Detailed  information  about  the  method  and  its 
approach to adjusting for biases can be found in Mou-
nier et al. [32].

This method was appropriate for our analyses, as we 

had:

A) Sample  overlap  between  our  PA/ST  metrics  and 
mental  health,  even  when  using  the  published  sum-
mary  statistics.  For  example,  within  UK  Biobank 
there  is  a  46%  overlap  between  the  accelerometery 
and MHQ subsets of UKB;

B) Weak instruments when using PA/ST as exposures;
C) Winner’s  curse  as  our  instruments  for  PA/ST  were 

derived in the same study as our outcomes;

All MR analyses rely on several assumptions [32]:

•  The  exposure  SNPs  are  robustly  associated  with 
the relevant measured exposure. This is quantified 
by  the  F-statistic,  which  can  be  approximated  by 
the ratio of the SNP-exposure association estimate, 
β) ,  squared  (Eq.  1) 
β   and  its  standard  error,  SE(
[33].
(cid:31)

(cid:31)

2

F =

β

SE(β)

(1)

•  The  exposure  SNPs  are  not  associated  with  con-
founding  factors  that  bias  conventional  epidemio-
logical associations.

•  The  exposure  SNPs  are  only  associated  with  the 

outcome through the risk factor.

Bidirectional analyses

To test for a bidirectional relationship between PA or ST 
with  depression,  anxiety  or  well-being  we  used  MRlap, 
as  described  above,  using  the  latest  available  PGC  sum-
mary  statistics  for  depression  [22],  anxiety  [23],  subjec-
tive well-being [24] and the UKB MHQ well-being score 
as exposures and PA and ST as outcomes.

Sex stratified analysis

To  test  the  hypothesis  that  the  effects  of  PA  and  ST  on 
mental  health  differ  between  males  and  females  we  ran 
sex-specific  GWAS  for  our  mental  health  outcomes 
and  formally  compared  the  association  estimates  using 
Fisher’s z score (Eq. 2). Using Eq. 2, we also tested if the 
effects  of  depression,  anxiety  and  well-being  on  PA  and 
ST differed between males and females.

z =

(cid:31)βmale − (cid:30)βfemale

2

SE((cid:31)βmale)

+ SE((cid:30)βfemale)

2

(cid:31)

(2)

Sensitivity analysis

1.  Analysis  excluding  known  depression  and  anxiety 

loci

We  excluded  all  PA  and  ST  loci  also  known  to  be 
depression and anxiety loci, defined as reaching genome-
wide  significance 
in  the  primary  GWAS.  Depres-
sion  and  anxiety  loci  were  taken  from  the  most  recent 
GWAS studies [22, 23, 30, 34–36]. PA or ST SNPs were 
removed  from  analysis  if  the  SNP  was  in  linkage  dis-
equilibrium  (defined  as  R2 > 0.1)  with  a  depression, 
anxiety or well-being SNP in the same locus (defined as 
distance < 500  kb).  Linkage  disequilibrium  was  deter-
mined using a freely available online tool (https:// ldlink. 
nci. nih. gov/? tab= ldpair)  using  the  European  reference 
population.

2.  Analysis  using  other  MR  methods,  including  pleiot-

ropy robust methods

Four  2-sample  MR  methods  were  performed  using 
a  custom  pipeline:  inverse-variance  weighting  (IVW); 
MR-Egger;  weighted  median  (WM);  penalised  weighted 
median  (PWM).  More  details  of  these  methods  can  be 
found in Additional file 1.

3.  Analysis  using  different  p-value  thresholds  for  MR 

instrument selection

Casanova et al. BMC Medicine          (2023) 21:501 

Page 5 of 13

When an association was identified, we tested whether 
the  selection  of  PA  and  ST  instruments,  based  on  a 
p-value  threshold  of  1 × E − 05,  influenced  our  results. 
To  assess  this,  we  repeated  our  analyses  using  stricter 
p-value thresholds (5 × E − 06 and 1 × E − 06).

4.  Analysis of the PA and ST instrument using the Wray 
et  al.,  depression  summary  statistics  to  remove  bias 
due to sample overlap

We  extracted  the  genetic  variants  used  as  the  PA  and 
ST  instrument  from  the  older  Wray  et  al.,  PGC  GWAS 
of major depression that excluded UK Biobank and per-
formed  standard  2-sample  MR  including  IVW,  MR-
Egger,  WM  and  PWM. This  analysis  limits  any  bias  due 
to sample overlap.

5.  Analysis of individual MHQ questions used to create 

the well-being score

To  further  understand  how  different  dimensions  of 
well-being  affect  our  results  we  performed  an  MRlap 
analysis  of  the  individual  components  of  the  well-being 
score  (see  “Well-being”  section  above  for  details  of  the 
questions analysed).

Results
The  demographics  of  individuals  with  measured  men-
tal  health  outcomes  are  summarised  in  Table  1.  Briefly, 
depression  and  anxiety  were  more  prevalent  in  females, 
with  females  also  reporting  more  severe  symptoms.  No 
sex differences were observed for well-being.

Observational associations in UK Biobank MHQ

Observationally,  higher  PA  was  associated  with  lower 
odds  of  major  and  current  depression  as  well  as  lower 
odds  of  current  and  lifetime  GAD  (Additional  file  1: 
Table  S6).  For  example,  a  1-SD  higher  PA  was  associ-
ated  with  lower  odds  of  major  depression  (Odds  Ratio 
(OR): 0.85, 95% confidence intervals (CI): 0.83;0.86). Fur-
ther,  higher  PA  was  associated  with  higher  well-being 
scores and lower depression and anxiety severity. Further 
adjustment for BMI and TDI did not change the results 
(Additional file 1: Table S6).

Higher  ST  was  observationally  associated  with  higher 
odds  of  major  and  current  depression,  as  well  as  more 
severe depression and lower well-being (Additional file 1: 
Table S6). No association was observed between ST and 
anxiety. Further adjustment for BMI and TDI attenuated 
the association for current and lifetime.

Our MR analyses used valid instruments

The  final  SNPs  used  as  instruments  can  be  found  in 
Additional  file  1:  Tables  S1–5.  Mean  F-statistics  for 
these SNPs ranged between 17.7 and 41.2, providing evi-
dence  that  our  exposure  SNPs  were  robustly  associated 
with  the  relevant  measured  exposure.  We  summarised 
known associations of our exposure variants (Additional 
file  1:  Tables  S1–5)  and  tested  for  potential  associations 
with  potential  confounders  using  2-sample  MR. The  PA 
instrument was nominally associated with BMI and lower 
odds  of  ever  smoking,  although  not  when  using  more 
pleiotropy robust methods like MR Egger. The ST instru-
ment  was  nominally  associated  with  educational  attain-
ment. No association was noted with other confounders 
(alcohol consumption, BMI, diet, educational attainment 
and smoking).

Table 1  Basic  demographics  of  the  UK  Biobank  study  participants,  data  are  reported  as  means  (standard  deviation)  or  median 
[interquartile range]

Trait

N

Age (years)
Body mass index (kg/m2)
Townsend deprivation index

Sedentary time (hours/day)

Major depression — N cases (%)

Current depression — N cases (%)

Generalised anxiety disorder — N cases (%)

Current generalised anxiety disorder — N cases (%)

Severity of major depression

Severity of current depression

Severity of generalised anxiety disorder

Well-being score

All

145,982

56.56 (7.70)

26.78 (4.55)

 − 1.79 (2.78)

9.18 (2.35)

34,858 (23.88)

2659 (1.82)

7244 (4.96)

1854 (1.27)

3 [6]

2 [4]

0 [3]

13 [3]

Females

82,437

56.08 (7.63)

26.35 (4.88)

 − 1.75 (2.77)

8.89 (2.24)

24,022 (29.14)

1691 (2.05)

4706 (5.71)

1205 (1.46)

4 [6]

2 [4]

1 [4]

13 [3]

Males

63,545

57.19 (7.75)

27.33 (4.01)

 − 1.83 (2.80)

9.55 (2.43)

10,836 (17.05)

968 (1.52)

2536 (3.99)

649 (1.02)

0 [5]

1 [3]

0 [2]

13 [3]

 Casanova et al. BMC Medicine          (2023) 21:501 

Page 6 of 13

Genetically instrumented higher PA was associated 
with lower odds and severity of depression whilst ST 
was not associated with depression

Genetically instrumented higher PA was not associated 
with anxiety, whilst ST associated with lower odds 
of anxiety

When using the larger PGC dataset, a genetically instru-
mented  1-SD  higher  PA  was  associated  with  0.92  lower 
odds  of  major  depression  (95%  CI:  0.88;  0.97)  (Table  2 
and Fig. 1). Furthermore, a genetically instrumented 1-SD 
higher  PA  was  associated  with  lower  current  depres-
sion severity (beta =  − 0.11; 95% CI: − 0.18; − 0.04). Using 
UKB-derived mental health measures only, there was no 
evidence for an association between PA and current and 
major depression, or lifetime depression severity (Table 2 
and Fig. 1).

Genetically  instrumented  higher  ST  was  not  associ-
ated  with  either  the  PGC  summary  statistics  for  major 
depression  nor the UKB binary or continuous  measures 
of major and current depression (Table 3 and Fig. 2).

MR  provided  no  evidence  of  an  association  between 
higher genetically instrumented PA and current or life-
time  GAD  (OR:  1.11;  95%  CI:  0.84;  1.47)  (Table  2  and 
Fig.  1)  using  both  PGC  summary  statistics  and  UKB 
MHQ-derived measures. Further, there was no associa-
tion with GAD severity (Table 2 and Fig. 1).

In  contrast,  genetically 

instrumented  higher  ST 
was  associated  with  higher  odds  of  lifetime  anxiety 
(OR = 2.25;  95%  CI:  1.10;  4.60),  when  using  the  larger 
PGC  summary  statistics  (Table  3  and  Fig.  2).  Using 
UKB-derived  mental  health  measures  only,  there  was 
no association with current and lifetime GAD, or GAD 
severity (Table 3 and Fig. 2).

Table 2  Results of the 2 sample Mendelian randomisation analysis using MRLap for mental health outcome for all participants and 
stratified by sex. Results represent odds ratio or betas per standard deviation change in genetically instrumented physical activity

Exposure

  Physical activity

  Physical activity

Exposure

Outcome

PGC-Depression

PGC-Anxiety

Outcome

  Physical activity

Current depression

  Physical activity

Lifetime major depression

  Physical activity

Current anxiety disorder

  Physical activity

Lifetime anxiety disorder

Exposure

  Physical activity

Outcome

Well-being

  Physical activity

Severity of major depression

  Physical activity

Severity of current depression

  Physical activity

Severity of anxiety

  Physical activity

Subjective well-being (GWAS)

Strata

All

All

Strata

All

Females

Males

All

Females

Males

All

Females

Males

All

Females

Males

Strata

All

Females

Males

All

Females

Males

All

Females

Males

All

Females

Males

All

OR (95% CI)

0.93 (0.88; 0.97)

1.11 (0.84; 1.47)

OR (95% CI)

0.99 (0.93; 1.04)

0.99 (0.92; 1.07)

0.97 (0.89; 1.06)

1.00 (0.93; 1.08)

1.01 (0.93; 1.10)

0.99 (0.89; 1.09)

0.95 (0.88; 1.03)

0.96 (0.87; 1.06)

0.94 (0.84; 1.04)

0.99 (0.92; 1.06)

0.98 (0.89; 1.08)

0.99 (0.89; 1.09)

Beta (SE)

0.11 (0.04; 0.18)

0.12 (0.03; 0.21)

0.09 (0.01; 0.18)

 − 0.01 (− 0.09; 0.08)

 − 0.03 (− 0.12; 0.07)

0.02 (− 0.09; 0.13)

 − 0.11 (− 0.18; − 0.04)

 − 0.14 (− 0.22; − 0.05)

 − 0.08 (− 0.17; 0.01)

 − 0.03 (− 0.10; 0.04)

 − 0.08 (− 0.17; 0.01)

0.04 (− 0.06; 0.13)

 − 0.03 (− 0.18; 0.11)

P

1.58E − 03

4.75E − 01

P

5.91E − 01

8.37E − 01

4.81E − 01

9.44E − 01

7.69E − 01

8.24E − 01

1.93E − 01

4.07E − 01

2.18E − 01

7.99E − 01

6.78E − 01

7.64E − 01

P

1.41E − 03

8.32E − 03

3.40E − 02

8.68E − 01

5.92E − 01

7.18E − 01

1.60E − 03

2.18E − 03

7.67E − 02

3.65E − 01

7.09E − 02

4.29E − 01

6.74E − 01

Casanova et al. BMC Medicine          (2023) 21:501 

Page 7 of 13

Fig. 1  Forest plot of the results of the Mendelian randomisation analysis (MRlap) using genetically instrumented physical activity as exposure 
and binary (left) and continuous (right) outcome. Data represent standard deviation change in outcome per standard deviation change in exposure

Genetically instrumented higher PA and ST was associated 
with well‑being in opposite directions

A  1-SD  higher  genetically  instrumented  PA  was  associ-
ated  with  higher  a  well-being  score  (beta = 0.11,  95% 
CI: 0.04;  0.18, Table 2 and  Fig. 2), using the UKB MHQ 
derived  measures.  In  contrast,  there  was  no  association 
between  PA  and  subjective  well-being,  which  captures 
life  satisfaction  and  positive  affect,  from  the  published 
GWAS  (OR: − 0.031;  95%  CI − 0.176;  0.114,  Table  2  and 
Fig. 1).

Similarly, a 1-SD higher ST was associated with a lower 
well-being  score  (beta =  − 0.18,  95%  CI: − 0.33; − 0.04; 
Table 3 and Fig. 2) using the MHQ definition from UKB, 
but  there  was  no  association  when  analysing  subjec-
tive  well-being  from  the  published  GWAS  (Table  3  and 
Fig. 2).

There  was  no  association  between  well-being  and  ST 
when using either the published GWAS or the MHQ def-
inition from the UKB (Table 4).

Sex‑stratified analyses

There was no evidence of differences between males and 
females  in  our  sex-stratified  analyses  evidenced  using 
Fisher’s z score except when using depression as an expo-
sure and PA as an outcome, where the effect was signifi-
cantly  stronger  in  females  than  males  (Additional  file  1: 
Table S7).

Sensitivity analyses

1. Excluding known loci

Bidirectional results

A  higher  genetic  liability  to  depression  was  associated 
with  lower  PA  (beta =  − 0.25,  95%  CI: − 0.42; − 0.08; 
Table  4)  but  not  ST  (beta = 0.04,  95%C  I: − 0.11;  0.18; 
Table  4).  A  higher  genetic  liability  to  anxiety  was  not 
associated with either PA or ST (Table 4).

A genetically instrumented higher well-being using the 
published summary statistics was not associated with PA 
(beta = 0.13; 95% CI − 0.06; 0.31, Table 4). However, there 
was  an  association  when  using  the  UKB  MHQ-derived 
measures with a higher well-being score associating with 
increased PA (beta = 0.15; 95% CI 0.05; 0.25; Table 4).

We  excluded  7  SNPs  for  PA  and  1  for  ST  (Additional 
file 1: Tables S1–2). Excluding known depression, anxiety 
and well-being variants from our PA instrument slightly 
attenuated  our  findings  for  the  well-being  score  and 
severity of current depression in males (Additional file 1: 
Table  S8).  Wider  confidence  intervals  were  observed 
in  all  other  analyses.  Excluding  depression  anxiety  and 
well-being variants from our ST instrument did not sub-
stantially change our results (Additional file 1: Table S8). 
Similarly, our findings did not change when we excluded 
PA and ST loci from the depression instrument and well-
being (Additional file 1: Table S8).

2. IVW, Egger and weighted median

 Casanova et al. BMC Medicine          (2023) 21:501 

Page 8 of 13

Table 3  Results of the 2 sample Mendelian randomisation analysis using MRLap for mental health outcome for all participants and 
stratified by sex. Results represent odds ratio or betas per standard deviation change in genetically instrumented sedentary time

Exposure

  Sedentary time

  Sedentary time

Exposure

Outcome

PGC-Depression

PGC-Anxiety

Outcome

  Sedentary time

Current depression

  Sedentary time

Lifetime major depression

  Sedentary time

Current anxiety disorder

  Sedentary time

Lifetime anxiety disorder

Exposure

  Sedentary time

Outcome

Well-being

  Sedentary time

Severity of major depression

  Sedentary time

Severity of current depression

  Sedentary time

Severity of anxiety

  Sedentary time

Subjective well-being (GWAS)

Strata

All

All

Strata

All

Females

Males

All

Females

Males

All

Females

Males

All

Females

Males

Strata

All

Females

Males

All

Females

Males

All

Females

Males

All

Females

Males

All

OR (95% CI)

0.96 (0.86; 1.07)

2.25 (1.10; 4.60)

Odds ratio (95% CI)

0.95 (0.84; 1.07)

0.96 (0.82; 1.12)

0.94 (0.76; 1.16)

1.06 (0.93; 1.20)

1.08 (0.92; 1.26)

1.02 (0.85; 1.22)

0.98 (0.83; 1.15)

0.88 (0.71; 1.08)

1.13 (0.88; 1.44)

0.97 (0.83; 1.12)

0.95 (0.78; 1.17)

0.99 (0.79; 1.25)

Beta (SE)

 − 0.18 (− 0.33; − 0.04)

 − 0.14 (− 0.31; 0.03)

 − 0.23 (− 0.44; − 0.02)

0.08 (− 0.06; 0.22)

0.04 (− 0.12; 0.20)

0.14 (− 0.09; 0.37)

0.05 (− 0.08; 0.18)

0.06 (− 0.11; 0.23)

0.03 (− 0.16; 0.22)

0.004 (− 0.12; 0.13)

0.04 (− 0.12; 0.20)

 − 0.02 (− 0.22; 0.17)

0.10 (− 0.35; 0.56)

P

4.38E − 01

2.59E − 02

P

4.01E − 01

5.97E − 01

5.80E − 01

3.97E − 01

3.62E − 01

8.41E − 01

7.55E − 01

2.15E − 01

3.43E − 01

6.34E − 01

6.47E − 01

9.50E − 01

P

1.46E − 02

1.14E − 01

2.91E − 02

2.47E − 01

6.26E − 01

2.43E − 01

4.69E − 01

4.73E − 01

7.60E − 01

9.52E − 01

6.12E − 01

8.12E − 01

6.59E − 01

Results  of  the  analysis  using  IVW,  MR  Egger  and 
weighted  median  can  be  found  in  Additional  file  1: 
Tables  S9–10.  For  PA  and  ST  results  of  the  pleiotropy 
robust  methods  are  generally  in  agreement  with  the 
results  from  MRlap,  with  Egger  and  weighted  median 
analysis showing directionally consistent results.

3. Different p-value thresholds

Using p = 5E − 06 as our instrument selection thresh-
old  for  PA,  66  SNPs  remained  in  our  instrument. 
Results  for  well-being  score  and  severity  of  current 
depression  were  all  directionally  consistent  with  3  out 
6  remaining  at  P < 0.05  (Additional  file  1:  Table  S11). 
Using p = 1E − 06 as our instrument selection threshold 
for PA, 24 SNPs remained in our instrument, with 4 out 
of 6 remaining directionally consistent but none reach-
ing nominal significance at P < 0.05.

Using  p = 5E − 06  and  p = 1E − 06  as  our  instrument 
selection  threshold  for  ST,  18  and  9  SNPs  remained  in 
our  instrument,  respectively.  Results  for  the  well-being 
score  were  all  directionally  consistent  but  none  were 
nominally significant (P < 0.05).

4.  2-sample  MR  with  non-overlapping  depression 
GWAS

Using  the  PA  and  ST  instruments  identified  in  our 
MRLap analysis we provide further evidence for the role 
of  PA  in  depression  using  the  summary  statistics  from 
the  Wray  et  al.  GWAS  of  major  depression  excluding 
the  UK  Biobank  data.  Here,  a  genetically  instrumented 
SD  with  higher  PA  was  associated  with  0.82  lower  odds 
of  depression  (95%  CI:  0.74,  0.92).  Results  were  consist-
ent  with  more  pleiotropy  robust  methods  (Additional 
file 1: Table S12) and Egger MR did not provide evidence 
of horizontal pleiotropy (Pintercept = 0.63). In contrast and 

Casanova et al. BMC Medicine          (2023) 21:501 

Page 9 of 13

Fig. 2  Forest plot of the results of the Mendelian randomisation analysis (MRlap) using genetically instrumented sedentary time as exposure 
and binary (left) and continuous (right) outcome. Data represent standard deviation change in outcome per standard deviation change in exposure

Table 4  Results  of  the  2  sample  Mendelian  randomisation  analysis  using  depression,  anxiety  and  well-being  as  predictors  for  all 
participants and stratified by sex. Results represent betas per standard deviation change in genetically instrumented risk of of the exposures

Exposure

  Depression

Outcome

Overall physical activity

  Depression

Sedentary time

Exposure

  Anxiety

Outcome

Overall physical activity

  Anxiety

Sedentary time

Exposure

Outcome

  Well-being GWAS

Overall physical activity

  Well-being GWAS

Sedentary time

  Well-being from UKB

Overall physical activity

  Well-being from UKB

Sedentary time

Strata

All

Females

Males

All

Females

Males

Strata

All

Females

Males

All

Females

Males

Strata

All

Females

Males

All

Females

Males

All

Females

Males

All

Females

Males

Beta (95% CI)

 − 0.25 (− 0.42; − 0.08)

 − 0.45 (− 0.67; − 0.23)

 − 0.08 (− 0.27; 0.11)

0.04 (− 0.11; 0.18)

0.17 (− 0.03; 0.36)

 − 0.08 (− 0.28; 0.12)

Beta (95% CI)

0.00 (− 0.08; 0.08)

0.01 (− 0.10; 0.10)

 − 0.01 (-0.11; 0.10)

 − 0.02 (− 0.13; 0.08)

 − 0.04 (− 0.18; 0.09)

0.00 (− 0.13; 0.12)

Beta (95% CI)

0.13 (− 0.06; 0.31)

0.07 (− 0.17; 0.31)

0.16 (− 0.04; 0.36)

0.07 (− 0.09; 0.23)

0.05 (− 0.18; 0.28)

0.10 (− 0.10; 0.29)

0.15 (0.05; 0.25)

0.18 (0.04; 0.33)

0.12 (− 0.002; 0.24)

 − 0.02 (− 0.12; 0.09)

 − 0.05 (− 0.19; 0.09)

0.00 (− 0.12; 0.12)

P

4.07E − 03

6.05E − 05

4.21E − 01

6.33E − 01

9.32E − 02

4.13E − 01

P

9.48E − 01

8.24E − 01

8.99E − 01

9.99E − 01

5.34E − 01

9.46E − 01

P

1.68E − 01

5.71E − 01

1.21E − 01

3.87E − 01

6.54E − 01

3.27E − 01

4.65E − 03

1.33E − 02

5.40E − 02

7.14E − 01

4.75E − 01

9.87E − 01

 Casanova et al. BMC Medicine          (2023) 21:501 

Page 10 of 13

consistent  with  our  MR  lap  results  genetically  instru-
mented,  ST  did  not  predict  depression  using  the  Wray 
et al. summary statistics (Additional file 1: Table S12).

5. Individual well-being questions from MHQ

To  investigate  the  differences  in  results  between  the 
two definitions of well-being (MHQ and GWAS), we ana-
lysed  the  association  between  genetically  instrumented 
PA  and  ST  time  with  the  three  questions  that  comprise 
the  MHQ  well-being  score  in  the  UKB.  Our  findings 
showed that a 1-SD genetically instrumented higher level 
of PA was associated with higher levels of general happi-
ness in all individuals (beta: 0.09, 95% CI: 0.03;0.15) and 
in females only (beta: 0.10, 95% CI: 0.01;0.18), but there 
was no significant association with happiness with health 
or meaningful life (Additional file 1: Table S13). Similarly, 
a  1-SD  genetically  instrumented  higher  level  of  ST  was 
associated with lower levels of general happiness in males 
only  (beta: − 0.19,  95%  CI: − 0.37; − 0.01),  but  there  was 
no  significant  association  with  happiness  with  health  or 
meaningful life (Additional file 1: Table S13).

Discussion
This  MR  study  provides  evidence  of  a  causal  bidirec-
tional relationship between objectively measured PA and 
depression.  We  confirmed  previous  findings  that  higher 
genetically determined PA associated with lower odds of 
major  depression  [19]  and  provided  new  evidence  that 
higher  PA  associated  with  higher  well-being.  This  study 
also  considered  for  the  first  time  the  role  of  ST,  a  dis-
tinct phenotype from low PA [16], on mental health out-
comes using MR. Higher genetically determined ST was 
associated  with  higher  odds  of  anxiety  and  lower  well-
being,  the  latter  with  the  exception  of  the  females  only 
analysis. For the first time, we also highlight bidirectional 
causal pathways between PA and depression and PA and 
well-being.

Whilst  our  UKB  only  analysis  demonstrated  no  clear 
evidence  of  association  between  PA  and  lifetime  major 
depression status, this was likely due to a lack of power 
in  UKB  as  there  was  robust  evidence  of  an  inverse 
association  between  PA  and  lifetime  major  depression 
using  the  PGC  summary  statistics.  This  latter  result  is 
consistent  with  previous  MR  using  similar  exposure 
and  outcomes  [19]  as  well  as  with  prospective  studies 
showing  that  those  with  higher  levels  of  PA  had  lower 
odds  of  depression  [3,  6].  Our  study  goes  beyond  that 
of  Choi  and  colleagues  by  using  a  MR  method  specifi-
cally designed to account for (a) weak instrument bias, 
which occurs when instrumenting physical activity and 
(b)  sample  overlap,  an  important  source  of  potential 
bias  when  using  UKB  datasets.  We  also  demonstrated 

consistent  results  using  our  PA  and  ST  instruments  in 
the  same  depression  GWAS  as  Choi  and  colleagues, 
with  strong  inverse  relationships  between  PA  and 
depression.

Using  the  individual-level  data  in  UKB  we  also  pro-
vided evidence that PA causes lower depression severity. 
This  adds  to  previous  research  which  has  demonstrated 
that exercise programmes are associated with an amelio-
ration of depressive symptoms [37].

There  was  no  evidence  ST  was  associated  with  major 
depression,  even  when  using  the  larger  PGC  data-
set.  Future  work  should  repeat  these  analyses  using  the 
recently  published  larger  GWAS  of  major  depression 
[30],  an  analysis  we  did  not  perform  due  to  data  access 
constraints.

Our  study  found  that  higher  genetically  determined 
PA contributed to a higher well-being score, while higher 
genetically  determined  ST  contributed  to  a  lower  well-
being score, as defined by the MHQ in UKB. However, we 
did  not  observe  any  significant  association  between  PA, 
ST and well-being using the subjective well-being defini-
tion  from  the  published  GWAS  [24].  To  investigate  this 
difference  further,  we  explored  the  relationship  between 
higher levels of PA and ST with the individual questions 
that  comprise  the  UKB  well-being  score.  We  found  that 
higher  levels  of  PA  were  associated  with  higher  levels 
of  general  happiness  in  all  individuals  and  in  females 
only,  while  higher  levels  of  sedentary  time  were  associ-
ated with lower levels of general happiness in males only. 
There  was  no  significant  association  between  either  PA 
or ST and happiness with health or meaningful life. Our 
results  suggest  that  the  happiness  element  of  subjective 
well-being  is  important  in  the  relationship  between  ST, 
PA and well-being, but not the meaningful (eudaimonic) 
or life satisfaction element (cognitive hedonic). This may 
explain  the  discrepancy  between  our  UKB  results  and 
the  GWAS  definition  of  subjective  well-being. The  pub-
lished GWAS did not include questions on happiness in 
their phenotype definition, which our sensitivity analyses 
suggest is crucial in the PA/ST to well-being relationship. 
This fits with previous observational literature that shows 
increasing volumes of PA are associated with higher lev-
els  of  happiness  [38,  39].  Some  studies  have  remained 
sceptical  about  the  association  between  PA  and  happi-
ness, suggesting that the contribution of PA to happiness 
might be minor compared to other demographic and life-
style  factors,  our  study  provides  robust  causal  evidence 
for the association between PA and happiness [40].

This study also highlights the importance of ST in men-
tal  health  and  well-being.  We  add  to  the  evidence  base 
that not only is PA good for well-being, reducing ST will 
also  have  beneficial  well-being  effects  [2].  This  further 

Casanova et al. BMC Medicine          (2023) 21:501 

Page 11 of 13

highlights  that  ST  is  an  important  construct  for  health 
and well-being [14, 41].

We  provide  evidence  for  potential  causal  roles  of  ST 
in  anxiety.  Higher  genetically  determined  ST  increased 
odds of anxiety (PGC summary statistics), but these find-
ings were not consistent when using the UKB definitions 
of  anxiety,  although  lack  of  power  might  explain  this 
discrepancy.  Our  findings  are  in  agreement  with  exist-
ing evidence of an association between ST and increased 
anxiety [9, 42].

Our  bidirectional  analysis  provided  evidence  that 
higher  genetic  liability  of  depression  associated  with 
lower PA, but not with higher ST. This differs to the pre-
vious  MR  study  [19],  but  is  likely  due  to  using  a  more 
recent  depression  GWAS  as  our  instrument  [22]  than 
those  used  by  Choi  et  al.  [43].  The  finding  of  a  bidirec-
tional  causal  association  between  depression  and  PA 
suggests  a  negative  feedback  loop  where  a  genetically 
higher risk of depression causes lower PA which, in turn, 
increases the risk and severity of depression. No bidirec-
tional associations were observed for anxiety.

This study had many strengths. Firstly, we used objec-
tively  measured  PA  and  ST,  therefore  eliminating  the 
potential  effect  of  self-reported  biases.  Secondly,  we 
used  validated  definitions  of  mental  health  outcomes 
[31],  this,  unlike  results  from  meta-analysis,  gives  us 
homogeneity  of  definitions,  an  issue  that  is  particularly 
important  in  mental  health  research.  Thirdly,  we  used 
an  MR  method  accounting  for  MR  biases  such  as  sam-
ple overlap and Winner’s curse, which can all affect MR 
results [32].

We  acknowledge  several  limitations  with  our  study. 
First,  the  UKB  is  not  population  representative,  with 
over-representation  of  females  and  individuals  from 
higher  socioeconomic  groups  [44–46].  Further,  our 
work focused on UKB participants genetically similar 
to  the  1000  genome  European  ancestry,  so  our  find-
ings  might  not  be  generalisable  to  other  ancestries. 
Second,  work  by  ourselves  and  others  have  suggested 
potential participation biases in the UKB subsets [47] 
completing  the  MHQ  and  physical  activity  monitor-
ing.  However,  we  have  replicated  our  findings  using 
MDD  summary  statistics  which  do  not  include  the 
UK  Biobank,  although  we  acknowledge  this  will  not 
limit  selection  bias  in  our  PA  and  ST  metrics.  Future 
work should consider accounting for potential partici-
pation  biases  using  recently  developed  methods  [48]. 
Third, our PA metrics focus on the overall time of PA, 
there  is  evidence  that  the  intensity  of  exercise  is  also 
important  for  mental  health,  which  we  were  not  able 
to test here. Further the type of PA and ST may also be 
important  in  mental  health  and  should  be  considered 

in  more  detail.  Fourth,  we  did  not  set  any  specific 
threshold  to  account  for  multiple  testing  because  our 
mental health phenotypes are correlated, i.e. not truly 
independent  from  each  other,  and  therefore  correc-
tions  such  as  Bonferroni’s  are  too  conservative.  We, 
instead,  report  confidence  intervals  for  all  our  esti-
mates.  Fifth,  our  results  are  limited  to  the  definitions 
of mental health available and cannot be extrapolated 
to different definitions. Finally, whilst we used a range 
of methods to account for pleiotropy, there was some 
evidence  that  our  PA  instrument  predicted  lower 
BMI.  We  and  others  have  previously  demonstrated 
the  importance  of  BMI  in  predicting  depression  sta-
tus [49,  50], future work should consider and test  the 
potentially mediating effect of BMI on the PA-depres-
sion relationship.

Conclusions
In  conclusion,  we  have  highlighted  the  importance  of 
both PA and ST on a range of mental health outcomes 
using  objectively  measured  predictors  and  extensive 
MR  methods  for  causal  inference.  Our  results  are  in 
agreement  with  other  methodological  approaches 
showing the importance of maintaining a high level of 
PA and reducing ST, for example when desk working. 
We also highlight the importance of considering bidi-
rectional  relationships,  with  evidence  that  depression 
or  poor  well-being  reduces  PA.  This  is  important  for 
public health interventions and highlights the need for 
individuals with depression to be supported to under-
take  more  PA.  Our  work  can  be  added  to  the  knowl-
edge base suggesting that both PA and ST need to be 
considered to improve public health.

Abbreviations
BMI 
CIDI-SF 
GAD 
GWAS 
IVW 
MHQ 
MR 
MR-Egger 
PA 
PGC 
PHQ-9 
PWM 
RCTs 
SNPs 
ST 
TDI 
UKB 
WHO 
WM 

 Body mass index
 Composite International Diagnostic Interview Short Form
 Generalised anxiety disorder
 Genome-wide association study
 Inverse variance weighted
 Mental health questionnaire
 Mendelian randomisation
 Egger Mendelian randomisation
 Physical activity
 Psychiatric Genomic Consortium
 Patient Health Questionnaire-9
 Penalised weighted median
 Randomised control trials
 Single nucleotide polymorphisms
 Sedentary time
 Townsend deprivation index
 UK Biobank
 World Health Organisation
 Weighted median

 Casanova et al. BMC Medicine          (2023) 21:501 

Page 12 of 13

Supplementary Information
The online version contains supplementary material available at https:// doi. 
org/ 10. 1186/ s12916- 023- 03211-z.

Additional file 1. This file includes the Supplementary methods and 
Table S1-S13. Tables S1-5 provide the list of SNPs included in the PA, 
ST, depression, anxiety and wellbeing instrument respectively. Table S6 
reports observational associations between PA/ST and mental health. 
Table S7 summarises any sex differences in our effect estimates. Tables 
S8-13 represent results from a range of sensitivity analyses. Detailed 
legends for each table are present in the additional file.

Acknowledgements
The authors would like to acknowledge the use of the University of Exeter 
High-Performance Computing (HPC) facility in carrying out this work.
This research has been conducted using the UK Biobank Resource, under 
application 9072. This work uses data provided by patients and collected by the 
NHS as part of their care and support, Copyright © (2023), NHS England. Re-used 
with the permission of the NHS England [and/or UK Biobank]. All rights reserved.
This study was supported by the National Institute for Health and Care 
Research Exeter Biomedical Research Centre. The views expressed are those 
of the author(s) and not necessarily those of the NIHR or the Department of 
Health and Social Care.
The authors wish to thank the UK Biobank participants and coordinators for 
this unique dataset.

Authors’ contributions
F.C. and J.T. designed the study and wrote the manuscript. F.C., J.O., V.K., 
R.B., A.R.W., J.B., and J.T. were involved in data processing, statistical analyses 
and interpretation. J.T. is the guarantor. All authors assisted in the writing, 
reviewing and approval of the manuscript. All authors read and approved the 
manuscript.

Funding
This study was supported by the National Institute for Health and Care 
Research Exeter Biomedical Research Centre. The views expressed are those 
of the author(s) and not necessarily those of the NIHR or the Department of 
Health and Social Care.
This research has been conducted using the UK Biobank resource under 
application number 9072. JO, FC and JT are supported by an Academy of 
Medical Sciences (AMS) Springboard award, which is supported by the AMS, 
the Wellcome Trust, GCRF, the Government Department of Business, Energy 
and Industrial strategy, the British Heart Foundation and Diabetes UK 
[SBF004\1079]. A.R.W is supported by the European Research Council grant: 
SZ-245 50,371-GLUCOSEGENES-FP7-IDEAS-ERC. JB and VK are funded by a UK 
Research and Innovation (UKRI) Expanding Excellence in England (E3) grant 
awarded to the University of Exeter. The funders had no role in the study 
design, analysis or interpretation. All authors confirm their independence 
from the funders and confirm they had full access to all the data and can take 
responsibility for the integrity of the data and accuracy of the data analysis.

Availability of data and materials
UKB data are available to any bona fide researcher following application. 
Including the data on PA and ST: https:// www. ukbio bank. ac. uk/ enable- your- 
resea rch/ apply- for- access
The PA and ST whole cohort summary stats are available here: http:// dx. doi. 
org/https:// doi. org/ 10. 6084/ m9. figsh are. 24680 853
Summary statistics for the mental health metrics are available from the PGC: 
https:// pgc. unc. edu/ for- resea rchers/ downl oad- resul ts/ and here http:// dx. doi. 
org/https:// doi. org/ 10. 6084/ m9. figsh are. 24680 853

Declarations

Ethics approval and consent to participate
The Northwest Multi-Center Research Ethics Committee approved the collec-
tion and use of UKB data (Research Ethics Committee reference 11/NW/0382). 
All UK Biobank participants gave informed consent for the use of their data, 
health records, and biological materials for health-related research purposes.

Consent for publication
Not applicable.

Competing interests
The authors declare that they have no competing interests.

Received: 3 August 2023   Accepted: 4 December 2023

References
 1. 

Trautmann S, Rehm J, Wittchen HU. The economic costs of mental 
disorders: Do our societies react appropriately to the burden of mental 
disorders? EMBO Rep. 2016;17(9):1245–9.

 2.  Zhang ZJ, Chen WY. A systematic review of measures for psychological 

 3. 

 4. 

well-being in physical activity studies and identification of critical issues. J 
Affect Disorders. 2019;256:473–85.
Schuch FB. Physical Activity and Incident Depression: A Meta-Analysis 
of Prospective Cohort Studies (vol 175, pg 631, 2018). Am J Psychiat. 
2018;175(6):574–574.
Schuch FB, Stubbs B, Meyer J, Heissel A, Zech P, Vancampfort D, Rosen-
baum S, Deenik J, Firth J, Ward PB, et al. Physical activity protects from 
incident anxiety: A meta-analysis of prospective cohort studies. Depress 
Anxiety. 2019;36(9):846–58.

 5.  US Department of Health and Human Services: Physical activity guide-

lines advisory committee scientific report. 2018. https:// health. gov/ sites/ 
defau lt/ files/ 2019- 09/ PAG_ Advis ory_ Commi ttee_ Repor tpdf. Accessed 08 
Dec 2023.

 6.  Gianfredi V, Blandi L, Cacitti S, Minelli M, Signorelli C, Amerio A, Odone 
A. Depression and Objectively Measured Physical Activity: A Sys-
tematic Review and Meta-Analysis. Int J Environ Res Public Health. 
2020;17(10):3738. https:// doi. org/ 10. 3390/ ijerp h1710 3738.

 7.  Rebar AL, Stanton R, Geard D, Short C, Duncan MJ, Vandelanotte C. 

A meta-meta-analysis of the effect of physical activity on depression 
and anxiety in non-clinical adult populations. Health Psychol Rev. 
2015;9(3):366–78.

 8.  Zhai L, Zhang Y, Zhang D. Sedentary behaviour and the risk of depression: 

a meta-analysis. Br J Sports Med. 2015;49(11):705–9.

 9.  Allen MS, Walter EE, Swann C. Sedentary behaviour and risk of anxiety: A 

systematic review and meta-analysis. J Affect Disorders. 2019;242:5–13.

 10.  Atkin AJ, Adams E, Bull FC, Biddle SJ. Non-occupational sitting and men-
tal well-being in employed adults. Ann Behav Med. 2012;43(2):181–8.
 11.  Endrighi R, Steptoe A, Hamer M. The effect of experimentally induced 

sedentariness on mood and psychobiological responses to mental stress. 
Br J Psychiatry. 2016;208(3):245–51.

 12.  Tremblay MS, Aubert S, Barnes JD, Saunders TJ, Carson V, Latimer-Cheung 
AE, Chastin SFM, Altenburg TM, Chinapaw MJM, Participants STCP. Seden-
tary Behavior Research Network (SBRN) - Terminology Consensus Project 
process and outcome. Int J Behav Nutr Phys Act. 2017;14(1):75.

 13.  Stamatakis E, Gill JMR. Sitting behaviour and physical activity: two sides of 

the same cardiovascular health coin? Br J Sports Med. 2019;53(14):852–3.

 14.  Dempsey PC, Biddle SJH, Buman MP, Chastin S, Ekelund U, Friedenre-
ich CM, Katzmarzyk PT, Leitzmann MF, Stamatakis E, van der Ploeg HP, 
et al. New global guidelines on sedentary behaviour and health for 
adults: broadening the behavioural targets. Int J Behav Nutr Phys Act. 
2020;17(1):151.

 15.  Whipple MO, Regensteiner JG, Bergouignan A. Is Being Physically Active 

Enough to Be Metabolically Healthy? The Key Role of Sedentary Behavior. 
Diabetes Care. 2021;44(1):17–9.

 16.  Bull FC, Al-Ansari SS, Biddle S, Borodulin K, Buman MP, Cardon G, Carty 
C, Chaput JP, Chastin S, Chou R, et al. World Health Organization 2020 
guidelines on physical activity and sedentary behaviour. Br J Sports Med. 
2020;54(24):1451–62.

 17.  Lawlor DA, Harbord RM, Sterne JAC, Timpson N, Smith GD. Mendelian 

randomization: using genes as instruments for making causal inferences 
in epidemiology. Stat Med. 2008;27(8):1133–63.

Casanova et al. BMC Medicine          (2023) 21:501 

Page 13 of 13

Variants Associated With Anxiety and Stress-Related Disorders: A 
Genome-Wide Association Study and Mouse-Model Study. JAMA Psy-
chiat. 2019;76(9):924–32.

 37.  Conn VS. Depressive symptom outcomes of physical activity interven-
tions: meta-analysis findings. Ann Behav Med. 2010;39(2):128–38.
 38.  Richards J, Jiang X, Kelly P, Chau J, Bauman A, Ding D. Don’t worry, be 

happy: cross-sectional associations between physical activity and happi-
ness in 15 European countries. BMC Public Health. 2015;15:53.
 39.  Zhang Z, Chen W. A Systematic Review of the Relationship Between 

Physical Activity and Happiness. J Happiness Stud. 2019;20(4):1305–22.
 40.  Blacklock RE, Rhodes RE, Brown SG. Relationship between regular walk-
ing, physical activity, and health-related quality of life. J Phys Act Health. 
2007;4(2):138–52.

 41.  Ellingson LD, Meyer JD, Shook RP, Dixon PM, Hand GA, Wirth MD, Paluch 
AE, Burgess S, Hebert JR, Blair SN. Changes in sedentary time are associ-
ated with changes in mental wellbeing over 1year in young adults. Prev 
Med Rep. 2018;11:274–81.

 42.  de Wit L, van Straten A, Lamers F, Cuijpers P, Penninx B. Are sedentary 

television watching and computer use behaviors associated with anxiety 
and depressive disorders? Psychiatry Res. 2011;186(2–3):239–43.

 43.  Wray NR, Ripke S, Mattheisen M, Trzaskowski M, Byrne EM, Abdellaoui A, 
Adams MJ, Agerbo E, Air TM, Andlauer TMF, et al. Genome-wide associa-
tion analyses identify 44 risk variants and refine the genetic architecture 
of major depression. Nat Genet. 2018;50(5):668–81.

 44.  Fry A, Littlejohns TJ, Sudlow C, Doherty N, Adamska L, Sprosen T, Collins R, 

Allen NE. Comparison of Sociodemographic and Health-Related Charac-
teristics of UK Biobank Participants With Those of the General Population. 
Am J Epidemiol. 2017;186(9):1026–34.

 45.  Tyrrell J, Mulugeta A, Wood AR, Zhou A, Beaumont RN, Tuke MA, Jones 
SE, Ruth KS, Yaghootkar H, Sharp S, et al. Using genetics to understand 
the causal influence of higher BMI on depression. Int J Epidemiol. 
2019;48(3):834–48.

 46.  Tyrrell J, Wood AR, Ames RM, Yaghootkar H, Beaumont RN, Jones SE, 

Tuke MA, Ruth KS, Freathy RM, Davey Smith G, et al. Gene-obesogenic 
environment interactions in the UK Biobank study. Int J Epidemiol. 
2017;46(2):559–75.

 47.  Tyrrell J, Zheng J, Beaumont R, Hinton K, Richardson TG, Wood AR, Davey 
Smith G, Frayling TM, Tilling K. Genetic predictors of participation in 
optional components of UK Biobank. Nat Commun. 2021;12(1):886.
 48.  Schoeler T, Speed D, Porcu E, Pirastu N, Pingault JB, Kutalik Z. Participation 
bias in the UK Biobank distorts genetic associations and downstream 
analyses. Nat Hum Behav. 2023;7(7):1216–27.

 49.  Casanova F, O’Loughlin J, Martin S, Beaumont RN, Wood AR, Watkins ER, 

Freathy RM, Hagenaars SP, Frayling TM, Yaghootkar H, et al. Higher adipos-
ity and mental health: causal inference using Mendelian randomization. 
Hum Mol Genet. 2021;30(24):2371–82.

 50.  Casanova F, O’Loughlin J, Lewis C, Frayling TM, Wood AR, Tyrrell J. Simu-

lated distributions from negative experiments highlight the importance 
of the body mass index distribution in explaining depression-body mass 
index genetic risk score interactions. Int J Epidemiol. 2022;51(5):1581–92.

Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub-
lished maps and institutional affiliations.

 18.  Davies NM, Holmes MV, Davey Smith G. Reading Mendelian randomisa-
tion studies: a guide, glossary, and checklist for clinicians. BMJ. 2018;362: 
k601.

 19.  Choi KW, Chen CY, Stein MB, Klimentidis YC, Wang MJ, Koenen KC, Smoller 

JW. Major Depressive Disorder Working Group of the Psychiatric Genom-
ics C: Assessment of bidirectional relationships between physical activity 
and depression among adults: a 2-sample Mendelian randomization 
study. JAMA Psychiat. 2019;76(4):399–408.

 20.  Zheng J, Baird D, Borges MC, Bowden J, Hemani G, Haycock P, Evans DM, 

Smith GD. Recent developments in Mendelian randomization studies. 
Curr Epidemiol Rep. 2017;4(4):330–45.

 21.  Doherty A, Smith-Byrne K, Ferreira T, Holmes MV, Holmes C, Pulit SL, Lind-

gren CM. GWAS identifies 14 loci for device-measured physical activity 
and sleep duration. Nat Commun. 2018;9(1):5257.

 22.  Howard DM, Adams MJ, Clarke TK, Hafferty JD, Gibson J, Shirali M, 

Coleman JRI, Hagenaars SP, Ward J, Wigmore EM, et al. Genome-wide 
meta-analysis of depression identifies 102 independent variants and 
highlights the importance of the prefrontal brain regions. Nat Neurosci. 
2019;22(3):343–52.

 23.  Otowa T, Hek K, Lee M, Byrne EM, Mirza SS, Nivard MG, Bigdeli T, Aggen 
SH, Adkins D, Wolen A, et al. Meta-analysis of genome-wide association 
studies of anxiety disorders. Mol Psychiatry. 2016;21(10):1391–9.
 24.  Okbay A, Baselmans BM, De Neve JE, Turley P, Nivard MG, Fontana MA, 
Meddens SF, Linner RK, Rietveld CA, Derringer J, et al. Genetic vari-
ants associated with subjective well-being, depressive symptoms, and 
neuroticism identified through genome-wide analyses. Nat Genet. 
2016;48(6):624–33.

 25.  McManus S, Bebbington P, Jenkins R, Brugha T. Mental health and wellbe-
ing in England: Adult Psychiatric Morbidity Survey 2014. In: Leeds NHS 
DIgital. 2016. https:// files. digit al. nhs. uk/ pdf/q/ 3/ mental_ health_ and_ 
wellb eing_ in_ engla nd_ full_ report. pdf. Accessed 08 Dec 2023.

 26.  Casanova F, Tyrrell J, Beaumont RN, Ji Y, Jones SE, Hattersley AT, Weedon 
MN, Murray A, Shore AC, Frayling TM, et al. A genome-wide associa-
tion study implicates multiple mechanisms influencing raised urinary 
albumin-creatinine ratio. Hum Mol Genet. 2019;28(24):4197–207.
 27.  Bycroft C, Freeman C, Petkova D, Band G, Elliott LT, Sharp K, Motyer A, 

Vukcevic D, Delaneau O, O’Connell J, et al. The UK Biobank resource with 
deep phenotyping and genomic data. Nature. 2018;562(7726):203–9.
 28.  Willetts M, Hollowell S, Aslett L, Holmes C, Doherty A. Statistical machine 

learning of sleep and physical activity phenotypes from sensor data in 
96,220 UK Biobank participants. Sci Rep. 2018;8(1):7961.

 29.  Loh PR, Tucker G, Bulik-Sullivan BK, Vilhjalmsson BJ, Finucane HK, Salem 
RM, Chasman DI, Ridker PM, Neale BM, Berger B, et al. Efficient Bayesian 
mixed-model analysis increases association power in large cohorts. Nat 
Genet. 2015;47(3):284–90.

 30.  Levey DF, Stein MB, Wendt FR, Pathak GA, Zhou H, Aslan M, Quaden 
R, Harrington KM, Nunez YZ, Overstreet C, et al. Bi-ancestral depres-
sion GWAS in the Million Veteran Program and meta-analysis in >1.2 
million individuals highlight new therapeutic directions. Nat Neurosci. 
2021;24(7):954–63.

 31.  Davis KAS, Coleman JRI, Adams M, Allen N, Breen G, Cullen B, Dickens 
C, Fox E, Graham N, Holliday J, et al. Mental health in UK Biobank - 
development, implementation and results from an online questionnaire 
completed by 157 366 participants: a reanalysis. BJPsych Open. 2020;6(2): 
e18.

 32.  Mounier N, Kutalik Z. Bias correction for inverse variance weighting Men-

delian randomization. Genet Epidemiol. 2023;47(4):314–31.

 33.  Bowden J, Del Greco MF, Minelli C, Zhao Q, Lawlor DA, Sheehan NA, 
Thompson J, Davey Smith G. Improving the accuracy of two-sample 
summary-data Mendelian randomization: moving beyond the NOME 
assumption. Int J Epidemiol. 2019;48(3):728–42.

 34.  Levey DF, Gelernter J, Polimanti R, Zhou H, Cheng Z, Aslan M, Quaden 

R, Concato J, Radhakrishnan K, Bryois J, et al. Reproducible Genetic Risk 
Loci for Anxiety: Results From approximately 200,000 Participants in the 
Million Veteran Program. Am J Psychiatry. 2020;177(3):223–32.
 35.  Purves KL, Coleman JRI, Meier SM, Rayner C, Davis KAS, Cheesman R, 
Baekvad-Hansen M, Borglum AD, Wan Cho S, JurgenDeckert J, et al. A 
major role for common genetic variation in anxiety disorders. Mol Psy-
chiatry. 2020;25(12):3292–303.

 36.  Meier SM, Trontti K, Purves KL, Als TD, Grove J, Laine M, Pedersen MG, 
Bybjerg-Grauholm J, Baekved-Hansen M, Sokolowska E, et al. Genetic
