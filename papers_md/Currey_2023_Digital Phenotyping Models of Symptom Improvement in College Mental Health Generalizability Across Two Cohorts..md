# Currey_2023_Digital Phenotyping Models of Symptom Improvement in College Mental Health Generalizability Across Two Cohorts.

Journal of Technology in Behavioral Science 
https://doi.org/10.1007/s41347-023-00310-9

Digital Phenotyping Models of Symptom Improvement in College 
Mental Health: Generalizability Across Two Cohorts

Danielle Currey1,2 · Ryan Hays1 · John Torous1 

Received: 13 April 2022 / Revised: 17 January 2023 / Accepted: 18 February 2023 
© The Author(s), under exclusive licence to Springer Nature Switzerland AG 2023

Abstract
Smartphones can be used to gain insight into mental health conditions through the collection of survey and sensor data. 
However, the external validity of this digital phenotyping data is still being explored, and there is a need to assess if predic-
tive models derived from this data are generalizable. The first dataset (V1) of 632 college students was collected between 
December 2020 and May 2021. The second dataset (V2) was collected using the same app between November and December 
2021 and included 66 students. Students in V1 could enroll in V2. The main difference between the V1 and V2 studies was 
that we focused on protocol methods in V2 to ensure digital phenotyping data had a lower degree of missing data than in the 
V1 dataset. We compared survey response counts and sensor data coverage across the two datasets. Additionally, we explored 
whether models trained to predict symptom survey improvement could generalize across datasets. Design changes in V2, 
such as a run-in period and data quality checks, resulted in significantly higher engagement and sensor data coverage. The 
best-performing model was able to predict a 50% change in mood with 28 days of data, and models were able to generalize 
across datasets. The similarities between the features in V1 and V2 suggest that our features are valid across time. In addi-
tion, models must be able to generalize to new populations to be used in practice, so our experiments provide an encouraging 
result toward the potential of personalized digital mental health care.

Keywords  College · Digital phenotyping · Smartphone · Depression · Anxiety · Stress

Abbreviations
PHQ-9 
GAD-7 
PSS 
UCLA 
PSQI 
PQ-16 
D-WAI 

 Patient Health Questionaire-9
 Generalized Anxiety Disorder-7
 Perceived Stress Scale
 UCLA Loneliness Survey
 Pittsburgh Sleep Quality Index
 Prodromal Questionaire-16
 Digital Working Alliance Inventory

Background

The recent rise in youth mental health needs continues to 
impact college mental health. Labeled as a crisis not only by 
the popular press media (Aslanian & Roth, 2021; Hartocollis 

 *  John Torous 

jtorous@bidmc.harvard.edu

1  Beth Israel Deaconess Medical Center, Harvard Medical 
School, 330 Brookline Ave, MA 02215 Boston, USA
2  Case Western Reserve University School of Medicine, 

Cleveland, OH, USA

2021) but also by the US Surgeon General (Murthy 2021) 
and  reflected  in  rising  rates  of  depression  and  anxiety 
(Eisenberg et al., 2020), college mental health requires new 
solutions. Technology, especially smartphone applications 
(apps), has been proposed as one promising solution, with 
the majority of counseling centers already recommending 
mental  health  apps  (Melcher  &  Torous, 2020)  and  new 
efforts expanding around COVID-19. However, the emerg-
ing evidence suggests that mental health apps are not yet 
impacting clinical outcomes (Goldberg et al., 2022), and 
uptake by college students is minimal (Lattie et al., 2021). 
Thus, understanding why smartphone apps today are not 
transforming college mental health and refocusing efforts 
to make them more appealing and practical for students is a 
pressing need for technology research.

Emerging data from the general population and college 
student studies presents a consistent picture of low uptake 
and  engagement.  For  example,  a  recent  study  offered 
access to an evidence-based app designed especially for 
college  mental  health,  but  of  50,000  eligible  students, 
only 117 downloaded the app (Lattie et al., 2021). Look-
ing at qualitative data, students want their mental health to 

Vol.:(0123456789)1 3 
consist of in-person care and are resistant to technology-
first approaches (Lattie et al., 2020; Smith et al., 2021). 
Students are interested in apps (Borghouts et al., 2021) but 
want them to be personalized to their needs and responsive 
to their mental state. But most apps, including those already 
recommended by college mental health centers, are neither 
personalized nor responsive.

However, apps can be both personalized and responsive, 
and emerging research suggests direct relevance to college 
mental health (Chikersal et al., 2021; Mack et al., 2021). This 
is possible by using smartphones as closed-loop systems that 
learn about the mental state of each student through real-time 
surveys and sensors (e.g., accelerometer to measure sleep 
duration) to create personalized and context-aware models 
of mental health. Sometimes referred to as digital pheno-
typing (Torous et al., 2016) or behavioral sensing (Mohr 
et al., 2020), these methods have already shown feasibility 
and promising correlations in studies with college students 
(Melcher et al., 2020; Melcher et al., 2021; Wang et al., 
2014). Successfully applied, digital phenotyping can be used 
as the tailoring variable in just-in-time adaptive interventions 
(Nahum-Shani et al., 2018) to offer app interventions that 
are more personalized, engaging, and effective than current 
offerings. A recent 2022 review noted this type of “intelligent 
automation” as a highly promising means to expand engage-
ment and scalability of apps (Lattie et al., 2021).

Toward realizing this potential of intelligent automation, 
it is first necessary to understand if results can replicate. 
While there have already been numerous studies examining 
digital phenotyping signals from college students (Melcher 
et al., 2020), the use of different apps, populations, study 
durations, and outcome measures precludes any quantita-
tive comparison between studies. Questions remain if digital 
signals found in one study or group of students can be rep-
licated in another. Furthermore, no studies have examined 
if predictive models of symptom change developed in one 
study are valid or generalizable when applied to another 
dataset, a necessary condition if seeking to offer personal-
ized models into mental health apps. For example, is a model 
that predicts future changes in depression scores based on 
smartphone-derived sleep metrics and surveys able to accu-
rately predict such changes in a different sample of students 
at a different time?

In this paper, we have two primary goals. First, using the 
same app, we explore college mental health digital pheno-
typing with two different datasets (V1 and V2) and explore 
how a study designed toward reducing the missingness of 
digital phenotyping can impact results. Second, we present 
models from V1 that can generalize and predict symptom 
improvement in a second dataset (V2). Along with our sec-
ond aim, we explore model performance across different 
subsets of the study population.

Journal of Technology in Behavioral Science

Methods

Data Sets

Two distinct datasets were used for this work, with com-
monalities and differences designed to facilitate questions 
around internal and external validity. Institutional Review 
Board approval was obtained through the Beth Israel Dea-
coness Medical Center Institutional Review Board, and all 
participants signed written informed consent.

Both  studies  utilized  the  open-source  mindLAMP 
app to collect active (survey) and passive (sensor) data 
from undergraduate student participants over the course 
of 1 month. mindLAMP was developed by the Division 
of Digital Psychiatry at Beth Israel Deaconess Medical 
Center and can administer surveys and collect sensor data 
(Torous et al., 2016). Use of the mindLAMP app in col-
lege students was informed by our review of apps available 
offered to college students (Melcher & Torous, 2020) and 
the pilot study of mindLAMP, which helped us ensure the 
app was usable and relevant (Melcher et al., 2020). The 
first study (V1) was collected between December 2020 and 
May 2021 (Patel & Torous 2022). In total, 632 participants 
logged into the app and were included in this analysis. The 
second study (V2) has never been reported on and aimed 
to recruit 100 students to also use the mindLAMP app 
for one month between November and December 2021. 
In both studies, participants were asked to complete daily 
surveys about their mental health on the app, enable con-
stant digital phenotyping by allowing access to sensor 
data, and complete weekly surveys also about their men-
tal health. We collected daily survey results as well as 
weekly to allow us to gain information about the day-to-
day fluctuations in mental health as well as larger changes 
on the weekly level. The passive data/sensors collected 
in both studies included GPS, accelerometer, and screen 
state. In both studies, participants were compensated for 
completing the weekly surveys during the 1st, 3rd, and 4th 
weeks of the study. No compensation was linked to digital 
phenotyping or daily surveys. Of note, those who partook 
in the V1 study were eligible to partake in the V2 study, 
given the two studies happened at different time periods.
Differences between the studies were primarily around 
enrollment and scheduling of interventions in the apps. In 
the V2 study, eligible participants were asked to complete 
a 3-day run-in period. During this run-in period, they were 
asked to (1) complete a single-item survey about interest 
in the study and (2) enable digital phenotyping through 
access to sensors on their smartphone. Only those partici-
pants who responded to a survey each of the 3 days and 
had phones able to collect passive data above a predeter-
mined threshold were deemed eligible to partake. In the 

1 3 
Journal of Technology in Behavioral Science 

V1 study, there was no run-in period. The purpose of this 
run-in period in the V2 study was to attempt to reduce 
missing data (both active and passive) and thus be able 
to build models with potentially higher-quality data. As 
an additional control for data quality, participants were 
discontinued from the study if they did not complete any 
activities in the app for 5 consecutive days. The second 
difference  was  that  in  the  V2  study,  participants  were 
asked to complete daily activities beyond the daily surveys 
in the app via the scheduling feed feature (see Appendix 
A for screenshots). They were asked to complete the same 
activities each day for a week. The first week included 
daily exercises around identifying negative thought pat-
terns, the second week was self-reflection through journ-
aling, the third was different mindfulness exercises, and 
the fourth was brain training/cognitive exercises. Each 
activity was designed to take an average of 5 min or less. 
Participants were told that they should complete these 
activities as they appeared in their daily feed, but activity 
completion was not compensated, and participants were 
not otherwise penalized for lack of engagement. Of note, 
in the V1 study, participants has equal access to the major-
ity of these same activities in the app, but they were not 
scheduled in the feed.

Features

Active Data Features

The weekly surveys included the Patient Health Question-
aire-9 (PHQ-9) (Kroenke et al., 2001), Generalized Anxi-
ety Disorder-7 (GAD-7) (Spitzer et al., 2006), Perceived 
Stress Scale (PSS) (Cohen et al., 1983), UCLA Loneliness 
Survey  (Russell, 1996),  Pittsburgh  Sleep  Quality  Index 
(PSQI) (Buysse et al., 1989), Prodromal Questionaire-16 
(Loewy et al., 2005), and Digital Working Alliance Inven-
tory (DWAI) (Goldberg et al., 2021). Both V1 and V2 had 
daily surveys consisting of a subset of the weekly questions. 
V2’s daily survey additionally had questions regarding sleep 
duration and quality, which were not included in this analy-
sis. A full list of daily and weekly questions can be found in 
Appendix B.1 and B.2.

Passive Data Features

From the raw passive data, several features were computed. This 
includes sleep duration from accelerometer data, screen duration 
from screen state, and home time and entropy from GPS data. 
As GPS data is one of the more variable features, it was used 
as a measure of the overall quality of the passive data (Kiang 
et al., 2021). The implementation of these features can be found 
on GitHub at https:// github. com/ BIDMC Digit alPsy chiat ry/ 
LAMP- cortex.

Comparison Between V1 and V2

The average of each passive and active data feature was 
computed to produce correlation matrices for V1 and V2. 
For passive data, days with values of zero or without data 
were excluded. P-values were corrected using the Hochberg 
method  via  the  statsmodels.stats.multitest.multipletests 
module in Python (Seabold & Perktold 2010). To better 
understand these matrices, hierarchical clustering of the 
correlations was performed using sklearn (Pedregosa et al., 
2011). Finally, as many features were not normally distrib-
uted, Mann–Whitney tests were performed to compare each 
feature in V1 to V2 using the scipy.stats module (Virtanen 
et al., 2020).

Cross‑Cohort Models

Logistic regression models were trained to predict improve-
ment in each of the weekly scores using all of the active and 
passive data features (listed in Appendix B). One challenge 
was to define “improvement” in a way that was reasonable 
for our cohort. Thus, only participants with a minimum start-
ing score of at least one and that completed at least two 
weekly surveys at least 7 days apart were included. Par-
ticipants with a starting score of zero (i.e., no symptoms) 
were excluded because they can only get worse; they can-
not improve and score below zero. Weekly surveys were 
required to be at least 7 days apart to ensure there was a 
reasonable amount to allow for changes in score. Ideally, 
weekly surveys would be 21 days apart (weeks 1 to 4), but 
especially for V1, many participants did not complete all 
weekly surveys. Thus, these criteria allowed us to include a 
larger sample in our analysis. Models were trained on both 
V1 and V2 and tested on the other data set. We compared 
inputting the average of each feature over the entirety of 
the study to the average over the first 10 days (for V2, this 
was the first 10 days excluding the trial period). Ten days 
was chosen as it is about a week of data but also includes 
participants that may have taken the second weekly survey 
late (between days 8 and 10). Participants who did not have 
data from all features were excluded. Output was compared 
between requiring an improvement/decrease of 25% and 50% 
in survey scores for PHQ-9, GAD-7, PSS, UCLA Loneli-
ness, PQ-16, and PSQI. The 50% threshold was chosen to 
align with standard definitions of response, and 25% as 
an intermediate response. Then, using an input of the first 
10 days of data and defining improvement as a 25% decrease 
in survey score, models were evaluated to determine if per-
formance differences existed among different subsets of the 
participants. The 25% threshold was chosen, as for some 
smaller subsets of the data, there were no members of both 
the improved / not improved class with the clinical threshold 
of 50% (Kroenke et al., 2001). Performance was compared 

1 3across participants with different living situations (living 
at home, on campus, or off-campus), different severity of 
depression based on starting PHQ-9 score (based on clinical 
standards (Kroenke et al., 2001)), and those that participated 
in both V1 and V2 versus those that only participated in one 
study. The Scikit-Learn LogisticRegression model was used 
with a l1_ratio of 0.5 (Pedregosa et al., 2011). Class weights 
were balanced, and all input features were standardized. Per-
formance was evaluated using AUC-ROC. We did not adjust 
for confounders given the pilot nature of this work.

Results

A total of 309 students were screened as eligible for the 
V2 study. Of these, 163 completed the informed consent 
process, and 150 registered for an account. In total, 53 were 
unable to complete the enrollment as they did not pass the 
run-in period. A total of 66 completed the study, with 30 
being discontinued for non-engagement and 0 lost to fol-
low-up. In total, 54 of the 96 participants enrolled had par-
ticipated in the V1 study, 40 of whom completed the study. 
Demographics of those who partook in the V1 and V2 stud-
ies are presented in Table 1. V1 and V2 participants had an 
average age of 21.5 ± 3.9 and 21.3 ± 3.9, respectively. The 
average PHQ-9 scores were 7.9 ± 5.3 for V1 and 8.0 ± 4.5 
for V2. The average GAD-7 scores were 6.7 ± 4.8 for V1 and 
7.3 ± 4.3 for V2. Demographics for the participants who did 
not complete the run-in period or were discontinued from 
V2 are shown in Appendix C.

Figure 1 shows the maps of the correlations between 
the features to compare the relationships between vari-
ables across V1 and V2. Dendrograms for both studies 
can be found in Appendix E. The similarity between the 
correlation maps indicates that even though data was col-
lected at two different time points with a different set of 
participants, the relationships between variables are main-
tained. As listed in Table 2, there are some differences 

Table 1   Race and gender in the college data sets

Journal of Technology in Behavioral Science

between the two datasets. Most notably, there are signifi-
cant differences between the number of activities com-
pleted and some of the passive data features. Participants 
in V2 completed significantly more activities (36 ± 9 vs. 
22 ± 12; p < 0.001), which makes sense as more activities 
were scheduled for this study compared to the V1 study. 
Therefore, we then evaluated the percentage of scheduled 
activities that were completed among the groups (Fig. 2). 
Considering the scheduled activities common to V1 and 
V2 (the weekly surveys and daily surveys), V2 participants 
completed significantly more (0.89 ± 0.17 vs. 0.66 ± 0.33; 
p < 0.001). However, if we consider all activities (includ-
ing module activities for V2), then V2 had a lower comple-
tion rate than V1 (0.66 ± 0.33 vs. 0.52 ± 0.16; p < 0.001). 
The number of unscheduled activities completed was not 
significantly different between V1 (1 ± 3) and V2 (1 ± 
1). V2 participants were also able to achieve significantly 
better passive data coverage (as measured by GPS) than 
in V1 (p < 0.001) (Fig. 2). Some survey questions as well 
as the home time, screen duration, and sleep duration pas-
sive features were also significantly different between the 
groups (p < 0.05) (Appendix D). For the regression mod-
els to predict improvement on each of the weekly scores, 
Fig. 3 shows that most survey models trained on 28 days 
of data and with an improvement threshold of 50% had 
the highest average area under the curve (AUC) (0.748).

Finally, Fig. 4 shows the performance differences across 
different sub-populations in the study. Specifically, models 
trained on the entire data set (V1 or V2) were then validated 
on subsets of the other study population. We hypothesized 
that certain subsets of the population, such as living situa-
tion and severity of depression, would have different model 
performances as a model trained on the population may not 
capture the phenotype of certain subgroups. Figure 4a shows 
differences in living situations. There is a shift toward living 
on campus (as opposed to living at home or in an off-campus 
apartment) between V1 and V2, which makes sense as there 
were fewer quarantine restrictions during the V2 study.

Race

Female

Male

Nonbinary

Total

Female

Male

Nonbinary

Total

College V1

College V2

American Indian or Alaskan Native
Asian
African American
Latinx
Native Hawaiian/Pacific Islander
White
Other
Total

0
86
32
74
4
179
19
394

2
47
17
41
1
102
11
221

0
0
0
1
1
12
2
16

* One white participant in college V1 put “prefer not to say” for their gender

2
133
49
116
6
294*
32
632

0
15
1
3
1
26
0
46

0
5
0
2
0
12
0
19

0
0
0
0
0
1
0
1

0
20
1
5
1
39
0
66

1 3 
Journal of Technology in Behavioral Science 

Fig. 1   Correlation maps for 
all the features shared between 
colleges V1 and V2. a shows 
correlations for college V1 and 
b shows correlations for College 
V2. The corresponding numbers 
for questions and features are 
listed in Appendix B and C. The 
magnitude of the correlation is 
designated by the color shown 
in the bar to the right. Signifi-
cant correlations are denoted 
with * (p < 0.05)

1 3Journal of Technology in Behavioral Science

Table 2   Significantly different features between the colleges V1 and V2 data sets

Feature

P-value (corrected)

(PSS) In the last week, how often have you found that you could not cope with all the things that you had to do?
(PSS) In the past week, how often have you felt that you were on top of things?
UCLA
(UCLA) I have nobody to talk to
(UCLA) I cannot tolerate being so alone
(UCLA) I lack companionship
(UCLA) I find myself waiting for people to call or write
(UCLA) I feel isolated from others
(UCLA) I am unhappy being so withdrawn
(UCLA) I feel shut out and excluded by others
(PQ-16) I sometimes see special meanings in advertisements, shop windows, or in the way things are arranged around me
(PQ-16) I have had the sense that some person or force is around me, even though I could not see anyone
(PQ-16) I feel that parts of my body have changed in some way, or that parts of my body are working differently than 

0.04676
0.05145
0.02638
0.04676
0.04676
0.03270
0.00288
0.00608
0.04676
0.01190
0.04676
0.04676
0.003689

before

(PSQI) Component 5 (Appendix B, 68–74)
(DWAI) The app is easy to use and operate
Number of activities completed
Home time
Screen duration
Sleep duration
GPS data quality (coverage)

0.04676
5.640e − 6
1.021e − 34
5.141e − 6
7.570e − 24
0.00010
5.141e − 24

There are also differences in the performance of the 
models between the different groups. This makes sense 
as a participant’s experiences in different living situa-
tions likely impact their data. Similarly, the severity of 
PHQ-9 scores interacts with other surveys as symptoms 
may manifest differently based on levels of depression 
at the beginning of the study, as shown in Fig.  4b. In 
PSS and UCLA, the different PHQ-9 phenotypes result 

in  different  performances.  Finally,  in  Fig.  4c,  except 
for  PQ-16,  there  does  not  appear  to  be  a  large  differ-
ence between the performance of any model for V2. The 
results are more variable for models trained on V2 and 
tested on V1. Overall, although some participants com-
pleted both V1 and V2, models do not appear to perform 
differently on these participants versus those that only 
completed one study.

Fig. 2   a  Comparison  of  the  average  GPS  data  quality  (coverage) 
between V1 and V2. b Comparison of the percent of scheduled activ-
ities completed by each participant in colleges V1 and V2, including 

those common to both studies and unique to V2 (module activities). 
V1 is shown in orange, and V2 is in blue

1 3 
Journal of Technology in Behavioral Science 

Fig. 3   Comparison of AUC performance for models tested on college 
V1 (and trained on V2, shown in orange) and models tested on col-
lege  V2  (and  trained  on  V1,  shown  in  blue).  Each  graph  uses  input 
from either 10 or 28 days of data and predicts improvement of either 
25 or 50%. a shows 50% improvement for 28 days of input, b shows 

50% improvement for 10 days of input, c shows 25% improvement for 
28 days of input, and d shows 25% improvement for 10 days of input. 
The number of participants used for testing/training of each model is 
shown in Appendix F

Discussion

Comparison of Both Studies

The potential of smartphone apps to improve college mental 
health requires they become more personalized and respon-
sive. Toward this goal, our results highlight how predictive 
models of symptom change can be built with digital phe-
notyping data and demonstrate the potential for these types 
of models to be generalized across populations of students. 
Our transparent methods, open-source app, and reproducible 
study design offer a tangible mechanism for continued vali-
dation and improvement of these new digital phenotyping 
models for college mental health.

Results comparing both studies suggest numerous areas of 
overlap that suggest the external validity of digital phenotyp-
ing methods to quantify college mental health. The common 
correlations between both studies, shown in Fig. 1, imply that 
the features we have collected and engineered may be valid 
across studies. Differences in the correlations are not possible 
to explain with our methods but may reflect that the V2 study 
was conducted later in the pandemic when students were more 
likely to have been able to return to campus and attend in-
person activities. The differences in PQ-16 and PSQI questions 

1 3Journal of Technology in Behavioral Science

Fig. 4   a  Performance  of  participants  living  either  on  campus,  at 
home,  or  in  an  off-campus  apartment.  b  Performance  on  partici-
pants with low (0–5), medium (6–10), or high (> 10) starting PHQ-9 
scores.  c  Performance  on  participants  that  participated  in  both  stud-

ies  versus  those  that  only  completed  one  study.  The  left  column  of 
plots shows the counts of each group in each dataset, and plots to the 
right show the AUC for each group for models tested on college V1 
(orange) and V2 (blue)

are likely an effect of small differences in study populations. 
Most students do not exhibit prodromal symptoms.

The differences in passive data, however, are likely due 
to differences in study design. As sensors may be turned off 
after participants have not interacted with the app after sev-
eral days (due to Apple and Android smartphone operating 
systems), the lead-in period that was part of the V2 study, as 
well as efforts to ensure engagement at least every 5 days, 
resulted in passive data with less missingness. Additionally, 
backend updates to the app made between the two studies 
may have improved passive data capture. Although the differ-
ences in screen duration, home time, and sleep duration may 
be a result of lifestyle changes from earlier to later in the pan-
demic, it is plausible that the greater spread in the V1 study 
was a result of the lower data quality (Patel & Torous 2022).
Methods  in  the  V2  study  supported  higher  rates  of 
engagement. Participants in the V2 study completed sig-
nificantly more activities than those in V1, after controlling 
for all activities in the app that were the same in both studies, 
and had a significantly higher percent completion rate of the 
activities common between the studies. However, unsched-
uled activities were not different between V1 and V2 when 
including only activities in both studies. Thus, it is unclear 
the extent to which the lead-in period was responsible for 
the increase in engagement compared to the task feed. The 

lack of differences in participants’ working alliance toward 
the app between V1 and V2 suggests that these engagement 
features in the V2 study may be selecting for more exter-
nal vs internal motivators. We showed that we could obtain 
increased engagement and higher passive data quality in V2, 
but it is unclear how this higher-quality data may be impor-
tant or what the necessary threshold for data should be. Such 
standards are still lacking in the field.

Cross‑Cohort Models

Our results of generalizability of symptom prediction models 
between both studies offer evidence of external validity. We 
showed that models trained to predict improvement on each of 
the weekly scores in V1 study performed better than V2 study, 
although the results for V2 models predicting improvement 
on V1 were nearly similar. It is notable that the larger sample 
size dataset of V1, and not the higher quality dataset of V2, 
was superior here, with one explanation being that as a larger 
dataset, V1 offers a better representation of the underlying 
data distribution. Moreover, models trained on data from the 
entirety of the study perform better than those trained on data 
from the first 10 days, and the difference is minimal. In addi-
tion, performance is better with the improvement threshold 
at 50% compared to 25%. However, the 25% threshold for 

1 3 
Journal of Technology in Behavioral Science 

symptom reduction may be more practical for what an app 
is able to offer, as most participants will not expect a large 
improvement over the course of a short time.

The differences in performance shown in Fig. 4a and b 
indicate that there are differences in certain sub-populations 
that are not captured in a general model. Other studies have 
explored the idea that some demographic or other informa-
tion may be needed to allow the population to identify differ-
ences between populations (Liu et al., 2019). However, the 
fact that the model tested on V2 performs similarly on par-
ticipants that participated in both V1 and V2 as opposed to 
just one study is encouraging, as it indicates that the model 
can perform reasonably well on new participants. Gener-
alization is important because for models to be useful in 
practice, they must perform well on a wide set of features. 
Although there are differences in context and data between 
the two studies, this work demonstrates the potential of mod-
els to generalize across datasets. We are now aware of other 
digital phenotyping studies in college mental health that 
have sought to replicate their results (Melcher et al., 2020), 
and few digital phenotyping studies across all of the mental 
health currently offer generalizability results.

Limitations and Future Directions

There are several limitations of this work. First, we used the 
average of each feature for analysis, but the variance between 
survey scores or passive data over time may also be useful. 
Future work should explore using variance as well as aver-
ages for models. Moreover, the way that we defined improve-
ment for our models with 25 and 50% reduction may not be 
ideal to capture symptom change over time. Lower targets of 
even 10% symptom improvement may be more reasonable 
with the app used for self-help, and higher reductions like 
50% when the app is used in concert with clinical care. In 
addition, 10 days of data may not be the optimal amount to 
balance the practicality of using a shorter time window and 
the greater amount of information captured in a larger time 
period. In longer studies, this time window should be varied 
to determine the time delay between activities and improve-
ment and to maximize this balance. There was some overlap 
of students between both datasets, but being able to validate 
models across even the same students at different times still 
presents an important clinical target. Finally, we did not adjust 
for confounders given the pilot nature of this work.

remains  unclear  given  the  models  trained  on  V1  data 
outperformed those trained in V2 data. The next step in 
this work will be prospectively applying the models vali-
dated here to offer just-in-time adaptive interventions to 
college students toward assessing if this personalization 
can increase engagement and improve clinical metrics. 
Finally, this work was done based on two samples of col-
lege students. This group has many advantages, such as 
their comfort level with technology, that make them ideal 
candidates  for  digital  mental  health  studies,  but  future 
work should explore other age and demographic groups 
and should seek to explore generalizability across more 
diverse populations. Still, the rising unmet need for men-
tal health services does make this population important to 
study in itself.

Overall, we explored two college data sets and examined 
design choices such as a run-in period and scheduling activi-
ties that can improve passive and active data quality. We pre-
sented models to predict symptom improvement that were 
generalized across the two studies. Finally, we explored this 
generalization through different subsets of the data, showing 
that performance will change based on differences in the data. 
This work demonstrates the potential of building generaliz-
able models and the opportunity to next use them to tailor 
app-based care.

Appendix A

A.1

Screenshots of the mindLAMP activity feed each week for 
college V2. Each day has a morning daily survey. At the end 
of each week is the weekly survey, as shown in (b). (a) Week 
1: Thought patterns. The first day includes a tip on identifying 
thought patterns, and each day has the “Record, rationalize, 
replace” activity. (b) Week 2: Journaling. Journaling provides 
a free space for participants to write. (c) Week 3: Mindful-
ness. The first day includes a tip about mindfulness, and each 
day has a different breathing activity. (d) Week 4: Distraction 
games. Each day of the final week alternates between the jew-
els and spatial span games.

Appendix B

B.1

Conclusions

Our work also suggests fruitful next steps. While we were 
able to increase engagement and quality of passive data 
in the V2 study, the actual utility of higher quality data 

Weekly survey questions. Answers were on a Likert scale 
(0 = not at all, 1 = several days, 2 = more than half the days, 
and 3 = nearly every day). Note that for the PSQI component 
score, components 1 and 6 are absent as those questions 
were not included in the survey.

1 3Survey

PHQ-9

GAD-7

PSS

UCLA Loneliness

Question number

Question

Journal of Technology in Behavioral Science

0
1
2
3
4
5
6

7

8

9

10
11
12
13
14
15
16
17
18
19
20

21
22

23
24

25
26
27

28

29
30
31
32
33
34
35
36
37
38
39
40
41
42

Total score
Over the past week, I have had little interest or pleasure in doing things
Over the past week, I have felt down, depressed, or hopeless
Over the past week, I have had trouble falling asleep, starting asleep, or sleeping too much
Over the past week, I have felt tired or have had little energy
Over the past week, I have experienced poor appetite or overeating
Over the past week, I have felt bad about myself, or that I am a failure or have let down myself or 

my family

Over the past week, I have had trouble concentrating on things such as reading the newspaper or 

watching television

Over the past week, I have found myself moving or speaking so slowly that other people could have 
noticed. Or the opposite—being so fidgety or restless that I have been moving around a lot more 
than usual

Over the past week, I have had thoughts that I would be better off dead, or thoughts of hurting 

myself
Total score
Over the past week, I have felt nervous, anxious, or on edge
Over the past week, I have not been able to stop or control worrying
Over the past week, I have been worrying too much about different things
Over the past week, I have had trouble relaxing
Over the past week, I have felt so restless that it's hard to sit still
Over the past week, I have felt myself becoming easily annoyed or irritable
Over the past week, I have felt afraid as if something awful might happen
Total score
In the last week, how often have you been upset because of something that happened unexpectedly?
In the last week, how often have you felt that you were unable to control the important things in 

your life?

In the last week, how often have you felt nervous and stressed?
In the last week, how often have you felt confident about your ability to handle your personal 

problems?

In the last week, how often have you felt that things were going your way?
In the last week, how often have you found that you could not cope with all the things that you had 

to do?

In the last week, how often have you been able to control irritations in your life?
In the last week, how often have you felt that you were on top of things?
In the last week, how often have you been angered because of things that happened that were 

outside of your control?

In the last week, how often have you felt difficulties were piling up so high that you could not 

overcome them?

Total score
I am unhappy doing so many things alone
I have nobody to talk to
I cannot tolerate being so alone
I lack companionship
I feel as if nobody really understands me
I find myself waiting for people to call or write
There is no one I can turn to
I am no longer close to anyone
My interests and ideas are not shared by those around me
I feel left out
I feel completely alone
I am unable to reach out and communicate with those around me
My social relationships are superficial

1 3 
Journal of Technology in Behavioral Science 

Survey

Question number

Question

PQ-16

PSQI

DWAI

PSQI Component 

Score

43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60

61
62
63
64
65
66

67
68
69
70
71
72
73
74
75

76

77
78
79
80
81
82
83
89

90
91
92
93
94

I feel starved for company
No one really knows me well
I feel isolated from others
I am unhappy being so withdrawn
It is difficult for me to make friends
I feel shut out and excluded by others
People are around me but not with me
Total score
I feel uninterested in the things I used to enjoy
I often seem to live through events exactly as they happened before (déjà vu)
I sometimes smell or taste things that other people can’t smell or taste
I often hear unusual sounds like banging, clicking, hissing, clapping or ringing in my ears
I have been confused at times whether something I experienced was real or imaginary
When I look at a person, or look at myself in a mirror, I have seen the face change right before my eyes
I get extremely anxious when meeting people for the first time
I have seen things that other people apparently can't see
My thoughts are sometimes so strong that I can almost hear them
I sometimes see special meanings in advertisements, shop windows, or in the way things are 

arranged around me

Sometimes I have felt that I’m not in control of my own ideas or thoughts
Sometimes I feel suddenly distracted by distant sounds that I am not normally aware of
I have heard things other people can't hear like voices of people whispering or talking
I often feel that others have it in for me
I have had the sense that some person or force is around me, even though I could not see anyone
I feel that parts of my body have changed in some way, or that parts of my body are working 

differently than before

Total score
How often is it that you cannot get to sleep within 30 min?
How often is it that you wake up in the middle of the night or early morning?
How often have you had trouble sleeping because you cannot breathe comfortably?
How often have you had trouble sleeping because you cough or snore loudly?
How often have you had trouble sleeping because you feel too hot?
How often have you had trouble sleeping because you have bad dreams?
How often have you had trouble sleeping because you have pain?
During the past week, how often have you had trouble staying awake while driving, eating meals, 

or engaging in social activity?

During the past week, how much of a problem has it been for you to keep up enthusiasm to get 

things done?

Total score
I trust the app to guide me towards my personal goals
I believe the app tasks will help me to address my problems
The app encourages me to accomplish tasks and make progress
I agree that the tasks within the app are important for my goals
The app is easy to use and operate
The app supports me to overcome challenges
Total score

Component 2
Component 3
Component 4
Component 5
Component 7

1 3B.2

Daily survey questions common to colleges V1 and V2. 
Answers were on a Likert scale (0 = not at all, 1 = several 
days, 2 = more than half the days, and 3 = nearly every day).

Race

Total

Survey

Question Number Question

Journal of Technology in Behavioral Science

Completed the 
study

Discontinued

Did not complete  
run-in

F M N Total F M N Total F M N Total

46 19 1

66

17 9

4

30

28 20 5

53

84
85
86
87

PHQ-9

GAD-7

B.3

Total score
I felt down today
Today I felt little interest or pleasure
Today I had trouble relaxing

Appendix D

Comparison of the average (a) home time, (b) screen dura-
tion, and (c) sleep duration. These features are significantly 
different between V1 and V2.

Appendix E

Numbers for passive data and active features.

Question Number

Feature

Dendrogram representation of the hierarchical clustering of 
the correlations is shown in Fig. 2 for colleges V1 and V2.

88
95
96
97
98
99

Number of activities
Entropy
Home time
Screen duration
GPS data quality
Sleep duration

Appendix C

Race  and  gender  in  the  college  V2  dataset.  Comparing 
participants that did not make it through the run-in period 
were discontinued, and completed the study. F = female, 
M = male, and N = nonbinary.

Completed the 
study

Discontinued

Did not complete  
run-in

Race

F M N Total F M N Total F M N Total

0

0

0

0

0

0

0

0

0

0

0

0

American 
Indian or 
Alaskan 
Native

Asian

African 

American

Latinx

Native 

Hawaiian 
/ Pacific 
Islander

15 5

1

3

1

0

2

0

0

0

0

0

20

1

5

1

White

Other

26 12 1

0

0

0

39

0

7

1

0

0

9

0

2

1

1

0

4

1

1

2

0

0

1

0

10

11 6

4

1

0

1

0

1

1

4

0

14

1

14 8

1

1

0

1

0

0

4

0

17

3

4

1

26

2

Appendix F

Number of participants used for model training and testing 
for each survey. There was no time input feature in mind-
LAMP at the time of the V1 study, so many of the PSQI 
responses could not be used.

V1

V2

Survey

10 days

28 days

10 days

28 days

PHQ-9
GAD-7
PSS
UCLA
PQ-16
PSQI

57
53
58
55
49
40

144
138
144
135
122
74

40
39
40
38
39
41

59
58
60
56
57
60

Acknowledgements  The many people who have continued to test and 
improve mindLAMP through their feedback and ideas.

Author Contributions  All authors contributed equally.

Funding  This work was supported by the Lee family gift to the HTEC 
fund at BIDMC.

Declarations 

Ethics Approval  This study was performed in line with the principles 
of the Declaration of Helsinki. Approval was granted by the Ethics 
Committee of BIDMC (IRB # 2020P000862, approved 5/30/2021).

Consent to Participate  Written informed consent was obtained from 
all participants.

1 3 
Journal of Technology in Behavioral Science 

Consent for Publication  NA as no personal health information is pre-
sented and no case examples are presented.

Conflict of Interest  JT  is  a  cofounder  of  Precision  Mental  Wellness, 
which is not mentioned in this paper.

References

Aslanian, S., & Roth, A. (2021). “Under pressure: Inside the college 

mental health crisis,” American Public Media Reports.

Borghouts, J., Eikey, E. V., Mark, G., De Leon, C., Schueller, S. M., 
Schneider, M., Stadnick, N., Zheng, K., Mukamel, D. B., & Sorkin, 
D. H. (2021). Understanding mental health app use among commu-
nity college students: Web-based survey study. Journal of Medical 
Internet Research, 23(9), e27745.

Buysse, D. J., Reynolds, C. F., Monk, T. H., Berman, S. R., & Kupfer, 
D. J. (1989). The Pittsburgh sleep quality index: A new instru-
ment for psychiatric practice and research. Psychiatry Research, 
28(2), 193–213.

Chikersal, P., Doryab, A., Tumminia, M., Villalba, D. K., Dutcher, J. M., 
Liu, X., Cohen, S., Creswell, K. G., Mankoff, J., Creswell, D. J., 
Goel, M., & Dey, A. K. (2021). Detecting depression and predict-
ing its onset using longitudinal symptoms captured by passive sens-
ing: A machine learning approach with robust feature selection. 
ACM Transactions on Computer-Human Interaction, 28(1), 1–41.
Cohen, S., Kamarck, T., & Mermelstein, R. (1983). A global meas-
ure of perceived stress. Journal of Health and Social Behavior, 
24(4), 385–396.

Eisenberg, D., Lipson, S. K., Heinze, J., Zhou, S., Talaski, A., Patterson, 
A., Fogel, S., Schulz,   P., & Li, L. (2020). “The healthy minds 
study: Fall 2020 data report,” The Healthy Minds Study.

Goldberg, S. B., Baldwin, S. A., Riordan, K. M., Torous,  J., Dahl, 
C. J., Davidson, R. J., & Hirshberg, M. J. (2021). “Alliance with 
an unguided smartphone app: Validation of the Digital Working 
Alliance Inventory,” Assessment.

Goldberg, S. B., Lam, S. U., Simonsson, O., Torous, J., & Sun, S. 
(2022). “Mobile phone-based interventions for mental health: 
A systematic meta-review of 14 meta-analyses of randomized 
controlled trials,” PLOS Digital Health, 1(1).

Hartocollis, A. (2021). “Another surge in the virus has colleges fear-

ing a mental health crisis,” The New York Times.

Kiang, M. V., Chen, J. T., Krieger, N., Buckee, C. O., Alexander, M. 
J., Baker, J. T., Buckner, R. L., Coombs, G., Rich-Edwards,  J. 
W., Carlson, K. W., & Onnela, J. (2021). “Sociodemographic 
characteristics of missing data in digital phenotyping,” Scien-
tific Reports, 11(1).

Kroenke, K., Spitzer, R. L., & Williams, J. B. (2001). The PHQ-
9: Validity of a brief depression severity measure. Journal of 
General Internal Medicine, 17(3), 261–272.

Lattie, E. G., Cohen, K. A., Hersch, E., Williams, K. D., Kruzan, K. P., 
Maclver, C., Hermes, J., Maddi, K., Kwasny, M., & Mohr, D. C. 
(2021). “Uptake and effectiveness of a self-guided mobile app plat-
form for college student mental health,” Internet Interventions, 27.
Lattie, E. G., Kornfield, R., Ringland, K. E., Zhang, R., Winquist, 
N., & Reddy, M. (2020). “Designing mental health technolo-
gies that support the social ecosystem of college students,” 
Proceedings of the 2020 CHI Conference on Human Factors 
in Computing Systems.

Liu, T., Nicholas, J., Theilig, M., Guntuku, S., Kording, K., Mohr, 
D.,  &  Ungar,  L.  (2019).  Machine  learning  for  phone-based 

relationship estimation. Proceedings of the ACM on Interactive, 
Mobile, Wearable and Ubiquitous Technologies, 3(4), 1–23.
Loewy, R. L., Bearden, C. E., Johnson, J. K., Raine, A., & Cannon, 
T. D. (2005). The prodromal questionnaire (PQ): Preliminary 
validation of a self-report screening measure for prodromal and 
psychotic syndromes. Schizophrenia Research, 79, 117–125.
Mack, D. L., DaSilva, A. W., Rogers, C., Hedlund, E., Murphy,  
E. I., Vojodanovski, V., Plomp, J., Wang, W., Nepal, S. K., 
Holtzheimer,  P. E., Wagner, D. D., Jacobson, N. C., Meyer, 
M. L., Campbell, A. T., & Huckins. (2021). “Mental health and 
behavior of college students during the COVID-19 pandemic: 
Longitudinal  mobile  smartphone  and  ecological  momen-
tary assessment study, part II,” Journal of Medical Internet 
Research, 23(6), e28892.

Melcher, J., Hays, R., & Torous, J. (2020). Digital phenotyping for 
mental health of college students: A clinical review. Evidence 
Based Mental Health, 23(4), 161–166.

Melcher, J., & Torous, J. (2020). Smartphone apps for college mental 
health: A concern for privacy and quality of current offerings. 
Psychiatric Services, 71(11), 1114–1119.

Mohr, D. C., Shilton, K., & Hotopf, M. (2020). “Digital phenotyping, 
behavioral sensing, or personal sensing: names and transparency 
in the digital age,” npj Digital Med, 3(1).

Murthy, V. H. (2021). “Protecting youth mental health,” Office of 

the Surgeon General.

Melcher, J., Lavoie, J., Hays,  R., D’Mello, R., Rauseo-Ricupero, N., 
Camacho,  E., Rodriguez-Villa, E., Wisniewski,  H., Lagan, S., 
Vaidyam, A., & Torous, J. (2021). “Digital phenotyping of stu-
dent mental health during COVID-19: An observational study of 
100 college students,” Journal of American College Health, 1–13.
Nahum-Shani, I., Smith, S. N., Spring, B. J., Collins, L. M., Witkiewitz, 
K., Tewari, A., & Murphy, S. A. (2018). Just-in-time adaptive inter-
ventions (JITAIs) in mobile health: Key components and design 
principles for ongoing health behavior support. Annals of Behavioral 
Medicine, 52(6), 446–462.

Patel, S. K., & Torous, J. (2022). “Exploring the neuropsychiatric 
sequalae of perceived COVID-19 exposure in college students: 
A pilot digital phenotyping study,” Frontiers in Psychiatry, 12.
Pedregosa, F., Varoquaux,  G., Gramfort, A., Michel, V., Thirion,  B., 
Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg,  V., 
Vanderplas, J., Passos,  A., Cournapeau, D., Brucher,  M., Perrot, M.,  
& Duchesnay, E. (2011). “Scikit-learn: Machine learning in Python,” 
Journal of Machine Learning Research, 2825–2830.

Russell, D. (1996). UCLA Loneliness Scale (Version 3): Reliability, 
validity, and factor structure. Journal of Personality Assessment, 
66(1), 20–40.

Seabold, S., & Perktold, J. (2010). “statsmodels: Econometric and statisti-
cal modeling with python,” Proceedings of the Python in Science 
Conference.

Smith, A. C., Fowler, L. A., Graham, A. K., Jaworski, B. K., Firebaugh, 
M.-L., Monterubio, G. E., Vazquez, M. M., DePietro, B., Sadeh-
Sharvit, S., Balantekin, K. N., Topooco, N., Wilfley, D. E., & 
Taylor, C. (2021). Digital overload among college students: Impli-
cations for mental health app use. Social Sciences, 10(8), 279.
Spitzer, R. L., Kroenke, K., Williams, J. B., & Löwe, B. (2006). A brief 
measure for assessing generalized anxiety disorder: The GAD-7. 
Archives of Internal Medicine, 166(10), 1092–1097.

Torous, J., Kiang, M. V., Lorme, J., & Onnela, J.-P. (2016). New tools 
for new research in psychiatry: A scalable and customizable plat-
form to empower data driven smartphone research. JMIR Mental 
Health, 3(2), e16.

Virtanen, P., Gommers, R., & Oliphant, T. E. (2020). “SciPy 1.0: Fun-
damental algorithms for scientific computing in Python,” Nature 
Methods, 261–272.

1 3Wang, R., Chen, F., Chen, Z., Li, T., Harari, G., Tignor, S., Zhou, X., 
Ben-Zeev, D. & Campbell, T. A. (2014). “StudentLife: Assessing 
mental health, academic performance and behavioral trends of 
college students using smartphones,” Proceedings of the ACM 
International  Joint  Conference  on  Pervasive  and  Ubiquitous 
Computing.

Publisher's  Note  Springer  Nature  remains  neutral  with  regard  to 
jurisdictional claims in published maps and institutional affiliations.

Journal of Technology in Behavioral Science

Springer Nature or its licensor (e.g. a society or other partner) holds 
exclusive rights to this article under a publishing agreement with the 
author(s) or other rightsholder(s); author self-archiving of the accepted 
manuscript version of this article is solely governed by the terms of 
such publishing agreement and applicable law.

1 3
