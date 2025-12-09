# Wani_2024_Blood-based DNA methylation and exposure risk scores predict PTSD with high accuracy in military and civilian cohorts.

Wani et al. BMC Medical Genomics          (2024) 17:235  
https://doi.org/10.1186/s12920-024-02002-6

BMC Medical Genomics

RESEARCH

Open Access

Blood-based DNA methylation and exposure 
risk scores predict PTSD with high accuracy 
in military and civilian cohorts
Agaz H. Wani1, Seyma Katrinli2†, Xiang Zhao3†, Nikolaos P. Daskalakis4,5,6, Anthony S. Zannas7,8,9,10, 
Allison E. Aiello11, Dewleen G. Baker12,13,14, Marco P. Boks15, Leslie A. Brick16, Chia‑Yen Chen17, 
Shareefa Dalvie18,19, Catherine Fortier5,20, Elbert Geuze21,22, Jasmeet P. Hayes23, Ronald C. Kessler24, 
Anthony P. King25, Nastassja Koen26,27,28, Israel Liberzon29, Adriana Lori30, Jurjen J. Luykx22,31, 
Adam X. Maihofer12,13,32, William Milberg33, Mark W. Miller34,35, Mary S. Mufford27,36, Nicole R. Nugent37,38,39, 
Sheila Rauch40,41, Kerry J. Ressler5,30,42, Victoria B. Risbrough12,13,32, Bart P. F. Rutten43, Dan J. Stein26,27,28, 
Murray B. Stein12,14,44, Robert J. Ursano45, Mieke H. Verfaellie46,47, Eric Vermetten48,49, Christiaan H. Vinkers50,51,52, 
Erin B. Ware53, Derek E. Wildman1, Erika J. Wolf35,54, Caroline M. Nievergelt12,13,32, Mark W. Logue3,35,55, 
Alicia K. Smith2,30,56 and Monica Uddin1* 

Abstract 
Background  Incorporating genomic data into risk prediction has become an increasingly popular approach for rapid 
identification of individuals most at risk for complex disorders such as PTSD. Our goal was to develop and validate 
Methylation Risk Scores (MRS) using machine learning to distinguish individuals who have PTSD from those who 
do not.

Methods  Elastic Net was used to develop three risk score models using a discovery dataset (n = 1226; 314 cases, 912 
controls) comprised of 5 diverse cohorts with available blood‑derived DNA methylation (DNAm) measured on the Illu‑
mina Epic BeadChip. The first risk score, exposure and methylation risk score (eMRS) used cumulative and childhood 
trauma exposure and DNAm variables; the second, methylation‑only risk score (MoRS) was based solely on DNAm 
data; the third, methylation‑only risk scores with adjusted exposure variables (MoRSAE) utilized DNAm data adjusted 
for the two exposure variables. The potential of these risk scores to predict future PTSD based on pre‑deployment 
data was also assessed. External validation of risk scores was conducted in four independent cohorts.

Results  The eMRS model showed the highest accuracy (92%), precision (91%), recall (87%), and f1‑score (89%) in clas‑
sifying PTSD using 3730 features. While still highly accurate, the MoRS (accuracy = 89%) using 3728 features and MoR‑
SAE (accuracy = 84%) using 4150 features showed a decline in classification power. eMRS significantly predicted PTSD 
in one of the four independent cohorts, the BEAR cohort (beta = 0.6839, p=0.006), but not in the remaining three 
cohorts. Pre‑deployment risk scores from all models (eMRS, beta = 1.92; MoRS, beta = 1.99 and MoRSAE, beta = 1.77) 
displayed a significant (p < 0.001) predictive power for post‑deployment PTSD.

†Seyma Katrinli and Xiang Zhao contributed equally to this work.

*Correspondence:
Monica Uddin
monica43@usf.edu
Full list of author information is available at the end of the article

© The Author(s) 2024. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which 
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory 
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this 
licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 2 of 14

Conclusion  The inclusion of exposure variables adds to the predictive power of MRS. Classification‑based MRS may 
be useful in predicting risk of future PTSD in populations with anticipated trauma exposure. As more data become 
available, including additional molecular, environmental, and psychosocial factors in these scores may enhance their 
accuracy in predicting PTSD and, relatedly, improve their performance in independent cohorts.

Keywords  DNA methylation, Machine learning, PTSD, Risk scores

Background
Posttraumatic stress disorder (PTSD) is a psychiatric dis-
order that can develop after experiencing or witnessing a 
life-threatening event such as a war/combat, natural dis-
aster, violence, or serious accident. PTSD occurs in ~ 13% 
of  the  trauma-exposed  population  [1],  and  females  are 
twice  as  likely  to  experience  PTSD  as  males  [2].  PTSD 
commonly  occurs  together  with  other  psychiatric  disor-
ders [3–6] and has also been associated with other health 
conditions such as accelerated aging [7, 8], cardiovascular 
and metabolic disorders [9, 10], and poor physical health 
[11].  Consequently,  the  overall  burden  caused  by  PTSD 
is  high,  with  an  estimated  annual  economic  burden  of 
$232 billion in the United States in 2018, including $76.1 
billion in excess direct health care costs [12]. Identifying 
individuals  at  elevated  risk  of  PTSD  would  enhance  the 
ability to develop timely preventive strategies and thera-
pies for this disorder.

Incorporating  genomic  data  into  risk  prediction  has 
become an increasingly popular approach for rapid iden-
tification  of  individuals  most  at  risk  for  complex  disor-
ders  such  as  PTSD.  In  particular,  polygenic  risk  scores 
(PRS)  have  been  evaluated  in  both  research  and  clinical 
contexts  to  estimate  risk  to  develop  complex  disorders, 
including  coronary  artery  disease,  breast  cancer,  Type 
2  diabetes,  and  Alzheimer’s  Disease  (reviewed  in  [13]). 
These genetically-based risk scores are attractive as they 
access  lifetime  risk  for  a  particular  disorder  and  lever-
age  variation  across  hundreds  to  thousands  of  variants. 
However, most PRSs are not yet clinically useful, as they 
typically  explain  only  a  small  proportion  of  variance  in 
risk  for  a  particular  disorder  and  do  not  capture  envi-
ronmental factors that influence risk or detect the effect 
of  disease  progression  itself  [14],  both  of  which  may  be 
important  to  identifying  individuals  at  highest  risk  for 
disease.

In  contrast,  risk  scores  based  on  DNA  methylation 
(DNAm)  levels,  which  are  modifiable  and  dynamic,  can 
potentially  convey  more  information  about  disease  risk. 
A  growing  literature  has  shown  that  approaches  origi-
nally  developed  for  generating  PRS  can  be  adapted  for 
DNAm  data  (reviewed  in  [15,  16]).  The  resulting  meth-
ylation risk scores (MRS) have been shown in some cases 
to  be  more  indicative  of  current  disease  state  [17]  and 
health-related phenotypes [18], as well as more predictive 

of  future  disease  risk  [19],  than  PRS-based  approaches. 
Indeed,  for  PTSD,  which  requires  an  environmental 
exposure—trauma/shocking event —to meet the require-
ments  for  a  diagnosis,  MRS-based  risk  scores  that  cap-
ture  the  differential  effects  of  this  exposure  may  be 
particularly  informative  for  identifying  trauma-exposed 
individuals most at risk for the disorder.

To this end, here we leverage a large, ancestrally diverse 
set of cohorts to take a first step toward developing MRS 
for PTSD. We focus specifically on developing scores that 
distinguish  between  those  with  vs.  without  the  disorder 
(i.e.,  a  diagnostic  MRS  that  correctly  classifies  current 
cases  vs.  trauma-exposed  controls),  and  attempt  to  rep-
licate these MRS in multiple external validation cohorts. 
We further test whether these diagnostic risk scores have 
prognostic  value,  i.e.,  can  predict  future  PTSD  among 
individuals  prior  to  trauma  exposure.  Finally,  to  gain 
insight into potential mechanisms, we investigate the bio-
logical significance associated with the specific cytosine-
guanine sites separated by a phosphate group (i.e. (CpG) 
sites) that comprise the MRS.

Methods
Cohorts

In  order  to  maximize  the  available  data  from  which  to 
develop  risk  scores  using  machine  learning  approaches, 
we  created  a  discovery  cohort  comprised  of  1226  indi-
viduals  drawn  from  five  cohorts  (Table  1).  Two  of 
these  cohorts  are  civilian—  Detroit  Neighborhood 
Health  Study  (DNHS)  and  Grady  Trauma  Project 
(GTP),  and  three  cohorts  are  military—  Army  Study  to 
Assess  Risk  and  Resilience  in  Servicemembers  (Army 
STARRS),  Marine  Resilience  Study  (MRS  I&II),  and 
Prospective  Research  in  Stress-related  Military  Opera-
tions  (PRISMO).  Details  about  each  cohort  are  given  in 
the supplementary file. The overall workflow of the pre-
processing  and  methods  combining  data  from  the  five 
cohorts is shown in supplementary file (Figure S1).

Quality Control (QC) procedures

DNAm  from  whole  blood  was  measured  using  the  Illu-
mina  MethylationEPIC  BeadChip  following  the  manu-
facturer’s  recommended  protocol.  Raw  DNAm  β  values 
were obtained, and a sex check was conducted using the 

N

  Army STARRS

  DNHS

  GTP

  MRS I&II

  PRISMO

  All

Gender, Male (%)

  Army STARRS

  DNHS

  GTP

  MRS I&II

  PRISMO

  All

Age, mean (SD)

  Army STARRS

  DNHS

  GTP

  MRS I&II

  PRISMO

  All

Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 3 of 14

Table 1  Demographic and clinical characteristics of the studies 
included in the discovery cohort

Table 1  (continued)

Current PTSD

Cases

Controls

P value

Total

  All

Current PTSD

Cases

Controls

P value

Total

42

31

161

63

17

314

42 (27)

10 (2)

25 (5)

63 (51)

17 (34)

111

385

323

60

33

912

111 (73)

161 (39)

107 (22)

60 (49)

33 (66)

153

416

484

123

50

1226

153 (100)

171 (41)

132 (27)

123 (100)

50 (100)

  African American

187 (59.6)

703 (77.1)

  White

  Other

93 (29.6)

34 (10.8)

168 (18.4)

41 (4.5)

‑

‑

‑

890 (72.6)

261 (21.3)

75 (6.1)

Smoking Score, mean (SD)

  Army STARRS

‑5.4 (18.4)

‑7.8 (18)

4.75E‑01

‑7.1 (18.1)

  DNHS

  GTP

  MRS I&II

  PRISMO

  All

3.8 (30.5)

‑0.6 (33)

4.45E‑01

‑0.3 (32.8)

‑4.1 (35.4)

‑2.8 (35.4)

7.05E‑01

‑3.3 (35.4)

‑8.5 (17)

‑10.8 (15)

4.43E‑01

‑9.6 (16)

1.3 (16.9)

2 (21.3)

9.06E‑01

1.7 (19.7)

‑4.1 (29.3)

‑2.9 (31.3)

5.21E‑01

‑3.2 (30.8)

Childhood Trauma, mean (SD)

  Army STARRS

  DNHS

7.1 (3.3)

7.6 (5.7)

6.3 (2.2)

4.4 (3.4)

1.44E‑01

6.5 (2.5)

4.44E‑03

4.7 (3.7)

157 (50)

472 (51.8)

629 (51.3)

  GTP

56.1 (20.1)

37.7 (13.4)

1.67E‑21

43.8 (18.1)

25.8 (5.1)

25.5 (5.2)

7.54E‑01

25.6 (5.2)

  MRS I&II

  PRISMO

41.7 (12.2)

37.5 (10.4)

4.10E‑02

39.6 (11.5)

5.5 (2.6)

2.8 (2.2)

1.03E‑03

3.7 (2.7)

51.6 (11.1)

55.6 (17.1)

7.66E‑02

55.3 (16.8)

  All

39.1 (26.2)

18.5 (18.5)

3.3E‑32

23.8 (22.6)

41.7 (11.4)

42.4 (12.5)

5.48E‑01

42.2 (12.1)

Cumulative Trauma, Mean (SD)

23.3 (2.3)

22.9 (1.9)

3.59E‑01

23.1 (2.1)

  Army STARRS

28.1 (10.1)

27.5 (9.1)

8.29E‑01

27.7 (9.3)

36.1 (13.4)

44.1 (18)

5.89E‑16

42.1 (17.3)

  DNHS

  GTP

  MRS I&II

  PRISMO

PTSD symptom severity, mean (SD)

  Army STARRS

56.9 (9.6)

22.4 (5.8)

4.83E‑28

32 (17)

  DNHS

  GTP

  MRS I&II

  PRISMO

  All

63 (16)

32.7 (11.4)

1.89E‑11

34.9 (14.2)

  All

70.4 (18.6)

25.1 (16.9)

2.17E‑32

38.5 (27.1)

65.4 (14.8)

13.6 (11.8)

1.30E‑42

40.2 (29.2)

42 (4.4)

27 (4.8)

6.72E‑13

32.1 (8.5)

63.1 (16.7)

27.7 (13.3)

5.88E‑88

35.8 (20.5)

1 (0)

12.2 (7)

7 (3.1)

1 (0)

6.1 (4.1)

4.4 (2.8)

11.2 (2.9)

10.3 (3.8)

6.5 (3.1)

7.6 (4.8)

5.9 (3.8)

5.2 (4)

‑

1 (0)

3.63E‑05

6.6 (4.7)

2.33E‑17

5.3 (3.1)

0.125

0.557

10.8 (3.4)

6.1 (3.5)

9.45E‑15

5.8 (4.3)

Self-reported Race/Ethnicity, N (%)

  Army STARRS

  African American

3 (2)

  White

  Other

  DNHS

29 (19)

10 (6.5)

12 (7.8)

88 (57.5)

11 (7.2)

  African American

28 (6.7)

381 (91.6)

  Other

  GTP

3 (0.7)

4 (1)

  African American

153 (31.6)

307 (63.4)

  Other

  MRS I&II

8 (1.7)

16 (3.3)

  African American

2 (1.6)

2 (1.6)

  White

  Other

  PRISMO

53 (43.1)

53 (43.1)

8 (6.5)

5 (4.1)

  African American

1 (2)

  White

  Other

11 (22)

5 (10)

1 (2)

27 (54)

5 (10)

‑

‑

‑

‑

‑

‑

‑

‑

‑

‑

‑

‑

‑

‑

‑

15 (9.8)

117 (76.5)

21 (13.7)

409 (98.3)

7 (1.7)

460 (95)

24 (5)

4 (3.3)

106 (86.2)

13 (10.6)

2 (4)

38 (76)

10 (20)

minfi R package [20] to eliminate any sex-discordant sam-
ples. Quality control (QC) was performed on each cohort 
separately,  using  a  standardized  pipeline  as  previously 
described  [21].  A  total  of  818,691  probes  passed  QC. 
Normalization  was  carried  out  using  the  single-sample 
Noob (ssNoob) method in the minfi R package [20]. Fur-
thermore,  ComBat  adjustment  was  performed,  using  an 
empirical Bayesian framework implemented in the SVA R 
package  [22,  23]  to  reduce  the  likelihood  of  bias  due  to 
known batch effects (chip and position), while preserving 
the  variation  for  age,  sex  (if  applicable),  and  PTSD.  The 
resulting QC’d data was used in subsequent analyses.

Estimation of covariates
Smoking scores

Studies have linked methylation at many genomic loci to 
smoking  status  [24–29].  Therefore,  to  adjust  for  DNAm 
differences  related  to  smoking,  we  calculated  smoking 
scores  from  DNAm  data  based  on  the  weights  obtained 
from 39 CpGs located at 27 loci, as previously described 
[30].

  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 4 of 14

Cell proportions

It  is  important  to  consider  cellular  heterogeneity  in 
epigenome-wide  association  studies  (EWAS)  [31]  since 
whole  blood  contains  various  cell  types,  each  with  its 
own DNAm profile [32, 33]. To address this, cell propor-
tions  (CD4 + T,  CD8 + T,  Natural  Killer  (NK),  B-cells, 
monocytes, and neutrophils) were estimated using refer-
ence data [34] and the Robust Partial Correlation (RPC) 
method implemented in the EpiDISH R package [35].

Ancestry principal components

Several    studies  have  found  variations  in  DNAm  levels 
among  different  populations  (race/ethnicity)  at  certain 
CpG  sites  [36–41].  Therefore,  to  account  for  popula-
tion  stratification,  ancestry  principal  components  (PCs) 
were  generated  from  methylation  data  using  a  subset  of 
CpGs  in  close  proximity  to  SNPs  in  data  from  the  1000 
Genomes  Project  [42,  43].  As  previously  reported  [42, 
43],  PC  2  and  3  were  the  components  most  correlated 
with  ancestry  and  thus,  used  to  adjust  for  population 
stratification in this study.

(number  of  traumatic  events  experienced)  and  child-
hood  trauma  (experienced  at < 18  years  of  age)—along 
with  DNAm  data,  as  increasing  levels  of  exposures  are 
known  to  substantially  increase  the  risk  of  developing 
PTSD  [47–50]  and  were  thus  hypothesized  to  contrib-
ute high predictive power to our model. The purpose of 
Model  2  was  to  classify  PTSD  using  only  DNAm  data, 
without relying on the discriminatory power of cumula-
tive trauma or childhood trauma; this model would ena-
ble potential application to cohorts in which only DNAm 
data were available. Model 3 was developed with a unique 
purpose,  distinct  from  Model  1.  Namely,  it  was  created 
to  account  for  variations  in  exposure  variables  among 
individual  cohorts.  In  this  model,  exposure  variables 
were  intentionally  excluded  from  the  analysis  because 
they were used as covariates in DNAm data adjustment. 
While Model 3 addresses the challenge of cohort-specific 
variations, it does not possess the same predictive power 
as Model 1, which incorporates these exposure variables. 
The  adjusted  data  was  then  subjected  to  the  following 
analysis processes.

Covariate adjustment

Feature selection and scaling

All the discovery cohorts had a small percentage of miss-
ing values (ranging from 0.002 to 0.03%). As the machine 
learning  models  require  complete  data,  we  used  the 
mean  method—a  common  and  simple  imputation  tech-
nique  to  impute  the  missing  data  while  maintaining  the 
distribution  of  the  data  [44,  45].  We  then  adjusted  the 
DNAm data for potential confounding factors, including 
cell composition, ancestry, smoking score, sex (if applica-
ble), and age, for models 1 and 2 (described below). The 
adjustment was made for each CpG by regressing out all 
the covariates using linear regression and then replacing 
the values of CpG with the corresponding residuals [46]. 
For model 3 (described below), we also regressed out the 
two  exposure  variables  of  interest,  cumulative  trauma 
and childhood trauma, in addition to the covariates used 
in  models  1  and  2.  This  was  done  separately  for  each 
cohort to account for any differences related to exposure 
variables in individual cohorts.

Analysis
Overall approach

Our  goal  was  to  develop  a  series  of  models  based  on 
important  (i.e.  set  of  features  with  best  classification 
accuracy)  methylation-  and  (in  some  cases)  exposure-
related features to classify PTSD that would then be used 
to derive risk scores with which to predict PTSD. To train 
the  models,  we  utilized  unique,  trauma  exposed  par-
ticipants  from  the  discovery  cohort  in  a  cross-sectional 
approach.  Model  1  was  designed  to  classify  PTSD  by 
including  two  exposure  variables—cumulative  trauma 

We used SelectKBest in Scikit-learn [51], a univariate fea-
ture selection approach. This method computes ANOVA 
F-values  based  on  univariate  statistical  tests  to  identify 
the best features in relation to a particular phenotype. We 
identified the most important features from DNAm and 
exposure  variables  (in  cases  of  Models  1  &  2)  based  on 
the rank order of the features’ association with PTSD. For 
Model  3,  we  selected  features  solely  from  DNAm  data. 
The  feature  selection  process  was  repeated  500  times, 
ranging from 10 to 5000 features with a 10-feature incre-
ment each time to determine the optimal feature set for 
the Elastic Net model best accuracy. As different studies/
cohorts  used  different  instruments  to  measure  cumula-
tive  trauma  and  childhood  trauma,  we  normalized  the 
data using a min–max scale that ranged from [1].

Training and testing

In order to identify the best model to classify PTSD and 
determine risk scores, we trained three popular machine 
learning  models  —Random  Forest,  Lasso,  and  Elas-
tic Net on 75% of the data, and then tested them on the 
remaining  25%  using  the  Scikit-learn  [51]  framework. 
We  also  conducted  a  tenfold  cross-validation  on  train-
ing  and  testing  data  to  evaluate  the  effectiveness  of  the 
models  (Figure  S1.1).  After  selecting  the  most  accurate 
machine  learning  model,  which  was  evaluated  based  on 
the  methylation  and  exposure  variable  dataset,  we  used 
important features identified during the feature selection 
process to classify PTSD. Following covariate adjustment 
of  the  two  additional  exposure  variables,  we  re-ran  the 

Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 5 of 14

feature  selection  process  to  identify  important  features 
for Model 3 (described below). Performance of the mod-
els was assessed using accuracy, precision, recall, f1-score 
and area under the curve (AUC) metrics.

Risk scores

Risk  scores  are  the  weighted  sum  of  the  important  fea-
tures. Using feature weights (i.e. effect sizes) from train-
ing  data  (75%),  we  created  risk  scores  using  discovery 
cohort test data (25%), in order to test for an association 
between  risk  scores  and  PTSD.  Model  1  contributed  to 
the development of exposure and methylation risk scores 
(eMRS), whereas Model 2 provided methylation-only risk 
scores  (MoRS).  Finally,  Model  3  led  to  the  creation  of 
methylation-only risk scores with adjusted exposure vari-
ables (MoRSAE).

A  logistic  model  was  employed  to  test  for  an  associa-
tion  between  risk  scores  (eMRS,  MoRS  and  MoRSAE) 
and  PTSD,  and  the  Nagelkerke  approach  was  used  to 
assess  the  models’  resulting  R-Squared   (R2)  values.  For 
all analyses, a Wilcoxon rank-sum test was used to assess 
differences in risk scores between cases and controls. To 
assess the direction of effect and strength of association 
among  study  variables  in  the  both  discovery  and  inde-
pendent cohorts, Pearson’s and point-biserial correlation 
was used, as appropriate.

Independent validation

To validate the risk scores, we tested their ability to dis-
tinguish those with vs. without PTSD in four independ-
ent, external cohorts using the same pre-processing and 
covariate adjustment pipeline as in the discovery cohort. 
Brief  descriptions  of  the  external  cohorts  (NCPTSD-
TRACTS, BEAR, DCHS and PROGrESS) are provided in  
Supplementary  File  1.  We  utilized  weights  from  signifi-
cant  features  identified  in  models  1,  2,  and  3  of  the  dis-
covery cohort to generate risk scores (i.e., eMRS, MoRS, 
and MoRSAE) in the external cohorts. Similar to the dis-
covery cohorts, we conducted Pearson and Point-Biserial 
correlation  tests,  association  tests  using  logistic  regres-
sion  model,  and  Wilcoxon  rank-sum  tests  on  external 
cohorts.

MRS-based predictive analyses

In cohorts with available pre-deployment data, a logistic 
model was used to predict post-deployment PTSD using 
risk  scores  calculated  from  pre-deployment  DNAm  data 
and  exposure  data  (Army  STARRS,  MRS  I&II;  n = 276). 
Note  that  these  participants  had  their  post-deployment 
DNAm  data  included  in  the  discovery  cohort  analyses 
described above.

Enrichment analysis

To  investigate  the  biological  significance  of  the  impor-
tant  CpGs  identified  in  the  feature  selection  step,  we 
performed  Gene  Ontology  (GO)  enrichment  analysis 
and Kyoto Encyclopedia of Genes and Genomes (KEGG) 
pathway analysis using missMethyl [52]. Gene ontologies 
and KEGG pathways that reached a nominal significance 
level of p < 0.05 were considered important.

Results
Description of discovery cohort

Table  1  provides  a  summary  of  the  demographic  char-
acteristics  and  clinical  information  of  all  participants 
(n = 1226)  in  the  discovery  cohort  with  current  PTSD. 
More  information  about  cumulative  and  childhood 
trauma is provided in Table S1. A slight majority of par-
ticipants  were  male  (n = 629).  Two  cohorts,  DNHS  and 
GTP, were comprised mostly of African Americans, while 
the remaining three cohorts were predominantly of Euro-
pean  ancestry.  In  all  cohorts,  a  significant  difference  in 
PTSD symptom severity was observed between cases and 
controls (p < 0.05). With the exception of Army STARRS, 
childhood trauma also demonstrated a significant differ-
ence  between  PTSD  cases  and  controls  (p < 0.05)  in  all 
cohorts.  Finally,  a  significant  difference  was  observed  in 
cumulative trauma between cases and controls in DNHS 
and GTP (p < 0.001).

Development of methylation risk scores to distinguish 
those with vs. without PTSD

We  developed  three  different  risk  scores  with  the  goal 
of  distinguishing  those  with  vs.  without  PTSD  using 
machine  learning  approaches.  Our  first  model,  eMRS, 
included  both  exposure  and  DNAm  variables  and  iden-
tified 3730 features (3728 CpGs, cumulative trauma, and 
childhood trauma) as important in the discovery cohort. 
Using  these  3730  features,  Elastic  Net  approaches  were 
employed to achieve the best accuracy (92%; Fig. 1), pre-
cision  (91%),  recall  (87%),  and  f1-score  (89%);  Table  2 
(See  Fig.  S2  for  AUCs  with  Lasso  and  Random  Forest 
approaches).  The  eMRS  significantly  predicted  PTSD 
(beta = 2.64,  p < 0.001),   R2 = 0  0.70),  with  higher  eMRS 
values  in  PTSD  cases  than  controls  (p < 0.001;  Fig.  2A, 
left  plot).  Our  second  MoRS  model,  based  solely  on  the 
3728  methylation  features  in  model  1,  accurately  clas-
sified  PTSD  with  89%  accuracy  and  had  an  AUC  of 
95%  (Fig.  3;  Table  2).  Additionally,  the  precision,  recall, 
and  f1-score  were  at  86%,  83%,  and  84%,  respectively, 
as  shown  in  Table  2.  As  with  eMRS,  the  MoRS  signifi-
cantly predicted PTSD (beta = 2, p < 0.001,  R2 = 0.54) and 
had  higher  MoRS  values  in  cases  vs  controls  (p < 0.001) 
(Fig.  2A,  middle  plot).  Our  third  and  final  model  (i.e., 

 Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 6 of 14

Fig. 1  The confusion matrix for Model 1 displays an accuracy of 92% on test data (N = 307), while the ROC curve indicates an AUC of 96% 
during the tenfold cross‑validation using all data (N = 1226)

Table 2  Elastic net model performance across the three models

Model

Accuracy (%)

Precision (%)

Recall (%)

F1-score (%)

AUC (%)

eMRS (Model 1)

MoRS (Model 2)

MoRSAE (Model 3)

92

89

84

91

86

80

87

83

77

89

84

78

96

95

89

MoRSAE), which used DNAm data adjusted for the two 
exposure variables as well as the other covariates in mod-
els 1 and 2, identified 4150 significant features that classi-
fied PTSD with 84% accuracy and an AUC of 89% (Fig. 4, 
with precision, recall, and f1-score at 80%, 77%, and 78%, 
respectively (Table 2). As with models eMRS and MoRS, 
MoRSAE  significantly  predicted  PTSD  (beta = 1.20, 
p < 0.001,   R2 = 0.36)  and  had  significantly  (p < 0.001)  dif-
ferent,  and  higher,  MoRSAE  in  PTSD  cases  vs.  controls 
(Fig. 2A, right plot). In summary, while all three models 
produced  risk  scores  that  significantly  predicted  PTSD 
in  the  test  dataset,  and  showed  higher  scores  in  aggre-
gate  between  cases  and  controls,  there  was  a  decline 
in  effect  size  (b)  and  explanatory  power   (R2)  such  that 
eMRS > MoRS > MoRSAE.

Intercorrelation among study variables

A  significant  positive  point-biserial  correlation  between 
eMRS  and  current  PTSD  was  observed  (ρ = 0.72, 
p < 0.001;  Figure  S3).  Cumulative  trauma  (ρ = 0.40, 
p < 0.001)  and  childhood  trauma  (ρ = 0.57,  p < 0.001) 
also  showed  a  positive  and  significant  correlation  with 
eMRS. Notably, there was also a significant and positive 
point-biserial  correlation  (ρ = 0.62,  p < 0.001)  between 

MoRS  and  PTSD,  significant  and  positive  correlation 
between cumulative trauma and MoRS (ρ = 0.16, p < 0.01) 
and  childhood  trauma  and  MoRS  (ρ = 0.169,  p < 0.01) 
(Figure  S3).  In  contrast,  while  we  observed  a  signifi-
cant  (p < 0.001)  and  positive  point-biserial  correlation 
(ρ = 0.49)  between  MoRSAE  and  PTSD  (Figure  S3),  we 
observed  a  negative  correlation  between  MoRSAE  and 
cumulative  trauma  (ρ = -0.13,  p = 0.02)  and  childhood 
trauma (ρ = -0.12, p = 0.03), respectively.

Validation of risk scores in external cohorts

We  conducted  external  validation  on  risk  scores  from 
the three different models across four external cohorts— 
NCPTSD-TRACTS,  BEAR,  DCHS  and  PROGrESS. 
The  NCPTSD-TRACTS  cohort  demonstrated  a  notice-
able  distinction  (p < 0.05)  in  childhood  trauma,  but  not 
in  cumulative  trauma  (Table  S1)  between  cases  and 
controls.  Similar  to  the  discovery  cohorts,  the  BEAR 
cohort  exhibited  a  significant  difference  in  both  cumu-
lative  trauma  and  childhood  trauma  when  compar-
ing  cases  and  controls.  The  DCHS  cohort,  on  the  other 
hand, only showed a significant difference in cumulative 
trauma, while the PROGrESS cohort did not display any 

Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 7 of 14

Fig. 2  Distribution and variation of risk scores between cases and controls in test data (N = 307) in figure legend, 0 is No PTSD and 1 is PTSD. A) 
The distribution of risk scores for Models 1, 2, and 3 is shown for both cases and controls. B) The difference in risk scores, and associated p value, 
between cases and controls is displayed. Model 1 calculates exposure and methylation risk scores (eMRS), while Model 2 calculates risk scores based 
only on methylation variables (MoRS). Model 3 calculates risk scores based on methylation variables adjusted for exposure variables (MoRSAE). 
The risk scores are higher in PTSD cases compared to controls. The Wilcoxon test confirms a significant difference in risk scores between cases 
and controls with p < 0.001 for all models (1, 2, and 3)

Fig. 3  The confusion matrix for Model 2 displays an accuracy of 89% on test data (N = 307), while the ROC curve indicates an AUC of 95% 
during the tenfold cross‑validation using all data (N = 1226)

significant  difference  in  trauma  variables  between  cases 
and controls.

The  eMRS  significantly  predicted  PTSD  in  one  exter-
nal  cohort,  BEAR  (beta = 0.6839,  p = 0.006)  (Table  S2); 

in  this  cohort,  there  was  also  a  significant  correlation 
(ρ = 0.24,  p = 0.003)  between  eMRS  and  PTSD  (Figure 
S4)  and  a  significant  difference  in  eMRS  between  PTSD 
cases  and  controls  (p = 0.02,  Figure  S5).  The  eMRS  did 

 Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 8 of 14

Fig. 4  The confusion matrix for Model 3 displays an accuracy of 84% on test data (N = 307), while the ROC curve exhibits an AUC of 89% 
during the tenfold cross‑validation process using all data (N = 1226)

not  significantly  predict  PTSD  in  any  of  the  other  three 
independent  cohorts;  however,  the  correlation  between 
eMRS  and  PTSD  showed  the  same  (i.e.,  positive)  direc-
tion  of  effect  in  the  NCPTSD-TRACTS  (beta = 0.0598, 
p = 0.35), PROGrESS (beta = 0.1141, p = 0.53) and DCHS 
(beta = 0.0631,  p = 0.81)  cohorts  (Figures  S6-S11).  For 
model 2, the MoRS did not significantly predict PTSD in 
any  external  cohort  (NCPTSD-TRACTS:  beta = -0.0977, 
p = 0.28;  BEAR:  beta = 0.0239,  p = 0.93;  PROGrESS: 
beta = 0.2156,  p = 0.52;  DCHS:  beta = 0.3739,  p = 0.37). 
On the other hand, for model 3, the MoRSAE approached 
significance  in  association  with  PTSD  in  the  NCPTSD-
TRACTS cohort (beta = -0.1707, p = 0.05) and had signif-
icant difference in risk scores between cases and controls 
(p = 0.018)  (Figure  S7);  however,  the  direction  of  effect 
was opposite to that observed in the discovery cohort.

Testing of pre-deployment risk scores to predict future 
PTSD

A compelling feature of risk scores is their ability to pre-
dict future disease risk. In our data, we were able to test 
the predictive ability of the MRS derived from our diag-
nostic/classification models on prospective risk of PTSD 
in  two  of  our  pre-deployment  military  cohorts,  MRS 
I&II and Army STARRS (with data from the two cohorts 
analyzed together). MRS were calculated using “unseen” 
DNAm data from a pre-deployment timepoint, i.e. using 
DNAm  data  not  included  in  the  discovery  cohort.  All 
three  models  significantly  predicted  future  PTSD  based 
on  risk  scores  calculated  with  pre-deployment  data 
(eMRS beta = 1.92, p < 0.001,  R2 = 0.53; MoRS beta = 1.99, 
p < 0.001,   R2 = 0.46;  and  MoRSAE  beta = 1.77,  p < 0.001, 

 R2 = 0.47)  and  had  significant  difference  in  risk  scores 
between individuals who developed PTSD and those who 
did not (Figs. 5, 6, 7).

Assessment of biological significance among Important 
CpGs

Gene  ontology  (GO)  analysis  on  the  set  of  3728  CpGs 
from  models  1  and  2  revealed  403  nominally  significant 
GO terms; among the 4150 important CpGs from Model 
3,  382  nominally  significant  GO  terms  were  identi-
fied. There  were  115  GO  terms  common  between  mod-
els,  including  regulation  of  muscle  adaptation,  positive 
regulation  of  autophagy  of  mitochondrion,  and  sucrose 
metabolic process. Additionally, the Kyoto Encyclopedia 
of  Genes  and  Genomes  (KEGG)  pathway  analysis  iden-
tified  47  pathways  for  models  1  and  2  and  25  pathways 
for  model  3  at  p < 0.05  (list  of  GO  and  KEGG  terms  are 
provided in Supplementary File 2). Further, 14 pathways 
were common in models 1 and 2, and model 3, including, 
HIF-1 signaling pathway, mTOR signaling pathway, Insu-
lin  signaling  pathway  and  Galactose  metabolism.  None 
of the GO terms or KEGG pathways passed the multiple 
hypothesis correction test.

Discussion
It is crucial to identify individuals who are at a higher risk 
of developing PTSD in order to provide timely preventive 
measures  and  effective  therapeutic  interventions.  MRS 
offer  dynamic  and  modifiable  genomic-based  insights 
into  disease  risk.  In  this  study,  we  leveraged  machine 
learning and a diverse set of cohorts to develop MRS for 
PTSD, with an initial aim of distinguishing those with vs. 

Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 9 of 14

Fig. 5  Distribution and difference in risk scores (eMRS) between PTSD cases and controls pre‑ and post‑deployment (N = 262) — in figure legend, 
0 is No PTSD and 1 is PTSD. A) The distribution of risk scores revealed that individuals who developed PTSD post‑deployment had higher scores 
compared to those who did not, both before and after deployment. B) The difference in risk scores showed there was a significant (p < 0.001) 
difference in risk scores in those with PTSD post‑deployment using Wilcoxon test

without PTSD and, subsequently to predict future PTSD 
cases.  MRS  derived  from  three  different  models  dem-
onstrated both high precision and high accuracy in pre-
dicting  PTSD  (i.e.,  identifying  probable  PTSD  cases  vs. 
controls)  in  the  test  dataset  and,  moreover,  significantly 
predicted  future  PTSD.  Although  our  approach  did  not 
yield MRS that consistently predicted PTSD in independ-
ent  cohorts,  our  work  leverages  data  from  a  diverse  set 
of cohorts to develop what is, to our knowledge, the first 
methylation-based  risk  scores  for  PTSD.  Future  work 
that builds on this approach will help to advance person-
alized preventive strategies and therapeutic interventions 
for PTSD in order to reduce the impact of this debilitat-
ing disorder on individuals and society.

Among  the  three  models  tested,  the  eMRS  model 
showed  the  highest  accuracy  and  precision  to  classify 
PTSD by using both exposure and DNAm variables. The 
inclusion  of  exposure  variables  substantially  adds  to  the 
predictive  power  of  the  model.  This  finding  aligns  with 
the  literature  that  suggests  that  experiencing  trauma, 
particularly during childhood, significantly increases the 
likelihood  of  developing  PTSD  [47,  53,  54].  It  is  note-
worthy  that,  despite  not  including  any  trauma  expo-
sure factors, the second model (MoRS) and third model 

(MoRSAE) that solely utilized methylation data in train-
ing  still  displayed  notable  predictive  ability  in  the  test 
dataset.  These  findings  suggest  that,  even  without  using 
trauma  variables  in  prediction,  DNAm  can  still  provide 
significant predictive information about PTSD. This also 
emphasizes  the  significant  impact  that  trauma  can  have 
on  the  epigenetic  landscape,  which  is  consistent  with 
other  research  studies  [55,  56]  that  reported  methyla-
tion differences linked to trauma. Overall, the decrease in 
classification accuracy across the models in the test data-
set,  from  eMRS  to  MoRSAE,  highlights  the  crucial  role 
and discriminatory power that both DNAm and trauma 
exposure have in classifying PTSD.

Our  attempts  to  validate  the  three  models  showed 
variable  results  across  models  and  cohorts.  The  eMRS 
significantly predicted PTSD in one cohort, BEAR, with 
the  same  direction  of  effect  as  in  the  discovery  cohort; 
the  MoRSAE  approached  significance  in  predicting 
PTSD  (p = 0.05)  in  the  NCPTSD-TRACTS  cohort  for 
MoRSAE,  although  with  an  opposite  direction  of  effect 
to  the  discovery  cohort.  This  variability  may  be  due  to 
individual  differences  in  the  type  or  severity  of  trauma 
in  each  cohort.  For  example,  similar  to  the  discovery 
sample,  the  BEAR  cohort  showed  significantly  higher 

 Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 10 of 14

Fig. 6  Distribution and difference in risk scores (MoRS) between cases and controls pre‑ and post‑deployment (N = 262) — in figure legend, 0 is No 
PTSD and 1 is PTSD. A) Distribution of risk scores between cases and controls. Risk scores are higher in those who developed PTSD post‑deployment 
than who didn’t in both pre and post deployment. B) Difference in risk scores between cases and controls. Wilcoxon test showed a significant 
difference (p < 0.001) in risk scores between cases and controls

levels  of  both  cumulative  and  childhood  trauma  in  par-
ticipants with vs. without PTSD—a pattern not observed 
in  any  of  the  other  three  validation  cohorts  (Table  S1). 
While we attempted to account for variability in trauma 
exposure  by  regressing  out  these  effects  in  our  MoR-
SAE  model,  this  did  not  improve  the  validation  results. 
These results suggest that it may be necessary to develop 
a  trauma-specific  MRS  in  order  to  more  precisely  cap-
ture  the  influence  of  trauma,  and  its  variability,  in  rela-
tion  to  classification  and  prediction  of  PTSD  risk  that 
generalizes across cohorts. We acknowledge that smaller 
sample  sizes  like  the  BEAR  cohort  can  increase  the  risk 
of  false  positives.  Still,  the  significant  correlation  and 
prediction results suggest that the observed strong asso-
ciation between eMRS and PTSD in the BEAR cohort is 
less  likely  due  to  chance  alone.  We  emphasize  the  need 
for  future  studies  with  larger  discovery  and  validation 
datasets to confirm our findings and further explore the 
observed association.

The ability to predict PTSD prior to deployment is par-
ticularly  important,  as  deployment  is  linked  to  a  higher 
probability  of  trauma  exposure  than  typically  observed 

in community samples and higher trauma load increases 
risk  for  PTSD  [54].  All  three  models  significantly  pre-
dicted future development of PTSD based on pre-deploy-
ment data, which is notable because these data preceded 
trauma exposure and were not included in the training or 
testing phase of MRS model development. This suggests 
that  classification-based  MRS  may  be  useful  in  predict-
ing risk for future PTSD in populations with anticipated 
trauma exposure.

Previous work has leveraged DNAm data as one among 
many biomarker types included in risk score approaches 
to predicting PTSD [57, 58]. An earlier study focused on 
war zone-related PTSD identified a set of 343 candidate 
biomarkers,  of  which  98  were  DNAm  values  associated 
with particular genes [57]. From our identified list of sig-
nificant  CpGs  (3728  in  models  1  and  2),  cg16335858  in 
GYLTL1B  (Glycosyltransferase-like  1B)  was  previously 
identified as a biomarker in diagnosing war zone-related 
PTSD  [57].  From  the  list  of  4150  CpGs  (model  3),  one 
additional CpG, cg25448062 in FADS1 (Fatty acid desat-
urase  1)  was  identified  as  a  diagnostic  biomarker  in  the 
same  study.  A  subsequent  study  [58]  showed  prediction 

Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 11 of 14

Fig. 7  Distribution and difference in risk scores (MoRSAE) between cases and controls pre‑ and post‑deployment (N = 262) — in figure legend, 0 
is No PTSD and 1 is PTSD. A) The distribution of MoRSAE is higher in those who developed PTSD post‑deployment B) The difference in risk scores 
showed there was a significant (p < 0.001) difference in risk scores in those with PTSD post‑deployment using Wilcoxon test

of  post-deployment  PTSD  symptoms  with  the  best 
AUC  of  88%  and  CpGs  cg01208318  and  cg17137457  as 
top  predictors  but  none  of  these  were  replicated  in  our 
study. More broadly, it is interesting to note that, 4 CpGs 
(cg04583842,  cg04987734,  cg16758086  and  cg19719391) 
in  genes  BANP,  CDC42BPB,  CHD5  and  Intergenic 
respectively,  have  been  associated  with  PTSD  in  recent 
PGC  EWAS  meta-analyses  (Katrinli  et  al.,  submitted). 
Our  results  build  on  these  earlier  studies,  highlight-
ing novel CpGs that, when combined in a weighted, risk 
score format, may contribute to PTSD prediction.

In this study, there were no results from GO or KEGG 
pathway  analyses  that  remained  significant  following 
multiple hypothesis testing; however, the GO terms and 
KEGG pathways shared among the three models provide 
interesting  clues  about  the  biological  mechanisms  that 
may be involved in the development of PTSD. For exam-
ple,  positive  regulation  of  autophagy  of  mitochondrion, 
identified as nominally significant biological processes in 
all three models, is noteworthy, as prior research has sug-
gested  that  autophagy  plays  a  role  in  neurodegenerative 
illnesses  [59–61],  and  exploring  its  connection  to  PTSD 
could provide insights into the disorder’s neurobiological 

underpinnings.  Additionally,  the  link  to  sucrose  meta-
bolic  process  is  intriguing  and  raises  questions  about 
the  relationship  between  energy  metabolism  and  stress 
responses [61], as metabolic disorders have been associ-
ated  with  PTSD  [63].  KEGG  pathway  analyses  revealed 
additional  implicated  pathways,  including  mTOR  and 
insulin  signaling,  which  play  a  crucial  role  in  cellular 
growth and metabolism, highlighting the extensive physi-
ological  effects  of  PTSD  beyond  psychological  distress 
[63, 64].

Our  study  is  not  without  limitations.  Chief  among 
these  is  our  external  validation  results,  which  showed 
validation for only one model in one of the four cohorts 
tested. To date, attempts to validate risk scores in exter-
nal, independent cohorts–as done in this study–are not 
common, and most work focusses on reporting results 
based on validation in a test (i.e., internal) dataset [14]. 
Results  from  this  work  highlight  the  need  to  increase 
efforts to do so, in order to arrive at robust, generaliz-
able MRS with the potential for future clinical applica-
tion. While our three classification-based MRS models 
showed good prediction of future PTSD in pre-deploy-
ment  data,  it  is  unclear  whether  they  would  perform 

 Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 12 of 14

as  well  in  predicting  future  PTSD  in  civilian  popula-
tions.  As  more  data  become  available,  the  inclusion  of 
additional  molecular,  environmental,  and  psychosocial 
factors  in  MRS  scores  may  enhance  their  accuracy  in 
predicting  the  condition  and,  relatedly,  improve  their 
performance in independent cohorts.

Supplementary Information
The online version contains supplementary material available at https:// doi. 
org/ 10. 1186/ s12920‑ 024‑ 02002‑6.

Supplementary Material 1.

Supplementary Material 2.

Authors’ contributions
PGC‑PTSD writing group: N.P.D., S.K., M.W.L., C.M.N., N.R.N., A.K.S., M.B.S., M.U., 
A.H.W., E.B.W., A.S.Z., and X.Z. Study PI or co‑PI: A.E.A., D.G.B., C.F., E.G., R.C.K., 
M.W.L., W.M., M.W.M., C.M.N., N.R.N., S.A.M.R., K.J.R., V.R., A.K.S., D.J.S., M.B.S., M.U., 
R.J.U., E.V., D.E.W., and E.J.W. Obtained funding for studies: M.P.B., C.F., E.G., R.C.K., 
M.W.L., J.J.L., C.M.N., N.R.N., S.A.M.R., K.J.R., B.P.F.R., A.K.S., M.U., R.J.U., and E.V. Clini‑
cal: C.F., E.G., J.P.H., N.K., S.A.M.R., K.J.R., M.H.V., E.V., and E.J.W. Contributed data: 
C.F., J.P.H., S.K., A.P.K., I.L., A.L, J.J.L., W.M., M.W.M., C.M.N., N.R.N., S.A.M.R., A.K.S., 
M.B.S., M.H.V., and E.J.W. Statistical analysis: M.P.B., L.B., C.‑Y.C., S.D., S.K., A.P.K., I.L., 
M.W.L., A.X.M., M.S.M., C.M.N., B.P.F.R., A.K.S., C.H.V., A.H.W., E.B.W., and X.Z. Bioin‑
formatics: M.P.B., L.B., C.‑Y.C., S.K., M.W.L., A.X.M., B.P.F.R., and X.Z. Genomics: M.P.B., 
B.P.F.R., and C.H.V. PI of the EWAS group: M.W.L., C.M.N., A.K.S., and M.U.

Funding
This work was supported by the National Institutes of Health (R01MD011728 
to MU, DW, AEA, R01MH108826 to AKS, MWL, CMN, MU and R01MH106595 to 
CMN, KCK, KJR and MBS). Army STARRS was sponsored by the Department of 
the Army and funded under cooperative agreement number U01MH087981 
with the U.S. Department of Health and Human Services, National Institutes 
of Health, National Institute of Mental Health (NIH/NIMH) to co‑PIs Robert J. 
Ursano and Murray B. Stein. NCPTSD‑TRACTS was supported by Translational 
Research Center for TBI and Stress Disorders (TRACTS), a VA Rehabilitation 
Research and Development Traumatic Brain Injury National Research Center 
(B3001‑C) to CF, and RF1AG068121 to EW. DCHS was supported by the Bill 
and Melinda Gates Foundation (OPP 1017641). Additional support for DJS and 
NK was provided by the South African Medical Research Council. The BEAR 
cohort was supported by R01MH105379 to NRN. The PROGrESS Cohort was 
supported by DOD #W81XWH‑11–1‑0073 to SMR and by the National Center 
for Advancing Translational Sciences of the NIH Award #UL1TR000433 to GAM. 
Data collection of PRISMO was funded by the Dutch Ministry of Defense, and 
DNAm analyses were funded by the VIDI Award fellowship from the Nether‑
lands Organization for Scientific Research (NWO, grant number 917.18.336 to 
BPFR). SK was supported by NIH BIRCWH K12HD085850. APK was supported 
by K23 MH112852. VBR was supported by VA Merit Award BX005872. EW was 
additionally supported by Merit Review Award Number I01 CX‑001276–01 
from the U.S. Dept. of Veterans Affairs CSRD Service.

Availability of data and materials
Owing to military cohort data sharing restrictions, data from MRS I& II, Army 
STARRS, PRISMO, and NCPTSD‑TRACTS cannot be publicly posted. For other 
cohorts, individual‑level data from the cohorts or cohort‑level summary 
statistics may be made available to researchers following an approved analysis 
proposal through the PGC Post‑traumatic Stress Disorder EWAS group with 
agreement of the cohort PIs. For additional information on access to these 
data, including PI contact information for the contributing cohorts, please 
contact the corresponding author.

Declarations

Ethics approval and consent to participate
All participants included in analyses of the discovery and external validation 
cohorts provided informed consent for their participation. Details on the 

specific IRB approval associated with each study are provided in the Sup‑
plementary Material.

Consent for publication
Not applicable.

Competing interests
Murray B. Stein has in the past 3 years received consulting income from Acadia 
Pharmaceuticals, Aptinyx, atai Life Sciences, BigHealth, Biogen, Bionomics, 
BioXcel Therapeutics, Boehringer Ingelheim, Clexio, Delix Therapeutics, Eisai, 
EmpowerPharm, Engrail Therapeutics, Janssen, Jazz Pharmaceuticals, Neu‑
roTrauma Sciences, PureTech Health, Sage Therapeutics, Sumitomo Pharma, 
and Roche/Genentech. Dr. Stein has stock options in Oxeia Biopharmaceuti‑
cals and EpiVario. He has been paid for his editorial work on Depression and 
Anxiety (Editor‑in‑Chief ), Biological Psychiatry (Deputy Editor), and UpToDate 
(Co‑Editor‑in‑Chief for Psychiatry). He has also received research support from 
NIH, Department of Veterans Affairs, and the Department of Defense. He is on 
the scientific advisory board for the Brain and Behavior Research Foundation 
and the Anxiety and Depression Association of America. Dr. Chia‑Yen Chen 
is an employee of Biogen. Dr. Nikolaos P. Daskalakis has served on scientific 
advisory boards for BioVie Pharma, Circular Genomics and Sentio Solutions 
for unrelated work. Dr. Nicole R. Nugent is a member of the scientific advisory 
board for Ilumivu. Dr. Sheila Rauch support from Wounded Warrior Project 
(WWP), Department of Veterans Affairs (VA), National Institute of Health (NIH), 
McCormick Foundation, Tonix Pharmaceuticals, Woodruff Foundation, and 
Department of Defense (DOD). Dr. Rauch also receives royalties from Oxford 
University Press and American Psychological Association Press. Dr Ressler 
reported receiving personal consulting fees from Sage Therapeutics, Senseye, 
Boerhinger Ingelheim, Jazz Pharmaceuticals, and Acer, Inc. and a sponsored 
research grant from Alto Neuroscience outside the submitted work.

Author details
1 Genomics Program, College of Public Health, University of South Florida, 
Tampa, FL, USA. 2 Department of Gynecology and Obstetrics, Emory University, 
Atlanta, GA, USA. 3 Department of Biostatistics, Boston University School 
of Public Health, Boston, MA, USA. 4 Broad Institute of MIT and Harvard, Stanley 
Center for Psychiatric Research, Cambridge, MA, USA. 5 Department of Psychia‑
try, Harvard Medical School, Boston, MA, USA. 6 Center of Excellence in Depres‑
sion and Anxiety Disorders, McLean Hospital, Belmont, MA, USA. 7 University 
of North Carolina at Chapel Hill, Carolina Stress Initiative, Chapel Hill, NC, USA. 
8 Department of Genetics, University of North Carolina at Chapel Hill, Chapel 
Hill, NC, USA. 9 Department of Psychiatry, University of North Carolina at Chapel 
Hill, Chapel Hill, NC, USA. 10 Institute for Trauma Recovery, University of North 
Carolina at Chapel Hill, Chapel Hill, NC, USA. 11 Robert N Butler Columbia Aging 
Center, Department of Epidemiology, Columbia University, New York, NY, 
USA. 12 Department of Psychiatry, University of California San Diego, La Jolla, 
CA, USA. 13 Veterans Affairs San Diego Healthcare System, Center of Excel‑
lence for Stress and Mental Health, San Diego, CA, USA. 14 Veterans Affairs San 
Diego Healthcare System, Psychiatry Service, San Diego, CA, USA. 15 Depart‑
ment of Psychiatry, Brain Center University Medical Center Utrecht, Utrecht, 
UT, Netherlands. 16 Department of Psychiatry and Human Behavior, Warren 
Alpert Medical School of Brown University, Providence, RI, USA. 17 Biogen Inc., 
Translational Sciences, Cambridge, MA, USA. 18 Department of Pathology, 
University of Cape Town, Cape Town, Western Province, South Africa. 19 Division 
of Human Genetics, University of Cape Town, Cape Town, Western Province, 
South Africa. 20 VA Boston Healthcare System, TRACTS/GRECC, Boston, MA, 
USA. 21 Brain Research and Innovation Centre, Netherlands Ministry of Defence, 
Utrecht, UT, Netherlands. 22 Department of Psychiatry, UMC Utrecht Brain 
Center Rudolf Magnus, Utrecht, UT, Netherlands. 23 Department of Psychol‑
ogy, The Ohio State University, Columbus, OH, USA. 24 Department of Health 
Care Policy, Harvard Medical School, Boston, MA, USA. 25 The Ohio State 
University, College of Medicine, Institute for Behavioral Medicine Research, 
Columbus, OH, USA. 26 Department of Psychiatry & Mental Health, University 
of Cape Town, Cape Town, Western Province, South Africa. 27 University of Cape 
Town, Neuroscience Institute, Cape Town, Western Province, South Africa. 
28 SA MRC Unit On Risk & Resilience in Mental Disorders, University of Cape 
Town, Cape Town, Western Province, South Africa. 29 Department of Psychiatry 
and Behavioral Sciences, Texas A&M University College of Medicine, Bryan, TX, 
USA. 30 Department of Psychiatry and Behavioral Sciences, Emory University, 
Atlanta, GA, USA. 31 Department of Translational Neuroscience, UMC Utrecht 
Brain Center Rudolf Magnus, Utrecht, UT, Netherlands. 32 Veterans Affairs San 

Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 13 of 14

Diego Healthcare System, Research Service, San Diego, CA, USA. 33 VA Boston 
Healthcare System, GRECC/TRACTS, Boston, MA, USA. 34 Boston University 
School of Medicine, Psychiatry, Boston, MA, USA. 35 VA Boston Healthcare 
System, National Center for PTSD, Boston, MA, USA. 36 Department of Psy‑
chiatry and Mental Health, University of Cape Town, Cape Town, Western 
Province, South Africa. 37 Department of Emergency Medicine, Warren Alpert 
Brown Medical School, Providence, RI, USA. 38 Department of Pediatrics, 
Warren Alpert Brown Medical School, Providence, RI, USA. 39 Department 
of Psychiatry and Human Behavior, Warren Alpert Brown Medical School, 
Providence, RI, USA. 40 Department of Psychiatry & Behavioral Sciences, Emory 
University, Atlanta, GA, USA. 41 Joseph Maxwell Cleland Atlanta Veterans Affairs 
Medical Center, Mental Health Service Line, Atlanta, USA. 42 McLean Hospital, 
Belmont, MA, USA. 43 School for Mental Health and Neuroscience, Department 
of Psychiatry and Neuropsychology, Maastricht Universitair Medisch Centrum, 
Maastricht, Limburg, Netherlands. 44 School of Public Health, University of Cali‑
fornia San Diego, La Jolla, CA, USA. 45 Department of Psychiatry, Uniformed 
Services University, Bethesda, MD, USA. 46 Department of Psychiatry, Boston 
University School of Medicine, Boston, MA, USA. 47 VA Boston Healthcare 
System, Memory Disorders Research Center, Boston, MA, USA. 48 Department 
of Psychiatry, Leiden University Medical Center, Leiden, ZH, Netherlands. 
49 Department of Psychiatry, New York University School of Medicine, New 
York, NY, USA. 50 Amsterdam Neuroscience, Mood, Anxiety, Psychosis, Sleep & 
Stress Program, Amsterdam, Holland, Netherlands. 51 Department of Anatomy 
and Neurosciences, Amsterdam UMC Location Vrije Universiteit Amsterdam, 
Amsterdam, Holland, Netherlands. 52 Department of Psychiatry, Amsterdam 
UMC Location Vrije Universiteit Amsterdam, Amsterdam, Holland, Netherlands. 
53 Survey Research Center, University of Michigan, Institute for Social Research, 
Ann Arbor, MI, USA. 54 Department of Psychiatry, Boston University Chobanian 
& Avedisian School of Medicine, Boston, MA, USA. 55 Boston University School 
of Medicine, Psychiatry, Biomedical Genetics, Boston, MA, USA. 56 Department 
of Human Genetics, Emory University, Atlanta, GA, USA. 

Received: 12 February 2024   Accepted: 29 August 2024

References
 1.  Kessler RC, Aguilar‑Gaxiola S, Alonso J, Benjet C, Bromet EJ, Cardoso G, 
et al. Trauma and PTSD in the WHO world mental health surveys. Eur J 
Psychotraumatol. 2017;8(sup5):1353383.

 2.  Yehuda R, Hoge CW, McFarlane AC, Vermetten E, Lanius RA, Niev‑

ergelt CM, et al. Post‑traumatic stress disorder. Nat Rev Dis Primers. 
2015;1(1):15057.

 3.  Kessler RC, Sonnega A, Bromet E, Hughes M, Nelson CB. Posttraumatic 

stress disorder in the National Comorbidity Survey. Arch Gen Psychiatry. 
1995;52(12):1048–60.

 4.  Kulka RA, Schlenger WE, Fairbank JA, Hough RL, Jordan BK, Marmar CR, 
et al. Trauma and the Vietnam war generation: Report of findings from 
the National Vietnam Veterans Readjustment Study. Philadelphia: Brun‑
ner/Mazel; 1990. xxix, 322‑xxix, p.

 5.  Brady KT, Killeen TK, Brewerton T, Lucerini S. Comorbidity of psychi‑
atric disorders and posttraumatic stress disorder. J Clin Psychiatry. 
2000;61(Suppl 7):22–32.

 6.  Kessler RC, Wang PS. The descriptive epidemiology of commonly 

 7. 

occurring mental disorders in the United States. Ann Rev Public Health. 
2008;29(1):115–29.
Lohr JB, Palmer BW, Eidt CA, Aailaboyina S, Mausbach BT, Wolkowitz 
OM, et al. Is post‑traumatic stress disorder associated with prema‑
ture senescence? A review of the literature. Am J Geriatr Psychiatry. 
2015;23(7):709–25.

 8.  Katrinli S, Stevens J, Wani AH, Lori A, Kilaru V, van Rooij SJH, et al. Evaluat‑
ing the impact of trauma and PTSD on epigenetic prediction of lifespan 
and neural integrity. Neuropsychopharmacology. 2020;45(10):1609–16.
 9.  Rosenbaum S, Stubbs B, Ward PB, Steel Z, Lederman O, Vancampfort D. 

The prevalence and risk of metabolic syndrome and its components 
among people with posttraumatic stress disorder: a systematic review 
and meta‑analysis. Metabolism. 2015;64(8):926–33.

 10.  Dedert EA, Calhoun PS, Watkins LL, Sherwood A, Beckham JC. Posttrau‑
matic stress disorder, cardiovascular, and metabolic disease: a review of 
the evidence. Ann Behav Med. 2010;39(1):61–78.

 11.  Pacella ML, Hruska B, Delahanty DL. The physical health consequences 
of PTSD and PTSD symptoms: a meta‑analytic review. J Anxiety Disord. 
2013;27(1):33–46.

 12.  Davis LL, Schein J, Cloutier M, Gagnon‑Sanschagrin P, Maitland J, 

Urganus A, et al. The economic burden of posttraumatic stress 
disorder in the united states from a societal perspective. J Clin 
Psychiatry. 2022;83(3):21m14116.

 13.  Lambert SA, Abraham G, Inouye M. Towards clinical utility of polygenic 

risk scores. Hum Mol Genet. 2019;28(R2):R133–42.

 14.  Yousefi PD, Suderman M, Langdon R, Whitehurst O, Davey Smith G, 

Relton CL. DNA methylation‑based predictors of health: applications and 
statistical considerations. Nat Rev Genet. 2022;23(6):369–83.

 15.  Huls A, Czamara D. Methodological challenges in constructing DNA 

methylation risk scores. Epigenetics. 2020;15(1–2):1–11.

 16.  Nabais MF, Gadd DA, Hannon E, Mill J, McRae AF, Wray NR. An overview of 
DNA methylation‑derived trait score methods and applications. Genome 
Biol. 2023;24(1):28.

 17.  Thompson M, Hill BL, Rakocz N, Chiang JN, Geschwind D, Sankarara‑

man S, et al. Methylation risk scores are associated with a collection of 
phenotypes within electronic health record systems. NPJ Genom Med. 
2022;7(1):50.

 18.  McCartney DL, Hillary RF, Stevenson AJ, Ritchie SJ, Walker RM, Zhang Q, 
et al. Epigenetic prediction of complex traits and death. Genome Biol. 
2018;19(1):136.

 19.  Clark SL, Hattab MW, Chan RF, Shabalin AA, Han LKM, Zhao M, et al. 

A methylation study of long‑term depression risk. Mol Psychiatry. 
2020;25(6):1334–43.

 20.  Aryee MJ, Jaffe AE, Corrada‑Bravo H, Ladd‑Acosta C, Feinberg AP, Hansen 
KD, et al. Minfi: a flexible and comprehensive Bioconductor package for 
the analysis of Infinium DNA methylation microarrays. Bioinformatics. 
2014;30(10):1363–9.

 21.  Katrinli S, Maihofer AX, Wani AH, Pfeiffer JR, Ketema E, Ratanatharathorn A, 

et al. Epigenome‑wide meta‑analysis of PTSD symptom severity in three 
military cohorts implicates DNA methylation changes in genes involved 
in immune system and oxidative stress. Mol Psych. 2022;27(3):1720–28.

 22.  Johnson WE, Li C, Rabinovic A. Adjusting batch effects in microar‑
ray expression data using empirical Bayes methods. Biostatistics. 
2006;8(1):118–27.

 23.  Leek JT, Johnson WE, Parker HS, Jaffe AE, Storey JD. The sva package for 
removing batch effects and other unwanted variation in high‑through‑
put experiments. Bioinformatics (Oxford, England). 2012;28(6):882–3.
 24.  Ambatipudi S, Cuenin C, Hernandez‑Vargas H, Ghantous A, Le Calvez‑

Kelm F, Kaaks R, et al. Tobacco smoking‑associated genome‑wide DNA 
methylation changes in the EPIC study. Epigenomics. 2016;8(5):599–618.

 25.  Besingi W, Johansson ÅJ. Smoke‑related DNA methylation changes in the 

etiology of human disease. Hum Mol Genet. 2014;23(9):2290–7.
 26.  Breitling LP, Yang R, Korn B, Burwinkel B, Brenner H. Tobacco‑smoking‑

related differential DNA methylation: 27K discovery and replication. Am J 
Hum Genet. 2011;88(4):450–7.

 27.  Guida F, Sandanger TM, Castagné R, Campanella G, Polidoro S, Palli D, 

et al. Dynamics of smoking‑induced genome‑wide methylation changes 
with time since smoking cessation. Hum Mol Genet. 2015;24(8):2349–59.

 28.  Joehanes R, Just AC, Marioni RE, Pilling LC, Reynolds LM, Mandaviya PR, 
et al. Epigenetic signatures of cigarette smoking. Circ Cardiovasc Genet. 
2016;9(5):436–47.

 29.  Zong D, Liu X, Li J, Ouyang R, Chen P. The role of cigarette smoke‑

induced epigenetic alterations in inflammation. Epigenetics Chromatin. 
2019;12(1):65.

 30.  Li S, Wong EM, Bui M, Nguyen TL, Joo J‑HE, Stone J, et al. Causal effect 

of smoking on DNA methylation in peripheral blood: a twin and family 
study. Clin Epigenet. 2018;10:18.

 31.  Jaffe AE, Irizarry RA. Accounting for cellular heterogeneity is critical in 
epigenome‑wide association studies. Genome Biol. 2014;15(2):R31‑R.

 32.  Houseman EA, Accomando WP, Koestler DC, Christensen BC, Marsit CJ, 
Nelson HH, et al. DNA methylation arrays as surrogate measures of cell 
mixture distribution. BMC Bioinformatics. 2012;13:86.

 33.  Reinius LE, Acevedo N, Joerink M, Pershagen G, Dahlén SE, Greco D, et al. 
Differential DNA methylation in purified human blood cells: implica‑
tions for cell lineage and studies on disease susceptibility. PLoS ONE. 
2012;7(7):e41361.

 Wani et al. BMC Medical Genomics          (2024) 17:235 

Page 14 of 14

 34.  Salas LA, Koestler DC, Butler RA, Hansen HM, Wiencke JK, Kelsey KT, et al. 
An optimized library for reference‑based deconvolution of whole‑blood 
biospecimens assayed using the Illumina HumanMethylationEPIC Bead‑
Array. Genome Biol. 2018;19(1):64.

 35.  Teschendorff AE, Breeze CE, Zheng SC, Beck S. A comparison of 

reference‑based algorithms for correcting cell‑type heterogeneity in 
epigenome‑wide association studies. BMC Bioinformatics. 2017;18(1):105.

 36.  Adkins RM, Krushkal J, Tylavsky FA, Thomas F. Racial differences in gene‑
specific DNA methylation levels are present at birth. Birth Defects Res A. 
2011;91(8):728–36.

 37.  Heyn H, Moran S, Hernando‑Herraez I, Sayols S, Gomez A, Sandoval J, 

et al. DNA methylation contributes to natural human variation. Genome 
Res. 2013;23(9):1363–72.

epigenetic profiles in posttraumatic stress disorder. Proc Natl Acad Sci 
USA. 2013;110(20):8302–7.

 56.  Uddin M, Aiello AE, Wildman DE, Koenen KC, Pawelec G, de Los SR, et al. 
Epigenetic and immune function profiles associated with posttraumatic 
stress disorder. Proc Natl Acad Sci USA. 2010;107(20):9470–5.

 57.  Dean KR, Hammamieh R, Mellon SH, Abu‑Amara D, Flory JD, Guffanti G, 
et al. Multi‑omic biomarker identification and validation for diagnos‑
ing warzone‑related post‑traumatic stress disorder. Mol Psychiatry. 
2020;25(12):3337–49.

 58.  Schultebraucks K, Qian M, Abu‑Amara D, Dean K, Laska E, Siegel C, et al. 
Pre‑deployment risk factors for PTSD in active‑duty personnel deployed 
to Afghanistan: a machine‑learning approach for analyzing multivariate 
predictors. Mol Psychiatry. 2021;26(9):5011–22.

 38.  Terry MB, Ferris JS, Pilsner R, Flom JD, Tehranifar P, Santella RM, et al. 

 59.  Guo F, Liu X, Cai H, Le W. Autophagy in neurodegenerative dis‑

eases: pathogenesis and therapy. Brain Pathol (Zurich, Switzerland). 
2018;28(1):3–13.

 60.  Nixon RA. The role of autophagy in neurodegenerative disease. Nat Med. 

2013;19(8):983–97.

 61.  Mizushima N, Levine B, Cuervo AM, Klionsky DJ. Autophagy fights disease 

through cellular self‑digestion. Nature. 2008;451(7182):1069–75.
 62.  Picard M, McManus MJ, Gray JD, Nasca C, Moffat C, Kopinski PK, et al. 

Mitochondrial functions modulate neuroendocrine, metabolic, inflam‑
matory, and transcriptional responses to acute psychological stress. Proc 
Natl Acad Sci USA. 2015;112(48):E6614–23.

 63.  Michopoulos V, Vester A, Neigh G. Posttraumatic stress disorder: A meta‑

bolic disorder in disguise? Exp Neurol. 2016;284(Pt B):220–9.

 64.  Ni L, Xu Y, Dong S, Kong Y, Wang H, Lu G, et al. The potential role of the 
HCN1 ion channel and BDNF‑mTOR signaling pathways and synaptic 
transmission in the alleviation of PTSD. Transl Psychiatry. 2020;10(1):101.

Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub‑
lished maps and institutional affiliations.

Genomic DNA methylation among women in a multiethnic New York 
City birth cohort. Cancer Epidemiol Biomark Prev. 2008;17(9):2306–10.
 39.  Nielsen DA, Hamon S, Yuferov V, Jackson C, Ho A, Ott J, et al. Ethnic diver‑
sity of DNA methylation in the OPRM1 promoter region in lymphocytes 
of heroin addicts. Hum Genet. 2010;127(6):639–49.

 40.  Husquin LT, Rotival M, Fagny M, Quach H, Zidane N, McEwen LM, et al. 
Exploring the genetic basis of human population differences in DNA 
methylation and their causal impact on immune gene regulation. 
Genome Biol. 2018;19(1):222.

 41.  Kwabi‑Addo B, Wang S, Chung W, Jelinek J, Patierno SR, Wang BD, et al. 
Identification of differentially methylated genes in normal prostate 
tissues from African American and Caucasian men. Clin Cancer Res. 
2010;16(14):3539–47.

 42.  Barfield RT, Almli LM, Kilaru V, Smith AK, Mercer KB, Duncan R, et al. 

Accounting for population stratification in DNA methylation studies. 
Genet Epidemiol. 2014;38(3):231–41.

 43.  Ratanatharathorn A, Boks MP, Maihofer AX, Aiello AE, Amstadter AB, 

Ashley‑Koch AE, et al. Epigenome‑wide association of PTSD from hetero‑
geneous cohorts with a common multi‑site analysis pipeline. Am J Med 
Genet B Neuropsychiatr Genet. 2017;174(6):619–30.

 44.  Jamshidian M, Mata M. 2 ‑ Advances in Analysis of Mean and Covariance 
Structure when Data are Incomplete**This research was supported in 
part by the National Science Foundation Grant DMS‑0437258. In: Lee S‑Y, 
editor. Handbook of Latent Variable and Related Models. Amsterdam: 
North‑Holland; 2007. p. 21–44.

 45.  Hasan MK, Alam MA, Roy S, Dutta A, Jawad MT, Das S. Missing value 
imputation affects the performance of machine learning: A review 
and analysis of the literature (2010–2021). Inform Med Unlocked. 
2021;27:100799.

 46.  Manduchi E, Fu W, Romano JD, Ruberto S, Moore JH. Embedding covari‑
ate adjustments in tree‑based automated machine learning for biomedi‑
cal big data analyses. BMC Bioinformatics. 2020;21(1):430.

 47.  Breslau N, Peterson EL, Schultz LR. A second look at prior trauma and the 
posttraumatic stress disorder effects of subsequent trauma: a prospective 
epidemiological study. Arch Gen Psychiatry. 2008;65(4):431–7.

 48.  Breslau N, Chilcoat HD, Kessler RC, Davis GC. Previous exposure to trauma 
and PTSD effects of subsequent trauma: results from the detroit area 
survey of trauma. Am J Psychiatry 1999;156(6):902–7.

 49.  Brady KT, Back SE. Childhood trauma, posttraumatic stress disorder, and 

alcohol dependence. Alcohol Res: Curr Rev. 2012;34(4):408–13.

 50.  LeardMann CA, Smith B, Ryan MAK. Do adverse childhood experiences 
increase the risk of postdeployment posttraumatic stress disorder in US 
Marines? BMC Public Health. 2010;10(1):437.

 51.  Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel O, 

et al. Scikit‑learn: Machine Learning in Python. J Mach Learn Res. 
2011;12:2825–30.

 52.  Phipson B, Maksimovic J, Oshlack A. missMethyl: an R package for analyz‑
ing data from Illumina’s HumanMethylation450 platform. Bioinformatics. 
2015;32(2):286–8.

 53.  McFarlane AC. Posttraumatic stress disorder: a model of the longitudinal 

course and the role of risk factors. J Clin Psych. 2000;61(Suppl 5):15–20 
discussion 1‑3.

 54.  Brewin CR, Andrews B, Valentine JD. Meta‑analysis of risk factors for 

posttraumatic stress disorder in trauma‑exposed adults. J Consult Clin 
Psychol. 2000;68(5):748–66.

 55.  Mehta D, Klengel T, Conneely KN, Smith AK, Altmann A, Pace TW, et al. 
Childhood maltreatment is associated with distinct genomic and
