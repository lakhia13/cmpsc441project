# Gao_2023_Increased neurocardiological interplay after mindfulness meditation a brain oscillation-based approach.

fnhum-17-1008490

June 13, 2023

Time: 14:41

# 1

OPEN ACCESS

EDITED BY
Changming Wang,
Capital Medical University, China

REVIEWED BY
Elzbieta Olejarczyk,
The Polish Academy of Sciences, Poland
XuanYu Chen,
Flinders University, Australia
Chuanliang Han,
Chinese Academy of Sciences (CAS), China

*CORRESPONDENCE
Hin Hung Sik

hinhung@hku.hk

RECEIVED 31 July 2022
ACCEPTED 02 June 2023
PUBLISHED 19 June 2023

CITATION
Gao J, Sun R, Leung HK, Roberts A, Wu BWY,
Tsang EW, Tang ACW and Sik HH (2023)
Increased neurocardiological interplay after
mindfulness meditation: a brain
oscillation-based approach.
Front. Hum. Neurosci. 17:1008490.
doi: 10.3389/fnhum.2023.1008490

COPYRIGHT
© 2023 Gao, Sun, Leung, Roberts, Wu, Tsang,
Tang and Sik. This is an open-access article
distributed under the terms of the Creative
Commons Attribution License (CC BY). The
use, distribution or reproduction in other
forums is permitted, provided the original
author(s) and the copyright owner(s) are
credited and that the original publication in this
journal is cited, in accordance with accepted
academic practice. No use, distribution or
reproduction is permitted which does not
comply with these terms.

TYPE Brief Research Report
PUBLISHED 19 June 2023
DOI 10.3389/fnhum.2023.1008490

Increased neurocardiological
interplay after mindfulness
meditation: a brain
oscillation-based approach

Junling Gao1, Rui Sun2, Hang Kin Leung1, Adam Roberts3,
Bonnie Wai Yan Wu1, Eric W. Tsang2, Andrew C. W. Tang4 and
Hin Hung Sik1*

1Buddhist Practices and Counselling Science Lab, Centre of Buddhist Studies, The University of
Hong Kong, Hong Kong, Hong Kong SAR, China, 2Department of Rehabilitation Sciences, The
Hong Kong Polytechnic University, Hong Kong, Hong Kong SAR, China, 3Singapore-ETH Centre, Future
Resilient Systems Programme, Singapore, Singapore, 4Department of Psychology, HKU School of
Professional and Continuing Education, Hong Kong, Hong Kong SAR, China

Background: Brain oscillations facilitate interaction within the brain network and
between the brain and heart activities, and the alpha wave, as a prominent brain
oscillation, plays a major role in these coherent activities. We hypothesize that
mindfully breathing can make the brain and heart activities more coherent in
terms of increased connectivity between the electroencephalogram (EEG) and
electrocardiogram (ECG) signals.

Methods: Eleven participants (28–52 years) attended 8 weeks of Mindfulness
Based Stress Reduction (MBSR) training. EEG and ECG data of two states of
mindful breathing and rest, both eye-closed, were recorded before and after the
training. EEGLAB was used to analyze the alpha band (8–12 Hz) power, alpha peak
frequency (APF), peak power and coherence. FMRIB toolbox was used to extract
the ECG data. Heart coherence (HC) and heartbeat evoked potential (HEP) were
calculated for further correlation analysis.

Results: After 8 weeks of MBSR training, the correlation between APF and HC
increased signiﬁcantly in the middle frontal region and bilateral temporal regions.
The correlation between alpha coherence and heart coherence had similar
changes, while alpha peak power did not reﬂect such changes. In contrast,
spectrum analysis alone did not show difference before and after MBSR training.

Conclusion: The brain works in rhythmic oscillation, and this rhythmic
connection becomes more coherent with cardiac activity after 8 weeks of MBSR
training. Individual APF is relatively stable and its interplay with cardiac activity
may be a more sensitive index than power spectrum by monitoring the brain-
heart connection. This preliminary study has important implications for the
neuroscientiﬁc measurement of meditative practice.

KEYWORDS

alpha peak frequency, mindfulness meditation, heart coherence, brain-heart connection,
effective connectivity, resting-state EEG

Frontiers in Human Neuroscience

01

frontiersin.org

fnhum-17-1008490

June 13, 2023

Time: 14:41

# 2

Gao et al.

10.3389/fnhum.2023.1008490

1. Introduction

Mindfulness meditation, a popular form of meditation, has
demonstrated a wide range of beneﬁts across various domains
such as education, clinical settings, commercial industries, and
the military (Goldberg et al., 2020; Duﬀ, 2022). Mind-body
to mindfulness meditation, and recent
connection is central
studies suggest
that meditation can modulate brain network
organization and the neural representation of cardiac activity
within the default mode network (Jiang et al., 2020; Lurz and
Ladwig, 2022; Wong et al., 2022). Nevertheless, research on the
potential neural mechanisms underlying brain-heart connection
remains relatively scarce when compared to enormous research
on other mechanisms of mindfulness (Ng et al., 2005; Minhas
et al., 2022). Our previous study demonstrated brain-heart
entrainment in mindfulness meditation practitioners, however, it
only examined the data at a group-level (Gao et al., 2016). To better
understand how the brain and body interact during meditation,
this study focuses on instantaneous brain-heart entrainment
during mindfulness meditation practice at an individual
level,
which would support a greater application in mindfulness
practice.

Naturally, immediate mind-body connections can be felt by
individuals in their response to signiﬁcant events or intense
emotions, with the heart being particularly responsive. This is
because that central nervous system modulates visceral organ
activity through the autonomic nervous system, with most
visceral organs functioning autonomously but exhibiting a clear
circadian rhythm (Tran et al., 2021; Chambers et al., 2022).
Maintaining coherent mind-body activity and circadian rhythms
is essential for our well-being, and disruptions can lead to visceral
organ dysfunction or even cardiac arrest (Tran et al., 2021).
Recognizing the importance of mind-body coherence, the bio-
medical-social model has been proposed for promoting health
(Heidger, 2011).

To simplify the investigation of the mind-body connection,
this study examines the relationship between cerebral and cardiac
activities, as the heart is the most responsive organ to external
stimuli (Lutwak and Dill, 2012). Electroencephalography (EEG)
and electrocardiography (ECG) can easily measure brain and
cardiac activities, respectively. Diﬀerent EEG frequency bands, such
as delta, theta, alpha, beta, and gamma, reﬂect various mental
states. Among these, the alpha wave is the primary human brain
oscillation, with changes in alpha wave activity being the most
reliable outcomes in EEG meditation studies (Lomas et al., 2015).

Diﬀerent meditation forms can induce changes in distinct brain
wave bands; for example, traditional Tibetan Buddhist meditation
is associated with gamma band changes (Lutz et al., 2004; Ferrarelli
et al., 2013; Jiang et al., 2020). Research has also shown that
the anterior cingulate cortex connects to the autonomic nervous
system (Devinsky et al., 1995), and frontal midline theta rhythm
correlates with heart rate variability during meditation (Kubota
et al., 2001). Nonetheless, increased alpha wave activity, particularly
in the occipital and frontal regions, has been universally observed
during various meditations (Cahn and Polich, 2006).

In this study, we focus on alpha wave analysis due to
its signiﬁcance in brain rhythm and dominance during eyes-
closed relaxation which has been proposed as a form of "cortical

idling" (Vanwinsum et al., 1984). The alpha power is inversely
proportional to the fraction of cortical neurons recruited for
any given task (Gevins and Schaﬀer, 1980). There is similarity
of alpha peak frequency (APF) to the central processing unit’s
main frequency within the brain network (Bera, 2015). The
APF has been implicated in cognitive preparedness (Angelakis
et al., 2004) and is positively correlated with processing speed,
memory, and cognitive performance in healthy individuals (Vogt
et al., 1998; Clark et al., 2004; Moretti et al., 2013; Sanchez-
Lopez et al., 2018). Clinical patients typically exhibit reduced
APF and lower cognitive performance compared to healthy
individuals (Klimesch et al., 1993; Bertaccini et al., 2022).
Higher alpha frequency is associated with better academic
performance (Klimesch, 1999) and intelligence (Anokhin and
Vogel, 1996).

Alpha peak frequency is a largely heritable trait, with
heritability accounting for most individual APF (iAPF) variance
(Mierau et al., 2017). Although iAPF is highly stable across
time and considered a heritable neurophysiological marker and
true endophenotype, evidence suggests that APF can be volatile
during diﬀerent mental states and may reﬂect a change in cerebral
oxygenation (Angelakis et al., 2004). Alpha wave activity can be
measured by averaging alpha band power within the 8–12 Hz range,
and alpha peak power can be speciﬁed to calibrate the highest
alpha power in 8–12 Hz range. Slight peak power of variations
across brain regions may occur due to diﬀerences in brain network
interactions (Mierau et al., 2017).

To measure the interactive activity among brain network, the
topography of this interactive synchronization can be calculated
by alpha coherence (Zheng et al., 2007). Coherence is typically
calculated using mean cross-power density over respective mean
auto-power spectral densities. Diﬀerent methods have been
developed to calculate brain connectivity, and mindfulness training
has been shown to modulate brain connectivity in diverse
populations (Kilpatrick et al., 2011; Jovanovic et al., 2013; Lifshitz
et al., 2019; Li et al., 2022).

Alpha waves are generated by thalamo-cortical information
interactions, such as feedback loops between excitatory and
inhibitory neurons (Dasilva, 1991; van Schie and Bekkering,
2007). These loops facilitate cortical information processing and
communication with the thalamus, potentially causing slight iAPF
shifts in diﬀerent mental states. The interplay between the thalamus
and cortex plays a critical role in various brain functions, including
consciousness and perception, and may contribute to brain-heart
activity interactions (Min et al., 2020).

The dynamic interaction between cerebral and cardiac electrical
activities can be directly reﬂected by the heartbeat evoked potential
(HEP). The R-peak of QRS waves in ECG is considered an
event related to ongoing cerebral electrical activity, allowing
HEP calculation using event-related potential methods. HEP
varies among individuals due to diﬀerences in body structure
and function, with higher HEP observed in those with greater
interoception (Jiang et al., 2020; Coll et al., 2021).

This study aims to investigate brain-heart interaction with a
focus on alpha oscillation, given its prominence in meditation
research. We primarily analyze the oscillation and synchronization
of neurophysiological systems between the brain network and
cardiac activity. By examining the fundamental synchronization,
we would demonstrate the critical role of brain-heart coherence

Frontiers in Human Neuroscience

02

frontiersin.org

fnhum-17-1008490

June 13, 2023

Time: 14:41

# 3

Gao et al.

10.3389/fnhum.2023.1008490

in a meditative state. Additionally, we did coherence analysis
in quantitative EEG to provide cortico-cortical interactions and
further topographical information on coherent oscillatory activity
during mindfulness meditation.

2. Materials and methods

2.1. Participants

Thirteen healthy participants from a local Mindfulness Based
Stress Reduction (MBSR) class were recruited for this EEG study.
Each of them was paid $HK200 to compensate for their time. The
Beck Depression Inventory (BDI) was used to exclude participants
with depression (Yeung et al., 2002). All participants had completed
education at or above the undergraduate level. None of them had
experience in MBSR. During the experiment, they were requested
to only practice the mindfulness breathing technique learned from
their MBSR course. The course was taught following the standard
MBSR program consisting of one pre-program orientation session,
eight weekly classes and one all-day class when the teacher
provided direct instructions. Also, participants had to make a
strong commitment to practice 45 min of MBSR training each day
as home assignments for 8 weeks individually, which included body
scanning and mindful breathing. The research was approved by the
local Institutional Review Board (IRB) and participants provided
their written informed consent before participating in this study.
One participant dropped out, and another participant had unusable
EEG data due to technical issues. Eventually, data from eleven
participants (6 males, 5 females, mean age 35.7 years; 7 Asians and 4
Caucasians) were used for the ﬁnal data report in this brief research.

2.2. Experiment procedure

Electroencephalogram data were recorded ﬁrst at the beginning
of the MBSR training (within 2 weeks), which was taught by a
qualiﬁed MBSR teacher. The second round of EEG data collection
was collected less than 1 month after the MBSR course, resulting
in two data sets with two conditions. One condition was having
the participants undergo 10 min of eye-closed normal rest, while
the other condition was 10 min of eye-closed mindful breathing.
Participants were instructed before each task not to ruminate or
fall asleep, and the experiment took place in a quiet room. To
make sure that trainees knew the correct way to perform the
MBSR mindful breathing, the early-stage MBSR condition was set
as 2 weeks after of training MBSR. All of the participants conﬁrmed
they did follow the instructions after the experiment and their
practice of mindfulness breathing was generally good. The Five
Facets Mindfulness Questionnaire (FFMQ) was used to measure
the change in mindfulness practice quality, and the score of non-
reacting facet increased from 22.8 ± 6.5 to 23.9 ± 7.3 (p = 0.042).
Please refer to the previous paper for more details (Gao et al., 2016).
The sequence of rest and mindful breathing was counter-balanced,
with half of the participants randomly assigned to perform the
mindful breathing task ﬁrst and the other half doing the rest task
ﬁrst.

2.3. Data acquisition and analysis

The data were acquired by a 128-channel NeuroSCAN system
in a quiet room. The sampling rate was set at 1,000 Hz. The system
has the reference default at the left mastoid, and we recomputed
the reference to the combination of both mastoids afterward during
data processing. The ECG electrodes were placed at the left and
right infraclavicular fossae after cleaning the area with alcohol.

Heart coherence was calculated by peak power divided by total
power (McCraty and Zayas, 2014; McCraty, 2022), where peak
power was determined by calculating the integral in a window
0.03 Hz wide, centered on the highest peak in the 0.04–0.4 Hz range
of the HRV power spectrum, and the total power was determined by
calculating the integral in a window of 0.0033–0.4 Hz wide. Heart
coherence has a value between 0 and 1 and indicates the magnitude
of similarity between the waveform of the HRV tachogram and a
sinusoidal wave (McCraty and Zayas, 2014; McCraty, 2022).

EEGLAB was used to extract the power of alpha peak, peak
frequency of the alpha wave, and alpha coherence. Eye movement
and ECG artifacts in the EEG data were cleaned using independent
component analysis (ICA). To evaluate the instantaneous heart
and brain coupling of each participant, we found the interval
RR from ECG data using the detect function of FMRIB toolbox,
then calculated the participant’s heart coherence. Using the RR
interval obtained, we set the window length accordingly for further
power spectrum analysis of the EEG data. Given the prominence
of the alpha wave, this study mainly focused on the alpha wave
band (8–12 Hz).

Functional connectivity between brain regions was estimated
from EEG coherence between electrodes overlying the participant’s
head (Bowyer, 2016). Coherence is one mathematical method used
to determine if two or more sensors, or brain regions, have similar
neuronal oscillatory activity. Coherence ranges from zero to one,
with a value near one indicating that EEG signals have similar
phase and amplitude diﬀerences at all time points and a value near
zero indicating that signals have a random diﬀerence in phase and
amplitude (Bowyer, 2016). In this study, we used lagged coherence
to exclude the non-lagged part of coherence which is believed to
be eﬀects of volume conduction (Milz et al., 2014). The lagged
coherence calculation details can be calculated as following,

LagCoh (f ) =

[ImGxy(f )]2

Gxx

(cid:0)f (cid:1) Gyy

(cid:0)f (cid:1) − [ReGxy(f )]2

where Gxy(f )
(cid:0)f (cid:1) , Gyy
Gxx
channel X and Y.

is

the

and
(cid:0)f (cid:1) are the auto-power spectral densities for each

spectral density

cross-power

To calculate the instantaneous brain-heart interplay, a sliding
window of 60 s was used, and the Pearson correlation coeﬃcient
was calculated between heart coherence and these alpha wave
indexes (Kim et al., 2013, 2014). This process returned an r-value
for each channel and each condition. The r-value diﬀerence
between before and after intervention was then calculated, and
ﬁnally, paired-sample t-tests were used to compare this r-value
diﬀerence between the mindful breathing and rest conditions.
Similar indices were calculated for the gamma wave.

Heartbeat evoked potential (HEP) was also calculated, as HEP
can reﬂect the interaction between cardiac and cerebral activities
(Jiang et al., 2020; Coll et al., 2021). The HEP was calculated by

Frontiers in Human Neuroscience

03

frontiersin.org

fnhum-17-1008490

June 13, 2023

Time: 14:41

# 4

Gao et al.

10.3389/fnhum.2023.1008490

extracting epochs that were time-locked to the R peaks of QRS
wave identiﬁed earlier in ECG channel, with the time window
set as −200 to 600 ms around the R peak event onset. Then
epochs were averaged to obtain the HEP data for each participant.
For each channel, paired-sample t-tests were used to analyze the
diﬀerence between conditions. Instantaneous correlation between
HEP and alpha wave indexes were also explored. Finally, we
also calculated brain eﬀective connectivity with partial directed
coherence (PDC) (Baccala and Sameshima, 2001). Signiﬁcant
diﬀerences were determined using p < 0.05. The ﬂowchart of data
collection and analysis is shown in Supplementary Figure 1.

3. Results

After MBSR training, participants had a greater brain-heart
connection during mindful breathing than that at the early-stage
training. This training eﬀect did not happen during close-eye rest.
This higher brain-heart connection is most obvious between
the alpha peak and heart coherence but also appears between alpha-
coherence and heart coherence, with a similar distribution. The
increased brain-heart connection is most apparent in the middle
frontal and also appears in the temporal and occipital regions of
the scalp. See Figures 1, 2.

Figure 1 shows an overall 2-D map of brain areas with increased
brain-heart connection after 8-week mindfulness training; while
Figure 2 shows a single channel with signiﬁcantly increased
brain-heart connection in terms of alpha coherence and heart
coherence. That is, a dark dot means a signiﬁcant change of brain-
heart connection after mindfulness training (see Supplementary
Tables 1, 2 for statistic).

show a signiﬁcant

Additionally, we calculated heart coherence and gamma
coherence, which did not
result. See
Supplementary Figure 2. Also, results of HEP analysis did
not show any diﬀerence after mindfulness training. Correlational
analysis between HEP and various alpha indexes were also
done. See Supplementary Figures 3–5. The power spectral
alpha peak
analysis of
frequency, and alpha coherence are shown in the Supplementary
Figures 6–9, respectively.

alpha peak power,

alpha power,

With regard to connectivity among brain regions only, these
brain connectivity results are shown in the Supplementary
Figure 10 and Supplementary Tables 3, 4. It demonstrates
signiﬁcantly increased brain connectivity was found after MBSR
training,
in terms of PDC indices, while less increased brain
connectivity is found during the resting state. The increased brain
connectivity was found mainly in the middle frontal with other
regions, including the temporal, parietal and occipital regions.

4. Discussion

The current study ﬁnds that the link between the brain
and heart during meditation may follow coherent rhythms
rather than amplitudes of neurophysiological activity due to a
stronger correlation between heart coherence and alpha wave
peak frequency instead of its peak power. Our previous study
on mindfulness meditation found entrainment between brain and

heart, but only in a group of meditators (Gao et al., 2016). That
study did not examine any longitudinal eﬀect of mindfulness
meditation either, as only spectrum analysis was made on EEG.
Similarly, we did not ﬁnd signiﬁcant longitudinal change in MBSR
training when directly comparing the spectral analysis of alpha
band, including the alpha power, alpha peak power, APF, alpha
coherence in the current study. However, we demonstrated that
instantaneous brain-heart connection considering both central
and peripheral physiological activities can be more sensitive to
mental state, and to measure the longitudinal eﬀect of mindfulness
training.

By measuring the simultaneous interplay between the EEG and
ECG, we found that APF becomes more correlated with heart
activities after 8 weeks of mindfulness meditation. This longitudinal
change did not happen during normal rest conditions. We did
not ﬁnd a similar brain-heart connection in the gamma wave
band (see Supplementary material). This implies the importance
of alpha wave and heart coherence when calculating brain-heart
connectivity. Our results demonstrated that APF can be a better
EEG measure than alpha power (amplitude) as it is more stable
in test-retest reliability (Salinsky et al., 1991; Rocha et al., 2020).
The greater between-session variability in EEG power may lead
to insigniﬁcant ﬁndings, as shown in the current results that no
signiﬁcant ﬁnding in alpha peak power and its correlation with
heart coherence.

Although APF is relatively stable and largely heritable,
accumulating evidence indicates that APF can shift slightly
during diﬀerent states, such as sleep, sensorimotor processing or
neurological disorders (Uhhaas and Singer, 2006). Mindfulness
breathing meditation may modulate the frequency of synchronous
neural activity and tune the alpha oscillation to be synchronized
with the heart activity. As shown by current results, the instant
correlation between APF and Heart coherence became more
positive after 8 weeks of MBSR training.

Heart coherence was calculated by the ratio of

low and
high frequency of heart rate, which partially reﬂects the balance
between the parasympathetic nervous system and sympathetic
nervous system (McCraty and Zayas, 2014; McCraty, 2022).
Heart coherence is associated with greater levels of emotion
regulation and cognitive ﬂexibility. The authors suggested that
heart coherence may reﬂect a state of physiological coherence that is
associated with better emotional and cognitive functioning (Shaﬀer
et al., 2014). Heart coherence represents the ordering degree in
the oscillation of heart rhythm intervals (Kim et al., 2013). This
study found heart coherence is a sensitive marker for meditation
states, given its strong correlation with middle-frontal APF and
alpha coherence. We did not ﬁnd a similar correlation between
heart coherence and gamma waves. It is plausible that gamma wave
is generated by neurons in a ﬁring state and communicating with
local cortical areas. Bursts of fast waves, such as gamma and beta
waves, play a supportive role in working memory and volitional
control.

In contrast, the alpha wave as the slow wave is generated
by the thalamo-cortical information interaction, such as feedback
loops of excitatory and inhibitory neurons (Dasilva, 1991; van
Schie and Bekkering, 2007). This loop enables the cortex to poll
information from the thalamus and process it, and then relay the
processed information back to the thalamus. Furthermore, the
interplay between the thalamus and cortex plays a critical role

Frontiers in Human Neuroscience

04

frontiersin.org

fnhum-17-1008490

June 13, 2023

Time: 14:41

# 5

Gao et al.

10.3389/fnhum.2023.1008490

FIGURE 1
Maps of brain-heart connections. This connection (r-value) was calculated based on correlation of alpha peak frequency and heart coherence (left
column), and correlation of alpha coherence and heart coherence (right column). The upper row is showing normal rest control condition before
and after 8-week mindfulness-based stress reduction (MBSR) training; the lower row is showing mindful breathing condition before and after MBSR
training. Color represents the r-value differences between before and after MBSR training. The black dots indicate electrodes with signiﬁcant
differences before and after MBSR training (p < 0.05, uncorrected).

in a variety of brain functioning, including consciousness and
perception (Min et al., 2020). During mindfulness breathing, the
practitioner needs to consciously monitor their breath-in and -
out. Breathing activity can be either conscious or unconscious. It
is assumed that mindful breathing may contribute to increased
interaction between brain-heart activities and improve the dynamic
oscillatory integration between the peripheral vegetative system
(including the cardiovascular system) and the central nervous
system. This is vital for individuals to maintain hemostasis, and
physical and mental health (Gebber et al., 1999).

Animal studies have found that the rhythmic activity in the
respiratory pathway can dynamically modulate the coupling of
central oscillators and peripheral targets (Gebber et al., 2004). The
discharges of sympathetic nerves generated by central oscillators
are around 10 Hz, parallel to the alpha wave band (Gebber et al.,
1999). Our results demonstrate that mindfully controlled breathing
can cause a slight shift of iAPF in diﬀerent mind states. This may
modulate the coupling of central oscillators and peripheral targets,

including cardiac activity, and enhance the cardio-respiratory
coordination and, broadly, body-mind connection. Future studies
are needed to investigate the role of respiratory activities in
connecting cardiac and cerebral activities to determine their
potential mediative relationship.

In addition to APF, we found that heart coherence is also
correlated with alpha coherence, which is involved in alpha wave
generation. A previous study of alpha coherence demonstrated
that functional interaction between posterior and anterior brain
regions might be involved in generating alpha rhythm during the
waking time (Wang et al., 1992). Alpha coherence can be applied to
illustrate the functional relationship between diﬀerent brain regions
(Achermann and Borbely, 1998; Cantero et al., 1999; Jorge et al.,
2017). The fronto-occipital fasciculi physiologically supports this
long-range interaction (Mai et al., 2004). Alpha coherence can
discern diﬀerent arousal levels and is a sensitive index to evaluate
various mental states (Cantero et al., 1999). For example, alpha
coherence is reduced in patients with Alzheimer’s disease during

Frontiers in Human Neuroscience

05

frontiersin.org

fnhum-17-1008490

June 13, 2023

Time: 14:41

# 6

Gao et al.

10.3389/fnhum.2023.1008490

FIGURE 2
Examples of linear regressions for channel Fz of one participant. (A) Instantaneous correlation (60 s, with 4 s sliding) of alpha coherence and heart
coherence during mindful breathing before (r = –0.153, p = 0.077; blue line) and after (r = 0.361, p < 0.0001; red line) mindfulness-based stress
reduction (MBSR) training; (B) normal rest before (r = 0.190, p = 0.028; blue line) and after (r = –0.226, p = 0.008; red line) MBSR training. Solid line
represents signiﬁcant correlation (p < 0.05).

task that needs memory activity (Hogan et al., 2003). On the
other hand, how the sinusoidal oscillations of alpha wave creates
coherence among brain regions and its generation mechanism has
not been fully illustrated (Miranda de Sá and Infantosi, 2005).

Heartbeat evoked potential reﬂects the relationship of cardiac
electric activity and cerebral electric activity, and it is found to
be related to the sense of interoception. In this study, we did not
ﬁnd any longitudinal change in HEP, or any correlation between

Frontiers in Human Neuroscience

06

frontiersin.org

fnhum-17-1008490

June 13, 2023

Time: 14:41

# 7

Gao et al.

10.3389/fnhum.2023.1008490

the HEP and alpha band power, alpha peak frequency, or alpha
coherence. We did ﬁnd great variability of HEP among individuals,
and also HEP could be easily contaminated by direct cardiac electric
activity. This may contribute to the negative ﬁnding of HEP in
mindfulness training.

Several

limitations are worth noting. Firstly, the number
of participants in this brief report is relatively small and no
control group was recruited. More participants are in future
studies to ensure statistical power after correction for multiple
comparisons. The limited sample size and absence of a control
group may restrict the generalizability of the ﬁndings to broader
populations. A second limitation is that although there is a
signiﬁcant increased correlation between cardiac and cerebral
activities after mindfulness training, no causal relationship can be
made. Additional measurement of breath rate may help explore
the causal and mediative relationship between brain, cardiac and
respiratory activities.

In sum, 8-week MBSR training can promote brain-heart
coherence. Additionally, brain connectivity between two signals
provides richer information compared to undirected functional
connectivity (Baccala and Sameshima, 2001; Kaminski et al., 2016).
The increased alpha rhythm-ECG synchronization at the frontal
lobe during MBSR after 8-week training indicates the importance
of coherence to maintain an optimal psychophysiological state.
It is suggested that the coherence of neurophysiological activity,
especially the neurocardiological interplay, plays a vital role in
mind and body wellbeing (McCraty et al., 2009). This rhythm-
based analysis can also be used to explore other types of meditations
which may have diﬀerent eﬀects on APF and heart coherence.

Author contributions

JG conducted the experiment and prepared the manuscript.
RS analyzed the data and experiment design. HL assisted on
data analysis, and together with AR and BW, helped prepare
the manuscript and shared important ideas. ET and AT helped
on statistics and experiment data analysis. HS helped on the
experiment design and coordinated the study. All authors
contributed to the article and approved the submitted version.

Funding

This study was partially supported by the SPF-201209176152
fund from the University of Hong Kong and the MaMa
Charitable Foundation.

Acknowledgments

We would like to thank Dr. Shuk-wah Helen MA for her

teaching of MBSR course.

Conﬂict of interest

The authors declare that the research was conducted in the
absence of any commercial or ﬁnancial relationships that could be
construed as a potential conﬂict of interest.

Data availability statement

Publisher’s note

The original contributions presented in this

study are
included in the article, further inquiries can be directed to the
corresponding author.

Ethics statement

The studies involving human participants were reviewed and
approved by the Institutional Review Board (IRB), The University
of Hong Kong. The patients/participants provided their written
informed consent to participate in this study.

References

All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their aﬃliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed or
endorsed by the publisher.

Supplementary material

The Supplementary Material for this article can be found
https://www.frontiersin.org/articles/10.3389/fnhum.

online
2023.1008490/full#supplementary-material

at:

Achermann, P., and Borbely, A. A. (1998). Coherence analysis of the human sleep
electroencephalogram. Neuroscience 85, 1195–1208. doi: 10.1016/S0306-4522(97)
00692-1

Anokhin, A., and Vogel, F.

(1996). EEG alpha rhythm frequency and
intelligence in normal adults. Intelligence 23, 1–14. doi: 10.1016/S0160-2896(96)80
002-X

Angelakis, E., Lubar, J. F., Stathopoulou, S., and Kounios, J. (2004). Peak alpha
frequency: An electroencephalographic measure of cognitive preparedness. Clin.
Neurophysiol. 115, 887–897. doi: 10.1016/j.clinph.2003.11.034

Baccala, L. A., and Sameshima, K. (2001). Partial directed coherence: A new concept
in neural structure determination. Biol. Cybern. 84, 463–474. doi: 10.1007/PL0000
7990

Frontiers in Human Neuroscience

07

frontiersin.org

fnhum-17-1008490

June 13, 2023

Time: 14:41

# 8

Gao et al.

10.3389/fnhum.2023.1008490

Bera, T. K. (2015). “Noninvasive electromagnetic methods for brain monitoring: A
technical review,” in Brain-computer interfaces : Current trends and applications, 1st
Edn, ed. A. T. Azar (Cham: Springer International Publishing).

Kim, D. K., Rhee, J. H., and Kang, S. W. (2014). Reorganization of the brain and
heart rhythm during autogenic meditation. Front. Integr. Neurosci. 7:109. doi: 10.3389/
fnint.2013.00109

Bertaccini, R., Ellena, G., Macedo-Pascual, J., Carusi, F., Trajkovic, J., Poch, C.,
et al. (2022). Parietal alpha oscillatory peak frequency mediates the eﬀect of practice
on visuospatial working memory performance. Vision 6:30. doi: 10.3390/vision602
0030

Klimesch, W. (1999). EEG alpha and theta oscillations reﬂect cognitive and memory
performance: A review and analysis. Brain Res. Rev. 29, 169–195. doi: 10.1016/S0165-
0173(98)00056-3

Klimesch, W., Schimke, H., and Pfurtscheller, G. (1993). Alpha frequency, cognitive

Bowyer, S. M. (2016). Coherence a measure of the brain networks: Past and present.

load and memory performance. Brain Topogr. 5, 241–251. doi: 10.1007/BF01128991

Neuropsychiatr. Electrophysiol. 2:1. doi: 10.1186/s40810-015-0015-7

Cahn, B. R., and Polich, J. (2006). Meditation states and traits: EEG, ERP, and
neuroimaging studies. Psychol. Bull. 132, 180–211. doi: 10.1037/0033-2909.132.2.180

Cantero, J. L., Atienza, M., Salas, R. M., and Gomez, C. M. (1999). Alpha EEG
coherence in diﬀerent brain states: An electrophysiological index of the arousal
level in human subjects. Neurosci. Lett. 271, 167–170. doi: 10.1016/s0304-3940(99)00
565-0

Kubota, Y., Sato, W., Toichi, M., Murai, T., Okada, T., Hayashi, A., et al. (2001).
Frontal midline theta rhythm is correlated with cardiac autonomic activities during
the performance of an attention demanding meditation procedure. Cogn. Brain Res.
11, 281–287. doi: 10.1016/S0926-6410(00)00086-0

Li, H., Yan, W., Wang, Q. W., Liu, L., Lin, X., Zhu, X. M., et al. (2022).
Mindfulness-based cognitive therapy regulates brain connectivity in patients with
late-life depression. Front. Psychiatry 13:841461. doi: 10.3389/fpsyt.2022.841461

Chambers, L., Seidler, K., and Barrow, M. (2022). Nutritional entrainment of
circadian rhythms under alignment and misalignment: A mechanistic review. Clin.
Nutr. ESPEN 51, 50–71. doi: 10.1016/j.clnesp.2022.06.010

Lifshitz, M., Sacchet, M. D., Huntenburg, J. M., Thiery, T., Fan, Y., Gartner, M., et al.
(2019). Mindfulness-based therapy regulates brain connectivity in major depression.
Psychother. Psychosomat. 88, 375–377. doi: 10.1159/000501170

Clark, C. R., Veltmeyer, M. D., Hamilton, R. J., Simms, E., Paul, R., Hermens,
D., et al. (2004). Spontaneous alpha peak frequency predicts working memory
performance across the age span. Int. J. Psychophysiol. 53, 1–9. doi: 10.1016/j.ijpsycho.
2003.12.011

Coll, M. P., Hobson, H., Bird, G., and Murphy, J. (2021). Systematic review
and meta-analysis of the relationship between the heartbeat-evoked potential and
interoception. Neurosci. Biobehav. Rev. 122, 190–200. doi: 10.1016/j.neubiorev.2020.
12.012

Dasilva, F. L. (1991). Neural mechanisms underlying brain waves - from neural
membranes to networks. Electroencephalogr. Clin. Neurophysiol. 79, 81–93. doi: 10.
1016/0013-4694(91)90044-5

Devinsky, O., Morrell, M. J., and Vogt, B. A. (1995). Contributions of anterior

cingulate cortex to behaviour. Brain 118, 279–306. doi: 10.1093/brain/118.1.279

Lomas, T., Ivtzan, I., and Fu, C. H. (2015). A systematic review of

the
neurophysiology of mindfulness on EEG oscillations. Neurosci. Biobehav. Rev. 57,
401–410. doi: 10.1016/j.neubiorev.2015.09.018

Lurz, J., and Ladwig, K. H. (2022). Mind and body interventions in cardiology: The
importance of the brain-heart connection. Herz 47, 103–109. doi: 10.1007/s00059-
022-05104-y

Lutwak, N., and Dill, C. (2012). The mind body connection and cardiovascular

disease. Int. J. Clin. Pract. 66, 1126–1127. doi: 10.1111/ijcp.12002

Lutz, A., Greischar, L. L., Rawlings, N. B., Ricard, M., and Davidson, R. J.
(2004). Long-term meditators self-induce high-amplitude gamma synchrony during
mental practice. Proc. Natl. Acad. Sci. U. S. A. 101, 16369–16373. doi: 10.1073/pnas.
0407401101

Mai, J. K., Assheuer, J., and Paxinos, G. (2004). Atlas of the human brain. Amsterdam:

Duﬀ, C. (2022). Educational policy shifts: A critical review of the emerging trend of

Elsevier Academic Press.

mindfulness in education. Policy Futures Educ. 20, 608–616.

Ferrarelli, F., Smith, R., Dentico, D., Riedner, B. A., Zennig, C., Benca, R. M., et al.
(2013). Experienced mindfulness meditators exhibit higher parietal-occipital EEG
gamma activity during NREM sleep. PLoS One 8:e73417. doi: 10.1371/journal.pone.
0073417

Gao, J., Fan, J., Wu, B. W., Halkias, G. T., Chau, M., Fung, P. C., et al. (2016).
Repetitive religious chanting modulates the late-stage brain response to fear- and
stress-provoking pictures. Front. Psychol. 7:2055. doi: 10.3389/fpsyg.2016.02055

Gebber, G. L., Das, M., and Barman, S. M. (2004). An unusual form of phase
walk in a system of coupled oscillators. J. Biol. Rhythms 19, 542–550. doi: 10.1177/
0748730404268053

Gebber, G. L., Zhong, S., Lewis, C., and Barman, S. M. (1999). Human brain alpha
rhythm: Nonlinear oscillation or ﬁltered noise?. Brain Res. 818, 556–560. doi: 10.1016/
s0006-8993(98)01303-1

Gevins, A. S., and Schaﬀer, R. E. (1980). A critical-review of electroencephalographic

(EEG) correlates of higher cortical functions. Crit. Rev. Bioeng. 4, 113–164.

Goldberg, S. B., Riordan, K. M., Sun, S. F., Kearney, D. J., and Simpson, T. L. (2020).
Eﬃcacy and acceptability of mindfulness-based interventions for military veterans:
A systematic review and meta-analysis. J. Psychosom. Res. 138:110232. doi: 10.1016/
j.jpsychores.2020.110232

Heidger, P. M. (2011). A model course for exploring social, ethical, and legal aspects

of biomedical research. FASEB J. 25:673.

Hogan, M. J., Swanwick, G. R. J., Kaiser, J., Rowan, M., and Lawlor, B. (2003).
Memory-related EEG power and coherence reductions in mild Alzheimer’s disease.
Int. J. Psychophysiol. 49, 147–163. doi: 10.1016/S0167-8760(03)00118-1

Jiang, H., He, B., Guo, X., Wang, X., Guo, M., Wang, Z., et al. (2020). Brain-heart
interactions underlying traditional Tibetan Buddhist meditation. Cereb. Cortex 30,
439–450. doi: 10.1093/cercor/bhz095

Jorge, M. S., Spindola, L., Katata, J. H. B., and Anghinah, R. (2017). Alpha band EEG
coherence in healthy nonagenarians. Arq. Neuropsiquiatr. 75, 609–613. doi: 10.1590/
0004-282X20170102

Jovanovic, A., Perovic, A., and Borovcanin, M. (2013). Brain connectivity measures:

Computation and comparison. EPJ Nonlinear Biomed. 1:2. doi: 10.1140/epjnbp2

Kaminski, M., Brzezicka, A., Kaminski, J., and Blinowska, K. J. (2016). Measures
of coupling between neural populations based on granger causality principle. Front.
Comput. Neurosci. 10:114. doi: 10.3389/fncom.2016.00114

Kilpatrick, L. A., Suyenobu, B. Y., Smith, S. R., Bueller, J. A., Goodman, T., Creswell,
J. D., et al. (2011). Impact of mindfulness-based stress reduction training on intrinsic
brain connectivity. Neuroimage 56, 290–298. doi: 10.1016/j.neuroimage.2011.02.034

Kim, D. K., Lee, K. M., Kim, J., Whang, M. C., and Kang, S. W. (2013). Dynamic
correlations between heart and brain rhythm during Autogenic meditation. Front.
Hum. Neurosci. 7:414. doi: 10.3389/fnhum.2013.00414

McCraty, R. (2022). Following the rhythm of the heart: Heartmath institute’s path to
HRV biofeedback. Appl. Psychophysiol. Biofeedback 47, 305–316. doi: 10.1007/s10484-
022-09554-2

McCraty, R., and Zayas, M. A. (2014). Cardiac coherence, self-regulation, autonomic
stability, and psychosocial well-being. Front. Psychol. 5:1090. doi: 10.3389/fpsyg.2014.
01090

McCraty, R., Atkinson, M., Tomasino, D., and Bradley, R. T. (2009). The coherence
heart: Heart-brain interactions, psychophysiological coherence, and the emergence of
system-wide order. Integr. Rev. 5, 1–106.

Mierau, A., Klimesch, W., and Lefebvre, J. (2017). State-dependent alpha peak
frequency shifts: Experimental evidence, potential mechanisms and functional
implications. Neuroscience 360, 146–154. doi: 10.1016/j.neuroscience.2017.07.037

Milz, P., Faber, P. L., Lehmann, D., Kochi, K., and Pascual-Marqui, R. D. (2014).
sLORETA intracortical lagged coherence during breath counting in meditation-naïve
participants. Front. Hum. Neurosci. 8:303. doi: 10.3389/fnhum.2014.00303

Min, B. K., Kim, H. S., Pinotsis, D. A., and Pantazis, D. (2020). Thalamocortical
inhibitory dynamics support conscious perception. Neuroimage 220:117066. doi: 10.
1016/j.neuroimage.2020.117066

Minhas, S., Patel, J. R., Malik, M., Hana, D., Hassan, F., and Khouzam, R. N. (2022).
Mind-body connection: Cardiovascular sequelae of psychiatric illness. Curr. Probl.
Cardiol. 47:100959. doi: 10.1016/j.cpcardiol.2021.100959

Miranda de Sá, A., and Infantosi, A. F. C. (2005). Evaluating the entrainment of the
alpha rhythm during stroboscopic ﬂash stimulation by means of coherence analysis.
Med. Eng. Phys. 27, 167–173. doi: 10.1016/j.medengphy.2004.09.011

Moretti, D. V., Paternico, D., Binetti, G., Zanetti, O., and Frisoni, G. B. (2013).
EEG upper/low alpha frequency power ratio relates to temporo-parietal brain atrophy
and memory performances in mild cognitive impairment. Front. Aging Neurosci. 5:63.
doi: 10.3389/fnagi.2013.00063

Ng, S. M., Yau, J. K., Chan, C. L., Chan, C. H., and Ho, D. Y. (2005).
The measurement of body-mind-spirit well-being toward multidimensionality and
transcultural applicability. Soc. Work Health Care 41, 33–52. doi: 10.1300/J010v41n01_
03

Rocha, H. A., Marks, J., Woods, A. J., Staud, R., Sibille, K., and Keil, A. (2020). Re-test
reliability and internal consistency of EEG alpha-band oscillations in older adults with
chronic knee pain. Clin. Neurophysiol. 131, 2630–2640. doi: 10.1016/j.clinph.2020.07.
022

Salinsky, M. C., Oken, B. S., and Morehead, L. (1991). Test-retest reliability in EEG
frequency analysis. Electroencephalogr. Clin. Neurophysiol. 79, 382–392. doi: 10.1016/
0013-4694(91)90203-g

Sanchez-Lopez, J., Silva-Pereyra, J., Fernandez, T., Alatorre-Cruz, G. C., Castro-
Chavira, S. A., Gonzalez-Lopez, M., et al. (2018). High levels of incidental physical
activity are positively associated with cognition and EEG activity in aging. PLoS One
13:e0191561. doi: 10.1371/journal.pone.0191561

Frontiers in Human Neuroscience

08

frontiersin.org

fnhum-17-1008490

June 13, 2023

Time: 14:41

# 9

Gao et al.

10.3389/fnhum.2023.1008490

Shaﬀer, F., McCraty, R., and Zerr, C. L. (2014). A healthy heart is not a metronome:
An integrative review of the heart’s anatomy and heart rate variability. Front. Psychol.
5:1040. doi: 10.3389/fpsyg.2014.01040

Vogt, F., Klimesch, W., and Doppelmayr, M. (1998). High-frequency components
in the alpha band and memory performance. J. Clin. Neurophysiol. 15, 167–172.
doi: 10.1097/00004691-199803000-00011

Tran, D. T., St Pierre Schneider, B., and McGinnis, G. R. (2021). Circadian rhythms
in sudden cardiac arrest: A review. Nurs. Res. 70, 298–309. doi: 10.1097/NNR.
0000000000000512

Wang, G., Takigawa, M., and Matsushita, T. (1992). Correlation of alpha activity
between the frontal and occipital cortex. Jpn. J. Physiol. 42, 1–13. doi: 10.2170/jjphysio
l.42.1

Uhhaas, P. J., and Singer, W. (2006). Neural synchrony in brain disorders: Relevance
for cognitive dysfunctions and pathophysiology. Neuron 52, 155–168. doi: 10.1016/j.
neuron.2006.09.020

Wong, G. F., Sun, R., Adler, J., Yeung, K. W., Yu, S., and Gao, J. L. (2022). Loving-
kindness meditation (LKM) modulates brain-heart connection: An EEG case study.
Front. Hum. Neurosci. 16:891377. doi: 10.3389/fnhum.2022.891377

van Schie, H. T., and Bekkering, H. (2007). Neural mechanisms underlying
immediate and ﬁnal action goals in object use reﬂected by slow wave brain potentials.
Brain Res. 1148, 183–197. doi: 10.1016/j.brainres.2007.02.085

Vanwinsum, W., Sergeant, J., and Geuze, R. (1984). The functional-signiﬁcance
of event-related desynchronization of alpha-rhythm in attentional and activating
tasks. Electroencephalogr. Clin. Neurophysiol. 58, 519–524. doi: 10.1016/0013-4694(84)
90042-7

Yeung, A., Howarth, S., Chan, R., Sonawalla, S., Nierenberg, A. A., and Fava, M.
(2002). Use of the Chinese version of the beck depression Inventory for screening
depression in primary care. J. Nerv. Ment. Dis. 190, 94–99. doi: 10.1097/00005053-
200202000-00005

Zheng, L. L., Jiang, Z. Y., and Yu, E. Y. (2007). Alpha spectral power and coherence
in the patients with mild cognitive impairment during a three-level working memory
task. J. Zhejiang Univ. Sci. B 8, 584–592. doi: 10.1631/jzus.2007.B0584

Frontiers in Human Neuroscience

09

frontiersin.org
