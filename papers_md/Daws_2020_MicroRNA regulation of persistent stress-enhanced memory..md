# Daws_2020_MicroRNA regulation of persistent stress-enhanced memory.

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
Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

Published in final edited form as:

Mol Psychiatry. 2020 May ; 25(5): 965–976. doi:10.1038/s41380-019-0432-2.

microRNA regulation of persistent stress-enhanced memory

Stephanie E. Sillivan1,2, Sarah Jamieson1,2, Laurence de Nijs3, Meghan Jones1,2, Clara 
Snijders3, Torsten Klengel4, Nadine F. Joseph1,2, Julian Krauskopf5, Jos Kleinjans5, 
Christiaan H. Vinkers6, Marco P.M. Boks6, Elbert Geuze6,7, Eric Vermetten6,7,8, Sabina 
Berretta4, Kerry J. Ressler4, Bart P.F. Rutten3, Gavin Rumbaugh2, Courtney A. Miller1,2,*

1Department of Molecular Medicine, The Scripps Research Institute, Jupiter, FL USA 
2Department of Neuroscience, The Scripps Research Institute, Jupiter, FL USA. 3School for 
Mental Health and Neuroscience, Department of Psychiatry and Neuropsychology, Maastricht 
University, Maastricht, The Netherlands. 4Department of Psychiatry, Harvard Medical School, 
McLean Hospital, Belmont, MA, USA. 5Department of Toxicogenomics, Maastricht University, 
Maastricht, The Netherlands. 6Brain Center Rudolf Magnus, Department of Psychiatry, University 
Medical Center Utrecht, The Netherlands. 7Research Centre for Military Mental Healthcare, 
Ministry of Defence, Utrecht, The Netherlands. 8Department of Psychiatry, Leiden University 
Medical Center, Leiden, The Netherlands.

Abstract

Disruption of persistent, stress-associated memories is relevant for treating posttraumatic stress 
disorder (PTSD) and related syndromes, which develop in a subset of individuals following a 
traumatic event. We previously developed a stress-enhanced fear learning (SEFL) paradigm in 
inbred mice that produces PTSD-like characteristics in a subset of mice, including persistently 
enhanced memory and heightened cFos in the basolateral amygdala complex (BLC) with retrieval 
of the remote (30 day old) stress memory. Here the contribution of BLC microRNAs (miRNAs) to 
stress-enhanced memory was investigated because of the molecular complexity they achieve 
through their ability to regulate multiple targets simultaneously. We performed small-RNA 
sequencing (smRNA-Seq) and quantitative proteomics on BLC tissue collected from mice one 
month after SEFL and identified persistently changed microRNAs, including mir-135b-5p, and 
proteins associated with PTSD-like heightened fear expression. Viral-mediated overexpression of 
mir-135b-5p in the BLC of stress-resilient animals enhanced remote fear memory expression and 
promoted spontaneous renewal 14 days after extinction. Conversely, inhibition of BLC 
mir-135b-5p in stress-susceptible animals had the opposite effect, promoting a resilient-like 
phenotype. mir-135b-5p is highly conserved across mammals and was detected in postmortem 
human amygdala, as well as human serum samples. The mir-135b passenger strand, mir-135b-3p, 
was significantly elevated in serum from PTSD military veterans, relative to combat-exposed 
control subjects. Thus, miR-135b-5p may be an important therapeutic target for dampening 

Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, 
subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms
*Correspondence to: Courtney Miller cmiller@scripps.edu, 130 Scripps Way, Jupiter, FL 33458, Phone 561-228-2958. 
Disclosures: Authors declare no competing interests.

 
 
 
 
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

Sillivan et al.

Page 2

persistent, stress-enhanced memory and its passenger strand a potential biomarker for responsivity 
to a mir-135-based therapeutic.

Keywords

resilience; susceptibility; PTSD; memory; biomarker

Introduction

Unlike memory formation, mechanisms supporting long-lasting, remote memory are largely 
unknown, yet highly relevant to psychiatric disorders marked by persistent, unwanted 
memories, such as posttraumatic stress disorder (PTSD). PTSD is a chronic, debilitating 
disorder in which patients exhibit heightened, perseverant and extinction-resistant memories 
of trauma1. Nearly everyone experiences at least one traumatic event, but only 10–20% 
display enduring symptoms of PTSD2. Exposure therapy, a form of cognitive behavioral 
therapy (CBT) that utilizes extinction of fearful memories, is considered the gold standard 
treatment. However, many patients are resistant or experience exacerbated symptoms with 
exposure therapy and, of those who respond, most retain their PTSD diagnosis3. Thus, 
development of adjunctive pharmacotherapies to enhance success of the various forms of 
CBT is needed. But first, deeper insight into the underlying neurobiology to identify 
potential targets is required. Specifically, there is a need to better understand the mechanisms 
that determine differential responses to stress and how those responses persist for extended 
periods of time.

To identify mechanisms governing persistent, differential stress susceptibility, we developed 
a stress-enhanced fear learning (SEFL) paradigm in inbred C57BL/6 mice that results in 
PTSD-like characteristics, including persistently enhanced memory, in a subset of mice 
termed stress susceptible (SS)4, 5. This contrasts with stress resilient (SR) mice that do not 
display stress-induced enhancements. Importantly, the protocol allows for the study of 
molecular phenotypes associated with selective vulnerability because SS mice can be 
identified from training data, avoiding the mechanistic confounds introduced by the 
additional phenotyping commonly required. We also reported differential expression of 
genes with known polymorphisms in human PTSD genomic studies between SS and SR 
animals4.

A role for miRNAs in mediating memory has emerged over the past decade6. miRNAs are 
endogenous ~20–24 nucleotide RNAs that act as translational repressors through direct 
binding to the 3’-UTR of target mRNAs and noncleavage degradation of target mRNA via 
deadenylation7. Protein translation is required for formation of new memories, and its 
regulation via synapse-specific miRNA localization can modulate synaptic plasticity8–10. 
Indeed, the expression of miRNA biogenesis regulators Dicer and Pasha influences fear 
memories11, 12. Fear conditioning (FC) regulates miRNA expression and modulation of 
these miRNAs impacts consolidation and retrieval13–18. However, these prior studies all 
focused on recent, not remote, fear memory and the additional impact of stress is unknown. 
Yet, miRNAs are excellent remote memory candidate regulators because their wide genomic 

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 3

range of potential target proteins confers a complexity capable of handling the intricacies of 
memory. Importantly, mature miRNAs can have very long half-lives (i.e. months)19, lending 
themselves to the goal of memory persistence. Here we examined involvement of miRNAs 
in mediating susceptibility to remote, stress-enhanced memories in our SEFL paradigm, with 
the hypothesis that a unique miRNA signature defines susceptibility to stress-enhanced 
memory, differentiating it from stress resilience and providing a potential path for selective 
memory modulation20, 21.

Materials and Methods

Animals:

Adult C57BL/6 mice, 8–10 weeks of age (The Jackson Laboratory, Bar Harbor, ME), were 
maintained on a 12:12 hour light/dark cycle and supplied with food and water ad libitum. 
Mice were group housed 3–4/cage, acclimated to the facility for 1 week then handled for 3 
days prior to experiments. For additional details see Supplement 1.

Behavior:

Acute restraint stress and auditory fear conditioning (SEFL) were performed as previously 
described4. Extinction training consisted of 60 tone presentations over two days and retrieval 
consisted of 5 tones; both were performed in a context unique from training. Subthreshold 
training consisted of habituation to context A for 3×4 min trials 24 hours after Recall Test 1, 
followed by 2 CS-US pairings at 0.15mA the next day. 24 hours later, mice received Recall 
Test 2. For a full description of fear conditioning, extinction and anxiety tests (open field, 
elevated plus maze [EPM] and acoustic startle response), please refer to4 and Supplement 1.

Human serum samples:

Sequenced subjects (N=24) were part of a prospective cohort study of 1,032 Dutch military 
soldiers deployed to Afghanistan between 2005 and 2009 for four months22. All participants 
gave written informed consent and the study was conducted in accordance with the 
Declaration of Helsinki. For additional details see Supplement 1.

Human brain tissue:

Human amygdala containing all major sub-nuclei was dissected, snap frozen and stored at 
−80°C until further processing. Tissue was isolated from four control post-mortem brain 
samples (details below) from the Harvard Brain and Tissue Resource Center (HBTRC) at 
Mclean Hospital.

Sample

Group

Sex

Age

PMI

RIN

Cause of death

#30

#8

#39

#55

Control

Control

F

F

Control M

Control M

44

61

74

57

10.7

16.8

14.3

17.3

7.8

6.7

5.3

5.1

cardiac arrest

cardiopulmonary arrest/ myocardial infarction

cardiopulmonary arrest/ myocardial infarction

cardiac arrest; coronary artery disease

PMI: post-mortem interval in hours; RIN: RNA integrity number

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

RNA extraction:

Page 4

For rodent studies, total RNA was extracted from fresh frozen bilateral tissue punches using 
the miRVANA PARIS RNA extraction kit (Life Technologies, Carlsbad, CA). For human 
studies, total RNA was extracted using the Norgen RNA/DNA/Protein Purification Plus Kit 
(Norgen Biotek, Ontario, Canada) according to the manufacturer’s protocol. For additional 
details, please see supplemental methods.

miRNA Library Preparation, Sequencing and data analysis:

Single end smRNA-seq was performed on mouse BLC samples using the TruSeq small RNA 
library prep kit (Illumina, San Diego, CA) or the NEBNext Small RNA Library Prep Set for 
Illumina (New England BioLabs Inc., Ipswich, MA, USA). miRNAs that had at least 0.5 
log2 fold change between SS and SR in both sequencing runs were considered ‘candidate 
miRNAs’ and analyzed for pathway analysis. For human serum samples, libraries were also 
prepared with the TruSeq Kit For additional details, please see supplemental methods.

QPCR:

A cDNA library was created from 50ng of total RNA using the mirCURY LNA RT Kit 
(Qiagen, Germantown, MD) and PCR reactions were performed in triplicate for each sample 
using the miRCURY LNA SYBR Green PCR Kit and the following locked nucleic acid 
(LNA) SYBR green primers from Qiagen. Data were normalized using the Δ
Please see supplemental methods for additional details.

t method23. 

Δc

Quantitative mass spectrometry:

Pooled samples from each treatment group were submitted for liquid chromatography–mass 
spectrometry (LC-MS) at the Harvard Mass Spectrometry and Proteomics Resource 
Laboratory. Raw data were submitted for analysis in Proteome Discoverer 2.1.0.81 (Thermo 
Fisher) software. Candidate proteins were identified as those that had at least 1.5 log2 fold 
change between treatment groups. Please see supplemental methods for additional details.

miRNA inhibitors and lenti-miR viruses:

Miridian miRNA hairpin inhibitors directed against mmu-miR-135b-5p or the 
nonmammalian miRNA cel-miR-67 were obtained from GE Dharmacon (Lafayette, CO). To 
overexpress (OE) mir-135b-5p, pre-miR-135b-5p or a scramble nontargeting control 
sequence in the lentiviral vector CD513 were obtained from System Biosciences (Palo Alto, 
CA). The OE vector was packaged with GFP into lentivirus using a 2nd generation 
packaging system at the Emory Viral Vector Core (Emory University, Atlanta, GA). Titers 
obtained were 3×108 iu/ml for OE.

Intra-amygdalar infusions:

miRNA inhibitors, non-targeting controls, or lenti-mirs were injected bilaterally into the 
BLC (AP: 1.5 mm, ML: ±3.2 mm from bregma and DV: – 4.7 mm from the skull) of mice as 
previously described20. Inhibitors were reconstituted in water then prepared with jetPEI 
transfection reagent (Polyplus Transfection, Illkirch, France). 1ul of 400ng/ul was injected 
28 days after fear conditioning and then animals were tested 48 hours later. For lentiviral 

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 5

experiments, 1.5ul of viruses were injected 23 days after fear conditioning and animals were 
tested 1 week later to give sufficient time for viral expression.

Dual fluorescence in situ hybridization (FISH):

Expression analysis experiments to detect miRNAs were performed as described, with 
modification24. Please see supplemental methods for additional details.

Cell fractionation:

Fresh tissue was dissected from naïve animals and immediately placed into homogenization 
buffer as previously described25, with modification. Please see supplemental methods for 
additional details.

Statistics and data analysis:

All statistical results and sample sizes are reported in the figure legends. We identified 
candidate miRNAs based on fold change and reproducibility in two separate biological 
replicate cohorts of SEFL animals. miRNAs that had at least 0.5 log2 fold change difference 
between SS and SR animals were considered candidate regulators of traumatic memory. For 
comparisons with more than one group, an ANOVA was performed with post-hoc Tukey t-
tests. For comparisons with two groups, t-test were performed. For behavioral analyses of 
datapoints across time or extinction bins, a repeated measures ANOVA was performed. For 
correlations of two datapoints, a Pearson correlation was performed with the R squared 
value reported.

Results

Long-lasting dysregulation of miRNAs after stress-enhanced memory formation

SEFL was performed in male mice, followed by a remote memory test 30 days later (Fig. 
1A). As previously reported4, unbiased cluster analysis identifies varied memory strength at 
the recall test as a result of prior stress that was predicted by freezing during FC (Fig. 1B). 
Indeed, stressed animals that froze more during training displayed the highest freezing 
during the remote memory recall test and thus, were classified as SS. To interrogate 
mechanisms underlying differential memory strength between SS and SR animals, despite 
identical training and genetic homozygosity, we performed small RNA-sequencing 
(smRNA-Seq) and quantitative proteomics on basolateral amygdala complex (BLC; lateral 
and basolateral) tissue of SEFL-trained mice that did not undergo a retrieval test. Tissue was 
isolated 30 days after training to identify miRNAs in SS mice contributing to enhanced 
memory strength through persistent change following SEFL, not miRNA changes 
dynamically induced by the act of memory retrieval. The BLC was chosen because it is 
highly stress-responsive and fear memories rely on this region26. Further, we previously 
demonstrated that SS animals have exaggerated cFos activation in the BLC relative to SR 
and FC (no stress) animals, consistent with human PTSD imaging studies27. And, unlike 
hippocampus-dependent memories, for which influence shifts to the cortex as long-lasting 
memory develops, auditory fear memory continues to rely on the amygdala long after 
learning26. Importantly, freezing at the end of training, which classifies stress susceptibility, 
did not differ between SR and FC animals, but did differ between SR and SS (Fig. 1C).

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 6

SmRNA-Seq was performed on two separate cohorts of animals at two genomics facilities 
employing different reagents and bioinformatics pipelines to yield miRNA profiles 
associated with susceptibility to stress-enhanced memory. We compared the two datasets and 
identified 42 miRNAs that were differentially expressed between SS and SR groups in both 
datasets (Fig. 1D, Supplemental Table 1 and Supplemental Excel Table.1–2). 41 of these 
were upregulated in SS animals. Pathway analysis with DIANA’s mirPATH software using 
the microCts algorithm identified target pathways predicted to be regulated by these 
differentially expressed miRNAs. It included pathways that critically regulate stress and 
learning processes, including ECM-receptor interaction, MAPK signaling pathway and 
Thyroid Hormone Signaling (Fig. 1E). DIANA mirPath also provides access to two other 
target predicting algorithms, TargetScan and Tarbase. We compared all three algorithms and 
used the results to guide sequencing validation to miRNAs predicted by at least 2 algorithms 
that have targets significantly involved in pathways related to learning and memory 
(Supplemental Table 2).

One miRNA on this list, mir-135b-5p, is predicted to target proteins in both ECM-receptor 
interaction and Thyroid Hormone Signaling pathways. Interestingly, thyroid hormone 
signaling has been implicated in amygdala-based memory processes28, 29 and family 
members of mir-135b-5p have been studied in depressive and anxiety-like behaviors30, 31, as 
well as cortical axon guidance32 and synaptic plasticity33. Importantly, mir-135b-5p is 
conserved from mouse to human brain tissue34. Only one study has examined mir-135b-5p 
in the context of neuronal processes, identifying both mir-135a and mir-135b as regulators 
of axon guidance, migration and regeneration in cultured cortical and hippocampal cells32. 
We examined mir-135b-5p expression in the adult mouse brain and found it is broadly 
expressed in brain areas involved in emotion and memory, such as the BLC, the 
hypothalamus and the frontal cortex (Fig. 1F). In situ hybridization revealed anatomical 
localization of mir-135b-5p throughout the BLC (Fig. 1G). Using a cell fractionation assay, 
mir-135b-5p expression was detected throughout cells, including synaptosomes, where it 
could regulate synaptic protein translation underlying memory (Fig. 1H). Confirming the 
smRNA-Seq results by qPCR in an independent cohort that was not sequenced and did not 
undergo extinction training, we found BLC mir-135b-5p levels were elevated in SEFL 
animals that displayed the greatest freezing one month earlier, during training (Fig. 1I). The 
increase in mir-135b-5p was specific to the BLC, as no change was observed in other brain 
regions assessed from SEFL animals that have known roles in stress resilience and memory, 
such as the hippocampus, nucleus accumbens and the frontal cortex (Fig. 1J). Further, the 
selective elevation of levels of mir-135b-5p in SS BLC developed over time, as levels were 
equivalent across groups 24 hours and 7 days after SEFL (Fig. 1K). This suggests 
recruitment of mir-135b-5p during “incubation” of the fear memory35, rather than during its 
initial formation or consolidation. The validation of mir-135b-5p upregulation specifically in 
the BLC of SS animals 30 days after SEFL indicated that this candidate miRNA may 
contribute to the long-lasting traumatic memory phenotype. Therefore, we further explored 
the role of mir-135b-5p with in vivo functional manipulations in the SEFL model.

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 7

mir-135b-5p overexpression enhances memory expression in stress resilient mice

We examined the functional role of mir-135b-5p in regulating persistent stress-enhanced 
memory using a lentivirus that overexpresses (OE) pre-mir-135b-5p (premirOE-
mir-135b-5p) or a scrambled non-targeting sequence to mimic the elevated mir-135b-5p seen 
in SS mice. We injected premirOE-135b-5p into the BLC of SR mice 3 weeks after SEFL 
and performed extinction one week later (Fig. 2A). Enhanced memory expression was 
observed in SR-premirOE-135b-5p mice (Fig. 2B–C). Extinction was achieved with a strong 
protocol (Supplemental Fig. 1), yet mir-135b-5p levels remained elevated at the conclusion 
of extinction in SR-premirOE-135b-5p mice relative to SR-nontargeting control animals 
(Fig. 2D), suggesting the potential for spontaneous recovery if mediated by mir-135b-5p. 
Indeed, a 5-tone recall test two weeks after extinction demonstrated a return of enhanced 
fear memory in SR-premirOE-135b-5p animals (Fig. 2E). Anxiety-related open field, 
elevated plus maze and acoustic startle behaviors were no different in naïve animals injected 
with premirOE-135b-5p in the BLC or the nontargeting control, indicating that OE of 
mir-135b-5p is not simply anxiogenic (Supplemental Fig. S2).

mir-135b-5p inhibition selectively ameliorates stress-enhanced memory expression in 
stress susceptible mice

To explore the converse functional impact of mir-135b-5p on stress-enhanced memory, we 
utilized a synthetic hairpin mir-135b-5p inhibitor (INH) that sequesters mir-135b-5p to 
assess the consequence of mir-135b-5p inhibition on stress-enhanced memory in SS mice. 
We injected the INH into the BLC of mice 28 days after SEFL, followed by extinction 2 
days later (Fig. 3A). INH-mir-135b-5p reduced freezing in SS mice relative to a non-
targeting control inhibitor during the first 10 CS+ tone presentations (Fig. 3B–C). In 
addition, consistent with mir-135b-5p’s role in memory enhancement, the miRNA appeared 
to have been degraded during the extinction process in the INH-mir-135b-5p animals, which 
displayed reduced freezing, as its levels were markedly reduced in the INH-mir-135b-5p 
group by the end of the extinction protocol (2 days; Fig. 3D). Two weeks after the two day 
extinction protocol, which results in complete extinction (Supplemental Fig. 3), we assessed 
extinction retention with a 5-tone recall test and observed no differences between the groups 
(Fig. 3E). However, a subthreshold training protocol resulted in further enhancement of the 
fear memory in SS-INH-nontargeting controls that was absent in SS-INH-mir-135b-5p mice, 
suggesting a persistent dampening of memory via prior mir-135b-5p inhibition, rather than 
acute suppression of retrieval (Fig. 3F).

Interestingly, further knockdown of BLC mir-135b-5p in SR animals via BLC infusion of 
INH-mir-135b-5p did not alter memory (Fig. 3G). This may not be surprising, as levels of 
mir-135b-5p are not different between FC and SR males (Fig. 1I). We have previously 
reported that SEFL females do not cluster into stress-induced subgroups, but rather, display 
a more uniform SS-like phenotype4. Here we find that levels of mir-135b-5p do not differ 
between FC and SEFL females, regardless of their freezing during training (Fig. 3H). In 
accordance with this, INH-mir-135b-5p in SEFL females does not reduce memory strength 
(Fig. 3I). Together this suggests not only a sex-specific role for mir-135b-5p, but also a 
threshold of its expression must be reached to achieve pathologic memory effects and 
subsequent amelioration by reduction of mir-135b-5p levels. Further, BLC mir-135b-5p 

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 8

levels are not merely anxiotropic, as we observed no differences in anxiety-related open field 
and elevated plus maze tasks after INH-mir-135b-5p infusion in naïve mice (Supplemental 
Fig. 2). Importantly, delivery of non-targeting viral and inhibitor controls to the BLC did not 
disrupt the expected phenotypic differences in memory strength between SS and SR 
animals4 (Supplemental Fig. 2), indicating that behavioral differences observed also cannot 
be attributed to technical manipulation of the BLC disrupting stress-associated phenotypes.

mir-135b is conserved in humans and elevated in serum of military personnel with PTSD

The mir-135b stem loop sequence is 100% conserved from mouse to human (Fig. 4A). 
While amygdala tissue from human PTSD subjects could not be obtained for this project, we 
measured levels of mature mir-135b-5p and the −3p arm, indicated to be the passenger 
strand by miRBase 22, in postmortem human amygdala tissue by qPCR (Fig. 4B and 
Supplemental Fig. 4). Both were detected, but −5p was expressed at much higher levels than 
−3p, indicating this is the major mir-135b isoform in the human amygdala. This is consistent 
with miRBase 22’s assignment of −3p as the passenger strand and our own finding that −3p 
levels in the mouse BLC and plasma are below the level of detection by qPCR. Interestingly, 
−5p levels are also below the level of detection in mouse plasma. We next measured levels of 
mir-135b-5p and −3p in serum samples collected from a cohort of well-characterized male 
Dutch military six months after a four month deployment in Afghanistan, at which time 
trauma exposure and PTSD symptomatology were assessed. mir-135b-3p was selectively 
elevated in members of the military diagnosed with PTSD (“susceptible”) relative to 
members without the diagnosis (“resilient”) and non-trauma exposed healthy military 
controls (Fig. 4C–D and Supplemental Excel Table 3). Consistent with levels of −3p being 
low, there were two samples with values of 0 in the data, one in the Control group and one in 
the PTSD Resilient group. To ensure that these two data points were not responsible for the 
significant elevation in the PTSD Susceptible group, we first confirmed they were not 
outliers by a Grubbs Test. They could not be statistically excluded based on a Grubbs test, 
but we still repeated the ANOVA without the data points and found that the statistical 
support for selective elevation of mir-135b-3p in PTSD Susceptible was further strengthened 
by their exclusion (F(2,15)=18.65, P<0.0001; Post hoc: Control vs PTSD Susceptible 
P=0.0002, PTSD Resilient vs Susceptible P=0.0012). Passenger strands have traditionally 
been thought to be degraded upon release from the mature strand at the site of production. 
However, growing evidence indicates they can enter circulation and functionally impact 
distal structures36. Therefore, it will be important to identify the sites and actions of elevated 
mir-135b-3p. Regardless, this identifies mir-135b-3p’s potential as a biomarker of PTSD.

Long-lasting BLC proteomic dysregulation in SS mice includes mir-135b-5p putative 
targets

While some studies on miRNAs in the brain have successfully identified an individual 
protein target capable of recapitulating the behavioral effect of the miRNA of interest, these 
protein targets often have a wide genomic impact themselves. Examples include 
transcription factors and epigenetic modifiers37, 38. However, one appealing aspect of 
miRNAs in the context of psychiatric disorders is the potential for a single miRNA to 
simultaneously titrate the levels of multiple protein targets to achieve behavioral outcomes. 
Therefore, we performed quantitative mass spectrometry (MS) on BLC tissue from SEFL 

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 9

animals 30 days after training (no extinction) to identify proteome-wide potential 
mir-135b-5p targets that may participate in stress-enhanced memory. 3,560 proteins were 
detected in the BLC by MS, with 72 downregulated and 663 upregulated by at >1.5 log2 fold 
change between SS and SR (Fig. 5A and Supplemental Excel Table 4). The top 10 most 
significant pathways from Ingenuity Pathway Analysis (IPA) revealed functional annotations 
related to neuronal structure (e.g. Density of microtubules, Organization of cytoskeleton) in 
the downregulated protein list (Fig. 5B), while the upregulated pathways included transport 
of molecules and several related to cancers (Fig. 5C). The 5 proteins with the greatest 
increase in SS BLC are listed in Figure 5D. While many proteins are expected to participate 
in miRNA-independent processes, downregulation of SS proteins could reflect a coordinated 
interaction with upregulated miRNAs that are responsive to stress-enhanced memory, such 
as mir-135b-5p. A total of 272 mir-135b-5p targets were predicted by at least two of the 
three major databases (TargetScan, DIANA, mirDB), but only 76 were detected in BLC 
tissue at both the RNA and protein level (Fig. 5E). Interestingly, 24% (18) of predicted 
mir-135b-5p protein targets detected in the BLC were regulated between SS and SR animals 
in the proteomics dataset and included Ntrk2, the TrkB BDNF receptor well characterized 
for its role in amygdala-dependent fear and extinction learning, as well as PTSD (Fig. 5E–
F)39. Pathway analysis of these 18 mir-135b-5p putative targets that were changed by SEFL 
identified annotations related to neuronal function, including spatial learning, long-term 
depression of neurons, plasticity of synapse and excitatory postsynaptic potential of neurons 
(Fig. 5G). Because many predicted mir-135b-5p targets could be false positives, we also 
examined the BLC proteome of naïve animals injected with premirOE-135b-5p in the BLC 
at physiologically relevant levels. We aligned the MS datasets and identified 13 proteins 
downregulated by >50% in both SS animals and naive premirOE-135b-5p animals (Fig. 5H), 
with functions including protein folding and degradation (Bag3), chromosome looping 
(Hmgb2), ion channel trafficking (Caskin1) and vesicle transport (Arfgap1). The number of 
potential targets increased to 99 proteins with a criteria of downregulation by >25%. IPA 
identified pathways related to neuronal function (e.g. Neuromuscular disease, Disorder of 
basal ganglia), as well as non-neuronal pathways with molecules in need of future functional 
studies in the brain (Fig. 5I).

Discussion

Utilizing a stress-enhanced fear learning protocol we developed4, that results in differential 
stress susceptibility in an inbred mouse strain commonly used in neuroscience, c57bl/6, we 
identified 42 miRNAs differentially expressed in the amygdala between susceptible and 
resilient mice one month after training. Based on its conservation in humans and predicted 
regulation of processes that could be reasonably expected to contribute to memory, we 
selected one of these, mir-135b-5p, for in-depth study. After confirming that remote 
(between 7 and 30 days post-SEFL) upregulation of mir-135b-5p is selective to SS mice, we 
further determined the change was unique to the amygdala, in that mir-135b-5p levels were 
unchanged by SEFL in other memory and stress-related brain regions. Elevating local BLC 
levels of mir-135b-5p in resilient mice enhanced remote fear memory expression, 
phenocopying the stress-enhanced memory displayed by SS mice, and resulted in 
spontaneous renewal of the memory two weeks after complete extinction. Conversely, intra-

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 10

amygdala inhibition of mir-135b-5p in SS mice resulted in a marked reduction in freezing 
and suppressed renewal of the memory with subthreshold training two weeks after complete 
extinction.

The bidirectional impact of mir-135b-5p manipulation on memory strength begs the 
question of what memory process is most likely being targeted. miRNA levels were 
measured by smRNA-seq one month after SEFL training in the absence of retrieval, in order 
to identify contributors to enhanced remote memory strength observed in SS mice, as 
opposed to dynamic, retrieval-induced changes. Our hypothesis that mir-135b-5p contributes 
to the long-term storage of remote, stress-enhanced memory will require development of a 
small molecule inhibitor in order to achieve tight temporal control of the miRNA’s 
activity40. However, some evidence in support of the memory storage hypothesis can be 
drawn from the present results. First, mir-135b-5p’s elevation associated with stress 
susceptibility is present in SS mice at rest in the home cage, rather than being retrieval-
induced. mir-135b-5p’s impact on memory could still be due to enhanced retrieval of remote 
fear memories in SS mice. However, prior inhibition of mir-135b-5p in SS mice prevented 
the return of fear after subthreshold training two weeks later, indicating this miRNA has a 
role beyond the acute blockade of retrieval. In addition, the lack of an effect of mir-135b-5p 
inhibition in SR males and SEFL females argues against INH-mir-135b-5p producing a 
retrieval deficit. Accelerated extinction is also an unlikely explanation for the reduction in 
fear memory strength in SS mice following knockdown of mir-135b-5p, as the inhibitor, 
delivered 48 hours prior, had an immediate effect on memory expression, present from the 
first conditioned stimulus presentation. A blockade of reconsolidation is also unlikely, as the 
reduction in memory strength in INH-mir-135b-5p SS mice was not retrieval-dependent; 
reduced freezing was present from the start of the first retrieval test. Taken together, the most 
parsimonious explanation is that mir-135b-5p specifically contributes to the storage of 
stress-enhanced fear memory within the amygdala. While a pharmacological approach will 
be needed to definitively address this, we are intrigued by the possibility that maladaptive, 
stress-enhanced memory could be selectively titrated, without influencing other memories, 
as suggested by the results presented in Figure 3. Indeed, there is precedent for the selective, 
retrieval-independent targeting of maladaptive memories, as we have previously identified a 
mechanism unique to the storage of methamphetamine-associated memory that allows for its 
selective disruption20, 21.

Combining smRNA-Seq with global quantitative MS identified a number of putative 
miRNA-dependent and -independent pathways differentially regulated between SS and SR 
animals that warrant further investigation, as many are likely critical regulators of the 
maladaptive behavioral and neurochemical adaptations associated with persistent, stress-
enhanced memory. This approach is also powerful, in that target identification is not limited 
to the miRNA target prediction algorithms, which are unable to take into account factors 
such as tissue and cell type-specificity and noncanonical miRNA-target interactions, such as 
center binding. Indeed, without this a priori prediction filter, our quantitative MS identified 
many proteins regulated in the context of mir-135b-5p overexpression that are not predicted 
mir-135b-5p targets by Targetscan. These changes are likely a combination of secondary 
responses to the overexpression and true, direct mir-135b-5p mediated suppression that 
warrant additional investigation. These include CASK Interacting Protein 1 (Caskin1), a 

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 11

cytosolic protein that binds scaffolding membrane proteins such as CASK at presynaptic 
sites41; ADP Ribosylation Factor GTPase Activating Protein 1 (Arfgap1), a GTPase that 
regulates vesicle release and protein trafficking within the Golgi and endoplasmic 
reticulum42; and TANK Binding Kinase 1 (Tbk1), a serine/threonine kinase for which 
variants have been associated with early-onset Alzheimer disease43. It will be interesting to 
determine if disruption of a single mir-135b-5p target is sufficient to recapitulate the impact 
of inhibiting the miRNA itself, or if the simultaneous inhibition of several targets, a unique 
capability of miRNAs, is required.

Further bolstering the therapeutic potential of mir-135b-5p, we found that this conserved 
miRNA is expressed in human amygdala and the miRNA’s passenger strand, mir-135b-3p, 
is elevated in individuals from a well-characterized military cohort diagnosed with PTSD 
after a four month deployment to Afghanistan. The upregulation of mir-135b-3p was 
specific to susceptible individuals, as it was not elevated in individuals from the same 
military cohort that did not develop PTSD as a result of the same combat exposure. In Figure 
3 we report that the elevation of mir-135b-5p is specific to male mice, as is the behavioral 
impact of reducing intra-amygdala levels of the miRNA. Interestingly, the Dutch military 
cohort consisted solely of men. Thus, it will be important to ascertain the levels of mir-135b 
in females diagnosed with PTSD in order to determine the extent to which this miRNA’s 
impact is sex-specific. Regardless, the correspondence between the SEFL findings and 
results in humans with a PTSD diagnosis argues for the therapeutic discovery potential of 
the SEFL protocol4 and suggests that mir-135b-3p may serve as a biomarker capable of 
identifying individuals that would be responsive to a mir-135b-based therapeutic40.

Supplementary Material

Refer to Web version on PubMed Central for supplementary material.

Acknowledgements

We thank the Scripps Florida Genomics Core for sequencing services, Nripesh Prasad at the Genomic Services Lab 
at Hudson Alpha for sequencing services and data analysis, Adrian Reich and the Bioinformatics Core for data 
analysis, the Mouse Behavior core and Alicia Brantley for assistance and behavioral equipment, all members of the 
Miller/Rumbaugh Labs for their technical assistance and thoughtful discussions. This work was funded by grants 
from the National Institute of Mental Health MH105400 and MH105400–02 (Diversity Supplement) (CM), 
National Institute of Neurological Disorders and Stroke NS096833 (CM), National Institute on Drug Abuse 
DA041469 (SS) and the Brain and Behavior Foundation-NARSAD Young Investigator Award (SS). This research 
project was supported in part by the Viral Vector Core of the Emory Neuroscience National Institute of 
Neurological Disorders and Stroke Core Facilities grant, P30NS055077. LdN and smRNA-Seq experiments in 
human serum were funded by a VIDI award number 91718336 from the Netherlands Scientific Organization (BR) 
and the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie 
grant agreement No 707362 (LDN).

References:

1. American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders. 5th edn: 

Washington, DC, 2013.

2. Kessler RC, Chiu WT, Demler O, Merikangas KR, Walters EE. Prevalence, severity, and 

comorbidity of 12-month DSM-IV disorders in the National Comorbidity Survey Replication. Arch 
Gen Psychiatry 2005; 62(6): 617–627. [PubMed: 15939839] 

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 12

3. Schottenbauer MA, Glass CR, Arnkoff DB, Tendick V, Gray SH. Nonresponse and dropout rates in 
outcome studies on PTSD: review and methodological considerations. Psychiatry 2008; 71(2): 134–
168. [PubMed: 18573035] 

4. Sillivan SE, Joseph NF, Jamieson S, King ML, Chevere-Torres I, Fuentes I et al. Susceptibility and 
Resilience to Posttraumatic Stress Disorder-like Behaviors in Inbred Mice. Biol Psychiatry 2017; 
82(12): 924–933. [PubMed: 28778658] 

5. Levinsohn EA, Ross DA. To Bend and Not Break: The Neurobiology of Stress, Resilience, and 

Recovery. Biol Psychiatry 2017; 82(12): e89–e90. [PubMed: 29129201] 

6. Bredy TW, Lin Q, Wei W, Baker-Andresen D, Mattick JS. MicroRNA regulation of neural plasticity 

and memory. Neurobiol Learn Mem 2011; 96(1): 89–94. [PubMed: 21524708] 

7. Eulalio A, Huntzinger E, Nishihara T, Rehwinkel J, Fauser M, Izaurralde E. Deadenylation is a 

widespread effect of miRNA regulation. RNA 2009; 15(1): 21–32. [PubMed: 19029310] 

8. Hou Q, Ruan H, Gilbert J, Wang G, Ma Q, Yao WD et al. MicroRNA miR124 is required for the 

expression of homeostatic synaptic plasticity. Nat Commun 2015; 6: 10045. [PubMed: 26620774] 
9. Lee K, Kim JH, Kwon OB, An K, Ryu J, Cho K et al. An activity-regulated microRNA, miR-188, 
controls dendritic plasticity and synaptic transmission by downregulating neuropilin-2. J Neurosci 
2012; 32(16): 5678–5687. [PubMed: 22514329] 

10. Schratt GM, Tuebing F, Nigh EA, Kane CG, Sabatini ME, Kiebler M et al. A brain-specific 

microRNA regulates dendritic spine development. Nature 2006; 439(7074): 283–289. [PubMed: 
16421561] 

11. Fiorenza A, Lopez-Atalaya JP, Rovira V, Scandaglia M, Geijo-Barrientos E, Barco A. Blocking 
miRNA Biogenesis in Adult Forebrain Neurons Enhances Seizure Susceptibility, Fear Memory, 
and Food Intake by Increasing Neuronal Responsiveness. Cereb Cortex 2016; 26(4): 1619–1633. 
[PubMed: 25595182] 

12. Konopka W, Kiryk A, Novak M, Herwerth M, Parkitna JR, Wawrzyniak M et al. MicroRNA loss 
enhances learning and memory in mice. J Neurosci 2010; 30(44): 14835–14842. [PubMed: 
21048142] 

13. Dias BG, Goodman JV, Ahluwalia R, Easton AE, Andero R, Ressler KJ. Amygdala-dependent fear 
memory consolidation via miR-34a and Notch signaling. Neuron 2014; 83(4): 906–918. [PubMed: 
25123309] 

14. Volk N, Paul ED, Haramati S, Eitan C, Fields BK, Zwang R et al. MicroRNA-19b associates with 
Ago2 in the amygdala following chronic stress and regulates the adrenergic receptor beta 1. J 
Neurosci 2014; 34(45): 15070–15082. [PubMed: 25378171] 

15. Griggs EM, Young EJ, Rumbaugh G, Miller CA. MicroRNA-182 regulates amygdala-dependent 

memory formation. J Neurosci 2013; 33(4): 1734–1740. [PubMed: 23345246] 

16. Lin Q, Wei W, Coelho CM, Li X, Baker-Andresen D, Dudley K et al. The brain-specific 

microRNA miR-128b regulates the formation of fear-extinction memory. Nat Neurosci 2011; 
14(9): 1115–1117. [PubMed: 21841775] 

17. Mathew RS, Tatarakis A, Rudenko A, Johnson-Venkatesh EM, Yang YJ, Murphy EA et al. A 

microRNA negative feedback loop downregulates vesicle transport and inhibits fear memory. Elife 
2016; 5.

18. Wang RY, Phang RZ, Hsu PH, Wang WH, Huang HT, Liu IY. In vivo knockdown of hippocampal 
miR-132 expression impairs memory acquisition of trace fear conditioning. Hippocampus 2013; 
23(7): 625–633. [PubMed: 23520022] 

19. Schaefer A, O’Carroll D, Tan CL, Hillman D, Sugimori M, Llinas R et al. Cerebellar 

neurodegeneration in the absence of microRNAs. J Exp Med 2007; 204(7): 1553–1558. [PubMed: 
17606634] 

20. Young EJ, Blouin AM, Briggs SB, Sillivan SE, Lin L, Cameron MD et al. Nonmuscle myosin IIB 
as a therapeutic target for the prevention of relapse to methamphetamine use. Mol Psychiatry 
2016; 21(5): 615–623. [PubMed: 26239291] 

21. Young EJ, Aceti M, Griggs EM, Fuchs RA, Zigmond Z, Rumbaugh G et al. Selective, retrieval-

independent disruption of methamphetamine-associated memory by actin depolymerization. Biol 
Psychiatry 2014; 75(2): 96–104. [PubMed: 24012327] 

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 13

22. Rutten BPF, Vermetten E, Vinkers CH, Ursini G, Daskalakis NP, Pishva E et al. Longitudinal 

analyses of the DNA methylome in deployed military servicemen identify susceptibility loci for 
post-traumatic stress disorder. Mol Psychiatry 2018; 23(5): 1145–1156. [PubMed: 28630453] 
23. Livak KJ, Schmittgen TD. Analysis of relative gene expression data using real-time quantitative 

PCR and the 2(-Delta Delta C(T)) Method. Methods 2001; 25(4): 402–408. [PubMed: 11846609] 

24. Kasai A, Kakihara S, Miura H, Okada R, Hayata-Takano A, Hazama K et al. Double In situ 

Hybridization for MicroRNAs and mRNAs in Brain Tissues. Front Mol Neurosci 2016; 9: 126. 
[PubMed: 27920667] 

25. Most D, Ferguson L, Blednov Y, Mayfield RD, Harris RA. The synaptoneurosome transcriptome: a 
model for profiling the emolecular effects of alcohol. Pharmacogenomics J 2015; 15(2): 177–188. 
[PubMed: 25135349] 

26. Gale GD, Anagnostaras SG, Godsil BP, Mitchell S, Nozawa T, Sage JR et al. Role of the 

basolateral amygdala in the storage of fear memories across the adult lifetime of rats. J Neurosci 
2004; 24(15): 3810–3815. [PubMed: 15084662] 

27. Stevens JS, Kim YJ, Galatzer-Levy IR, Reddy R, Ely TD, Nemeroff CB et al. Amygdala Reactivity 

and Anterior Cingulate Habituation Predict Posttraumatic Stress Disorder Symptom Maintenance 
After Acute Civilian Trauma. Biol Psychiatry 2017; 81(12): 1023–1029. [PubMed: 28117048] 
28. Barez-Lopez S, Montero-Pedrazuela A, Bosch-Garcia D, Venero C, Guadano-Ferraz A. Increased 
anxiety and fear memory in adult mice lacking type 2 deiodinase. Psychoneuroendocrinology 
2017; 84: 51–60. [PubMed: 28654773] 

29. Montero-Pedrazuela A, Fernandez-Lamo I, Alieva M, Pereda-Perez I, Venero C, Guadano-Ferraz 
A. Adult-onset hypothyroidism enhances fear memory and upregulates mineralocorticoid and 
glucocorticoid receptors in the amygdala. PLoS One 2011; 6(10): e26582. [PubMed: 22039511] 
30. Issler O, Haramati S, Paul ED, Maeno H, Navon I, Zwang R et al. MicroRNA 135 is essential for 
chronic stress resiliency, antidepressant efficacy, and intact serotonergic activity. Neuron 2014; 
83(2): 344–360. [PubMed: 24952960] 

31. Mannironi C, Biundo A, Rajendran S, De Vito F, Saba L, Caioli S et al. miR-135a Regulates 
Synaptic Transmission and Anxiety-Like Behavior in Amygdala. Mol Neurobiol 2017.

32. van Battum EY, Verhagen MG, Vangoor VR, Fujita Y, Derijck A, O’Duibhir E et al. An Image-

Based miRNA screen identifies miRNA-135s as regulators of CNS axon growth and regeneration 
by targeting Kruppel-like factor 4. J Neurosci 2017.

33. Hu HY, Guo S, Xi J, Yan Z, Fu N, Zhang X et al. MicroRNA expression and regulation in human, 
chimpanzee, and macaque brains. PLoS Genet 2011; 7(10): e1002327. [PubMed: 22022286] 
34. de Rie D, Abugessaisa I, Alam T, Arner E, Arner P, Ashoor H et al. An integrated expression atlas 
of miRNAs and their promoters in human and mouse. Nat Biotechnol 2017; 35(9): 872–878. 
[PubMed: 28829439] 

35. Pickens CL, Golden SA, Adams-Deutsch T, Nair SG, Shaham Y. Long-lasting incubation of 
conditioned fear in rats. Biol Psychiatry 2009; 65(10): 881–886. [PubMed: 19167702] 

36. Wu CaA P MicroRNA Passenger Strand. Circulation Cardiovascular Genetics 2014; 7: 567–568. 

[PubMed: 25140065] 

37. Hollander JA, Im HI, Amelio AL, Kocerha J, Bali P, Lu Q et al. Striatal microRNA controls 

cocaine intake through CREB signalling. Nature 2010; 466(7303): 197–202. [PubMed: 20613834] 

38. Im HI, Hollander JA, Bali P, Kenny PJ. MeCP2 controls BDNF expression and cocaine intake 
through homeostatic interactions with microRNA-212. Nat Neurosci 2010; 13(9): 1120–1127. 
[PubMed: 20711185] 

39. Andero R, Ressler KJ. Fear extinction and BDNF: translating animal models of PTSD to the clinic. 

Genes Brain Behav 2012; 11(5): 503–512. [PubMed: 22530815] 

40. Velagapudi SP, Gallo SM, Disney MD. Sequence-based design of bioactive small molecules that 
target precursor microRNAs. Nat Chem Biol 2014; 10(4): 291–297. [PubMed: 24509821] 

41. Stafford RL, Ear J, Knight MJ, Bowie JU. The molecular basis of the Caskin1 and Mint1 

interaction with CASK. J Mol Biol 2011; 412(1): 3–13. [PubMed: 21763699] 

42. Chornyy S, Parnis A, Shmoish M, Cassel D. High abundance of ArfGAP1 found in the mossy 

fibers in hilus of the dentate gyrus region of the mouse brain. PLoS One 2017; 12(12): e0189659. 
[PubMed: 29240824] 

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 14

43. Verheijen J, van der Zee J, Gijselinck I, Van den Bossche T, Dillen L, Heeman B et al. Common 
and rare TBK1 variants in early-onset Alzheimer disease in a European cohort. Neurobiol Aging 
2018; 62: 245.e241–245.e247.

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 15

Figure 1. SEFL induces long-lasting miRNA changes in the BLC
(A) Overview of experimental paradigm to study long-term memory storage in SEFL mice. 
(B) Pearson correlation between freezing during 5-tone recall test and freezing during cued 
FC in SEFL trained mice, with animals divided into SR (pink) or SS (red) subgroups based 
on training performance4, r = 0.601, p = 0.003, n = 22. (C) Cued FC profile of SEFL trained 
animals used for smRNA-seq (no retrieval). RM-ANOVA between SR and SS: F(1,14) = 
5.05; p = 0.041; post hoc t-test: t(14) = 3.315, p = 0.0005. n=6–9/group. (D) Volcano plot of 
miRNA expression in SS vs SR animals. (E) Pathway analysis of miRNAs listed in D using 
DIANA mirPath software and the microCts algorithm to identify pathways significantly 
targeted by SS miRNAs. (F) Characterization of mir-135b-5p expression in the adult mouse 
brain, n = 2–3/region. (G) Localization of mir-135b-5p in the BLC measured with in situ 
hybridization. (H) Characterization of mir-135b-5p expression in subcellular fractions to 
determine localization, n = 4/region. (I) qPCR validation of elevated BLC mir-135b-5p 
expression in SS mice. One-way ANOVA: F(3, 12) = 5.532; p = 0.0128; Post-hoc Tukey test 
p < 0.05 for high vs FC (*) and high vs moderate (#), n = 4–7/group. (J) mir-135b-5p levels 
in the hippocampus hippocampus (Hpc), nucleus accumbens (NAc) or the frontal cortex 
(FrCtx) of mice 30 days after SEFL (no extinction), n = 8–12/group. (K) mir-135b-5p levels 
in the BLC 24 hours or 7 days after SEFL (no extinction), n=6–8/group. Error bars are ± 
S.E.M.

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 16

Figure 2. mir-135b-5p overexpression enhances traumatic memory expression in SR mice.
(A) Overview of strategy to OE BLC mir-135b-5p in SR animals. (B-C) Freezing during the 
first ten tones of extinction on Day 1. RM-ANOVA for 10 tones extinction Day 1: F(1,21) = 
6.04; p = 0.023. Unpaired t-test for average of 10 tones: t(21) = 2.457, p = 0.0228. 
Nontargeting virus n = 10, premirOE-135b-5p n = 13. (D) mir-135b-5p levels in SR mice 
after extinction. Unpaired t-test: t(18) = 2.532, p = 0.0209. Nontargeting virus n = 9; 
premirOE-135b-5p n = 11. (E) Extinction retention from the end of extinction day 2 
(average freezing to tones 28–30) to a 5 tone recall test 2 weeks later. RM-ANOVA 5 tone 
recall: F(1,20) = 5.27, p = 0.033. Post-hoc t-test for tone 1: t(20) = 2.673, p = 0.0146. 
Nontargeting virus n = 9, premirOE-135b-5p n = 13. Error bars are ± S.E.M.

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 17

Figure 3. BLC inhibition of mir-135b-5p in SS mice weakens stress-enhanced memory 
expression.
(A) Overview of strategy to decrease BLC mir-135b-5p tone in SS animals. (B-C) Freezing 
during first 10 tones on Day 1 of extinction. RM-ANOVA for 10 tones extinction day 1: 
F(1,28)=5.814; p=0.023. Unpaired t-test for average of 10 tones: t(29) =2.638, p=0.0133. 
Nontargeting control n = 14, INH-mir-135b-5p n = 17. (D) mir-135b-5p levels in SS mice 
after inhibition. Unpaired t-test: t(18) = 2.987, p = 0.0079. Nontargeting control n = 9; INH-
mir-135b-5p n = 11. (E) Extinction retention from the end of extinction Day 2 to the first 5 
tone recall test. (F) Freezing after subthreshold re-training. Paired t-test SS-
nontargetingINH: t(3) = 3.927, p = 0.0294. Nontargeting control n = 4; INH-mir-135b-5p n = 
6. (G) Extinction (6 tone bins) for SR male mice injected with INH-mir-135b-5p or 
nontargeting control. (H) mir-135b-5p expression in the BLC of SEFL females (no 
extinction) 30 days after training. (I) Extinction (6 tone bins) for stressed female mice 
injected with INH-mir-135b-5p inhibitor or nontargeting control. Error bars are ± S.E.M.

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 18

Figure 4. mir-135b is highly conserved in humans and elevated in the serum of PTSD-susceptible 
subjects.
(A) Conservation of the mouse pre-mir-135b sequence from mouse to human. The 
sequences of the 5’ and 3’ arms are highlighted in yellow. (B) qPCR expression of mir-135b 
isoforms in human amygdala, n = 3–4 brains. (C) Characteristics of human subjects used for 
the evaluation of circulating mir-135b in serum. (D) Sequencing expression of mir-135b 
isoforms in the serum of human subjects. One-way ANOVA for mir-135b-3p: F(2, 17) = 
15.32; p = 0.0002; Post-hoc Tukey test p < 0.05 for control vs susceptible (*) and resilient vs 
susceptible (#), n = 6–8/group. Error bars are ± S.E.M.

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.

 
 
 
 
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

Sillivan et al.

Page 19

Figure 5. Global proteomic profile identifies putative mir-135b-5p targets downregulated in SS 
animals.
(A) Summary of the protein changes identified in BLC tissue that are at least 1.5 log2fold 
change between SS and SR animals 30 days after SEFL and the top 10 significant pathways 
of downregulated (B) or upregulated proteins (C). (D) The top 5 upregulated proteins in SS 
vs SR animals that were identified in the proteomics screen. (E-F) Protein expression of 
putative mir-135b-5p targets obtained by mass spectrometry that are 1.5 log2 fold change or 
greater between SS and SR animals 30 days after SEFL and the top 10 significant pathways 
of regulated mir-135b-5p target proteins (G). (H-I) Proteins changed by at least 50% in BLC 
tissue after viral mediated mir-135b-5p overexpression or SEFL and the top regulated 
pathways in proteins changed by at least 25% in those groups.

Mol Psychiatry. Author manuscript; available in PMC 2019 November 30.
