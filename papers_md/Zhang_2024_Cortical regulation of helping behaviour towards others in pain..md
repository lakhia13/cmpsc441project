# Zhang_2024_Cortical regulation of helping behaviour towards others in pain.

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
Nature. Author manuscript; available in PMC 2025 February 01.

Published in final edited form as:

Nature. 2024 February ; 626(7997): 136–144. doi:10.1038/s41586-023-06973-x.

Cortical regulation of helping behavior toward others in pain

Mingmin Zhang1,4, Ye Emily Wu1,2,4, Mengping Jiang1, Weizhe Hong1,3,*
1Department of Neurobiology and Department of Biological Chemistry, David Geffen School of 
Medicine, University of California, Los Angeles, CA 90095, USA

2Department of Neurology, David Geffen School of Medicine, University of California, Los 
Angeles, CA 90095, USA

3Department of Bioengineering, Samueli School of Engineering, University of California, Los 
Angeles, CA 90095, USA

4These authors contributed equally.

Abstract

Humans and animals display various forms of prosocial helping behavior towards others in 
need1-3. While previous research has investigated how individuals may perceive others’ states4,5, 
the neural mechanisms of how they respond to others’ needs and goals with helping behavior 
remain largely unknown. Here we show that mice engage in a form of helping behavior towards 
other individuals experiencing physical pain and injury—they exhibit allolicking (social licking) 
behavior specifically towards the injury site, which aids the recipients in coping with pain. Using 
microendoscopic imaging, we found that single-neuron and ensemble activity in the anterior 
cingulate cortex (ACC) encodes others’ state of pain and that this representation is different 
from that of general stress in others. Furthermore, functional manipulations demonstrate a causal 
role of the ACC in bidirectionally controlling targeted allolicking. Interestingly, this behavior is 
represented in a population code in the ACC that differs from that of general allogrooming, a 
distinct type of prosocial behavior elicited by others’ emotional stress. These findings significantly 
advance our understanding of the neural coding and regulation of helping behavior.

Main

The ability to engage in different forms of prosocial behaviors to address the various 
needs of others is critical for enhancing survival and promoting social cohesion1-3. One 
crucial form of prosocial action that remains inadequately understood is helping behavior, 
which involves taking actions to assist others in achieving specific goals1-3,6. Such helping 
behavior is distinct from other types of prosocial behavior such as comforting that is aimed 
at relieving another’s emotional distress1,7,8, and has been documented in a wide range 
of social species from humans to rodents2,3,6. For example, humans may provide practical 

* whong@ucla.edu .
Author contributions: M.Z., Y.E.W., and W.H. designed the study. M.Z. performed all experiments. Y.E.W. and M.Z. performed 
computational data analysis. M.J. assisted in some experiments. Y.E.W., M.Z., and W.H. wrote the manuscript. W.H. supervised the 
entire study.

Competing interests: The authors declare no competing interests.

 
 
 
 
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

Zhang et al.

Page 2

support to help others solve problems or avoid harm, and rats have been observed to 
help free a constrained conspecific3,6,9. While prior studies have shown that humans and 
animals may perceive others’ states4,5, the mechanisms of how an individual responds to 
others’ specific needs and goals with targeted helping behavior remain largely unknown. 
Although these helping responses require an initial recognition of others’ states and needs, 
this recognition would have limited value to those in need if the observers do not provide 
assistance.

Animals often need to cope with pain and injury to maintain their health and well-being. 
The experience of pain elicits robust instinctive behavioral responses, such as self-licking of 
the injury site, which can not only alleviate pain but also reduce the risk of infection and 
promote wound healing through enzymes and other components contained in the saliva10-14. 
In social situations, one individual’s pain or injury also presents a salient social signal that 
may elicit helping responses from other individuals—humans often offer physical assistance 
to treat others’ wounds, and a wide range of animals, from primates to rodents, can care for 
others’ injury sites through communal wound licking, which is thought to promote wound 
healing, prevent infection, and promote social bonds15-17. This targeted helping response 
is distinct from comforting behavior that primarily provides general emotional support, 
as ongoing, localized pain in another individual presents a specific need that requires a 
goal-oriented action directed towards the site of injury. However, the characteristics of this 
behavior, how it aids others in wound care, and the underlying neural circuitry have been 
largely unclear.

Helping responses to others in pain

To characterize how mice respond to conspecifics experiencing ongoing pain, we acutely 
induced localized pain in one mouse (“demonstrator”) in a pair of co-housed mice by 
injecting melittin into one hind paw (Fig. 1a, Extended Data Fig. 1a). Melittin is a major 
component in bee venom and induces tonic pain sensation and inflammation18. Following 
melittin injection, demonstrator mice displayed sustained self-licking towards the injected 
paw (Extended Data Fig. 1b-e), a common behavioral response to self-pain and injury18. 
Self-licking was specifically directed towards the injected paw but not the other paws 
(Extended Data Fig. 1b-e).

We next examined how a naïve cage mate (“observer”) interacts with a melittin-injected 
demonstrator (Fig. 1a, b). Compared to the control group where demonstrators received a 
saline injection in the hind paw, observers displayed a higher level of allogrooming (social 
grooming) behavior towards melittin-injected demonstrators in both males and females (Fig. 
1c-e, g, k, Extended Data Fig. 2, Supplementary Video 1). This behavior was primarily 
directed towards the dorsal flank, neck, and head regions of the recipient (Fig. 1b) This 
increase in allogrooming is reminiscent of our previous research demonstrating that mice 
exhibit increased allogrooming as a form of comforting behavior towards emotionally 
distressed animals19, and may reflect a response to a general negative state in others induced 
by local pain and injury21.

Strikingly, we found that observers also exhibited a marked increase in allolicking behavior 
towards the melittin-injected paws of the demonstrators in both male and female animals 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 3

(Fig. 1b-e, h, i, l, m, Extended Data Fig. 2, Supplementary Video 2, Methods), with 
more pronounced increase in males than in females (Wilcoxon rank-sum test, P = 0.0067; 
Supplementary Note 1). The use of side- and bottom-view cameras allowed us to distinguish 
behaviors targeted at the injured hind paw from those targeted at other body areas (Fig. 
1a, b). Similar to self-licking in demonstrators, allolicking by observers was specifically 
targeted at the melittin-injected paw, but not other uninjected paws, of the demonstrator (Fig. 
1b, d, e, h, l, Extended Data Fig. 1f-i, Extended Data Fig. 2b, c, f, j). Thus, allolicking 
targeted at the injured paw is a separate behavioral response that can be distinguished 
from general allogrooming that is broadly directed towards other body parts outside the 
pain region. Moreover, we observed distinct patterns of head movements during allolicking 
and allogrooming using a digital gyroscope (Methods)—allogrooming was associated with 
rhythmic head bobbing, as evident in the oscillatory changes in head angle, whereas such 
movements were not observed during allolicking (Fig. 1n, o). This further suggests that 
allolicking and allogrooming represent separate behavioral responses that not only target 
different body locations but are also associated with distinct motor patterns.

Interestingly, we observed a positive correlation between the total durations of allogrooming 
and allolicking towards melittin-injected demonstrators (Fig. 1p), suggesting that these 
behaviors might be co-regulated. The correlation is specific to these two behaviors, as the 
duration of allogrooming did not correlate with that of allolicking towards uninjured paws 
(Fig. 1q) and the duration of allogrooming or allolicking did not correlate with that of 
close investigation (Fig. 1r, s). Moreover, while social investigation mostly occurred within 
the first five minutes of the interaction period, allogrooming and allolicking continued 
throughout the entire session (Fig. 1e). Thus, allolicking and allogrooming are separate 
from (and occur mostly after) investigative social behavior that is intended for assessing the 
state of the demonstrator. We further examined the relationship between dominance status 
and allolicking and allogrooming behaviors, and found that the amount of allolicking and 
allogrooming behavior was not significantly different between dominant and subordinate 
observers (Extended Data Fig. 1j-m).

Lastly, to determine if these behavioral responses are generalized to different pain 
conditions, we also examined how observers respond to demonstrators with injection of 
formalin, another chemical that elicits sustained pain through mechanisms different from 
those of melittin-induced pain (Methods)20. We found that observers displayed increased 
targeted allolicking towards the injured paw as well as general allogrooming of other 
body parts (Extended Data Fig. 3), suggesting that both behaviors reflect active responses 
towards conspecifics in pain. By contrast, demonstrators that experienced an acute stressor 
(acute restraint), but not ongoing pain, elicited only general allogrooming, but not targeted 
allolicking, from observers (Extended Data Fig. 4), indicating that targeted allolicking 
towards the injury site is a specific behavioral response to ongoing local pain in others.

Allolicking helps others cope with pain

Self-licking is an instinctive response towards an injury site that provides multiple benefits. 
It is a prevalent pain-coping behavior, likely providing tactile-induced analgesia13,14,21. 
Licking also covers the injury site with silva, which contains components (such as enzymes 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 4

and growth factors) that can reduce pain, prevent infection, and enhance wound healing10-14. 
As allolicking by an observer appears to be similar to self-licking (i.e., both are licking 
behaviors specifically towards the injury site), allolicking may aid the demonstrator by 
serving a comparable function as the demonstrator’s own self-licking. If this is the case, 
allolicking by observers may lead to a reduced need for the demonstrator to engage in 
self-licking.

Indeed, the interaction with observers resulted in an overall decrease in the amount of 
self-licking exhibited by the demonstrators, as compared to when observers were absent 
(Fig. 2a, b). Interestingly, this reduction was positively correlated with the total duration of 
observers’ allogrooming and allolicking (Fig. 2c). Importantly, the reduction in self-licking 
was not correlated with general investigation time (Fig. 2d), suggesting that this effect 
is not attributable to the mere presence or proximity of a social partner. In particular, 
demonstrators that received a low level of allogrooming and allolicking exhibited no 
significant reduction of self-licking (Extended Data Fig. 5a). By contrast, demonstrators 
that received a high level of allogrooming and allolicking exhibited a significant reduction 
of self-licking (Fig. 2e, Extended Data Fig. 5b), and the combined duration of self-licking 
and allolicking in a social setting is comparable to the amount of time that animals spent 
self-licking when they were alone (Extended Data Fig. 5b).

In addition to an overall decrease of self-licking throughout the entire session, we also 
observed a decrease in the probability of self-licking during the periods within each session 
when demonstrators received allogrooming or allolicking from observers, compared to other 
periods (Fig. 2f). Interestingly, the reduction in the probability of self-licking is greater 
during allolicking compared to that during general allogrooming, suggesting that targeted 
allolicking may have a more direct and effective role in reducing self-licking. Moreover, 
to determine how allolicking may acutely reduce self-licking, we examined the temporal 
dynamics of self-licking towards the injured paw following the onset of allolicking (Fig. 
2g). Self-licking, like any other behavior, shows temporal dynamics that reflects a natural 
termination of the behavior (Fig. 2h, i). However, allolicking led to a more rapid reduction 
in the probability of self-licking compared to the natural temporal dynamics (Fig. 2h, i). 
This phenomenon was specific to allolicking towards the injured paw and was not observed 
when allolicking was directed towards the uninjured paw (Fig. 2j, k). Together, these results 
support the notion that targeted allolicking towards others in pain can benefit the recipient by 
partially replacing the need for self-licking.

As allolicking and self-licking are directed towards the same injured paw, one could argue 
that the decrease in demonstrator’s self-licking may be due to a passive interruption by 
observers’ allolicking. If this were the case, one would expect that, given the strong 
instinctive motivation for animals to self-lick their injury site, the demonstrators would 
frequently avoid allolicking from observers to resume self-licking. However, we found that 
in the vast majority of instances (88%), allolicking was voluntarily halted by observers, 
rather than passively avoided by demonstrators (Fig. 2l). This suggests that allolicking is not 
forced upon demonstrators but rather a proactive behavioral response from observers that 
leads to reduced need for self-licking in demonstrators.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 5

The perception of pain and local injuries in other animals likely involves multiple sensory 
modalities. These may include not only visual cues, such as self-licking of the demonstrator, 
but also olfactory cues (e.g. chemical signals released from the local injury site and 
pheromones released from other body parts) and textile cues (e.g. local tissue swelling). 
We did not observe obvious vocalizations during this prosocial interaction (Extended Data 
Fig. 5c, d). To directly assess whether witnessing others’ acute behavioral response to 
pain (self-licking) is required for the elicitation of allolicking by observers, we co-injected 
lidocaine with melittin to suppress melittin-induced pain (Fig. 2m). In the presence of 
lidocaine, the demonstrator exhibited a substantially lower level of self-licking (Fig. 2n), 
indicating a lower level of pain. Interestingly, the observer mice correspondingly displayed a 
considerably lower level of allolicking (Fig. 2o), and the demonstrator's self-licking and the 
observer's allolicking were positively correlated (Extended Data Fig. 5e-g). Thus, directly 
observing others’ pain responses promotes allolicking from observers.

To further investigate whether allolicking could also be elicited by local chemical and/or 
textile cues in the absence of demonstrators' self-licking, we examined allolicking towards 
melittin-injected demonstrators that were under sedation (Fig. 2p). The injury site in sedated 
demonstrators displayed typical responses to melittin injection, such as tissue swelling and 
inflammation (Extended Data Fig. 1a), but these animals did not exhibit any self-licking 
behavior. Interestingly, we found that allolicking could still be elicited towards the melittin-
injected paw of sedated demonstrators (Fig. 2q-s, Extended Data Fig. 5h). However, the 
onset latency of allolicking towards sedated demonstrators tended to be longer compared 
to that towards awake animals (Extended Data Fig. 5i). In addition, when interacting with 
an awake demonstrator, the observer could readily differentiate the injured paw from the 
uninjured one and initiate selective allolicking promptly (Extended Data Fig. 5j). However, 
when the demonstrator was sedated, the observer took longer to differentiate between the 
two paws before directing allolicking specifically towards the injured one (Extended Data 
Fig. 5k). Thus, while observers could perceive others’ injury likely through local chemical 
and/or textile cues, self-licking behavior provides an additional cue that allows the observers 
to readily locate the injury site and initiate targeted allolicking. Together, our results suggest 
that targeted allolicking towards the pain or injury site of others is a form of proactive 
helping response that can aid the recipient in coping with pain.

Encoding of others’ pain versus stress

To further examine the neural representations of pain in others and the resulting behavioral 
responses, we performed in vivo microendoscopic calcium imaging in the anterior cingulate 
cortex (ACC) of freely behaving animals (Fig. 3a-c). The ACC has emerged as an important 
brain area for the perception and social transmission of others’ pain2,3,22-24 and avoidance 
of harm to others25. However, whether and how the ACC may regulate targeted helping 
behavior in response to others’ pain is unclear. Specifically, how neural activity dynamics in 
the ACC may differentially respond to others in pain versus general stress and encode the 
subsequent helping and comforting behaviors remains elusive.

We first imaged observer mice when they freely interacted with naïve vs. melittin-injected 
demonstrators (Fig. 3d), and analyzed how individual ACC neurons responded when 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 6

observers closely investigated demonstrators in naïve or pain state. We identified subsets of 
ACC neurons that exhibited significant activation in response to naïve or pain-experiencing 
demonstrators (Fig. 3e-g). The majority of neurons in these two populations did not overlap 
(Fig. 3e-g, Extended Data Fig. 6a-e; Methods), suggesting that the ACC responds differently 
at the single-cell level to animals in naïve and pain states. Furthermore, investigations of 
naïve vs. pain-experiencing animals could be decoded significantly above chance using 
ensemble activity in the ACC (Fig. 3h, Extended Data Fig. 7a, b, k, l; Methods), suggesting 
that ACC activity can consistently distinguish others’ naïve and pain states at the population 
level.

The result that animals exhibit increased allogrooming towards both pain-experiencing 
and stressed animals (Fig. 1c-e, Extended Data Fig. 2-4) raises the question of whether 
animals simply perceive another’s pain as a stress signal. However, as allolicking is directed 
specifically towards pain-experiencing animals but not those experiencing general stress 
only (Fig. 1c-e, Extended Data Fig. 2-4), it is conceivable that animals can differentiate 
others’ pain vs. stress state. To examine this, we compared the neural representation of 
stressed demonstrators (exposed to acute restraint) vs. those in pain in the ACC (Fig. 3i, 
Extended Data Fig. 8a). Interestingly, demonstrators' stress and pain states activate largely 
distinct populations of ACC neurons (Fig. 3j-l, Extended Data Fig. 6f-j, 8c, d; Methods). 
These two cell groups were anatomically intermixed (Fig. 3k, Extended Data Fig. 8h). 
Notably, among the neurons activated by both animals in pain and those in stress, a fraction 
significantly higher than chance (87 out of 162 neurons, Fisher’s exact test, P < 0.0001, Fig. 
3j, Extended Data Fig. 8g) also responded to naïve animals. This suggests that a portion of 
the shared activation of other’s pain and stress is due to a general response to social stimuli. 
Nonetheless, a subset of neurons (75 out of 162 neurons) showed significant activation in 
response to other’s pain and stress, but not to other’s naïve state, suggesting that a fraction of 
ACC neurons may respond to a shared component of these two aversive states in others.

We further performed k-means clustering of all ACC neurons based on their activity 
dynamics during investigation towards demonstrators in naive, pain, and stress states. We 
found that ACC neurons can be grouped into distinct clusters (clusters 1–5) that exhibit 
preferential activation by each type of demonstrator, as well as a cluster (cluster 6) that 
generally responded to social targets (Fig. 3m, Extended Data Fig. 8c, d). Together, our 
findings suggest that the neural representation of others’ pain state in the ACC is partially 
distinct from that of the stress state (Supplementary Note 2).

Encoding of self- versus others’ pain

As animals respond to their own experiences and those of others with distinct behaviors 
(e.g. self-licking toward themselves versus allolicking toward others), self- and other-related 
pain likely elicits different neural representations. To investigate this, we analyzed single-
neuron responses in the ACC during the perception of others’ pain and experience of 
self-pain. Observers were presented with melittin-injected demonstrators, and then subjected 
to self-pain (induced by melittin injection into their own paws; Methods) (Fig. 3n, Extended 
Data Fig. 8b). We identified individual neurons that exhibited increased average activity 
when observers experienced self-pain (Methods). By comparing these cells with those 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 7

activated during close investigation of melittin-injected demonstrators, we found that the 
majority of activated neurons were selectively responsive to either self-pain or observation 
of others’ pain, but not both (Fig. 3o). Similarly, neurons activated during observers’ 
own self-licking (indicative of their response to self-pain) and those activated during 
observation of demonstrators’ self-licking (indicative of others’ response to pain) were 
largely non-overlapping (Extended Data Fig. 8j; Methods). Observers’ own self-licking and 
their observation of others’ self-licking can also be differentiated at the population level 
(Fig. 3p, Extended Data Fig. 7c). Thus, self- and other-related pain recruit distinct neural 
representations in the ACC.

While prosocial behavior requires differentiating others from oneself, the perception of 
others’ pain can evoke a similar negative state in the observer, which is thought to 
motivate the observer to take prosocial actions1,2,22,25. It has been hypothesized that this 
affective sharing may occur because witnessing others’ experience could generate a neural 
representation that resembles the neural representation of the observer’s own experience of 
that negative state2,23,26. Indeed, while the majority of neurons were selectively activated 
during self-pain or others’ pain, a fraction of neurons (8.7%) activated by others’ pain also 
responded to self-pain (Fig. 3o). To confirm that this overlap was not solely because self-
pain and others’ pain were triggered by the same stimulus (melittin), we induced self-pain 
using a distinct pain stimulus (electric shock). We found that although most of the activated 
neurons responded differentially during electric shock-induced self-pain experience and 
investigation of melittin-injected demonstrators, a subset of neurons still responded to both 
self- and others’ pain (Fig. 3q, Extended Data Fig. 6k-n; Methods).

We next asked whether population activity elicited by self- or others’ pain may predict 
the other state. Interestingly, models trained to decode others’ pain could also decode the 
experience of self-pain (Fig. 3s, Extended Data Fig. 7d), whereas they could not decode 
a self-regarding behavior (self-grooming) (Fig. 3v). Conversely, models trained to decode 
self-pain could also decode the perception of demonstrators in pain (Fig. 3t, Extended 
Data Fig. 7e), but not self-grooming or the perception of naïve demonstrators (Fig. 3u, w). 
Together, these findings suggest that while self- and other-related pain recruit distinct neural 
representations in the ACC, a fraction of self-pain-activated neurons are also recruited while 
perceiving others’ pain, and population activity in the ACC contains shared information that 
encodes both self- and others’ pain (Extended Data Fig. 7a).

Control of allolicking and allogrooming

To examine whether the ACC may play a causal role in regulating helping behavior 
towards others in pain, we performed chemogenetic inhibition of ACC neurons in observers 
by expressing the inhibitory DREADD hM4Di under a pan-neuronal promoter (Fig. 4a, 
b). CNO-injected observers exhibited a significant decrease in both targeted allolicking 
and general allogrooming towards melittin-injected demonstrators, as compared to saline-
injected observers (Fig. 4c-e). As a control, mCherry-expressing observers did not exhibit 
significant changes in allogrooming or allolicking upon CNO injection (Extended Data Fig. 
9a-d). This observed decrease in allolicking and allogrooming did not appear to be due to a 
general decrease in sociability or a general behavioral deficit, as inhibiting ACC neurons did 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 8

not affect close investigation behavior towards demonstrators (Fig. 4c-e), and the duration 
of allolicking or allogrooming during chemogenetic inhibition was not correlated to that of 
investigation (Extended Data Fig. 9e, f). Furthermore, in a three-chamber social preference 
assay, we found that chemogenetic inhibition of ACC neurons had no significant effect on 
animals’ preference for social targets (Extended Data Fig. 9g-i). These findings suggest that 
inhibition of ACC activity impairs allolicking and allogrooming in response to others’ pain 
and that this effect is not a secondary consequence of a disruption in general sociability. In 
addition, we found that hM4d silencing of ACC neurons also suppressed allolicking towards 
the injured paw of sedated animals (Extended Data Fig. 9j, k). This suggests that the ACC 
regulates allolicking towards both awake and sedated animals, consistent with the notion that 
both forms of allolicking represent behavioral responses to another's pain and/or injury.

To further investigate whether augmenting activity in the ACC can enhance these prosocial 
behaviors, we expressed ChR2 (channelrhodopsin-2) in ACC pyramidal neurons of observer 
mice (Fig. 4f, g). During observers’ interaction with melittin-injected demonstrators, light 
stimulation led to a significant increase in the probability of both targeted allolicking and 
general allogrooming (Fig. 4h, i, Extended Data Fig. 10a; Supplementary Note 3), indicating 
that ACC activation can enhance these prosocial behaviors. Furthermore, an increase in 
allolicking probability was evident during the initial period of the 3-minute light-on phase, 
although it was variable at the level of individual stimulation epochs (Extended Data 
Fig. 10a, e). Notably, similar to naturally occurring allolicking, optogenetically induced 
allolicking was targeted specifically to the injected paw but not the other paws (Fig. 4i), 
suggesting that the optogenetic induction of allolicking requires the presence of local pain 
in others. In contrast, optogenetic activation of ACC neurons did not increase the amount 
of observers’ investigation behavior during the entire light-on period (Extended Data Fig. 
10b) or the initial period (Extended Data Fig. 10f). Additionally, the level of allolicking 
or allogrooming was not correlated with that of investigation during stimulation (Extended 
Data Fig. 10c, d). These together suggest that activation of ACC neurons elicits a distinct 
effect on allolicking and allogrooming that did not depend on an increase in investigation 
(Supplementary Note 4). As a control, EYFP-expressing animals did not exhibit significant 
changes in allogrooming or allolicking upon optogenetic stimulations (Extended Data Fig. 
10g, h).

To examine whether the observed effects of the functional manipulations were specific to 
the ACC, we performed optogenetic activation of the neighboring prelimbic cortex (PrL) 
(Extended Data Fig. 10i, j). Unlike the ACC, activation of the PrL had no effect on 
either allolicking or allogrooming towards melittin-injected demonstrators (Extended Data 
Fig. 10k). To further determine whether the ACC might regulate observers’ self-licking in 
response to self-pain, we performed optogenetic stimulation of ACC neurons in subject mice 
injected with melittin. We found that ACC activation did not increase self-licking (Extended 
Data Fig. 10l, m), consistent with previous findings that loss-of-function of the ACC did not 
affect acute behavioral responses to self-pain, such as self-licking27. Together, these findings 
demonstrate a crucial role of the ACC in the co-regulation of these two distinct behavioral 
responses to others’ pain. This is reminiscent of the observation that naturally occurring 
allolicking and allogrooming towards animals in pain are correlated (Fig. 1p).

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 9

Separable coding of helping and comforting

While targeted allolicking and general allogrooming are co-modulated in both natural 
interactions and functional manipulations, they are also differentially regulated in a context-
dependent manner—allogrooming is directed towards both stressed and pain-experiencing 
demonstrators, while allollicking is elicited specifically towards demonstrators with local 
pain. These findings prompt the question of whether these two behaviors engage similar or 
different ACC neurons. K-means clustering of all ACC neurons identified clusters exhibiting 
increased activity during these behaviors (Extended Data Fig. 8e, f; Supplementary 
Note 5). Interestingly, allolicking and allogrooming activated largely non-overlapping 
ACC neurons; only 16.8% allolicking-activated neurons and 14.5% allogrooming-activated 
neurons exhibited significant activation during the other behavior (Fig. 5a-d, Extended 
Data Fig. 8e, f). These two groups of cells were anatomically intermixed in the ACC 
with no obvious spatial clustering (Fig. 5b, Extended Data Fig. 8i). Furthermore, linear 
decoders trained using ACC population activity could differentiate between allogrooming 
and allolicking bouts, with the time course of performance peaking during the execution of 
behaviors (Fig. 5e, f, Extended Data Fig. 7f). Thus, although allolicking and allogrooming 
are co-regulated by the ACC, they nonetheless recruit largely separate populations of ACC 
neurons and are associated with distinct population codes.

The observation that allogrooming occurs towards both stressed and pain-experiencing 
demonstrators further raises the question of how allogrooming towards others in pain 
is encoded compared to allogrooming towards stressed animals. One possibility is that 
behaviors towards animals in pain are more similar to each other compared to those 
towards stressed animals (Fig. 5g, left); alternatively, allogrooming towards different 
aversive states may show greater similarity compared to allolicking (Fig. 5g, right). To 
distinguish these possibilities, we performed principal component analysis of population 
activity during bouts of allolicking and allogrooming (Fig. 5h, Extended Data Fig. 8k). 
Interestingly, pair-wise Euclidean distances between allolicking and allogrooming events 
towards demonstrators in pain were significantly larger than those between allogrooming 
events towards demonstrators in pain and stress (Fig. 5i; Supplementary Note 6). This 
suggests that the distinction between the population code of allolicking and allogrooming is 
more prominent than the difference between those associated with allogrooming of different 
types of demonstrators.

Allolicking and self-licking share similar motor patterns, and allolicking towards others in 
pain can partially fulfill their need for self-licking. Meanwhile, these behaviors represent 
distinct responses to pain in others versus oneself. To investigate whether these behaviors 
are associated with similar or different neural representations in the ACC, we exposed the 
subject animals to melittin-injected demonstrators to induce allolicking, and subsequently 
administered melittin injections in the subjects themselves to elicit self-licking. We found 
that individual ACC neurons that were activated during allolicking or self-licking were 
largely non-overlapping (Fig. 5j-k), and that these two behaviors could be discriminated 
using decoding models trained on population activity (Fig. 5l, Extended Data Fig. 7g). 
Similarly, allogrooming and self-grooming could be classified based on population activity 
(Fig. 5m, Extended Data Fig. 7i). Therefore, wound licking directed towards others and 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 10

oneself are linked to distinct single-cell and ensemble responses in the ACC, in alignment 
with the differentiation of self versus others in prosocial behavior.

Allolicking and allogrooming represent proactive behavioral responses that are distinct 
from the mere perception of others’ pain. We therefore examined whether these behaviors 
are also represented in the ACC differently as compared to simply perceiving others’ 
pain. At the single-cell level, most neurons significantly activated during allolicking 
(83.0%) or allogrooming (73.4%) did not show activation during close investigation (Fig. 
5n, o, Extended Data Fig. 8l, m), suggesting that neural responses observed during 
allolicking and allogrooming are not simply elicited by sensory cues. Additionally, decoders 
constructed using population activity could discriminate close investigation from allolicking 
or allogrooming (Fig. 5p, q, Extended Data Fig. 7h, j, 8n). Collectively, these findings 
indicate that the neural representations of allolicking and allogrooming in the ACC are 
distinct from each other and from that of perceiving others’ pain.

Discussion

In nature, animals evolve instinctive behavioral strategies, such as self-licking of wounds, 
to cope with pain and injuries14. Here, we found that mice display robust allolicking 
specifically towards the injury site of others, which serves as a targeted helping behavior 
that supports others’ goal of coping with local wound or pain. While previous studies 
have utilized a few paradigms of helping behavior in rodents9,25,28, they typically require 
training animals to perform an artificial behavior over multiple days9,25,28, and/or the 
learned behavior may be elicited by factors unrelated to the needs of conspecifics29. As 
the paradigm reported here focuses on an ethologically relevant behavior (allolicking) that is 
naturally observed in the wild, it reflects a direct, likely innate, response to a specific need 
of others that requires no training. It provides a relatively rapid and easy-to-implement assay 
for investigating innate helping behavior.

Although previous studies examined behavioral responses to other individuals in pain17, 
allolicking behavior was not investigated separately, and it remained unclear whether there 
was a specific increase in allolicking directed at the injury site (Supplementary Note 1). Our 
approach enabled us to differentiate between two types of observers’ behaviors—targeted 
allolicking vs. general allogrooming—towards others experiencing pain. Previous studies 
have shown that allogrooming can be elicited by another’s general state of stress19,30. 
While allogrooming can also be elicited by ongoing pain, targeted allolicking is specifically 
displayed in response to local injury, suggesting that mice are capable of perceiving 
the specific states and needs of others and displaying prosocial behaviors in a context-
appropriate manner (Fig. 5r). The perception of local injury or pain in others is likely 
mediated by multiple sensory cues, including observation of the demonstrators’ self-licking 
behavior and local chemical and/or textile cues. Of note, targeted allolicking is a proactive 
behavioral response that is distinct from the phenomenon of social transfer of pain, in 
which animals passively increase pain sensitivities themselves following an interaction with 
pain-experiencing individuals22,31. Future research should examine the potential connections 
between these two processes.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 11

Echoing our finding that a general stress state vs. ongoing local pain in others elicit different 
behavioral responses from observers, we found that a subset of ACC neurons responded 
differentially to these two states. This is consistent with previous findings that rat ACC 
neurons activated when witnessing others receiving foot-shock are partially distinct from 
those of a conditioned fear state23. Moreover, although a subset of rat ACC neurons were 
active both during self-pain and when observing others’ pain without direct social contact23, 
it was unclear whether this reflects the encoding of self-pain versus other’s pain in direct 
interactions when animals respond to others’ pain with allolicking. We showed that during 
prosocial interactions in mice, the neural representations of self and others’ pain in the 
ACC involve both distinct and shared encoding (Extended Data Fig. 7a). This differential 
representation of self- and other-related pain is consistent with the self-other differentiation 
in prosocial behavior, while the shared encoding of these two states might play a role 
in the generation of a negative emotional state in oneself when witnessing the pain of 
others2,23,26,32.

In addition, we found that targeted allolicking is not only encoded in the ACC but also 
bidirectionally regulated by this brain region. The ACC is involved in comforting behavior 
towards emotionally stressed conspecifics in rodents30,33 and decision-making in prosocial 
contexts in non-human primates34,35 and rats25. Here, our data demonstrate a distinct role 
of the ACC in regulating both targeted allolicking and general allogrooming towards others 
in pain, beyond the initial perception of others’ state. The co-modulation of allolicking and 
allogrooming during functional manipulations, which echoes the strong correlation between 
these behaviors in natural conditions (Fig. 1p), might reflect a common motivational drive 
that promotes both behaviors in response to others in pain. However, these two behaviors 
are also differentially regulated in a context-dependent manner and are associated with 
separable neural representations in the ACC at both single-cell and population levels (Fig. 
5r). Interestingly, this is reminiscent of previous findings that comforting and helping 
behaviors in young children are correlated with distinct brain activation patterns as revealed 
by electroencephalogram36.

Collectively, our study advances our understanding of how the brain represents others’ 
negative states and regulates the expression of appropriate helping behavior to address 
others’ specific states and needs. These insights could aid the development of interventions 
that promote context-appropriate prosocial behavior in health and disease.

Care and experimental manipulations of all animals were carried out in accordance with 
the NIH Guide for Care and Use of Laboratory Animals and approved by UCLA IACUC. 
Animals were housed in 12 h light-dark cycle (10 p.m. – 10 a.m. light), with food and 
water available ad libitum. All experiments were performed during the dark cycle of the 
animals in a dark room illuminated by infrared or red light. For characterization of prosocial 
interaction between observer mice and demonstrator mice, 12-16-week-old male and female 
C57BL/6J mice purchased from Jackson Laboratories (stock No.: 000664) were used. 
For microendoscopic calcium imaging and chemogenetic and optogenetic experiments, 

Nature. Author manuscript; available in PMC 2025 February 01.

Methods:

Animals

 
 
 
 
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

Zhang et al.

Page 12

C57BL/6J males purchased from Jackson Laboratories (stock No.: 000664) were used. 
Animals used for stereotaxic surgery were 8-12 weeks old.

Stereotaxic surgeries

Mice were anesthetized with isoflurane and mounted on a stereotaxic device. Anatomical 
coordinates of brain regions of interest were determined based on Paxinos and Franklin’s 
the Mouse Brain in Stereotaxic Coordinates atlas. The ACC targeted in chemogenetics, 
optogenetics, and imaging experiments encompassed both the Cg1 and Cg2 subregions.

For optogenetic activation of ACC or PrL neurons, AAV2-CamKIIɑ-ChR2-EYFP 
(University of North Carolina vector core) was injected bilaterally at AP (anterior-posterior) 
1.0, ML (medial-lateral) ±0.25, DV (dorsal-ventral) −1.8 relative to the bregma for the ACC, 
and AP 1.7, ML ±0.25, DV −1.8 for the PrL, with 400nL at each site. Ferrule fiber-optic 
cannulas (200 μm core diameter, 0.37 numerical aperture; Inper) were then implanted 0.4 
mm above the viral injection sites, with a 15-degree angle on the left side. Following the 
surgeries, we allowed the mice to recover for four weeks before conducting behavioral 
testing.

For chemogenetic inhibition of ACC neurons, AAV5-hSyn-hM4Di-mCherry (Addgene, 
Catalog # 50475-AAV5) was injected. Given that the ACC covers a relatively large area 
along the AP axis, we injected 750 nL total of the AAV (per hemisphere) bilaterally at 
multiple sites (AP 0.0/1.0/2.0, ML ±0.3, DV −1.8 and AP 2.0, ML ±0.3, DV −1.5) along this 
axis to ensure effective inhibition. Following the surgeries, we allowed the mice to recover 
for four weeks before conducting behavioral testing.

For microendocopic calcium imaging of ACC neurons, we injected 500 nL total AAV1-
hSyn-GCaMP6f (Addgene, Catalog # 100837-AAV1) at AP 1.0, ML 0.3, DV −1.8 and 
−1.6. One week after the viral injection, a 1.1-mm (diameter) circular craniotomy was 
created at AP 1.0, ML 0.55, and the tissue above the injection site was carefully aspirated 
using a 28-gauge needle. A 1.0-mm (diameter) GRIN (gradient refractive index) lens (4.0 
mm in length; Inscopix) was then implanted at AP 1.0, ML 0.5, and DV −1.6. After lens 
implantation, mice were singly housed for three to four weeks before a base plate was placed 
on top of the lens. Individual animals were then co-housed with other C57BL/6J mice before 
imaging experiments.

Behavior assays

Prior to behavioral testing, animals were extensively habituated to human handling 
procedures and to the behavior setup for at least four consecutive days. Behaviors were 
recorded using Point Grey cameras (FLIR) at 20 frames per second. Side-view and 
bottom-view videos were synchronously recorded using the StreamPix software (NorPix). 
Behavioral videos were manually annotated for different behaviors in a frame-by-frame 
manner using custom MATLAB code (https://github.com/pdollar/toolbox). Both side-view 
and bottom-view videos were examined simultaneously to ensure accurate annotation of 
allolicking and allogrooming behaviors. Targeted allolicking was defined as visible licking 
by an observer mouse that was directed towards the melittin- or saline-injected paw of 
another mouse. Allogrooming was defined as visible licking and/or mouth contact localized 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 13

on the body trunk, shoulder region, and head of another mouse, during which the actor 
mouse shows head bobbing indicative of licking motions. Close investigation was defined as 
an actor mouse orienting its snout towards another mouse and positioning itself within half a 
head length of the other mouse.

Social interaction with demonstrators in pain.—Same-sex pairs of age-matched 
C57BL/6J mice (12-16 weeks old) were cohoused for more than three weeks before the 
behavioral test. The test was conducted in a cage with a transparent bottom, and the bedding 
was removed to enable video recording from a bottom review. While observing allolicking 
towards the injected paws was challenging from the side or top view, the bottom-view 
camera allowed us to clearly visualize it. To minimize potential stress caused by this 
experimental setup, mice were habituated in the testing cage for four consecutive days, with 
the duration of habituation gradually increasing from 30 minutes on day 1 to ~two hours 
on day 4. On the day of testing, mice were first habituated in the testing cage for 1.5 hours 
before the behavior test was conducted. One mouse in each pair was randomly assigned as 
the demonstrator and the other as the observer. For the control test, the demonstrator was 
removed from the cage, subcutaneously injected with 20 μL saline into one plantar hind paw, 
and then returned to the testing cage. On the second day, the demonstrator was injected with 
either 20 μL of 1mg/ml melittin (Sigma-Aldrich Catalog # M2272, diluted in saline) or 5% 
formalin (Sigma-Aldrich Catalog # 8187081000, diluted in saline) into the other plantar hind 
paw before being reunited with the observer. Behaviors during the 30-min period following 
the reunion were recorded and analyzed. Melittin and formalin are known to elicit pain 
through different molecular and cellular pathways and result in different temporal patterns 
of pain response18,20,37,38. Formalin typically induces pain responses that consist of an 
early phase (~ 0-5 min after injection) and a late phase (~15-30 min after injection), as 
well as slow but long-lasting tissue edema (~30 min to two weeks after injection)37. On 
the other hand, melittin acutely induces a continuous pain response that last ~30-60 min, 
with a relatively short period of tissue edema (~ 5 min to 48 hrs after injection)18. We 
found that the increase in targeted allolicking towards melittin-injected demonstrators was 
more pronounced compared to that towards formalin-injected animals (Fig. 1h and Extended 
Data Fig. 3f), possibly due to the sustained pain response and rapid tissue inflammation. In 
addition, the faster recovery after melittin injection leads to less suffering to animals.

For the analysis of the correlation between the duration of allolicking, allogrooming, and 
investigation behaviors towards demonstrators in pain (Fig. 1p-s), we combined 12 mice 
from the assay described above (Fig. 1a-m) and 24 mice from a separate experiment that 
examined the demonstrators’ self-licking behavior in the presence or absence of observers 
(Fig. 2a-e; see the “Demonstrators’ self-licking behavior in the presence or absence of 
observers” section below). We were able to incorporate data from the second experiment 
as the analysis in Fig. 1p-s only examined observers’ behaviors when they interacted with 
melittin-injected demonstrators and did not involve comparison to saline-injected controls.

To examine fine head movements during allolicking and allogrooming, head angles were 
measured using a high-precision gyroscope attached to the microendoscope used for calcium 
imaging (see the “Microendoscopic calcium imaging” section below). Raw quaternions 
measuring three-axial orientations were converted to Euler angles at each time point and 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 14

aligned with behavior annotations to identify the onsets and offsets of behavioral events. The 
signal was processed using a high-pass filter to eliminate noise with a frequency lower than 
1.5Hz. Either the pitch or roll angle was used to represent the head angle (depending on 
the orientation of the microendoscope relative to the head of the animal) and calculate the 
power spectrum during allolicking and allogrooming presented in Fig. 1n-o. Quantification 
of averaged power between 2-6 Hz shows a significant difference between the two behaviors 
(Two-sided Wilcoxon rank-sum test. P < 0.0001). 71 allolicking bouts and 63 allogrooming 
bouts from 4 animals imaged during social interaction with demonstrators in stress and 
demonstrators in pain were used for the analysis. Only bouts longer than 3 seconds were 
included.

Vocalizations emitted during prosocial interactions were recorded using an ultrasound 
recording device (UltraSoundGate 116H) and a microphone (CM16) placed above the 
testing cage. The behavior video was synchronized with the audio recording, and 
annotations of the observers’ behaviors were aligned with the audio signals. 13 animal 
pairs were recorded, and no obvious vocalizations were detected. As a positive control, when 
postnatal day 5 pups were placed in the testing cage, frequent vocalizations were captured.

For the examination of social interaction after co-injection of lidocaine and melittin into 
demonstrators (Fig. 2m-o), pairs of age-matched male C57BL/6J mice (12-16 weeks old) 
were cohoused and habituated to the experimental setup as described above. On the day of 
testing, 10 μl 4% lidocaine (Thermo Fisher Scientific, Catalog # J6303514, diluted in saline) 
or saline was injected into one hind paw of the demonstrator. After 5 minutes, a mixture 
of 20 μl 1mg/ml melittin and 2% lidocaine or 20 μl 1mg/ml melittin alone was injected 
into the same plantar hind paw. The demonstrator was then returned to the testing cage 
to reunite with the observer. Behaviors displayed during the first 15 minutes following the 
reunion were recorded and analyzed. After 15 mins, the pain-suppressing effect of lidocaine 
diminished in demonstrators co-injected with melittin and lidocaine, as indicated by an 
increase in self-licking behavior. Consequently, behaviors observed after 15 minutes were 
not included in the analysis.

To assess the relationship between dominance status and prosocial behaviors (Extended Data 
Fig. 1j-m), pairs of age-matched male C57BL/6J mice (12-16 weeks old) were cohoused, 
habituated to the experimental setup, and tested in the prosocial interaction assay following 
melittin injection as described above. One day before the prosocial interaction assay, the 
dominance relationship within each animal pair was determined using the tube test39,40. 
The two animals were placed at opposite ends of a closed acrylic tube (length 60 cm; 
circumference 2.5 cm) and the first animal to retreat out of its end of the tube was designated 
as the loser and the other animal the winner. The assay was repeated three times and the 
animal that won at least two out of three times was considered dominant and the other 
animal subordinate. The animals were habituated to the tube for two days before the tube 
test.

Social interaction with sedated demonstrators.—Same-sex pairs of age-matched 
C57BL/6J mice (12-16 weeks old) were cohoused and habituated to the experimental 
setup as described above. On the day of testing, one animal in each pair was randomly 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 15

selected as the demonstrator and the other as the observer. The demonstrator first received 
intraperitoneal injection of a sedative, dexmedetomidine (0.8 mg/kg body weight; Sigma-
Aldrich Catalog # SML0956), and then returned to the testing cage. 30 minutes later, the 
demonstrator was subcutaneously injected with 20 μL saline into one hind paw and 20 μL 
1mg/ml melittin into the other hind paw. To rule out the possibility that the differences in 
observer behaviors towards the two injected paws were due to different odors of the injected 
solutions, 3 μL saline was applied to the surface of the paw injected with melittin and 3 
μL melittin was applied to the surface of the paw injected with saline. The demonstrator 
was then placed in the corner of the testing cage, with both saline- and melittin-injected 
paws fully exposed and accessible by observers. Behaviors were recorded for 30 min. The 
observers’ allolicking behavior towards the injured paw of sedated demonstrators displayed 
motor characteristics similar to that towards awake demonstrators. As the primary focus 
of this experiment is to distinguish allolicking towards melittin- vs. saline-injected paws, 
allogrooming towards other body parts was not analyzed.

We found that while observers initiated allolicking towards sedated demonstrators with a 
delayed onset compared to awake ones, this behavior was displayed at similar levels during 
the later stage of the interaction (Fig. 1d, h, l and Fig. 2q-s). This may be due to the 
absence of self-licking and other active behaviors in sedated demonstrators, which could 
lead to increased exposure of the injury site to observers. Similarly, although sedation 
and co-injection of lidocaine both lead to decreased or absent self-licking, they generate 
two fundamentally distinct states in demonstrators—demonstrators treated with lidocaine 
exhibited more natural behaviors due to pain relief, which likely results in less exposure of 
the injury site and/or reduced receptivity to allolicking (Fig. 2m-o).

Social interaction with stressed demonstrators.—Same-sex pairs of age-matched 
C57BL/6J mice (12-16 weeks old) were cohoused and habituated to the experimental setup 
as described above. To examine if the animals display any allolicking in this experiment, 
the test was also conducted in a cage with a transparent bottom, so that we could visualize 
the behavior using a bottom-view camera. On the day of testing, one animal in each pair 
was randomly assigned as the demonstrator and was removed from the cage and kept in 
a restrainer for 15 min. In control experiments, the demonstrator was placed in a separate 
cage for 15 min. The mice were then reunited, and behaviors were recorded for 20 min. 
Control experiments were performed one day before the restraint experiments. While the 
observers displayed a significantly increased amount of allogrooming towards stressed 
demonstrators compared to unstressed controls, the total duration of allogrooming towards 
stressed demonstrators in this experiment appeared to be lower compared to that observed in 
our previous study where the experiments were carried out in the home cage19. This is likely 
due to the fact that in the current study, the animals were tested in cages without bedding 
materials, which presents a distinct environment from the home cage.

Demonstrators’ self-licking behavior in the presence or absence of observers.
—To investigate self-licking behavior in demonstrator mice towards their melittin-injected 
paws in the presence of observer mice, we used the procedures outlined in "Social 
interaction with demonstrators in pain". For the evaluation of self-licking behavior in the 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 16

absence of observers, demonstrators remained in the testing cage following melittin injection 
with no observers present. To minimize the effects of testing order, we randomly assigned 
half of the demonstrators to be tested initially with observers present and the other half 
without. After a week, the groups were switched, and the animals were re-tested under the 
opposite conditions. Behaviors during the 30-minute period after melittin injection were 
recorded and analyzed. For the quantification of the normalized amount of self-licking in 
Fig. 2e, the duration of self-licking in the presence of observer mice was normalized to 
the duration of self-licking in the absence of observer mice. The period between 5 and 
15 minutes after melittin injection, during which the demonstrators showed a high level of 
self-licking behavior (Extended Data Fig. 1d), was used for this quantification.

Demonstrators’ self-licking behavior during allolicking or allogrooming by 
observers.—For the quantification of the probability of self-licking during different time 
periods (Fig. 2f) and characterization of the temporal dynamics of self-licking during 
allolicking (Fig. 2h-k), we included 30 animals (12 animals shown in Fig.1 and 18 animals 
shown in Fig. 2b) that showed a relatively high level of allolicking and allogrooming 
behaviors (total duration of allolicking and allogrooming ≥ 50 s). Six animals shown in 
Fig. 2b displayed a low level of allolicking and allogrooming behaviors (total duration of 
allolicking and allogrooming < 50 s), which precluded reliable quantification of self-licking 
during these behaviors; these animals were not included for this analysis. In Fig. 2f, we 
calculated the percentage of time that demonstrators displayed self-licking behavior during 
time periods when demonstrators exhibited allolicking, allogrooming, or neither of these 
behaviors. In Fig. 2h and 2j, the onset of each allolicking bout towards injured or uninjured 
paws was defined as time 0, and the probability of self-licking between 2 s before and 5 
s after time 0 was calculated for each bout. Only bouts longer than 2 seconds in which 
the demonstrator was displaying self-licking behavior at 0.1 s before allolicking onset were 
included. Among the 30 mice tested, 85 allolicking bouts toward the injured paw from 24 
animals and 18 allolicking bouts toward uninjured paws from 11 animals met this criterion 
and were included in this analysis. Traces in Fig. 2h and 2j reflect averaged values across 
all bouts. The fraction of reduction in self-licking was calculated as 1 – the averaged area 
under curve per second between 0-5 s following allolicking onset. The control data (grey 
curves) were generated by randomly permuting the annotation of allolicking behavior in 
each experiment in a circular manner for 1000 iterations.

Optogenetic experiments

Prior to an experiment, a ferrule patch cord was coupled to the ferrule fiber implanted in 
the observer mouse using a zirconia split sleeve (Doric Lenses). Optic fibers were connected 
using an FC/PC adaptor (Doric Lenses) to a 473-nm blue laser (CNI Laser). An Arduino 
micro-controller board and a customized MATLAB program were used to control light 
pulses.

To examine social interaction with demonstrators in pain, mice were habituated to the testing 
cage and optic fibers for four consecutive days before testing. Demonstrator mice were 
injected with 20 μL of 1mg/ml melittin in one hind paw and subsequently returned to the 
testing cage. The optogenetic stimulation protocol started one minute after reuniting the 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 17

mice. 473 nm laser was delivered at 20 Hz, with 15 ms pulses for 3 minutes, followed by a 
3-min light-off period. The light irradiance was 0.4-0.8 mW mm−2 in the target region. We 
used this relatively low level of laser power to avoid potential abnormal behavioral responses 
in subject animals, such as immobility or seizure. This light-on/light-off cycle was repeated 
five times in each session, with a total duration of 30 minutes. Out of the 18 subject animals 
included in Fig. 4i, five were tested across two sessions (30 minutes each), with the averaged 
results shown in the figure. The other 13 animals underwent one session.

To examine the effect of ACC activation on self-licking, mice were habituated to the testing 
cage and optic fibers for four consecutive days before testing. On the day of testing, the 
subject mice were injected with 20 μl 1mg/ml melittin in one hind paw and returned to 
the testing cage. The optogenetic stimulation protocol was the same as delineated above 
and started one minute after returning subject mice to the testing cage. The duration and 
bout number of self-licking were quantified and compared between the light-on and light-off 
periods.

Optogenetic experiments require the attachment of optic fibers, which introduces a certain 
degree of physical constraint on the animals and makes it harder for observer mice to 
allolick the injured paw. Animals were pre-tested with optic fibers attached and those that 
did not show any baseline allogrooming and allolicking behavior (6 out of 24 mice) were not 
included in the subsequent manipulation experiments.

Note that the amount of behavior in the optogenetic activation and chemogenetic inhibition 
experiments (see the following section) is not directly comparable. In the optogenetic 
experiments, behaviors were quantified over either the light-on or light-off periods, which 
had a cumulative duration of 15 minutes. In contrast, in the hM4Di experiments, behaviors 
during the entire 30 minutes were quantified. In addition, the use of optic fibers in 
optogenetic experiments likely leads to reduced baseline allolicking behavior compared to 
the saline control in the chemogenetic experiments (Fig. 4d, e, i; Supplementary Note 3).

Chemogenetic experiments

Social interaction with demonstrators in pain.—The mice were acclimated to the 
experimental setup following the protocol outlined in the "Behavior assays" section. In 
addition, the subject mice were habituated to human handling and intraperitoneal injection 
by receiving injection of 0.2 mL saline daily for four consecutive days. On the day of 
testing, the subject mouse (observer) was injected with 1% DMSO in saline (as control) 
or CNO41 (5 mg/kg body weight; Enzo, Catalog # BML-NS105) diluted in saline with 
1% DMSO 35 minutes before the behavior test. Next, 20 μL 1 mg/mL melittin was 
injected into one hind paw of the demonstrator mouse, and the two mice were reunited. 
Behaviors were recorded for 30 minutes following the reunion. The order of the control 
and CNO experiments was counterbalanced across the subject animals, with half of the 
animals undergoing the control condition first, followed by the CNO condition, and the other 
half tested with the reverse order. The control and CNO experiments were separated by 
one week. In each experiment, a different hind paw of the demonstrator was injected with 
melittin.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 18

Social interaction with sedated demonstrator.—The mice were acclimated to the 
experimental setup following the protocol outlined in the "Behavior assays" section. The 
subject mice were habituated as described above. On the testing day, the demonstrator 
was sedated via intraperitoneal injection of dexmedetomidine (0.8 mg/kg body weight) and 
returned to the testing cage. 5 minutes later, the subject mouse (observer) was injected with 
1% DMSO in saline (as control) or CNO (5 mg/kg body weigh) diluted in saline with 1% 
DMSO. After 30 minutes, 20 μl 1 mg/mL melittin was injected into one hind paw and 20 
μl saline into the other hind paw of the sedated demonstrator. 3 μL saline was applied to the 
surface of the paw injected with melittin and 3 μL melittin was applied to the surface of the 
paw injected with saline. After 5 minutes, the demonstrator was returned to the testing cage 
and the two hind paws were exposed. Behaviors were recorded for 30 minutes following 
reunion. One week later, the experiments were repeated, with the control and CNO groups 
reversed as outlined above.

Three-chamber social preference assay.—The assay was performed in a three-
chamber apparatus consisting of two side chambers (25 cm × 25 cm) and a center chamber 
(12.5 cm × 25 cm). Before the test, mice were habituated in the apparatus with an empty 
wire cup in each of the side chambers for three days. On the day of testing, the subject 
mouse was injected with CNO (5 mg/kg body weight) 30 minutes before the behavior assay. 
The mouse was then allowed to explore the three chamber freely for 10 minutes, with an 
empty cup in each of the side chambers. Next, an unfamiliar, same-sex mouse was placed 
under the cup in one of the chambers (designated as the social chamber), and the subject 
mouse was allowed to freely explore the three chambers for another 10 min. The social 
chamber was randomly chosen in a counterbalanced manner across all subject animals. 
Behaviors were recorded from the top view and SLEAP software (https://sleap.ai/)42 was 
used to track animals after the experiments. The social preference score was calculated as 
(time spent in the social area – time spent in the non-social area)/ (time spent in the social 
area + time spent in the non-social area). The social and non-social areas were defined as the 
quarter of the side chambers with the mouse-containing cup and the empty cup, respectively.

Histology

Animals were perfused with 20 mL PBS and 20 mL 4% paraformaldehyde. The brains 
were dissected and post-fixed with paraformaldehyde overnight at 4°C. Then the brains were 
dehydrated in 20% sucrose overnight at 4°C. 60 μm sections were cut using a Leica CM1950 
cryostat. Images were acquired using a Leica DM6 B microscope.

Microendoscopic calcium imaging

Behavior assays—Imaging experiments were performed at least seven days after 
the base plate was placed. Mice were habituated to human handling procedures, the 
microendoscope, and the experimental setups for at least four days before imaging 
experiments. Calcium fluorescence videos and behavior videos were simultaneously 
recorded using a microendoscope (UCLA Miniscope V4, purchased from Open Ephys; 
https://github.com/Aharoni-Lab/Miniscope-DAQ-QT-Software) and video cameras (from 
side and bottom views), respectively. The microendoscopes were connected to a digital 
acquisition device (DAQ) through a flexible, ultra-light coaxial cable. Behavior videos 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 19

were annotated by a human annotator frame by frame to identify onset and offset times 
of individual behaviors exhibited by the subject animals, including close investigation, 
allolicking, allogrooming, and self-grooming.

Social interaction with naive demonstrators and demonstrators in pain.: In each 
experiment, each subject animal was presented with 2-4 familiar animals in total, with 
a ~5-min interval between two successive presentations. Each demonstrator animal was 
presented twice—firstly in naïve state and subsequently after melittin injection (20 μL 1mg/
ml). During each presentation, the subject animal was allowed to freely interact with the 
demonstrator animal for ~5-10 min.

Social interaction with demonstrators in stress and demonstrators in pain.: In each 
experiment, each subject animal was presented with two familiar cage mates in total, with 
a ~5-min interval between two successive presentations. Each demonstrator animal was 
presented three times—firstly in naïve state, secondly after 15-min restraint stress, and lastly 
after melittin injection (20 μL 1mg/ml). After the second presentation (restraint stress), the 
demonstrators were allowed to recover from the stress state in the home cage for 30 minutes 
before melittin injection. During each presentation, the subject animal was allowed to freely 
interact with the demonstrator animal for ~5-10 min.

Experiences of self-pain and pain in others.: In each experiment, each subject animal 
was presented with two familiar cage mates in total, with a ~5-min interval between two 
successive presentations. Each demonstrator animal was presented twice—firstly in naïve 
state and subsequently after melittin injection (20 μL 1mg/ml). During each presentation, the 
subject animal was allowed to freely interact with the demonstrator animal for ~5-10 mins. 
To examine neural activity during ongoing self-pain, the subject animal was subsequently 
transferred to a foot-shock chamber and received 9 foot-shocks (2 s, 0.4 mA) with a 
random interval between 20 s and 40 s. As our population activity analysis necessitates 
multiple trials of pain experiences (see the section “Analysis of population dynamics” 
below), we induced self-pain using foot-shock, which is a common method to induce acute 
pain experiences and allows for multiple deliveries with well-defined onset within one 
experiment. As foot-shock- and melittin-induced pain experiences likely involve distinct 
sensory stimuli, we also examined neural activity during melittin-induced self-pain and 
self-licking behavior. To this end, the subject animal was subsequently injected with melittin 
into the hind paw (10 μL 1mg/ml). The neural activity and behavior of the subject animal 
during the ~10 min after the melittin injection were analyzed.

For the analyses presented in Fig. 3i-w and Fig. 5, we used cage mates as demonstrators 
for all the experiments. The animals were co-housed for at least three weeks following 
base plate attachment, and we carefully monitored the animals during co-housing to ensure 
that there was no damage to the GRIN lens implanted on the observer mice. For the 
analyses presented in Fig. 3d-h, as we used up to four demonstrator animals, we also used 
familiar, non-cage mate animals. We familiarized the observer animals with the non-cage 
mate demonstrators by allowing them to freely interact for 30 minutes per day for at least 3 
consecutive days prior to conducting the imaging experiments.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 20

Similar to optogenetic experiments, the attachment of the miniature microendoscope device 
introduces a certain degree of physical constraint on the animals and makes it harder for 
the observer mice to allolick the injured paw of the demonstrators. Therefore, following the 
presentation of each melittin-injected demonstrator, we also included an additional 10-15 
min session during which observer animals were presented with the same melittin-injected 
demonstrator under sedation, as the injured paws in sedated animals were more easily 
accessible to the observers. Allolicking events towards the injured paws of both awake and 
sedated demonstrators were combined for the analyses shown in Fig. 5 to enhance statistical 
power. Allolicking towards both awake and sedated demonstrators injected with melittin was 
selectively targeted at the injured paw (Fig. 2q-s), displayed similar motor characteristics, 
and required the activity of the ACC (Extended Data Fig. 9j), suggesting that allolicking 
in both scenarios represents a behavioral response to another's pain and/or injury. In the 
analysis presented in Fig. 5h, i, allogrooming towards pain-experiencing demonstrators 
included events directed at awake, melittin-injected demonstrators. We obtained qualitatively 
similar results when allogrooming towards sedated, melittin-injected demonstrators was 
used for this analysis (Supplemental Note 6). For the analyses of neural responses associated 
with the perception of different types of demonstrators in Fig. 3, interactions with sedated 
demonstrators were not included.

Extraction of calcium signals—Calcium fluorescence videos were recorded at 30 Hz. 
Raw videos from each imaging session were processed using an integrated Miniscope 
Analysis package (https://github.com/etterguillaume/MiniscopeAnalysis). Briefly, raw 
videos were first processed using the NormCorre algorithm (https://github.com/
flatironinstitute/NoRMCorre)43 for motion correction. Motion corrected videos were 
then processed using Constrained Non-Negative Matrix Factorization (CNMF-E, https://
github.com/zhoupc/CNMF_E)44 to isolate cellular signals and associated regions of interest 
(ROI). Δ F/F calcium traces of individual cells were z-scored and presented throughout in 
units of standard deviation (s.d.) prior to downstream analysis. As CNMF-E can identify 
fluorescence changes from non-neuronal sources, such as motion artefacts or neuropil 
signals, we manually inspected extracted ROIs and traces to remove ROIs that lacked a 
soma-like shape and/or showed signs of motion artefacts in their traces.

Analysis of single-cell responses

Response to naive demonstrators versus demonstrators in pain (Fig. 3e-g).: We obtained 
a total of 4120 neurons from 11 independent imaging experiments in 11 subject animals 
(375 ± 161 neurons from each animal, mean ± SD). To examine how naïve demonstrators 
and demonstrators in pain may be differentially repressented in the ACC, we examined 
the responses of individual neurons during close investigation towards these two types 
of demonstrators. We used an ROC (receiver operating characteristic) analysis39,45 to 
identify neurons that significantly respond during each type of investigation event. A binary 
threshold was applied to the Δ F/F signal to classify each time point as showing or not 
showing a particular event. The true positive rate and false positive rate of detection were 
calculated over a range of binary thresholds spanning the minimum and maximum values 
of the neural signal and used to construct an ROC curve that describes how well the neural 
signal detects each event at different thresholds. The area under the ROC curve (auROC) 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 21

was then calculated as a measure of how strongly neural activity was modulated by each 
event. The observed auROC was compared to a null distribution generated by circularly 
permuting the calcium signals by a random time shift 200 times. A neuron was considered 
significantly responsive (α < 0.05) if its observed auROC value was above the 97.5th 
percentile (activated) or below the 2.5th percentile (suppressed) of the null distribution. Only 
time points annotated as the behavior event of interest and times points annotated as baseline 
(not exhibiting any of the annotated behaviors) were included for this analysis, so that the 
identification of cells responsive to a particular behavior was not influenced by their activity 
during other types of behavior.

Response to demonstrators in stress versus demonstrators in pain (Fig. 3j-m).: We 
obtained a total of 4388 neurons from 10 independent imaging experiments in 10 subject 
animals (439 ± 67 neurons from each animal, mean ± SD). Individual neurons that 
were significantly responsive during close investigation towards demonstrator in stress or 
demonstrators in pain were identified using the ROC analysis described above.

Response to experience of self-pain versus pain in others (Fig. 3o, q, r, Extended Data 
Fig. 8j).: We obtained a total of 2399 neurons from 6 independent imaging experiments in 
6 subject animals (400 ± 77 neurons from each animal, mean ± SD). To identify neurons 
that show increased average activity following melittin injection (Fig. 3o), we first computed 
the average activity increase of individual neurons between 0.5 to 2.5 minutes following 
melittin injection compared to the baseline activity, which was calculated as averaged 
activity between 1.5 to 3.5 minutes before melittin injection. During the baseline period, 
the subject mice remained isolated in the testing cage in the absence of demonstrators. We 
next generated null distributions by applying a random time shift to the activity trace of each 
neuron through circular permutation. A neuron was considered to exhibit increased average 
activity following melittin injection if the observed activity increase exceeded the 95th 
percentile of the null distribution. These neurons were then compared to neurons activated 
during close investigation towards demonstrators in pain (defined based on ROC analysis 
outlined above).

To compare neurons activated during the observation of demonstrators’ self-licking behavior 
and the observers’ own self-licking behavior (Extended Data Fig. 8j), we considered the 
observer animal to be observing another’s self-licking behavior when it was oriented 
towards the demonstrator during the demonstrator’s self-licking behavior and the distance 
between the animals was within half a head-length. Neurons significantly activated during 
observation of others’ self-licking or the observers’ own self-licking were then defined using 
the ROC analysis as described above.

To identify neurons activated during foot-shock-induced self-pain (Fig. 3q), we defined 
experience of self-pain as the 4-second period following the onset of each foot-shock. 
Individual neurons that were significantly responsive during self-pain or close investigation 
towards demonstrators in pain were identified using the ROC analysis described above.

Assessment of neural responses to different states of others within and across 
demonstrators.: In the analyses of the overlaps between different cell groups presented 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 22

in Fig. 3, the response types of individual cells were defined based on ROC analysis using 
pooled data from different demonstrators. This enhances statistical power by increasing the 
number of behavior frames included in the analysis, and preferentially identifies cells that 
show consistent response properties across demonstrator animals.

To further assess ACC neuronal responses to different states of others within and across 
demonstrators, we first performed a within-subject analysis to determine if ACC neurons 
responded differentially to different states of the same demonstrator. Using ROC analysis 
on data from each individual demonstrator, we identified cells that were activated by others’ 
naïve, pain, or stress state within the same demonstrator. For each state, we identified 
cells with auROC values that exceeded the 95th percentile of the null distribution in the 
within-demonstrator ROC analysis. A slightly less stringent auROC cutoff (95th percentile) 
was applied compared to when using data from all demonstrators (97.5th percentile) due 
to reduced statistical power when using data from only one demonstrator. We found 
that different response types showed substantial non-overlap in individual demonstrators 
(Extended Data Fig. 6e, j, n). This suggests that distinct states of an identical demonstrator 
indeed recruit different neuronal populations in the ACC.

Moreover, we examined if the ACC displayed consistent neural responses to the same 
states in different demonstrators. To this end, we compared the overlap between cells that 
responded to the same state (i.e., naïve, pain, or stress) in different demonstrators to that 
between cells that responded to different states in different demonstrators (Extended Data 
Fig. 6d, i, m). For each state in each demonstrator, we identified the top 25% most activated 
cells (based on auROC values in the within-demonstrator ROC analysis) that were also 
defined as activated in the ROC analysis using data from all demonstrators. Demonstrators 
with a minimum of 10 cells in each response type were included for the analysis to enhance 
the robustness of the results. We found that the overlap between cells of the same response 
type in different demonstrators was significantly higher than that between cells of different 
response types in different demonstrators. This suggests that there exists a shared neural 
signature in response to the same state across demonstrators as well as distinctions in neural 
responses to different states.

To further determine whether individual cells are similarly tuned to the same state 
across different demonstrators, we performed ROC analysis on data from each individual 
demonstrator and subsequently calculated the correlation of the auROC values of the 
responsive cells (defined based on data from all demonstrators) between pairs of 
demonstrators. The auROC value provides a quantitative measure of how strong a cell is 
tuned to a particular state or behavior. If a cell displays similar auROC values for the same 
state in different demonstrators, it indicates that this cell displays a similar response to 
that state across demonstrators. We found that the auROC values of cells that responded 
to the same state were significantly correlated between different demonstrators, suggesting 
that these cells exhibit similar tuning properties to others’ pain state across demonstrators 
(Extended Data Fig. 6a, b, f, g, k, groups 1 and 3 in Extended Data Fig. 6c, h, and group 1 
in Extended Data Fig. 6l). We next calculated the correlation by selecting the same number 
of top responsive cells based on auROC values computed after circularly permuting the 
calcium signals by a random time shift. We observed significantly lower correlations for 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 23

the shuffled data compared to the observed values (groups 2 and 4 in Extended Data Fig. 
6c, h, and group 2 in Extended Data Fig. 6l). Furthermore, we calculated the correlations 
between auROC values for different states in the same demonstrator and found that they 
were significantly lower than those of auROC values for the same state between different 
demonstrators (groups 5 and 6 in Extended Data Fig. 6c, h, and groups 3 and 4 in Extended 
Data Fig. 6l; correlation was calculated separately for cells responsive to either state). 
This suggests that the responses of these cells to the same state of others across different 
demonstrators were more similar compared to their responses to different states of the same 
demonstrators.

Note that because self-pain-responsive cells were identified based on the same subject 
animal in each experiment, the cross-demonstrator analysis was only performed for other-
pain-responsive cells in Extended Data Fig. 6k-n.

Response during allolicking versus allogrooming (Fig. 5a).: For this analysis, we 
included experiments during which the subject animals exhibited both targeted allolicking 
and allogrooming behaviors from the two behavior paradigms shown in Fig. 3d and 3i. 
We obtained a total of 5080 neurons from 12 independent imaging experiments in 12 
subject animals (423 ± 146 neurons from each animal, mean ± SD). As subject animals 
exhibited allogrooming towards both demonstrators in pain and demonstrators in stress, 
we included allogrooming towards both demonstrator types to increase statistical power. 
Individual neurons that were significantly responsive during allolicking or allogrooming 
were identified using the ROC analysis described above.

Response during allolicking versus self-licking (Fig. 5j).: For this analysis, we included 6 
independent imaging experiments in 6 subject animals during which the subject animals 
exhibited targeted allolicking and self-licking behaviors from the behavior paradigm 
shown in Fig. 3n (2399 neurons in total, 400 ± 77 neurons from each animal, mean 
± SD). Individual neurons that were significantly responsive during allolicking towards 
demonstrators in pain or self-licking were identified using the ROC analysis described 
above.

Response during allolicking versus investigation (Fig. 5n).: For this analysis, we included 
experiments during which the subject animals exhibited targeted allolicking behavior from 
the two behavior paradigms shown in Fig. 3d and 3i. We obtained a total of 5852 neurons 
from 14 independent imaging experiments in 14 subject animals (418 ± 141 neurons from 
each animal, mean ± SD). Individual neurons that were significantly responsive during 
allolicking or investigation towards demonstrators in pain were identified using the ROC 
analysis described above.

Response during allogrooming versus investigation (Extended Data Fig. 8l).: For this 
analysis, we included experiments during which the subject animals exhibited allogrooming 
behavior from the two behavior paradigms shown in Fig. 3d and 3i. We obtained a total 
of 5406 neurons from 13 independent imaging experiments in 13 subject animals (416 ± 
142 neurons from each animal, mean ± SD). Since subject animals exhibited allogrooming 
towards both demonstrators in pain and demonstrators in stress, we included allogrooming 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 24

towards both demonstrator types to increase statistical power. Individual neurons that were 
significantly responsive during allogrooming or investigation towards demonstrators in pain 
or demonstrators in stress were identified using the ROC analysis described above.

Quantification of averaged cell responses (Fig. 3g, l, r, Fig. 5c, d, k, o, Extended Data 
Fig. 8m).: Activity of individual cells during each behavior bout was aligned to behavior 
onset (time 0) and averaged across all behavior bouts within each imaging session. Only 
behavior bouts with a duration > 1.5 s were included and neighboring behavior bouts with 
an interval < 2 s were merged into a longer bout. The values of activity change were 
derived by subtracting the baseline activity, which was calculated as averaged activity over 
a 3-s time window between 5 s and 2 s before behavior onset. Fig. 3g, l, Fig. 5c, k, o, 
and Extended Data Fig. 8m show heatmaps of the activity changes of 15 example cells in 
different response types as indicated in the figures and legends. Fig. 3r and Fig. 5d show 
averaged traces of all cells in different response types as indicated in the figures and legends.

Cell clustering based on response property (Fig. 3m, Extended Data Fig. 8c-f).: Cells 
were clustered based on their activity dynamics during the 5 seconds before and after 
behavior onset. Only behavior bouts with a duration > 1.5 s were included and adjacent 
behavior bouts with an interval < 2 s were merged into a longer bout. Activity of individual 
cells during each behavior bout was aligned to behavior onset (time 0) and averaged across 
all behavior bouts within each imaging session. Baseline activity, calculated as averaged 
activity over a 3-s time window between 5 s and 2 s before behavior onset, was then 
subtracted. Activity data from various types of behavioral event were concatenated for each 
cell, and K-means clustering was subsequently performed, with the number of clusters 
selected based on the Calinski-Harabasz criterion. In Fig. 3m, we calculated the averaged 
activity changes for individual cells in each cluster as the averaged activity (after baseline 
subtraction) within the 5 seconds following behavior onset.

K-means clustering analysis provides a high-level view of the activity structure of ACC 
neurons at the level of neuronal clusters. Yet, individual cells with specific response 
properties as revealed by the single-cell ROC analysis may not be grouped into unique 
clusters if their activity dynamics lack sufficiently high similarity. Although neurons that 
were activated by both stressed and pain-experiencing demonstrators (but not by naïve 
demonstrators) did not emerge as a distinct cluster in our K-means clustering analysis (Fig. 
3m, Extended Data Fig. 8c, d), cells exhibiting this response pattern could still be identified 
when analyzed at the level of individual cells (Fig. 3j, Extended Data Fig. 8g).

Assessment of overlap between cells of different response types (Fig. 3e, j, o, q, 5a, 
j, n, Extended Data Fig. 8j, l).: To determine whether the overlaps between various cell 
populations significantly deviate from chance levels, we performed Fisher’s exact test. In 
this test, an odds ratio that is greater than 1 with a significant P value indicates a higher-
than-chance-level overlap between two cell groups, whereas an odds ratio that is smaller 
than 1 with a significant P value indicates a lower-than-chance-level overlap. (Fig. 3e) Odds 
ratio = 5.3, P < 0.0001. (Fig. 3j) Odds ratio = 7.3, P < 0.0001. (Fig. 3o) Odds ratio = 1.1, P 
= 0.796. (Fig. 3q) Odds ratio = 1.5, P = 0.056. (Fig. 5a) Odds ratio = 2.5, P < 0.0001. (Fig. 
5j) Odds ratio = 3.3, P < 0.0001. (Fig. 5n) Odds ratio = 2.0, P < 0.0001. (Extended Data 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 25

Fig. 8g) Odds ratio = 14.2, P < 0.0001. (Extended Data Fig. 8j) Odds ratio = 0.4, P = 0.035. 
(Extended Data Fig. 8l) Odds ratio = 2.4, P < 0.0001.

Analysis of population dynamics

Binary decoding between different types of events (Fig. 3h, p, Fig. 5e, f, l, m, p, q, 
Extended Data Fig. 8n).: Support Vector Machine (SVM) models were used to identify 
hyperplanes that best separate population vectors associated with different types of events. 
Decoder performance was computed independently for each experiment using a leave-one-
out cross-validation (LOOCV) procedure.

For each experiment, the mean population activity associated with an event was considered 
as a sample, and samples were taken for all instances of each of two types of events. Only 
events with a duration > 1.5 s were included and neighboring behavior bouts with an interval 
< 2 s were merged into a longer event. The mean activity of each cell during an event was 
calculated by averaging the activity within a 10-s period following behavior onset (if the 
duration of the event was > 10 s) or during the entire bout (if the duration of the event was ≤ 
10 s). All cells were included for the analysis.

We used a hold-out sample for testing in each validation fold, while the remaining samples 
were used for training. We removed any samples that occurred within 3 s (Fig. 3h), 10 
s (Fig. 3p), or 20 s (Fig. 5e, f, l, m, p, q, Extended Data Fig. 8n) before the onset or 
after the offset of the test sample on a given fold from the training set for that fold. This 
practice avoids temporal contamination between training and test samples, which could 
lead to overestimated decoding performance. For each dataset, we determined the smallest 
window size that is required to eliminate temporal contamination based on performance 
for the shuffled control data. This allowed us to avoid temporal contamination between 
training and test samples while maximally preserving training samples. We applied the 
same criteria to the observed data and shuffled control data in each decoding analysis as 
well as across analyses within each group of comparison (between naïve demonstrators 
and demonstrators in pain in Fig. 3h, between observers’ self-licking and observation of 
demonstrators’ self-licking in Fig. 3p, and between allolicking and allogrooming in Fig. 5e, 
f, l, m, p, q, Extended Data Fig. 8n). To equalize representation of training samples for each 
group in each fold, we randomly downsampled the group with more samples. In each fold, 
we first performed partial-least-square (PLS) regression on the training set with behavior 
type as the response variable. Next, we utilized the first n PLS components in the training 
data that explain at least 50% of the total variance to construct an SVM model. We then 
computed the first n components for the held-out sample using the loadings determined 
from the training set and generated a prediction score for the hold-out sample based on 
these components. Finally, we compared all prediction scores from all validation folds with 
ground truth sample labels using an ROC curve, and we used the area under this curve 
(auROC) as the final performance metric. The number of test samples for each group was 
equalized by randomly downsampling the group with more samples. The LOOCV procedure 
was repeated 10 times to account for the randomness during the downsampling of training 
and test samples. The averaged auROC was then computed across the 10 rounds. We 
measured the chance performance for each experiment by performing the same procedure 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 26

but first circularly permuting the activity trace for each neuron. This process was repeated 20 
times and the averaged auROC was calculated.

To obtain the time courses of decoder performance (Fig. 5f, q), we performed the 
aforementioned LOOCV procedures using population activities at different time points 
relative to behavior onset (time 0). At each time point (ranging from 15 seconds before to 
15 seconds after behavior onset with a 1-s interval), samples of population activity at that 
time point were calculated as the averaged activity between 0 s and 1.5 s after that time 
point. Time-courses for shuffled control data were computed by randomly permuting activity 
traces in a circular manner.

To perform the population analysis with sufficient training examples, we included 
experiments during which the animals displayed at least 4 bouts of either of the two types 
of events in the decoding analyses presented in Fig. 3h, Fig. 5e, f, l, m, p, q, and Extended 
Data Fig. 8n. In addition, in the LOOCV procedures, we included folds in which the number 
of training samples for any group was at least 4 for the calculation of decoding performance. 
These criteria led to variations in the number of mice included in each analysis in Fig. 5 and 
Extended Data Fig. 8n, depending on the types of events being decoded (exact sample sizes 
are provided in Supplementary Table 1).

Mutual decoding of self-pain and pain in others (Fig. 3s-w).: To examine whether 
population activity patterns during experiences of self-pain and pain in others may contain 
shared information, we asked whether classification models trained to decode the perception 
of others’ pain could also decode the experience of self-pain (Fig. 3s). We first calculated 
the mean activity of each cell during each event of foot-shock, investigation towards 
demonstrators in pain, or baseline period (defined as a period during which the subject 
animal did not exhibit social investigation, allolicking, allogrooming, or self-grooming). 
All cells were included for the analysis. For foot-shock, mean activity was calculated by 
averaging the activity during the 2-s shock. For investigation, mean activity was calculated 
by averaging the activity over a 3-s period following behavior onset (if bout duration was 
> 3 s) or over the entire duration of the bout (if bout duration was ≤ 3 s). For baseline 
periods, we excluded the first and last 1 s of each bout from the calculation of mean activity 
to avoid influence from neighboring behavior bouts. We then calculated mean activity as the 
averaged activity between 1 s and 4 s following bout onset (if bout duration was > 3 s) or 
between 1 s after bout onset and 1 s before bout offset (if bout duration was ≤ 3 s). All 
instances of foot-shocks and baseline periods were taken as the test set. For each sample 
of the test set, we constructed a training set that consisted of all instances of investigation 
events and baseline periods, excluding those that occurred within a 90-s time window 
before the onset or after the offset of the test sample. The number of training samples 
for each group was equalized by randomly downsampling the group with more samples. 
We performed PLS regression on the training set with event type as the response variable, 
and utilized the first n PLS components that explain at least 50% of the total variance to 
construct an SVM model. We then computed the first n components for the test sample 
using the loadings determined from the training set and generated a prediction score for 
the test sample based on these components. We subsequently compared prediction scores 
for all test samples with ground truth labels using an ROC curve, and we used the area 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 27

under this curve (auROC) as the final performance metric. The number of test samples for 
each group was equalized by randomly downsampling the group with more samples. This 
procedure was repeated 10 times to account for the randomness during the downsampling 
of training and test samples, and the averaged auROC across the 10 rounds was computed. 
To calculate chance performance, we utilized the same procedure, but with the additional 
step of circularly permuting the activity trace for each neuron. This permutation process was 
repeated 20 times and the averaged auROC was computed.

Conversely, to investigate whether classification models trained to decode the experience 
of self-pain could also decode the perception of pain in others (Fig. 3t), we conducted 
similar procedures but used population activity during investigation towards others in pain 
and baseline periods to construct test samples and population activity during foot-shocks and 
baseline periods to construct training samples.

For mutual decoding between self-pain or others’ pain and self-grooming or others’ neutral 
state (Fig. 3u-w), we followed similar procedures, using mean activity during various events 
to create test and training sets as indicated in the figures and legends.

To perform these analyses with sufficient training samples, we included experiments in 
which the animals displayed at least 3 bouts of the event type that was used for model 
training. Additionally, during cross validation, we included folds in which the number of 
training samples for any group was at least 3 for the calculation of decoding performance.

Evaluation of decoding performance after removal of significantly responsive cells 
(Extended Data Fig. 7b-j): To assess how cells that are identified as significantly 
responsive in the ROC analysis contribute to population coding, we performed decoding 
analysis as delineated above after excluding these cells. In most cases (Extended Data 
Fig. 7b, c, e, h-j), we observed a significant decrease in decoding performance after the 
removal of these cells, consistent with the notion that these cells contribute to the differential 
population coding of distinct states and behaviors. In a small number of groups (Extended 
Data Fig. 7d, f, g), we observed a trend towards decreased performance after cell removal, 
although this trend did not reach statistical significance. This suggests that other cells that 
did not reach the threshold for being categorized as significantly responsive are also part 
of the neural ensemble that contributes to the high-dimensional features that differentiate 
different states.

In all the boxplots for decoding analysis (Fig. 3h, p, s-w, Fig. 5e, l, m, p, Extended Data 
Fig. 7b-j, Extended Data Fig. 8n), each observer animal was considered an independent 
biological sample, and the boxplots displayed the variations in decoder performance across 
animals.

Principal component analysis (Fig. 5h, i).—To analyze the separation of population 
vectors associated with different types of behaviors, we performed principal component 
analysis based on mean population activity during different behavior events for each 
experiment. The mean activity of each cell during each event was calculated by averaging 
the activity over a 5-s period following behavior onset (if bout duration was > 5 s) or over 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 28

the entire duration of the bout (if bout duration was ≤ 5 s). We then computed the averaged 
pairwise Euclidean distance between different behavior categories in the space defined by 
the top 3 PC projections for each experiment. The fraction of total variance accounted for by 
each of the first PCs is shown in Extended Data Fig. 8k.

Statistics and reproducibility

All statistical analyses were conducted using Prism (v10, GraphPad) or MATLAB (R2019b, 
MathWorks). Details about the types of statistical tests used, test statistics, P values, and 
samples sizes are provided in Supplementary Table 1. When parametric tests were used, data 
normality was confirmed using the D’Agostino&Pearson test. P values were corrected for 
multiple comparisons when necessary. Bar plots show mean ± s.e.m. In boxplots, the center 
line indicates the median, the box limits indicate the upper and lower quartiles, and the 
whiskers indicate the minimum and maximum value, the 10th and 90th percentiles, or data 
within 1.5× interquartile range, as indicated in figure legends. The significance threshold 
was held at α = 0.05 (ns, not significant (P > 0.05); *P < 0.05; **P < 0.01; ***P < 0.001; 
****P < 0.0001). All behavioral, imaging, chemogenetics, and optogenetics experiments 
were replicated in multiple subject animals with similar results. Example micrographs 
(Fig. 3b, Fig. 4b, g, Extended Data Fig. 10j) show representative results based on at least 
three independent animals. Sample sizes were not predetermined using statistical methods. 
Experiments were randomized whenever possible. Experimenters were not blind to group 
allocation.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Extended Data

Page 29

Extended Data Fig. 1. Behavioral responses of demonstrators and observers following melittin 
injection.
(a) Example images showing saline- or melittin-injected paws. (b) Example raster plots 
showing self-licking behavior directed towards the melittin-injected paw or other paws 
in demonstrator animals. Each row indicates an individual demonstrator animal. (c) Time 
courses of the cumulative duration of self-licking behavior towards the melittin-injected 
paw and other paws. (d) Duration of self-licking behavior towards the melittin-injected 
paw and other paws during 5-minute intervals throughout the interaction period. (e) Total 
duration of self-licking behavior towards the melittin-injected paw and other paws. (f) 
Duration of allolicking towards the uninjected forepaws of demonstrators that were injected 
with either melittin or saline in the hind paw during 5-minute sliding windows throughout 
the interaction period. (g) Time courses of the cumulative duration of allolicking towards 
the uninjected forepaws. (h, i) Total duration (h) and number of bouts (h) of allolicking 
towards the uninjected forepaws of melittin- and saline-injected demonstrators. (j-m) Total 
duration of different behaviors displayed by dominant observers when interacting with 
subordinate demonstrators in pain and by subordinate observers when interacting with 
dominant demonstrators in pain, including investigation (j), general allogrooming (k), 
allolicking towards injured paws and uninjured paws (l), and general allogrooming and 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 30

targeted allolicking combined (m). In (c, d), data are mean ± s.e.m. In (e, h, i, j-m), the 
center line in the boxplots indicates the median, the box limits indicate the upper and lower 
quartiles, and the whiskers indicate the 10th and 90th percentiles. n = 24 mice in (c-e), 12 
mice per group in (f-i), and 13 mice per group in (j-m). (e, h, i) Wilcoxon signed-rank test. 
(j, k, m) Unpaired t-test. (l) Two-way repeated measures ANOVA with post hoc Bonferroni’s 
multiple comparisons test. All statistical tests are two-sided. ****P < 0.0001, **P < 0.01, 
*P < 0.05. ns, not significant. Details of statistical analyses are provided in Supplementary 
Table 1.

Extended Data Fig. 2. Behaviors of female observers towards female demonstrators in pain.
(a) Example raster plots showing general allogrooming and targeted allolicking behaviors 
towards demonstrators injected with either melittin or saline (control). Each row indicates an 
individual observer animal, and the same observers were plotted for the control and melittin-
injected groups. (b) Time courses of the cumulative duration of different behaviors towards 
demonstrators in pain and control animals, including investigation, general allogrooming, 
targeted allolicking towards injured paws, allolicking towards uninjured paws, and general 
allogrooming and targeted allolicking combined. Data are mean ± s.e.m. (c) Duration 
of various behaviors during 5-minute sliding windows throughout the interaction period. 
(d-k) Quantification of the duration (d-g) and bout number (h-k) of behaviors towards 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 31

demonstrators in pain and control animals. In (d-k), the center line in the boxplots indicates 
the median, the box limits indicate the upper and lower quartiles, and the whiskers indicate 
the minimum and maximum values. n = 18 mice per group in (b-k). (d, e, g, h, i, 
k) Wilcoxon signed-rank test. (f, j) Two-way repeated measures ANOVA with post hoc 
Bonferroni’s multiple comparisons test. All statistical tests are two-sided. ***P < 0.001, 
**P < 0.01, *P < 0.05. ns, not significant. Details of statistical analyses are provided in 
Supplementary Table 1.

Extended Data Fig. 3. Observers’ behaviors towards demonstrators experiencing pain induced 
by formalin injection.
(a) Example raster plots showing general allogrooming and targeted allolicking behaviors 
towards formalin- and saline-injected demonstrators. Each row indicates an individual 
observer animal, and the same observers were plotted for the control and formalin-injected 
groups. (b) Time courses of the cumulative duration of different behaviors towards 
formalin- and saline-injected demonstrators, including investigation, general allogrooming, 
targeted allolicking towards injured paws, allolicking towards uninjured paws, and general 
allogrooming and targeted allolicking combined. Data are mean ± s.e.m. (c) Duration 
of various behaviors during 5-minute intervals throughout the interaction period. (d-k) 
Quantification of the duration (d-g) and bout number (h-k) of various behaviors towards 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 32

formalin- and saline-injected demonstrators. In (d-k), the center line in the boxplots 
indicates the median, the box limits indicate the upper and lower quartiles, and the whiskers 
indicate the minimum and maximum values. n = 16 mice per group in (b-k). (d, e, g, h, 
i, k) Wilcoxon signed-rank test. (f, j) Two-way repeated measures ANOVA with post hoc 
Bonferroni’s multiple comparisons test. All statistical tests are two-sided. ***P < 0.001, 
**P < 0.01, *P < 0.05. ns, not significant. Details of statistical analyses are provided in 
Supplementary Table 1.

Extended Data Fig. 4. Observers display general allogrooming but not targeted allolicking 
towards demonstrators in a stress state induced by acute restraint.
(a) Schematic of the behavioral protocol for examining interaction between observer mice 
and demonstrators in stress. (b) Time courses of the cumulative duration of investigation, 
general allogrooming, and allolicking of paws towards stressed demonstrators and controls. 
Data are mean ± s.e.m. (c) Duration of various behaviors during 5-minute intervals 
throughout the interaction period. (d) Quantification of the duration of various behaviors 
towards stressed demonstrators and controls. The center line in the boxplots indicates the 
median, the box limits indicate the upper and lower quartiles, and the whiskers indicate the 
minimum and maximum values. n = 12 mice per group in (b-d). (d) Two-sided Wilcoxon 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 33

signed-rank test. **P < 0.01. ns, not significant. Details of statistical analyses are provided 
in Supplementary Table 1.

Extended Data Fig. 5. Allolicking assists others in coping with pain.
(a, b) Duration of self-licking behavior exhibited by demonstrators and combined duration 
of self-licking by demonstrators and targeted allolicking by observers. The demonstrators 
were either isolated or housed with cage mates after receiving melittin injection. The 
demonstrators were divided into a “low prosocial” group (a) and a “high prosocial” group 
(b) based on the level of targeted allolicking and general allogrooming behaviors exhibited 
by the cage mates. The combined duration of allolicking and allogrooming by cage mates 
were < 50 s in the “low prosocial” group, and ≥ 50 s in the “high prosocial” group. Grey 
bar: the amount of time that demonstrators spent self-licking when they were alone; blue 
bar: the amount of time that demonstrators spent self-licking when they were together 
with observers; red bar: the combined duration of self-licking and allolicking in a social 
setting. (c, d) Example spectrograms overlaid with behavior annotations showing the lack 
of vocalizations during interaction between observers and demonstrators in pain, as well as 
prior to the onset of allolicking or allogrooming behavior (c). This contrasts with frequent 
vocalizations emitted by pups (d). (e-g) Correlations between the duration of self-licking 
by demonstrators and allolicking (e) or allogrooming (f) by observers or the two behaviors 
combined (g). Solid lines represent linear regression lines and dashed lines indicate 95% 
confidence intervals. (h) Raster plots showing targeted allolicking by observers towards the 
melittin- and saline-injected paws of sedated demonstrators. (i) Onset latency of allolicking 
towards the injured paw of awake and sedated demonstrators. (j, k) The fraction of targeted 
allolicking towards the injured paw and allolicking toward the uninjured paw of awake (j) 
and sedated (k) demonstrators during different interaction periods. In (a, b, i-k), data are 
mean ± s.e.m. n = 6 mice per group in (a), 18 mice per group in (b), 16 mice in (e-g), and 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 34

12 mice in the awake group and 18 mice in the sedated group in (i-k). (a, b) Friedman test 
with post hoc Dunn’s multiple comparisons test. (e-g) Linear regression. (i) Wilcoxon rank-
sum test. (j, k) Two-way repeated measures ANOVA with post hoc Bonferroni’s multiple 
comparisons test. All statistical tests are two-sided. ****P < 0.0001, **P < 0.01, *P < 0.05. 
ns, not significant. Details of statistical analyses are provided in Supplementary Table 1.

Extended Data Fig. 6. Response of ACC neurons to different states of others across 
demonstrators.
(a, b, f, g, k) Pearson correlation of auROC values (reflecting cells’ tuning properties) 
with respect to investigation (“inv”) towards others in neutral (a), pain (b, g, k) or stress 
(f) state between pairs of demonstrators. auROC values were derived using data from 
each demonstrator and Pearson correlation coefficient was calculated for cells defined as 
significantly responsive based on data pooled from all demonstrators. Each dot represents 
correlation between a pair of demonstrators. P values less than 10−10 are plotted as 10−10 
for visualization purposes. (c, h, l) Correlation between auROC values for the same state 
of others (neutral, pain, or stress) across pairs of demonstrators (“dem”): groups 1 and 3 in 
(c, h), group 1 in (l). Correlation derived from randomly shuffled data (grey bars): groups 
2 and 4 in (c, h), group 2 in (l). Correlation between auROC values for different states of 
others within the same demonstrators: groups 5 and 6 in (c, h), groups 3 and 4 in (l); for 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 35

these groups, correlation was calculated separately for cells responsive to either state. (d, i, 
m) Overlap between activated cells in the same or different response types across pairs of 
demonstrators. (e, j, n) Fraction of cells from each response type that overlap with the other 
response type within the same demonstrators. Activated cells were defined based on auROC 
values derived from data from each individual demonstrator. In (c-e, h-j, l-n), the center line 
in the boxplots indicates the median, the box limits indicate the upper and lower quartiles, 
and the whiskers indicate data within 1.5× interquartile range. Data were from 11 mice in 
(a-e), 10 mice in (f-j), 6 mice in (k-n). (c, d) Kruskal-Wallis test with post-hoc Dunn’s 
multiple comparison test. (h, i, l) One-way ANOVA test with with post hoc Bonferroni’s 
multiple comparisons test. (m) Wilcoxon rank-sum test. All statistical tests are two-sided. 
****P < 0.0001, **P < 0.01. Details of statistical analyses and sample sizes are provided in 
Supplementary Table 1.

Extended Data Fig. 7. Single-cell- and population-level representations of prosocial behaviors 
and different states of demonstrators.
(a) Schematics illustrating dissociable and shared aspects in the neural representations 
of different states or behaviors at the single-cell and population levels. (b-j) Decoding 
performance using all cells and after removing significantly responsive cells in different 
groups of decoding analysis. Data in the “All cells” groups in (b-j) are the same as presented 
in Fig. 3h, 3p, 3s (left), 3t (left), 5e, 5l, 5p, 5m, and Extended Data Fig. 8n, respectively. (k, 
l) Fraction of variance explained by the first three PC (k) and PLS (l) components in the data 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 36

used for decoding of others’ neutral versus pain state (Fig. 3h). In (b-l), the center line in the 
boxplots indicates the median, the box limits indicate the upper and lower quartiles, and the 
whiskers indicate the minimum and maximum values (b-j) or data within 1.5× interquartile 
range (k, l). n = 11 mice in (b, h, j-l), 6 mice in (c-e, g), 8 mice in (f), 12 mice in (i). 
(b-j) Two-sided Wilcoxon signed-rank test. ***P < 0.001, **P < 0.01, *P < 0.05. ns, not 
significant. Details of statistical analyses are provided in Supplementary Table 1.

Extended Data Fig. 8. Response of ACC neurons to others’ pain and stress states and during 
prosocial behaviors.
(a, b) Schematic timelines showing the order of the presentation of different types 
of demonstrators and self-pain experiences for examining the neural representations of 
others’ stress versus pain state (a) and self-pain versus others’ pain (b). (c, e) Heatmaps 
showing average responses of all recorded ACC neurons during the 5 seconds before 
and after the onset of close investigation of demonstrators in neutral, stress, or pain state 
(c) as well as allolicking and allogrooming (e). Each row represents the activity of an 
individual cell aligned to the onset of close investigation, allolicking, or allogrooming 
towards demonstrators (time 0). Cells are clustered using K-means clustering based on 
their activity dynamics. Clusters are separated by dashed horizontal lines. (d, f) Cells in 
clusters showing a trend of increased activity preferentially in response to one type of 
demonstrator or behavior in (c, e) are ordered by the time each cell takes to reach 50% 
of its maximum activity. (g) The expected and observed percentages of neurons activated 
by all three demonstrator types (naïve, stress, and pain) among the neurons activated by 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 37

both stressed and pain-experiencing demonstrators. (h, i) Pair-wise distances between cells 
activated by demonstrators in stress or pain (h), or between cells activated during allolicking 
or allogrooming (i) within the field of view. Distances between cells within the same 
response type or from different response types are compared. Grey boxes show distances 
calculated after cell type identities were randomly shuffled. (j) Venn diagram showing the 
overlap between neurons activated during the observers’ self-licking after receiving melittin 
injection or when observing self-licking of melittin-injected demonstrators. (k) Fraction of 
variance accounted for by the first three PCs in the PCA analysis of population activity 
associated with allolicking and allogrooming as presented in Fig. 5g-i. (l) Venn diagram 
and example calcium traces of cells selectively activated during either allogrooming or 
investigation, but not both, towards demonstrators in pain or stress. (m) Heatmaps showing 
average responses of example cells (each row) activated selectively by either allogrooming 
or investigation (but not both) aligned to the onset of each type of behavior (time 0). (n) 
Performance of decoders trained on population activity in classifying allogrooming versus 
investigation. In (h, i, k, n), the center line in the boxplots indicates the median, the box 
limits indicate the upper and lower quartiles, and the whiskers indicate the minimum and 
maximum values. n = 4388 cells from 10 mice in (c, d, g), 5080 cells from 12 mice in (e, 
f), 10 mice per group in (h), 12 mice per group in (i), 2399 cells from 6 mice in (j), 6 mice 
per group in (k), 5406 cells from 13 mice in (l), 11 mice per group in (n). (h, i) Friedman 
test. (n) Wilcoxon signed-rank test. All statistical tests are two-sided. ***P < 0.001. ns, not 
significant. Details of statistical analyses are provided in Supplementary Table 1.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 38

Extended Data Fig. 9. Behavioral effects of DREADD inhibition of ACC neurons.
(a) Schematic of viral injection and experimental paradigm for DREADD inhibition 
experiments in mCherry-expressing control animals. (b) Time courses of the cumulative 
duration of general allogrooming, targeted allolicking, allogrooming and allolicking 
combined, and social investigation towards pain-experiencing demonstrators by observers 
that were injected with either CNO or saline. The observers expressed mCherry but not 
hM4Di. Data are mean ± s.e.m. (c, d) Quantification of the total duration (c) and bout 
number (d) of general allogrooming, targeted allolicking, allogrooming and allolicking 
combined, and social investigation towards pain-experiencing demonstrators by mCherry-
expressing observers that were injected with either CNO or saline. (e, f) Correlation 
between the duration of investigation and allolicking (e) or allogrooming (f) directed 
towards demonstrators in pain during chemogenetic inhibition of ACC neurons. Solid 
lines: linear regression lines, dashed lines: 95% confidence intervals. (g) Schematic of the 
three-chamber social preference test. (h) Total time spent in the “social” and “non-social” 
zones in hM4Di-expressing animals injected with CNO or saline. (i) Sociability scores of 
hM4Di-expressing animals injected with CNO or saline. (j, k) Duration and bout number 
of allolicking (j) or investigation (k) displayed by hM4Di-expressing observers injected with 
CNO or saline towards melittin-injected demonstrators that were under sedation. In (c, d, 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 39

h-k), the center line in the boxplots indicates the median, the box limits indicate the upper 
and lower quartiles, and the whiskers indicate the 10th and 90th percentiles (h, i) or the 
minimum and maximum values (c, d, j, k). n = 10 mice per group in (b-d), 16 mice in 
(e, f), 14 mice per group in (h, i), and 11 mice per group in (j, k). (c, d, i) Paired t-test. 
(e, f) Linear regression. (h) Two-way repeated measures ANOVA followed by post hoc 
Bonferroni’s multiple comparisons test. (j, k) Wilcoxon signed-rank test. All statistical tests 
are two-sided. **P < 0.01. *P < 0.05. ns, not significant. Details of statistical analyses are 
provided in Supplementary Table 1.

Extended Data Fig. 10. Optogenetic activation of ACC neurons and control experiments.
(a) Example raster plots showing an overall increase in allolicking/allogrooming during 
the 3-minute laser-on periods in ACC optogenetic activation experiments, compared to 
the 1.5-minute laser-off periods immediately before and after stimulation. (b) Duration 
of investigation behavior towards demonstrators in pain during periods of optogenetic 
activation of ACC neurons (laser-on phases) compared to laser-off phases. (c, d) Correlation 
between the duration of investigation and allolicking (c) or allogrooming (d) during 
optogenetic activation. Solid lines: linear regression lines, dashed lines: 95% confidence 
intervals. (e, f) The probability of allolicking (e) and investigation (f) during the 30 
seconds before and after the onset of laser stimulation in experiments where stimulations 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 40

were initiated after the first three minutes of the interaction. (g) Schematic of viral 
injection and experimental paradigm for light-stimulation experiments the ACC in EYFP-
expressing control animals. (h) Quantification of the total duration of general allogrooming, 
targeted allolicking, and allogrooming and allolicking combined towards pain-experiencing 
demonstrators by EYFP-expressing observers during laser-on and laser-off periods. (i) 
Schematic of viral injection and experimental paradigm for optogenetic activation of 
excitatory neurons in the PrL. (j) Example image showing ChR2-EYFP expression. Scale 
bar, 500 μm. ( k) Quantification of the total duration of general allogrooming, targeted 
allolicking of the injured paw, allolicking of uninjured paws, and allogrooming and targeted 
allolicking combined towards pain-experiencing demonstrators by observers during laser-on 
and laser-off periods. (l, m) Comparison of the duration (l) and bout number (m) of self-
licking behavior displayed by melittin-injected subject animals during optogenetic activation 
of ACC neurons versus periods without laser stimulation. In (e, f), data are mean ± s.e.m. In 
(h, k), the center line in the boxplots indicates the median, the box limits indicate the upper 
and lower quartiles, and the whiskers indicate the minimum and maximum values. n = 18 
mice per group in (b), 18 mice in (c, d), 80 trials from 16 mice per group in (e, f), 22 mice 
per group in (h), 11 mice per group in (l, m), and 8 mice per group in (k). (b, e, f, h, k, l, m) 
Wilcoxon signed-rank test. (c, d) Linear regression. All statistical tests are two-sided. **P < 
0.01. ns, not significant. Details of statistical analyses are provided in Supplementary Table 
1.

Supplementary Material

Refer to Web version on PubMed Central for supplementary material.

Acknowledgements:

We thank M. Ma, S. Chaudhry, X. Zhang, L. Gu, and S. Kim for technical assistance, C. Cahill for suggestions on 
pain-related experimental procedures, and members of the Hong lab for valuable comments. Schematics in Fig. 1a, 
Fig. 2a, m, p, Fig. 3a, d, i, n, Fig. 4a, f, Extended Data Fig. 4a, Extended Data Fig. 9a, Extended Data Fig. 10g, i 
were created using BioRender. This work was supported in part by NIH grants (R01 MH130941, R01 NS113124, 
R01 MH132736, RF1 NS132912, and UF1 NS122124), a Packard Fellowship in Science and Engineering, a Keck 
Foundation Junior Faculty Award, a Vallee Scholar Award, and a Mallinckrodt Scholar Award (to W.H.).

Data availability:

All data and analyses necessary to understand the conclusions of the manuscript are 
presented in the main text and in Extended Data. Source data supporting the findings of 
the manuscript is included in the supplemental data.

Code availability:

Code for behavioral analysis (https://github.com/pdollar/toolbox and https://
github.com/hongw-lab/Behavior_Annotator), animal pose tracking (https://github.com/
murthylab/sleap/releases/tag/v1.2.9), analysis of mouse vocalizations (https://github.com/
rtachi-lab/usvseg)46, microendoscopic imaging data analysis (https://github.com/
etterguillaume/MiniscopeAnalysis, https://github.com/zhoupc/CNMF_E, and https://
github.com/flatironinstitute/NoRMCorre), ROC (receiver operating characteristic) and 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 41

SVM decoding analysis is available on GitHub (https://github.com/hongw-lab/
Code_for_2023_ZhangM).

References

1. Wu YE & Hong W Neural basis of prosocial behavior. Trends Neurosci 45, 749–762 (2022). 

[PubMed: 35853793] 

2. Waal F. B. M. de & Preston SD Mammalian empathy: behavioural manifestations and neural basis. 

Nat Rev Neurosci 18, 498–509 (2017). [PubMed: 28655877] 

3. Keysers C, Knapska E, Moita MA & Gazzola V Emotional contagion and prosocial behavior in 

rodents. Trends Cogn Sci 26, 688–706 (2022). [PubMed: 35667978] 

4. Ferretti V & Papaleo F Understanding others: Emotion recognition in humans and other animals. 

Genes Brain Behav 18, e12544 (2019). [PubMed: 30549185] 

5. Sterley T-L & Bains JS Social communication of affective states. Curr Opin Neurobiol 68, 44–51 

(2021). [PubMed: 33434768] 

6. Melis AP The evolutionary roots of prosociality: the case of instrumental helping. Curr Opin 

Psychology 20, 82–86 (2018).

7. Dunfield KA A construct divided: prosocial behavior as helping, sharing, and comforting subtypes. 

Front Psychol 5, 958 (2014). [PubMed: 25228893] 

8. Lim KY & Hong W Neural mechanisms of comforting: Prosocial touch and stress buffering. Horm. 

Behav 153, 105391 (2023). [PubMed: 37301130] 

9. Bartal IB-A, Decety J & Mason P Empathy and Pro-Social Behavior in Rats. Science 334, 1427–

1430 (2011). [PubMed: 22158823] 

10. Li AK, Koroly MJ, Schattenkerk ME, Malt RA & Young M Nerve growth factor: acceleration of 

the rate of wound healing in mice. Proc Natl Acad Sci 77, 4379–4381 (1980). [PubMed: 6933491] 

11. Berckmans RJ, Sturk A, Tienen LM van, Schaap MCL & Nieuwland R Cell-derived vesicles 
exposing coagulant tissue factor in saliva. Blood 117, 3172–80 (2011). [PubMed: 21248061] 
12. Day BJ The science of licking your wounds: Function of oxidants in the innate immune system. 

Biochem Pharmacol 163, 451–457 (2019). [PubMed: 30876918] 

13. Lu J. et al. Somatosensory cortical signature of facial nociception and vibrotactile touch–induced 

analgesia. Sci Adv 8, eabn6530 (2022). [PubMed: 36383651] 

14. Huang T. et al. Identifying the pathways required for coping behaviours associated with sustained 

pain. Nature 565, 86–90 (2019). [PubMed: 30532001] 

15. Hutson JM, Niall M, Evans D & Fowler R Effect of salivary glands on wound contraction in mice. 

Nature 279, 793–795 (1979). [PubMed: 450129] 

16. Dittus WPJ & Ratnayeke SM Individual and social behavioral responses to injury in wild toque 

macaques (Macaca Sinica). Int J Primatol 10, 215–234 (1989).

17. Li C-L et al. Validating Rat Model of Empathy for Pain: Effects of Pain Expressions in Social 

Partners. Front Behav Neurosci 12, 242 (2018). [PubMed: 30386220] 

18. Lariviere WR & Melzack R The bee venom test: a new tonic-pain test. Pain 66, 271–277 (1996). 

[PubMed: 8880850] 

19. Wu YE et al. Neural control of affiliative touch in prosocial interaction. Nature 599, 262–267 

(2021). [PubMed: 34646019] 

20. Mogil JS Animal models of pain: progress and challenges. Nat Rev Neurosci 10, 283–294 (2009). 

[PubMed: 19259101] 

21. Duan B, Cheng L & Ma Q Spinal Circuits Transmitting Mechanical Pain and Itch. Neurosci Bull 

34, 186–193 (2018). [PubMed: 28484964] 

22. Smith ML, Asada N & Malenka RC Anterior cingulate inputs to nucleus accumbens control the 
social transfer of pain and analgesia. Science 371, 153–159 (2021). [PubMed: 33414216] 

23. Carrillo M. et al. Emotional Mirror Neurons in the Rat’s Anterior Cingulate Cortex. Curr Biol 29, 

1301–1312 (2019). [PubMed: 30982647] 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 42

24. Allsop SA et al. Corticoamygdala Transfer of Socially Derived Information Gates Observational 

Learning. Cell 173, 1329–1342 (2018). [PubMed: 29731170] 

25. Hernandez-Lallement J. et al. Harm to Others Acts as a Negative Reinforcer in Rats. Curr Biol 30, 

949–961 (2020). [PubMed: 32142701] 

26. Lockwood PL The anatomy of empathy: Vicarious experience and disorders of social cognition. 

Behav Brain Res 311, 255–266 (2016). [PubMed: 27235714] 

27. Johansen JP, Fields HL & Manning BH The affective component of pain in rodents: Direct 

evidence for a contribution of the anterior cingulate cortex. Proc. Natl. Acad. Sci 98, 8077–8082 
(2001). [PubMed: 11416168] 

28. Sato N, Tan L, Tate K & Okada M Rats demonstrate helping behavior toward a soaked conspecific. 

Anim Cogn 18, 1039–1047 (2015). [PubMed: 25964095] 

29. Ueno H. et al. Rescue-like Behaviour in Mice is Mediated by Their Interest in the Restraint Tool. 

Sci Rep 9, 10648 (2019). [PubMed: 31375693] 

30. Burkett JP et al. Oxytocin-dependent consolation behavior in rodents. Science 351, 375–378 

(2016). [PubMed: 26798013] 

31. Langford DJ et al. Social Modulation of Pain as Evidence for Empathy in Mice. Science 312, 

1967–1970 (2006). [PubMed: 16809545] 

32. Bernhardt BC & Singer T The Neural Basis of Empathy. Annu Rev Neurosci 35, 1–23 (2012). 

[PubMed: 22715878] 

33. Phillips HL et al. Dorsomedial prefrontal hypoexcitability underlies lost empathy in frontotemporal 

dementia. Neuron 111, 797–806 (2023). [PubMed: 36638803] 

34. Gangopadhyay P, Chawla M, Monte OD & Chang SWC Prefrontal–amygdala circuits in social 

decision-making. Nat Neurosci 24, 5–18 (2021). [PubMed: 33169032] 

35. Haroush K & Williams ZM Neuronal Prediction of Opponent’s Behavior during Cooperative 

Social Interchange in Primates. Cell 160, 1233–1245 (2015). [PubMed: 25728667] 

36. Paulus M, Kühn-Popp N, Licata M, Sodian B & Meinhardt J Neural correlates of prosocial 

behavior in infancy: Different neurophysiological mechanisms support the emergence of helping 
and comforting. Neuroimage 66, 522–530 (2013). [PubMed: 23108275] 

37. Tjølsen A, Berge O-G, Hunskaar S, Rosland JH & Hole K The formalin test: an evaluation of the 

method. Pain 51, 5–17 (1992). [PubMed: 1454405] 

38. Chen J, Guan S-M, Sun W & Fu H Melittin, the Major Pain-Producing Substance of Bee Venom. 

Neurosci Bull 32, 265–272 (2016). [PubMed: 26983715] 

39. Kingsbury L. et al. Correlated Neural Activity and Encoding of Behavior across Brains of Socially 

Interacting Animals. Cell 178, 429–446.e16 (2019). [PubMed: 31230711] 

40. Zhou T, Sandi C & Hu H Advances in understanding neural mechanisms of social dominance. 

Curr. Opin. Neurobiol 49, 99–107 (2018). [PubMed: 29428628] 

41. Armbruster BN, Li X, Pausch MH, Herlitze S & Roth BL Evolving the lock to fit the key to create 
a family of G protein-coupled receptors potently activated by an inert ligand. Proc. Natl. Acad. Sci 
104, 5163–5168 (2007). [PubMed: 17360345] 

42. Pereira TD et al. SLEAP: A deep learning system for multi-animal pose tracking. Nat. methods 19, 

486–495 (2021).

43. Pnevmatikakis EA & Giovannucci A NoRMCorre: An online algorithm for piecewise rigid motion 

correction of calcium imaging data. J Neurosci Meth 291, 83–94 (2017).

44. Zhou P. et al. Efficient and accurate extraction of in vivo calcium signals from microendoscopic 

video data. Elife 7, e28728 (2018). [PubMed: 29469809] 

45. Kingsbury L. et al. Cortical Representations of Conspecific Sex Shape Social Behavior. Neuron 

107, 941–953.e7 (2020). [PubMed: 32663438] 

46. Tachibana RO, Kanno K, Okabe S, Kobayasi KI & Okanoya K USVSEG: A robust method for 

segmentation of ultrasonic vocalizations in rodents. PLoS ONE 15, e0228907 (2020). [PubMed: 
32040540] 

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 43

Fig. 1. Mice display targeted allolicking towards social partners in pain.
(a) Paradigm for examining the interaction between an observer mouse and a demonstrator 
mouse in pain. (b) Example frames showing general allogrooming and targeted allolicking. 
(c) Example raster plots showing observers’ allogrooming and allolicking towards 
demonstrators injected with either melittin or saline (control). (d) Time courses of the 
cumulative duration of various behaviors towards demonstrators in pain and control animals. 
Time 0 indicates the start of the interaction. (e) Duration of behaviors during 5-minute 
sliding windows throughout the interaction. (f-m) Total duration (f-i) and bout number 
(j-m) of various behaviors. (n) Example traces showing dynamics of changes in head angle 
during allogrooming and allolicking. Each row indicates an individual behavior event. (o) 
Power spectrum analysis of dynamics of head angle. (p-s) Correlations between the total 
duration of various behaviors towards demonstrators in pain. Solid lines: linear regression 
lines, dashed lines: 95% confidence intervals. (d,o) mean ± s.e.m. (f-m) center line: median, 
box limits: upper and lower quartiles, whiskers: minimum and maximum values. n = 12 
mice in (d-m), 63 (allogrooming) and 71 (allolicking) bouts in 4 mice in (o), and 36 mice 
in (p-s). (f,g,i-k,m) Paired t-test. (h,l) Two-way repeated measures analysis of variance 
(ANOVA) with post hoc Bonferroni’s multiple comparisons test. (p-s) Linear regression. All 
statistical tests are two-sided. ****P < 0.0001, ***P < 0.001, **P < 0.01, *P < 0.05. ns, not 
significant. See Supplementary Table 1 for details of statistical analyses.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 44

Fig. 2. Allolicking by observers reduces self-licking in demonstrators.
(a,b) Schematic (a) and quantification (b) of self-licking in demonstrator mice in the 
presence or absence of observers. (c,d) Correlation between the reduction in self-licking 
and the total duration of allogrooming and allolicking (c) or social investigation (d). Solid 
lines: linear regression lines, dashed lines: 95% confidence intervals. (e) Duration of self-
licking in demonstrators that received a high level of allolicking or allogrooming (Methods), 
normalized to that in solitary demonstrators. (f) Probability of demonstrators’ self-licking 
while receiving allogrooming or allolicking. (g) Raster plots showing observers’ allolicking 
and demonstrators' self-licking. (h,j) Time courses of the probability of demonstrators’ 
self-licking around the onset of observers' allolicking of the injured or uninjured paw. (i,k) 
The fraction of reduction in self-licking during the 5 s after the onset of allolicking of 
the injured or uninjured paw. (l) The number of allolicking bouts that were halted due to 
active termination by observers or passive avoidance by demonstrators. (m-o) Schematic 
and quantification of demonstrators' self-licking and observers' allolicking after melittin 
injection or melittin/lidocaine co-injection into demonstrators. (p-s) Schematic (p), time 
courses of the cumulative duration (q), total duration (r), and bout number (s) of allolicking 
towards the melittin- and saline-injected paws of sedated demonstrators. (b,h,j,q) mean ± 
s.e.m. (e,f,i,k,l,n,o,r,s) center line: median, box limits: upper and lower quartiles, whiskers: 
10th and 90th percentiles (e,f,i,k) or minimum and maximum values (l,n,o,r,s). (b,e,l) Paired 
t-test. (f) Friedman test with post doc Dunn’s multiple comparisons test. (i,k,r,s) Wilcoxon 
signed-rank test. (n,o) Wilcoxon rank-sum test. All statistical tests are two-sided. ****P < 
0.0001, ***P < 0.001, **P < 0.01, *P < 0.05. ns, not significant. See Supplementary Table 1 
for details of statistical analyses and sample sizes.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 45

Fig. 3. Neural representations of others’ pain and stress in the ACC.
(a,d,i,n) Schematic of microendoscopic imaging (a) during interaction with naïve or 
pain-experiencing demonstrators (d), during interaction with stressed or pain-experiencing 
demonstrators (i), and during perception of others’ pain and experience of self-pain (n). (b) 
Example image showing GCaMP6f expression and GRIN lens implantation in the ACC. 
Scale bar, 500 μm. ( c) Single neurons in an example field of view. (e,j,o,q) Venn diagrams 
and example calcium traces showing neurons activated by others’ naïve or pain state (e), by 
others’ stress or pain (j), by self-pain (melittin-induced) or others’ pain (melittin-induced) 
(o), and by self-pain (electric-footshock-induced) or others’ pain (melittin-induced) (q). (f,k) 
Example field of view showing the spatial distribution of cells activated by various states 
of demonstrators. (g,l) Heatmaps showing average responses of example cells (each row) 
activated selectively by a particular state, aligned to the investigation onset (time 0). (h,p) 
Performance of decoders trained on population activity in classifying others’ naïve or pain 
state (h), and observers’ self-licking versus observation of others’ self-licking (p). (m) K-
means clustering of ACC cells based on neural responses to others’ states. Heatmaps show 
the averaged activity changes of individual cells. (r) Responses (mean ± s.e.m.) of cells 
activated by both self-pain and others’ pain. (s-w) Performance of models trained to decode 
the perception of others’ pain versus baseline in predicting self-pain (s, left), others’ pain 
(s, right), or self-grooming (v). Performance of models trained to decode self-pain versus 
baseline in predicting the perception of others’ pain (t, left), self-pain (t, right), others’ naive 
state (u), or self-grooming (w). (h,p,s-w) boxplots showing medians, upper/lower quartiles, 
and minimum/maximum (whiskers); two-sided Wilcoxon singed-rank test. ***P < 0.001, *P 
< 0.05. ns, not significant. See Supplementary Table 1 for details of statistical analyses and 
sample sizes.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 46

Fig. 4. The ACC bidirectionally regulates allolicking and allogrooming behaviors.
(a) Schematic of experimental paradigm for DREADD inhibition of ACC neurons during 
interaction with demonstrators in pain. (b) Example image showing hM4Di-mCherry 
expression in the ACC. Scale bar, 500 μm. ( c-e) Quantification of the cumulative duration 
(c), total duration (d), and bout number (e) of various behaviors towards melittin-injected 
demonstrators by CNO- or saline-injected observers that expressed hM4Di. (f) Schematic 
of experimental paradigm for optogenetic activation of ACC pyramidal neurons during 
interaction with demonstrators in pain. (g) Example image showing ChR2-EYFP expression 
in the ACC. Scale bar, 500 μm. ( h) Example camera frames showing general allogrooming 
and targeted allolicking during optogenetic activation. (i) Quantification of the total duration 
of various behaviors during light on and off periods. n = 16 mice in (c-e) and 18 mice in 
(i). (c) mean ± s.e.m. (d, e, i) center line: median, box limits: upper and lower quartiles, 
whiskers: minimum and maximum values; two-sided Wilcoxon signed-rank test. ***P < 
0.001, **P < 0.01, *P < 0.05. ns, not significant. See Supplementary Table 1 for details of 
statistical analyses.

Nature. Author manuscript; available in PMC 2025 February 01.

 
 
 
 
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

Zhang et al.

Page 47

Fig. 5. Separable representation of allolicking and allogrooming in the ACC.
(a,j,n) Venn diagrams and example calcium traces showing neurons activated during 
either allolicking or allogrooming (a), during either self-licking or allolicking (j), and 
during either allolicking or investigation towards demonstrators in pain (n). (b) Example 
field of view showing the spatial distribution of cells activated during allolicking, 
allogrooming, or both. (c,k,o) Heatmaps showing average responses of example cells 
(each row) activated selectively during either allolicking or allogrooming (c), cells 
activated during either allolicking or self-licking (k), and cells activated during either 
allolicking or social investigation (o), aligned to the onset of each type of behavior. (d) 
Responses of allogrooming or allolicking cells during each type of behavior. (e,l,m,p) 
Performance of decoders in classifying allolicking versus allogrooming (e), allolicking 
versus self-licking (l), allogrooming versus self-grooming (m), and allolicking versus social 
investigation (p). (f,q) Decoder performance relative to behavior onset (time 0) in classifying 
allolicking versus allogrooming (f) and allolicking versus social investigation (q). (g) Two 
hypotheses of neural representations of allogrooming and allolicking towards demonstrators 
experiencing pain or stress. (h) Principal component projections of population activity 
associated with episodes (each dot) of allogrooming towards stressed animals, allogrooming 
towards animals in pain, and allolicking towards animals in pain from one example 
imaging session. (i) Average Euclidean distances in PC space between allogrooming events 
towards stressed animals and animals in pain and between allogrooming and allolicking 
events towards animals in pain. (r) Main conclusion of the study. (d,f,q) mean ± s.e.m. 
(e,i,l,m,p) center line: median, box limits: upper and lower quartiles, whiskers: minimum 
and maximum values; Wilcoxon signed-rank test. All statistical tests are two-sided. ***P < 
0.001, **P < 0.01, *P < 0.05. See Supplementary Table 1 for details of statistical analyses 
and sample sizes.

Nature. Author manuscript; available in PMC 2025 February 01.
