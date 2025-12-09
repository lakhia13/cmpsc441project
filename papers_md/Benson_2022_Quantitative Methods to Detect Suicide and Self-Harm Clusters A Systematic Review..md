# Benson_2022_Quantitative Methods to Detect Suicide and Self-Harm Clusters A Systematic Review.

Systematic Review
Quantitative Methods to Detect Suicide and Self-Harm Clusters:
A Systematic Review

Ruth Benson 1,2,*, Jan Rigby 3, Christopher Brunsdon 3, Grace Cully 1,2, Lay San Too 4 and Ella Arensman 1,2,5

1

School of Public Health, College of Medicine and Health, University College Cork,
Western Gateway Building, T12 XF62 Cork, Ireland; grace.cully@ucc.ie (G.C.); ella.arensman@ucc.ie (E.A.)

2 National Suicide Research Foundation, University College Cork, 4.28 Western Gateway Building,

T12 XF62 Cork, Ireland

3 National Centre for Geocomputation, Maynooth University, W23 F2H6 Maynooth, Ireland;

jan.rigby@mu.ie (J.R.); christopher.brunsdon@mu.ie (C.B.)

4 Centre for Mental Health, Melbourne School of Population and Global Health, The University of Melbourne,

Melbourne, VIC 3053, Australia; tiffany.too@unimelb.edu.au

5 Australian Institute for Suicide Research and Prevention, School of Applied Psychology, Grifﬁth University,

Brisbane, QLD 4122, Australia

* Correspondence: ruth.benson@ucc.ie

Abstract: Suicide and self-harm clusters exist in various forms, including point, mass, and echo
clusters. The early identiﬁcation of clusters is important to mitigate contagion and allocate timely
interventions. A systematic review was conducted to synthesize existing evidence of quantitative
analyses of suicide and self-harm clusters. Electronic databases including Medline, Embase, Web
of Science, and Scopus were searched from date of inception to December 2020 for studies that
statistically analyzed the presence of suicide or self-harm clusters. Extracted data were narratively
synthesized due to heterogeneity among the statistical methods applied. Of 7268 identiﬁed studies, 79
were eligible for narrative synthesis. Most studies quantitatively veriﬁed the presence of suicide and
self-harm clusters based on the scale of the data and type of cluster. A Poisson-based scan statistical
model was found to be effective in accurately detecting point and echo clusters. Mass clusters are
typically detected by a time-series regression model, although limitations exist. Recently, the statistical
analysis of suicide and self-harm clusters has progressed due to advances in quantitative methods
and geospatial analytical techniques, most notably spatial scanning software. The application of
such techniques to real-time surveillance data could effectively detect emerging clusters and provide
timely intervention.

Keywords: systematic review; suicide; self-harm; cluster detection; contagion; geospatial analysis

1. Introduction

Suicide clusters are commonly referred to as a higher number of suicide deaths, at-
tempted suicides, or self-harm events that occur in a population, location, or period than
usually expected, based on statistical probability or community expectancy [1]; however,
due to a lack of consensus regarding an operational deﬁnition of suicide clusters, par-
ticularly relating to the minimal number of cases that constitute a cluster, deﬁnitions
are typically determined on an ad hoc basis in terms of the spatial and temporal lim-
its of a cluster [2]. Clusters are suggested to be a product of a phenomenon known as
contagion, whereby direct or indirect exposure to suicide results in subsequent suicide
cases [3]. Suicide clusters are mostly reported within the adolescent population, particularly
15–24-year-olds [4,5] and are estimated to account for between 1% and 5% of all adolescent
deaths by suicide [6,7]. Previous evidence suggests that an increase in the incidence of
suicide clusters in recent years is linked to the broadening of social connections through
electronic communication systems and internet-based social sites [8], particularly in the

Citation: Benson, R.; Rigby, J.;

Brunsdon, C.; Cully, G.; Too, L.S.;

Arensman, E. Quantitative Methods

to Detect Suicide and Self-Harm

Clusters: A Systematic Review. Int. J.

Environ. Res. Public Health 2022, 19,

5313. https://doi.org/10.3390/

ijerph19095313

Academic Editor: Paul B. Tchounwou

Received: 29 March 2022

Accepted: 23 April 2022

Published: 27 April 2022

Publisher’s Note: MDPI stays neutral

with regard to jurisdictional claims in

published maps and institutional afﬁl-

iations.

Copyright: © 2022 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

Int. J. Environ. Res. Public Health 2022, 19, 5313. https://doi.org/10.3390/ijerph19095313

https://www.mdpi.com/journal/ijerph

International Journal ofEnvironmental Researchand Public HealthInt. J. Environ. Res. Public Health 2022, 19, 5313

2 of 13

form of suicide pacts [9]. Geographical remoteness, economic deprivation, and indigenous
status are factors associated with suicide clusters [10–12]. Furthermore, suicide clusters
are more likely to occur in areas inhabited by disadvantaged cohorts, as certain risk fac-
tors associated with suicide including unemployment, socio-economic deprivation, and
substance abuse occur more often in this population [13].

The patterns of suicide and self-harm mainly researched and documented within the
literature are of two main types: mass clusters and point clusters. Mass clusters (or temporal
clusters) involve a temporary increase in the total number of suicides within a population
relative to the period before and after the cluster, with a lack of spatial relevance typically
observed in the aftermath of a real or ﬁctional suicide documented in the media [9,10]. In
contrast, point clusters (or spatiotemporal clusters) are those that occur close together in
both space and time within a given community or institution, and clusters of this nature
can occur without the presence of media coverage [11]. A third pattern of suicide (spatial
clusters) has been identiﬁed in the literature [2–12], wherein deaths cluster by location
but not time, and are known as ‘locations where people frequently take their lives’, often
occurring at well-known public or historical sites; however, this pattern is not as extensively
researched compared with mass and point clusters. A phenomenon known as echo clusters,
wherein one or more successive suicide cluster occurs at a distinct point away from the
initial cluster, has been statistically veriﬁed in indigenous populations in rural Australia,
but there is a dearth of evidence of this phenomenon elsewhere [14,15].

In recent years, an increasing number of studies have addressed the identiﬁcation and
detection of suicide clusters at both a national and local level [16–18]. The detection of clus-
ters enhances the knowledge on the aetiology of emerging suicide clustering by establishing
links between conﬁrmed or suspected suicide cases and identifying socioecological factors
associated with the increased risk of clusters within the affected area or population [19].
Policy makers and public health ofﬁcials also beneﬁt from early detection of suicide clusters
by means of implementing targeted and timely interventions. Signiﬁcant advances in
spatial cluster detection have emerged in recent decades with the development of computer
mapping and its integration with robust statistical models [19]. Previous studies that
investigated the presence of suicide clusters have applied different techniques that follow
frequentist and Bayesian probability models, and they have incorporated spatial scanning
software [16–20]. Nonetheless, a standardized and systematic approach to the statistical
ascertainment of suicide and self-harm clusters is still lacking in contemporary research.

To date, no systematic review of the quantitative methods that effectively detect
suicide and self-harm clusters has been conducted. The main aim of this systematic review
is to synthesize the existing evidence based on statistical techniques used in successfully
detecting suicide and self-harm clusters. In this regard, this review seeks to determine an
accurate and precise approach to quantitatively verify suicide and self-harm clusters within
a population, and to ensure that clusters of suicide and self-harm are detected in a timely
manner, hence mitigating further cases.

2. Materials and Methods

In accordance with the PRISMA guidelines [21], a comprehensive search strategy was
established, including MeSH terms where relevant (see supplementary material for com-
pleted PRISMA checklist). The review was registered with The International Prospective
Register of Systematic Reviews (PROSPERO, registration number CRD42018100354) to
avoid duplication. The search strategy was applied to four bibliography databases: Med-
line, Embase, Web of Science, and Scopus from their inception to August 2018, to identify
as much relevant literature as possible. The lead author conducted an updated search,
applying the same search strategy in December 2020. The search terms included ((suicide
(MeSH) OR suicid*) OR (self-injurious behaviour (MeSH) OR (self-injur* OR self-poison*
OR self-mutilat* OR self-harm*)] AND [(cluster* OR imitat* OR contagion OR copycat
OR werther effect)] OR (spatiotemporal analysis OR time-space analysis OR geospatial
analysis OR statistical analysis*)). Inclusion criteria included studies that (a) have been

Int. J. Environ. Res. Public Health 2022, 19, 5313

3 of 13

published in a scholarly journal, (b) have applied a statistical method to detect suicide or
self-harm clusters in a population, and (c) have the full-text available in English. Exclusion
criteria eliminated (a) narrative reports of suicide or self-harm clustering that were not
statistically veriﬁed, (b) grey literature including media reports relating to potential suicide
or self-harm clusters, and (c) non-English language articles.

The title and abstracts of all references generated by the search were screened for
relevance by three authors (RB, GC, LST) to avoid content bias. For those articles of which
full texts were not available, the full text was requested from the lead author. Additional
hand searches of reference lists of relevant systematic reviews were also conducted to
identify other eligible studies. Only published scholarly articles were included to obtain the
most robust methodological approach possible. Data extraction in table format was used to
summarize study results. A meta-analysis was not considered due to the heterogeneity of
statistical methodology applied in the included studies; hence, the data was narratively
synthesized as a result. Subgroup analysis was conducted on four study groups based on
commonalities in cluster type identiﬁed during preliminary analysis. For the purpose of
the current research and to avoid misinterpretation, suicide clusters will henceforth refer
to clusters of death by suicide, whereas self-harm clusters will describe the clustering of
self-harm events including attempted suicide.

3. Results

The electronic searches identiﬁed 7246 publications, excluding duplicates. Based on
the screening of titles and abstracts generated by the database searches, 295 potentially
relevant publications were identiﬁed. Of those publications selected for full text screening,
216 did not meet the eligibility criteria, resulting in 79 relevant articles applicable for review
(Figure 1; full details of all relevant articles included as supplementary material). The
relevant studies were sub-divided, based on their primary focus, into point suicide clusters
(n = 51), point self-harm clusters (n = 8), mass suicide clusters (n = 19), and echo suicide
clusters (n = 1).

Figure 1. PRISMA ﬂow diagram.

Int. J. Environ. Res. Public Health 2022, 19, x FOR PEER REVIEW 3 of 13   werther effect)] OR (spatiotemporal analysis OR time-space analysis OR geospatial anal-ysis OR statistical analysis*)). Inclusion criteria included studies that (a) have been pub-lished in a scholarly journal, (b) have applied a statistical method to detect suicide or self-harm clusters in a population, and (c) have the full-text available in English. Exclusion criteria eliminated (a) narrative reports of suicide or self-harm clustering that were not statistically verified, (b) grey literature including media reports relating to potential sui-cide or self-harm clusters, and (c) non-English language articles. The title and abstracts of all references generated by the search were screened for relevance by three authors (RB, GC, LST) to avoid content bias. For those articles of which full texts were not available, the full text was requested from the lead author. Additional hand searches of reference lists of relevant systematic reviews were also conducted to identify other eligible studies. Only published scholarly articles were included to obtain the most robust methodological approach possible. Data extraction in table format was used to summarize study results. A meta-analysis was not considered due to the hetero-geneity of statistical methodology applied in the included studies; hence, the data was narratively synthesized as a result. Subgroup analysis was conducted on four study groups based on commonalities in cluster type identified during preliminary analysis. For the purpose of the current research and to avoid misinterpretation, suicide clusters will henceforth refer to clusters of death by suicide, whereas self-harm clusters will describe the clustering of self-harm events including attempted suicide.  3. Results The electronic searches identified 7246 publications, excluding duplicates. Based on the screening of titles and abstracts generated by the database searches, 295 potentially relevant publications were identified. Of those publications selected for full text screening, 216 did not meet the eligibility criteria, resulting in 79 relevant articles applicable for re-view (Figure 1; full details of all relevant articles included as supplementary material). The relevant studies were sub-divided, based on their primary focus, into point suicide clusters (n = 51), point self-harm clusters (n = 8), mass suicide clusters (n = 19), and echo suicide clusters (n = 1).  Figure 1. PRISMA flow diagram. The literature in this area predominately originates from the Oceania continent, Eu-rope, and the Americas. Considerably less research on the topic has been published in Int. J. Environ. Res. Public Health 2022, 19, 5313

4 of 13

The literature in this area predominately originates from the Oceania continent, Europe,
and the Americas. Considerably less research on the topic has been published in Asia
and in the African region to date. In terms of the level of geographic samples analyzed,
approximately half of all studies were based on a national sample (n = 39), almost a third
involved a regional sample (n = 25), and the remaining studies focused on state, city and
investigations into locations associated with frequently occurring suicides or self-harm acts.
The statistical analysis of point suicide and self-harm clusters commenced in 1975, with
over two thirds of studies published in the last 5 years (n = 35). Although mass suicide
cluster statistical detection was ﬁrst documented within the literature in 1986, almost two
thirds of studies have been conducted within the last 5 years (n = 12).

The majority of identified publications (n = 51) primarily focused on the statisti-
cal analysis of point suicide clusters (Table 1). Those studies with alternative primary
objectives predominantly evaluated clusters in the context of their association with de-
mographics, socio-economic factors, cultural variables, and risk factors associated with
suicide clusters [7,22–24]. A Poisson model incorporating the Monte Carlo simulation
is the most widely applied statistical model, applied in half of all point suicide cluster
detection studies (n = 28) [16,17,22,24–49]. This test determines the significance of likely
clusters, most commonly at a 5% spatial parameter and three-month temporal parameter,
as well as detecting the relative risk of cluster. Geospatial analysis was conducted in
three quarters of point suicide cluster detection studies (75%, n = 38), by means of spatial
scanning using SaTSCan and FleXScan software, as well as hotspot analysis, spheri-
cal trigonometry, and Nearest Neighbor Analysis Exploratory Spatial Data Analysis
methods [16–18,22,23,25–32,36–38,40–47,50–55]. ArcGIS was the most predominantly
employed data visualization tool, whereas a small number of studies utilized alternate
tools such as QGis, GeoDa and Teraview. A minority of studies applied alternative
statistical analyses, including a regression model (n = 10) [22,26,29,38,43,44,50,56–59],
the Knox procedure (n = 1) [7], descriptive network analysis (n = 1) [47], Bayesian hierar-
chical modelling (n = 2) [24,25,48,49,59,60], the Kernel Density estimator (n = 2) [51,58],
Nearest Neighbor Analysis (n = 1) [50], Ripley’s K function (n = 1) [52], Moran’s I
(n = 4) [50,59–61], chi square (n = 5) [50,51,55,62,63], Fisher’s exact test (n = 1) [64], and
the Anderson Darling test (n = 1) [65]. Specific numerical details of detected clusters
were undocumented in the results of those studies that applied alternative statistical
techniques without the application of geospatial analysis. Comparing different statistical
methods, a discrete Poisson-based scan statistical approach will capture most param-
eters to identify point suicide clusters, since suicide mortality data tends to be in a
Poisson distribution.

A small number of studies (n = 8) focused on the detection of self-harm clusters within
populations (Table 2). Almost a third of self-harm cluster detection studies were based on
national samples (n = 3), with the remainder focusing on cluster detection at regional (n = 2),
county (n = 1), and city levels (n = 2). Most studies reported a signiﬁcant detection of self-
harm clusters (n = 7), with over half of the studies (n = 5) indicating the speciﬁc number of
self-harm clusters detected within the population, ranging from one to twenty-ﬁve clusters.
Scan statistics were applied in over half of all self-harm cluster detection studies [66–69],
with an alternative temporal scanning method applied in one investigation [70]. Those
studies that excluded geospatial techniques from the statistical analysis applied a regression
model or chi-squared test [71–73]; however, detailed information relating to identiﬁed
clusters was not explicated from such analyses. Based on a comparison of the statistical
methods applied, a regression-based scan statistical model will capture most parameters to
detect point self-harm clusters.

Int. J. Environ. Res. Public Health 2022, 19, 5313

5 of 13

Table 1. Point suicide clusters.

Number of Studies

Level of data used in the study

Type of analysis (Studies that
performed multiple statistical
analyses are counted twice.)

Nearest
Neighbour
Statistic

Location

2

Kernel
density
estimator

1

2

Geospatial analysis conducted

Clusters detected

City

2

51

State

6

Spherical
Trigonometry

Descriptive
network
analysis

Knox
procedure

Ripleys k
function

Chi-square

1

1

1

5

1

No

13

No

3

Addressed analysed

Not speciﬁed

Location of death

SaTScan spatial applied

Not speciﬁed

4

Number of clusters reported

7

Not speciﬁed

7

13

No

24

20+

3

Table 2. Point self-harm clusters.

Regional

18

Bayesian
hierarchical
model

Morans I

National

23

Anderson
Darling

Regression
model

Poisson
model

4

6

1

10

28

Fishers
Exact
Test

1

Yes

38

Yes

48

Residence

34

Yes

20

1–20

28

No clusters detected

3

Number of Studies

Level Of Data Used in
the Study

National

National

Regional

City

Location of studies

Sweden

New Zealand

New South Wales,
Australia

Edinburgh, Scotland

Aggregated data used

No

No

Yes

No

Type of statistical
analysis conducted

Geospatial analysis
conducted

Clusters detected

Number of
clusters reported

Logistical regression

SaTScan and
Knox Procedure

No

Yes

Yes

Yes

Not speciﬁed

Not speciﬁed

SaTScan, Hotspot
analysis (Getis-Ord Gi*)
and ArcGIS
for mapping

A scan interval test
proposed by
Naus, 1966

Yes

Yes

Twenty-ﬁve
spatial cluster
regions identiﬁed

No

Yes

1 cluster

8

Regional

Kwai Tsing,
Hong Kong

Yes

Chi square and
SaTScan

Yes

Yes

Four spatial
clusters, one
spatiotemporal cluster

City

National

County

Hamadan, Iran

Denmark

Meru, Kenya

No

Yes

No

Logistic regression and
Chi-square, SaTScan
and Monte
Carlo simulation

Multi-level regressions
and log likelihood
ratio tests

Multiple logistic
regression

Yes

Yes

2 clusters

No

No

N/A

No

Yes

Not speciﬁed

Int. J. Environ. Res. Public Health 2022, 19, 5313

6 of 13

Number of Studies

Level of data used in
the study

Type of analysis conducted
(Studies that performed
multiple statistical analyses
are counted twice.)

Geospatial analysis
conducted

Mass cluster(s) detected

Within the identiﬁed studies, over one third (35%, n = 19) reported on mass suicide
clusters (Table 3). Over two-thirds of mass suicide cluster research were based on national
samples (68%, n = 13), relating to high-proﬁle suicides reported within the media in
their countries. The remaining studies investigated mass clustering with regional (n = 4),
provincial (n = 1), and continental samples (n = 1). The primary aim of all the identiﬁed
studies was the statistical veriﬁcation of increased suicides within a population (i.e., the
detection of mass clusters). The most employed statistical analyses include a time-series
model such as the Seasonal Autoregressive Integrated Moving Average (SARIMA) model
(n = 11) [74–83], a regression model (n = 8) [82–89], a Poisson model (n = 4) [84,87–89], and
non-parametric tests (n = 3) [87,90,91]. When comparing statistical models to detect mass
clusters, a time-series regression model will capture the parameters of mass clustering as
accurately as possible, based on temporal data.

Table 3. Mass clusters.

19

Continental

1

National

13

Regional

4

Provincial

1

Poisson model

Regression analysis

Non-parametric tests,
i.e., Mann–Whitney
U test, Kolmogorov-
Smirnov test

Time-series models,
e.g., SARIMA

4

8

3

11

Yes

0

Yes

17

No

19

No

2

One study based on the statistical analysis of echo clusters, conducted in Australia,
was identiﬁed within the literature [92]. The application of a Poisson scan statistic method
to data based on the same geographical area but from two different periods, effectively
detected several clusters in each period. Although there are no additional studies of this
kind to compare this methodological approach against, the identiﬁed literature applies the
same methodology as point suicide clusters with an additional time dimension.

4. Discussion

This systematic review provides unique insights into the scope of quantitative meth-
ods used to detect suicide and self-harm clusters. The ﬁndings of this review indicate that
quantitative analysis of suicide and self-harm clusters continues to advance, in line with
enhancements in statistical models of veriﬁcation and spatial scanning methods. Devel-
opments in geographical cluster detection have coincided with a greater availability of
spatial data [93]. Open-source Geographical Information System (GIS) software was ap-
plied in all but one identiﬁed study of spatial suicide clusters, offering strengths including
cost-effectiveness, reproducibility, online support forums, and tutorials [94].

As corroborated by the results of the current review, the quality of geographical data
captured in a GIS database is crucially important for geospatial analysis and depends
on positional and attribute accuracy (e.g., latitude and longitude coordinates and health
outcome), as well as completeness of data. An awareness of the speciﬁc criteria for what
constitutes suicide and self-harm acts, the importance of data completeness, and the preci-
sion required in the measurement of geographical coordinates are all critical components
of accurate data recording, and in turn, accurate cluster detection [95]. The vast majority of
research involved retrospective ecological studies of suicide or self-harm clusters based
on aggregated geographical, mortality, and census data. The implementation of active

Int. J. Environ. Res. Public Health 2022, 19, 5313

7 of 13

surveillance involving proactive contact with data providers to access, record, and com-
plete, accurate and timely public health data, including geographical identiﬁers [95,96], is
recommended to enhance the precision of cluster detection.

To date, probabilistic model-based spatial scan statistics are the most widely applied
and reliable methods employed in the detection of point suicide and self-harm clusters.
Despite a dearth of literature within the area, research investigating echo clusters of suicide
has followed the same quantitative methodology as point cluster detection (i.e., a Poisson
based spatial scan statistic), integrating an additional time dimension to account for analysis
of at least two different time periods. The Poisson approach models how many times the
event is likely to occur within a speciﬁc period, whereas the Monte Carlo simulation is used
to evaluate the statistical signiﬁcance of the likelihood ratio for each circle. Based on the
signiﬁcance test, the scan statistic can identify the most likely cluster, as well as secondary
clusters, for which the likelihood ratios are less, but are still of importance [97].

SaTScan, which is a type of software using a cylindrical scan statistic involving a
moving circular geographical-based scan window and a time-based height dimension of
continuously varying radii, appears to be the most used scan approach within the reviewed
literature [20]. This tool evaluates the statistical signiﬁcance of point clusters with no prior
assumptions of the data. Although this software has been extensively applied within
epidemiological studies, a limitation of SaTScan is its inability to detect non-circular shaped
clusters or hotspots, such as the shapes of roads or rivers [98].

To detect irregularly shaped clusters, alternative approaches have been proposed
and applied within the reviewed research [98–100]. FleXScan [53], based on an adjustable
spatial scan window, is effective in detecting clusters that assume arbitrary shapes [100–103];
however, the efﬁcacy of this software is limited to the detection of small to moderate clusters
of approximately 30 cases [53]. Echelon scanning using EcheScan, also identiﬁed within the
literature, is used to detect non-circular shaped hotspots based on their spatial hierarchal
structure, visually represented by a dendrogram that is scanned from top to bottom [97,102].
Similar to the traditional spatial scan statistic, echelon scanning is based on the Poisson
model with Monte Carlo simulation; however, the scan window is smaller. EcheScan
software, developed in R, is easily accessible and incorporates open-source mapping tools;
however, limitations exist in some instances wherein the shape of the detected hotspot may
be too complex, or too large, to be easily interpreted [103].

The results of this review suggest that analysis window parameters of scan statistic
algorithms should be manipulated to determine the appropriate population and duration
thresholds, calibrating the optimal parameter combination, since the precision of results
can be affected by scale. Future research should seek to compare the performance of the
scan statistic algorithms via a simulation study and examine the spatial congruence and
sensitivity of the models. Based on the unique purposes of the scan statistics, the robustness
and sensitivity of a Poisson-based spatial scan hybrid approach should also be explored by
future research.

Mass cluster detection fundamentally concerns itself with an increase in cases during
a speciﬁc period, irrespective of spatial relevance. Quasi-experimental research designs,
such as time-series forecasting based on a regression model, measure how many future
observations are predictable based on past behavior [85,104]. In mass cluster detection,
media coverage of a ﬁctional or real high-proﬁle suicide is correlated with an increase in
cases of suicide during the aftermath of the suicide, by means of comparing frequencies
of suicide in an experimental time frame during and after the death was reported, against
the frequency of suicide in a control period. Such studies involve a crucial limitation that
must be considered when interpreting ﬁndings; that is, the difﬁculty to accept observed
increases in suicide and self-harm rates in terms of being a direct link to the high-proﬁle
case with absolute conﬁdence.

Int. J. Environ. Res. Public Health 2022, 19, 5313

8 of 13

4.1. Strengths and Limitations

This review sought to identify and synthesize literature relating to suicide and self-
harm cluster detection, demonstrating inclusivity in systematically reviewing all published
studies to date, and addressing all types of suicide and self-harm clusters. The primary
focus of the review was to examine the most robust global evidence using statistical
methods to detect suicide and self-harm clusters within a population as accurately as
possible; therefore, non-peer reviewed reports have been excluded from the synthesis,
which may limit the results. Due to study heterogeneity arising from methodological
diversity, a full quality appraisal was not carried out, hence, possible biases must be
considered in the context of limitations. Excluding non-English studies has not limited the
review since most research in this area has been conducted in English speaking countries.

4.2. Implications for Suicide Prevention and Considerations for Future Research

The ﬁndings of this review have implications for suicide prevention. More speciﬁ-
cally, this review has synthesized all empirical studies of suicide and self-harm clusters
in a population, arriving at the most comprehensive standardized approach to suicide
and self-harm cluster detection currently available, in the absence of a gold-standard
method. Innovatively, the conclusive approach of geospatial probabilistic modelling for
point suicide cluster detection has been incorporated in the development and evaluation
of a community response to a suicide cluster, demonstrating the utility of this technique
for suicide prevention purposes [44]. The comprehensive study identiﬁed in the review
applied spatiotemporal analysis to suicide mortality data and socioeconomic aggregated
data by way of identifying suicide clusters and spatial variations of risk-factors in Hong
Kong, for the purpose of informing the development of the targeted program, and eval-
uating its efﬁcacy post-program, using changes in suicide incidence and cluster patterns
as the outcome. The ﬁndings of the study emphasize the value of a temporal and spatial
monitoring surveillance system based on the methodology described here in prioritizing
suicide prevention measures. The outcome of the novel study further suggests a use for
such techniques in the monitoring and evaluation of population-level interventions to be
implemented as components in national suicide prevention strategies.

Ofﬁcial suicide mortality records can take up to two years post-death to be released,
due to delays resulting from prolonged medico-legal cause of death investigations, and
late registered deaths [105]. The application of cluster detection methods identiﬁed in this
review to provisional, real-time, suspected suicide data, would support the detection of
emerging clusters, providing an advanced opportunity to effectively intervene and mitigate
further contagion [106]. Early identiﬁcation of emerging suspected clusters would also
facilitate the acceleration of an evidence-based crisis response in vulnerable communities,
wherein screening and referral of susceptible individuals to appropriate clinical and support
services could occur in a timelier manner. Future research should consider the investigation
of self-harm clusters and suicide clusters within a population, to determine whether clusters
of self-harm precede clusters of suicide, thereby offering the opportunity for targeted
clinical intervention in populations wherein emerging self-harm clusters are detected as a
prevention strategy for possible subsequent suicide clustering.

Real-time active surveillance of suicide and self-harm would facilitate prospective
studies of suicide and self-harm clusters using prospective geospatial probabilistic mod-
elling [107]. The ﬁndings of such prospective studies would subsequently inform suicide
prevention strategies, action plans, policy planning, and service provision in a timely
manner. Although unexplored in studies, including those in this review, temporal analysis
of suicide data using a calendar approach based on date of death may detect temporal
clusters relating to signiﬁcant dates, such as the anniversary of the death of a loved one or
high-proﬁle individual, and seasonal trends when peaks are commonly observed. The de-
tection of this phenomenon should be incorporated as a key objective of a real-time suicide
surveillance system by way of indicating high-risk dates and periods that could require
deployment of additional resources to respond to possible increases in imitative behavior.

Int. J. Environ. Res. Public Health 2022, 19, 5313

9 of 13

5. Conclusions

The synthesized results of this systematic review demonstrate advances made in
epidemiological cluster detection, which is relevant to suicide and self-harm data, within
the forty-ﬁve-year period since statistical investigations into clusters of suicide and self-
harm were ﬁrst published. Most notably, the evolvement of open-source GIS software,
has effectively contributed to point cluster detection by means of geospatial probabilistic
modelling. Mass suicide cluster detection traditionally employs a time-series regression
analysis to verify temporal clustering within a population; however, the use of retrospec-
tive aggregated data in these studies compromises the accuracy and efﬁciency of cluster
detection investigations.

Supplementary Materials: The following supporting information can be downloaded at: https:
//www.mdpi.com/article/10.3390/ijerph19095313/s1, Table S1: PRISMA 2009 Checklist; Table S2:
Point Suicide Clusters; Table S3: Point Self-Harm Clusters; Table S4: Mass Clusters; Table S5:
Echo Clusters.

Author Contributions: Conceptualization, R.B., E.A. and J.R.; methodology, R.B., G.C. and L.S.T.;
formal analysis, R.B.; investigation, R.B.; writing—original draft preparation, R.B.; writing—review
and editing, R.B., J.R., C.B., G.C., L.S.T. and E.A., supervision, E.A., J.R. and C.B.; funding acquisition,
E.A and L.S.T. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by Irish Health Research Board, grant number IRRL-2015-1586.
L.S.T. was supported by a National Health and Medical Research Council Early Career Fellowship,
grant number GNT1156849.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Not applicable.

Acknowledgments: We gratefully acknowledge the support of Joe Murphy, assistant librarian at the
Mercy University Hospital Library, for his excellent advice that enhanced the search strategy applied.
We also wish to extend our gratitude to John Browne who delivered a postgraduate module based on
systematic reviews for the health sciences in University College Cork. The knowledge acquired from
this training proved to be invaluable in conducting this study.

Conﬂicts of Interest: The authors declare no conﬂict of interest.

References

1.

O’Carroll, P.W.; Mercy, J.A.; Steward, J.A. CDC recommendations for a community plan for the prevention and containment of
suicide clusters. MMWR Supp. 1988, 37, 1–12.

2. Niedzwiedz, C.; Haw, C.; Hawton, K.; Platt, S. The deﬁnition and epidemiology of clusters of suicidal behavior: A systematic

3.

review. Suicide Life Threat Behav. 2014, 44, 569–581. [CrossRef] [PubMed]
Bohanna, I. Suicide “contagion”: What we know and what we need to ﬁnd out. Can. Med. Assoc. J. 2013, 185, 861–862. [CrossRef]
[PubMed]

4. Hazell, P. Adolescent suicide clusters: Evidence, mechanisms, and prevention. Aust. N. Z. J. Psychiatry 1993, 27, 653–665.

5.
6.

[CrossRef]
Gould, M.S.; Wallenstein, S.; Kleinman, M. Time-space clustering of teenage suicide. Am. J. Epidemiol. 1990, 131, 71–78. [CrossRef]
Gould, M.; Wallenstein, S.; Kleinman, N. A Study of Time-Space Clustering of Suicide: Final Report; Centers for Disease Control and
Prevention (CDC): Atlanta, GA, USA, 1987.
Gould, M.S.; Wallenstein, S.; Kleinman, M.H.; O’Carroll, P.; Mercy, J. Suicide clusters: An examination of age-speciﬁc effects. Am.
J. Public Health 1990, 80, 211–212. [CrossRef]
Larkin, G.; Beautrais, A. Geospatial Mapping of Suicide Clusters; Te Pou o Te Whakaaro Nui: Auckland, New Zealand, 2012.
8.
Biddle, L.; Donovan, J.; Hawton, K.; Kapur, N.; Gunnell, D. Suicide and the internet. BMJ 2008, 336, 800–802. [CrossRef] [PubMed]
9.
10. Haw, C.; Hawton, K.; Niedzwiedz, C.; Platt, S. Suicide clusters: A review of risk factors and mechanisms. Suicide Life Threat Behav.

7.

2013, 43, 97–108. [CrossRef] [PubMed]
Joiner, T.E., Jr. The clustering and contagion of suicide. Curr. Dir. Psychol. Sci. 1999, 8, 89–92. [CrossRef]

11.
12. Cox, G.R.; Owens, C.; Robinson, J.; Nicholas, A.; Lockley, A.; Williamson, M.; Cheung, Y.T.D.; Pirkis, J. Interventions to reduce

suicides at suicide hotspots: A systematic review. BMC Public Health 2013, 13, 214. [CrossRef] [PubMed]

Int. J. Environ. Res. Public Health 2022, 19, 5313

10 of 13

13. Hsu, C.Y.; Chang, S.S.; Yip, P. Individual-, household-and neighbourhood-level characteristics associated with life satisfaction:

A multilevel analysis of a population-based sample from Hong Kong. Urban Stud. 2017, 54, 3700–3717. [CrossRef]

14. Hanssens, L. ‘Echo Clusters’-Are they a Unique Phenomenon of Indigenous Attempted and Completed Suicide? Aborig. Isl.

Health Work J. 2010, 34, 17–26. [CrossRef]

15. Hanssens, L. Suicide Echo Clusters: Are they Socially Determined, and the Result of a Pre-existing Vulnerability in Indigenous

16.

Communities in the Northern Territory? Aborig. Isl. Health Work J. 2011, 35, 14.
Jones, P.; Gunnell, D.; Platt, S.; Scourﬁeld, J.; Lloyd, K.; Huxley, P.; John, A.; Kamran, B.; Wells, C.; Dennis, M. Identifying probable
suicide clusters in Wales using national mortality data. PLoS ONE 2013, 8, e71713. [CrossRef] [PubMed]

17. Bando, D.H.; Moreira, R.S.; Pereira, J.C.; Barrozo, L.V. Spatial clusters of suicide in the municipality of Sao Paulo 1996–2005:

An ecological study. BMC Psychiatry 2012, 12, 124. [CrossRef]

18. Larkin, G.; Beautrais, A.L.; Xu, H. Geospatial mapping of suicide clusters in Cantebury New Zealand. Inj. Prev. 2010, 16

(Suppl. 1), A258. [CrossRef]

19. Mclafferty, S. Disease cluster detection methods: Recent developments and public health implications. Ann. GIS 2015, 21, 127–133.

[CrossRef]

20. Kulldorff, M. A spatial scan statistic. Commun. Stat.-Theory Methods 1997, 26, 1481–1496. [CrossRef]
21. Moher, D.; Liberati, A.; Tetzlaff, J.; Altman, D.G. Preferred reporting items for systematic reviews and meta-analyses: The PRISMA

statement. PLoS Med. 2009, 6, e1000097. [CrossRef]

22. Bando, D.H.; Brunoni, A.R.; Bensenor, I.M.; Lotufo, P.A. Suicide rates and income in Sao Paulo and Brazil: A temporal and spatial

epidemiologic analysis from 1996 to 2008. BMC Psychiatry 2012, 12, 127. [CrossRef]

23. Hill, N.T.; Spittal, M.J.; Pirkis, J.; Torok, M.; Robinson, J. Risk factors associated with suicide clusters in Australian youth:
Identifying who is at risk and the mechanisms associated with cluster membership. EClinicalMedicine 2020, 29, 100631. [CrossRef]
[PubMed]

24. Carcach, C. A spatio-temporal analysis of suicide in El Salvador. BMC Public Health 2017, 17, 339. [CrossRef]
25. Ngui, A.N.; Apparicio, P.; Moltchanova, E.; Vasiliadis, H.M. Spatial analysis of suicide mortality in Québec: Spatial clustering and

area factor correlates. Psychiatry Res. 2014, 220, 20–30. [CrossRef]

26. Cheung, Y.T.D.; Spittal, M.J.; Williamson, M.K.; Tung, S.J.; Pirkis, J. Application of scan statistics to detect suicide clusters in

Australia. PLoS ONE 2013, 8, e54168. [CrossRef] [PubMed]

27. Exeter, D.J.; Boyle, P.J. Does young adult suicide cluster geographically in Scotland? J. Epidemiol. Community Health 2007, 61,

28.

731–736. [CrossRef] [PubMed]
Johnson, A.M.; Woodside, J.M.; Johnson, A.; Pollack, J.M. Spatial patterns and neighborhood characteristics of overall suicide
clusters in Florida from 2001 to 2010. Am. J. Prev. Med. 2017, 52, e1–e7. [CrossRef]

29. Robinson, J.; Too, L.S.; Pirkis, J.; Spittal, M.J. Spatial suicide clusters in Australia between 2010 and 2012: A comparison of cluster

and non-cluster among young people and adults. BMC Psychiatry 2016, 16, 417. [CrossRef]

30. Núñez-González, S.; Lara-Vinueza, A.G.; Gault, C.; Delgado-Ron, J.A. Trends and spatial patterns of suicide among adolescent in

31.

Ecuador, 1997–2016. Clin. Pract. Epidemiol. Ment. Health 2018, 14, 283. [CrossRef] [PubMed]
Sy, K.T.L.; Shaman, J.; Kandula, S.; Pei, S.; Gould, M.S.; Keyes, K.M. Spatiotemporal clustering of suicides in the US from 1999 to
2016: A spatial epidemiological approach. Soc. Psychiatry Psychiatr. Epidemiol. 2019, 54, 1471–1482. [CrossRef] [PubMed]
32. Milner, A.; Too, L.S.; Spittal, M.J. Cluster Suicides among Unemployed Persons in Australia Over the Period 2001–2013. Soc. Indic.

Res. 2018, 137, 189–201. [CrossRef]

33. Gibbons, R.D.; Clark, D.C.; Fawcett, J. A statistical method for evaluating suicide clusters and implementing cluster surveillance.

Am. J. Epidemiol. 1990, 132 (Suppl. 1), S183–S191. [CrossRef] [PubMed]

34. Kirch, M.R.; Lester, D. Suicide from the Golden Gate Bridge: Do they cluster over time? Psychol. Rep. 1986, 59, 1314. [CrossRef]

[PubMed]

35. Cox, B.; Skegg, K. Contagious suicide in prisons and police cells. J. Epidemiol. Community Health 1993, 47, 69–72. [CrossRef]
36.

Fontanella, C.A.; Saman, D.M.; Campo, J.V.; Hiance-Steelesmith, D.L.; Bridge, J.A.; Sweeney, H.A.; Root, E.D. Mapping suicide
mortality in Ohio: A spatial epidemiological analysis of suicide clusters and area level correlates. Prev. Med. 2018, 106, 177–184.
[CrossRef] [PubMed]

37. Qi, X.; Hu, W.; Page, A.; Tong, S. Spatial clusters of suicide in Australia. BMC Psychiatry 2012, 12, 86. [CrossRef]
38. Qi, X.; Tong, S.; Hu, W. Spatial distribution of suicide in Queensland, Australia. BMC Psychiatry 2010, 10, 106. [CrossRef]

39.

[PubMed]
Strauss, M.J.; Klimek, P.; Sonneck, G.; Niederkrotenthaler, T. Suicides on the Austrian railway network: Hotspot analysis and
effect of proximity to psychiatric institutions. R. Soc. Open Sci. 2017, 4, 160711. [CrossRef] [PubMed]

40. Tomita, M.; Kubota, T.; Ishioka, F. Spatial Clustering Properties in the Temporal Variation of Suicide Rates/Numbers among

Japanese Citizens: A Comprehensive Comparison and Discussion. PLoS ONE 2015, 10, e0127358. [CrossRef] [PubMed]

41. Too, L.S.; Pirkis, J.; Milner, A.; Bugeja, L.; Spittal, M.J. Railway suicide clusters: How common are they and what predicts them?

Inj. Prev. 2017, 23, 328–333. [CrossRef] [PubMed]

42. Too, L.; Pirkis, J.; Milner, A.; Spittal, M. Clusters of suicides and suicide attempts: Detection, proximity, and correlates. Epidemiol.

Psychiatr. Sci. 2017, 26, 491–500. [CrossRef]

Int. J. Environ. Res. Public Health 2022, 19, 5313

11 of 13

43.

Sugg, M.M.; Woolard, S.; Lawrimore, M.; Michael, K.D.; Runkle, J.D. Spatial Clustering of Suicides and Neighborhood Determi-
nants in North Carolina, 2000 to 2017. Appl. Spat. Anal. Policy. 2021, 14, 395–413. [CrossRef]

44. Lai, C.; Law, Y.W.; Shum, A.K.; Ip, F.W.; Yip, P.S. A community-based response to a suicide cluster: A Hong Kong experience.

Crisis 2020, 41, 163–171. [CrossRef]

45. Too, L.S.; Spittal, M.J. Suicide Clusters among Top 10 High-Risk Occupations: A Study From 2001 to 2016 in Australia. J. Nerv.

Ment. Dis. 2020, 208, 942–946. [CrossRef]

46. Hill, N.T.; Too, L.S.; Spittal, M.J.; Robinson, J. Understanding the characteristics and mechanisms underlying suicide clusters in

Australian youth: A comparison of cluster detection methods. Epidemiol. Psychiatr. Sci. 2020, 29, e151. [CrossRef]

47. Yamaoka, K.; Suzuki, M.; Inoue, M.; Ishikawa, H.; Tango, T. Spatial clustering of suicide mortality and associated community

characteristics in Kanagawa prefecture, Japan, 2011–2017. BMC Psychiatry 2020, 20, 74. [CrossRef]

48. Hsu, C.Y.; Chang, S.S.; Lee, E.S.; Yip, P.S. Geography of suicide in Hong Kong: Spatial patterning, and socioeconomic correlates

and inequalities. Soc. Sci. Med. 2015, 130, 190–203. [CrossRef]

49. Yoshioka, E.; Hanley, S.J.; Sato, Y.; Saijo, Y. Geography of suicide in Japan: Spatial patterning and rural–urban differences. Soc.

Psychiatry Psychiatr. Epidemiol. 2021, 56, 731–7466. [CrossRef]

50. Vaz, E.; Shaker, R.R.; Cusimano, M.D. A geographical exploration of environmental and land use characteristics of suicide in the

greater Toronto area. Psychiatry Res. 2020, 1, 112790. [CrossRef]

51. Pérez-Costillas, L.; Blasco-Fontecilla, H.; Benítez, N.; Comino, R.; Antón, J.M.; Ramos-Medina, V.; López, A.; Palomo, J.L.;
Madrigal, L.; Alcalde, J.; et al. Space–time suicide clustering in the community of Antequera (Spain). Rev. Psiquiatr. Salud Men.
2015, 8, 26–34. [CrossRef] [PubMed]

52. Kassem, A.M.; Carter, K.K.; Johnson, C.J.; Hahn, C.G. Peer Reviewed: Spatial Clustering of Suicide and Associated Community

Characteristics, Idaho, 2010–2014. Prev. Chronic Dis. 2019, 16, E37. [CrossRef]

53. Takahashi, K.; Yokoyama, T.; Tango, T. FleXScan v3. 1: Software for the Flexible Scan Statistic; National Institute of Public Health:

Tokyo, Japan, 2010.

54. Lersch, K.M. Exploring the geography of suicide threats and suicide attempts: An application of Risk Terrain Modeling. Soc. Sci.

Med. 2020, 249, 112860. [CrossRef] [PubMed]

55. Ceccato, V.; Uittenbogaard, A. Suicides in commuting railway systems: The case of Stockholm county, Sweden. J. Affect. Disord.

2016, 198, 206–2157. [CrossRef] [PubMed]

56. Tidemalm, D.; Runeson, B.; Waern, M.; Frisell, T.; Carlström, E.; Lichtenstein, P.; Långström, N. Familial clustering of suicide risk:

A total population study of 11.4 million individuals. Psychol. Med. 2011, 41, 2527–2534. [CrossRef] [PubMed]

57. Dos Santos, A.D.; Guimarães, L.M.L.; De Carvalho, Y.F.; Viana, L.D.C.; Alves, G.L.; Lima, A.C.R.; Santos, M.B.; Góes, M.A.D.O.;
De Araújo, K.C.G.M. Spatial analysis and temporal trends of suicide mortality in Sergipe, Brazil, 2000–2015. Trends Psychiatry
Psychother. 2018, 40, 269–276. [CrossRef] [PubMed]

58. Bando, D.H.; Barrozo, L.V.; Volpe, F.M. Geographical clusters and social risk factors for suicide in the city of São Paulo, 2006–2015:

An ecologic study. Int. J. Soc. Psychiatry 2020, 66, 460–468. [CrossRef]

59. Beringuel, B.M.; de Barros Canuto, I.M.; Silva, A.P.; do Bonﬁm, C.V. Epidemiology and Spatiotemporal Clustering of Suicides in

the State of Pernambuco (1999–2018). Trends Psychol. 2021, 29, 123–138. [CrossRef]

60. Guo, Y.; Chau, P.P.; Chang, Q.; Woo, J.; Wong, M.; Yip, P.S. The geography of suicide in older adults in Hong Kong: An ecological

61.

study. Int. J. Geriatr. Psychiatry 2020, 35, 99–112. [CrossRef] [PubMed]
Santos, E.G.; Barbosa, I.R.; Severo, A.K. Space-time analysis of mortality by suicide in the State of Rio Grande do Norte, Brazil, in
the period from 2000 to 2015. Cien Saude Colet. 2020, 25, 633–643. [CrossRef] [PubMed]

62. Reser, J.P. Australian Aboriginal suicide deaths in custody: Cultural context and cluster evidence. Aust. Psychol. 1989, 24, 325–342.

[CrossRef]

63. Lazzarini, T.A.; Gonçalves, C.C.M.; Benites, W.M.; Silva LFd Tsuha, D.H.; Ko, A.I.; Rohrbaugh, R.; Andrews, J.R.; Croda, J. Suicide
in Brazilian indigenous communities: Clustering of cases in children and adolescents by household. Rev. Saúde Públ. 2018, 52, 56.
[CrossRef]

64. Austin, A.E.; van den Heuvel, C.; Byard, R.W. Cluster hanging suicides in the young in South Australia. J. Forensic Sci. 2011, 56,

1528–1530. [CrossRef]

65. Mackenzie, D.W.; Lester, D.; Manson, R.; Yeh, C. Do suicides from the Golden Gate Bridge cluster? Psychol. Rep. 2016, 118, 70–73.

[CrossRef] [PubMed]

66. Torok, M.; Konings, P.; Batterham, P.J.; Christensen, H. Spatial clustering of fatal, and non-fatal, suicide in new South Wales,

Australia: Implications for evidence-based prevention. BMC Psychiatry 2017, 17, 339. [CrossRef] [PubMed]

67. Gould, M.S.; Petrie, K.; Kleinman, M.H.; Wallenstein, S. Clustering of attempted suicide: New Zealand national data. Int. J.

Epidemiol. 1994, 23, 1185–1189. [CrossRef]

68. Leung, M.; Chow, C.B.; Ip, P.; Yip, S. Pure spatial and space-time clusters of self-harm in Kwai Tsing 2004 to 2012. Spat

Spatiotemporal Epidemiol. 2018, 27, 1–9. [CrossRef] [PubMed]

69. Karami, M.; Yazdi–Ravandi, S.; Ghaleiha, A.; Olfatifar, M. Comparison of the clusters and non-clusters areas of attempted suicide
cases in Hamadan Province, western Iran: Findings from a pilot study (2016–2017). J. Res. Health Sci. 2018, 18, e00425. [CrossRef]
Smeeton, N.; Wilkinson, G. The identiﬁcation of clustering in parasuicide. Br. J. Psychiatry 1988, 153, 218–221. [CrossRef]

70.

Int. J. Environ. Res. Public Health 2022, 19, 5313

12 of 13

71. Mittendorfer-Rutz, E.; Rasmussen, F.; Wasserman, D. Familial clustering of suicidal behaviour and psychopathology in young

suicide attempters. Soc. Psychiatry Psychiatr. Epidemiol. 2008, 43, 28–36. [CrossRef] [PubMed]

72. Pisinger, V.S.; Hawton, K.; Tolstrup, J.S. School-and class-level variation in self-harm, suicide ideation and suicide attempts in

Danish high schools. Scand. J. Public Health 2019, 47, 146–156. [CrossRef] [PubMed]

73. Goodman, M.L.; Puffer, E.S.; Keiser, P.H.; Gitari, S. Suicide clusters among young Kenyan men. Health Psychol. 2020, 25, 1004–1013.

[CrossRef] [PubMed]

74. Queinec, R.; Benjamin, C.; Beitz, C.; Lagarde, E.; Encrenaz, G. Suicide contagion in France: An epidemiologic study. Inj. Prev.

75.
76.

2010, 16 (Suppl. 1), A241. [CrossRef]
Jonas, K. Modelling and suicide: A test of the Werther effect. Br. J. Soc. Psychol. 1992, 31, 295–306. [CrossRef]
Sinyor, M.; Williams, M.; Tran, U.S.; Schaffer, A.; Kurdyak, P.; Pirkis, J.; Niederkrotenthaler, T. Suicides in Young People in Ontario
Following the Release of “13 Reasons Why”. Can. J. Psychiatry 2019, 64, 798–804. [CrossRef] [PubMed]

77. Niederkrotenthaler, T.; Stack, S.; Till, B.; Sinyor, M.; Pirkis, J.; Garcia, D.; Rockett, I.R.H.; Tran, U.S. Association of increased youth

suicides in the United States with the release of 13 Reasons Why. JAMA Psychiatry 2019, 76, 933–940. [CrossRef]

78. Whitley, R.; Fink, D.S.; Santaella-Tenorio, J.; Keyes, K.M. Suicide mortality in Canada after the death of Robin Williams, in the
context of high-ﬁdelity to suicide reporting guidelines in the Canadian media. Can. J. Psychiatry 2019, 64, 805–812. [CrossRef]
[PubMed]
Fink, D.S.; Santaella-Tenorio, J.; Keyes, K.M. Increase in suicides the months after the death of Robin Williams in the US. PLoS
ONE 2018, 13, e0191405. [CrossRef] [PubMed]

79.

80. Pirkis, J.; Currier, D.; Too, L.S.; Bryant, M.; Bartlett, S.; Sinyor, M.; Spittal, M.J. Suicides in Australia following media reports of the

81.

death of Robin Williams. Aust. N. Z. J. Psychiatry 2020, 54, 99–104. [CrossRef]
Sinyor, M.; Tran, U.S.; Garcia, D.; Till, B.; Voracek, M.; Niederkrotenthaler, T. Suicide mortality in the United States following the
suicides of Kate Spade and Anthony Bourdain. 2020. Aust. N. Z. J. Psychiatry 2021, 55, 613–619. [CrossRef] [PubMed]

82. Bridge, J.A.; Greenhouse, J.B.; Ruch, D.; Stevens, J.; Ackerman, J.; Sheftall, A.H.; Horowitz, L.M.; Kelleher, K.J.; Campo, J.V.
Association between the release of netﬂix’s 13 Reasons Why and suicide rates in the United States: An interrupted time series
analysis. J. Am. Acad. Child Adolesc. Psychiatry 2020, 59, 236–243. [CrossRef] [PubMed]

83. Romer, D. Reanalysis of the Bridge et al. study of suicide following release of 13 Reasons Why. PLoS ONE 2020, 15, e0227545.

84.

[CrossRef]
Jang, S.A.; Sung, J.M.; Park, J.Y.; Jeon, W.T. Copycat suicide induced by entertainment celebrity suicides in South Korea. Psychiatry
Investig. 2016, 13, 74. [CrossRef] [PubMed]

85. Chen, Y.Y.; Tsai, P.C.; Chen, P.H.; Fan, C.C.; Hung, G.C.L.; Cheng, A.T. Effect of media reporting of the suicide of a singer in

Taiwan: The case of Ivy Li. Soc. Psychiatry Psychiatr. Epidemiol. 2010, 45, 363–369. [CrossRef] [PubMed]

86. Phillips, D.P.; Carstensen, L.L. Clustering of teenage suicides after television news stories about suicide. N. Engl. J. Med. 1986, 315,

685–689. [CrossRef] [PubMed]

87. Ladwig, K.H.; Kunrath, S.; Lukaschek, K.; Baumert, J. The railway suicide death of a famous German football player: Impact on

the subsequent frequency of railway suicide acts in Germany. J. Affect. Disord. 2012, 136, 194–198. [CrossRef]

88. Cheng, Q.; Chen, F.; Yip, P.S. The Foxconn suicides and their media prominence: Is the Werther Effect applicable in China? BMC

Public Health 2011, 11, 841. [CrossRef] [PubMed]

89. Lee, S.Y. Media Coverage of Adolescent and Celebrity Suicides and Imitation Suicides among Adolescents. J. Broadcast. Electron.

Media 2019, 63, 130–143. [CrossRef]

90. Koburger, N.; Mergl, R.; Rummel-Kluge, C.; Ibelshäuser, A.; Meise, U.; Postuvan, V.; Roskar, S.; Székely, A.; Tóth, M.D.; Van der
Feltz-Cornelis, C.; et al. Celebrity suicide on the railway network: Can one case trigger international effects? J. Affect. Disord.
2015, 85, 38–46. [CrossRef] [PubMed]

91. Etzersdorfer, E.; Sonneck, G.; Nagel-Kuess, S. Newspaper reports and suicide. N. Engl. J. Med. 1992. [CrossRef]
92. Too, L.S.; Pirkis, J.; Milner, A.; Robinson, J.; Spittal, M.J. Clusters of suicidal events among young people: Do clusters from one

time period predict later clusters? Suicide Life Threat Behav. 2019, 49, 561–571. [CrossRef]

93. Lawson, A.B.; Kleinman, K. Spatial and Syndromic Surveillance for Public Health; John Wiley & Sons: Hoboken, NJ, USA, 2005.
94. Maurya, S.P.; Ohri, A.; Mishra, S. (Eds.) Open-Source GIS: A Review. In Proceedings of the National Conference on Open-Source

GIS: Opportunities and Challenges, Varanasi, India, 9–10 October 2015.

95. Nsubuga, P.; White, M.E.; Thacker, S.B.; Anderson, M.A.; Blount, S.B.; Broome, C.V.; Chiller, T.M.; Espitia, V.; Imtiaz, R.;
Sosin, D.; et al. Public Health Surveillance: A Tool for Targeting and Monitoring Interventions. In Disease Control Priorities in
Developing Countries, 2nd ed.; Jamison, D.T., Breman, J.G., Measham, A.R., Alleyne, G., Claeson, M., Evans, D.B., Jha, P., Mills, A.,
Musgrove, P., Eds.; The International Bank for Reconstruction and Development/The World Bank: Washington, DC, USA; Oxford
University Press: New York, NY, USA, 2006; Chapter 53; pp. 99–1015, ISBN -10 0-8213-6179-1.

96. Cromley, E.K.; McLafferty, S.L. GIS and Public Health; Guilford Press: New York, NY, USA, 2011.
97.

Ishioka, F.; Kurihara, K. (Eds.) Evaluation of Hotspot Detection Method Based on Echelon Structure. In Proceedings of the 59th
ISI World Statistics Congress, Hong Kong, China, 25–30 August 2013; p. 5366.

98. Tango, T.; Takahashi, K. A ﬂexibly shaped spatial scan statistic for detecting clusters. Int. J. Health Geogr. 2005, 4, 11. [CrossRef]
99. Patil, G.P.; Taillie, C. Upper-level set scan statistic for detecting arbitrarily shaped hotspots. Environ. Ecol. Stat. 2004, 11, 183–197.

[CrossRef]

Int. J. Environ. Res. Public Health 2022, 19, 5313

13 of 13

100. Kurihara, K. Hotspots Detection for Cellular Surface Data. Bull. Int. Stat. Inst. 2003, 54, 115–116.
101. Tango, T.; Takahashi, K. A ﬂexible spatial scan statistic with a restricted likelihood ratio for detecting disease clusters. Stat. Med.

2012, 31, 4207–4218. [CrossRef]

102. Myers, W.; Patil, G.P.; Joly, K. Echelon approach to areas of concern in synoptic regional monitoring. Environ. Ecol. Stat. 1997, 4,

131–152. [CrossRef]

103. Kurihara, K.; Ishioka, F.; Kajinishi, S. Spatial and temporal clustering based on the echelon scan technique and software analysis.

JJSD 2020, 3, 313–332. [CrossRef]

104. Terrell, C. Predictions in Time Series Using Regression Models; Scientiﬁc e-Resources: New Delhi, India, 2019.
105. Värnik, P.; Sisask, M.; Värnik, A.; Laido, Z.; Meise, U.; Ibelshäuser, A.; Van Audenhove, C.; Reynders, A.; Kocalevent, R.D.;
Kopp, M.; et al. Suicide registration in eight European countries: A qualitative analysis of procedures and practices. Forensic Sci.
Int. 2010, 202, 86–92. [CrossRef] [PubMed]

106. Baran, A.; Gerstner, R.; Ueda, M.; Gmitrowicz, A. Implementing real-time data suicide surveillance systems. Crisis 2021, 42,

321–327. [CrossRef] [PubMed]

107. Kulldorff, M. Prospective time periodic geographical disease surveillance using a scan statistic. J. R. Stat. Soc. Ser. A 2001, 164,

61–72. [CrossRef]
