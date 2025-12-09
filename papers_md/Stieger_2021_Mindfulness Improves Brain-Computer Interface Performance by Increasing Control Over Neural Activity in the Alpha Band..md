# Stieger_2021_Mindfulness Improves Brain-Computer Interface Performance by Increasing Control Over Neural Activity in the Alpha Band.

Cerebral Cortex, January 2021;31: 426–438

doi: 10.1093/cercor/bhaa234
Advance Access Publication Date: 23 September 2020
Original Article

O R I G I N A L A R T I C L E

Mindfulness Improves Brain–Computer Interface
Performance by Increasing Control Over Neural
Activity in the Alpha Band

James R. Stieger
Mary Jo Kreitzer4 and Bin He 1

1,2, Stephen Engel3, Haiteng Jiang1, Christopher C. Cline2,

1Department of Biomedical Engineering, Carnegie Mellon University, Pittsburgh, PA 15213, USA, 2Department
of Biomedical Engineering, University of Minnesota, Minneapolis, MN 55414, USA, 3Department of Psychology,
University of Minnesota, Minneapolis, MN 55414, USA and 4Earl E. Bakken Center for Spirituality & Healing,
University of Minnesota, Minneapolis, MN 55414, USA

Address correspondence to Bin He, PhD, Department of Biomedical Engineering, Carnegie Mellon University, 5000 Forbes Avenue, Pittsburgh, PA 15213,
USA. Email: bhe1@andrew.cmu.edu.

Abstract

Brain–computer interfaces (BCIs) are promising tools for assisting patients with paralysis, but suffer from long training
times and variable user proficiency. Mind–body awareness training (MBAT) can improve BCI learning, but how it does so
remains unknown. Here, we show that MBAT allows participants to learn to volitionally increase alpha band neural
activity during BCI tasks that incorporate intentional rest. We trained individuals in mindfulness-based stress reduction
(MBSR; a standardized MBAT intervention) and compared performance and brain activity before and after training between
randomly assigned trained and untrained control groups. The MBAT group showed reliably faster learning of BCI than the
control group throughout training. Alpha-band activity in electroencephalogram signals, recorded in the volitional resting
state during task performance, showed a parallel increase over sessions, and predicted final BCI performance. The level of
alpha-band activity during the intentional resting state correlated reliably with individuals’ mindfulness practice as well
as performance on a breath counting task. Collectively, these results show that MBAT modifies a specific neural signal
used by BCI. MBAT, by increasing patients’ control over their brain activity during rest, may increase the effectiveness of
BCI in the large population who could benefit from alternatives to direct motor control.

Key words: alpha rhythm, brain–computer interface, learning, mindfulness meditation, rehabilitation

Introduction

Through noninvasively decoding user intent in real time, brain–
computer interfaces (BCIs) bypass traditional neuromuscular
pathways to provide alternative routes of communication and
action for those afflicted by paralysis resulting from stroke,
trauma, and other neuromuscular disorders. One promising
approach attempts to decipher motor imagery from the
electroencephalogram (EEG) by recording sensorimotor rhythms
(SMRs), which predictably change in response to real and
imagined movements (Pfurtscheller and Neuper 2001; He et al.
2013). The intuitive and continuous nature of SMR-based BCIs

enables the extension of the user through the control of virtual
objects, drones, wheelchairs, and robotic arms (Wolpaw and
McFarland 2004; Tsui et al. 2011; Lafleur et al. 2013; Edelman
et al. 2019). Users, for example, might imagine turning a steering
wheel with their left hand to direct a wheelchair to the left or
drink independently with a robotic arm after imagining reaching
for a cup.

However, major challenges remain in the translation of
long training
BCIs from the lab to the clinic—specifically,
times and variable user proficiency currently prevent the
widespread adoption of BCI technology. At least 20% of users
are unable to control typical BCIs proficiently even after

© The Author(s) 2020. Published by Oxford University Press. All rights reserved. For permissions, please e-mail: journals.permissions@oup.com

Mindfulness Improves Brain–Computer Interface Performance by ICONA in the AB

Stieger et al.

427

extensive training, while performance fluctuations prohibit
the safe use of robotic end effectors for daily activities
(Blankertz et al. 2010). Though the vast majority of recent work
has emphasized the development of decoding algorithms to
improve BCI control, a promising complementary approach
is to discover how individuals can be trained to interact with
the system more effectively (Guger et al. 2000; Edelman et al.
2016; Perdikis et al. 2018). How individuals learn to control a BCI
remains largely unknown; the paucity of research describing
the evolution of explicit learning metrics—such as brain signal
modulation—while the user gains control over the device
remains a major hindrance to the development of effective
training protocols (Perdikis et al. 2018).

Preliminary work has suggested mind–body awareness train-
ing (MBAT; e.g., yoga, meditation, etc.) may help to overcome
some of the challenges BCI users face—as experienced practi-
tioners demonstrate higher levels of BCI proficiency—however,
no research to date has generated a convincing explanation of
the underlying mechanisms of this influence (Cassady et al.
2014; Tan et al. 2014). In initial work from our lab, Cassady et al.
found those with 1 year or more of consistent MBATs were
able to more rapidly achieve greater levels of BCI proficiency
compared with controls. In this paradigm, participants began
with simple BCI tasks, then progressed to more complicated
tasks as proficiency was achieved (proficiency determined by an
accuracy greater than 80% for four consecutive runs or through-
out a given session; see description of left/right (LR), up/down
(UD), and 2D BCI tasks in Methods). Not only did MBAT prac-
titioners progress through each stage faster, a greater propor-
tion of proficient subjects was found in the MBAT group after
training. Cassady et al. additionally showed MBAT participants
demonstrated greater spectral power differences in EEG Mu
rhythm power between the motor (C3 and C4) electrodes used to
control the device. However, as participants progressed through
different stages of training at different times, only the initial
runs of the first task and session could be compared between
the two groups. Tan et al. was able to establish a more causal link
between MBAT and BCI performance by measuring one session
of BCI performance before and after a 12-week mindfulness
class, musical performance class, or waitlist condition. After
the intervention, a significant improvement in BCI accuracy
was found in the MBAT, but not in either the music or the
waitlist control groups. Since the electrodes, frequency bands,
and potentially motor imagery strategy used in the BCI task
could vary before and after the intervention, no electrophysi-
ological explanation was given for the accuracy improvements
reported. The prior work cited above highlights a lacuna in our
understanding—what happens in our brains as we “learn” to
control a BCI, and “how” does MBAT impact this process?

Current theories of neurofeedback learning indicate that
BCI control is achieved through the coordination of specific
distributed brain networks, such as the sensorimotor network
(SMN), fronto-parietal network (FPN), salience network (SN), and
default mode network (DMN) (Thomas Yeo et al. 2011; Ninaus
et al. 2013; Ramot et al. 2016; Sitaram et al. 2017). These networks
participate in different aspects of BCI performance such as
neurofeedback control (SMN, FPN), and neurofeedback reward
processing (SN, DMN) (Sitaram et al. 2017). Meditation practice
has consistently been shown to alter both the structural and
functional profiles of regions of interest within these networks,
however, how these alterations impact BCI performance is
currently speculative (Fox et al. 2014, 2016; Tang et al. 2015).
The reported increases in gray matter and neural activity

within the SMN and SN of expert meditators suggest MBAT
may facilitate motor imagery during BCI control by forging a
deeper mind–body connection (Fox et al. 2014, 2016; Jiang et al.
2020). MBAT could lead to improved performance through the
ability to direct and sustain attention to the BCI task by altering
structures of the FPN such as the dorsolateral prefrontal cortex,
or posterior parietal cortex (Tang et al. 2007; Hasenkamp et al.
2012; Wander et al. 2013). Alternatively, MBAT could aid BCI
control by reducing activity in the DMN, which has often been
linked to mind wandering (Raichle et al. 2001; Christoff et al.
2009). Finally, MBAT’s impact on the SN, and in particular the
anterior cingulate cortex and anterior insula, which influence
moment-to-moment alertness, awareness of
internal and
external states, and maintenance of task demands, may alter the
way neurofeedback reward is processed (Craig 2009; Brewer et al.
2011; Amiez et al. 2012; Hasenkamp et al. 2012; Ninaus et al. 2013;
Fox et al. 2014, 2016). While EEG does not allow the precise spatial
localization of the activity in these networks, it is ideally suited
to examine the oscillatory correlates of their communication.

Specifically, MBAT’s impact could result from meditation’s
effects on alpha band power. Energy at these frequencies
serves as the input to the decoding algorithms that control BCI
(Schalk et al. 2004). Additionally, meditation has been shown
to modulate specifically energy within this band. For example,
expert meditators display greater alpha power during rest, a
trait associated with greater BCI proficiency (Cahn and Polich
2006; Blankertz et al. 2010). Increases in alpha power have also
been observed following the recognition of mind wandering,
which mindfulness programs train individuals to monitor
and may additionally reflect a learned ability to inhibit task
irrelevant activity (Klimesch et al. 2007; Jensen and Mazaheri
2010; Braboszcz and Delorme 2011; Mathewson et al. 2011; Roux
and Uhlhaas 2014; Clayton et al. 2015; Rahl et al. 2017).

While intuitive conjectures arise from research claiming
MBAT enhances factors hypothesized to underlie BCI profi-
ciency, to our knowledge none have been formally tested. We
therefore designed and conducted a longitudinal BCI study to
test whether and how short-term MBAT affects the learning
and ultimate performance of SMR-based BCI control (Fig. 1A).
A major goal of this work was to discover the neural bases of
MBAT’s effects on SMR-based BCI performance. We predicted
MBAT would confer this advantage through enhancing the
capacity to: 1) direct attention to the BCI task, 2) generate
motor imagery, and/or 3)
intentionally modulate rhythmic
synchronization and desynchronization of neural activity
during motor imagery or rest. This rigorous examination of how
users learned to control the device and which aspects of this
process could be accelerated or enhanced by MBAT should lead
to better BCI training methods for larger populations of patients.

Materials and Methods

Experiment Design

During the BCI tasks, users attempted to steer a virtual cursor
from the center of the screen out to one of four targets (Fig. 1B).
Participants initially received the following instructions: “Imag-
ine your left (right) hand opening and closing to move the cursor
left (right). Imagine both hands opening and closing to move the
cursor up. Finally, to move the cursor down, voluntarily rest; in
other words, clear your mind.” In separate blocks of trials, partic-
ipants drove the cursor toward a target that required (LR) move-
ment only, UD only, and combined 2D movement (2D). Cursor

428

Cerebral Cortex, 2021, Vol. 31, No. 1

Figure 1. BCI training and control. (A) Experimentation timeline for BCI training.
Participants visited the lab for an initial assessment of BCI proficiency followed
by random assignment to either the MBSR course or an 8-week waitlist condi-
tion. After the intervention, BCI learning was assessed through a series of up
to 10 training sessions occurring three times per week. (B) BCI task. Following
a 2 s intertrial interval, a target appeared on the screen for 2 s indicating
where the cursor should be directed. During the feedback control period, the
participant was given up to 6 s to direct a cursor toward the correct target. The
cursor was controlled by changes in alpha power measured over bilateral motor
cortices. During lateralized motor imagery, reductions in alpha power (blue in
scalp images) are typically observed over the contralateral motor cortex, and
weaker increases in alpha power (yellow in scalp topographies) are observed
over the ipsilateral motor cortex. Bilateral motor imagery typically results in
bilateral desynchronization of alpha activity relative to rest. In this way, alpha
power asymmetry controlled lateral motion while the contrast between alpha
power during motor imagery and rest controlled vertical motion.

control was determined by the user’s ability to modulate the mu
rhythm—an EEG oscillation in the alpha band (8–12 Hz) recorded
over sensorimotor areas—such that alpha power asymmetry
governed lateral motion while the contrast between alpha power
during motor imagery and rest determined vertical motion (a
standard BCI approach) (Schalk et al. 2004; He et al. 2013).

Following an initial baseline assessment of BCI performance,
participants were randomly assigned to the mindfulness-based
stress reduction (MBSR) group or a waitlist control group,
respectively. The MBSR intervention seeks to teach mindfulness,
defined by MBSR’s founder Jon Kabat-Zinn as “awareness that
arises through paying attention, on purpose, in the present
moment, non-judgmentally” (Kabat-Zinn 1982). Following the 8-
week MBSR course, or comparable waiting period, participants
returned to the lab for 6–10 sessions of BCI training. Groups

(MBSR, n = 33, and control, n = 29) were compared across various
metrics of BCI performance and electrophysiological activity
throughout training. After completion of the last session, the
wait-list control subjects were provided with the opportunity
to join an MBSR class comparable with that provided to the
experimental subjects at a later date.

Participants

All participants provided written informed consent and the
study was approved by the Institutional Review Boards of the
University of Minnesota and Carnegie Mellon University. In total,
144 participants were enrolled in the study and 76 partici-
pants completed all experimental requirements. Seventy-two
participants were assigned to each intervention by block ran-
domization, with 42 participants completing all sessions in the
experimental group (MBSR before BCI training; MBSR subjects)
and 34 completing experimentation in the control group. Only
participants without (or with negligible) prior yoga or meditation
experience were included in our study.

Typical participant involvement required roughly 6 h/week
over the course of 4 months, which we believe accounted for
the high attrition rate. We note that the attrition rate may be
different in the much needed study of highly motivated clinical
patients struggling to be able to interact with the world again,
especially when guided by professional clinicians who have
experience running clinical trials (Chaudhary et al. 2016). No sig-
nificant differences were observed between groups (dropped vs.
completed/experimental vs. control) in terms of demographics
or initial BCI performance. A power analysis suggested a sample
size of 40 participants in each group to achieve a statistical
power of 0.9. The first group of participants (MBSR, n = 10;
control, n = 11) completed 6 BCI sessions, however, results indi-
cated learning was still taking place; thus, the experiment was
extended to 10 BCI session.

Four subjects were excluded from the analysis due to non-
compliance with the task demands and one was excluded due
to experimenter error. Further, to evaluate the learning of BCI
control, analysis focused on those that did not demonstrate
ceiling performance in the baseline BCI assessment (accuracy
above 90% in 1D control). The results describe data collected
from 33 MBSR subjects (Age = 42 ± 15, F = 26) and 29 controls
(Age = 36 ± 13, F = 23).

Mindfulness-based Stress Reduction

MBSR training consisted of a class that met weekly for 2.5–3 h
per class along with a 7.5 h silent retreat during the sixth week
of the class. Participants were also assigned home practice of 1 h
per day, 6 days per week. The content of the course was standard
for MBSR, and included “body scans” and breath-focused med-
itation. Class attendance was recorded and participants were
asked to use the Insight Timer (Insight Network, Inc.) to record
their home practice. MBSR participants recorded on average
21.52 ± 1.33 h of formal practice outside of class throughout the
course. Classes were taught by instructors of the University of
Minnesota Earl E. Bakken Center for Spirituality & Healing.

Measuring Mindfulness

A validated behavioral measure of mindfulness, breath counting
accuracy, was used to assess the effects of the MBSR intervention
(Levinson et al. 2014; Wong et al. 2018; Lim et al. 2018). In separate

Mindfulness Improves Brain–Computer Interface Performance by ICONA in the AB

Stieger et al.

429

18 min sessions before and after the intervention (as well as
BCI training), participants were asked to count their breaths
in cycles of nine (inhale and exhale counting as one), pressing
one button for the first eight breaths, and a second button for
the ninth (Levinson et al. 2014). Accuracy was quantified as the
number of correctly labeled breath cycles divided by the total
number of cycles. Breath counting accuracy was chosen as our
measure of mindfulness because skill in breath counting has
been found to be associated with self-reported mindfulness, less
mind-wandering, more meta-awareness, extent of meditation
practice, and distinct brain activity (Levinson et al. 2014; Lim
et al. 2018). The quantification of mindfulness is challenging and
though the absence of self-report questionnaires may be seen
as a limitation of this study, we believed the use of an objective
rather than subjective measure of mindfulness would produce
more reliable results.

BCI Cursor Control

BCI experiments were conducted using BCI2000, a general-
purpose software platform for BCI research (Schalk et al. 2004).
Each BCI session consisted of 6 runs (25 trials each; ∼3 min dura-
tion) of LR, UD, and 2D conditions for a total of 18 runs per day. As
sessions progressed, participants were encouraged to find their
own strategies. The control signal was extracted as different
combinations of the autoregressive (AR) spectral amplitudes of
the small Laplacian filtered electrodes C3 and C4 in a 3 Hz bin
surrounding 12 Hz normalized to zero mean and unit variance.
The magnitude of the cursor movement was determined by
the normalized AR amplitude difference, updated every 40 ms.
Horizontal motion was controlled by lateralized alpha power
(C4—C3) and vertical motion was controlled by up and down reg-
ulating total alpha power (C4 + C3). BCI accuracy was quantified
by a percent valid correct metric, calculated as the number of
hits divided by the total number of nontimeout trials (a timeout
occurred when the cursor did not contact a target within 6 s).

EEG Acquisition and Preprocessing

Participants wore a 64-channel EEG cap, which was set up
according to the international 10-10 system. EEG was acquired
using SynAmps RT amplifiers and Neuroscan acquisition
software (Compumedics Neuroscan). The scalp-recorded EEG
signals were digitized at 1000 Hz and filtered between 0.1 and
200 Hz with an additional notch filter at 60 Hz and stored
for offline analysis conducted using custom Matlab software
(R2018b, MathWorks Inc.) in conjunction with the EEGLAB (V.
14.1.1) and FieldTrip (revision 20190419) toolboxes (Delorme and
Makeig 2004; Oostenveld et al. 2011).

EEG data were first bandpass filtered between 1 and
100 Hz and downsampled to 250 Hz. Noisy channels with high
impedance were rejected by visual inspection and spherically
interpolated. The data were rereferenced to a common average.
Ocular artifacts were removed using independent component
analysis (ICA) and a template matching procedure. Runs were
broken into individual trials which included pre and post
intertrial intervals (2 s each), target presentation (2 s), and
feedback control periods (0.04–6 s), however, only trials with
feedback durations longer than 1 s were used for spectral
analysis (described below). Finally, trials with excessive EEG
variance were rejected on the basis of visual inspection. On
average, 84% [63 trials] ± 5.3% [4 trials] (mean ± SD) of the trials
of each type (ranging between 41% [31 trials] and 100% [76 trials])

were retained for analysis during each session. The number of
trials per type did not differ between groups.

Power Spectrum Analysis

Complex Morlet wavelet convolution was used to estimate the
power spectrum of the EEG signals. A family of wavelets was
created with 30 frequencies log spaced between 4 and 60 Hz with
cycles increasing from 3 cycles at 4 Hz to 10 cycles at 60 Hz. The
alpha band power was extracted by averaging a 3 Hz bin centered
at 12 Hz.

A Fisher discriminant score—calculated as the magnitude of
the mean difference in alpha power between trial types normal-
ized by the pooled standard deviation across trials—was used
to assess differences in spectral power during BCI operation
(Perdikis et al. 2018). In order to estimate the average strength
of the control signal during a given session, the Fisher score was
calculated based on the same combination of electrodes used
to control the BCI (described above). To obtain topographical
maps of alpha power discriminability between trial types, the
Fisher score was calculated separately for each electrode. Event-
related synchronization (ERS) is typically observed during rest
where populations of neurons synchronize their activity (which
leads to increases in alpha power) while event-related desyn-
chronization (ERD) is typically observed when motor neurons
are recruited during motor imagery (which leads to independen-
t/desynchronized computations and reductions in alpha power)
(Pfurtscheller and Lopes Da Silva 1999). Individual trial type ERD
was estimated by normalizing the alpha power during BCI opera-
tion by the alpha power during the 1 s preceding the trial. Finally,
changes in topological discriminability and ERD were calculated
by subtracting each subject’s baseline discriminability/ERD from
the average of their final 3 BCI sessions to provide a stable
estimate of neural activity during trained BCI operation.

Source Imaging

To image the underlying source of alpha activity, dynamic imag-
ing of coherent sources (DICS) was used to identify the spatial
source distributions (Gross et al. 2001). The leadfield matrix
was calculated using the Colin27 MNI template and boundary
element modeling (BEM) in the Fieldtrip toolbox using 3898
equally distributed grid points (8 mm uniform spacing) in the
gray matter. DICS spatial filters were constructed from the lead-
field matrix and a cross-spectral density matrix to maximize the
activity of interest at each specific grid point while suppressing
the contribution of all other grid points. The spatial distribution
of power was obtained by multiplying the spatial filters and
Fourier-transformed sensor level data. A source space Fisher
score was calculated by independently estimating alpha power
for each trial type then calculating the Fisher score (as above) at
each grid point.

Statistical Analysis

Linear mixed-effects models were fit using the lme4 package
in R (3.5.0) and P-values were computed with the
(1.1–21)
lmerTest package (3.1–0), using Satterthwaite approximation
for degrees of freedom (Bates et al. 2014; Kuznetsova et al.
2017). For between session comparisons of BCI performance, BCI
accuracy was modeled over time with fixed effects of session
(levels: 11), group (levels: MBSR, control), and task (levels: LR,
UD, 2D). Random effects included within subject factors of

430

Cerebral Cortex, 2021, Vol. 31, No. 1

session and task. The average BCI control signal over time was
modeled with fixed effects of session, levels, and task (levels:
LR, UD). Models were initially fit with three-way interactions
of group, task, and session. Fixed effects structures of the
mixed-effects models were reduced stepwise by excluding
nonsignificant
interaction terms/predictors and compared
using ANOVA ratio tests until the respectively smaller model
explained the data significantly worse than the larger model
(significant χ 2-test) (Kuznetsova et al. 2017). Cubic polynomial
contrasts were computed for the session factor, however,
only linear and quadratic terms (in addition to intercepts for
task) were used for the random effects. Residual plots were
examined for approximate normality and homoscedasticity.
Assumptions of normality and homoscedasticity were clearly
violated when attempting to fit the estimated BCI control signal
with cubic contrasts (presumably due to the large differences
in Fisher score between the LR and UD tasks [Fig. 3A,B]) thus
a two parameter box–cox transformation was applied to the
dependent variable of Fisher score instead.

A cluster-based permutation test (CBPT) statistic was used to
assess the group differences in the changes of Fisher discrim-
inant score recorded across the cortex during BCI training as
well as for all source analysis (Oostenveld et al. 2011). A similar
procedure was used for investigating the relationship between
source space rest ERS and meditation experience, except that
a t-transformation of the Pearson correlation was used as the
statistical metric.

Repeated measures ANOVAs were used to test group by
time interactions when data were found to be normally
distributed using the Shapiro–Wilks test. The breath counting
data displayed significant deviations from normality and were
fit with a rank-based analysis of linear models using the
Rfit package (0.23.0) as a robust alternative to least squares
(Kloke and McKean 2012). Significant findings were followed
by independent posthoc tests to aid inference. Nonparametric
tests were used when group data were found to be non-
Gaussian using the Shapiro–Wilks test. Confidence intervals and
Cohen’s d (difference in means/pooled standard deviation) were
calculated when the parametric tests’ assumptions were met.
All posthoc inferences were two-sided at a Holm–Bonferroni
corrected alpha level of 0.05 (0.025 per side). Outliers, defined as
three-scaled median absolute deviations away from the median,
were removed for posthoc statistical testing and are marked
with an x in all plots. Source imaging was used as a posthoc
inference to supplement the sensor level results and three
control subjects with outlying electrophysiological data were
removed for these plots and tests.

Results

MBSR Improves Mindfulness and BCI Control

The MBSR training was found to be effective, as indexed by
breath-counting accuracy—a validated behavioral measure
of mindfulness (Levinson et al. 2014). Using a rank based
interaction
ANOVA (see Methods: Statistics), a significant
= 4.92, P = 0.029;
was found between group and time (F1,60
Fig. 2A, Supplementary Table 1). Further analysis revealed
that, after the intervention, the MBSR group breath counting
accuracy was significantly greater than both their preinter-
= 11.8%,
vention levels (Wilcoxon Rank-Sum test (WRS): (cid:3)med
= 3.00,
IQRMBSR-Pre
P = 0.0027) and the postintervention levels of controls (WRS:

= 10.24%, Z(n1 = 32, n2 = 29)

= 15.60%, IQRMBSR-Post

(cid:3)med
Z(29,29)

= 15.40%, IQRMBSR-Post
= 4.14, P < 0.001).

= 10.24%, IQRcontrol-Post

= 15.18%,

Critically, the MBSR group showed greater improvements
in BCI performance than controls across training (Fig. 2B).
This effect was captured by a significant interaction between
the independent variables of session number and group
(MBSR and control) in a linear mixed-effects model for the
= 3.06, P = 0.003,
dependent variable of BCI accuracy (linear t184
= 3.26, P = 0.001, see
quadratic t1119
Supplementary Material: Statistical modeling; Supplementary
Table 2; Supplementary Fig. 1). The MBSR group displayed
significantly greater improvements in overall BCI performance
from baseline ((cid:3)μ = 8.98%, SDMBSR
= 15.96%,
= 2.32, P = 0.024, Cohen’s d = 0.59) suggesting
independent t60
MBSR had a positive influence on BCI training.

= −3.25, P = 0.001, cubic t1528

= 14.55%, SDcontrol

= 20.61%, Z(33,29)

= 11.94%, IQRMBSR

= 29.35%, IQRcontrol

To begin to probe how MBSR affected the BCI learning pro-
cess, performance change in individual BCI tasks was compared
between groups. The MBSR group displayed significantly greater
= 14.06%,
improvements in accuracy within the UD (WRS: (cid:3)med
= 2.24, P = 0.025)
IQRMBSR
=
and 2D (WRS: (cid:3)med
= 3.03, P = 0.002) tasks compared with controls,
15.18%, Z(33,26)
however, no significant differences were observed in the LR
= 15.88%,
task (WRS: (cid:3)med
= 1.06, P = 0.29). While greater improvements in BCI accu-
Z(33,29)
racy from baseline were observed in the MBSR group, the pro-
portion of participants reaching a proficiency criterion did not
differ between groups (see Supplementary Material: Proficiency
analysis).

= 10.24%, IQRcontrol

= 20.91%, IQRcontrol

= 8.89%, IQRMBSR

MBSR Enhances the Neural Contrast Between Motor
Imagery and Rest

We next examined the neural signals underlying BCI perfor-
mance using the Fisher score, which indexes the reliability of
signal differences between conditions (e.g., up vs. down in the
UD task; see Methods). MBSR participants exhibited a greater
ability to modulate their BCI-relevant EEG signals following
training for the UD, but not the LR task. A significant three-way
interaction was observed between group (MBSR and control),
task (LR and UD), and session when a mixed-effects model was
= 2.33, P = 0.02, see
fit to the Fisher score over time (Fig. 3A,B; t1028
Supplementary Material: Statistical modeling; Supplementary
Table 3; Supplementary Fig. 2).

= 0.38,

= 0.59,

independent t60

= 0.22, SDcontrol

Examining the change in estimated control signals in the
LR and UD tasks revealed that the differences in control signal
modulation arose from alpha power contrast between motor
imagery (up) and rest (down) (Fig. 3C; (cid:3)μ = 0.38, SDMBSR
= 0.65,
= 2.42, P = 0.018, Cohen’s
SDcontrol
d = 0.62) rather than motor imagery of
individual hands
((cid:3)μ = 0.017, SDMBSR
independent
= 0.22, P = 0.83, Cohen’s d = 0.058). Control analyses
t56
confirmed the difference in Fisher score was primarily driven
by the difference in mean alpha power rather than dif-
ference in variance (see Supplementary Material: Control
analysis—control signal components). These results were also
confirmed by examining the UD and LR components of the
2D task, which served as a replication of our results; see
Supplementary Material: 2D Analysis; Supplementary Figures
4–6. Because significant differences in the LR control signal
were not observed, subsequent analysis focused on the UD task
exclusively.

Mindfulness Improves Brain–Computer Interface Performance by ICONA in the AB

Stieger et al.

431

Figure 2. MBSR improves mindfulness and BCI control. (A) MBSR improves breath counting accuracy. A significant interaction was observed between group and time
suggesting MBSR affects breath counting accuracy (R-ANOVA P = 0.029). Following the intervention, MBSR participants displayed significantly greater breath counting
accuracies than their preintervention levels (WRS P = 0.0027) and the postintervention breath counting accuracies of controls (WRS P < 0.001). (B) The MBSR group
shows greater improvements in average BCI performance throughout training. A significant interaction was observed between group and session number suggesting
MBSR affects the learning of BCI control (mixed effects model, linear: P = 0.003, quadratic: P = 0.001, cubic: P = 0.001). (C) Significant improvements from baseline were
observed in the UD (WRS, P = 0.025) and 2D (WRS, P = 0.002) tasks suggesting the observed interaction resulted from MBSR improving the learning of BCI control. Violin
plots (A,C): shaded area represents kernel density estimate of the data, white circles represent the median, and gray bars represent the interquartile range. Line plots
(B): shaded area represents ±1 standard error of the mean (SEM).

Figure 3. MBSR increases the contrast between motor imagery and rest. (A) Change in estimated control signal modulation in the LR task during training. (B) Change
in control signal modulation in the UD task during training. A significant three-way interaction was observed between group, session number, and task suggesting
MBSR changes how the control signal is modulated throughout training (mixed effects model, P = 0.02). (C) A significant difference in control signal modulation was
observed in the UD (independent t test, P = 0.019), but not the LR task, suggesting the role MBSR plays in BCI training is by changing the contrast between alpha power
during motor imagery and rest. Line plots: Shaded area represents ± 1 SEM. Violin plots: shaded area represents kernel density estimate of the data, white circles
represent the median, and gray bars represent the interquartile range.

Chiefly, MBSR-trained participants learned to dramatically
alter both the amplitude and the spatial pattern of their
alpha power during BCI control (Fig. 4A). CBPTs (see Methods:
Statistics) revealed that changes in Fisher scores from baseline
were significantly greater for MBSR participants than controls
in the UD task across a wide range of electrodes including those
over frontal, midline, posterior, and motor areas (Fig. 4B; sensor
space—cluster stat [maxsum (t60)] = 110.0, P = 0.010; Fig. 4C;
source space—cluster stat [maxsum (t57)] = 6.67 × 103, P = 0.0001

see Supplementary Fig. 3 for Fisher score evolution across time
for LR vs. UD comparison).

Mindfulness Facilitates Alpha Power Up-regulation
During Volitional Rest
MBSR specifically led to increased alpha power up-regulation
during rest trials. We separated trials into those controlled by
motor imagery (up) and those controlled by resting (down) to

432

Cerebral Cortex, 2021, Vol. 31, No. 1

Figure 4. Alpha power contrast between motor imagery and rest is widespread. (A) The Fisher score was used to plot the difference between the distributions of alpha
power during motor imagery versus rest at each electrode throughout training (x-axis = session number). During the UD task, the control group (top row) displayed
the expected pattern in that the difference between motor imagery and rest is determined by the presence or absence of activity over the motor cortex. However, the
MBSR group produced an entirely different pattern of contrast that evolves throughout training. Brighter colors represent greater differences in alpha power between
trial types. (B) Comparing the change in Fisher score across the cortex during UD control revealed the MBSR group learned to generate greater alpha power contrast
between motor imagery and rest than controls across a wide range of electrodes (CBPT, P = 0.01). (C) Source imaging of the group difference in Fisher score change
during the UD task again confirms the differences in learned alpha power modulation are widespread (CBPT, P < 0.001).

determine which strategy contributed most to the observed
results. The ability to modulate spectral power in the alpha
band was calculated separately for each trial type by averaging
alpha power during BCI operation and normalizing by the
alpha power observed during the intertrial interval to estimate
ERD (reductions in alpha power) or ERS (increases in alpha
power). Power was averaged across the electrodes belonging
to the significant cluster identified by the CBPT (Fig. 4B). A
repeated measures ANOVA found a significant interaction
between trial type and group when modeling change in ERS
= 6.70, P = 0.012; Fig. 5A, Supplementary
from baseline (F1,60
Table 4). While no differences in alpha power modulation
were found during motor imagery between MBSR subjects and
controls ((cid:3)μ = −0.014 dB, SDMBSR
= 1.17 dB,
= −0.51, P = 0.61, Cohen’s d = −0.14), a
t56
independent
significant difference in the training-related increases in alpha
power ERS was observed between groups during the rest trials
((cid:3)μ = 1.37 dB, SDMBSR
= 1.56 dB, independent
= 2.32 dB, SDcontrol
= 2.61, P = 0.011, Cohen’s d = 0.68). Control analyses found
t58
no difference in passive resting state alpha power between the
MBSR and control group indicating the reported differences
in learned alpha ERS result from the MBSR subjects’ ability to
“intentionally up-regulate” alpha power “above and beyond”
the passive resting state during rest trials (see Supplementary
Material: Control analysis—resting state power).

= 0.92 dB, SDcontrol

Source imaging revealed that the greatest difference between
MBSR and control participants in the learned enhancement
of alpha ERS during rest could be localized to roughly the
same structures as the difference in Fisher score, suggesting
the increase in alpha activity during rest was driving the
(Fig. 5B; cluster stat (maxsum
improvement in BCI control
(t57)) = 5.52 × 103, P = 0.0055).

The learned ability to modulate alpha power during rest
displayed a dose-dependent relationship with at home medi-
tation practice and correlated with breath counting accuracy,
suggesting both arise from a common MBSR ability. Further, this
ability was found to predict final BCI performance indicating the
contribution this skill plays in BCI control. We quantified the
strength of association between alpha ERS within the identified
cluster in Figure 4B during BCI control and various behavioral
variables. The change in alpha ERS power from baseline dur-
ing rest trials was found to be significantly correlated with
the hours of meditation practiced outside of the MBSR class
= 0.43, P = 0.012). Source imaging also suggested
(Fig. 5C; r33
meditation practice is related to increases in alpha ERS with
the strongest associations found in frontal, left temporal, and
parietal areas (Fig. 5D; cluster stat (maxsum (t33)) = 2.29 × 103,
P = 0.028). Finally, alpha ERS was found to correlate significantly
with both ultimate BCI performance in the UD task (Fig. 6A;
= 0.51, P = 0.0027) as well as post BCI training breath counting
r32
= 0.41, P = 0.028). Collectively, these results
accuracy (Fig. 6B; r31
suggest that the ability to up-regulate alpha power during voli-
tional rest is related to mindfulness practice, results in better BCI
control, and facilitates the ability to notice when the mind has
wandered.

Discussion

Our work demonstrates that important aspects of BCI training
can be enhanced through a behavioral intervention (Vansteensel
et al. 2016; Perdikis et al. 2018). We further identified the spe-
cific neural bases of the improvement in performance: Sub-
jects trained in mindfulness were able to produce strikingly
different patterns of alpha activity when the BCI task required
volitional rest.

Mindfulness Improves Brain–Computer Interface Performance by ICONA in the AB

Stieger et al.

433

Figure 5. Localizing effects to rest. (A) Averaging over the significant electrodes in Figure 4B reveals the alpha power contrast between motor imagery and rest primarily
results due to the learned ability to increase alpha ERS during rest trials (independent t-test P = 0.011). (B) The significant difference in the learned ability to synchronize
alpha oscillations during rest covers roughly the same areas identified by the group difference in Fisher score in the source domain (CBPT, P = 0.0055). (C) The training
related increases in alpha ERS during rest displayed a dose-dependent response with meditation practice suggesting more at home meditation practice led to greater
changes in alpha ERS during BCI control (Pearson correlation, P = 0.012). (D) Source imaging suggested meditation practice is most strongly associated with greater
alpha ERS increases in frontal, temporal, and parietal areas (CBPT, P = 0.028).

This ability to up-regulate alpha band activity is function-
ally significant, as it has dose-dependent effects, predicts BCI
performance, and is related to accuracy in a breath count-
ing task. Future work incorporating the identified mindfulness-
based alpha pattern into the BCI decoder or combining mind-
fulness training with other interventions specifically targeting
the SMR could lead to even larger increases in accuracy, steeper
learning curves, and more consistent performance for many
different BCI training protocols.

We initially predicted MBAT would exert its effects through
augmenting the ability to sustain attention, generate motor
imagery, and/or
influence brain rhythms; we found the
strongest evidence for the latter. Increases in alpha band power
have been commonly reported when comparing meditators
and controls during both rest and meditation (Cahn and Polich
2006; Lee et al. 2018). Thus, prior research might predict the
MBSR intervention simply taught participants to passively “rest
better” by shifting baseline resting-state alpha power relative
to controls (Blankertz et al. 2010). However, no differences in

passive rest alpha power were observed between the groups
after the intervention, nor throughout training. Rather, MBSR
subjects demonstrated the ability to actively increase their
alpha power while attempting to control the cursor during
intentional rest.

This skill was not acquired directly from MBAT; that is, differ-
ences were not evident in the first session after MBAT training,
but instead were amplified throughout BCI training. Participants
may have learned gradually to apply a skill they acquired from
MBAT to help BCI performance, as this capacity was related to
the amount of time invested in meditation practice outside of
the class. This suggests that further practice could potentially
lead to further gains in alpha ERS during BCI control (Cahn and
Polich 2006; Hasenkamp et al. 2012; Saggar et al. 2012; Lee et al.
2018).

Our findings agree with prior work documenting experienced
meditators’ ability to up-regulate alpha band power during med-
itation, however, the nature of alpha oscillations during medita-
tion remains a mystery (Cahn and Polich 2006; Brandmeyer and

434

Cerebral Cortex, 2021, Vol. 31, No. 1

Figure 6. Rest trial alpha up-regulation predicts behavioral performance. Averaging over the significant electrodes in Figure 4B demonstrates that alpha power up-
regulation in the MBSR group correlates significantly with both A, ultimate UD BCI accuracy (Pearson correlation, P = 0.0027) and B, post BCI training breath counting
accuracy (Pearson correlation, P = 0.028).

Delorme 2018; Lee et al. 2018). Research claiming that the recog-
nition of mind wandering is associated with increases in alpha
power and activation of the salience network (which in turn
has been linked to alpha power) suggest alpha rhythms play an
integral role in the “letting go” of spontaneous thought (Sadaghi-
ani et al. 2010; Braboszcz and Delorme 2011; Hasenkamp et al.
2012; Ellamil et al. 2016; Sadaghiani and Kleinschmidt 2016).
In fact, reductions in neural noise, such as mind-wandering,
are generally cited to explain why experienced mindfulness
practitioners display enhanced abilities on tasks that probe
attention (Lutz et al. 2009; Slagter et al. 2009; MacLean et al.
2010; Schoenberg et al. 2014; Colzato et al. 2015; Fox et al. 2016;
Ziegler et al. 2019). The significant difference in the ability to
follow the breath between the experimental and control groups
subsequent to the MBSR intervention confirms previous reports
that mindfulness is associated with in mind wandering and the
significant correlation between the ability to up-regulate alpha
power during BCI control and breath counting accuracy suggests
the MBSR participants may be engaging in meditative practices
during the volitional rest trials of BCI control (Mrazek et al. 2012;
Levinson et al. 2014; Rahl et al. 2017).

The literature on alpha’s role in facilitating effective neural
communication through the periodic inhibition of task irrel-
evant information agrees with the previous claim (Palva and
Palva 2007; Jensen and Mazaheri 2010; Mathewson et al. 2011;
Jensen et al. 2014; Sadaghiani and Kleinschmidt 2016; Miller et al.
2018; Chapeton et al. 2019). Our study found that the strongest
relationship between meditation practice and increases in alpha
power during BCI control could be localized to the prefrontal,
left temporal, and parietal components of the DMN—which
has been extensively linked to mind wandering (Eichele et al.
2008; Christoff et al. 2009; Hasenkamp et al. 2012; Fox et al.
2015; Ellamil et al. 2016). Mind wandering can be seen as an
occupier of mental bandwidth, such that if participants are more
engaged with their internal narrative, less neural resources are
available for the task at hand. Efficient neural communication
likely occurs when the minimal sets of relevant processes are
able to interact; the alpha rhythm’s ability to act as a “windshield
wiper,” periodically removing unnecessary neural signals, may

allow it to open an information channel that would otherwise
be clogged by distracting thoughts, and improve communication
between task-relevant signals (Sadaghiani and Kleinschmidt
2016). Therefore, the view of alpha oscillations as pulsed inhi-
bition paired with significant improvements in the ability to
return attention to the breath might indicate MBAT reduces
mind wandering through stronger periodic gating of the DMN
(Jensen and Mazaheri 2010; Mathewson et al. 2011; Brickwedde
et al. 2019). However, what remains unclear is which facet of
the cycling recognition of mind wandering, dissolving of spon-
taneous thought, and subsequently renewed presence causes or
is caused by increased alpha power.

One limitation of our study design was the lack of an active
control group. While the inclusion of an active control condition
would have improved the rigor of our study, the work from Tan
et al. found expectations and the inclusion of an active control
condition (guitar lessons) had no impact on BCI performance
(Tan et al. 2014). It may be the case that active control designs
matter less when the complexity of attempting to control brain
activity baffles the most astute of us, however, this point may
demonstrate the need for better actively controlled interven-
tions that require the same mental commitment of time or
intensity as meditation practice (Goleman and Davidson 2017).
A further limitation may be the exclusive use of the breath
counting task as our sole measure of mindfulness. The breath
counting task is recommended as a standardized measure of
mindfulness to be used in addition to self-report questionnaires;
therefore, future work may be needed to discover whether BCI
performance can be predicted by self-reported levels of mind-
fulness (Wong et al. 2018).

Another limitation of the current work may be that MBAT did
not appear to improve BCI control in general. If the significant
increases in breath counting accuracy represent improvements
in the ability to refocus attention when the mind has wandered,
as we suggest, improvements across all domains of BCI control
would be expected; however, no significant differences in elec-
trophysiological activity were observed between the groups in
the motor imagery task conditions. Alterations in the structure

Mindfulness Improves Brain–Computer Interface Performance by ICONA in the AB

Stieger et al.

435

and function of sensorimotor cortex might require more medi-
tation experience to develop (Fox et al. 2014, 2016). Alternatively,
cuing the rest condition could promote mini-meditations lead-
ing to reduced mind wandering only during rest trials where
transfer learning would be expected to be strongest (Mrazek
et al. 2012; Rahl et al. 2017).

Though the rate of BCI proficiency (Combrisson and Jerbi
2015) did not differ between the groups in our study, we did
observe significantly greater improvements in performance
from baseline suggesting mindfulness training does not combat
the BCI proficiency problem (Blankertz et al. 2010), but rather
extends the innate capacities of the user—that is, short-term
MBAT may not directly impact the ability to perform motor
imagery, but rather create a more favorable baseline to which the
motor imagery can be compared. This finding could additionally
be complicated by the fact that a very low proportion of the
subjects in our study failed to attain a level of control considered
proficient in any paradigm. We believe this is due to the diverse
control options provided to the participant, echoing the call for
individualized neurofeedback protocols (Alkoby et al. 2018).

The alpha increase that we observed was widespread across
the cortex. Alpha oscillations are traveling waves in the human
neocortex, therefore, the trial averaging employed in this anal-
ysis might obscure various metastable brain states that occur
during BCI control (Zhang et al. 2018; Lozano-Soldevilla and
VanRullen 2019; Roberts et al. 2019). In fact, a recent resting-state
MEG study was able to decompose the DMN into anterior and
posterior subcomponents which were active at different points
in time (Vidaurre et al. 2018). Whether the increased alpha power
over the motor cortex results from radiating alpha sources or
traveling waves within or between disparate metastable brain
states is as yet unknown (Vidaurre et al. 2018; Zhang et al.
2018; Roberts et al. 2019). Additionally, those with greater breath
counting skill display more frequent transitions from an “idling
network” to a “task-ready network” (Lim et al. 2018). Discovering
whether more alpha power is present during these transitions
may be a promising avenue of exploration. Regardless, since
1) most continuous BCI paradigms utilize rest as a state to be
detected and 2) the decoder incorporates brain activity from
both rest and motor imagery conditions in its decisions (i.e.,
there are not separate classifiers for rest and motor imagery),
changing brain activity in one task improves classification of
both conditions (evinced by the significant improvements in
both 1D and 2D BCI control) (Perdikis et al. 2018; Edelman et al.
2019). Future work identifying the specific components of MBSR
that aid in this process could lead to easier, targeted training.

Whether noninvasive signals such as scalp EEG contain suf-
ficient information to allow the decoding of complex movement
commands generated by the brain remains a topic of debate.
Simple movement of computer cursors endures as the dominant
SMR BCI paradigm, while the decoding algorithm utilized in
this study (C3/C4 alpha power)—and implemented by BCI2000—
further dates this work (Schalk et al. 2004). However, studies
from our lab and others demonstrate that the decoding of more
complex motor imaginations through source imaging (Edelman
et al. 2016), navigation of wheelchairs (Rebsamen et al. 2010) and
continuous robotic arm control (Edelman et al. 2019) are possible
through EEG. The current work additionally provides insight into
the neural basis of learning such control, as well as demon-
strates the effects of MBAT upon this process (Vansteensel et al.
2016; Perdikis et al. 2018). Whether the impact of mindfulness
practice can be better detected by more sophisticated machine
learning techniques such as common spatial patterns (Guger

et al. 2000; Ang et al. 2008; Blankertz et al. 2008; Lotte and Guan
2011), or whether the widespread alpha increases engendered by
MBAT are only applicable within this limited domain remains
unclear. In the present study, we have focused on evaluating
how BCI performance differs between those attending an MBSR
intervention and a waitlisted control group in a simple, yet
identical, processing pipeline in order to address the question
of whether mindfulness would have an impact on BCI learning
and performance. It is anticipated that, while detailed aspects
of results may differ, the differences in performance we have
observed between the MBSR and control groups should remain.
Future investigations could test whether the differing patterns
of brain activity observed between the MBSR and control groups
in our study remain stable or change with varying neurofeed-
back protocols as more sophisticated algorithms are used.

In conclusion, MBAT gives users of BCI the ability to learn to
increase alpha power across the cortex on demand during rest.
Future work detecting this mindfulness-related alpha signal
through techniques such as common spatial patterns could
lead to added improvements in BCI control, as well as novel
neurofeedback paradigms (Guger et al. 2000; Ang et al. 2008;
Lotte and Guan 2011; van Lutterveld et al. 2017). Interventions or
methods that specifically target SMRs such as noninvasive brain
stimulation could additionally complement the performance
gains reported in this study (Soekadar et al. 2015; Baxter et al.
2016; Kraus et al. 2016). Future work studying the ability of
MBAT to promote the volitional up-regulation of alpha band
power could further illuminate the role alpha oscillations play
in neural communication and deepen our understanding of the
neural correlates of attention, mind-wandering, and letting go
of conscious thought.

Supplementary Material

Supplementary material can be found at Cerebral Cortex online.

Notes

We would like to thank the following colleagues for their assis-
tance in subject recruiting, data collection and analysis: Bhavani
Sai Rohit Murakonda, Chris Coogan, Andy Huynh, Samantha
Sherman, Alyssa Everson, Marisa Sanchez, Carter Ibister, James
Kerber, Angeliki Beyko, Desirae Hammond, Kit Breshears, Taylor
Boyle. Conflict of Interests: None declared.

Funding

National
EB021027, NS096761, EB008389).

Institutes of Health (grants AT009263, MH114233,

Author Contributions

B.H., S.E., J.R.S., and C.C.C. designed the experiments. J.R.S. and
C.C.C. collected the data. J.R.S. and H.J. analyzed the data. M.J.K.
corecruited subjects and helped facilitate the MBSR classes.
J.R.S., S.E., C.C.C., and B.H. wrote the paper. All authors discussed
the results and contributed to editing the manuscript.

References

Alkoby O, Abu-Rmileh A, Shriki O, Todder D. 2018. Can we
predict who will respond to neurofeedback? A review of the

436

Cerebral Cortex, 2021, Vol. 31, No. 1

inefficacy problem and existing predictors for successful EEG
neurofeedback learning. Neuroscience. 378:155–164.

Amiez C, Sallet J, Procyk E, Petrides M. 2012. Modulation of feed-
back related activity in the rostral anterior cingulate cortex
during trial and error exploration. Neuroimage. 63:1078–1090.
Ang KK, Chin ZY, Zhang H, Guan C. 2008. Filter Bank Common
Spatial Pattern (FBCSP) in brain-computer interface. In: Pro-
ceedings of the International Joint Conference on Neural Networks.
p. 2390–2397.

Bates D, Mächler M, Bolker B, Walker S. 2014. Fitting linear mixed-

effects models using lme4. J Stat Softw. 67:1–48.

Baxter BS, Edelman BJ, Nesbitt N, He B. 2016. Sensorimotor
rhythm BCI with simultaneous high definition-transcranial
direct current stimulation alters task performance. Brain
Stimul. 9:834–841.

Blankertz B, Sannelli C, Halder S, Hammer EM, Kübler A, Müller
K-R, Curio G, Dickhaus T. 2010. Neurophysiological predictor
of SMR-based BCI performance. Neuroimage. 51:1303–1309.
Blankertz B, Tomioka R, Lemm S, Kawanabe M, Müller KR. 2008.
Optimizing spatial filters for robust EEG single-trial analysis.
IEEE Signal Process Mag. 25:41–56.

Braboszcz C, Delorme A. 2011. Lost in thoughts: neural mark-
ers of low alertness during mind wandering. Neuroimage.
54:3040–3047.

Brandmeyer T, Delorme A. 2018. Reduced mind wandering in
experienced meditators and associated EEG correlates. Exp
Brain Res. 236:2519–2528.

Brewer JA, Worhunsky PD, Gray JR, Tang Y-Y, Weber J, Kober H.
2011. Meditation experience is associated with differences
in default mode network activity and connectivity. Proc Natl
Acad Sci. 108:20254–20259.

Brickwedde M, Krüger MC, Dinse HR. 2019. Somatosensory alpha
oscillations gate perceptual learning efficiency. Nat Commun.
10:263.

Cahn BR, Polich J. 2006. Meditation states and traits: EEG, ERP, and

neuroimaging studies. Psychol Bull. 132:180–211.

Delorme A, Makeig S. 2004. EEGLAB: an open source toolbox for
analysis of single-trial EEG dynamics including independent
component analysis. J Neurosci Methods. 134:9–21.

Edelman BJ, Baxter B, He B. 2016. EEG source imaging enhances
the decoding of complex right-hand motor imagery tasks.
IEEE Trans Biomed Eng. 63:4–14.

Edelman BJ, Meng J, Suma D, Zurn C, Nagarajan E, Baxter BS,
Cline CC, He B. 2019. Noninvasive neuroimaging enhances
continuous neural tracking for robotic device control. Sci
Robot. 4:1–13.

Eichele T, Debener S, Calhoun VD, Specht K, Engel AK, Hugdahl
K, Yves Von Cramon D, Ullsperger M. 2008. Prediction of
human errors by maladaptive changes in event-related brain
networks. Proc Natl Acad Sci USA. 105:6173–6178.

Ellamil M, Fox KCR, Dixon ML, Pritchard S, Todd RM, Thompson
E, Christoff K. 2016. Dynamics of neural recruitment sur-
rounding the spontaneous arising of thoughts in experienced
mindfulness practitioners. Neuroimage. 136:186–196.

Wong KF, Massar SAA, Chee MWL, Lim J. 2018. Towards an
objective measure of mindfulness: replicating and extending
the features of the breath-counting task. Mindfulness (NY).
9:1402–1410.

Fox KCR, Dixon ML, Nijeboer S, Girn M, Floman JL, Lifshitz M,
Ellamil M, Sedlmeier P, Christoff K. 2016. Functional neu-
roanatomy of meditation: a review and meta-analysis of
78 functional neuroimaging investigations. Neurosci Biobehav
Rev. 65:208–228.

Fox KCR, Nijeboer S, Dixon ML, Floman JL, Ellamil M, Rumak
SP, Sedlmeier P, Christoff K. 2014. Is meditation associated
with altered brain structure? A systematic review and meta-
analysis of morphometric neuroimaging in meditation prac-
titioners. Neurosci Biobehav Rev. 43:48–73.

Fox KCR, Spreng RN, Ellamil M, Andrews-Hanna JR, Christoff
K. 2015. The wandering brain: meta-analysis of functional
neuroimaging studies of mind-wandering and related spon-
taneous thought processes. Neuroimage. 111:611–621.

Cassady K, You A, Doud A, He B. 2014. The impact of mind-body
awareness training on the early learning of a brain-computer
interface. Dent Tech. 2:254–260.

Goleman D, Davidson RJ. 2017. Altered traits: science reveals how
meditation changes your mind, brain, and body. 1st ed. New York:
Avery, p. 90.

Chapeton JI, Haque R, Wittig JH, Inati SK, Zaghloul KA. 2019.
Large-scale communication in the human brain is rhythmi-
cally modulated through alpha coherence. Curr Biol. 29:2801–
2811.e5.

Gross J, Kujala J, Hämäläinen M, Timmermann L, Schnitzler
A, Salmelin R. 2001. Dynamic imaging of coherent sources:
studying neural interactions in the human brain. Proc Natl
Acad Sci. 98:694–699.

Chaudhary U, Birbaumer N, Ramos-Murguialday A. 2016. Brain-
computer interfaces for communication and rehabilitation.
Nat Rev Neurol. (9):513–525.

Christoff K, Gordon AM, Smallwood J, Smith R, Schooler JW. 2009.
Experience sampling during fMRI reveals default network
and executive system contributions to mind wandering. Proc
Natl Acad Sci USA. 106:8719–8724.

Clayton MS, Yeung N, Cohen Kadosh R. 2015. The roles of cortical
oscillations in sustained attention. Trends Cogn Sci. 9:188–195.
Colzato LS, Sellaro R, Samara I, Baas M, Hommel B. 2015.
Meditation-induced states predict attentional control over
time. Conscious Cogn. 37:57–62.

Combrisson E, Jerbi K. 2015. Exceeding chance level by chance:
the caveat of theoretical chance levels in brain signal clas-
sification and statistical assessment of decoding accuracy. J
Neurosci Methods. 250:126–136.

Craig AD. 2009. How do you feel—now? The anterior insula and

human awareness. Nat Rev Neurosci. 10:59–70.

Guger C, Ramoser H, Pfurtscheller G. 2000. Real-time EEG
analysis with subject-specific spatial patterns for a brain-
computer interface (BCI). IEEE Trans Rehabil Eng. 8:447–456.
Hasenkamp W, Wilson-Mendenhall CD, Duncan E, Barsalou
LW. 2012. Mind wandering and attention during focused
meditation: a fine-grained temporal analysis of fluctuating
cognitive states. Neuroimage. 59:750–760.

He B, Gao S, Yuan H, Wolpaw JR. 2013. Brain–computer interfaces.
In: He B, editor. Neural engineering. 2nd ed. New York: Springer,
pp. 87–151.

Jensen O, Gips B, Bergmann TO, Bonnefond M. 2014. Temporal
coding organized by coupled alpha and gamma oscillations
prioritize visual processing. Trends Neurosci. 37:357–369.
Jensen O, Mazaheri A. 2010. Shaping functional architecture
by oscillatory alpha activity: gating by inhibition. Front Hum
Neurosci. 4:186.

Jiang H, He B, Guo X, Wang X, Guo M, Wang Z, Xue T, Li H,
Xu T, Ye S et al. 2020. Brain-heart interactions underlying
traditional Tibetan Buddhist meditation. Cereb Cortex. 30:
439–450.

Mindfulness Improves Brain–Computer Interface Performance by ICONA in the AB

Stieger et al.

437

Kabat-Zinn J. 1982. An outpatient program in behavioral
medicine for chronic pain patients based on the practice
of mindfulness meditation: theoretical considerations and
preliminary results. Gen Hosp Psychiatry. 4:33–47.

Perdikis S, Tonin L, Saeedi S, Schneider C, Millán J del R. 2018. The
Cybathlon BCI race: successful longitudinal mutual learn-
ing with two tetraplegic users. PLoS Biol. e2003787:16. doi:
10.1371/journal.pbio.200.

Klimesch W, Sauseng P, Hanslmayr S. 2007. EEG alpha oscil-
lations: the inhibition-timing hypothesis. Brain Res Rev.
53:63–88.

Pfurtscheller G, Lopes Da Silva FH. 1999. Event-related EEG/MEG
synchronization and desynchronization: basic principles.
Clin Neurophysiol. 110:1842–1857.

Kloke JD, McKean JW. 2012. Rfit: rank-based estimation for linear

Pfurtscheller G, Neuper C. 2001. Motor imagery and direct brain-

models. R I Dent J. 4:57–64.

Kraus D, Naros G, Bauer R, Khademi F, Leão MT, Ziemann U,
Gharabaghi A. 2016. Brain state-dependent transcranial mag-
netic closed-loop stimulation controlled by sensorimotor
desynchronization induces robust increase of corticospinal
excitability. Brain Stimul. 9:415–424.

Kuznetsova A, Brockhoff PB, Christensen RHB. 2017. lmerTest
package: tests in linear mixed effects models. J Stat Softw.
82:1–26.

Lafleur K, Cassady K, Doud A, Shades K, Rogin E, He B. 2013.
Quadcopter control in three-dimensional space using a non-
invasive motor imagery-based brain–computer interface. J
Neural Eng. 10:46003–46015.

Lee DJ, Kulubya E, Goldin P, Goodarzi A, Girgis F. 2018. Review of
the neural oscillations underlying meditation. Front Neurosci.
12:1–7.

Levinson DB, Stoll EL, Kindy SD, Merry HL, Davidson RJ. 2014.
A mind you can count on: validating breath counting as a
behavioral measure of mindfulness. Front Psychol. 5:1202.
Lim J, Teng J, Patanaik A, Tandi J, Massar SAA. 2018. Dynamic
functional connectivity markers of objective trait mindful-
ness. Neuroimage. 176:193–202.

Lotte F, Guan C. 2011. Regularizing common spatial patterns to
improve BCI designs: unified theory and new algorithms. IEEE
Trans Biomed Eng. 58:355–362.

Lozano-Soldevilla D, VanRullen R. 2019. The hidden spatial
dimension of alpha: 10-Hz perceptual echoes propagate as
periodic traveling waves in the human brain. Cell Rep. 26:374–
380.e4.

Lutz A, Slagter HA, Rawlings NB, Francis AD, Greischar LL, David-
son RJ. 2009. Mental training enhances attentional stability:
neural and behavioral evidence. J Neurosci. 29:13418–13427.
MacLean KA, Ferrer E, Aichele SR, Bridwell DA, Zanesco AP,
Jacobs TL, King BG, Rosenberg EL, Sahdra BK, Shaver PR et al.
2010. Intensive meditation training improves perceptual dis-
crimination and sustained attention. Psychol Sci. 21:829–839.
Mathewson K, Lleras A, Beck D, Fabiani M, Ro T, Gratton G.
2011. Pulsed out of awareness: EEG alpha oscillations repre-
sent a pulsed-inhibition of ongoing cortical processing. Front
Psychol. 2:99.

Miller EK, Lundqvist M, Bastos AM. 2018. Working memory 2.0.

Neuron. 100:463–475.

Mrazek MD, Smallwood J, Schooler JW. 2012. Mindfulness and
mind-wandering: finding convergence through opposing
constructs. Emotion. 12:442–448.

Ninaus M, Kober SE, Witte M, Koschutnig K, Stangl M, Neu-
per C, Wood G. 2013. Neural substrates of cognitive control
under the belief of getting neurofeedback training. Front Hum
Neurosci. 7:914.

Oostenveld R, Fries P, Maris E, Schoffelen JM. 2011. FieldTrip:
open source software for advanced analysis of MEG, EEG,
and invasive electrophysiological data. Comput Intell Neurosci.
2011:156869.

Palva S, Palva JM. 2007. New vistas for α-frequency band oscilla-

tions. Trends Neurosci. 30:150–158.

computer communication. Proc IEEE. 89:1123–1134.

Rahl HA, Lindsay EK, Pacilio LE, Brown KW, David Creswell J. 2017.
Brief mindfulness meditation training reduces mind wander-
ing: the critical role of acceptance. Emotion. 17:224–230.

Raichle ME, MacLeod AM, Snyder AZ, Powers WJ, Gusnard DA,
Shulman GL. 2001. A default mode of brain function. Proc Natl
Acad Sci. 98:676–682.

Ramot M, Grossman S, Friedman D, Malach R. 2016. Covert neu-
rofeedback without awareness shapes cortical network spon-
taneous connectivity. Proc Natl Acad Sci. 113:E2413–E2420.
Rebsamen B, Guan C, Zhang H, Wang C, Teo C, Ang MH, Bur-
det E. 2010. A brain controlled wheelchair to navigate in
familiar environments. IEEE Trans Neural Syst Rehabil Eng. 18:
590–598.

Roberts JA, Gollo LL, Abeysuriya RG, Roberts G, Mitchell PB,
Woolrich MW, Breakspear M. 2019. Metastable brain waves.
Nat Commun. 10:1–17.

Roux F, Uhlhaas PJ. 2014. Working memory and neural oscilla-
tions: alpha-gamma versus theta-gamma codes for distinct
WM information? Trends Cogn Sci. 18:16–25.

Sadaghiani S, Kleinschmidt A. 2016. Brain networks and α-
oscillations: structural and functional foundations of cogni-
tive control. Trends Cogn Sci. 20:805–817.

Sadaghiani S, Scheeringa R, Lehongre K, Morillon B, Giraud
A-L, Kleinschmidt A. 2010. Intrinsic connectivity networks,
alpha oscillations, and tonic alertness: a simultaneous elec-
troencephalography/functional magnetic resonance imaging
study. J Neurosci. 30:10243–10250.

Saggar M, King BG, Zanesco AP, MacLean KA, Aichele SR, Jacobs
TL, Bridwell DA, Shaver PR, Rosenberg EL, Sahdra BK et al.
2012. Intensive training induces longitudinal changes in
meditation state-related EEG oscillatory activity. Front Hum
Neurosci. 6:256.

Schalk G, McFarland DJ, Hinterberger T, Birbaumer N, Wolpaw JR.
2004. BCI2000: a general-purpose brain-computer interface
(BCI) system. IEEE Trans Biomed Eng. 51:1034–1043.

Schoenberg PLA, Hepark S, Kan CC, Barendregt HP, Buitelaar
JK, Speckens AEM. 2014. Effects of mindfulness-based cogni-
tive therapy on neurophysiological correlates of performance
monitoring in adult attention-deficit/hyperactivity disorder.
Clin Neurophysiol. 125:1407–1416.

Sitaram R, Ros T, Stoeckel L, Haller S, Scharnowski F, Lewis-
Peacock J, Weiskopf N, Blefari ML, Rana M, Oblak E et al. 2017.
Closed-loop brain training: the science of neurofeedback. Nat
Rev Neurosci. 18:86–100.

Slagter HA, Lutz A, Greischar LL, Nieuwenhuis S, Davidson RJ.
2009. Theta phase synchrony and conscious target percep-
tion: impact of intensive mental training. NIH Public Access J
Cogn Neurosci. 21:1536–1549.

Soekadar SR, Witkowski M, Birbaumer N, Cohen LG. 2015.
Enhancing Hebbian learning to control brain oscillatory
activity. Cereb Cortex. 25:2409–2415.

Tan LF, Dienes Z, Jansari A, Goh SY. 2014. Effect of mindful-
ness meditation on brain-computer interface performance.
Conscious Cogn. 23:12–21.

438

Cerebral Cortex, 2021, Vol. 31, No. 1

Tang Y-Y, Hölzel BK, Posner MI. 2015. The neuroscience of

mindfulness meditation. Nat Rev Neurosci. 16:312–312.

organises into frequency specific phase-coupling networks.
Nat Commun. 9:1–13.

Tang Y-Y, Ma Y, Wang J, Fan Y, Feng S, Lu Q, Yu Q, Sui D, Roth-
bart MK, Fan M et al. 2007. Short-term meditation training
improves attention and self-regulation. Proc Natl Acad Sci.
104:17152–17156.

Wander JD, Blakely T, Miller KJ, Weaver KE, Johnson LA, Olson
JD, Fetz EE, Rao RPN, Ojemann JG. 2013. Distributed cortical
adaptation during learning of a brain-computer interface
task. Proc Natl Acad Sci USA. 110:10818–10823.

Wolpaw JR, McFarland DJ. 2004. Control of a two-dimensional
movement
a noninvasive brain-computer
interface in humans. Proc Natl Acad Sci USA. 101:
17849–17854.

signal by

Zhang H, Watrous AJ, Patel A, Jacobs J. 2018. Theta and alpha
oscillations are traveling waves in the human neocortex.
Neuron. 98:1269–1281.e4.

Ziegler DA, Simon AJ, Gallen CL, Skinner S, Janowich JR, Volponi
JJ, Rolle CE, Mishra J, Kornfield J, Anguera JA et al. 2019.
Closed-loop digital meditation improves sustained attention
in young adults. Nat Hum Behav. 3:746–757.

Thomas Yeo BT, Krienen FM, Sepulcre J, Sabuncu MR, Lashkari
D, Hollinshead M, Roffman JL, Smoller JW, Zöllei L, Polimeni
JR et al. 2011. The organization of the human cerebral cortex
estimated by intrinsic functional connectivity. J Neurophysiol.
106:1125–1165.

Tsui CSL, Gan JQ, Hu O. 2011. A self-paced motor imagery based
brain-computer interface for robotic wheelchair control. Clin
EEG Neurosci. 42:225–229.

van Lutterveld R, Houlihan SD, Pal P, Sacchet MD, McFarlane-
Blake C, Patel PR, Sullivan JS, Ossadtchi A, Druker S, Bauer C
et al. 2017. Source-space EEG neurofeedback links subjective
experience with brain activity during effortless awareness
meditation. Neuroimage. 151:117–127.

Vansteensel MJ, Pels EGM, Bleichner MG, Branco MP, Denison
T, Freudenburg ZV, Gosselaar P, Leinders S, Ottens TH, Van
Den Boom MA et al. 2016. Fully implanted brain-computer
interface in a locked-in patient with ALS. N Engl J Med.
375:2060–2066.

Vidaurre D, Hunt LT, Quinn AJ, Hunt BAE, Brookes MJ, Nobre AC,
Woolrich MW. 2018. Spontaneous cortical activity transiently
