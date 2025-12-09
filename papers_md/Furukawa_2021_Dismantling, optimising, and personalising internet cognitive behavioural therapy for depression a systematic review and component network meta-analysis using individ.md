# Furukawa_2021_Dismantling, optimising, and personalising internet cognitive behavioural therapy for depression a systematic review and component network meta-analysis using individ

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

HHS Public Access
Author manuscript
Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

Published in final edited form as:

Lancet Psychiatry. 2021 June ; 8(6): 500–511. doi:10.1016/S2215-0366(21)00077-8.

Dismantling, optimising, and personalising internet cognitive 
behavioural therapy for depression: a systematic review and 
component network meta-analysis using individual participant 
data

A full list of authors and affiliations appears at the end of the article.

Summary

Background—Internet cognitive behavioural therapy (iCBT) is a viable delivery format of 
CBT for depression. However, iCBT programmes include training in a wide array of cognitive 
and behavioural skills via different delivery methods, and it remains unclear which of these 
components are more efficacious and for whom.

Methods—We did a systematic review and individual participant data component network meta-
analysis (cNMA) of iCBT trials for depression. We searched PubMed, PsycINFO, Embase, and 
the Cochrane Library for randomised controlled trials (RCTs) published from database inception 
to Jan 1, 2019, that compared any form of iCBT against another or a control condition in the 
acute treatment of adults (aged ≥18 years) with depression. Studies with inpatients or patients with 
bipolar depression were excluded. We sought individual participant data from the original authors. 
When these data were unavailable, we used aggregate data. Two independent researchers identified 
the included components. The primary outcome was depression severity, expressed as incremental 
mean difference (iMD) in the Patient Health Questionnaire-9 (PHQ-9) scores when a component 
is added to a treatment. We developed a web app that estimates relative efficacies between any 
two combinations of components, given baseline patient characteristics. This study is registered in 
PROSPERO, CRD42018104683.

Findings—We identified 76 RCTs, including 48 trials contributing individual participant data (11 
704 participants) and 28 trials with aggregate data (6474 participants). The participants’ weighted 
mean age was 42·0 years and 12 406 (71%) of 17 521 reported were women. There was suggestive 

Correspondence to: Prof Toshi A Furukawa MD, Department of Health Promotion and Human Behavior, Kyoto University Graduate 
School of Medicine/School of Public Health, Kyoto 606-8501, Japan, furukawa@kuhp.kyoto-u.ac.jp.
*Co-first authors
†Co-last authors
Contributors
TAF and OE conceived the study. TAF, AS, AC, OE, PCu, and EK designed the study. PCu, EK, CM, AS, EGO, and TAF selected 
the studies and extracted data. GA, CGB, JSh, TB, FWB, CBu, PCa, IC, HC, AM, JD, MJHH, DDE, LF, NRF, DRS, IDE, EF, VKr, 
AG, SG, EL, SB, HDH, LHS, RJ, RK, MK, CBj, AK, HR, JPK, JSchr, BM, SM, LB, OL, PJ, JL, JM, AWG, DCM, JM-M, JG-C, SN, 
A-CZ, KO, ADW, JMN, SP, RP, JSchn, WP, NEP, DR, IMR, SLR, LBS, JSm, VS, VJP, BU, KMPvB, SvL, NG, VKa, KV, LW, AvS, 
PZ, CK, and MH contributed the individual participant data. OE, EK, and PCu verified the data. OE analysed the data. TAF, AS, EGO, 
OE, EK, and PCu interpreted the results. TAF and OE wrote the first draft of the manuscript. All authors had access to all the data and 
provided critical input and revisions to the draft manuscripts and approved the final manuscript. TAF, AS, EGO, OE, EK, and PCu had 
final responsibility for the decision to submit for publication.

Data sharing
The full aggregate-level data and the analysis R codes are available online at GitHub. Individual-level data cannot be made available 
due to confidentiality agreements in the original studies.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 2

evidence that behavioural activation might be beneficial (iMD −1·83 [95% credible interval (CrI) 
−2·90 to −0·80]) and that relaxation might be harmful (1·20 [95% CrI 0·17 to 2·27]). Baseline 
severity emerged as the strongest prognostic factor for endpoint depression. Combining human 
and automated encouragement reduced dropouts from treatment (incremental odds ratio, 0·32 
[95% CrI 0·13 to 0·93]). The risk of bias was low for the randomisation process, missing outcome 
data, or selection of reported results in most of the included studies, uncertain for deviation 
from intended interventions, and high for measurement of outcomes. There was moderate to high 
heterogeneity among the studies and their components.

Interpretation—The individual patient data cNMA revealed potentially helpful, less helpful, 
or harmful components and delivery formats for iCBT packages. iCBT packages aiming to be 
effective and efficient might choose to include beneficial components and exclude ones that are 
potentially detrimental. Our web app can facilitate shared decision making by therapist and patient 
in choosing their preferred iCBT package.

Funding—Japan Society for the Promotion of Science.

Introduction

Cognitive behavioural therapy (CBT) is the most widely studied type of psychotherapy for 
depression.1,2 CBT encompasses a wide array of cognitive and behavioural skills, which 
are sometimes administered alone but more commonly in various combinations. Moreover, 
training in these skills is generally administered in a flexible way, because it is believed that 
their efficacy is moderated by individual patients’ characteristics. It is then of the utmost 
importance to know which of these components are more contributory to its effectiveness, 
and which combinations of them are optimal and for whom.3

Traditional approaches to examine components involved so-called dismantling studies, 
in which the whole treatment package is compared against a package that omits one 
component.4,5 However, such studies have been typically underpowered and of poor 
methodological quality. Moreover, these studies have proved difficult to combine because 
each study examined very diverse components and covered heterogeneous conditions.6 With 
new advances in the science of evidence synthesis, complex interventions can now be 
dismantled through component network meta-analysis (cNMA) by estimating the individual 
efficacies of the various components contained in a network of randomised controlled trials 
(RCTs).7,8 cNMA increases statistical power by combining direct and indirect comparisons 
while fully respecting the randomised structure of the evidence—ie, treatment effects are 
estimated separately in each study, and then study-specific estimates are pooled across the 
network.9

One fundamental limitation of all previous dismantling studies and cNMAs is that they dealt 
mainly with face-to-face CBT, in which it is difficult to be sure that the claimed components 
have actually been administered as intended and that no other elements were introduced, 
unless treatment fidelity was monitored. In the past two decades, computerised or internet 
CBT (iCBT) has been introduced and widely tested in trials. It is now well established that 
guided iCBT can be as effective as face-to-face individual, group, or other delivery formats 
of CBT of similar length.10–12 iCBT provides a unique platform whereby each cognitive 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 3

and behavioural skill is offered uniformly and as intended by the programme developers. 
Moreover, iCBT brings additional clinical questions regarding delivery methods to improve 
its adherence.

The aim of this individual participant data cNMA was to elucidate which of the skills 
and delivery methods commonly included in the broadly conceived iCBT packages are 
efficacious and for whom.

Methods

Search strategy, selection criteria, and data extraction

In this systematic review and individual participant data cNMA we used an existing 
database of psychological treatments for depression, which is updated annually through 
comprehensive literature searches in PubMed, PsycINFO, Embase, and the Cochrane 
Library.13 Searches combined terms for depression and psychotherapies with filters for 
randomised controlled trials without any language restrictions. The full search strings are in 
the appendix (pp 4–8). EK and PCu independently checked this database for eligible studies; 
disagreements were resolved by discussion. The last update search was done on Jan 1, 2019.

We included all RCTs that compared any form of iCBT against another form of iCBT or a 
control condition in the acute phase treatment of adults (aged ≥18 years) with depression, 
either diagnosed as unipolar major or minor depression according to operationalised 
diagnostic criteria, such as DSM-5 or ICD-10, or judged so by elevated scores on self-report 
measures with satisfactory reliability and validity. We excluded studies with inpatients or 
patients with bipolar depression.

We conceptualised CBT broadly as psychotherapy involving training in any of the cognitive 
or behavioural skills, including cognitive restructuring, behavioural activation, interpersonal 
skills, structured problem solving, or third wave components. The iCBT had to be a web-
based or app-based programme using the internet to deliver the CBT contents. We excluded 
studies of telephone CBT, computerised CBT available only on a clinic-based computer, and 
when therapists delivered CBT through teleconferencing or emails.

The control conditions of interest were being on a waiting list for treatment, no treatment, 
attention or psychological placebo, and treatment as usual. Studies have defined different 
conditions as treatment as usual.14,15 In our study, treatment as usual was defined as 
including conventional drug treatment either as part of the general practitioners’ care or 
as part of the study protocol. Watchful waiting or follow-up by community nurses were 
classified as attention or psychological placebo, even when it was regarded as treatment as 
usual in some settings.

The definitions of our components of interest for the intervention and control arms, as 
conceptualised and defined by TAF and PC who are expert clinicians and researchers in 
CBT and iCBT, are shown in the panel. The various forms of iCBT and control conditions 
as conceptualised from the component perspective are shown in the table. The intervention 
could be of any duration.

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 4

Pairs of two independent reviewers (TAF, AS, EGO) classified all identified treatment arms 
and their constituent components according to the definitions in the panel and table, using 
all available information from the publications, the iCBT programmes if accessible, and 
inquiries with the original investigators. The component could be of any length. A CBT skill 
component was judged present when it was mentioned as such in the publication or was 
allocated a session or lesson in the programme. When skills not covered in this classification 
(eg, expressive writing, dreamwork) were included, we assumed such interventions to have 
some non-specific treatment effects only. The impact of this assumption was tested in a 
sensitivity analysis excluding such trials.

Pairs of two independent reviewers (TAF, AS, EGO) independently assessed the validity 
of the included studies using the revised risk of bias tool by Cochrane.17 The assessment 
was strictly on the primary outcome used in this review, which was depression severity 
derived either from the individual participant data or the aggregate data, depending on data 
availability. Any disagreement was resolved through discussion or through consultation with 
a third reviewer.

Authors of the identified studies were contacted via email and requested to contribute 
individual-level data. When data provision was explicitly declined or the authors did not 
respond after three attempts, the individual participant data were deemed unavailable. After 
collecting individual participant data, two independent reviewers (EK, TAF) cross-examined 
the provided data against the original publications. When the numbers did not match, we 
contacted the authors for clarification. Duplicate data were excluded.

This protocol for this study has already been published.18 This report follows the Preferred 
Reporting Items for Systematic Reviews and Meta-Analyses extension statements for 
network meta-analysis19 and for individual participant data meta-analysis.20 The PRISMA-
individual participant data checklist is provided in the appendix (pp 84–87).

Statistical analyses

Our primary outcome was depression severity as measured on a continuous scale for 
depression at the end of the acute phase treatment. We accepted any depression measures 
with established reliability and validity. The scale scores were converted into the most 
frequently used scale, the Patient Health Questionnaire-9 (PHQ-9),21 when the established 
conversion algorithms were available.22,23

Our secondary outcomes were dropout from treatment, defined as completing less than 80% 
of the contents of the programme in individual participant data studies or according to the 
original authors’ definition in aggregate data studies, and dropout from the end-of-treatment 
assessment for any reason.

We first did a network meta-analysis at the treatment level to examine if the network of 
the identified trials was amenable to network meta-analysis. A fundamental pre-requisite 
for network meta-analyses is the so-called transitivity—ie, to have effect modifiers 
evenly distributed across comparisons. We therefore examined the distribution of potential 
effect modifiers in studies grouped by treatment comparison. We did a two-step random 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 5

effects network meta-analysis at the treatment level, using both aggregate data and 
individual participant data studies; for aggregate data studies we used the published 
data, and for individual participant data studies we used multiple imputations based on 
individual participant data to impute missing data. We did the network meta-analysis in a 
frequentist setting in R using netmeta,24 assuming common heterogeneity for all treatment 
comparisons.25 We checked network inconsistency, a statistical expression of intransitivity, 
using the back-calculation26 and the design-by-treatment methods.27

Subsequently, we used cNMA models that jointly synthesised aggregate data and individual 
participant data studies. We did both a two-step and a one-step cNMA. In the two-step 
approach, we calculated trial-level estimates of treatment effects from studies for which 
individual participant data were available and therefore could be re-analysed, and used 
published trial-level estimates from studies for which individual participant data were 
not available. In the one-step approach, we used the full individual participant data 
including patient-level covariates when available and trial-level estimates of treatment 
effects when individual participant data were not available. The models disentangled the 
effects of components assuming additivity,9 and examined component–covariate interactions 
using shrinkage methods.28 We estimated component-specific incremental mean differences 
(iMD; the added benefit of adding a component to a treatment). The component-covariate 
interactions were modelled assuming linearity. We examined the robustness of the 
assumption of additive component effects by doing a sensitivity analysis including two-way 
interactions. We used the parameter estimates to develop a web app for which the inputs are 
patient characteristics and two combinations of components, and the output is the estimated 
relative treatment effects between the two combinations. By using individual-level data, we 
were able to examine prognostic factors (baseline characteristics which predict the outcome 
regardless of the intervention) and effect modifiers (those which predict differential response 
to treatments) and to estimate individual relative treatment effects based on these factors.

We repeated the procedure for the two secondary outcomes, using a binomial likelihood, 
to estimate incremental odds ratios (iORs) for each component.7 For the dropout from 
treatment outcome, we only used studies comparing active treatments, because this outcome 
cannot be measured for controls (waiting list, treatment as usual, no treatment, attention or 
psychological placebo).

We did four prespecified sensitivity analyses by excluding studies without formal diagnosis 
of major depression, excluding studies with patients from special populations, excluding 
arms that used skills not covered in our classifications, and limiting the analysis to studies 
with high adherence, for the primary outcome. We also did two post-hoc analyses by 
excluding arms which taught more than four CBT components, and by using a model that 
assumed two-way interactions between the components.

Details of statistical models used and of fitting procedures are given in the appendix (pp 
9–15). The appendix (p 16) lists changes from the protocol.

We examined whether studies providing individual participant data were systematically 
different from studies not providing individual participant data by comparing the baseline 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 6

characteristics and symptom changes of included participants. We examined possible small 
study effects and publication bias by visually inspecting contour-enhanced funnel plots of 
pairwise meta-analyses for efficacy between all active arms versus waiting list. This study is 
registered in PROSPERO (CRD42018104683)

Role of the funding source

The funders of the study had no role in study design, data collection, data analysis, data 
interpretation, or writing of the report.

Results

Up to Jan 1, 2019, we screened 21 162 citations, of which we examined 131 potentially 
eligible studies in full text. We finally included 76 trials and sought individual participant 
data from the original authors. Authors of 48 (63%) studies agreed to provide individual 
participant data representing 11 704 randomly assigned participants; the remaining 28 
studies were included as aggregate data, representing 6474 randomly assigned participants 
(appendix p 17). The lists of the included studies (with responses to author queries), 
excluded studies (with reasons), and studies awaiting assessment are included in the 
appendix (pp 18–41).

The participants’ weighted mean age was 42·0 years, and 12 406 (71%) of 17 521 reported 
participants were women. Operationalised diagnostic criteria were used in 27 studies.

The 76 included studies had 179 arms. These arms included all of our pre-specified 
components of interest, ranging from behaviour therapy for insomnia in four arms to 
conventional drug treatment in 143 arms. The inter-rater reliability of judgements for 
components was excellent, with a mean percentage agreement of 93·3% (range 84·0–98·6%) 
and a mean κ of 0·76 (range 0·38–0·96) for the 17 components (panel; appendix pp 42–51). 
We were able to access five iCBT programmes ourselves (Sadness Program, Wellbeing 
Course, Kokoroapp, BeatingTheBlues, and MoodGym), which were used in 20 of the 
included studies (appendix pp 42–51). The identified components were confirmed by the 
co-authors who contributed the individual participant data (appendix pp 18–28). Using the 
conceptualisations in the table, the type of therapy or control condition was represented 
in the following number of arms: CBT (n=72), cognitive therapy (n=2), behavioural 
activation (n=11), problem-solving therapy (n=11), third-wave cognitive behavioural therapy 
(n=6), psychoeducation (n=6), waiting list (n=51), treatment as usual (n=10), attention or 
psychological placebo (n=9), or no treatment (n=1). The treatment duration ranged from 3 
to 24 weeks (median 8 weeks). The median completion rate of programme lessons was 72% 
(range 25–95%) in 46 studies that reported the values. Antidepressant use was reported by 
4031 (40%) of 10 041 participants (appendix pp 52–57).

The risk of bias according to the Cochrane’s revised risk of bias tool17 was low in 66 
studies (86%) for randomisation process, in six studies (8%) for the deviation from intended 
interventions, in 64 studies (83%) for missing outcome data, in two studies (3%) for 
measurement of the outcome, and 53 studies (69%) for selection of the reported results. 
The inter-rater reliability of risk of bias assessment was satisfactory, with a mean percentage 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 7

agreement of 93·9% (range 87·5–97·8%) and a mean weighted κ of 0·52 (range 0·17–0·84) 
for the five domains (appendix pp 58–59).

In the individual participant data studies a small minority of patients (387 [3·5%] of 11 122) 
had scores of less than 5 points on PHQ-9 at baseline and would be classified as euthymic 
according to the commonly accepted cutoff.21 We excluded such patients in the analyses 
because they would not normally be targets for treatment for acute depression. Patients 
missing both baseline and endpoint scores (390 [3·5%] of 11 122) were also excluded. Two 
studies29,30 used scales that could not be converted into PHQ-9 and were therefore excluded 
from the analyses.

The mean age of the participants was 42·9 years (SD 12·3) in the 48 trials with individual 
participant data and 39·3 years in the 28 studies with aggregate data. In the individual 
participant data trials, 6732 (65%) of 10 309 reported participants were women and in the 
aggregate data trials 3117 (71%) of 4389 reported participants were women. The mean 
baseline score was 13·2 (SD 4·7) and the mean endpoint PHQ-9 score was 9·0 (SD 5·5) in 
individual participant data trials; and the mean baseline score was 13·0 (SD 5·5) and the 
mean endpoint PHQ-9 score was 8·8 (SD 4·8) in aggregate data trials. Overall, there was no 
indication of systematic differences between individual participant data and aggregate data 
studies.

Figure 1 shows the network geometry for the primary outcome. Figure 2 shows the results 
from the pairwise meta-analyses and network meta-analysis at the treatment level, using 
the two-step approach in which we generated trial-level results based on the individual 
participant data as described earlier when individual participant data were available and 
could be re-analysed, and used trial-level results as reported in the original publications 
when individual participant data were not available. Cognitive therapy, behavioural 
activation, third-wave cognitive behavioural therapy, CBT, psychoeducation, and problem-
solving therapy were all shown to be more efficacious than waiting list. Forest plots of 
pairwise meta-analyses with more than five studies are shown in the appendix (pp 61–63). 
Transitivity was assessed by investigating the distribution of potential effect modifiers, 
including age, gender, and baseline severity of depression (appendix pp 64–65). One 
comparison (cognitive therapy vs attention or psychological placebo) had much higher 
baseline severity than all other comparisons but otherwise these effect modifiers appeared 
to be evenly distributed across comparisons (appendix pp 64–65). The design-by-treatment 
test for global inconsistency showed strong evidence of global inconsistency (Q=37·8, 17 
df, p=0·0026); however, the back-calculation method identified only one comparison of 18 
that showed evidence of inconsistency, a proportion that would be empirically expected31 
(appendix p 65). Common heterogeneity τ was considered moderate to high. The contour-
enhanced funnel plot comparing all active treatments versus waiting list showed no evidence 
of publication bias (appendix p 66).

Figure 3 shows the main effects from the individual participant data cNMA, using the 
one-step approach in which we analysed individual participant data if available but also used 
trial-level results when individual participant data were not available. There was stronger 
evidence that the behavioural activation and non-specific treatment effects components had 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 8

beneficial effects, but the relaxation component was detrimental. There was weaker evidence 
that behaviour therapy for insomnia was also helpful, showing large point estimates but with 
wider confidence intervals.

Baseline severity was the strongest prognostic factor but the estimated effect modifications 
(ie, interactions with treatment components) were relatively small. Full results for the 
interaction terms, the network diagrams at the component level, and results from cNMA 
at the aggregate data level are given in the appendix (pp 67–72).

On the basis of these results we can estimate patient-specific relative effects between any 
combinations. For example, for a 45-year-old female patient, in a relationship, and with 
a baseline PHQ-9 score of 12, the relative effect of an efficient iCBT package consisting 
of psychoeducation, behavioural intervention, and problem solving using automated 
and human encouragement (ie, non-specific treatment effects plus psychoeducation plus 
behavioural activation plus problem solving plus automated encouragement plus human 
encouragement) versus waiting list control can be estimated as −4·9 (95% credible interval 
[95% CrI] −6·8 to −3·1). Our web app provides estimates of relative efficacies between any 
two combinations of components, for any given patient characteristics.

For dropouts from treatment, we did a cNMA of studies comparing active treatments from 
five trials providing aggregate data and ten providing individual participant data. Because 
of the small sample size, we only did a two-step cNMA. The obtained estimates for the 
components were imprecise but there was some suggestion that automated encouragement 
and human encouragement reduced dropout from treatment (combined iOR 0·32 [95% CrI 
0·13–0·93]; appendix p 73). For dropouts from assessment, both the two-step and one-step 
cNMA were done (appendix pp 74–76).

The results of the pre-specified and post-hoc sensitivity analyses for the primary outcome 
are shown in the appendix (pp 77–83); these results were concordant with the primary 
analyses.

Discussion

We did a network meta-analysis of the broadly conceived iCBT treatments for depression 
and their control conditions, and a cNMA of 17 components variably included in these 
packages based on 48 trials with individual participant data and 28 trials with aggregate data. 
All iCBT treatment packages were found to be superior to the waiting list control. There 
was evidence that the non-specific treatment effects and behavioural activation components 
might have beneficial effects whereas the relaxation component might have negative effects, 
and weaker evidence that the behaviour therapy for insomnia component might be helpful. 
Having automated encouragement via emails or text messaging and human encouragement 
by telephone or email without reference to the therapeutic contents might enhance adherence 
to the treatment. Baseline severity of depression emerged as the strongest prognostic factor; 
given the baseline severity, age, gender, and relationship status, our web app can estimate the 
relative effects of any combination treatment over another.

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 9

López-López and colleagues’8 cNMA of CBT for depression found no evidence of specific 
effects for any skills or delivery formats. These negative findings might be due to the fact 
that the authors included mostly face-to-face CBT interventions, which generally allowed 
broad discretion to therapists who might have reduced, modified, or even left out some 
contents and introduced new contents outside the therapy manual, unless the trials were 
rigorously monitored for fidelity. López-López and colleagues’ decomposition of the CBT 
contents also raised some concerns because some arms had only homework as their content 
while many arms did not have psychoeducation (few CBT programmes would take place 
without psychoeducation about depression and its cognitive behavioural model).

In our study behavioural activation emerged as a beneficial component. This finding 
is in line with the systematic review of dismantling studies, which estimated a pooled 
standardised mean difference (SMD) of −0·46 (95% CI −0·91 to −0·01) for the additive 
effect of behavioural activation.6 Given that the typical standard deviation of PHQ-9 is 
approximately 6, the iMD of −1·83 (95% CrI −2·90 to −0·80) for behavioural activation in 
our cNMA corresponds to a standardised effect size of −0·31 (95% CrI −0·48 to −0·13) and 
is largely consistent with the estimate of the systematic review.

The same systematic review found no additive effect of cognitive restructuring; the SMD 
based on three dismantling studies was −0·06 (95% CI −0·68 to 0·55).6 This result is again 
concordant with our current findings, which estimated the iMD for cognitive restructuring to 
be 0·30 (95% CrI −0·87 to 1·41), corresponding to a standardised effect size of 0·05 (95% 
CrI −0·15 to 0·24).

The non-specific treatment effects component had a robust additive effect of an iMD of 
−1·41 (95% CrI −2·52 to −0·30), corresponding to a standardised effect size of −0·24 
(95% CrI −0·42 to −0·05). In our decomposition model, the non-specific treatment effects 
component includes both the placebo effect and the common or non-specific psychotherapy 
factor,33,34 and can contribute to the efficacy of many bona fide treatments in comparison 
with non-active controls.

There was suggestive evidence that behaviour therapy for insomnia could be beneficial. 
However, this therapy was included as a component in only four studies and the estimates 
for its efficacy were imprecise. It must be pointed out that these four studies did not limit 
their participants to those having depression and insomnia. The effects of behaviour therapy 
for insomnia warrants further research.

By contrast, relaxation emerged as potentially harmful in our cNMA, with iMD of 1·20 
(95% CrI 0·17 to 2·27). We are aware of no dismantling study for relaxation in depression 
treatments. However, the cNMA of CBT for panic disorder has identified muscle relaxation 
as detrimental.7 There are various potential explanations for this. Relaxation tended to 
be included in CBT arms that included a greater number of skills, which might have 
allowed less time to learn and practise those particular skills and have reduced their efficacy. 
However, when we ran a sensitivity analysis limiting the included number of CBT skills 
per arm to four or fewer, the estimates were similar to those of the primary analysis. 
Relaxation might be conceived as working in the opposite direction of exposure, which 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 10

might be a principal therapeutic mechanism in anxiety, and behavioural activation, which 
might be a principal therapeutic mechanism in depression. Relaxation might also plausibly 
exert its effects by reducing hyperarousal symptoms but this reduction might have been 
unpleasant for patients with depression who already feel flat and under-aroused. In our 
network, relaxation exercises were included in 36 arms but the reports generally did not 
specify what patients actually did in each programme.

With regard to delivery formats of iCBT, we studied the effects of initial face-to-face 
contact, automated encouragement, human encouragement, and therapeutic guidance. We 
found that human encouragement in conjunction with automated encouragement decreases 
dropout from treatment (combined iOR 0·32 [95% CrI 0·13 to 0·93]; appendix p 73) and 
might be able to promote therapy efficacy (combined iMD −0·55 [95% CrI −1·75 to 0·65]; 
figure 3). Because human encouragement without reference to the therapeutic contents can 
be provided by trained lay people, these findings if replicated could increase scalability of 
iCBT.

The findings about therapeutic guidance might appear surprising given that guided iCBT 
has been shown to be superior to unguided iCBT,10 especially among patients with 
higher baseline severity of depression.35 In our decomposition, guided iCBT could involve 
human encouragement only or both human encouragement and therapeutic guidance; the 
additive effect of guidance could then be due to human encouragement or due to the 
combination of human encouragement plus therapeutic guidance when the baseline severity 
was high at 25 points; the incremental effect decreased when the baseline severity was 
lower. The component perspective also brought some insight into the nature of the current 
unguided iCBT programmes. These programmes often included relaxation as a component: 
14 (48%) of 29 programmes used relaxation when neither human encouragement nor 
therapeutic guidance was used, 13 (45%) of 29 programmes used relaxation when only 
human encouragement was used, but only nine (20%) of 44 programmes used relaxation 
when human encouragement plus therapeutic guidance were used (Fisher’s exact p=0·021; 
appendix pp 43–51). There might therefore be room for unguided iCBT itself to improve its 
efficacy by appropriately choosing the included components.

There are several important limitations to this study. First, the included studies were 
limited to iCBT. Any conclusions about specific efficacy of CBT skills therefore pertain 
to iCBT and will inform which components to include in the efficacious and efficient 
iCBT package, but such findings might not readily generalise to face-to-face CBT. For 
example, behavioural activation emerged as beneficial but cognitive restructuring did not 
in the current analyses, not because of these skills’ intrinsic efficacy but simply because 
of their ease of learning within iCBT. However, the concordance between our findings 
and those of face-to-face dismantling studies6 is encouraging. Similarly, our conclusions 
are applicable to the components and delivery modes as implemented in the included 
studies. There are potentially different ways for a particular component to be delivered 
and it is always possible that a specific form of the same component might prove to be 
efficacious. Second, although the median completion rate of the programme lessons was 
72% and, thus, we can assume that most participants had actually completed a majority 
of the included components, no data were available as to exactly which components were 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 11

completed and by whom. Our analysis considered components as being simply present or 
absent on the basis of the descriptions of each programme. In reality, components might 
have varied between programmes in terms of their length, depth, and content. Even when 
present, some components might have been less comprehensively executed than others—
eg, when they were offered later in the iCBT package than earlier or when they were 
presented along with many other components. Additionally, there is no guarantee that the 
completion of a component means that the participants had acquired the corresponding 
skill. The present analyses, therefore, can only speak to the effects of the decision to 
include particular components as their principal ones in the iCBT programme at the 
start of the treatment, as per the intention-to-treat principle of interpreting RCTs. To 
appreciate the effects of actual execution of the treatment, we would need more detailed 
data of individual participants’ adherence, their learned contents, and different analytical 
approaches.36 Third, several programmes had components not covered in the current 
scheme, including expressive writing, dreamwork, positive psychology, graded exposure, 
worry time, or physical exercises. Such trials might have had a slightly different focus, 
such as the transdiagnostic programme including graded exposure in which the same 
cognitive restructuring technique might have been presented slightly differently than when 
it is used mainly as a therapy for depression. A sensitivity analysis excluding trials 
that used such miscellaneous components, however, corroborated the primary analysis 
results. Fourth, there was indication of intransitivity for a comparison between cognitive 
therapy and attention or psychological placebo and of global inconsistency in the network. 
However, this intransitivity is unlikely to have affected the estimates for the components 
to a great extent, because the components included in the cognitive therapy and attention 
or psychological placebo comparison were also included in other comparisons. We only 
assessed the transitivity assumption for a small number of possible effect modifiers, thus, 
our network might have been confounded by unobserved imbalances across comparisons, 
such as antidepressant use and treatment duration. Fifth, when the individual participant data 
were pooled, there were only four commonly reported patient characteristics that we could 
analyse as prognostic factors or effect modifiers. Important potential effect modifiers, such 
as childhood adversities37 or baseline cognitive or behavioural skills,38 were therefore not 
included in our model. Researchers are encouraged to agree on essential measurements to be 
taken in future iCBT trials. Lastly, we assumed additivity of the component effects—ie, that 
for any given component (c), the relative effect of c plus X versus X only is the same for 
any X, where X represents any combination of components not including c. Thus, our results 
assumed no interactions between components. Although a post-hoc sensitivity analysis 
examining potential interactions among components provided similar results to the additive 
model, the study was possibly underpowered to detect interactions among components. 
Combinations of components can be justified only so far as they are clinically sensible. We 
must be careful when extrapolating the combinations beyond those examined in the current 
dataset: as more and more components are combined to build packages not explored in the 
trials included in this study, the uncertainty around the estimates increases, and possible 
deviations from our assumptions (eg, additivity of component effects) might have a bigger 
impact on the validity of our results than when we limit the combinations to those included 
in this study. More and larger studies varying in included components (eg, in the form of 
fully factorial trials39,40) are necessary to extend and consolidate the estimates.

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 12

The major strengths of the study are as follows. We used state-of-the-art evidence synthesis 
methods to elucidate specific efficacies of various skills and delivery methods of iCBT. The 
cNMA increased precision by including more studies than narrowly defined dismantling 
studies and by combining direct and indirect estimates. The included studies were generally 
of adequate quality except for the domains for which psychotherapy trials cannot escape 
possible biases due to unfeasibility of blinding. The decomposition of treatments sometimes 
called for subtle judgements and publications might have failed to provide enough 
information; with detailed definitions as described in the table and inquiries of the authors 
when necessary (see appendix pp 18–41 for results of our communications), we were able 
to achieve satisfactory to excellent inter-rater agreement. In the current network, there was 
no evidence of data availability bias for individual participant data or of publication bias of 
active treatments over the waiting list, the most frequent control condition. Lastly, by using 
individual participant data we were able to estimate relative efficacies of any combination of 
components based on patients’ baseline characteristics.

In conclusion, this individual participant data cNMA of iCBT has identified potentially 
helpful and less helpful components and delivery formats for reducing depression and 
enhancing adherence to the programme with suggestive evidence. Future iCBT packages 
aiming to be effective and efficient might include behavioural activation but not relaxation. 
Behavioural therapy for insomnia and problem solving might also be included in packages 
but cognitive restructuring would probably not be chosen. To boost adherence, automated 
encouragement and human encouragement might be used. Such packages have the potential 
to be more efficacious, less burdensome for users, and less demanding on provider 
resources, with the net effect of rendering iCBT even more scalable. However, readers 
should note that our analyses are limited by several important factors as previously 
outlined; moreover, the evidence supporting some of these recommendations, especially for 
cognitive restructuring, problem solving, or therapeutic guidance is still relatively imprecise, 
warranting further experimentations to refine iCBT packages.

Supplementary Material

Refer to Web version on PubMed Central for supplementary material.

Authors 

Toshi A Furukawa*,
Department of Health Promotion and Human Behavior, Kyoto University Graduate 
School of Medicine/School of Public Health, Kyoto, Japan

Aya Suganuma*,
Department of Health Promotion and Human Behavior, Kyoto University Graduate 
School of Medicine/School of Public Health, Kyoto, Japan

Edoardo G Ostinelli*,
Department of Psychiatry, Warneford Hospital, University of Oxford, Oxford, UK

Gerhard Andersson,

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 13

Department of Clinical Neuroscience, Centre for Psychiatry Research, Karolinska 
Institutet and Stockholm Health Care Services, Stockholm County Council, 
Stockholm, Sweden

Department of Behavioral Sciences and Learning, Linköping University, Linköping, 
Sweden

Christopher G Beevers,
Department of Psychology and Institute for Mental Health Research, University of 
Texas at Austin, Austin, TX, USA

Jason Shumake,
Department of Psychology and Institute for Mental Health Research, University of 
Texas at Austin, Austin, TX, USA

Thomas Berger,
Department of Clinical Psychology and Psychotherapy, University of Bern, Bern, 
Switzerland

Florien Willemijn Boele,
Patient Centred Outcomes Research Group, Leeds Institute of Medical Research at 
St James’s, University of Leeds, Leeds, UK

Claudia Buntrock,
Department of Clinical Psychology and Psychotherapy, Friedrich-Alexander-
University Erlangen-Nürnberg, Erlangen, Germany

Per Carlbring,
Department of Psychology, Stockholm University, Stockholm, Sweden

Isabella Choi,
Central Clinical School, Brain and Mind Centre, Faculty of Medicine and Health, 
University of Sydney, Sydney, NSW, Australia

Helen Christensen,
Black Dog Institute and University of New South Wales, Prince of Wales Hospital, 
Sydney, NSW, Australia

Andrew Mackinnon,
Black Dog Institute and University of New South Wales, Prince of Wales Hospital, 
Sydney, NSW, Australia

Jennifer Dahne,
Department of Psychiatry and Behavioral Sciences, Medical University of South 
Carolina, Charleston, SC, USA

Marcus J H Huibers,
Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

David D Ebert,

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 14

Department for Sport and Health Sciences, Chair for Psychology & Digital Mental 
Health Care, Technical University Munich, Germany

Louise Farrer,
Centre for Mental Health Research, The Australian National University, Canberra, 
Australia

Nicholas R Forand,
Department of Psychiatry, The Donald and Barbara Zucker School of Medicine at 
Hofstra/Northwell, Hempstead, NY, USA

Daniel R Strunk,
Department of Psychology, The Ohio State University, Columbus, OH, USA

Iony D Ezawa,
Department of Psychology, The Ohio State University, Columbus, OH, USA

Erik Forsell,
Department of Clinical Neuroscience, Centre for Psychiatry Research, Karolinska 
Institutet and Stockholm Health Care Services, Stockholm County Council, 
Stockholm, Sweden

Viktor Kaldo,
Department of Clinical Neuroscience, Centre for Psychiatry Research, Karolinska 
Institutet and Stockholm Health Care Services, Stockholm County Council, 
Stockholm, Sweden

Department of Psychology, Faculty of Health and Life Sciences, Linnaeus 
University, Växjö, Sweden

Anna Geraedts,
Soulve Innovations, Utrecht, Netherlands

Simon Gilbody,
Department of Health Sciences, University of York, York, UK

Elizabeth Littlewood,
Department of Health Sciences, University of York, York, UK

Sally Brabyn,
Department of Health Sciences, University of York, York, UK

Heather D Hadjistavropoulos,
Department of Psychology, University of Regina, Regina, SK, Canada

Luke H Schneider,
Anxiety Treatment and Research Clinic, St Joseph’s Healthcare Hamilton, Hamilton, 
ON, Canada

Robert Johansson,
Department of Psychology, Stockholm University, Stockholm, Sweden

Robin Kenter,

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 15

Department of Clinical Psychology, Faculty of Psychology, University of Bergen, 
Bergen, Norway

Marie Kivi,
Department of Psychology, University of Gothenburg, Gothenburg, Sweden

Cecilia Björkelund,
Primary Health Care, School of Public Health and Community Medicine, Institute of 
Medicine, University of Gothenburg, Gothenburg, Sweden

Annet Kleiboer,
Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Heleen Riper,
Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Jan Philipp Klein,
Department of Psychiatry and Psychotherapy, Luebeck University, Luebeck, 
Germany

Johanna Schröder,
Institute for Sex Research, Sexual Medicine and Forensic Psychiatry, University 
Medical Center Hamburg-Eppendorf, Hamburg, Germany

Björn Meyer,
Research Department, GAIA AG, Hamburg, Germany

Steffen Moritz,
Department of Psychiatry and Psychotherapy, University Medical Center Hamburg-
Eppendorf, Hamburg, Germany

Lara Bücker,
Department of Psychiatry and Psychotherapy, University Medical Center Hamburg-
Eppendorf, Hamburg, Germany

Ove Lintvedt,
Norwegian Center for E-health research, Tromsø, Norway

Peter Johansson,
Department of Health, Medicine and Caring Sciences, Linköping University, 
Norrköping, Sweden

Johan Lundgren,
Department of Health, Medicine and Caring Sciences, Linköping University, 
Norrköping, Sweden

Jeannette Milgrom,
Parent-Infant Research Institute and Austin Health, Melbourne School of 
Psychological Sciences, University of Melbourne, VIC, Australia

Alan W Gemmill,

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 16

Parent-Infant Research Institute and Austin Health, Melbourne School of 
Psychological Sciences, University of Melbourne, VIC, Australia

David C Mohr,
Center for Behavioral Intervention Technologies, Department of Preventive 
Medicine, Northwestern University, Chicago, IL, USA

Jesus Montero-Marin,
Department of Psychiatry, Warneford Hospital, University of Oxford, Oxford, UK

Javier Garcia-Campayo,
Aragon Institute for Health Research, Miguel Servet University Hospital, Zaragoza, 
Spain

Primary Care Prevention and Health Promotion Research Network, RedIAPP, 
Madrid, Spain

Stephanie Nobis,
Klinikum Osnabrück, Osnabrück, Germany

Anna-Carlotta Zarski,
Department of Clinical Psychology and Psychotherapy, Friedrich-Alexander-
University Erlangen-Nürnberg, Erlangen, Germany

Kathleen O’Moore,
Black Dog Institute and University of New South Wales, Prince of Wales Hospital, 
Sydney, NSW, Australia

Alishia D Williams,
Department of Psychology, Faculty of Science, The University of New South Wales, 
Sydney, NSW, Australia

Jill M Newby,
School of Psychology, University of New South Wales at the Black Dog Institute, 
Sydney, NSW, Australia

Sarah Perini,
Clinical Research Unit for Anxiety and Depression, St Vincent’s Hospital, Sydney, 
NSW, Australia

Rachel Phillips,
Faculty of Medicine, School of Public Health, Imperial College London, London, UK

Justine Schneider,
School of Sociology & Social Policy and Institute of Mental Health, University of 
Nottingham, Nottingham, UK

Wendy Pots,
Department of Psychology, Health & Technology, University of Twente, Enschede, 
Netherlands

Nicole E Pugh,
Private practice, Vancouver, BC, Canada

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 17

Derek Richards,
University of Dublin, Trinity College, School of Psychology, E-mental Health 
Research Group, Dublin, Ireland

SilverCloud Health, Clinical Research & Innovation, Dublin, Ireland

Isabelle M Rosso,
McLean Hospital, Belmont, MA, USA

Scott L Rauch,
McLean Hospital, Belmont, MA, USA

Lisa B Sheeber,
Oregon Research Institute, Eugene, OR, USA

Jessica Smith,
Imperial Clinical Trials Unit, Imperial College London, London, UK

Viola Spek,
School of Applied Psychology, Fontys University of Applied Science, Eindhoven, 
Netherlands

Victor J Pop, MD,
Department of Medical & Clinical Psychology, Tilburg University, Tilburg, 
Netherlands

Burçin Ünlü,
PsyQ Online, Haarlem, Netherlands

Kim M P van Bastelaar,
Amsterdam University Medical Centre, Amsterdam, Netherlands

Sanne van Luenen,
Department of Clinical Psychology, Leiden University, Leiden, Netherlands

Nadia Garnefski,
Department of Clinical Psychology, Leiden University, Leiden, Netherlands

Vivian Kraaij,
Department of Clinical Psychology, Leiden University, Leiden, Netherlands

Kristofer Vernmark,
Department of Behavioral Sciences and Learning, Linköping University, Linköping, 
Sweden

Lisanne Warmerdam,
National Health Care Institute, Diemen, Netherlands

Annemieke van Straten,
Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Pavle Zagorscak,
Department of Education and Psychology, Freie Universität Berlin, Berlin, Germany

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 18

Christine Knaevelsrud,
Department of Education and Psychology, Freie Universität Berlin, Berlin, Germany

Manuel Heinrich,
Department of Education and Psychology, Freie Universität Berlin, Berlin, Germany

Clara Miguel,
Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Andrea Cipriani,
Department of Psychiatry, Warneford Hospital, University of Oxford, Oxford, UK

Oxford Health NHS Foundation Trust, Warneford Hospital, Oxford, UK

Orestis Efthimiou†,
Department of Psychiatry, Warneford Hospital, University of Oxford, Oxford, UK

Institute of Social and Preventive Medicine, University of Bern, Bern, Switzerland

Eirini Karyotaki†,
Department of Global Health and Social Medicine, Harvard Medical School, Boston, 
MA, USA

Pim Cuijpers†
Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Affiliations

Department of Health Promotion and Human Behavior, Kyoto University Graduate 
School of Medicine/School of Public Health, Kyoto, Japan

Department of Health Promotion and Human Behavior, Kyoto University Graduate 
School of Medicine/School of Public Health, Kyoto, Japan

Department of Psychiatry, Warneford Hospital, University of Oxford, Oxford, UK

Department of Clinical Neuroscience, Centre for Psychiatry Research, Karolinska 
Institutet and Stockholm Health Care Services, Stockholm County Council, 
Stockholm, Sweden

Department of Behavioral Sciences and Learning, Linköping University, Linköping, 
Sweden

Department of Psychology and Institute for Mental Health Research, University of 
Texas at Austin, Austin, TX, USA

Department of Psychology and Institute for Mental Health Research, University of 
Texas at Austin, Austin, TX, USA

Department of Clinical Psychology and Psychotherapy, University of Bern, Bern, 
Switzerland

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 19

Patient Centred Outcomes Research Group, Leeds Institute of Medical Research at 
St James’s, University of Leeds, Leeds, UK

Department of Clinical Psychology and Psychotherapy, Friedrich-Alexander-
University Erlangen-Nürnberg, Erlangen, Germany

Department of Psychology, Stockholm University, Stockholm, Sweden

Central Clinical School, Brain and Mind Centre, Faculty of Medicine and Health, 
University of Sydney, Sydney, NSW, Australia

Black Dog Institute and University of New South Wales, Prince of Wales Hospital, 
Sydney, NSW, Australia

Black Dog Institute and University of New South Wales, Prince of Wales Hospital, 
Sydney, NSW, Australia

Department of Psychiatry and Behavioral Sciences, Medical University of South 
Carolina, Charleston, SC, USA

Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Department for Sport and Health Sciences, Chair for Psychology & Digital Mental 
Health Care, Technical University Munich, Germany

Centre for Mental Health Research, The Australian National University, Canberra, 
Australia

Department of Psychiatry, The Donald and Barbara Zucker School of Medicine at 
Hofstra/Northwell, Hempstead, NY, USA

Department of Psychology, The Ohio State University, Columbus, OH, USA

Department of Psychology, The Ohio State University, Columbus, OH, USA

Department of Clinical Neuroscience, Centre for Psychiatry Research, Karolinska 
Institutet and Stockholm Health Care Services, Stockholm County Council, 
Stockholm, Sweden

Department of Clinical Neuroscience, Centre for Psychiatry Research, Karolinska 
Institutet and Stockholm Health Care Services, Stockholm County Council, 
Stockholm, Sweden

Department of Psychology, Faculty of Health and Life Sciences, Linnaeus 
University, Växjö, Sweden

Soulve Innovations, Utrecht, Netherlands

Department of Health Sciences, University of York, York, UK

Department of Health Sciences, University of York, York, UK

Department of Health Sciences, University of York, York, UK

Department of Psychology, University of Regina, Regina, SK, Canada

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 20

Anxiety Treatment and Research Clinic, St Joseph’s Healthcare Hamilton, Hamilton, 
ON, Canada

Department of Psychology, Stockholm University, Stockholm, Sweden

Department of Clinical Psychology, Faculty of Psychology, University of Bergen, 
Bergen, Norway

Department of Psychology, University of Gothenburg, Gothenburg, Sweden

Primary Health Care, School of Public Health and Community Medicine, Institute of 
Medicine, University of Gothenburg, Gothenburg, Sweden

Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Department of Psychiatry and Psychotherapy, Luebeck University, Luebeck, 
Germany

Institute for Sex Research, Sexual Medicine and Forensic Psychiatry, University 
Medical Center Hamburg-Eppendorf, Hamburg, Germany

Research Department, GAIA AG, Hamburg, Germany

Department of Psychiatry and Psychotherapy, University Medical Center Hamburg-
Eppendorf, Hamburg, Germany

Department of Psychiatry and Psychotherapy, University Medical Center Hamburg-
Eppendorf, Hamburg, Germany

Norwegian Center for E-health research, Tromsø, Norway

Department of Health, Medicine and Caring Sciences, Linköping University, 
Norrköping, Sweden

Department of Health, Medicine and Caring Sciences, Linköping University, 
Norrköping, Sweden

Parent-Infant Research Institute and Austin Health, Melbourne School of 
Psychological Sciences, University of Melbourne, VIC, Australia

Parent-Infant Research Institute and Austin Health, Melbourne School of 
Psychological Sciences, University of Melbourne, VIC, Australia

Center for Behavioral Intervention Technologies, Department of Preventive 
Medicine, Northwestern University, Chicago, IL, USA

Department of Psychiatry, Warneford Hospital, University of Oxford, Oxford, UK

Aragon Institute for Health Research, Miguel Servet University Hospital, Zaragoza, 
Spain

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 21

Primary Care Prevention and Health Promotion Research Network, RedIAPP, 
Madrid, Spain

Klinikum Osnabrück, Osnabrück, Germany

Department of Clinical Psychology and Psychotherapy, Friedrich-Alexander-
University Erlangen-Nürnberg, Erlangen, Germany

Black Dog Institute and University of New South Wales, Prince of Wales Hospital, 
Sydney, NSW, Australia

Department of Psychology, Faculty of Science, The University of New South Wales, 
Sydney, NSW, Australia

School of Psychology, University of New South Wales at the Black Dog Institute, 
Sydney, NSW, Australia

Clinical Research Unit for Anxiety and Depression, St Vincent’s Hospital, Sydney, 
NSW, Australia

Faculty of Medicine, School of Public Health, Imperial College London, London, UK

School of Sociology & Social Policy and Institute of Mental Health, University of 
Nottingham, Nottingham, UK

Department of Psychology, Health & Technology, University of Twente, Enschede, 
Netherlands

Private practice, Vancouver, BC, Canada

University of Dublin, Trinity College, School of Psychology, E-mental Health 
Research Group, Dublin, Ireland

SilverCloud Health, Clinical Research & Innovation, Dublin, Ireland

McLean Hospital, Belmont, MA, USA

McLean Hospital, Belmont, MA, USA

Oregon Research Institute, Eugene, OR, USA

Imperial Clinical Trials Unit, Imperial College London, London, UK

School of Applied Psychology, Fontys University of Applied Science, Eindhoven, 
Netherlands

Department of Medical & Clinical Psychology, Tilburg University, Tilburg, 
Netherlands

PsyQ Online, Haarlem, Netherlands

Amsterdam University Medical Centre, Amsterdam, Netherlands

Department of Clinical Psychology, Leiden University, Leiden, Netherlands

Department of Clinical Psychology, Leiden University, Leiden, Netherlands

Department of Clinical Psychology, Leiden University, Leiden, Netherlands

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 22

Department of Behavioral Sciences and Learning, Linköping University, Linköping, 
Sweden

National Health Care Institute, Diemen, Netherlands

Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Department of Education and Psychology, Freie Universität Berlin, Berlin, Germany

Department of Education and Psychology, Freie Universität Berlin, Berlin, Germany

Department of Education and Psychology, Freie Universität Berlin, Berlin, Germany

Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Department of Psychiatry, Warneford Hospital, University of Oxford, Oxford, UK

Oxford Health NHS Foundation Trust, Warneford Hospital, Oxford, UK

Department of Psychiatry, Warneford Hospital, University of Oxford, Oxford, UK

Institute of Social and Preventive Medicine, University of Bern, Bern, Switzerland

Department of Global Health and Social Medicine, Harvard Medical School, Boston, 
MA, USA

Department of Clinical, Neuro and Developmental Psychology, Vrije Universiteit 
Amsterdam, Amsterdam, Netherlands

Acknowledgments

This study was supported, in part, by the Japan Society for the Promotion of Science grant-in-aid for scientific 
research (grant number 17K19808) to TAF. EGO is supported by the National Institute for Health Research (NIHR) 
Oxford Cognitive Health Clinical Research Facility and by the NIHR Oxford Health Biomedical Research Centre 
(grant BRC-1215–20005). JD is supported by the National Institute on Drug Abuse (NIDA K23 DA045766). 
HDH is supported by the Canadian Institutes of Health Research (152917). DCM is supported by grants from 
the National Institute of Mental Health (P50 MH119029, R01 MH111610). AC is supported by the NIHR Oxford 
Cognitive Health Clinical Research Facility, by an NIHR Research Professorship (grant RP-2017–08ST2–006), 
the NIHR Oxford and Thames Valley Applied Research Collaboration, and the NIHR Oxford Health Biomedical 
Research Centre (grant BRC-1215–20005). OE was supported by project grant number 180083 from the Swiss 
National Science Foundation. EK was supported by the Netherlands Organisation for Health Research and 
Development (project number 019.182SG.001). The views expressed are those of the authors and not necessarily 
those of any of the funding agencies listed here.

Declaration of interests

TAF reports grants from Japan Society for Promotion of Science, during the conduct of the study; grants 
and personal fees from Mitsubishi-Tanabe, personal fees from MSD, grants and personal fees from Shionogi, 
outside the submitted work; a patent 2018–177688 concerning smartphone CBT apps pending; and an intellectual 
properties for Kokoro-app licensed to Tanabe-Mitsubishi. AC reports personal fees from Italian Network for 
Paediatric Trials and CARIPLO Foundation; and grants and personal fees from Angelini Pharma, outside the 
submitted work. EGO reports personal fees from Angelini Pharma, outside the submitted work. PCa reports 
personal fees from Osmond Foundation and Sandoz, outside the submitted work. JD is co-owner of Behavioral 
Activation Tech LLC, a small business that develops and evaluates mobile app-based treatments for depression and 
co-occurring disorders. DDE has served as a consultant to or on the scientific advisory boards of Sanofi, Novartis, 
Minddistrict, Lantern, Schoen Kliniken, Ideamed, German health insurance companies (BARMER, Techniker 
Krankenkasse), and a number of federal chambers for psychotherapy; is a stakeholder of the Institute for health 
training online (GET.ON), which aims to implement scientific findings related to digital health interventions into 
routine care. NRF is an employee of AbleTo. JPK reports grants and personal fees from Servier; personal fees 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 23

from Beltz, Elsevier, Hogrefe, and Springer, outside the submitted work; funding for clinical trials (German Federal 
Ministry of Health and Servier); payments for presentations on internet interventions (Servier); and payments 
for workshops and books (Beltz, Elsevier, Hogrefe, and Springer) on psychotherapy for chronic depression and 
on psychiatric emergencies. BM is an employee of GAIA AG. DCM reports personal fees from Apple, Pear 
Therapeutics, and Otsuka Pharmaceuticals and has an equity interest in Adaptive Health, outside the submitted 
work. JMM is supported by a Wellcome Trust Grant (104908/Z/14/Z). SN is an employee of GET.ON Institut. 
DR is an employee of SilverCloud Health. LBS is an employee of Influents Innovations. PZ reports grants 
and non-financial support from Techniker Krankenkasse (German public health insurance company), outside the 
submitted work. CK reports personal fees from Oberbergklinik and Servier; and grants and non-financial support 
from Techniker Krankenkasse, outside the submitted work. MH reports grants and non-financial support from 
Techniker Krankenkasse, outside the submitted work. All other authors declare no competing interests.

References

1. Barth J, Munder T, Gerger H, et al. Comparative efficacy of seven psychotherapeutic interventions 
for patients with depression: a network meta-analysis. PLoS Med 2013; 10: e1001454. [PubMed: 
23723742] 

2. Cuijpers P, Karyotaki E, de Wit L, Ebert DD. The effects of fifteen evidence-supported therapies for 

adult depression: a meta-analytic review. Psychother Res 2019; 30: 1–15.

3. Institute of Medicine. Psychosocial interventions for mental and substance use disorders: a 

framework for establishing evidence-based standards. Washington, DC: The National Academies 
Press, 2015.

4. Ahn H, Wampold BE. Where oh where are the specific ingredients? A meta-analysis of component 

studies in counseling and psychotherapy. J Couns Psychol 2001; 48: 251–57.

5. Bell EC, Marcus DK, Goodlad JK. Are the parts as good as the whole? A meta-analysis of 

component treatment studies. J Consult Clin Psychol 2013; 81: 722–36. [PubMed: 23688145] 
6. Cuijpers P, Cristea IA, Karyotaki E, Reijnders M, Hollon SD. Component studies of psychological 
treatments of adult depression: a systematic review and meta-analysis. Psychother Res 2017; 29: 
1–15. [PubMed: 29254460] 

7. Pompoli A, Furukawa TA, Efthimiou O, Imai H, Tajika A, Salanti G. Dismantling cognitive-

behaviour therapy for panic disorder: a systematic review and component network meta-analysis. 
Psychol Med 2018; 48: 1945–53. [PubMed: 29368665] 

8. López-López JA, Davies SR, Caldwell DM, et al. The process and delivery of CBT for depression in 
adults: a systematic review and network meta-analysis. Psychol Med 2019; 49: 1937–47. [PubMed: 
31179960] 

9. Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis 
of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 
2009; 169: 1158–65. [PubMed: 19258485] 

10. Cuijpers P, Noma H, Karyotaki E, Cipriani A, Furukawa TA. Effectiveness and acceptability of 
cognitive behavior therapy delivery formats in adults with depression: a network meta-analysis. 
JAMA Psychiatry 2019; 76: 700–07. [PubMed: 30994877] 

11. Wagner B, Horn AB, Maercker A. Internet-based versus face-to-face cognitive-behavioral 

intervention for depression: a randomized controlled non-inferiority trial. J Affect Disord 2014; 
152–154: 113–21.

12. Karyotaki E, Ebert DD, Donkin L, et al. Do guided internet-based interventions result in clinically 

relevant changes for patients with depression? An individual participant data meta-analysis. Clin 
Psychol Rev 2018; 63: 80–92. [PubMed: 29940401] 

13. Cuijpers P, Karyotaki E, Ciharova M. A meta-analytic database of randomised trials on 
psychotherapies for depression. 2020. https://osf.io/825c6/ (accessed March 16, 2021).

14. Watts SE, Turnell A, Kladnitski N, Newby JM, Andrews G. Treatment-as-usual (TAU) is anything 

but usual: a meta-analysis of CBT versus TAU for anxiety and depression. J Affect Disord 2015; 
175: 152–67. [PubMed: 25618002] 

15. Cuijpers P, Quero S, Papola D, Cristea IA, Karyotaki E. Care-as-usual control groups across 

different settings in randomized trials on psychotherapy for adult depression: a meta-analysis. 
Psychol Med 2019; published online Dec 17. 10.1017/S0033291719003581.

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 24

16. Roemer L, Erisman SM, Orsillo SM. Mindfulness and acceptance-based treatments for anxiety 

disorders. In: Antony MM, Stein MB, eds. Oxford Handbook of Anxiety and Related Disorders. 
Oxford: Oxford University Press, 2008: 476–87.

17. Sterne JAC, Savović J, Page MJ, et al. RoB 2: a revised tool for assessing risk of bias in 

randomised trials. BMJ 2019; 366: l4898. [PubMed: 31462531] 

18. Furukawa TA, Karyotaki E, Suganuma A, et al. Dismantling, personalising and optimising internet 
cognitive-behavioural therapy for depression: a study protocol for individual participant data 
component network meta-analysis. BMJ Open 2019; 8: e026137.

19. Hutton B, Salanti G, Caldwell DM, et al. The PRISMA extension statement for reporting of 

systematic reviews incorporating network meta-analyses of health care interventions: checklist and 
explanations. Ann Intern Med 2015; 162: 777–84. [PubMed: 26030634] 

20. Stewart LA, Clarke M, Rovers M, et al. Preferred reporting items for systematic review and meta-
analyses of individual participant data: the PRISMA-IPD statement. JAMA 2015; 313: 1657–65. 
[PubMed: 25919529] 

21. Kroenke K, Spitzer RL, Williams JB. The PHQ-9: validity of a brief depression severity measure. J 

Gen Intern Med 2001; 16: 606–13. [PubMed: 11556941] 

22. Wahl I, Löwe B, Bjorner JB, et al. Standardization of depression measurement: a common 

metric was developed for 11 self-report depression measures. J Clin Epidemiol 2014; 67: 73–86. 
[PubMed: 24262771] 

23. Furukawa TA, Reijnders M, Kishimoto S, et al. Translating the BDI and BDI-II into the HAMD 
and vice versa with equipercentile linking. Epidemiol Psychiatr Sci 2019; 29: e24. [PubMed: 
30867082] 

24. Rücker G, Krahn U, König J, Efthimiou O, Schwarzer G. netmeta: network meta-analysis using 

frequentist methods. 2019. https://github.com/guido-s/netmeta (accessed April 23, 2021).

25. Efthimiou O, Debray TP, van Valkenhoef G, et al. GetReal in network meta-analysis: a review of 

the methodology. Res Synth Methods 2016; 7: 236–63. [PubMed: 26754852] 

26. König J, Krahn U, Binder H. Visualizing the flow of evidence in network meta-analysis and 

characterizing mixed treatment comparisons. Stat Med 2013; 32: 5414–29. [PubMed: 24123165] 

27. White IR, Barrett JK, Jackson D, Higgins JP. Consistency and inconsistency in network meta-

analysis: model estimation using multivariate meta-regression. Res Synth Methods 2012; 3: 111–
25. [PubMed: 26062085] 

28. Seo M, White IR, Furukawa TA, et al. Comparing methods for estimating patient-specific 

treatment effects in individual patient data meta-analysis. Stat Med 2020; 40: 1553–73. [PubMed: 
33368415] 

29. Beevers CG, Pearson R, Hoffman JS, Foulser AA, Shumake J, Meyer B. Effectiveness of an 

internet intervention (Deprexis) for depression in a united states adult sample: a parallel-group 
pragmatic randomized controlled trial. J Consult Clin Psychol 2017; 85: 367–80. [PubMed: 
28230390] 

30. Day V, McGrath PJ, Wojtowicz M. Internet-based guided self-help for university students with 
anxiety, depression and stress: a randomized controlled clinical trial. Behav Res Ther 2013; 51: 
344–51. [PubMed: 23639300] 

31. Veroniki AA, Vasiliadis HS, Higgins JP, Salanti G. Evaluation of inconsistency in networks of 

interventions. Int J Epidemiol 2013; 42: 332–45. [PubMed: 23508418] 

32. Seo M, Furukawa TA, Veroniki AA, et al. The Kilim plot: a tool for visualizing network meta-

analysis results for multiple outcomes. Res Synth Methods 2021; 12: 86–95. [PubMed: 32524754] 

33. Wampold BE. How important are the common factors in psychotherapy? An update. World 

Psychiatry 2015; 14: 270–77. [PubMed: 26407772] 

34. Cuijpers P, Reijnders M, Huibers MJH. The role of common factors in psychotherapy outcomes. 

Annu Rev Clin Psychol 2019; 15: 207–31. [PubMed: 30550721] 

35. Karyotaki E, Efthimiou O, Miguel C, et al. Internet-based cognitive behavioral therapy for 
depression: a systematic review and individual patient data network meta-analysis. JAMA 
Psychiatry 2021; published online Jan 20. 10.1001/jamapsychiatry.2020.4364.

36. Hernán MA, Hernández-Díaz S. Beyond the intention-to-treat in comparative effectiveness 

research. Clin Trials 2012; 9: 48–55. [PubMed: 21948059] 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 25

37. Nemeroff CB, Heim CM, Thase ME, et al. Differential responses to psychotherapy versus 

pharmacotherapy in patients with chronic forms of major depression and childhood trauma. Proc 
Natl Acad Sci USA 2003; 100: 14293–96. [PubMed: 14615578] 

38. Cheavens JS, Strunk DR, Lazarus SA, Goldstein LA. The compensation and capitalization models: 
a test of two approaches to individualizing the treatment of depression. Behav Res Ther 2012; 50: 
699–706. [PubMed: 22982085] 

39. Uwatoko T, Luo Y, Sakata M, et al. Healthy campus trial: a multiphase optimization strategy 

(MOST) fully factorial trial to optimize the smartphone cognitive behavioral therapy (CBT) app 
for mental health promotion among university students: study protocol for a randomized controlled 
trial. Trials 2018; 19: 353. [PubMed: 29973252] 

40. Watkins E, Newbold A, Tester-Jones M, et al. Implementing multifactorial psychotherapy research 
in online virtual environments (IMPROVE-2): study protocol for a phase III trial of the MOST 
randomized component selection method for internet cognitive-behavioural therapy for depression. 
BMC Psychiatry 2016; 16: 345. [PubMed: 27716200] 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 26

Evidence before this study

Research in context

Psychotherapy is a complex intervention, comprising multiple components in various 
combinations. There are two types of research to disentangle specific contributions of 
psychotherapy components: so-called dismantling studies and, more recently, component 
network meta-analyses. We searched PubMed from inception to Oct 9, 2020, for relevant 
reviews with the following terms in titles and abstracts: (“Mental Disorders”[Mesh] 
“Psychotherapy”[Mesh] dismantl*) and (“Mental Disorders”[Mesh] “Psychotherapy”
[Mesh] component network meta-analysis). We identified three systematic reviews of 
dismantling studies and two component network meta-analyses. Earlier reviews of 
dismantling studies found no additive effects of specific components among dismantling 
studies; however, the most recent review focusing on depression found behavioural 
activation, but not cognitive restructuring or mindfulness, to have significant additive 
effects. A component network meta-analysis of face-to-face cognitive behavioural 
therapy (CBT) for panic disorder singled out muscle relaxation to be harmful; a 
component network meta-analysis of CBT for depression found no evidence of specific 
effects of any components or their combinations.

Added value of this study

Three new features strengthened the precision, sensitivity, and clinical relevance of 
our study. First, component network meta-analysis increased precision of estimates by 
including more studies than narrowly defined dismantling studies and by combining 
direct and indirect estimates while maintaining randomised comparisons. Second, by 
focusing on iCBT, we could be certain that the components had been offered and 
made accessible as intended by the researchers, in contrast to face-to-face CBT, for 
which the contents might have been modified or skipped when its conduct was not 
well monitored. Third, the use of individual participant data allowed us to identify 
prognostic factors and effect modifiers and thus estimate personalised relative effects 
among different interventions, depending on individual patients’ characteristics. We 
found suggestive evidence that non-specific treatment effects (including placebo effect 
and common factors) and behavioural activation might have beneficial effects, whereas 
relaxation might be detrimental. Combining human encouragement to proceed with the 
iCBT programme with automated encouragement decreased the number of patients who 
dropped out from treatment. We developed a web app that estimates relative efficacies 
between any two combinations of components based on baseline patient characteristics.

Implications of all the available evidence

Future iCBT packages aiming to be effective and efficient might include behavioural 
activation but not relaxation. These packages might further include behaviour therapy 
for insomnia and problem solving, but probably not cognitive restructuring. Automated 
encouragement could be used in iCBT packages along with human encouragement to 
increase adherence. Our web app can facilitate shared decision making by therapist and 
patient in choosing their preferred iCBT package.

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 27

Panel: Components, their definitions, and the number of trial arms 
including each component

Waiting component; 52 arms

Participants know that they can receive an active treatment, after a waiting phase. 
Usually patients on a waiting list do not receive any treatment during the waiting phase. 
However, in some trials the patients allocated to a waiting list received some non-specific 
therapeutic components, such as psychological placebo, psychoeducation, or treatment as 
usual. In such cases, we assumed that the waiting component was present, recorded the 
interventions provided while waiting, and classified such an arm as waiting list.

Conventional drug treatment; 143 arms

Treatment as usual or care as usual can denote many different conditions in the 
literature.14,15 In this study we focused on the use of conventional drug treatment and 
extracted the data on whether conventional drug treatment was present (drug treatment 
was part of the protocol treatment), allowed, or absent. When the drug was used to the 
same extent in both arms, the conventional drug treatment component was assumed to be 
present.

Non-specific treatment effects; 142 arms

Effects of an intervention due to the patients’ belief that they are receiving some form of 
treatment (placebo effect) and to the common or non-specific factors of psychotherapies. 
These two elements were indistinguishable in the current network of psychotherapies.

Psychoeducation about depression; 111 arms

Provision of information about the cause and nature of depression. Patients are taught 
their symptoms can be interpreted under a particular psychopathological model. For 
example, if cognitive distortion is cited as the cause of depression, such an explanation 
was counted towards the psychoeducation about depression component as defined here. 
We considered psychoeducation to be present only if there was a dedicated module 
(psychoeducation or introductory). Advice about lifestyle modification (eg, exercise, 
food, sleep hygiene as opposed to cognitive behavioural therapy [CBT] for insomnia) or 
provision of information about depression in informational websites were regarded as a 
form of psychoeducation.

Cognitive restructuring; 74 arms

This component teaches the patient to evaluate and modify their own irrational, 
maladaptive, or dysfunctional thoughts using strategies such as Socratic questioning and 
guided imagery.

Behavioural activation; 84 arms

This component aims to help people increase potentially reinforcing experiences through 
activity scheduling and increased engagement in pleasant activities.

Interpersonal skills training; 31 arms

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 28

Training in appropriate social behaviours. Includes assertiveness training, which teaches 
the patient to stand up for their own rights by expressing their feelings and wishes in an 
honest and respectful manner that does not insult or hurt others.

Problem solving; 55 arms

This skill includes the following step-by-step approach to personal problems: defining 
personal problems, generating multiple solutions, selecting the best solution, working out 
a systematic plan for this solution, and evaluating whether the solution has resolved the 
problem.

Relaxation; 36 arms

This skill is aimed at reducing general tension through induction of a relaxed body state. 
The most common techniques are Jacobson’s progressive muscle relaxation and applied 
relaxation.

Third-wave components; 14 arms

Various techniques are aimed at helping patients to develop more adaptive emotional 
responses to situations, such as the ability to observe symptomatic processes without 
overly identifying with them or without reacting to them in ways that cause further 
distress.16 Some typical examples are training in mindfulness, self-compassion, or 
acceptance.

Behaviour therapy for insomnia; 4 arms

This skill aims at treating chronic insomnia based on the principles of sleep restriction 
and stimulus control. This skill might also involve cognitive restructuring around 
maladaptive beliefs for sleep or teaching sleep hygiene; however, sleep hygiene only 
would count towards lifestyle modification and would be included in the psychoeducation 
about depression component.

Relapse prevention; 62 arms

Review of learned skills and listing action plans for foreseeable future problems based 
on the skills learned. An explanation of relapse in depression only would be counted as 
the psychoeducation about depression component; to qualify for the relapse prevention 
component, more participation is needed from the patient.

Homework required; 68 arms

When completion of some homework assignment is required (or explicitly encouraged 
repeatedly) before proceeding with the programme, either checked by humans or 
mandated by a computer program. The homework must pertain to an exercise in applying 
the learned CBT or other skills related to the participant’s own situation and must require 
some active participation from the participant. Simple reviewing of the materials or 
further reading were not regarded as homework.

Initial face-to-face contact; 57 arms

Initial face-to-face human contact, such as the initial evaluation session or the initial 
orientation session, is present. We also considered this component to be present when 

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 29

the patients were receiving conventional drug treatment and the doctors were aware that 
the patients were in the trial, or when the patients were referred from their general 
practitioner for the trial.

Automated encouragement to proceed with internet cognitive behavioural therapy 
(iCBT); 48 arms

Provision of automated, fixed prompts or encouragements to proceed with the treatment 
programme. Such prompts should not contain any support related to the therapeutic 
contents.

Human encouragement to proceed with iCBT; 73 arms

Prompts or encouragements are prepared and provided by human beings to proceed 
with the treatment programme via telephone or email. Such prompts should not contain 
any support related to the therapeutic contents. Peer support such as discussion groups 
counted towards this component.

Therapeutic guidance for iCBT; 44 arms

Guidance regarding the contents of iCBT. Therapeutic guidance related to the treatment 
content could be provided on a scheduled basis or as needed. Provision of technical 
support only did not count toward this component.

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 30

Figure 1: Network diagram
The width of the lines is proportional to the number of comparisons, which is given on each 
line.

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 31

Figure 2: Relative effects (mean differences in PHQ-9 scores with 95% CIs) of internet cognitive 
behavioural therapy of depression
Treatments (listed in alphabetical order) are shown in grey, direct effects (pairwise meta-
analyses) are shown in blue, and the network meta-analysis results are shown in red. 
Common heterogeneity τ was estimated to be 1·1 in terms of the PHQ-9 scores. An 
effect size of less than 0 in the network meta-analysis results shows that the treatment 
in the column is favoured (ie, lower PHQ-9 scores) versus the treatment in the row. 
An effect size of less than 0 in the pariwise meta-analyses results shows that the 
treatment in the row is favoured versus the treatment in the column. 3W=third-wave 
cognitive behavioural therapy. APP=attention or psychological placebo. BA=behavioural 
activation. CBT=cognitive behavioural therapy. CT=cognitive therapy. NT=no treatment. 
PE=psychoeducation. PHQ-9=Personal Health Questionnaire-9. PST=problem-solving 
therapy. TAU=treatment as usual. WL=waiting list.

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Furukawa et al.

Page 32

Figure 3: Individual participant data component network meta-analysis for depression severity
Potentially beneficial components are shown in green (darker green for stronger statistical 
evidence) and potentially harmful components are shown in red according to an index 
similar to the Z-score (median of the posterior distribution divided by the corresponding 
standard deviation for Bayesian analyses), thus taking account of the magnitude of the effect 
estimates and their uncertainty.32 More details about the colouring scheme are provided 
in the appendix (p 68). The specific efficacy for conventional drug treatment could not 
be estimated because this component was either present or absent in all comparisons in 
the network. Common heterogeneity τ was estimated to be 1·20 (95%CrI 0·89 to 1·57) in 
terms of the PHQ-9 scores. iCBT=internet cognitive behavioural therapy. iMD=incremental 
mean difference. CrI=credible interval. PHQ-9=Patient Health Questionnaire-9. *0=female 
and 1=male. †0=not in a relationship (single, separated, divorced, or widowed) and 1=in a 
relationship (married or having a stable partner).

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

 
 
 
 
Furukawa et al.

Page 33

Conceptualisation of internet cognitive behavioural therapy or control conditions from the component 
perspective

Table:

Cognitive behavioural therapy

ns ± pe ± re + cr + (ba ± ps ± at ± bi) ± rp ± dt ± ae ± he ± tg ± ff ± hw

Possible decompositions into components

Cognitive therapy

ns ± pe ± re + cr ± rp ± dt ± ae ± he ± tg ± ff ± hw

Behavioural activation

ns ± pe ± re + ba ± rp ± dt ± ae ± he ± tg ± ff ± hw

Problem-solving therapy

ns ± pe ± re + ps ± rp ± dt ± ae ± he ± tg ± ff ± hw

Third-wave cognitive behavioural therapy

ns ± pe ± re ± cr ± ba ± ps ± at ± bi + 3w ± rp ± dt ± ae ± he ± tg ± ff ± hw

Psychoeducation

Waiting list

Treatment as usual

Attention or psychological placebo

No treatment

ns + pe ± rp ± dt ± ae ± he ± tg ± ff

w ± ns ± pe ± dt ± ff

ns + dt + ff

ns ± ff

± ff

The first component and a component marked with a + denotes that the component is required. A component marked with a ± denotes that the 
component is optional. At least one of the components within brackets is required. 3w=third-wave components. ae=automated encouragement 
to proceed with internet cognitive behavioural therapy. ba=behavioural activation. ba=behaviour therapy for insomnia. cr=cognitive restructuring. 
dt=conventional drug treatment. ff=initial face-to-face contact. he=human encouragement to proceed with internet cognitive behavioural therapy. 
hw=homework required. is=interpersonal skills training. ns=non-specific treatment effects. pe=psychoeducation about depression. ps=problem 
solving. re=relaxation. rp=relapse prevention. tg=therapeutic guidance for internet cognitive behavioural therapy. w=waiting component.

Lancet Psychiatry. Author manuscript; available in PMC 2022 June 01.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t
