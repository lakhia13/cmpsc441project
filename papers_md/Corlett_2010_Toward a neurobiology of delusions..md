# Corlett_2010_Toward a neurobiology of delusions.

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

NIH Public Access
Author Manuscript
Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

Published in final edited form as:

Prog Neurobiol. 2010 November ; 92(3): 345–369. doi:10.1016/j.pneurobio.2010.06.007.

Toward a Neurobiology of Delusions

P.R. Corlett1,*, J.R. Taylor1, X.-J. Wang2, P.C. Fletcher3, and J.H. Krystal1
1Department of Psychiatry, Yale University, School of Medicine, New Haven, Connecticut, USA

2Department of Neurobiology and Kavli Institute of Neuroscience, Yale University School of
Medicine, New Haven, Connecticut, USA

3Department of Psychiatry, Brain Mapping Unit and Behavioural and Clinical Neurosciences
Institute, University of Cambridge, School of Clinical Medicine, Cambridge

Abstract

Delusions are the false and often incorrigible beliefs that can cause severe suffering in mental
illness. We cannot yet explain them in terms of underlying neurobiological abnormalities.
However, by drawing on recent advances in the biological, computational and psychological
processes of reinforcement learning, memory, and perception it may be feasible to account for
delusions in terms of cognition and brain function. The account focuses on a particular parameter,
prediction error – the mismatch between expectation and experience – that provides a
computational mechanism common to cortical hierarchies, frontostriatal circuits and the amygdala
as well as parietal cortices. We suggest that delusions result from aberrations in how brain circuits
specify hierarchical predictions, and how they compute and respond to prediction errors. Defects
in these fundamental brain mechanisms can vitiate perception, memory, bodily agency and social
learning such that individuals with delusions experience an internal and external world that
healthy individuals would find difficult to comprehend. The present model attempts to provide a
framework through which we can build a mechanistic and translational understanding of these
puzzling symptoms.

Keywords

Delusions; Prediction; Error; Learning; Memory; Reconsolidation; Habit

1. Introduction

Delusions are the extraordinary and tenacious false beliefs suffered by patients with various
ailments ranging from schizophrenia (Schneider, 1959), to traumatic brain injury (Coltheart
et al., 2007), Alzheimer’s (Flint, 1991) and Parkinson’s disease (Ravina et al., 2007), the
ingestion of psychotogenic drugs (Corlett et al., 2009a) and, less frequently, autoimmune
disorders such as Morvan’s syndrome (Hudson et al., 2008) or potassium channel
encephalopathy (Parthasarathi et al., 2006). Given this range of potential diagnoses, each
with its own candidate neuropathology, it is perhaps unsurprising that we have not
converged upon an agreed neurobiology of delusions. Delusions are particularly hard to
study because of their insidious onset and tonic nature, their conceptual rather than
behavioral basis (making them difficult to study using animal models), and the absence of a
coherent theoretical model. We aim to address these issues in the current review by
developing a translational model of delusion formation which we believe makes delusions

*Corresponding Author: Dr. Philip R. Corlett (BA, PhD), philip.corlett@yale.edu, Yale University School of Medicine, Department of
Psychiatry, Connecticut Mental Health Centre, Abraham Ribicoff Research Facility, 34 Park Street, New Haven, CT 06519.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 2

tractable for animal modeling, amenable to investigation with functional neuroimaging and
grounded within a theoretical framework that makes testable predictions.

Our task is made more difficult when one considers the range of odd beliefs from which
people suffer; fears of persecution by clandestine forces (Melo et al., 2006); beliefs that
televisions or newspapers are communicating a specific and personal message (Conrad,
1958b; Startup and Startup, 2005), the conviction that one’s thoughts and movements are
under the control of an external agent or are broadcast out loud (Schneider, 1959); an
unrealistic belief in one’s own fame or power (Karson, 1980; Kraeplin, 1902), that one is
infested with parasites (Thiebierge, 1894) or deceased (Cotard, 1880), or the subject of a
stranger’s love (De Clerambault, 1942), or that family members have been replaced by
imposters or even robots (Capgras, 1923).

We take a cognitive neuropsychiatric approach to delusions. That is, the starting point is to
review what we understand about the healthy functioning of a particular process, e.g.
familiar face recognition, before extrapolating to the disease case, when face recognition
fails and delusions of misidentification form (Halligan and David, 2001). This approach has
proven successful for explaining certain delusions (Ellis and Young, 1990) but not yet for
delusions in general. Perhaps this is because there are difficulties defining delusions as well
as deciding what they have in common (if anything) with normal, healthy beliefs (Berrios,
1991; Delespaul and van Os, 2003; Jones, 2004; Owen et al., 2004). Beliefs are not easily
accessible to the techniques of neuroscience which are more suited to representing states
with clear experiential boundaries (Damasio, 2000). (Knobel et al., 2008).

Furthermore, delusions are difficult to model in animals, given that they involve
dysfunctions of what many consider uniquely human faculties like consciousness, language,
reality monitoring and meta-cognition (Angrilli et al., 2009; Berrios, 1991; Moritz et al.,
2006). Computational models of core cognitive functions (such as working memory) are
being applied to gain insights into neural dysfunction in schizophrenia (Seamans and Yang,
2004; Winterer, 2006) and some are beginning to address the phenomenology of specific
psychotic symptoms (Loh et al., 2007), however, these models have focused on circuit
mechanisms within a local area (like prefrontal cortex), they are unable to capture the
content of particular symptoms which involve information processing across large networks
of interacting brain regions (Fuster, 2001).

There is a need for a testable conceptual model of delusions, one that is rooted in
translational cognitive neuroscience. We, and others, propose that beliefs (both normal and
abnormal) arise through a combination of innate or endowed processes, learning, experience
and interaction with the world (Friston, 2010). Like other forms of information, beliefs are
represented in the brain through the formation and strengthening of synaptic connections
between neurons, for example causal beliefs may be mediated by a strengthening of the
synaptic associations between pools of neurons representing a particular cause and their
counterparts representing an associated effect (Dickinson, 2001; McLaren and Dickinson,
1990; Shanks, 2010). There are neural (and hence cognitive) limits set on the range of
possible connections that can be made (Kandel, 1998). The strength of those connections is
modifiable such that those conveying an adaptive advantage are strengthened and those that
are disadvantageous are weakened (Hebb, 1949b; Thorndike, 1911).

This set of sculpted connections is used to predict subsequent states of the internal and
external world and respond adaptively (Friston, 2005b); however, should that next state be
surprising, novel or uncertain new learning is required (Schultz, 2000). Our premise is based
upon the idea that the brain is an inference machine (Helmholtz, 1878/1971) and that
delusions correspond to false inference. This inference is necessarily probabilistic and rests

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 3

upon some representation of predictions (prediction error) and uncertainty (i.e., precision)
about those predictions. Within this framework, we see delusions as maladaptive beliefs that
mis-represent the world. They might arise through any number of perturbations within this
scheme, from an unconstrained specification of the possible or lawful set of neural
connections (Hoffman and Dobscha, 1989); providing the potential for bizarre beliefs to
form (Hemsley and Garety, 1986a), to an adventitious and inappropriate reinforcement of
particular neural connections (King et al., 1984; Shaner, 1999); engendering unexpected
percepts, attentional capture and beliefs that deviate grossly from reality (Corlett et al.,
2009a; Corlett et al., 2007a; Fletcher and Frith, 2009). Impaired predictive mechanisms have
been previously implicated in delusions of alien control; whereby the sufferer believes their
movements are under the control of an external agent because of an inability to
appropriately predict the sensory consequences of their actions (Frith et al., 2000b). We
propose that this account generalizes from actions to numerous cognitive processes, that
predictive learning and prediction errors are general mechanisms of brain function (Friston,
2005b; Schultz and Dickinson, 2000) and that aberrant predictions and prediction errors
provide a unifying explanation for delusions with disparate contents.

A crucial distinction, which we will appeal to repeatedly, is between prediction errors per se
and the precision or uncertainty about those errors. We will develop the argument that
delusions (and their neurotransmitter basis) represent a failure to properly encode the
precision of predictions and prediction errors; in other words, a failure to optimise
uncertainty about sensory information. Here, prediction errors encode information that
remains to be explained by top-down predictions (Rao and Ballard, 1999). This distinction is
important because it is easy to confuse the role of phasic dopaminergic discharges as
encoding reward prediction error (Montague et al., 1996; Schultz et al., 1997), and the role
of dopamine in modulating or optimising the precision of prediction errors that may or may
not be reward-related (Friston et al., 2009), for example by modulating the signal to noise
response properties of neural units encoding prediction error. In what follows, we will
assume that the pathophysiology of delusions involves a misrepresentation of salience,
uncertainty, novelty or precision (mathematically precision is the inverse of uncertainty).
Biologically, this corresponds to aberrant modulation of post synaptic gain that, presumably,
involves NMDA receptor function (Friston, 2010). This fits comfortably with the role of
dopamine in controlling signal to noise and the numerous proposals that dopamine (at least
in terms of its tonic discharge rates) encodes uncertainty or violation of expectations
(Fiorillo et al., 2003; Preuschoff et al., 2006).

The challenge is to provide empirical data that test the hypothesis. Numerous investigators
have accepted this challenge and, by sharing a set of common simplifying assumptions, we
are beginning to develop an understanding of delusions in the brain. Here, we review this
growing understanding, beginning with a set of principles which, we believe, are important
in developing our understanding of the neurobiology of delusions.

2. Reductionist principles for a neuroscience of delusion

The four principles are as follows: Beliefs and memories share cognitive and neural
mechanisms (1); learning memory and belief influence perception (2); affect impacts upon
learning and memory and hence belief (3); our sense of self, agency, free will and beliefs
about others are governed by the same simple neural learning mechanisms (4). By taking a
reductionist approach, grounded in formal animal learning theory, computational and
cognitive neuroscience we can begin to tackle the hard problems of belief, delusion, and the
brain; problems often considered beyond the scope of neuroscience. Below, we consider the
principles in more detail before discussing their implications for understanding the cognitive
neuroscience of delusions.

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 4

2.1 Beliefs and memories share cognitive and neural underpinnings

Beliefs are notoriously difficult to define (Dennett, 1995), but generally refer to the attitude
we have with regard to propositions about the world. Perhaps a pragmatic analysis might
help. What functions do beliefs serve? Like memories, beliefs help us to organize incumbent
information and coordinate adaptive responses (Dennett, 1995). In other words, though
beliefs and memories are based on past experiences they are utilized to predict the future and
respond accordingly (Corlett, 2009). The most rigorous and formal definition of beliefs
appeals to probability theory, and in particular Bayesian formulations (Bayes, 1763). This
framework, which we use later, associates beliefs with probability distributions that are
represented by the brain (Fiser et al., 2010). These comprise posterior beliefs that are
conditioned upon sensory information and are constrained by prior beliefs. In the context of
hierarchical Bayesian inference, the posterior belief (having seen the evidence) rests on
empirical priors. Empirical priors are prior beliefs that are themselves optimised during
hierarchical inference (Friston, 2005b). Assuming that the brain uses hierarchical inference
to make predictions about the world, most of the beliefs it entertains can be regarded as
empirical prior beliefs. From now on, we will refer to these as prior beliefs or priors and
associate these with the source of top-down predictions that are used to form prediction
errors. Some have equated beliefs with stimulus-response habits in experimental animals:
the behaviors that track previously experienced contingencies but are insensitive to
alterations in those contingencies (Eichenbaum, 2000). Indeed, in view of their tenacity and
tendency to misrepresent true contingency, some have pointed out the similarities of beliefs
to superstitious behaviors (Beck et al., 2007). Thus, beliefs, and therefore delusions, are
regarded as representing adventitiously reinforced superstitions; predictions about the future
that were formed accidentally and inappropriately but that nevertheless persist (Freeman et
al., 2009; Shaner, 1999). Despite capturing aspects of belief phenomenology, these theories
offer neither a mechanistic nor a neurobiological explanation of belief or delusion formation.
This is what we seek here.

One compelling approach equates the process of human belief formation with Pavlovian
conditioning. The same processes that drive animals to learn predictive associations between
sensory stimuli and salient events (rewards or punishments) also contribute to the
acquisition of beliefs in humans (Dickinson, 2001). Expectancy and experience, or, more
specifically, mismatches between the two, are crucial for learning (Alloy and Tabachnik,
1984; Courville et al., 2006; Waldmann, 1998). This mismatch, or prediction error, is central
to formal associative learning theories, driving learning directly (Rescorla, 1972) and
indirectly, via the allocation of attention toward potentially explanatory cues (Pearce and
Hall, 1980). However, there is also a tendency to focus on, and learn about, highly salient
stimuli that consistently predict important consequences (Mackintosh, 1975). Under one
account (Grossberg, 1982), the occurrence of an expected event that matches an active
expectancy will amplify its representation in short-term memory, increasing the likelihood
that it will be consolidated within long-term memory as well as the strength of this
consolidation. By contrast, when an unexpected event violates the active expectancy, an
orienting system is activated which resets short-term memory (dropping active expectancies)
and engages an orienting response, permitting the acquisition of new explanatory
associations. In essence, organisms learn associations between stimuli, events, thoughts and
percepts to build an internal model of their environment. (Sokolov, 1960; Tolman, 1932).
This model is itself predictive and, whenever significant novelty is detected due to a
mismatch between its predictions and actual experience it must be updated (Grossberg,
1982). In short, the allocation of attention toward appropriately salient events depends upon
the optimization of the precision of top-down priors, relative to bottom-up evidence; both in
sensory cortices [involving acetylcholine (Yu and Dayan, 2005)] and in frontrostriatal
circuits [involving dopamine (Friston et al., 2009)].

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 5

This presents the organism with a challenge: to navigate the world successfully, we must
sustain a set of prior beliefs (our internal model), sufficiently robust that we do not react
reflexively and chaotically to any incoming sensory stimulus. At the same time, these beliefs
(priors) must not be so immutable that our responses become fixed, stereotypical and
insensitive to change(Corlett et al., 2009b). According to learning models of delusions,
during the earliest phases of delusion formation aberrant novelty, salience or prediction error
signals drive attention toward redundant or irrelevant environmental cues, the world seems
to have changed, it feels strange and sinister, such signals and experiences provide an
impetus for new learning which updates the world model inappropriately, manifest as a
delusion (Corlett et al., 2009a; Corlett et al., 2007a; Gray, 2004, 1991; Hemsley, 1994;
Kapur, 2003). The insight relief that delusions bring engages strong memory consolidation,
furthermore, they are deployed reflexively in response to similar aberrant experiences
(Mishara, 2009) and as such, they are rapidly rendered impervious to contradiction (Corlett
et al, 2009a, see below).

2.1.1 Neural instantiation of predictive learning and belief—Midbrain dopamine
neurons in substantia nigra (SN) and ventral tegmental area (VTA) code a reward prediction
error (Montague et al., 1996; Schultz et al., 1997). When primates (Schultz et al., 1993;
Waelti et al., 2001) and rodents (Takahashi et al., 2009) learn, activity in these neurons
reflects a mismatch between expected and experienced reward that is redolent of the
prediction error signal from formal learning theories (Waelti et al., 2001) and machine
learning models (Montague et al., 1996; Sutton, 1998). However, recent studies have
identified punishment prediction error signals (Matsumoto and Hikosaka, 2009) and
mismatches between expected and experienced information (Bromberg-Martin and
Hikosaka, 2009) in distinct anatomical populations of midbrain dopamine neurons,
suggesting that these neurons and the circuits in which they are embedded are involved in
the processing of salient events that will guide future adaptive behavior, for both positively
and negatively valenced events (Hikosaka et al., 2008a). In human subjects, a circuit
involving the midbrain and its projection sites in the striatum and prefrontal cortex signal
prediction errors that guide causal learning (Corlett et al., 2004; Fletcher et al., 2001; Turner
et al., 2004).

Prediction error-driven learning and memory may represent a basic mode of brain function,
referred to as predictive coding (Friston, 2005b, 2009; Schultz and Dickinson, 2000), that is,
brains, component brain systems and even single neurons minimize uncertainty about
incident information (either external or internal) by structurally or functionally embodying a
prediction and responding to errors in the accuracy of the prediction (Fiorillo, 2008). Rapid
excitatory and inhibitory neurotransmitters (glutamate and GABA) interact with slower
neuromodulatory transmitters to instantiate this predictive coding scheme (Friston, 2005b,
2009), but the precise mechanism for computing prediction error signals remain poorly
understood. Across successive levels of cortical hierarchies, top-down signaling from
neurons in layers higher up the hierarchy confer expectancies, possibly through
glutamatergic NMDA receptors but this is still not established empirically. Bottom-up inputs
to a layer are signaled from the layer below through fast glutamatergic and GABAergic
mechanisms. At a given level, any mismatch between expectancy and experience is
transmitted up the cortical hierarchy to the level above via AMPA receptor signaling
(Angelucci et al., 2002a; Angelucci et al., 2002b; Friston, 2005b, 2009; Sherman and
Guillery, 1998). Slower neuromodulatory transmitters, like dopamine, acetylcholine,
serotonin and cannabinoids are engaged (Corlett et al., 2009a), mediating the post prediction
error response by encoding the precision of or uncertainty associated with a particular
prediction error(Friston, 2005c). Such uncertainty signals engage subsequent processing
such as enhancing neural maintenance of working memory (Lavin et al., 2005) and
modulating synaptic plasticity down the hierarchy thus tuning subsequent responses (Grace,

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 6

1991; Herrero et al., 2008). We shall refer this perspective on cortical processing, through
feedforward signaling of sensory stimuli and feedback signaling of expectation and priors,
as the Bayesian model.

According to this model, a prior belief is updated by prediction errors to provide a
probabilistic prediction of expected inputs. Input probabilities are learnt at synapses by
virtue of experience-dependent learning (Soltani and Wang, 2010), and read out at the level
of neural activity populations (Ma et al., 2006) . However, beliefs and priors are more than
expectancies; strong prior beliefs can enhance, attenuate or vitiate sensed inputs sculpting
them to conform to expectations (Jaspers, 1963). The power of prior expectancies can be
observed in visual illusions, for example the hollow mask illusion in which a hollow mask is
perceived as a convex face as a result of extended lifetime experience that faces are not
concave but convex. Likewise strong neural priors can sculpt input signals so that they
conform to expectancies (Rao and Ballard, 1999). Beliefs then, not only provide a
mechanism through which current information is interpreted in light of the past; they involve
an inductive inference that ensures experiences conform with expectancies (Clifford, 1877) .
In associative learning, such behavioral inflexibility involves training in which expectancies
are continuously confirmed (Adams, 1981). The representations and neural circuits
controlling behavior gradually shift from more plastic goal-directed, knowledge-based
frontal, temporal and ventral striatal regions of the brain toward more inflexible habitual
behavior, decreased involvement of frontal cortices and a shift toward dorsal striatal circuits
(Belin et al., 2009; Daw et al., 2005; Eichenbaum, 2000). This shift is marked by an
increasing strength of the behavior even when the contingency no longer pertains or when
the consequences of that behavior are no longer desired.

Whilst Bayesian models are often considered rational and optimal (Shanks, 2008), they have
nevertheless been deployed to explain irrational processes such as the spread of panic and
rumor within a crowd (which occurs rapidly in salient situations with few explanatory
priors; Butts, 1998) and, more recently, a biophysically plausible model offers an
explanation for base rate neglect in probabilistic decision making (Soltani & Wang, 2010).
Essentially we advocate an explanation of delusions as a disruption to the normal Bayesian
predictive mechanisms of the brain such that predictable and irrelevant events mismatch
with expectancies and their salience demands new learning and explanation; a delusion
represents an explanatory mechanism, an attempt to impose order on a disordered perceptual
and cognitive world (McReynolds, 1960; Maher, 1975; Gray et al, 1991; Kapur, 2003;
Corlett et al, 2007; Fletcher & Frith, 2009; Corlett et al, 2009a).

2.1.2 Oscillation signatures of match and mismatch events—In our introduction
we alluded to the importance of dysfunctional neural circuits (rather than isolated regions)
when considering the pathophysiological mechanisms underpinning delusions. That is,
psychoses could be conceived as ‘disconnection syndromes’ (Friston and Frith, 1995). Inter-
and intra-regional neural connections and disconnections are still poorly understood at the
present time. One of the active research areas is the examination of the role of neural
oscillations in inter-areal communication (Uhlhaas et al., 2008; Uhlhaas et al., 2006a;
Uhlhaas and Singer). For example, oscillatory activity in the gamma frequency band (30–
50hz) contributes to synchronizing populations of neurons in different brain regions,
mediating the temporal structuring of neural activity necessary for sharing, transfer and
storage of information (or learning) between these groups of coordinated cells or cell
assemblies (Buzsaki, 2007). Such oscillations are thought to reflect the engagement of high
level cognitive processes such as attention (Joliot et al., 1994). A recent computational
model of selective attention, consisting of a reciprocally connected loop between a sensory
circuit and a high-level cognitive circuit, found that top-down signaling enhances gamma-
band oscillatory coherence only when there is a match between the attended stimulus feature

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 7

(expectation) and the actual stimulus feature (experience), and that this occurs exclusively in
sensory neurons selective for the actual feature and in memory neurons (that are the source
of top-down signaling) selective for the attended feature (Ardid et al., 2010).

Learning from the violation and confirmation of our expectancies can both be traced in
oscillatory activity of recurrent neural circuits (Grossberg, 2009). Match based learning
captures the Hebbian notion of cell assemblies; collections of synaptically interconnected
cells whose pre- and post- synaptic firing correlates and becomes mutually excitatory such
that when a fraction of an input pattern is incident upon the assembly, the whole output is
realized (Hebb, 1949a). In human learners, gamma oscillations (measured using EEG)
increase during acquisition of new associations, as does the coherence of oscillations in
cortical regions representing the stimuli being associated (Miltner et al., 1999). Neural
synchrony impacts on learning because synaptic plasticity depends on the timing of pre- and
post- synaptic neural spikes (Bi and Poo 2001).

But as we have observed, learning does not proceed by contiguity alone (Konorski, 1948).
Cell assemblies also represent events that do not match our expectancies (O’Donnell, 2003).
In terms of synaptic machinery, one type of mismatch based learning, which is based on
expected rewards, appears to be implemented in the mesocorticolimbic system through a tri-
synaptic arrangement between pre and post-synaptic glutamatergic signaling with a
modulatory role for the dopaminergic prediction error input from VTA (Pennartz et al.,
2000; Schultz, 1998). Ensembles of neurons are defined by their membrane potential states;
periods of very negative resting membrane potential or down states are periodically
interrupted by a plateau depolarization or Up state (Haider et al., 2006; Ros et al., 2009;
Sanchez-Vives and McCormick, 2000). Striatal up states are synchronized with those in
frontal cortex (Goto and O’Donnell, 2001). Dopamine D2 receptor signaling is associated
with an instability of prefrontal representations (Seamans and Yang, 2004), providing an
ensemble-level mechanism for surprise driven resetting of representations, search and new
learning (Braver and Cohen, 1999; Grossberg, 1982). On the other hand, dopamine, acting
through D1 receptors and their interaction with NMDA channels facilitates the maintenance
of Up-states in target neurons (Cepeda and Levine, 1998; Wang and O’Donnell, 2001) and
reinforces cell assemblies representing expected salient events (O’Donnell, 2003). In this
scheme, the excessive D2 signaling, impaired D1 and impoverished NMDA signaling that
comprise psychotic states would lead to a poor specification of prior expectancies and
frontostriatal cell assemblies comprised of cells representing merely coincident events and
spurious associations.

But, how are predictions and prediction errors reflected more generally in the oscillatory
signals of cortical hierarchies? While gamma oscillations are commonly enhanced under
conditions that involve cognitive control, the top-down specification of priors may be
reflected in beta-band (15–30 Hz) oscillations (Wang, In Press). For instance, when
recordings are made from the lateral intra-parietal cortex and prefrontal cortex of behaving
monkeys during a visual search task, the inter-areal cohence is enhanced in the beta
frequency band when the target and distractors are similar and visual search depends on top-
down signalling, relative to when the target and distractors are dissimilar and target
detection is based by feedforward perceptual ‘pop-out’ (Buschman and Miller, 2007).

Cortical areas have a well defined laminar structure and, in the neocortex, gamma band
oscillations are prominent in superficial layers (2/3) endowed with abundant horizontal
connections (Binzegger et al., 2004; Buhl et al., 1998). In contrast, deeper layers (5/6) tend
to display lower frequency beta-band oscillations (Wang, In Press). Between reciprocally
connected cortical areas, feedforward projections from a lower to a higher area originate in
superficial layers of the lower area. Feedback connections begin in deep layers of the higher

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 8

area and project to superficial layers of the lower area as well as subcortical structures. Thus
beta oscillations, produced in the deep layers, may be especially involved in long distance
signaling along feedback pathways. Top-down beta oscillations may encode the expectations
that guide match-based learning and perception (Berke et al., 2008). Moreover, prior
specifying, beta-frequency oscillatory feedback signals emanating from a ‘cognitive area’
project to superficial layers 2/3 in a ‘sensory area’, hence are well suited to modulating
gamma oscillations that are locally generated in the superficial layers, in a context
dependent manner (Wang, 2010).

There are competing theories regarding the roles of different oscillatory bands in conveying
neuronal predictions and prediction errors (Grossberg, 2009). For example, the relationship
between high frequency gamma and lower frequency theta band oscillations in hippocampal
neurons appears important for the recall of temporal sequences of events (Lisman and
Buzsaki, 2008), this form of coding may be especially important in specifying predictions
about the future (Lisman and Redish, 2009) and, if it is disrupted, prediction errors may
result (Lisman and Grace, 2005); these aberrant errors may be propagated to target
structures though inappropriate entrainment of oscillations between structures (Sirota et al.,
2008). Furthermore, there are magnetoencephalography data suggesting that, during a face
perception task in human subjects, higher-frequency gamma oscillations at lower levels of a
neural hierarchy can entrain lower frequency (alpha-band) oscillations in regions higher up
the hierarchy, which may represent accumulating prediction error for perceptual synthesis
(Chen et al, 2010). Through nonlinear coupling, gamma oscillations in the higher region
increase, providing a mechanism through which ascending prediction errors are damped
down or explained away (manifest as a decrease in alpha-band power; Chen et al, 2010).
More data are clearly required. However, we can predict that in delusion-prone individuals,
if predictions are poorly specified and errors signalled inappropriately, then low frequency
oscillations, gamma oscillations and their interaction should be perturbed. Consistent with
this prediction, highly schizotypal subjects have electrocortical responses to sensory
stimulation in the gamma and beta frequency ranges that were slower to habituate following
repeated presentation of the stimuli, indicative of maladaptive prior expectancies as well as
aberrant prediction error responses (Vernon et al., 2005). Furthermore, patients with
schizophrenia have reduced long-range phase synchrony in the beta band during gestalt
stimulus perception, perhaps indicative of aberrant prediction error. This aberrant signalling
correlated with delusion severity across subjects (Uhlhaas et al., 2006a).

2.1.3 Delusions as aberrant neural learning—Excessive and inappropriate dopamine
signaling is thought to render merely coincident events highly salient (Gray, 1991; Hemsley,
1994; Kapur, 2003), this may result from a dysfunction in glutamatergic and GABAergic
signaling and thence, the regulation of dopamine signaling (Carlsson et al., 2001; Grace,
1991; Laruelle et al., 2003). Either directly or indirectly, this dysregulation leads to the
inappropriate signaling of prediction error (Corlett et al., 2007a; Grace, 1991; Gray, 1991).
Since prediction error may guide attention toward events that may explain the feeling of
surprise or uncertainty (Pearce and Hall, 1980) and engage learning mechanisms (Rescorla,
1972), we can see that such a disruption has could lead to altered attention, learning, and
ultimately belief formation. To consider the nature of this disruption in a little more detail,
inappropriate prediction error signals could be conceived of as resulting from a change in
the signal to noise properties of dopamine signaling (Grace, 1991; Miller, 1976; Spitzer,
1995); due to deficits in glutamatergic regulation of VTA dopamine neurons. Physiological
noise is perceived by the system as real signal that engenders the cascade of events that a
true prediction error would engage, namely a search for explanation and new learning.
Ultimately, both of these possibilities; inappropriate prediction error and an altered signal to
noise ratio of the dopamine system; are reflective of poor precision in the estimation of
prediction error (Friston et al., 2009; Preuschoff et al., 2006), which will vitiate inference,

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 9

biasing it toward misrepresenting inputs (be they sensory or neural). If persistent, this
imprecision may ultimately lead to the formation of a new explanatory prior, or delusion,
that consolidates the misrepresentation allowing it to pervade the deluded individual’s future
perception and action (Jaspers, 1963). Aberrant mesocorticolimbic prediction error signals
have been recorded during causal learning with functional neuroimaging in patients with
schizophrenia and furthermore, the magnitude of those signal aberrations correlated with the
severity of delusions across subjects (Corlett et al., 2007b) [See Figure 1].

The relationship between conditioning and delusions has also been confirmed in the context
of a reward learning task (Schlagenhauf et al., 2009) and an aversive conditioning task (Holt
et al., 2008); in both cases, aberrant learning was related to the severity of delusional beliefs.
It appears that the brain systems that govern normal causal belief formation are internally
and inappropriately engaged when delusions form.

2.1.4 Multiple neural origins for prediction error and its dysfunction?—The
computation of VTA prediction error signals involves the interplay between the basal
ganglia and the prefrontal cortex (Schultz, 2007; Soltani and Wang, 2008), especially the
anterior cingulate cortex (Matsumoto et al., 2007; Rushworth and Behrens 2008) and the
orbitofrontal cortex (Schoenbaum et al., 2010). Other studies point to hippocampus,
specifically for signaling novelty in the form of mismatches between actual and expected
information (i.e. prediction errors) which may then be transmitted to the VTA via the
striatum (Lisman and Grace, 2005). This signaling of unexpected and salient events causes
the organism to stop its ongoing behavior and search for explanatory cues (Gray, 1991).
Patients with psychosis have increased regional cerebral blood flow (an indirect measure of
neural activity) in CA1 and, those in whom this effect is most pronounced have the most
severe delusions (Schobel et al., 2009). Likewise, individuals in the prodrome (the very
earliest phases of psychosis) release more striatal dopamine than controls and again, the
magnitude of that dopamine release correlates with the severity of delusion like ideas
(Howes et al., 2009). Contrary to the predictions of Gray and Kapur, this dopamine
dysfunction has been observed not in the limbic striatum but in the associative striatum, a
sub-region that is reciprocally connected with the dorsolateral prefrontal cortex (Haber,
2003; Haber et al., 2006). The latter is a part of the circuit engaged by prediction error
driven learning and, moreover, shows aberrant responses in subjects experiencing disturbed
percepts and odd beliefs (Corlett et al., 2004; Corlett et al., 2006; Corlett et al., 2007b). We
dicuss these observation in more detail below.

The rapidity with which reward prediction error signals are registered in VTA (of the order
of milliseconds) may be incommensurate with the calculation of a reward prediction error
(Redgrave and Gurney, 2006). Instead these signals could represent unexpected sensory
events through cholinergic inputs from the pedunculopontine tegmentum (Dommett et al.,
2005), or PPT, inputs which are combined with context representations from the prefrontal
cortex and hippocampus as well as motor representations from the putamen in order to
ascertain whether the organism or the environment was responsible for the unpredicted
event. This agency account suggests that dysfunctions in dopamine signaling could explain
both the sense of excessive agency for events in the world associated with paranoia (Kaney
and Bentall, 1992) as well as the externalization of agency associated with delusions of
passivity (Blakemore et al., 2002; Frith et al., 2000a). See below.

A further candidate site for prediction error dysfunction in psychosis is the habenula
(Shepard et al., 2006). The habenula, in concert with the prefrontal cortex, is responsible for
instantiating negative prediction error signals in the VTA; the dips below baseline firing that
engage extinction learning; abandoning what we have previously learned in favor of a new
prediction (Pan et al., 2008). A deficit in this signaling would raise baseline

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
Corlett et al.

Page 10

mesocorticolimbic dopamine levels (Lecourtier et al., 2008) and impair extinction learning
(Holt et al., 2008; Waltz et al., 2007), perhaps explaining why deluded individuals stick with
maladaptive and erroneous ideas (or corticostriatal cell assemblies) despite their
demonstrable falsehood(Corlett et al., 2009c).

Bringing these observations together, it appears that the mesocorticolimbic dopamine system
codes numerous types of expectation, their violation and the new learning that expectancy
violation engenders; permitting adaptation to prevailing environmental contingencies
(Schultz and Dickinson, 2000). When events that violate perceptual expectations are
experienced, the hippocampal projection to the striatum engages a broader population of
dopamine neurons in the VTA (Lodge and Grace, 2006a). Furthermore, the prefrontal cortex
maintains higher level expectancies representing goals and the actions required to achieve
those goals (Grace et al., 2007; Sesack and Grace, 2010) as well as reward values for
sensory stimuli (Schoenbaum et al., 2010) and actions (Rushworth and Behrens 2008).
When events occur that violate those expectancies, PFC modulates the responses of active
VTA dopamine neurons: engaging burst firing through its influence over the PPT (Lodge
and Grace, 2006a, b), allowing updating of expectancies through new learning. Furthermore,
PFC enables the quiescence of those same VTA neurons (through its influence on the
habenula) when contingencies change and learning is extinguished (Hikosaka et al., 2008b;
Pan et al., 2008). Reciprocal connections between VTA, PFC, striatum and hippocampus are
involved in this updating process so that future expectancies conform to the prevailing
environmental contingencies.

We predict that delusions are associated with a threefold disturbance in this circuitry: (i)
Excessive hippocampal drive to VTA (via striatum) engaging a broader population of VTA
dopamine neurons; (ii) Inappropriate engagement of PPT due to PFC dysfunction,
instigating burst firing in that expanded pool of recruited neurons and (iii) Impaired
habenula mediated inhibition of VTA dopamine neurons (which would normally instantiate
extinction learning when an expected event fails to occur).

These three deficits would confer the cardinal characteristics of delusions, their bizarreness
and tenacity: Bizarreness; due to the aberrant recruitment of VTA cells and their
incorporation into cell-assemblies which sculpt future expectancies; and tenacity; due to the
failure of PFC to control the habenula, and hence co-ordinate the dips in VTA neuron firing
below baseline that engage extinction learning when the predictions of the delusion are not
borne out.

While this model begins to implicate aberrant learning processes in delusion formation, it
does not address the range of different themes that form the content of delusions, nor does it
fully explain the behaviors in which deluded individuals engage when confronted with
evidence that challenges their belief (see below). In order to extend out explanation to
encompass these characteristics, we discuss below what we consider to be key factors: the
role of beliefs in instrumental conditioning (learning the relationships between our actions
and their effects in the world) and the impact of repeated recall and rehearsal of that
information on subsequent processing.

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

2.2 Learning, memory and belief alter perception

Perception is substantially constructive. That is, our expectancies (based on previous
experience) contribute to what we currently perceive by sculpting sensory inputs (Bruner et
al., 1949; Helmholtz, 1878/1971). The concepts and categories we have learned through
experience can influence what we perceive, for example, if subjects are shown simple
objects and asked to reproduce their colors, their responses are heavily influenced by the
shape of the object (Goldstone, 1995). Motivational state, itself interacting with learning and

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 11

memory (Berridge, 2007), can impact upon perceptual judgment; poorer children judge
coins to be larger and heavier than do richer children (McCurdy, 1956). When presented
with noisy, unstructured visual inputs, hungry subjects claim to see food objects (Atkinson,
1948). The impact of motivation on bottom-up perceptual inputs may be mirrored in the
mechanisms we use to imagine given percepts, a mechanism which, when inappropriately
engaged may elicit hallucinations (Grossberg, 2000) and the impaired reality monitoring
associated with delusional ideation (Simons et al., 2008)). For example, the spontaneous
confabulations of patients with orbitofrontal lesions represent an excessive influence of past
experience on current perception (Schnider, 2001) and delusional misidentification may
reflect a failure to specify perceptual expectations such that known people or places lack a
sense of familiarity (Fleminger, 1992) .

2.2.1 Neural mechanisms of the memory-perception cycle—Predictive coding and
prediction error may be a basic mode of brain function (Friston, 2005b, 2009; Mesulam,
2008). This theory is best encapsulated by sensory cortices, in particular the visual cortex;
whose anatomy recapitulates the idea of a hierarchically organized predictive coding system.
Further up the neural hierarchy, more distal to the site of sensory input, approaching
association cortices, the representations of sensory stimulation become more abstract
(Mesulam, 2008). But the percept does not emerge as a consequence of a simple uni-
directional progression up this hierarchy (Sperry, 1990). Rather the hierarchy is nested
(Feinberg, 2000; Feinberg and Keenan, 2005) or enriched by interactions (feedback as well
as feedforward) between its layers (Friston, 2005b, 2009). These interactions are instantiated
by sparse and rapid feedforward AMPA and GABAergic signaling meeting feedback
(possibly NMDA-mediated) signaling representing predicted inputs embodied in the layers
above (Friston, 2005b). Any mismatch between expectancy and experience (signaled via
AMPA receptors) can serve to update future priors. Dysinteractions within this Bayesian
hierarchical arrangement may be responsible for the symptoms of psychosis (Corlett et al.,
2009a; Fletcher and Frith, 2009). For example, in the absence of stable prior expectancies,
certain perceptual illusions may not be perceived by patients with schizophrenia (Dakin et
al., 2005; Dima et al., 2009; Emrich, 1989) nor individuals administered NMDA receptor
antagonists (Phillips and Silverstein, 2003) perhaps indicative of a common underlying
mechanism [although see (Passie et al., 2003) for a dissociation between the effects of
ketamine on a perceptual illusion and its psychotomimetic effects]. See Figure 2.

The thalamus has also been strongly implicated in conscious perception. Thalamocortical
circuits have intrinsic resonance in the gamma frequency range which is critical for
conscious perception, prediction and learning (Steriade et al., 1991). GABAergic neurons in
the basal ganglia projecting to the thalamus exert an inhibitory influence on thalamocortical
neurons thus protecting the cortex from sensory overload (Sharp et al., 2001). Hyperactivity
of dopamine or hypo-activity of glutamate in the striatum would compromise these
protective mechanisms leading to excessive cortical stimulation and psychosis (Carlsson et
al., 2001; Carlsson and Carlsson, 1990; Geyer and Vollenweider, 2008). Such a deficit could
conceivably alter the sense of background and foreground that permeates normal perception
(Conrad, 1958a). This could explain why other Gestalt principles, which involve grouping
the perceptual field on the basis of learned environmental regularities (Fiser, 2009; Vickery
and Jiang, 2009), are impaired by psychotomimetic drugs that alter dopaminergic and
glutamatergic function (Kurylo and Gazes, 2008). Gestalt organizing principles are similarly
disrupted in patients with schizophrenia (Silverstein et al., 2006; Uhlhaas and Mishara,
2007; Uhlhaas et al., 2006b).

Like other systems, thalamocortical circuits and their interaction with cortical information
processing have been subject to a Bayesian analysis (Koechlin et al., 1996). According to
this scheme, thalamocortical information represents the feedforward aspect (the information

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 12

being represented) and cortico-cortical processing represents the prior expectancies, the
operations to be performed on that information. Similar models have been developed to
account for perception of coherent visual motion and mental rotation, as well as the
predictive functions involved in enacting adaptive movements (Koechlin et al., 1996; Llinas
and Roy, 2009).

Inherent in all of these related schemes is the notion of a balance, between bottom-up and
top-down (or feedforward and feedback) signaling. This balance is necessary in order to
meet the afore-mentioned challenge of a system that is robust to noisy inputs (through
reliance on empirically derived prior expectations) but is also flexibly responsive to new
contexts and situations (through the capacity to alter priors on the basis of bottom-up signal).
With this in mind, it is clear that, in addition to poorly specified predictions, excessively
strong priors may be profoundly disruptive and psychotogenic (Corlett et al., 2009a).
Perceptual associations between sensory modalities appear to be learned using
mesocorticolimbic prediction error signals (den Ouden et al., 2010; den Ouden et al., 2009),
which may explain the phenomenon of sensory conditioned hallucinations (Ellison, 1941;
Seashore, 1895) whereby, learned associations between sensory stimuli (a tone predicts light
stimulation for example) alter perception, such that presentation of one stimulus (tone)
induces experience of the other (light) even though the latter is not present. Learned
associations can alter perception; Hallucination-prone individuals are more susceptible to
experiencing sensory conditioned hallucinations (Kot and Serper, 2002). Likewise
delusional beliefs can alter percepts such that they conform to the delusion (Jaspers, 1963).
Excessively strong top-down predictions may explain the psychotogenic effects of LSD and
sensory deprivation (Corlett et al., 2009a). Furthermore, individuals prone to abnormal
experiences and beliefs are more susceptible to the Deese-Roediger-McDermott memory
illusion whereby they claim to have experienced an event that was strongly expected but
nevertheless did not occur (Corlett et al., 2009d). We predict that such expectation-based
psychotic phenomena would be associated with inappropriate gamma and beta oscillations,
reflective of inappropriate reverbatory activity in recurrent neural circuits and of pattern
completion within Hebbian cell assemblies that are not relevant to the situation at hand.

2.3 Affect impacts upon learning, memory, perception and hence belief

The aberrant percepts that drive delusion formation often occur during periods of stress and
are themselves anxiogenic (Keinan and Keinan, 1994). Furthermore, individuals with a low
tolerance for ambiguity are more prone to paranormal beliefs and odd experiences (Houran
and Houran, 1998). Some models posit a vicious circle in which fear and aberrant perception
are mutually reinforcing and demand explanation, culminating in a delusion which then
subtends future aberrant percepts and inappropriate fear (Lange et al., 1998; Pally, 2007).
These models are descriptively compelling but are expressed largely at the higher cognitive
level. We seek a more fundamental neural and cognitive explanation. Simply put, we argue
that affectively charged uncertainty drives delusion formation, through establishment of
predictive associations that, whilst maladaptive, represent attempts to render the world more
predictable.

2.3.1 Neural mechanisms of affective modulation—The uncertainty engendered by
aberrations of experience is affectively charged (Vinogradov et al., 1992). Affective learning
is also prediction error driven, involving a circuit incorporating the VTA, amygdala and
hippocampus as well as the striatum and prefrontal cortex (Delgado et al., 2008b; Laviolette
and Grace, 2006; Milad et al., 2007; Milad et al., 2004; Schiller et al., 2008). Dysfunctions
within these nodes could engender fear in the wrong context, leading to maladaptive
learning about the danger of adverse consequences. The top-down instantiation of extinction
learning is particularly interesting in this respect; the dopaminergic and GABAergic

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 13

mechanisms that override old fear learning with new extinction learning (Bissiere et al.,
2003) may be impaired in schizophrenia (Holt et al., 2008). It is clear that paranoia could be
accounted for parsimoniously by appealing to an inappropriate engagement of the brain’s
fear system and its persistence by an impairment of the brain’s mechanisms of extinction.

The amygdala is crucial for fear learning in rodents and humans (Critchley et al., 2002;
Morris et al., 2002). However, its role may not be limited to fear; the amygdala is involved
in coding, processing and learning about salient stimuli (Balleine and Killcross, 2006; Paton
et al., 2006). The link between fear and uncertainty is emphasized by theorists who posit that
the amygdala is also engaged during conditions of uncertainty about biologically relevant
stimuli that warrant vigilance (Sander et al., 2003; Whalen et al., 1998). For example, fearful
faces represent ambiguous stimuli, since they signal the presence but not the source of threat
(Whalen et al., 2001). Amygdala responses to appetitive and aversive events are modulated
by predictability, being more marked when salient events are uncertain (Belova et al., 2007).
In this respect, it is noteworthy that animals with lesions of the central nucleus of the
amygdala do not allocate more attention to surprising events (Holland and Gallagher,
1993b).

Cholinergic interneurons in the substantia innominata/nucleus basalis and their projections
to posterior parietal cortices are important for the surprise-induced enhancement of attention
(Chiba et al, 1995; Bucci et al, 1998; Han et al, 1999). In humans, cues that predict aversive
events engage both striatum (Delgado et al., 2008a) and amygdala (Schiller et al., 2008) but
only the striatum codes aversive prediction error (Schiller et al., 2008), suggesting that the
amygdala is involved in representing the salience of events learned as a consequence of
prediction error signals transmitted from other regions. Aberrant prediction error responses
in the midbrain or striatum could therefore encourage inappropriate assignment of
significance to stimuli, thoughts and percepts (Kapur, 2003) which are then allocated
attention in the amygdala (Laviolette and Grace, 2006) through changes in fronto-parietal
spatial representations (Mohanty et al., 2009). These environmental contingencies are also
subjected to strong consolidation through changes in synaptic strength in the rhinal and
entorhinal cortices (Hikosaka et al., 2008a), hence, future encounters with similar cues will
engender rapid and powerful predictions of aversive stimulation which would engage
avoidance behaviors. Impairments in this system could then contribute to the maintenance of
paranoia (Freeman et al., 2007; Moutoussis et al., 2007).

Uncertainty is a powerful and uncomfortable experience. A consequence of such perceived
and unsettling lacking of control is that subjects strive to find consistent relationships. They
consequently become prone to finding illusory patterns, seeing figures in noise, recognizing
correlations between unrelated events, creating superstitious rituals and endorsing
conspiracy beliefs (Whitson and Galinsky, 2008). We contend that these healthy coping
mechanisms are magnified in individuals with psychosis, culminating in the formation of
delusions. These ‘filling in’ processes may result from top-down influences of orbitofrontal
cortex, which receives information from the each modality-specific cortical pathway
specifying what a particular sensory object is (Rolls et al., 2008), for example; the inferior
temporal cortex where object and face identity are encoded (Rolls, 2007) and the superior
temporal sulcus where face expression and gesture are represented (Hasselmo et al., 1989a;
Hasselmo et al., 1989b). Furthermore, the orbitofrontal cortex has inputs from the amygdala
and the ventral tegmental area (Takahashi et al., 2009) which may drive its ability to learn
affective value representations (Padoa-Schioppa and Assad, 2006) which appear to modulate
perception in a top-down manner (de Araujo et al, 2005); when affectively charged external
labels are applied to percepts, OFC responses bias cingulate and striatal responses in the
direction of the label (Grabenhorst et al., 2008). Furthermore, damage to the OFC can result
in spontaneous confabulation, a delusion-like disorder in which patients confuse ongoing

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 14

reality with past experiences (Schnider, 2003). Thus, hyper-engagement of top-down
attentional biases may contribute to the aberrant salience underpinning delusional beliefs
(Kapur, 2003) as well as to their maintenance (Corlett et al., 2009a; Corlett et al., 2009c).

2.4 Simple synaptic learning and memory mechanisms of belief govern

2.4.1 Our sense of self, agency and free will—Like beliefs, the self is difficult to
define and multifaceted (Mishara, 2007). We will focus on one conception of self, that of an
agent that is responsible for actions (Wegner, 2004). In this respect, excessive agency
accounts of paranoia (Kaney and Bentall, 1992) may be enriched by a consideration of the
phenomenon of superstitious instrumental conditioning (Skinner, 1948), in which spurious
associations are learned between an action and a salient outcome and the action persists
despite there being no causal connection between it and the salient outcome. An excessively
noisy dopamine system would be fertile grounds for superstitions, which are essentially
delusional associations that are reinforced between merely coincident thoughts or actions
and environmental events (Shaner, 1999). According to action reselection hypotheses of
dopaminergic prediction error signals (Redgrave and Gurney, 2006), inappropriate
dopaminergic prediction error signals would confer a spurious sense of agency for events.

Initial lesion studies suggested that hippocampal damage increased superstitious learning in
experimental animals (Devenport, 1979). However, more extensive investigations
implicated the parietal cortex in superstitious responding, suggesting that collateral damage
to this region of cortex may have occurred when the hippocampus was aspirated (Mittleman
et al., 1990). Elevated superstitious responding has been demonstrated in chronic ketamine
users with delusion like ideation and perceptual aberrations (Freeman et al., 2009) and
patients with schizophrenia who have delusions (Roiser et al., 2009), although the rate of
superstitious responding in (presumably non-delusional) control subjects was high in both of
these studies.

Lesions of the parietal cortex grossly alter bodily perception and representation, for
example, hemi-spatial neglect involves a failure to appreciate half of the body, external
world and mental images (Bisiach and Luzzatti, 1978). Perhaps another function of the
parietal cortex in instrumental learning involves keeping track of the sense of self as agent in
the environment (Farrer et al., 2008). Wegner and others hypothesize that a sense of self
agency may be learned through experience; having an intention to act very frequently
precedes the action itself and this contiguity binds intentions with actions through
associative learning (Glymour, 2004; Hume, 1739/2007; Wegner, 2004). This system can be
fooled using subliminal prime events that alter the contiguity between actions and outcomes
(Aarts et al., 2005) and furthermore, subjects judge the time between performing an action
and producing an outcome as shorter when the action was intentional, a process of action-
outcome binding (Moore et al., 2009). Schizophrenic patients with severe positive
symptoms show a hyper-binding effect, an exaggerated binding between their actions and
the outcomes they produce, consistent with a disturbed agency account of paranoia (Franck
et al., 2005; Haggard et al., 2003). This process of learned intentionality has been modeled
using Bayesian mechanisms; in essence, the task of inferring causal agency involves
conditioning the evidence (whether the outcome occurred?) over the priors (was there an
intention to act and would the outcome be consistent with the outcome performed?
(Hendricks, 2007; Lau et al., 2007). Inappropriate engagement of this inference mechanism
could account for excessive and inappropriate agency underpinning, for example, beliefs in
telekinesis or telepathy, but what about delusions of passivity or external control?

The parietal cortex has also been implicated in passivity experiences through prediction
error; in this case, the mismatch between expected and experienced consequences of
movements (Schnell et al., 2008). Producing movements over which we feel a sense of

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 15

agency also involves predictive learning and prediction error (Blakemore et al., 2002).
Again, a Bayesian mechanism may underlie motor control; an internal predictive model of
motor commands which is used to predict the sensory consequences of movements and
compare them with the actual sensory feedback during movement execution (Wolpert et al.,
1995; Wolpert and Miall, 1996). The cerebellum appears to store internal world models and
compute discrepancies between predicted and experienced sensory consequences of actions
(Blakemore et al., 2001). Event related functional MRI studies of the period before a
movement show that activations changes in the cerebellum and PFC occur several seconds
before movement onset and the degree of cerebellar activation correlates with that in
prefrontal and inferior parietal cortices (Allen et al., 2005).

Internal ‘forward’ models use an efference copy of motor commands (Von Holst, 1954) to
make a prediction about the sensory consequences of an action (Blakemore, 2003). This
comparison can be used to cancel sensory effects of performing the action, compared with
identical movements that are externally produced (Blakemore et al., 1999; Weiskrantz et al.,
1971). An impairment in such a predictive system would result in a failure to attenuate the
sensory consequences of self-produced actions, making them appear indistinguishable from
externally generated sensations and engendering the inference that one’s own movements
were externally caused (Blakemore et al., 2002; Frith et al., 2000a). This theory provides an
elegant explanation for why we can’t tickle ourselves, since we cancel the predicted sensory
consequences of the action (Blakemore et al., 2000b). However, patients experiencing
passivity phenomena and hallucinations, in whom sensory cancellation is presumed to be
impaired, rate self generated stimulation as ticklish (Blakemore et al., 2000a). Impaired
cancellation of efference copies has likewise been implicated in the pathophysiology of
hallucinations; here internally generated speech is misperceived as externally generated due
to this impairment in the cancellation of forward model predictions (Ford and Mathalon,
2005; Ford et al., 2007) .

There are some rare patients who call the proposed model of passivity into question;
subjects who have suffered haptic deafferentiation and therefore do not perceive sensory
feedback from the actions they perform (Fourneret et al., 2002). Since a haptically
deafferented subject does not suffer from delusions of passivity; some have argued that
aberrant percepts of one’s own action are not sufficient to explain passivity delusions;
invoking a further belief evaluation dysfunction that is necessary for the delusional inference
to occur (Coltheart, 2010). To clarify the prediction error based explanation of these
phenomena; patients with passivity experiences do not use forward model predictions to
cancel the predicted consequences of their movements so they experience the sensory
consequences of their actions and therefore attribute the source of their actions externally.
Haptically deafferented subjects should therefore be protected from passivity experiences;
since such experiences do not depend on absence of feedback but on inappropriately large or
unexpected feedback. It is this persistence and unexpected nature of aberrant prediction error
that engages delusion formation.

Parietal cortex receives inputs from the cerebellar internal model (Ito, 1993), possibly
combining them with a multi-sensory salience map of the external world and the motor
plans necessary to approach or avoid salient features (Mohanty et al., 2009). Activity in the
parietal operculum is also attenuated during self initiated movements compared with passive
movements (Weiller et al., 1996) and during self produced compared with external
stimulation. Patients with lesion to the right hemisphere in white matter underlying the
parietal operculum delusion that their limb belonged to their niece (Bottini et al., 2002).

Even healthy individuals can be tricked into accepting that a false hand belongs to their own
body (Botvinick and Cohen, 1998). If subjects perceive the false hand being stimulated at

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 16

the same time as they feel their own (occluded) hand receiving the same stimulation, they
begin to feel that the false hand belongs to them, incorporating it into their body schema
such that, when asked to estimate where their own hand is positioned, they point to a
location closer to the false hand (Makin et al., 2008). Patients with schizophrenia are more
susceptible to this illusion (Peled et al., 2003). It appears that the processes of multisensory
integration involved in judging ownership of a body part involve synaptic learning via
associative Hebbian mechanisms, representing the confluence of seeing a hand stimulated
and feeling a hand stimulated (Keysers et al., 2004). Furthermore, top-down attentional
biases seem to influence the illusion (Tsakiris and Haggard, 2005). These biases again
emerge through associative learning and are subject to the same formal rules, a surprising
mismatch between the expected confluence of sensation and vision weakens the illusion.
Likewise the illusion does not occur for a stick: people perceive rubber hand illusions more
readily than rubber object illusions (Press et al., 2008). Physiological noise in the
multisensory integration process that confers bodily ownership may engender mutated prior
expectations about the body which bias subsequent perception, resulting in
somatoparophrenias, delusions of body representation and agency (Vallar and Ronchi,
2009).

2.4.2 Social learning and therefore our beliefs about others—Social
neuroscientists also appreciate the power of prediction error and predictive coding (Behrens
et al., 2009; Kilner et al., 2007a, b; Lee, 2008a). Reinforcement learning circuits are engaged
when human subjects make social value judgments and a further network of brain regions is
engaged when subjects make judgments about the intentions of others – including the
superior temporal sulcus/temporoparietal junction (STS/TPJ) (Behrens et al., 2009). These
data build upon previous suggestions that associative principles like prediction error govern
various social attribution processes (Miller, 1959). For example social attributions made
about worker productivity are susceptible to associative learning phenomena like Kamin
blocking (Cramer et al., 2002).

fMRI studies of prediction error driven reinforcement learning usually require participants to
learn which of two stimuli to choose in order to win the most points (Pessiglione et al.,
2006). In an extension to the standard paradigm, Behrens and colleagues gave subjects an
additional source of information, the suggestion of a confederate who may or may not know
the appropriate choice to make. Hence the subjects learned simultaneously whether to
choose the blue or the green card and also whether they could trust the advice of the
confederate. They were able to distinguish brain regions coding a mismatch between
expected and experienced reward from brain regions coding a mismatch between expected
and experienced truth. Intriguingly, these analyses revealed that adjacent but distinct regions
of the anterior cingulate cortex coded reward and truth prediction error. The STS/TPJ also
appeared to reflect social prediction errors about the truth of the confederate’s advice
(Behrens et al., 2008).

The analysis of social learning in terms of prediction error has recently bridged theories of
both reinforcement learning and predictive coding. Building upon the empirical Bayes
model of brain function, this approach combines the forward model of intentional motor
control (Blakemore, 2003; Blakemore et al., 2001; Wolpert et al., 1995; Wolpert and Miall,
1996) with the observations of social prediction errors in STS (Behrens et al., 2008;
Hampton et al., 2008) to explain the function of the brain’s mirror neurons system through
its direct link between action and observation (Kilner et al., 2007a, b). Here, the most likely
cause of an observed action can be inferred by minimizing the prediction error across all
levels in the cortical hierarchy that are engaged by that observation.

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 17

Observing, imagining, or in any way representing an action excites the motor program used
to execute the same action (Jeannerod, 1994). Mirror Neurons discharge not only during
action execution but also during action observation; they were identified in non-human
primates, using neural recording, in area F5 and the inferior parietal lobule (Fogassi and
Luppino, 2005; Gallese et al., 1996; Rizzolatti et al., 1996). Functional magnetic resonance
imaging data have been used to infer the presence of mirror neurons in the human inferior
parietal lobule (Chong et al., 2008) and inferior frontal gyrus (Kilner et al., 2009). However
some have failed to find evidence of mirror neuron-like activations (Lingnau et al., 2009).
Indeed, the spatial resolution of fMRI is such that it may be inappropriate to ascribe the
response in a particular region to a specific population of cells. Furthermore, some have
questioned the reified status of mirror neurons; that is, instead of being indivisible, they may
simply reflect conditioning of an association between a motor program for an action and a
visual representation of that action; learned by experience across the life course (Heyes,
2010). The present theory does not depend on the exact origin of mirror representations and,
given that the regions in which mirror neurons have been identified with direct recording in
non-human primates largely overlap with those regions that responded to action observation
and execution in human subjects, we proceed by discussing the potential role of mirror
neurons in human social cognition (Gallese et al., 2004).

Implicit in the description of mirror neurons is the idea that information is passed by forward
connections from low level representations of the movement kinematics to high-level
representations of the intentions subtending the action. Observation of an action activates the
STS, which in turn drives the inferior parietal lobule which drives the inferior frontal gyrus.
Formally this is a recognition model that operates by the inversion of a generative model
(Kilner et al., 2007a, b). A generative model will produce an estimate of the visual
consequences of an executed action given the causes or goals of that action. By inverting the
model it is possible to infer the cause or goal of an action given the visual input (Kilner et
al., 2007a, b).

Again, bottom-up or top-down biases in this inference process would lead to gross
misrepresentations of other’s intentions. Those biases may arise due to aberrant prediction
error signals, forging maladaptive social expectations manifest phenomenologically as
intense feelings of social uncertainty and ultimately paranoia. More recently, it has emerged
that beliefs about somebody’s mental experience can influence how we perceive their
physical attributes (Teufel et al., 2009) . While the full connotations of this have yet to be
explored, it seems that we may perceive someone’s behavior depending on what we think
that they are thinking.

3. The fixity of delusions

By inappropriately updating subject’s priors, delusions are applied to all subsequent
experiences(Conrad, 1958b; Mishara, 2009). Why might this be? Indeed, if we are arguing
that delusions form under the influence of inappropriate, uncertain and imprecise prediction
error, why do delusions become so tenacious? Here we turn to a process that has received
increasing empirical attention in recent years; memory reconsolidation (Misanin et al., 1968;
Nader et al., 2000). We conceive of beliefs and delusions as a kind of memory (Eichenbaum,
2000), that is, a means through which past experiences and processing organize responses to
current inputs. Memories serve a more dynamic function than simple storage; they can be
recalled, returned to a labile state (Misanin et al., 1968; Nader et al., 2000), updated with
new information (Estes, 1997) and strengthened (Lee, 2008b); a set of reconsolidation
processes that appear to be engaged when unexpected events occur (Eisenhardt and Menzel,
2007). This updating process involves a streamlining or schematization of the representation
(Stickgold and Walker, 2007). We have previously argued that, once delusions are formed,

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 18

future prediction errors engage a reactivation, reconsolidation and strengthening of the
delusion; rendering it impervious to contradictory evidence; each time a delusion is
deployed, it is reinforced further, conferring resistance to contradiction (Corlett et al.,
2009c), rather like the formation of an instrumental habit with overtraining (Adams, 1981;
Lee, 2008b; Stickgold and Walker, 2007). That is, when subsequent prediction errors occur,
they are explicable in terms of the delusion and they serve to reinforce it, hence the
paradoxical observation that challenging subjects’ delusions can actually strengthen their
conviction (Milton et al., 1978; Simpson and Done, 2002). Neurobiologically, this
reconsolidation based strengthening would shift control of behavior toward the dorsal
striatal habit system (see Figure 3) and would manifest as immutable prior expectancies in
Bayesian cortical hierarchies(Corlett et al., 2009b; Corlett et al., 2009c; Mishara, 2009).
Delusions may be maintained despite being fallacious through disruptions in frontostriatal
synaptic metaplasticity, a form of ‘plasticty of plasticity’ (Abraham and Bear, 1996) that
allows old associations to be overridden by new learning. Metaplasticity can be restored
with n-acetyl-cysteiene , (Moussawi et al., 2009), a drug which increases the availability of
glutamate in extrasynaptic spaces by stimulating the cysteine-glutamate antiporter (Baker et
al., 2008).. This analysis of delusions, in terms of a shift away from computationally
expensive prefrontal processing toward striatal habit (Daw et al., 2005; Mishara, 2009) may
also explain the waxing and waning of delusional conviction and the paradoxical double
book-keeping; patients endorse particular delusions but do not act as if they truly believe
them (Bleuler, 1908; Sass, 2004); such situations would transpire if the goal-directed system
occasionally won the competition for control of behavior, a state of the system that can be
engendered by enhancing plasticity in prefrontal brain regions (Hitchcott et al., 2007;
Moussawi et al., 2009).

Here we draw upon advances in the cognitive neuroscience of addiction to make our case
about delusions. Like delusions, aberrant prediction error accounts have been outlined for
the generation of addictive behaviors (Lapish et al., 2006; Redish, 2004) as well as their
maintenance as habits despite maladaptive consequences (Takahashi et al., 2008). We posit
that the inappropriate prediction error that occurs in endogenous psychosis is internally
generated (rather than a plastic response to drug consumption, although see (Corlett et al.,
2009a) for a review of drug induced psychoses) and that they track merely coincident
environmental stimuli rather than cues that predict access to drug and drug induced hedonic
states. However, maladaptive prediction error responses in addiction and psychosis may be
indicative of a fronto-striatal system that is sensitized toward aberrant learning and may
therefore explain the strong co-morbidity between drug abuse and psychosis (Kalayasiri et
al., 2006; van Nimwegen et al., 2005).

Reactivating a delusion (perhaps having a patient engage with and ruminate upon it) may
drive its representation into a labile state; providing a novel therapeutic window in which to
intervene and destabilize the delusion. This approach has been taken previously with some
success (Rubin, 1976), however, future well-controlled investigations are essential.

4. One or Two Factors?

There are competing accounts of delusions in cognitive neuropsychiatry (Coltheart et al.,
2007; Freeman et al., 2002; Garety, 1991; Garety and Freeman, 1999; Gerrans, 2002;
Kinderman and Bentall, 1997; McKay et al., 2007). Some argue that perceptual aberrations
are all that is required for a delusion to form (Gerrans, 2002; Maher, 1974), others that
delusions result from top-down reasoning impairments (Freeman et al., 2002; Garety, 1991;
Garety and Freeman, 1999), others still posit some combination of both factors, a two-factor
approach in which perceptual and reasoning abnormalities combine (Coltheart et al., 2007;
McKay et al., 2007). The latter derive from observations that neurological patients with

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 19

delusions often have two sites of damage; a lesion in a perceptual region (such as the
fusiform face area) and an additional lesion in ‘belief evaluation’ regions, possibly in the
right frontal cortex (Ramachandran, 1998). The first damage engenders odd percepts and the
second generates bizarre explanations.

Prediction error driven Bayesian models of delusions (Corlett et al., 2009a; Fletcher and
Frith, 2009) subsume both factors into a single deficit in Bayesian inference; noise in
predictive learning mechanisms engender inappropriate percepts which update future priors,
leading to the formation and maintenance of delusions. Prediction error signals have been
registered in right dorsolateral prefrontal cortex during causal learning (Corlett et al., 2004;
Fletcher et al., 2001; Turner et al., 2004), psychotogenic drug administration and
endogenous psychosis are associated with inappropriate responding in this region, the
magnitude of which was predictive of delusion severity (Corlett et al., 2006; Corlett et al.,
2007b).

2-factor theorists have recently equated the inappropriate prediction error signals that we
reported in dorsolateral prefrontal cortex with their aberrant belief evaluation process or
factor 2 (Coltheart, 2010). However, a single deficit in Bayesian inference is able to explain
more of what we know about the interactions between perception and belief-based
expectation, the neurobiology of the delusions that occur in schizophrenia and the
maintenance of delusions in the face of contradictory evidence. That is, unlike 2-factor
theory, our model allows for dysfunctional prediction error to be calculated in PFC and
imposed upon the rest of the brain or, alternatively for surprising perceptual inputs to arrive
at PFC engaging surprise and demanding explanation. Both of these possibilities (bottom-up
and top-down) are aberrations of a single factor; Bayesian inference.

We recognize the strong neurological evidence that perceptual aberration and delusional
ideation are dissociable (Coltheart, 2010). However, we emphasize the potential
consequences of prefrontal cortical damage alone (their Factor 2) as well peripheral
perceptual dysfunction (their Factor 1); there are patients who suffer from delusion-like
spontaneous confabulations following damage to ventromedial and lateral prefrontal cortex
(Schnider, 2003; Turner et al., 2004) and at least one patient in whom peripheral sensations
are perturbed (following damage to the brachial plexus) who has somatic delusions in the
absence of any apparent structural damage and by extension any deficit in factor 2
(Ghoreishi, 2010).

In short, the present model suggests that inappropriate mismatches between expectancy and
experience engender prediction error where there ought to be none, driving new and aberrant
learning directly and through the allocation of attention toward irrelevant but potentially
explanatory cues (Corlett et al., 2007a). This learning normally provides the basis for a
variety of vital perceptual and cognitive functions that govern our interactions with the
environment and other agents so when it malfunctions, gross misrepresentations of reality,
delusions and perceptual aberrations, result.

5. A Neurodevelopmental Dimension?

Developmental studies suggest that children who go on to develop schizophrenia and
therefore likely delusions (although not all patients with schizophrenia have delusions) have
subtle neurological ‘soft-signs’ indicative of aberrant sensorimotor integration (Mohr et al.,
1996). In healthy individuals, there are relationships between motor developmental
milestones, structural integrity of the frontal cortex, striatum and cerebellum and executive
cognitive function, associations which are not present in patients with schizophrenia (Ridler
et al., 2006) suggesting impaired bootstrapping of cortical pathways into systems that can
predict and respond to their inputs and thus, an impairment of adaptive interaction with the

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
Corlett et al.

Page 20

environment and other agents; individuals with impaired sensorimotor integration
throughout development would learn impoverished or maladaptive prior expectancies about
the world (Hemsley and Garety, 1986b).

Different homeobox genes are responsible for controlling the development and patterning of
the frontal cortex (Tabares-Seisdedos and Rubenstein, 2009), midbrain dopamine neurons
(Maxwell and Li, 2005), the striatum (Long et al., 2009), the amygdala (Tole et al., 2005)
and cerebellum (Sillitoe et al., 2008). Some of these genes and their expression products
have been associated with psychotic symptoms, for example; DLX1 expression is decreased
in the thalamus of individuals with psychosis compared with those without a history of
psychosis and matched healthy controls (Kromkamp et al., 2003). Likewise, the homeogene
Engrailed 2 which controls cerebellar development is associated with schizophrenia
(Gourion et al., 2004). Knocking out FGF17, a gene that controls the patterning and
organization of frontal cortical development, leads to profound deficits in social interaction
in mice, perhaps indicative of a relationship to paranoia (Scearce-Levie et al., 2008). Indeed,
a human genetic association study revealed a link between the chromosome region where
FGF17 is found (8p13) and delusional beliefs (Chiu et al., 2002). We acknowledge that we
are speculating here and we appreciate the dangers of anthropomorphizing social behaviors
in rodents; future work should address the validity of FGF-knockout as a model of paranoia
by exploring other prediction error related processes in these animals; do they have a deficit
in conditioned avoidance learning, for example? We believe that the different themes of
delusional beliefs entertained by different subjects may have their origins in subtle
developmental dysfunctions in the circuits we have outlined, biasing prediction error driven
deficits in glutamatergic and dopaminergic processing toward a particular set of experiences
and a specific explanatory belief. Normal variation in these same genetic loci may underpin
individual differences in perceptual aberration as well as the themes and severity of
delusion-like ideation in the healthy population.

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

6. Explaining Delusion Content

We now attempt to account for different kinds of delusion within this framework. While the
scope of this section is by no means exhaustive, we believe that the range of delusions
potentially accounted for within the framework is compelling (see Figure 4).

6.1 Paranoia and delusions of reference

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Referential delusions involve the belief that objects, events and agents in the environment
are communicating specific and personal messages (Conrad, 1958b) ranging from the
inanimate to animate, from newspapers, to television newsreaders (Startup and Startup,
2005) and even the fictional television detective Columbo (Chadwick, 2007). The
psychotomimetic drug ketamine transiently induces delusions of reference in healthy
volunteers (Krystal et al., 1994; Oye et al., 1992; Pomarol-Clotet et al., 2006). It blocks
NMDA receptors (thus impairing the specification of top-down prior expectancies) while at
the same time enhancing bottom-up AMPA signaling (Jackson et al., 2004) and engages
acetylcholine release (Sarter et al., 2005). Low, sub psychotic doses of the drug engage the
right frontostriatal prediction error signaling system in response to unsurprising and highly
predictable events and the extent to which it does this showed a strong trend toward
predicting the severity of heightened perception and delusional ideation (Corlett et al.,
2006). We argue that delusions of reference form due to the attentional effects of aberrant
prediction error (Pearce and Hall, 1980) mediated via surprise induced acetylcholine release
from the nucleus basalis of meynert (Bao et al., 2001; Holland and Gallagher, 1993a, 1999a,
2006; Lee et al., 2005); subjects find their attention drawn toward irrelevant stimuli and
events in the environment and impute personal meaning upon them, an experience that
demands explanation, culminating in delusions of reference.

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 21

Paranoid ideation is associated with excessive fear or anxiety (Moutoussis et al., 2007). In
the context of the present analysis, paranoia would result when aberrant prediction error in
frontostriatal learning systems engages the amygdala, engendering a feeling of fear and a
state of hypervigilance. Relevant to this contention, delusions of reference and paranoid/
persecutory ideation tend to co-occur in patients with delusions (Startup and Startup, 2005),
that is, hypervigilance and the perception of meaning in irrelevant and innocuous events
may engender paranoia, since uncertainty and unpredictability are inherently fear inducing
(Vinogradov et al., 1992; Whitson and Galinsky, 2008). However, paranoid thoughts are
commonly about other people (Melo et al., 2006) and , as such, they may involve a
prediction error driven dysfunction in the social learning mechanisms that we use to infer
the intentions of others localized to frontostriatal and parietal circuits and the superior
temporal sulcus/temporoparietal junction (Behrens et al., 2009; Behrens et al., 2008).

Physiological noise in this system, as a result of NMDA receptor hypofunction (which
would disturb the specification of priors), AMPA receptor hyperfunction (which would
signal prediction error where there should be none) and elevated dopamine levels within the
mirror neuron circuit would impair the sufferer’s ability to use what they have learned about
their own actions and intentions to make inferences about other agents (Kilner et al., 2007a,
b). Those disturbances in predicting and learning the consequences of our own actions may
also have their origins in a disruption in the extended fronto-striatal-parietal reinforcement
learning circuit; as we outlined, the midbrain dopamine neurons implicated in the
pathophysiology of schizophrenia (Murray et al., 2008) may report an error in prediction,
which is then processed in a circuit incorporating the frontal cortex, striatum and
hippocampus (Redgrave and Gurney, 2006) as well as parietal cortex (Mittleman et al.,
1990). This signal may be used to discern whether the organisms’ actions caused a particular
outcome, or whether the outcome happened due to external events (Redgrave and Gurney,
2006), while hypofunctioning of this circuit would lead to a decreased sense of agency for
one’s own actions, perhaps most relevant to delusions of external control (see below), we
posit that the hyper engagement of this circuit could engender paranoia. That is, paranoid
persecutory ideation is associated with superstitious biases in action-outcome learning
(Kaney and Bentall, 1992). When playing rigged computer games paranoid individuals
claimed to control both negative and positive outcomes when in fact there was no
programmed contingency between their actions and the salient events.

Haggard and colleagues have reported an excessive binding between intentional actions and
the outcomes they produce in patients with schizophrenia, however they did not relate this
effect to delusions or paranoia in particular (Haggard et al., 2003). This maladaptive
perception of contiguity between actions and outcomes would seem to offer an explanation
for bizarre beliefs about telekinesis or enhanced predictive abilities, however in the context
of the mirror neuron system account for computing and inferring the intentions of others
(Kilner et al., 2007a, b), an individual who had learned spurious associations between their
actions and salient environmental outcomes would also be expected to use those associations
to infer the intentions of other agents. They would then ascribe supernatural abilities or
excessively powerful status to individuals whom they encountered., In the context of
prediction error induced amygdala responses, this inference would be affectively charged
and result in a fear and distrust that is incommensurate with the current situation. This model
makes some progress toward integrating neurobiology with psychodynamic explanations of
paranoia (Kinderman and Bentall, 1996, 1997) in which attentional biases toward perceived
threats are driven by mismatches between current self perceptions and how the patient
believes they ought to be, focusing or projecting a threatening attributional bias onto
external agents (Colby, 1977), patients with paranoia may attempt to avoid feelings of low
self-esteem by attributing the cause of adverse experiences externally (Bentall et al., 2001).
We believe that impairments in the brain’s mirror neuron system and its ability to infer the

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 22

intentions of others based on inverting its own predictions (Kilner et al., 2007a, b) may
underpin these processes of inappropriate external projection of threat.

6.2 Delusions of Motor Passivity

“My fingers pick up the pen, but I don’t control them. What they do is nothing to do with
me” (Mellor, 1970). It appears that these odd beliefs result from an impairment in the
cancellation of predicted sensory consequences of motor behaviors (Blakemore, 2003;
Blakemore et al., 2003; Frith, 2005), involving a defect in the specification of motor
predictions by the cerebellum which subsequently inappropriately engages parietal and
frontal cortices (Frith, 2005; Schnell et al., 2008; Spence et al., 1997). An action produced
without apparent forward model expectation is therefore ascribed to an external agent. A
similar aberrant efference copy account has been made with respect to auditory
hallucinations (Ford and Mathalon, 2005; Ford et al., 2007; Heinks-Maldonado et al., 2007).

However, some have criticized this model for failing to explain how patients with these
delusions (and underlying brain pathology) can engage in any behavior at all. Having a
sense of one’s self as the source of our intentional actions may be essential for goal-directed
instrumental learning (Glymour, 2004). This sense may be learned by the contiguous
association between perceiving an intention to act, executing the motor program and
encountering the consequences (Hume, 1739/2007; Wegner, 2004). Prediction errors due to
physiological noise from dysregulated midbrain dopamine neurons projecting to prefrontal
cortex could render those predictive associations unreliable (Corlett et al., 2007a). However,
there is a less computationally intensive brain system that can control instrumental learning
in the dorsolateral striatum. This system is said to mediate stimulus response habits (Daw et
al., 2005; McDonald and Hong, 2004; Reading et al., 1991; Tang et al., 2007; Tricomi et al.,
2009; Yin et al., 2004). The information used to guide behavior in this system is insensitive
to the current value of the outcome (Daw et al., 2005). Habitual organisms behave
reflexively, emitting motor responses to environmental cues irrespective of their
consequences (Adams, 1981). The dorsal striatal habit system is believed to govern
compulsive drug seeking and taking (Belin et al., 2009). The goal-directed and habit systems
are conceived of as competitors for the control of behavior – the system that is least
uncertain about the appropriate behavior given the context may win that competition (Daw
et al., 2005). Competition between them can be biased towards the habit system by extended
behavioral training (Adams, 1981); boosting synaptic dopamine levels in the striatum
(Nelson and Killcross, 2006), or modulating AMPA receptor function (Bespalov et al.,
2007). Goal directedness can be rescued by restoring dopamine induced plasticity in the
prefrontal cortex (Hitchcott et al., 2007). It is possible that the habit system wins the
competition in individuals with delusions (see below). Passivity experiences may therefore
be explained as instrumental actions controlled by the habit system in the context of a noisy
and inaccurate goal-directed system.

6.3 Delusions of Parasitosis

Individuals with delusional parasitosis are convinced that small animals such as insects or
lice are living on or within their skin (Berrios, 1982, 1985). This particular symptom
highlights the overlap between delusions and hallucinations, perceptions and beliefs which
calls in to question the strict clinical distinction (Corlett et al., 2009a; Fletcher and Frith,
2009; Frith, 2000). Striatal lesions (Huber et al., 2008), dopamine agonist medications
(Charuvastra and Yaeger, 2006; Mitchell and Vierkant, 1991), cocaine (Mitchell and
Vierkant, 1991; Siegel, 1978; Wallis, 1949) and amphetamine (Ellinwood, 1968; Ellinwood
et al., 1974) abuse can all engender delusions of parasitosis. Indeed, chronic treatment with
dopamine antagonists can induce behaviors indicative of parasitosis in experimental animals
(Ellison, 1994). In human stroke patients, delusions of parasitosis often occur following

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 23

lesions of right temporoparietal cortex, thalamus and putamen (Huber et al., 2008). Putamen
strongly influences visuotactile perception (Graziano and Gross, 1993; Ladavas et al., 1998;
Romo et al., 1995; Yoo et al., 2003), it contains bimodal cells with visual and tactile
receptive fields, which help to encode the location of sensory stimuli mainly near the face.
These cells project to parietal (ventral intraparietal cortex), primary somatosensory and pre-
motor cortices (Graziano and Gross, 1993; Ladavas et al., 1998).

We contend that sensations on the skin are a result of the same interaction between top-
down and bottom-up mechanisms that we argue are crucial for visual perception. This is
supported by the cutaneous rabbit illusion (Geldard and Sherrick, 1972) where simultaneous
stimulation of two points on the skin gives rise to the percept of a rabbit ‘hopping’ between
the two points; stimulation at a particular frequency is best explained by movement along a
trajectory between the two points. There are Bayesian accounts of the illusion (Goldreich,
2007). Parasitosis may arise either due to bottom-up sensation that is normally ignored – for
example a lack of adaptation of skin sensation over time or, alternatively, due to
inappropriate top-down expectations – the power of cognition in cutaneous sensation is also
underlined by contagious itch sensations experienced when subjects are exposed to
conversations about insects on the skin (Heaven and McBrayer, 2000; Mitchell, 1995).

The same learning mechanisms that underpin the rubber hand illusion (Press et al., 2008)
might also be involved in parasitosis; a deficit in Bayesian multisensory integration would
lead aberrant prediction error, driving attention toward potentially explanatory cues and
forging inappropriate visuotactile associations. These associations, between sensation and a
particular spatial location, might be represented by bimodal cells in the striatum, forming a
new prior, a top-down bias in attention to the skin which would contribute to the
maintenance of the delusion (Berrios, 1982; Corlett, 2009).

6.4 Delusions of Misidentification

There are two main classes of misidentification delusion; Capgras; in which patients believe
that their close family members have been replaced by imposters (Capgras, 1923), and
Fregoli; in which patients believe that strangers that they encounter are their relatives in
disguise (Courbon, 1927). Additionally, some patients have misidentification of their own
home either feeling it is unfamiliar (Feinberg and Keenan, 2005; Fleminger, 1992) or that
the hospital in which they find themselves is really their house hundreds of miles away
(Schnider, 2001). Two factor models of these disorders assume a dual deficit, one in
perception of affect, the other in belief evaluation (Coltheart et al., 2007). Instead, we argue
that phenomenology of the percepts are such that bizarre beliefs are inevitable; surprising
experiences demand surprising explanations (Kihlstrom, 1988) . In our Bayesian, predictive
learning scheme, Capgras results when patients experience an anomalous lack of affective
responding when confronted with their relatives (Ellis and Young, 1990), the delusion
constitutes a new prior driven by the experience, a means for explaining it away (Young,
2008). It is possible that the initial affective disturbance results from a failure to guide affect
perception by prior experience, that is, just like sensory perception, emotions are predicted
(Gilbert and Wilson, 2009); we have emotional priors, indeed, it is the prior expectancy of a
familiar face combined with an emotional response (learned through experience) which
breaks down in Capgras patients (Fleminger, 1992); fostering the misidentification of
someone (or something) familiar as unfamiliar (Young, 2008). With the Fregoli delusion, it
is a misplaced sense of familiarity (rather like a delusion of reference, specific to people)
which guides patients to infer that people they do not know are actually their relatives in
disguise.

In a meta-analysis of patients with delusional misidentification (Fregoli and Capgras
delusions) about persons or objects, surveying 48 cases following neurological insult,

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 24

Feinberg et al found that the overwhelming majority had damage to the right hemisphere,
commonly the frontal cortex. This observation is in line with our own work on prediction
error during causal learning implicating a region of right dorsolateral prefrontal cortex in
prediction error signaling (Corlett et al., 2004; Fletcher et al., 2001; Turner et al., 2004) and
implicating it in delusion formation (Corlett et al., 2006; Corlett et al., 2007b).

The laterality of damage that induces delusions seems replicable across studies of
neurological patients with delusions (Devinsky, 2009). Spitzer and Walter (2003) speculate
that this hemispheric bias can be explained by appealing to the different hemispheric modes
of information processing (Kosslyn et al., 1992). Whereas the left hemisphere is
characterized by smaller receptive fields resulting in focused, conjunctive coding, the right
hemisphere is characterized by larger, overlapping receptive fields resulting in a coarse
coding (Spitzer, 2003). In terms of Bayesian brain theory, receptive fields are related to the
top-down specification of expected inputs (Rao and Ballard, 1999). Increasing dopamine
levels may alter the signal to noise ratio of neurons, that is, it will increase the precision or
certainty with which a prediction error is signaled (Friston et al., 2009) such that subjects
respond to physiological noise as if it were meaningful signal (Grace, 1991). An increase in
dopamine levels would serve to inappropriately increase confidence in noisy signals. It will
therefore affect a system which relies on coarse coding, i.e. the right hemisphere, more
prominently than a system which relies on conjunctive coding, i.e. the left hemisphere. That
is, the right hemisphere is more susceptible to inappropriate optimization of prediction error
because its predictions and prediction errors are inherently more noisy than the processing
on the left hemisphere. Some speculate that, in response to right hemisphere error signals,
the left hemisphere begins to construct explanations resulting in delusions (Devinsky, 2009),
however the difficulty identifying and tracking delusions forming (Corlett et al., 2007a)
means that this contention has not found empirical support.

When considering delusions of misidentification of neurological origin, it seems puzzling
that damage in the same region could be associated with both an increase and a decrease in
perceived familiarity. Two factor theorists would suggest that this is parsimoniously
explained by ascribing the right frontal cortex the function of belief evaluation(Coltheart,
2010; Coltheart et al., 2007). However, we found that right frontal prediction error signal
during causal learning was also related to ketamine induced perceptual aberrations (Corlett
et al., 2006) and, furthermore, a study of individuals with lesions in the right dorsolateral
prefrontal cortex suggested that lesion patients attended to and learned about irrelevant
stimulus dimensions during a reward learning task (Hornak et al., 2004). It is possible that
damage or dysfunction in prefrontal cortex could, paradoxically elevate activation in the
remaining neurons since, in healthy individuals they provide a brake on subcortical
dopamine nuclei through glutamatergic (Grace, 1991; Laruelle et al., 2003) and GABAergic
mechanisms (Carlsson et al., 2001). Consequently, either due to a release from inhibition or
an alteration of signal to noise properties, dopamine neurons projecting back from VTA to
prefrontal cortex would increase in burst firing (Jackson et al., 2004) inducing rapid and
random post-synaptic potentials in remaining functional cortical neurons (Lavin et al.,
2005).

6.5 Cotard Delusion

Perhaps one of the most bizarre delusions is the sufferer believing that they have died
(Cotard, 1880), associated with claims that parts of them have “rotted away” or
“disappeared” (Gerrans, 2002). It is possible that the same impoverished habitual
mechanisms of instrumental action are engaged (see above) and the subject infers that the
intentional agent that they were has disappeared, that is, the Cotard delusion may be a
special case of passivity. Additionally, Some hypothesize that Capgras patients fail to
recognize family members due a disconnection between face recognition units in the

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 25

fusiform face area and the ascription of emotional meaning in the limbic system, therefore,
patients with Cotard delusion may have no connection at all between sensation and affective
processing (Gerrans, 2002; Ramachandran, 1998). In this analysis, Cotard delusion is the
converse of paranoia, instead of heightened and inappropriate emotional intensity it is a
failure to ascribe emotional significance to any event (Gerrans, 2002; Ramachandran, 1998).
Such a lack of emotional engagement with experiences would be surprising, engendering
prediction error and sculpting the erroneous conclusion that the patient had died. Again,
affective prediction fails, but instead of the rather specific effect in Capgras, it is a
generalized failure in predicting the affective qualities of all sensory inputs. Like Capgras
and Fregoli, this may involve a dysfunction in orbitofrontal cortex specifying top-down
emotional predictions (Rolls and Grabenhorst, 2008). The delusion has been reported in a
case study following right temporoparietal and bilateral frontal damage (Young et al., 1992),
it also occurs in schizophrenia (Coltheart et al., 2007). This delusion involves both a deficit
in affective forecasting (by the orbitofrontal cortex and amygdala), as well as (potentially) a
deficit in motor forecasting (and thus sensory cancellation), with a diminished sense of self
and emotional disengagement, the patient concludes that he/she is dead.

7. Why that odd belief? Individual differences in delusion susceptibility

While some psychotic patients get paranoid, others experience passivity, others still have
multiple bizarre delusions. We posit a single factor, prediction error dysfunction for delusion
formation and maintenance (Corlett et al., 2009a; Corlett et al., 2007a; Corlett, 2009;
Fletcher and Frith, 2009). We have recently applied this single factor account to explain the
range of phenomenological effects of pharmacologically distinct psychotomimetic drugs
from dopamine agonist amphetamines, to NMDA antagonists, cannabinoids and
serotonergic hallucinogens (Corlett et al., 2009a). We believe the same explanation may be
possible for the individual differences in susceptibility to different delusional themes
observed in patients with schizophrenia.

Schizophrenia is a heritable but heterogeneous mental illness; its genetic inheritance appears
to involve multiple genes of small effect (Tabares-Seisdedos and Rubenstein, 2009) or
alternatively multiple rare genetic variants each with a large impact (Walsh et al., 2008).
However, common to many of the identified risk genes for schizophrenia is a role in
associative learning, prediction error signaling and NMDA receptor dependent synaptic
plasticity (Hall et al., 2009; Stephan et al., 2006; Walsh et al., 2008). Some of the genes
implicated in prediction error driven learning (Frank et al., 2007; Heyser et al., 2000)
increase the risk for schizophrenia; the COMT val/met polymorphism may enhance
maladaptive feedback between frontal cortex and subcortical dopamine neurons and is
associated with risk for schizophrenia, aberrant salience and delusions (Bilder et al., 2004).
In addition, PP1R1b, the gene coding for neostriatal signaling nexus DARPP-32 which
integrates midbrain dopamine inputs with cortical glutamatergic signaling has been
associated with prediction error driven learning (Frank et al., 2007; Heyser et al., 2000)
frontostriatal structure and function as well as risk for schizophrenia (Meyer-Lindenberg et
al., 2007). Variation in the function of these genes may explain inter-subject variability in
susceptibility to delusions following psychotomimetic drug administration (Corlett et al.,
2009a; Corlett et al., 2007a; Svenningsson et al., 2003).

However, different delusional themes are characteristic following the administration of
different psychotomimetics; paranoia is more intense following cannabis administration
(D’Souza et al., 2009) whereas ketamine engenders delusions of reference (Krystal et al.,
1994; Oye et al., 1992; Pomarol-Clotet et al., 2006), although the two themes are by no
means mutually exclusive (Startup and Startup, 2005). We believe that a second genetic
insult may confer susceptibility to particular kinds of delusion in schizophrenia, an insult

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 26

involving disrupted cortical patterning and how the developing cortex interacts with
environmental inputs in forming and maintaining cortical hierarchies (Sur and Rubenstein,
2005). Although this appears to be a two-factor theory, when we consider how Bayesian
hierarchies like the brain develop into prediction engines (Friston, 2005b) through
interactions between neural circuitry and incoming stimulation (Sur and Rubenstein, 2005),
delusions really involve a singular dysfunction in predictive learning (i.e. an interaction
between the two deficits which leads to (dys)interactions between poorly specified top-down
predictions and noisy feedforward inputs; inducing aberrant and imprecise prediction errors
(Corlett et al., 2009a; Fletcher and Frith, 2009). The genes for building cortical hierarchies
may also engender prediction error dysfunction irrespective of dopaminergic/glutamatergic
‘prediction error’ risk gene status and furthermore, the two insults may interact to produce
more severe or varied delusions in the same patient.

Are there any empirical data to support of our contention that delusions with different
themes are mediated by distinct (but overlapping) neural circuits? Patients with delusions
secondary to neurological damage often have lesions in right frontal cortex but, according to
two factor theories, the theme of the belief is conferred by damage to a second structure; for
example the fusiform face area in Capgras delusion. Patients suffering from dementia with
Lewy bodies experience delusions (Nagahama et al., 2009; Nagahama et al., 2007) like
Capgras (Hirono and Cummings, 1999). Nagahama and colleagues used factor analysis to
classify psychotic symptoms in dementia with Lewy bodies. They found that hallucinations,
misidentification experiences and delusions were independent symptom domains
(Nagahama et al., 2007). More recently they replicated this factor structure in an
independent group of patients and assessed the neural correlates of those factors by
regressing factor scores onto resting state neuroimaging data across subjects (Nagahama et
al., 2009).

Patients suffering from misidentification had hypo-perfusion in left hippocampus, insula,
inferior frontal gyrus and nucleus accumbens compared to patients without those symptoms.
Individuals who had visual hallucinations of person or a feeling of presence had hypo-
perfusion in bilateral parietal and left ventral occipital gyrus. Patients with persecutory
delusions showed significant hyperactivity in right cingulate sulcus, bilateral middle frontal
gyri, right inferior frontal gyrus, left medial superior frontal gyrus and left middle
frontopolar gyrus. These distinct circuits tend to support our predicted delusion circuits (see
Figure 4); that is, paranoia involves a frontal hyperactivity; delusions that potentially involve
hyper salience of own body representations (e.g. hallucinations of people and feeling of
presence) involve a parietal dysfunction and reduplications of person and place involve a
predictive memory impairment; impaired familiarity processing and fronto-hippocampal as
well as frontostriatal dysfunction.

Lewy bodies appear to accumulate in the space between bands of cortex; occupied by
afferent or efferent connections with different cortical sites or with subcortical regions, that
is, they have a laminar distribution (Armstrong et al., 2001). Depending on which layer, they
preferentially influence the feedforward (prediction error specifying) connections
originating in laminae I-III and terminating in granular lamina IV of the adjacent lobe
(Armstrong et al., 2001). Alternatively, Lewy bodies may accumulate in the feedback fibers
(responsible for specifying prior expectations and attentional modulation) which originate in
laminae V and VI (and to some extent III) and terminate in lamina I (De Lacoste and White,
1993). Why the feedforward and feedback pathways of one particular circuit would be more
sensitive to Lewy body inclusions than another circuit (conferring a particular delusion
content) has yet to be determined, however, the disconnection that they engender within
particular circuits is consistent with the putative disconnections invoked to explain the
symptoms of schizophrenia (Friston, 2005a; Friston and Frith, 1995).

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 27

Finally, we turn to a rare but intriguing phenomenon, Folie a Deux (Lasegue, 1877), to
evaluate our proposal that delusional themes are mediated by inherited biological processes.
Folie a Deux (FD) is a psychotic disorder shared between two sufferers; an ‘inducer’ who
initially develops the belief and the ‘induced’, an apparently otherwise healthy individual
who comes to share the delusional belief. All kinds of rare delusional contents can be
transmitted e.g. Cotard, Capgras, Fregoli (Wolff and McKenzie, 1994).

FD commonly occurs in persons who live close together, the delusion perhaps being
transmitted through social learning processes. Additionally, if both patients are related, they
may share the same genetically driven illness or predisposition. Monozygotic twins can
share the same delusional themes (Lazarus, 1986); however, since they often share both
genetic and environmental exposure, it is difficult to discern the unique contributions made
by genes and environment. Scharfetter attempted to dissect these contributions by
identifying dyads in whom there was no cosanginuity (e.g. husband and wife) then
evaluating the risk for schizophrenia in each respective family. Incidence in both inducer
and induced was very high (6.5% to 26.2%, compared with 1% population incidence),
suggesting that a general predisposition toward delusions was necessary for accepting
someone else’s aberrant belief (Scharfetter, 1970). Future empirical research should
investigate the personality, cognitive and neural functions of related and unrelated FD dyads
to ascertain the roles of specific neural circuits in instantiating particular delusional beliefs.

8. Testing the hypothesis

Our sketch of the emerging neurobiology of delusional beliefs makes a number of testable
predictions which will assess the validity of the venture:

1. We have argued that delusions arise and are maintained due to aberrations of

glutamatergic synaptic plasticity, specifically chronically elevated synaptic
glutamate which renders inappropriate salience and learning that engenders a limit
on metaplasticity. Given its effectiveness against cocaine induced deficits in
metaplasticity (Moussawi et al., 2009), we predict that N-acetylcysteine should be
an effective treatment for delusions.

2. Patients with delusional parasitosis and delusions of passivity should be more

susceptible to the rubber hand illusion because of the dysinteraction between the
bimodal cells in their striatum and parietal and cerebellar circuits responsible for
coding top-down, motor expectancies and cancelling the sensory consequences of
actions.

3. Paranoia should be associated with prediction error dysfunction in

mesocorticolimbic regions as well as the mirror neuron circuit, especially the
superior temproral sulcus region involved in learning to infer the intentions of other
agents (Behrens et al., 2008).

4. Given a large enough sample and phenomenologically rigorous assessment it
should be possible to test our aetiological hypothesis about homeobox genes,
development and the specification of priors; we predict that subtle variation in the
gene coding for pax6 will alter amygdala development and therefore confer a risk
for paranoia (Tole et al., 2005); Engrailed 2 will be associated with an increased
likelihood of cerebellar dysfunction (Sillitoe et al., 2008) and as such will confer
risk for passivity delusions.

5. Reconsolidation processes should be enhanced in individuals with intractable

delusions – engaging and challenging their belief should increase its severity but
treatments that block reconsolidation (such as the alpha adrenergic receptor

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 28

antagonist, propanalol) should ameliorate delusions (if they have been actively
engaged).

6. Physical interventions that target reactivated representations of delusions should
also have therapeutic benefits (Rubin, 1976), for example, it may be possible to
disrupt the reconsolidation of delusions with transcranial magnetic stimulation
(TMS) (Corlett, 2009). Based on the observed relationship between DLPFC
dysfunction and delusional ideation (Corlett et al., 2006; Corlett et al., 2007b) as
well as the role of DLPFC in controlled memory retrieval and updating (Fletcher
and Henson, 2001) we suggest that specifically targeting that region with TMS
following memory engagement may prove beneficial.

7.

8.

Individuals with high positive schizotypy or treated with psychotomimetic drugs
should demonstrate aberrant prediction error signaling and therefore form learned
habits more rapidly than controls.

If delusions are learned habits, then pharmacological interventions that restore goal
directedness should be effective therapeutically; for example, antagonizing AMPA
receptors (Bespalov et al., 2007), boosting PFC dopamine levels (Hitchcott et al.,
2007) and attenuating striatal dopamine (Nelson and Killcross, 2006) should favor
plasticity and goal directedness. The dopamine partial agonist Aripiprazole
combines both antagonism of elevated striatal dopamine and an elevation of
attenuated prefrontal dopamine and may specifically target aberrant prediction error
signaling in midbrain dopamine neurons (Hamamura and Harada, 2007). It may be
particularly effective against cognitive habits like delusions.

In order to complete a revolution of translation, having been inspired by the role of
prediction error in associative learning in infrahuman species to develop our account of
delusions, we should use invasive preclinical neuroscientific approaches in combination
with associative learning phenomena to model delusion formation and maintenance in
experimental animals. There are a number of potential opportunities here; combining acute
psychotomimetic pharmacological models) to recapitulate putative neurobiological
mechanisms of psychosis) with associative learning tasks that are sensitive to prediction
error (to model delusion formation) or habit learning and memory reconsolidation (to model
delusion maintenance).

9. Conclusion

We have outlined an account of delusional beliefs based on the tenets of animal learning
theory and hierarchical Bayesian inference. We apply those tenets not only to explain
dysfunctions in Pavlovian predictive learning (Corlett et al., 2006; Corlett et al., 2007b) and
instrumental conditioning (Freeman et al., 2009; Murray et al., 2008; Roiser et al., 2009;
Schlagenhauf et al., 2009), but also to account for the perceptual, affective and social
disruptions that attend delusions (Bentall et al., 2001; Maher, 1974; Vinogradov et al.,
1992).

In deluded individuals, the ability to use learned information to constrain current experience
is impaired resulting aberrations of sensory and affective perception as well as cognition
(Gray, 1991; Hemsley, 1994). Delusions may arise as an explanation for these odd
happenings and they engage new learning (Kapur, 2003; Maher, 1974; McGhie and
Chapman, 1961). They bring such relief that they are stamped into memory and become a
new explanatory scheme for the sufferer (Jaspers, 1963), that is, delusions are elastic; they
encompass new experiences and maintain a certain consistency of the world for the patient.
In terms of the Bayesian model we outlined, delusions become the sufferer’s new priors and
they are used to predict and explain future experiences. We believe that the same prediction

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 29

error driven learning mechanisms can account for the fixity of delusional beliefs, since, now,
when subsequent physiological noise elicits a reactivation of the delusion, it is reinforced
and reconsolidated more strongly (Corlett et al., 2009c). These hypotheses are readily
testable in individuals suffering endogenous delusions, in healthy subjects exposed to
psychotomimetic model psychoses and in preclinical models by focusing on the framework
for translational cognitive neuroscience provided by formal associative learning theory,
hierarchical Bayesian learning, predictive coding and information theory – the concept that
intersects all of these is surprise or prediction error (Friston, 2010) and our model implicates
aberrant prediction in the pathophysiology of delusions.

We have applied this model to various different kinds of delusions, examining beliefs that
result from neurological damage as well as those that result from ingestion of
psychotomimetic compounds and those that occur in schizophrenia, we feel, with some
success. However, Brendan Maher, Emeritus Professor of the Psychology of Personality at
Harvard, astutely aligned delusions with scientific theories (Maher, 1988), suggesting that
scientists, like individuals with delusions, were extremely resistant to giving up their
preferred theories even in the face damningly negative evidence. Like scientists, deluded
individuals are confronted by surprising data which they explain away by abductive
inference, generating hypotheses that explain away the surprise (Coltheart et al., 2010).
Scientists (some of them at least) will engage in deductive inference to test the validity of
their conclusions; whilst patients with delusions may not engage in this process (Miller,
1976), showing a bias against disconfirmatory evidence (Woodward et al., 2006).
Furthermore, inductive inference, that is, reasoning from the specific to the general, has been
invoked to explain the influence of prior experience over current perception (Barlow, 1990).
We propose that the inductive process, reasoning beyond the data, may provide a
mechanism through which delusions are maintained and pervade future experiences
(Jaspers, 1963). Whilst the theory outlined in the present piece is our preferred explanation
of delusions, we hope that we engender discussion, debate and investigation. As Maher says
of science and psychosis: “Puzzles demand an explanation; the search for an explanation
begins and continues until one has been devised”. We hope that this article might encourage
others to join the search.

References

Aarts H, Custers R, Wegner DM. On the inference of personal authorship: enhancing experienced

agency by priming effect information. Conscious Cogn. 2005; 14:439–458. [PubMed: 16091264]
Abraham WC, Bear MF. Metaplasticity: the plasticity of synaptic plasticity. Trends Neurosci. 1996;

19:126–130. [PubMed: 8658594]

Adams, CD.; Dickinson, A. Actions and Habits: variations in associative representations during

instrumental learning. In: Spear, NE.; Miller, RR., editors. Information Processing in Animals:
memory Mechanisms. Erlbaum; New Jersey: 1981.

Allen G, McColl R, Barnard H, Ringe WK, Fleckenstein J, Cullum CM. Magnetic resonance imaging
of cerebellar-prefrontal and cerebellar-parietal functional connectivity. Neuroimage. 2005; 28:39–
48. [PubMed: 16023375]

Alloy LB, Tabachnik N. Assessment of covariation by humans and animals: the joint influence of prior

expectations and current situational information. Psychol Rev. 1984; 91:112–149. [PubMed:
6571422]

Angelucci A, Levitt JB, Lund JS. Anatomical origins of the classical receptive field and modulatory

surround field of single neurons in macaque visual cortical area V1. Prog Brain Res. 2002a;
136:373–388. [PubMed: 12143395]

Angelucci A, Levitt JB, Walton EJ, Hupe JM, Bullier J, Lund JS. Circuits for local and global signal
integration in primary visual cortex. J Neurosci. 2002b; 22:8633–8646. [PubMed: 12351737]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 30

Angrilli A, Spironelli C, Elbert T, Crow TJ, Marano G, Stegagno L. Schizophrenia as failure of left
hemispheric dominance for the phonological component of language. PLoS One. 2009; 4:e4507.
[PubMed: 19223971]

Ardid S, Wang XJ, Gomez-Cabrero D, Compte A. Reconciling coherent oscillation with modulation of
irregular spiking activity in selective attention: gamma-range synchronization between sensory and
executive cortical areas. J Neurosci. 2010; 30:2856–2870. [PubMed: 20181583]

Armstrong RA, Cairns NJ, Lantos PL. What does the study of the spatial patterns of pathological
lesions tell us about the pathogenesis of neurodegenerative disorders? Neuropathology. 2001;
21:1–12. [PubMed: 11304036]

Atkinson JW, McClelland DC. The projective expression of needs. II. The effect of different

intensities of the hunger drive on Thematic Apperception. Journal of Experimental Psychology.
1948; 38:643–658. [PubMed: 18893180]

Baker DA, Madayag A, Kristiansen LV, Meador-Woodruff JH, Haroutunian V, Raju I. Contribution of

cystine-glutamate antiporters to the psychotomimetic effects of phencyclidine.
Neuropsychopharmacology. 2008; 33:1760–1772. [PubMed: 17728701]

Balleine BW, Killcross S. Parallel incentive processing: an integrated view of amygdala function.

Trends Neurosci. 2006; 29:272–279. [PubMed: 16545468]

Bao S, Chan VT, Merzenich MM. Cortical remodelling induced by activity of ventral tegmental

dopamine neurons. Nature. 2001; 412:79–83. [PubMed: 11452310]

Barlow H. Conditions for versatile learning, Helmholtz’s unconscious inference, and the task of

perception. Vision Res. 1990; 30:1561–1571. [PubMed: 2288075]

Bayes T. An essay towards solving a problem in the doctrine of chances. Philos Trans R Soc Lond.

1763; 53:370–418.

Beck J, Beck J, Forstmeier W. Superstition and Belief as Inevitable ByProducts of an Adaptive

Learning Strategy. Human Nature. 2007; 18:35.

Behrens TE, Hunt LT, Rushworth MF. The computation of social behavior. Science. 2009; 324:1160–

1164. [PubMed: 19478175]

Behrens TE, Hunt LT, Woolrich MW, Rushworth MF. Associative learning of social value. Nature.

2008; 456:245–249. [PubMed: 19005555]

Belin D, Jonkman S, Dickinson A, Robbins TW, Everitt BJ. Parallel and interactive learning processes
within the basal ganglia: relevance for the understanding of addiction. Behav Brain Res. 2009;
199:89–102. [PubMed: 18950658]

Belova MA, Paton JJ, Morrison SE, Salzman CD. Expectation modulates neural responses to pleasant
and aversive stimuli in primate amygdala. Neuron. 2007; 55:970–984. [PubMed: 17880899]
Bentall RP, Corcoran R, Howard R, Blackwood N, Kinderman P. Persecutory delusions: a review and

theoretical integration. Clin Psychol Rev. 2001; 21:1143–1192. [PubMed: 11702511]

Berke JD, Hetrick V, Breck J, Greene RW. Transient 23–30 Hz oscillations in mouse hippocampus

during exploration of novel environments. Hippocampus. 2008; 18:519–529. [PubMed: 18398852]

Berridge KC. The debate over dopamine’s role in reward: the case for incentive salience.

Psychopharmacology (Berl). 2007; 191:391–431. [PubMed: 17072591]

Berrios GE. Tactile hallucinations: conceptual and historical aspects. J Neurol Neurosurg Psychiatry.

1982; 45:285–293. [PubMed: 7042917]

Berrios GE. Delusional parasitosis and physical disease. Compr Psychiatry. 1985; 26:395–403.

[PubMed: 4028691]

Berrios GE. Delusions as “wrong beliefs”: a conceptual history. Br J Psychiatry Suppl. 1991:6–13.

[PubMed: 1840782]

Bespalov AY, Harich S, Jongen-Relo AL, van Gaalen MM, Gross G. AMPA receptor antagonists
reverse effects of extended habit training on signaled food approach responding in rats.
Psychopharmacology (Berl). 2007; 195:11–18. [PubMed: 17634927]

Bilder RM, Volavka J, Lachman HM, Grace AA. The catechol-O-methyltransferase polymorphism:

relations to the tonic-phasic dopamine hypothesis and neuropsychiatric phenotypes.
Neuropsychopharmacology. 2004; 29:1943–1961. [PubMed: 15305167]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 31

Binzegger T, Douglas RJ, Martin KA. A quantitative map of the circuit of cat primary visual cortex. J

Neurosci. 2004; 24:8441–8453. [PubMed: 15456817]

Bisiach E, Luzzatti C. Unilateral neglect of representational space. Cortex. 1978; 14:129–133.

[PubMed: 16295118]

Bissiere S, Humeau Y, Luthi A. Dopamine gates LTP induction in lateral amygdala by suppressing

feedforward inhibition. Nat Neurosci. 2003; 6:587–592. [PubMed: 12740581]

Blakemore SJ. Deluding the motor system. Conscious Cogn. 2003; 12:647–655. [PubMed: 14656507]
Blakemore SJ, Frith CD, Wolpert DM. Spatio-temporal prediction modulates the perception of self-

produced stimuli. J Cogn Neurosci. 1999; 11:551–559. [PubMed: 10511643]

Blakemore SJ, Frith CD, Wolpert DM. The cerebellum is involved in predicting the sensory
consequences of action. Neuroreport. 2001; 12:1879–1884. [PubMed: 11435916]
Blakemore SJ, Oakley DA, Frith CD. Delusions of alien control in the normal brain.

Neuropsychologia. 2003; 41:1058–1067. [PubMed: 12667541]

Blakemore SJ, Smith J, Steel R, Johnstone CE, Frith CD. The perception of self-produced sensory
stimuli in patients with auditory hallucinations and passivity experiences: evidence for a
breakdown in self-monitoring. Psychol Med. 2000a; 30:1131–1139. [PubMed: 12027049]
Blakemore SJ, Wolpert D, Frith C. Why can’t you tickle yourself? Neuroreport. 2000b; 11:R11–16.

[PubMed: 10943682]

Blakemore SJ, Wolpert DM, Frith CD. Abnormalities in the awareness of action. Trends Cogn Sci.

2002; 6:237–242. [PubMed: 12039604]

Bleuler E. Die Prognose der Dementia praecox (Schizophreniegruppe). Allgemeine Zeitschrift für

Psychiatrie und psychischgerichtliche Medizin. 1908; 65:436–464.

Bottini G, Bisiach E, Sterzi R, Vallar G. Feeling touches in someone else’s hand. Neuroreport. 2002;

13:249–252. [PubMed: 11893919]

Botvinick M, Cohen J. Rubber hands ‘feel’ touch that eyes see. Nature. 1998; 391:756. [PubMed:

9486643]

Braver TS, Cohen JD. Dopamine, cognitive control, and schizophrenia: the gating model. Prog Brain

Res. 1999; 121:327–349. [PubMed: 10551035]

Bromberg-Martin ES, Hikosaka O. Midbrain dopamine neurons signal preference for advance
information about upcoming rewards. Neuron. 2009; 63:119–126. [PubMed: 19607797]
Bruner J, Bruner J, Postman L. Perception, cognition, and behavior. Journal of Personality. 1949;

18:14.

Buhl EH, Tamas G, Fisahn A. Cholinergic activation and tonic excitation induce persistent gamma
oscillations in mouse somatosensory cortex in vitro. J Physiol. 1998; 513 ( Pt 1):117–126.
[PubMed: 9782163]

Buschman TJ, Miller EK. Top-down versus bottom-up control of attention in the prefrontal and

posterior parietal cortices. Science. 2007; 315:1860–1862. [PubMed: 17395832]
Buzsaki G. The structure of consciousness. Nature. 2007; 446:267. [PubMed: 17361165]
Capgras J, Reboul-Lachaux J. L’illusion des “soises” dans un delire systematise. Bulletin de Society

Clinique de Medicine Mentale. 1923; 11:6–16.

Carlsson A, Waters N, Holm-Waters S, Tedroff J, Nilsson M, Carlsson ML. Interactions between
monoamines, glutamate, and GABA in schizophrenia: new evidence. Annu Rev Pharmacol
Toxicol. 2001; 41:237–260. [PubMed: 11264457]

Carlsson M, Carlsson A. Schizophrenia: a subcortical neurotransmitter imbalance syndrome?

Schizophr Bull. 1990; 16:425–432. [PubMed: 1981107]

Cepeda C, Levine MS. Dopamine and N-methyl-D-aspartate receptor interactions in the neostriatum.

Dev Neurosci. 1998; 20:1–18. [PubMed: 9600386]

Chadwick PK. Peer-professional first-person account: schizophrenia from the inside--phenomenology

and the integration of causes and meanings. Schizophr Bull. 2007; 33:166–173. [PubMed:
16973785]

Charuvastra A, Yaeger D. Tactile hallucinations associated with therapeutic doses of bupropion in 2

patients. J Clin Psychiatry. 2006; 67:1820–1821. [PubMed: 17196068]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 32

Chiu YF, McGrath JA, Thornquist MH, Wolyniec PS, Nestadt G, Swartz KL, Lasseter VK, Liang KY,

Pulver AE. Genetic heterogeneity in schizophrenia II: conditional analyses of affected
schizophrenia sibling pairs provide evidence for an interaction between markers on chromosome
8p and 14q. Mol Psychiatry. 2002; 7:658–664. [PubMed: 12140791]

Chong TT, Cunnington R, Williams MA, Kanwisher N, Mattingley JB. fMRI adaptation reveals mirror
neurons in human inferior parietal cortex. Curr Biol. 2008; 18:1576–1580. [PubMed: 18948009]

Clifford W. The ethics of belief. Contemporary Review. 1877
Colby KM. Appraisal of four psychological theories of paranoid phenomena. J Abnorm Psychol. 1977;

86:54–59. [PubMed: 838949]

Coltheart M. The neuropsychology of delusions. Ann N Y Acad Sci. 2010; 1191:16–26. [PubMed:

20392273]

Coltheart M, Langdon R, McKay R. Schizophrenia and monothematic delusions. Schizophr Bull.

2007; 33:642–647. [PubMed: 17372282]

Coltheart M, Menzies P, Sutton J. Abductive inference and delusional belief. Cogn Neuropsychiatry.

2010; 15:261–287. [PubMed: 20017038]

Conrad, K. Die Beginnende Schizophrenie. G. Thieme; Stuttgart: 1958a.
Conrad, K. Die BeginnendeSchizophrenie. G. Thieme; Stuttgart: 1958b.
Corlett PR, Aitken MR, Dickinson A, Shanks DR, Honey GD, Honey RA, Robbins TW, Bullmore ET,
Fletcher PC. Prediction error during retrospective revaluation of causal associations in humans:
fMRI evidence in favor of an associative model of learning. Neuron. 2004; 44:877–888. [PubMed:
15572117]

Corlett PR, Frith CD, Fletcher PC. From drugs to deprivation: a Bayesian framework for

understanding models of psychosis. Psychopharmacology (Berl). 2009a

Corlett PR, Frith CD, Fletcher PC. From drugs to deprivation: a Bayesian framework for

understanding models of psychosis. Psychopharmacology (Berl). 2009b; 206:515–530. [PubMed:
19475401]

Corlett PR, Honey GD, Aitken MR, Dickinson A, Shanks DR, Absalom AR, Lee M, Pomarol-Clotet
E, Murray GK, McKenna PJ, Robbins TW, Bullmore ET, Fletcher PC. Frontal responses during
learning predict vulnerability to the psychotogenic effects of ketamine: linking cognition, brain
activity, and psychosis. Arch Gen Psychiatry. 2006; 63:611–621. [PubMed: 16754834]

Corlett PR, Honey GD, Fletcher PC. From prediction error to psychosis: ketamine as a

pharmacological model of delusions. J Psychopharmacol. 2007a; 21:238–252. [PubMed:
17591652]

Corlett PR, Krystal JH, Taylor JR, Fletcher PC. Why do delusions persist? Front Hum Neurosci.

2009c; 3:12. [PubMed: 19636384]

Corlett PR, Krystal JK, Taylor JR, Fletcher PC. Why do delusions persist? Frontiers in Human

Neuroscience. 2009 In press.

Corlett PR, Murray GK, Honey GD, Aitken MR, Shanks DR, Robbins TW, Bullmore ET, Dickinson

A, Fletcher PC. Disrupted prediction-error signal in psychosis: evidence for an associative account
of delusions. Brain. 2007b; 130:2387–2400. [PubMed: 17690132]

Corlett PR, Simons JS, Pigott JS, Gardner JM, Murray GK, Krystal JH, Fletcher PC. Illusions and

delusions: relating experimentally-induced false memories to anomalous experiences and ideas.
Front Behav Neurosci. 2009d; 3:53. [PubMed: 19956402]

Cotard J. Du délire hypocondriaque dans une forme grave de la melancolie anxieuse. Memoire lu à la

Société médicopsychologique dans la Séance du 28 Juin 1880. Ann Medico-Psychol Med.
1880:168–174.

Courbon P, Fail G. Syndrome d’ “illusion de Frégoli” et schizophrénie. Bulletin de la Société Clinique

de Médecine Mentale. 1927; 15:121–124.

Courville AC, Daw ND, Touretzky DS. Bayesian theories of conditioning in a changing world. Trends

Cogn Sci. 2006; 10:294–300. [PubMed: 16793323]

Cramer RE, Weiss RF, William R, Reid S, Nieri L, Manning-Ryan B. Human agency and associative
learning: Pavlovian principles govern social process in causal relationship detection. Q J Exp
Psychol B. 2002; 55:241–266. [PubMed: 12188526]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 33

Critchley HD, Mathias CJ, Dolan RJ. Fear conditioning in humans: the influence of awareness and

autonomic arousal on functional neuroanatomy. Neuron. 2002; 33:653–663. [PubMed: 11856537]
D’Souza DC, Sewell RA, Ranganathan M. Cannabis and psychosis/schizophrenia: human studies. Eur

Arch Psychiatry Clin Neurosci. 2009; 259:413–431. [PubMed: 19609589]

Dakin S, Carlin P, Hemsley D. Weak suppression of visual context in chronic schizophrenia. Curr

Biol. 2005; 15:R822–824. [PubMed: 16243017]

Damasio, A. Thinking about Belief: Concluding Remarks. In: Schacter, DL.; Scarry, E., editors.
Memory, Brain and Belief. Harvard University Press; Cambridge Massachussetts / London,
England: 2000.

Daw ND, Niv Y, Dayan P. Uncertainty-based competition between prefrontal and dorsolateral striatal

systems for behavioral control. Nat Neurosci. 2005; 8:1704–1711. [PubMed: 16286932]

De Clerambault GG. Les Psychoses Passionelles. Oeuvere Psychiatrique:Paris: Presses Universities,

de France. 1942; 331:337–339. 357, 408.

De Lacoste MC, White CL 3rd. The role of cortical connectivity in Alzheimer’s disease pathogenesis:

a review and model system. Neurobiol Aging. 1993; 14:1–16. [PubMed: 8450928]

Delespaul P, van Os J. Jaspers was right after all--delusions are distinct from normal beliefs. Against.

Br J Psychiatry. 2003; 183:286. [PubMed: 14575030]

Delgado MR, Li J, Schiller D, Phelps EA. The role of the striatum in aversive learning and aversive
prediction errors. Philos Trans R Soc Lond B Biol Sci. 2008a; 363:3787–3800. [PubMed:
18829426]

Delgado MR, Nearing KI, Ledoux JE, Phelps EA. Neural circuitry underlying the regulation of

conditioned fear and its relation to extinction. Neuron. 2008b; 59:829–838. [PubMed: 18786365]

den Ouden HE, Daunizeau J, Roiser J, Friston KJ, Stephan KE. Striatal prediction error modulates

cortical coupling. J Neurosci. 2010; 30:3210–3219. [PubMed: 20203180]

den Ouden HE, Friston KJ, Daw ND, McIntosh AR, Stephan KE. A dual role for prediction error in

associative learning. Cereb Cortex. 2009; 19:1175–1185. [PubMed: 18820290]

Dennett, D. Do animals have beliefs. In: Roitblat, HL.; Meyer, JA., editors. Comparative Approaches

to Cognitive Science. MIT Press; Cambrudge Massachusetts; London, England: 1995.

Devenport LD. Superstitious bar pressing in hippocampal and septal rats. Science. 1979; 205:721–723.

[PubMed: 462183]

Devinsky O. Delusional misidentifications and duplications: right brain lesions, left brain delusions.

Neurology. 2009; 72:80–87. [PubMed: 19122035]

Dickinson A. The 28th Bartlett Memorial Lecture. Causal learning: an associative analysis. Q J Exp

Psychol B. 2001; 54:3–25. [PubMed: 11216300]

Dima D, Roiser JP, Dietrich DE, Bonnemann C, Lanfermann H, Emrich HM, Dillo W. Understanding
why patients with schizophrenia do not perceive the hollow-mask illusion using dynamic causal
modelling. Neuroimage. 2009; 46:1180–1186. [PubMed: 19327402]

Dommett E, Coizet V, Blaha CD, Martindale J, Lefebvre V, Walton N, Mayhew JE, Overton PG,

Redgrave P. How visual stimuli activate dopaminergic neurons at short latency. Science. 2005;
307:1476–1479. [PubMed: 15746431]

Eichenbaum, H.; Bodkin, JA. Belief and knowledge as distinct forms of memory. In: Schacter, DL.;

Scarry, E., editors. Memory Brain and Belief. Harvard University Press; Cambridge,
Massachusetts/London England: 2000.

Eisenhardt D, Menzel R. Extinction learning, reconsolidation and the internal reinforcement

hypothesis. Neurobiol Learn Mem. 2007; 87:167–173. [PubMed: 17079171]

Ellinwood EH Jr. Amphetamine psychosis. II. Theoretical implications. Int J Neuropsychiatry. 1968;

4:45–54. [PubMed: 5645819]

Ellinwood EH Jr, Sudilovsky A, Nelson LM. Behavior and EEG analysis of chronic amphetamine

effect. Biol Psychiatry. 1974; 8:169–176. [PubMed: 4858385]

Ellis HD, Young AW. Accounting for delusional misidentifications. Br J Psychiatry. 1990; 157:239–

248. [PubMed: 2224375]

Ellison DG. Hallucinations produced by sensory conditioning. Journal of Experimental Psychology.

1941; 28:1–20.

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 34

Ellison G. Stimulant-induced psychosis, the dopamine theory of schizophrenia, and the habenula.

Brain Res Brain Res Rev. 1994; 19:223–239. [PubMed: 7914793]

Emrich HM. A three-component-system hypothesis of psychosis. Impairment of binocular depth
inversion as an indicator of a functional dysequilibrium. Br J Psychiatry Suppl. 1989:37–39.
[PubMed: 2690888]

Estes WK. Processes of memory loss, recovery, and distortion. Psychol Rev. 1997; 104:148–169.

[PubMed: 9009883]

Farrer C, Frey SH, Van Horn JD, Tunik E, Turk D, Inati S, Grafton ST. The angular gyrus computes
action awareness representations. Cereb Cortex. 2008; 18:254–261. [PubMed: 17490989]
Feinberg TE. The nested heirarchy of consciousness: A neurobiological soultion to the problem of

mental unity. Neurocase. 2000; 6:75–81.

Feinberg TE, Keenan JP. Where in the brain is the self? Conscious Cogn. 2005; 14:661–678.

[PubMed: 16325140]

Fiorillo CD. Towards a general theory of neural computation based on prediction by single neurons.

PLoS ONE. 2008; 3:e3298. [PubMed: 18827880]

Fiorillo CD, Tobler PN, Schultz W. Discrete coding of reward probability and uncertainty by

dopamine neurons. Science. 2003; 299:1898–1902. [PubMed: 12649484]

Fiser J. Perceptual learning and representational learning in humans and animals. Learn Behav. 2009;

37:141–153. [PubMed: 19380891]

Fiser J, Berkes P, Orban G, Lengyel M. Statistically optimal perception and learning: from behavior to

neural representations. Trends Cogn Sci. 2010; 14:119–130. [PubMed: 20153683]
Fleminger S. Seeing is believing: the role of ‘preconscious’ perceptual processing in delusional

misidentification. Br J Psychiatry. 1992; 160:293–303. [PubMed: 1562856]

Fletcher PC, Anderson JM, Shanks DR, Honey R, Carpenter TA, Donovan T, Papadakis N, Bullmore
ET. Responses of human frontal cortex to surprising events are predicted by formal associative
learning theory. Nat Neurosci. 2001; 4:1043–1048. [PubMed: 11559855]

Fletcher PC, Frith CD. Perceiving is believing: a Bayesian approach to explaining the positive

symptoms of schizophrenia. Nat Rev Neurosci. 2009; 10:48–58. [PubMed: 19050712]

Fletcher PC, Henson RN. Frontal lobes and human memory: insights from functional neuroimaging.

Brain. 2001; 124:849–881. [PubMed: 11335690]

Flint AJ. Delusions in dementia: a review. J Neuropsychiatry Clin Neurosci. 1991; 3:121–130.

[PubMed: 1687962]

Fogassi L, Luppino G. Motor functions of the parietal lobe. Curr Opin Neurobiol. 2005; 15:626–631.

[PubMed: 16271458]

Ford JM, Mathalon DH. Corollary discharge dysfunction in schizophrenia: can it explain auditory

hallucinations? Int J Psychophysiol. 2005; 58:179–189. [PubMed: 16137779]

Ford JM, Roach BJ, Faustman WO, Mathalon DH. Synch before you speak: auditory hallucinations in

schizophrenia. Am J Psychiatry. 2007; 164:458–466. [PubMed: 17329471]

Fourneret P, Paillard J, Lamarre Y, Cole J, Jeannerod M. Lack of conscious recognition of one’s own

actions in a haptically deafferented patient. Neuroreport. 2002; 13:541–547. [PubMed:
11930177]

Franck N, Posada A, Pichon S, Haggard P. Altered subjective time of events in schizophrenia. J Nerv

Ment Dis. 2005; 193:350–353. [PubMed: 15870620]

Frank MJ, Moustafa AA, Haughey HM, Curran T, Hutchison KE. Genetic triple dissociation reveals
multiple roles for dopamine in reinforcement learning. Proc Natl Acad Sci U S A. 2007;
104:16311–16316. [PubMed: 17913879]

Freeman D, Garety PA, Kuipers E, Fowler D, Bebbington PE. A cognitive model of persecutory

delusions. Br J Clin Psychol. 2002; 41:331–347. [PubMed: 12437789]

Freeman D, Garety PA, Kuipers E, Fowler D, Bebbington PE, Dunn G. Acting on persecutory
delusions: the importance of safety seeking. Behav Res Ther. 2007; 45:89–99. [PubMed:
16530161]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 35

Freeman TP, Morgan CJ, Klaassen E, Das RK, Stefanovic A, Brandner B, Curran HV. Superstitious
conditioning as a model of delusion formation following chronic but not acute ketamine in
humans. Psychopharmacology (Berl). 2009

Friston K. Disconnection and cognitive dysmetria in schizophrenia. Am J Psychiatry. 2005a; 162:429–

432. [PubMed: 15741456]

Friston K. A theory of cortical responses. Philos Trans R Soc Lond B Biol Sci. 2005b; 360:815–836.

[PubMed: 15937014]

Friston K. The free-energy principle: a rough guide to the brain? Trends Cogn Sci. 2009; 13:293–301.

[PubMed: 19559644]

Friston K. The free-energy principle: a unified brain theory? Nat Rev Neurosci. 2010; 11:127–138.

[PubMed: 20068583]

Friston KJ. Hallucinations and perceptual inherence. Behavioral and Brain Sciences. 2005c; 28:764–

766.

Friston KJ, Daunizeau J, Kiebel SJ. Reinforcement learning or active inference? PLoS One. 2009;

4:e6421. [PubMed: 19641614]

Friston KJ, Frith CD. Schizophrenia: a disconnection syndrome? Clin Neurosci. 1995; 3:89–97.

[PubMed: 7583624]

Frith C. The neural basis of hallucinations and delusions. C R Biol. 2005; 328:169–175. [PubMed:

15771003]

Frith CD, Blakemore S, Wolpert DM. Explaining the symptoms of schizophrenia: abnormalities in the
awareness of action. Brain Res Brain Res Rev. 2000a; 31:357–363. [PubMed: 10719163]
Frith CD, Blakemore SJ, Wolpert DM. Abnormalities in the awareness and control of action. Philos

Trans R Soc Lond B Biol Sci. 2000b; 355:1771–1788. [PubMed: 11205340]

Frith, CD.; Dolan, RJ. The role of memory in the delusions associated with schizophrenia. In:

Schacher, D.; Scarry, E., editors. Memory, Brain and Belief. Harvard University Press; 2000.

Fuster JM. The prefrontal cortex--an update: time is of the essence. Neuron. 2001; 30:319–333.

[PubMed: 11394996]

Gallese V, Fadiga L, Fogassi L, Rizzolatti G. Action recognition in the premotor cortex. Brain. 1996;

119 ( Pt 2):593–609. [PubMed: 8800951]

Gallese V, Keysers C, Rizzolatti G. A unifying view of the basis of social cognition. Trends Cogn Sci.

2004; 8:396–403. [PubMed: 15350240]

Garety P. Reasoning and delusions. Br J Psychiatry Suppl. 1991:14–18. [PubMed: 1840774]
Garety PA, Freeman D. Cognitive approaches to delusions: a critical review of theories and evidence.

Br J Clin Psychol. 1999; 38 ( Pt 2):113–154. [PubMed: 10389596]

Geldard FA, Sherrick CE. The cutaneous “rabbit”: a perceptual illusion. Science. 1972; 178:178–179.

[PubMed: 5076909]

Gerrans P. A one-stage explanation of the Cotard delusion. Philosophy, Psychiatry & Psychology.

2002; 9:47–53.

Geyer MA, Vollenweider FX. Serotonin research: contributions to understanding psychoses. Trends

Pharmacol Sci. 2008; 29:445–453. [PubMed: 19086254]

Ghoreishi A. A somatic type delusional disorder secondary to peripheral neuropathy: a case report.

Psychiatria Danubina. 2010; 20:85–87. [PubMed: 18376336]

Gilbert DT, Wilson TD. Why the brain talks to itself: sources of error in emotional prediction. Philos

Trans R Soc Lond B Biol Sci. 2009; 364:1335–1341. [PubMed: 19528015]

Glymour C. We believe in freedom of the will so we can learn [Comment on Wegner, Precis of the

Illusion of Conscious Will. Behavioral and Brain Sciences. 2004; 27:661–662.
Goldreich D. A Bayesian perceptual model replicates the cutaneous rabbit and other tactile

spatiotemporal illusions. PLoS One. 2007; 2:e333. [PubMed: 17389923]

Goldstone R. Effects of categorization on color perception. Psychological Science. 1995; 6:298–304.
Goto Y, O’Donnell P. Network synchrony in the nucleus accumbens in vivo. J Neurosci. 2001;

21:4498–4504. [PubMed: 11404437]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 36

Gourion D, Leroy S, Bourdel MC, Goldberger C, Poirier MF, Olie JP, Krebs MO. Cerebellum

development and schizophrenia: an association study of the human homeogene Engrailed 2.
Psychiatry Res. 2004; 126:93–98. [PubMed: 15123388]

Grabenhorst F, Rolls ET, Bilderbeck A. How cognition modulates affective responses to taste and

flavor: top-down influences on the orbitofrontal and pregenual cingulate cortices. Cereb Cortex.
2008; 18:1549–1559. [PubMed: 18056086]

Grace AA. Phasic versus tonic dopamine release and the modulation of dopamine system responsivity:
a hypothesis for the etiology of schizophrenia. Neuroscience. 1991; 41:1–24. [PubMed: 1676137]
Grace AA, Floresco SB, Goto Y, Lodge DJ. Regulation of firing of dopaminergic neurons and control

of goal-directed behaviors. Trends Neurosci. 2007; 30:220–227. [PubMed: 17400299]

Gray JA. On biology, phenomenology, and pharmacology in schizophrenia. Am J Psychiatry. 2004;

161:377. author reply 377–378. [PubMed: 14754801]

Gray JA, Feldon J, Rawlins JNP, Hemsley D, Smith AD. The Neuropsychology of Schizophrenia.

Behav Brain Sci. 1991; 14:1–84.

Graziano MS, Gross CG. A bimodal map of space: somatosensory receptive fields in the macaque

putamen with corresponding visual receptive fields. Exp Brain Res. 1993; 97:96–109. [PubMed:
8131835]

Grossberg S. Processing of expected and unexpected events during conditioning and attention: a

psychophysiological theory. Psychol Rev. 1982; 89:529–572. [PubMed: 7178332]

Grossberg S. How hallucinations may arise from brain mechanisms of learning, attention, and volition.

J Int Neuropsychol Soc. 2000; 6:583–592. [PubMed: 10932478]

Grossberg S. Cortical and subcortical predictive dynamics and learning during perception, cognition,
emotion and action. Philos Trans R Soc Lond B Biol Sci. 2009; 364:1223–1234. [PubMed:
19528003]

Haber SN. The primate basal ganglia: parallel and integrative networks. J Chem Neuroanat. 2003;

26:317–330. [PubMed: 14729134]

Haber SN, Kim KS, Mailly P, Calzavara R. Reward-related cortical inputs define a large striatal region

in primates that interface with associative cortical connections, providing a substrate for
incentive-based learning. J Neurosci. 2006; 26:8368–8376. [PubMed: 16899732]

Haggard P, Martin F, Taylor-Clarke M, Jeannerod M, Franck N. Awareness of action in schizophrenia.

Neuroreport. 2003; 14:1081–1085. [PubMed: 12802207]

Haider B, Duque A, Hasenstaub AR, McCormick DA. Neocortical network activity in vivo is

generated through a dynamic balance of excitation and inhibition. J Neurosci. 2006; 26:4535–
4545. [PubMed: 16641233]

Hall J, Romaniuk L, McIntosh AM, Steele JD, Johnstone EC, Lawrie SM. Associative learning and the

genetics of schizophrenia. Trends Neurosci. 2009; 32:359–365. [PubMed: 19427043]

Halligan PW, David AS. Cognitive neuropsychiatry: towards a scientific psychopathology. Nat Rev

Neurosci. 2001; 2:209–215. [PubMed: 11256082]

Hamamura T, Harada T. Unique pharmacological profile of aripiprazole as the phasic component

buster. Psychopharmacology (Berl). 2007; 191:741–743. [PubMed: 17205315]

Hampton AN, Bossaerts P, O’Doherty JP. Neural correlates of mentalizing-related computations
during strategic interactions in humans. Proc Natl Acad Sci U S A. 2008; 105:6741–6746.
[PubMed: 18427116]

Hasselmo ME, Rolls ET, Baylis GC. The role of expression and identity in the face-selective responses
of neurons in the temporal visual cortex of the monkey. Behav Brain Res. 1989a; 32:203–218.
[PubMed: 2713076]

Hasselmo ME, Rolls ET, Baylis GC, Nalwa V. Object-centered encoding by face-selective neurons in

the cortex in the superior temporal sulcus of the monkey. Exp Brain Res. 1989b; 75:417–429.
[PubMed: 2721619]

Heaven L, McBrayer D. External motivators of self-touching behavior. Percept Mot Skills. 2000;

90:338–342. [PubMed: 10769920]

Hebb, DO. The Organization of Behavior. John Wiley; 1949a.
Hebb, DO. The organization of behaviour: a neuropsychological theory. Wiley; New York: 1949b.

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 37

Heinks-Maldonado TH, Mathalon DH, Houde JF, Gray M, Faustman WO, Ford JM. Relationship of
imprecise corollary discharge in schizophrenia to auditory hallucinations. Arch Gen Psychiatry.
2007; 64:286–296. [PubMed: 17339517]

von Helmholtz, H. The Facts of Perception. In: Kahl, R., editor. Selected Writings of Herman von

Helmholtz. Weslyan University Press; 1878/1971.

Hemsley, DR. Perceptual and cognitive abnormalities as the basis for schizophrenic symptoms. In:
David, AS.; Cutting, JC., editors. The Neuropsychology of Schizophrenia. Laurence Erlbaum
Associates; Hove, UK: 1994. p. 97-118.

Hemsley DR, Garety PA. The formation and maintenance of delusions: a Bayesian analysis. Br J

Psychiatry. 1986a; 149:51–56. [PubMed: 3779313]

Hemsley DR, Garety PA. The formation of maintenance of delusions: a Bayesian analysis. Br J

Psychiatry. 1986b; 149:51–56. [PubMed: 3779313]

Hendricks, KV.; Wiggers, P.; Jonker, CM.; Haselager, WF. Towards a computational model of the
self-attribution of agency. In: Oliver, P.; Kray, C., editors. the artificial intelligence and
simulation of behaviour annual convention. 2007. p. 350-356.

Herrero JL, Roberts MJ, Delicato LS, Gieselmann MA, Dayan P, Thiele A. Acetylcholine contributes

through muscarinic receptors to attentional modulation in V1. Nature. 2008; 454:1110–1114.
[PubMed: 18633352]

Heyes C. Mesmerising mirror neurons. Neuroimage. 2010; 51:789–791. [PubMed: 20167276]
Heyser CJ, Fienberg AA, Greengard P, Gold LH. DARPP-32 knockout mice exhibit impaired reversal

learning in a discriminated operant task. Brain Res. 2000; 867:122–130. [PubMed: 10837805]

Hikosaka O, Bromberg-Martin E, Hong S, Matsumoto M. New insights on the subcortical

representation of reward. Curr Opin Neurobiol. 2008a; 18:203–208. [PubMed: 18674617]
Hikosaka O, Sesack SR, Lecourtier L, Shepard PD. Habenula: crossroad between the basal ganglia and

the limbic system. J Neurosci. 2008b; 28:11825–11829. [PubMed: 19005047]

Hirono N, Cummings JL. Neuropsychiatric aspects of dementia with Lewy bodies. Curr Psychiatry

Rep. 1999; 1:85–92. [PubMed: 11122909]

Hitchcott PK, Quinn JJ, Taylor JR. Bidirectional modulation of goal-directed actions by prefrontal

cortical dopamine. Cereb Cortex. 2007; 17:2820–2827. [PubMed: 17322558]

Hoffman RE, Dobscha SK. Cortical pruning and the development of schizophrenia: a computer model.

Schizophr Bull. 1989; 15:477–490. [PubMed: 2814376]

Holland PC, Gallagher M. Amygdala central nucleus lesions disrupt increments, but not decrements, in
conditioned stimulus processing. Behav Neurosci. 1993a; 107:246–253. [PubMed: 8484890]
Holland PC, Gallagher M. Effects of amygdala central nucleus lesions on blocking and unblocking.

Behav Neurosci. 1993b; 107:235–245. [PubMed: 8484889]

Holland PC, Gallagher M. Amygdala circuitry in attentional and representational processes. Trends

Cogn Sci. 1999; 3:65–73. [PubMed: 10234229]

Holland PC, Gallagher M. Different roles for amygdala central nucleus and substantia innominata in
the surprise-induced enhancement of learning. J Neurosci. 2006; 26:3791–3797. [PubMed:
16597732]

Holt DJ, Lebron-Milad K, Milad MR, Rauch SL, Pitman RK, Orr SP, Cassidy BS, Walsh JP, Goff DC.

Extinction Memory Is Impaired in Schizophrenia. Biol Psychiatry. 2008

Hornak J, O’Doherty J, Bramham J, Rolls ET, Morris RG, Bullock PR, Polkey CE. Reward-related

reversal learning after surgical excisions in orbito-frontal or dorsolateral prefrontal cortex in
humans. J Cogn Neurosci. 2004; 16:463–478. [PubMed: 15072681]

Houran J, Houran J. Preliminary study of tolerance of ambiguity of individuals reporting paranormal

experiences. Psychological Reports. 1998; 82:183. [PubMed: 9520551]

Howes OD, Montgomery AJ, Asselin MC, Murray RM, Valli I, Tabraham P, Bramon-Bosch E,
Valmaggia L, Johns L, Broome M, McGuire PK, Grasby PM. Elevated striatal dopamine
function linked to prodromal signs of schizophrenia. Arch Gen Psychiatry. 2009; 66:13–20.
[PubMed: 19124684]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 38

Huber M, Karner M, Kirchler E, Lepping P, Freudenmann RW. Striatal lesions in delusional
parasitosis revealed by magnetic resonance imaging. Prog Neuropsychopharmacol Biol
Psychiatry. 2008; 32:1967–1971. [PubMed: 18930778]

Hudson LA, Rollins YD, Anderson CA, Johnston-Brooks C, Tyler KL, Filley CM. Reduplicative
paramnesia in Morvan’s syndrome. J Neurol Sci. 2008; 267:154–157. [PubMed: 17928004]

Hume, D. A treatise of human nature. Oxford University Press; Oxford: 1739/2007.
Ito M. Movement and thought: identical control mechanisms by the cerebellum. Trends Neurosci.

1993; 16:448–450. discussion 453–444. [PubMed: 7507615]

Jackson ME, Homayoun H, Moghaddam B. NMDA receptor hypofunction produces concomitant

firing rate potentiation and burst activity reduction in the prefrontal cortex. Proc Natl Acad Sci U
S A. 2004; 101:8467–8472. [PubMed: 15159546]

Jaspers, K. General Psychopathology. Manchester University Press; 1963.
Jeannerod M. The hand and the object: the role of posterior parietal cortex in forming motor
representations. Can J Physiol Pharmacol. 1994; 72:535–541. [PubMed: 7954083]

Joliot M, Ribary U, Llinas R. Human oscillatory brain activity near 40 Hz coexists with cognitive

temporal binding. Proc Natl Acad Sci U S A. 1994; 91:11748–11751. [PubMed: 7972135]

Jones H. Defining delusion. Br J Psychiatry. 2004; 185:354–355. [PubMed: 15459001]
Kalayasiri R, Sughondhabirom A, Gueorguieva R, Coric V, Lynch WJ, Morgan PT, Cubells JF,

Malison RT. Self-reported paranoia during laboratory “binge” cocaine self-administration in
humans. Pharmacol Biochem Behav. 2006; 83:249–256. [PubMed: 16549106]

Kandel ER. A new intellectual framework for psychiatry. Am J Psychiatry. 1998; 155:457–469.

[PubMed: 9545989]

Kaney S, Bentall RP. Persecutory delusions and the self-serving bias. Evidence from a contingency

judgment task. J Nerv Ment Dis. 1992; 180:773–780. [PubMed: 1469376]

Kapur S. Psychosis as a state of aberrant salience: a framework linking biology, phenomenology, and
pharmacology in schizophrenia. Am J Psychiatry. 2003; 160:13–23. [PubMed: 12505794]
Karson CN. A new look at delusions of grandeur. Compr Psychiatry. 1980; 21:62–69. [PubMed:

7357864]

Keinan G, Keinan G. Effects of stress and tolerance of ambiguity on magical thinking. Journal of

Personality and Social Psychology. 1994; 67:48.

Keysers C, Wicker B, Gazzola V, Anton JL, Fogassi L, Gallese V. A touching sight: SII/PV activation

during the observation and experience of touch. Neuron. 2004; 42:335–346. [PubMed:
15091347]

Kihlstrom, JF.; Hoyt, IP. Hypnosis and the Psychology of Delusions. In: Oltmanns, TF.; Maher, BA.,

editors. Delusional Beliefs. Wiley; New York: 1988.

Kilner JM, Friston KJ, Frith CD. The mirror-neuron system: a Bayesian perspective. Neuroreport.

2007a; 18:619–623. [PubMed: 17413668]

Kilner JM, Friston KJ, Frith CD. Predictive coding: an account of the mirror neuron system. Cogn

Process. 2007b; 8:159–166. [PubMed: 17429704]

Kilner JM, Neal A, Weiskopf N, Friston KJ, Frith CD. Evidence of mirror neurons in human inferior

frontal gyrus. J Neurosci. 2009; 29:10153–10159. [PubMed: 19675249]

Kinderman P, Bentall RP. Self-discrepancies and persecutory delusions: evidence for a model of

paranoid ideation. J Abnorm Psychol. 1996; 105:106–113. [PubMed: 8666699]

Kinderman P, Bentall RP. Causal attributions in paranoia and depression: internal, personal, and

situational attributions for negative events. J Abnorm Psychol. 1997; 106:341–345. [PubMed:
9131855]

King R, Barchas JD, Huberman BA. Chaotic behavior in dopamine neurodynamics. Proc Natl Acad

Sci U S A. 1984; 81:1244–1247. [PubMed: 6583705]

Knobel A, Heinz A, Voss M. Imaging the deluded brain. Eur Arch Psychiatry Clin Neurosci. 2008;

258(Suppl 5):76–80. [PubMed: 18985300]

Koechlin E, Anton JL, Burnod Y. Dynamical computational properties of local cortical networks for
visual and motor processing: a bayesian framework. J Physiol Paris. 1996; 90:257–262.
[PubMed: 9116679]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 39

Konorski, J. Conditioned reflexes and neuron organization. Cambridge University Press; 1948.
Kosslyn SM, Chabris CF, Marsolek CJ, Koenig O. Categorical versus coordinate spatial relations:

computational analyses and computer simulations. J Exp Psychol Hum Percept Perform. 1992;
18:562–577. [PubMed: 1593235]

Kot T, Serper M. Increased susceptibility to auditory conditioning in hallucinating schizophrenic

patients: a preliminary investigation. J Nerv Ment Dis. 2002; 190:282–288. [PubMed: 12011606]

Kraeplin, E. Clinical Psychiatry. MacMillan; New York: 1902.
Kromkamp M, Uylings HB, Smidt MP, Hellemons AJ, Burbach JP, Kahn RS. Decreased thalamic

expression of the homeobox gene DLX1 in psychosis. Arch Gen Psychiatry. 2003; 60:869–874.
[PubMed: 12963668]

Krystal JH, Karper LP, Seibyl JP, Freeman GK, Delaney R, Bremner JD, Heninger GR, Bowers MB

Jr, Charney DS. Subanesthetic effects of the noncompetitive NMDA antagonist, ketamine, in
humans. Psychotomimetic, perceptual, cognitive, and neuroendocrine responses. Arch Gen
Psychiatry. 1994; 51:199–214. [PubMed: 8122957]

Kurylo DD, Gazes Y. Effects of Ketamine on perceptual grouping in rats. Physiol Behav. 2008;

95:152–156. [PubMed: 18571682]

Ladavas E, Zeloni G, Farne A. Visual peripersonal space centred on the face in humans. Brain. 1998;

121 (Pt 12):2317–2326. [PubMed: 9874482]

Lange R, Lange R, Houran J. Delusions of the paranormal: A haunting question of perception. Journal

of Nervous and Mental Disease. 1998; 186:637. [PubMed: 9788641]

Lapish CC, Seamans JK, Chandler LJ. Glutamate-dopamine cotransmission and reward processing in

addiction. Alcohol Clin Exp Res. 2006; 30:1451–1465. [PubMed: 16930207]
Laruelle M, Kegeles LS, Abi-Dargham A. Glutamate, dopamine, and schizophrenia: from

pathophysiology to treatment. Ann N Y Acad Sci. 2003; 1003:138–158. [PubMed: 14684442]
Lasegue C, Falret J. La folie a deux (ou folie communiquee). Ann Med Psychol. 1877; 18:321–355.
Lau HC, Rogers RD, Passingham RE. Manipulating the experienced onset of intention after action

execution. J Cogn Neurosci. 2007; 19:81–90. [PubMed: 17214565]

Lavin A, Nogueira L, Lapish CC, Wightman RM, Phillips PE, Seamans JK. Mesocortical dopamine

neurons operate in distinct temporal domains using multimodal signaling. J Neurosci. 2005;
25:5013–5023. [PubMed: 15901782]

Laviolette SR, Grace AA. The roles of cannabinoid and dopamine receptor systems in neural

emotional learning circuits: implications for schizophrenia and addiction. Cell Mol Life Sci.
2006; 63:1597–1613. [PubMed: 16699809]

Lazarus A. Folie a deux in identical twins: interaction of nature and nurture. Br J Psychiatry. 1986;

148:324–326. [PubMed: 3719226]

Lecourtier L, Defrancesco A, Moghaddam B. Differential tonic influence of lateral habenula on

prefrontal cortex and nucleus accumbens dopamine release. Eur J Neurosci. 2008; 27:1755–1762.
[PubMed: 18380670]

Lee D. Game theory and neural basis of social decision making. Nat Neurosci. 2008a; 11:404–409.

[PubMed: 18368047]

Lee HJ, Groshek F, Petrovich GD, Cantalini JP, Gallagher M, Holland PC. Role of amygdalo-nigral

circuitry in conditioning of a visual stimulus paired with food. J Neurosci. 2005; 25:3881–3888.
[PubMed: 15829640]

Lee JL. Memory reconsolidation mediates the strengthening of memories by additional learning. Nat

Neurosci. 2008b; 11:1264–1266. [PubMed: 18849987]

Lingnau A, Gesierich B, Caramazza A. Asymmetric fMRI adaptation reveals no evidence for mirror

neurons in humans. Proc Natl Acad Sci U S A. 2009; 106:9925–9930. [PubMed: 19497880]

Lisman J, Buzsaki G. A neural coding scheme formed by the combined function of gamma and theta

oscillations. Schizophr Bull. 2008; 34:974–980. [PubMed: 18559405]

Lisman J, Redish AD. Prediction, sequences and the hippocampus. Philos Trans R Soc Lond B Biol

Sci. 2009; 364:1193–1201. [PubMed: 19528000]

Lisman JE, Grace AA. The hippocampal-VTA loop: controlling the entry of information into long-

term memory. Neuron. 2005; 46:703–713. [PubMed: 15924857]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 40

Llinas RR, Roy S. The ‘prediction imperative’ as the basis for self-awareness. Philos Trans R Soc

Lond B Biol Sci. 2009; 364:1301–1307. [PubMed: 19528011]

Lodge DJ, Grace AA. The hippocampus modulates dopamine neuron responsivity by regulating the
intensity of phasic neuron activation. Neuropsychopharmacology. 2006a; 31:1356–1361.
[PubMed: 16319915]

Lodge DJ, Grace AA. The laterodorsal tegmentum is essential for burst firing of ventral tegmental area
dopamine neurons. Proc Natl Acad Sci U S A. 2006b; 103:5167–5172. [PubMed: 16549786]
Loh M, Rolls ET, Deco G. A dynamical systems hypothesis of schizophrenia. PLoS Comput Biol.

2007; 3:e228. [PubMed: 17997599]

Long JE, Swan C, Liang WS, Cobos I, Potter GB, Rubenstein JL. Dlx1&2 and Mash1 transcription

factors control striatal patterning and differentiation through parallel and overlapping pathways. J
Comp Neurol. 2009; 512:556–572. [PubMed: 19030180]

Ma WJ, Beck JM, Latham PE, Pouget A. Bayesian inference with probabilistic population codes. Nat

Neurosci. 2006; 9:1432–1438. [PubMed: 17057707]

Mackintosh NJ. A theory of attention: Variations in the associability of stimuli with reinforcement.

Psychological Review. 1975:82.

Maher BA. Delusional thinking and perceptual disorder. J Individ Psychol. 1974; 30:98–113.

[PubMed: 4857199]

Maher, BA. Delusions as normal theories. Wiley; New York: 1988.
Makin TR, Holmes NP, Ehrsson HH. On the other hand: dummy hands and peripersonal space. Behav

Brain Res. 2008; 191:1–10. [PubMed: 18423906]

Matsumoto M, Hikosaka O. Two types of dopamine neuron distinctly convey positive and negative

motivational signals. Nature. 2009; 459:837–841. [PubMed: 19448610]

Maxwell SL, Li M. Midbrain dopaminergic development in vivo and in vitro from embryonic stem

cells. J Anat. 2005; 207:209–218. [PubMed: 16185245]

McCurdy HG. Coin perception studies and the concept of schemata. Psychological Review. 1956;

63:160–168. [PubMed: 13323171]

McDonald RJ, Hong NS. A dissociation of dorso-lateral striatum and amygdala function on the same

stimulus-response habit task. Neuroscience. 2004; 124:507–513. [PubMed: 14980722]

McGhie A, Chapman J. Disorders of attention and perception in early schizophrenia. Br J Med

Psychol. 1961; 34:103–116. [PubMed: 13773940]

McKay R, Langdon R, Coltheart M. Models of misbelief: Integrating motivational and deficit theories

of delusions. Conscious Cogn. 2007; 16:932–941. [PubMed: 17331741]

McLaren IP, Dickinson A. The conditioning connection. Philos Trans R Soc Lond B Biol Sci. 1990;

329:179–186. [PubMed: 1978363]

Mellor CS. First rank symptoms of schizophrenia. I. The frequnncy in schizophrenics on admission to
hospital. II. Differences between individual first rank symptoms. Br J Psychiatry. 1970; 117:15–
23. [PubMed: 5479324]

Melo SS, Taylor JL, Bentall RP. ‘Poor me’ versus ‘bad me’ paranoia and the instability of persecutory

ideation. Psychol Psychother. 2006; 79:271–287. [PubMed: 16774723]

Mesulam M. Representation, inference, and transcendent encoding in neurocognitive networks of the

human brain. Ann Neurol. 2008; 64:367–378. [PubMed: 18991346]

Meyer-Lindenberg A, Straub RE, Lipska BK, Verchinski BA, Goldberg T, Callicott JH, Egan MF,
Huffaker SS, Mattay VS, Kolachana B, Kleinman JE, Weinberger DR. Genetic evidence
implicating DARPP-32 in human frontostriatal structure, function, and cognition. J Clin Invest.
2007; 117:672–682. [PubMed: 17290303]

Milad MR, Quirk GJ, Pitman RK, Orr SP, Fischl B, Rauch SL. A role for the human dorsal anterior

cingulate cortex in fear expression. Biol Psychiatry. 2007; 62:1191–1194. [PubMed: 17707349]

Milad MR, Vidal-Gonzalez I, Quirk GJ. Electrical stimulation of medial prefrontal cortex reduces
conditioned fear in a temporally specific manner. Behav Neurosci. 2004; 118:389–394.
[PubMed: 15113265]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 41

Miller, NE. Liberalization of basic S-R concepts: Extensions to conflict behaviour, motivation and

social learning. In: Kock, S., editor. Psychology: A study of a science. McGraw-Hill; New York:
1959. p. 196-292.

Miller R. Schizophrenic psychology, associative learning and the role of forebrain dopamine. Med

Hypotheses. 1976; 2:203–211. [PubMed: 9558]

Miltner WH, Braun C, Arnold M, Witte H, Taub E. Coherence of gamma-band EEG activity as a basis

for associative learning. Nature. 1999; 397:434–436. [PubMed: 9989409]

Milton F, Patwa VK, Hafner RJ. Confrontation vs. belief modification in persistently deluded patients.

Br J Med Psychol. 1978; 51:127–130. [PubMed: 646958]

Misanin JR, Miller RR, Lewis DJ. Retrograde amnesia produced by electroconvulsive shock after

reactivation of a consolidated memory trace. Science. 1968; 160:554–555. [PubMed: 5689415]

Mishara AL. Is minimal self preserved in schizophrenia? A subcomponents view. Conscious Cogn.

2007; 16:715–721. [PubMed: 17920523]

Mishara AL, Corlett PR. Are delusions biologically adaptive? Salvaging the doxastic shear pin.

Behavioral and Brain Sciences. 2009; 32:530–531.

Mitchell CW. Effects of subliminally presented auditory suggestions of itching on scratching behavior.

Percept Mot Skills. 1995; 80:87–96. [PubMed: 7624224]

Mitchell J, Vierkant AD. Delusions and hallucinations of cocaine abusers and paranoid schizophrenics:

a comparative study. J Psychol. 1991; 125:301–310. [PubMed: 1880755]

Mittleman G, Whishaw IQ, Jones GH, Koch M, Robbins TW. Cortical, hippocampal, and striatal
mediation of schedule-induced behaviors. Behav Neurosci. 1990; 104:399–409. [PubMed:
2354035]

Mohanty A, Egner T, Monti JM, Mesulam MM. Search for a threatening target triggers limbic

guidance of spatial attention. J Neurosci. 2009; 29:10563–10572. [PubMed: 19710309]
Mohr F, Hubmann W, Cohen R, Bender W, Haslacher C, Honicke S, Schlenker R, Wahlheim C,

Werther P. Neurological soft signs in schizophrenia: assessment and correlates. Eur Arch
Psychiatry Clin Neurosci. 1996; 246:240–248. [PubMed: 8863002]

Montague PR, Dayan P, Sejnowski TJ. A framework for mesencephalic dopamine systems based on

predictive Hebbian learning. J Neurosci. 1996; 16:1936–1947. [PubMed: 8774460]

Moore JW, Wegner DM, Haggard P. Modulating the sense of agency with external cues. Conscious

Cogn. 2009

Moritz S, Woodward TS, Chen E. Investigation of metamemory dysfunctions in first-episode

schizophrenia. Schizophr Res. 2006; 81:247–252. [PubMed: 16256310]

Morris JS, deBonis M, Dolan RJ. Human amygdala responses to fearful eyes. Neuroimage. 2002;

17:214–222. [PubMed: 12482078]

Moussawi K, Pacchioni A, Moran M, Olive MF, Gass JT, Lavin A, Kalivas PW. N-Acetylcysteine

reverses cocaine-induced metaplasticity. Nat Neurosci. 2009; 12:182–189. [PubMed: 19136971]
Moutoussis M, Williams J, Dayan P, Bentall RP. Persecutory delusions and the conditioned avoidance

paradigm: towards an integration of the psychology and biology of paranoia. Cogn
Neuropsychiatry. 2007; 12:495–510. [PubMed: 17978936]

Murray GK, Corlett PR, Clark L, Pessiglione M, Blackwell AD, Honey G, Jones PB, Bullmore ET,

Robbins TW, Fletcher PC. Substantia nigra/ventral tegmental reward prediction error disruption
in psychosis. Mol Psychiatry. 2008; 13:239, 267–276. [PubMed: 17684497]

Nader K, Schafe GE, Le Doux JE. Fear memories require protein synthesis in the amygdala for

reconsolidation after retrieval. Nature. 2000; 406:722–726. [PubMed: 10963596]

Nagahama Y, Okina T, Suzuki N, Matsuda M. Neural correlates of psychotic symptoms in dementia

with Lewy bodies. Brain. 2009

Nagahama Y, Okina T, Suzuki N, Matsuda M, Fukao K, Murai T. Classification of psychotic

symptoms in dementia with Lewy bodies. Am J Geriatr Psychiatry. 2007; 15:961–967. [PubMed:
17974867]

Nelson A, Killcross S. Amphetamine exposure enhances habit formation. J Neurosci. 2006; 26:3805–

3812. [PubMed: 16597734]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 42

O’Donnell P. Dopamine gating of forebrain neural ensembles. Eur J Neurosci. 2003; 17:429–435.

[PubMed: 12581161]

Owen G, Harland R, Antonova E, Broome M. Jaspers’ concept of primary delusion. Br J Psychiatry.

2004; 185:77–78. [PubMed: 15231560]

Oye I, Paulsen O, Maurset A. Effects of ketamine on sensory perception: evidence for a role of N-

methyl-D-aspartate receptors. J Pharmacol Exp Ther. 1992; 260:1209–1213. [PubMed: 1312163]
Pally R. The predicting brain: unconscious repetition, conscious reflection and therapeutic change. Int

J Psychoanal. 2007; 88:861–881. [PubMed: 17681897]

Pan WX, Schmidt R, Wickens JR, Hyland BI. Tripartite mechanism of extinction suggested by

dopamine neuron activity and temporal difference model. J Neurosci. 2008; 28:9619–9631.
[PubMed: 18815248]

Parthasarathi UD, Harrower T, Tempest M, Hodges JR, Walsh C, McKenna PJ, Fletcher PC.

Psychiatric presentation of voltage-gated potassium channel antibody-associated encephalopathy.
Case report. Br J Psychiatry. 2006; 189:182–183. [PubMed: 16880491]

Passie T, Karst M, Borsutzky M, Wiese B, Emrich HM, Schneider U. Effects of different

subanaesthetic doses of (S)-ketamine on psychopathology and binocular depth inversion in man.
J Psychopharmacol. 2003; 17:51–56. [PubMed: 12680739]

Paton JJ, Belova MA, Morrison SE, Salzman CD. The primate amygdala represents the positive and
negative value of visual stimuli during learning. Nature. 2006; 439:865–870. [PubMed:
16482160]

Pearce JM, Hall G. A model for Pavlovian learning: variations in the effectiveness of conditioned but

not of unconditioned stimuli. Psychol Rev. 1980; 87:532–552. [PubMed: 7443916]

Peled A, Pressman A, Geva AB, Modai I. Somatosensory evoked potentials during a rubber-hand

illusion in schizophrenia. Schizophr Res. 2003; 64:157–163. [PubMed: 14613680]

Pennartz CM, McNaughton BL, Mulder AB. The glutamate hypothesis of reinforcement learning. Prog

Brain Res. 2000; 126:231–253. [PubMed: 11105650]

Pessiglione M, Seymour B, Flandin G, Dolan RJ, Frith CD. Dopamine-dependent prediction errors
underpin reward-seeking behaviour in humans. Nature. 2006; 442:1042–1045. [PubMed:
16929307]

Phillips WA, Silverstein SM. Convergence of biological and psychological perspectives on cognitive
coordination in schizophrenia. Behav Brain Sci. 2003; 26:65–82. discussion 82–137. [PubMed:
14598440]

Pomarol-Clotet E, Honey GD, Murray GK, Corlett PR, Absalom AR, Lee M, McKenna PJ, Bullmore
ET, Fletcher PC. Psychological effects of ketamine in healthy volunteers. Phenomenological
study. Br J Psychiatry. 2006; 189:173–179. [PubMed: 16880489]

Press C, Heyes C, Haggard P, Eimer M. Visuotactile learning and body representation: an ERP study

with rubber hands and rubber objects. J Cogn Neurosci. 2008; 20:312–323. [PubMed: 18275337]

Preuschoff K, Bossaerts P, Quartz SR. Neural differentiation of expected reward and risk in human

subcortical structures. Neuron. 2006; 51:381–390. [PubMed: 16880132]

Ramachandran, V.; Blakeslee, S. Phantoms in the Brain: Probing the mysteries of the human mind.

William Morrow; New York: 1998.

Rao RP, Ballard DH. Predictive coding in the visual cortex: a functional interpretation of some extra-

classical receptive-field effects. Nat Neurosci. 1999; 2:79–87. [PubMed: 10195184]

Ravina B, Marder K, Fernandez HH, Friedman JH, McDonald W, Murphy D, Aarsland D, Babcock D,
Cummings J, Endicott J, Factor S, Galpern W, Lees A, Marsh L, Stacy M, Gwinn-Hardy K,
Voon V, Goetz C. Diagnostic criteria for psychosis in Parkinson’s disease: report of an NINDS,
NIMH work group. Mov Disord. 2007; 22:1061–1068. [PubMed: 17266092]

Reading PJ, Dunnett SB, Robbins TW. Dissociable roles of the ventral, medial and lateral striatum on
the acquisition and performance of a complex visual stimulus-response habit. Behav Brain Res.
1991; 45:147–161. [PubMed: 1789923]

Redgrave P, Gurney K. The short-latency dopamine signal: a role in discovering novel actions? Nat

Rev Neurosci. 2006; 7:967–975. [PubMed: 17115078]

Redish AD. Addiction as a computational process gone awry. Science. 2004; 306:1944–1947.

[PubMed: 15591205]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 43

Rescorla, RA.; Wagner, AR. A theory of Pavlovian conditioning: Variations in the effectiveness of
reinforcement and non-reinforcement. In: Black, AH.; Prokasy, WF., editors. Classical
conditioning II: Current research and theory. Appleton-Century-Crofts; New York: 1972.
Ridler K, Veijola JM, Tanskanen P, Miettunen J, Chitnis X, Suckling J, Murray GK, Haapea M, Jones
PB, Isohanni MK, Bullmore ET. Fronto-cerebellar systems are associated with infant motor and
adult executive functions in healthy adults but not in schizophrenia. Proc Natl Acad Sci U S A.
2006; 103:15651–15656. [PubMed: 17028177]

Rizzolatti G, Fadiga L, Gallese V, Fogassi L. Premotor cortex and the recognition of motor actions.

Brain Res Cogn Brain Res. 1996; 3:131–141. [PubMed: 8713554]

Roiser JP, Stephan KE, den Ouden HE, Barnes TR, Friston KJ, Joyce EM. Do patients with

schizophrenia exhibit aberrant salience? Psychol Med. 2009; 39:199–209. [PubMed: 18588739]

Rolls ET. The representation of information about faces in the temporal and frontal lobes.

Neuropsychologia. 2007; 45:124–143. [PubMed: 16797609]

Rolls ET, Grabenhorst F. The orbitofrontal cortex and beyond: from affect to decision-making. Prog

Neurobiol. 2008; 86:216–244. [PubMed: 18824074]

Rolls ET, Grabenhorst F, Margot C, da Silva MA, Velazco MI. Selective attention to affective value
alters how the brain processes olfactory stimuli. J Cogn Neurosci. 2008; 20:1815–1826.
[PubMed: 18370603]

Romo R, Merchant H, Ruiz S, Crespo P, Zainos A. Neuronal activity of primate putamen during
categorical perception of somaesthetic stimuli. Neuroreport. 1995; 6:1013–1017. [PubMed:
7632884]

Ros H, Sachdev RN, Yu Y, Sestan N, McCormick DA. Neocortical networks entrain neuronal circuits

in cerebellar cortex. J Neurosci. 2009; 29:10309–10320. [PubMed: 19692605]

Rubin RD. Clinical use of retrograde amnesia produced by electroconvulsive shock. A conditioning

hypothesis. Can Psychiatr Assoc J. 1976; 21:87–90. [PubMed: 1277097]

Sanchez-Vives MV, McCormick DA. Cellular and network mechanisms of rhythmic recurrent activity

in neocortex. Nat Neurosci. 2000; 3:1027–1034. [PubMed: 11017176]

Sander D, Grafman J, Zalla T. The human amygdala: an evolved system for relevance detection. Rev

Neurosci. 2003; 14:303–316. [PubMed: 14640318]

Sarter M, Nelson CL, Bruno JP. Cortical cholinergic transmission and cortical information processing

in schizophrenia. Schizophr Bull. 2005; 31:117–138. [PubMed: 15888431]

Sass LA. Some Reflections on the (Analytic) Philosophical Approach to Delusion. Philosophy,

Psychiatry & Psychology. 2004; 11:71–80.

Scearce-Levie K, Roberson ED, Gerstein H, Cholfin JA, Mandiyan VS, Shah NM, Rubenstein JL,

Mucke L. Abnormal social behaviors in mice lacking Fgf17. Genes Brain Behav. 2008; 7:344–
354. [PubMed: 17908176]

Scharfetter C. On the hereditary aspects of symbiontic psychoses. A contribution towards the

understanding of the schizophrenia-like psychoses. Psychiatr Clin (Basel). 1970; 3:145–152.
[PubMed: 5422677]

Schiller D, Levy I, Niv Y, LeDoux JE, Phelps EA. From fear to safety and back: reversal of fear in the

human brain. J Neurosci. 2008; 28:11517–11525. [PubMed: 18987188]

Schlagenhauf F, Sterzer P, Schmack K, Ballmaier M, Rapp M, Wrase J, Juckel G, Gallinat J, Heinz A.
Reward feedback alterations in unmedicated schizophrenia patients: relevance for delusions. Biol
Psychiatry. 2009; 65:1032–1039. [PubMed: 19195646]

Schneider, K. Clinical Psychopathology. Grune & Stratton; New York: 1959.
Schnell K, Heekeren K, Daumann J, Schnell T, Schnitker R, Moller-Hartmann W, Gouzoulis-

Mayfrank E. Correlation of passivity symptoms and dysfunctional visuomotor action monitoring
in psychosis. Brain. 2008; 131:2783–2797. [PubMed: 18713781]

Schnider A. Spontaneous confabulation, reality monitoring, and the limbic system--a review. Brain

Res Brain Res Rev. 2001; 36:150–160. [PubMed: 11690611]

Schnider A. Spontaneous confabulation and the adaptation of thought to ongoing reality. Nat Rev

Neurosci. 2003; 4:662–671. [PubMed: 12894241]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 44

Schobel SA, Lewandowski NM, Corcoran CM, Moore H, Brown T, Malaspina D, Small SA.

Differential targeting of the CA1 subfield of the hippocampal formation by schizophrenia and
related psychotic disorders. Arch Gen Psychiatry. 2009; 66:938–946. [PubMed: 19736350]
Schultz W. Predictive reward signal of dopamine neurons. J Neurophysiol. 1998; 80:1–27. [PubMed:

9658025]

Schultz W, Apicella P, Ljungberg T. Responses of monkey dopamine neurons to reward and

conditioned stimuli during successive steps of learning a delayed response task. J Neurosci.
1993; 13:900–913. [PubMed: 8441015]

Schultz W, Dayan P, Montague PR. A neural substrate of prediction and reward. Science. 1997;

275:1593–1599. [PubMed: 9054347]

Schultz W, Dickinson A. Neuronal coding of prediction errors. Annu Rev Neurosci. 2000; 23:473–

500. [PubMed: 10845072]

Schultz W, Dickinson A. Neural coding of prediction errors. Annual Review of Neuroscience.

2000:473–500.

Seamans JK, Yang CR. The principal features and mechanisms of dopamine modulation in the

prefrontal cortex. Prog Neurobiol. 2004; 74:1–58. [PubMed: 15381316]

Seashore CE. Measurements of illusions and hallucinations in normal life. Studies from the Yale

Psychological Laboratory. 1895; 3:1–67.

Sesack SR, Grace AA. Cortico-Basal Ganglia reward network: microcircuitry.
Neuropsychopharmacology. 2010; 35:27–47. [PubMed: 19675534]

Shaner A. Delusions, superstitious conditioning and chaotic dopamine neurodynamics. Med

Hypotheses. 1999; 52:119–123. [PubMed: 10340292]

Shanks DR. Learning: from association to cognition. Annu Rev Psychol. 2010; 61:273–301. [PubMed:

19575617]

Sharp FR, Tomitaka M, Bernaudin M, Tomitaka S. Psychosis: pathological activation of limbic

thalamocortical circuits by psychomimetics and schizophrenia? Trends Neurosci. 2001; 24:330–
334. [PubMed: 11356504]

Shepard PD, Holcomb HH, Gold JM. Schizophrenia in translation: the presence of absence: habenular

regulation of dopamine neurons and the encoding of negative outcomes. Schizophr Bull. 2006;
32:417–421. [PubMed: 16717257]

Sherman SM, Guillery RW. On the actions that one nerve cell can have on another: distinguishing
“drivers” from “modulators”. Proc Natl Acad Sci U S A. 1998; 95:7121–7126. [PubMed:
9618549]

Siegel RK. Cocaine hallucinations. Am J Psychiatry. 1978; 135:309–314. [PubMed: 626219]
Sillitoe RV, Stephen D, Lao Z, Joyner AL. Engrailed homeobox genes determine the organization of

Purkinje cell sagittal stripe gene expression in the adult cerebellum. J Neurosci. 2008; 28:12150–
12162. [PubMed: 19020009]

Silverstein S, Uhlhaas PJ, Essex B, Halpin S, Schall U, Carr V. Perceptual organization in first episode

schizophrenia and ultra-high-risk states. Schizophr Res. 2006; 83:41–52. [PubMed: 16497484]
Simons JS, Henson RN, Gilbert SJ, Fletcher PC. Separable forms of reality monitoring supported by

anterior prefrontal cortex. J Cogn Neurosci. 2008; 20:447–457. [PubMed: 18004946]
Simpson J, Done DJ. Elasticity and confabulation in schizophrenic delusions. Psychol Med. 2002;

32:451–458. [PubMed: 11989990]

Sirota A, Montgomery S, Fujisawa S, Isomura Y, Zugaro M, Buzsaki G. Entrainment of neocortical
neurons and gamma oscillations by the hippocampal theta rhythm. Neuron. 2008; 60:683–697.
[PubMed: 19038224]

Skinner BF. Superstition” in the pigeon. Journal of Experimental Psychology. 1948; 38:168–172.

[PubMed: 18913665]

Sokolov, EN. Neuronal models and the orienting reflex. Josiah Macy Jr Foundation; New York: 1960.
Soltani A, Wang XJ. Synaptic computation underlying probabilistic inference. Nat Neurosci. 2010;

13:112–119. [PubMed: 20010823]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 45

Spence SA, Brooks DJ, Hirsch SR, Liddle PF, Meehan J, Grasby PM. A PET study of voluntary
movement in schizophrenic patients experiencing passivity phenomena (delusions of alien
control). Brain. 1997; 120 ( Pt 11):1997–2011. [PubMed: 9397017]

Sperry, RW. Forebrain Commisurectomy and consciuos awareness. In: Trevarthen, C., editor. Brain

Circuits and the Mind. Cambridge University Press; New York: 1990.

Spitzer M. A neurocomputational approach to delusions. Compr Psychiatry. 1995; 36:83–105.

[PubMed: 7758303]

Spitzer, M.; Walter, H. The cognitive neuroscience of agency in schizophrenia. In: David, A.; Kircher,
T., editors. The self in neuroscience and psychiatry. Cambridge University Press; Cambridge:
2003. p. 436-444.

Startup M, Startup S. On two kinds of delusion of reference. Psychiatry Res. 2005; 137:87–92.

[PubMed: 16226316]

Stephan KE, Baldeweg T, Friston KJ. Synaptic plasticity and dysconnection in schizophrenia. Biol

Psychiatry. 2006; 59:929–939. [PubMed: 16427028]

Steriade M, Dossi RC, Pare D, Oakson G. Fast oscillations (20–40 Hz) in thalamocortical systems and
their potentiation by mesopontine cholinergic nuclei in the cat. Proc Natl Acad Sci U S A. 1991;
88:4396–4400. [PubMed: 2034679]

Stickgold R, Walker MP. Sleep-dependent memory consolidation and reconsolidation. Sleep Med.

2007; 8:331–343. [PubMed: 17470412]

Sur M, Rubenstein JL. Patterning and plasticity of the cerebral cortex. Science. 2005; 310:805–810.

[PubMed: 16272112]

Sutton, RS.; Barto, AG. Reinforcement Learning: An Introduction. MIT Press; 1998.
Svenningsson P, Tzavara ET, Carruthers R, Rachleff I, Wattler S, Nehls M, McKinzie DL, Fienberg

AA, Nomikos GG, Greengard P. Diverse psychotomimetics act through a common signaling
pathway. Science. 2003; 302:1412–1415. [PubMed: 14631045]

Tabares-Seisdedos R, Rubenstein JL. Chromosome 8p as a potential hub for developmental

neuropsychiatric disorders: implications for schizophrenia, autism and cancer. Mol Psychiatry.
2009; 14:563–589. [PubMed: 19204725]

Takahashi Y, Schoenbaum G, Niv Y. Silencing the critics: understanding the effects of cocaine

sensitization on dorsolateral and ventral striatum in the context of an actor/critic model. Front
Neurosci. 2008; 2:86–99. [PubMed: 18982111]

Takahashi YK, Roesch MR, Stalnaker TA, Haney RZ, Calu DJ, Taylor AR, Burke KA, Schoenbaum

G. The orbitofrontal cortex and ventral tegmental area are necessary for learning from
unexpected outcomes. Neuron. 2009; 62:269–280. [PubMed: 19409271]

Tang C, Pawlak AP, Prokopenko V, West MO. Changes in activity of the striatum during formation of

a motor habit. Eur J Neurosci. 2007; 25:1212–1227. [PubMed: 17331217]

Teufel C, Alexis DM, Todd H, Lawrance-Owen AJ, Clayton NS, Davis G. Social cognition modulates
the sensory coding of observed gaze direction. Curr Biol. 2009; 19:1274–1277. [PubMed:
19559619]

Thiebierge G. Les acaraphobes. Annales de Dermatologie et de Syphiligraphie. 1894; 3:730–736.
Thorndike, EL. Animal Intelligence. MacMillan; New York: 1911.
Tole S, Remedios R, Saha B, Stoykova A. Selective requirement of Pax6, but not Emx2, in the

specification and development of several nuclei of the amygdaloid complex. J Neurosci. 2005;
25:2753–2760. [PubMed: 15758185]

Tolman, EC. Purposive behaviour in animals and men. Century; New York: 1932.
Tricomi E, Balleine BW, O’Doherty JP. A specific role for posterior dorsolateral striatum in human

habit learning. Eur J Neurosci. 2009; 29:2225–2232. [PubMed: 19490086]

Tsakiris M, Haggard P. The rubber hand illusion revisited: visuotactile integration and self-attribution.

J Exp Psychol Hum Percept Perform. 2005; 31:80–91. [PubMed: 15709864]

Turner DC, Aitken MR, Shanks DR, Sahakian BJ, Robbins TW, Schwarzbauer C, Fletcher PC. The

role of the lateral frontal cortex in causal associative learning: exploring preventative and super-
learning. Cereb Cortex. 2004; 14:872–880. [PubMed: 15054060]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Corlett et al.

Page 46

Uhlhaas PJ, Haenschel C, Nikolic D, Singer W. The role of oscillations and synchrony in cortical

networks and their putative relevance for the pathophysiology of schizophrenia. Schizophr Bull.
2008; 34:927–943. [PubMed: 18562344]

Uhlhaas PJ, Linden DE, Singer W, Haenschel C, Lindner M, Maurer K, Rodriguez E. Dysfunctional

long-range coordination of neural activity during Gestalt perception in schizophrenia. J Neurosci.
2006a; 26:8168–8175. [PubMed: 16885230]

Uhlhaas PJ, Mishara AL. Perceptual anomalies in schizophrenia: integrating phenomenology and

cognitive neuroscience. Schizophr Bull. 2007; 33:142–156. [PubMed: 17118973]
Uhlhaas PJ, Phillips WA, Mitchell G, Silverstein SM. Perceptual grouping in disorganized

schizophrenia. Psychiatry Res. 2006b; 145:105–117. [PubMed: 17081620]

Uhlhaas PJ, Singer W. Abnormal neural oscillations and synchrony in schizophrenia. Nat Rev

Neurosci. 11:100–113. [PubMed: 20087360]

Vallar G, Ronchi R. Somatoparaphrenia: a body delusion. A review of the neuropsychological

literature. Exp Brain Res. 2009; 192:533–551. [PubMed: 18813916]

van Nimwegen L, de Haan L, van Beveren N, van den Brink W, Linszen D. Adolescence,

schizophrenia and drug abuse: a window of vulnerability. Acta Psychiatr Scand Suppl. 2005:35–
42. [PubMed: 15877720]

Vernon D, Haenschel C, Dwivedi P, Gruzelier J. Slow habituation of induced gamma and beta

oscillations in association with unreality experiences in schizotypy. Int J Psychophysiol. 2005;
56:15–24. [PubMed: 15725486]

Vickery TJ, Jiang YV. Associative grouping: perceptual grouping of shapes by association. Atten

Percept Psychophys. 2009; 71:896–909. [PubMed: 19429967]

Vinogradov S, King RJ, Huberman BA. An associationist model of the paranoid process: application

of phase transitions in spreading activation networks. Psychiatry. 1992; 55:79–94. [PubMed:
1557472]

Von Holst E. Relations between the central nervous system and the peripheral organs. British Journal

of Animal Behaviour. 1954; 2:89–94.

Waelti P, Dickinson A, Schultz W. Dopamine responses comply with basic assumptions of formal

learning theory. Nature. 2001; 412:43–48. [PubMed: 11452299]

Waldmann, MR.; Martignon, L. A Bayesian network model of causal learning. In: Gernsbacher, MA.;

Derry, SJ., editors. Proceedings of the Twentieth Annual Conference of the Cognitive Science
Society. Mahwah, NJ: Earlbaum; 1998. p. 1102-1107.

Wallis GG. A case of hallucinosis due to cocaine. J R Nav Med Serv. 1949; 35:112. [PubMed:

18127069]

Walsh T, McClellan JM, McCarthy SE, Addington AM, Pierce SB, Cooper GM, Nord AS, Kusenda
M, Malhotra D, Bhandari A, Stray SM, Rippey CF, Roccanova P, Makarov V, Lakshmi B,
Findling RL, Sikich L, Stromberg T, Merriman B, Gogtay N, Butler P, Eckstrand K, Noory L,
Gochman P, Long R, Chen Z, Davis S, Baker C, Eichler EE, Meltzer PS, Nelson SF, Singleton
AB, Lee MK, Rapoport JL, King MC, Sebat J. Rare structural variants disrupt multiple genes in
neurodevelopmental pathways in schizophrenia. Science. 2008; 320:539–543. [PubMed:
18369103]

Waltz JA, Frank MJ, Robinson BM, Gold JM. Selective reinforcement learning deficits in

schizophrenia support predictions from computational models of striatal-cortical dysfunction.
Biol Psychiatry. 2007; 62:756–764. [PubMed: 17300757]

Wang J, O’Donnell P. D(1) dopamine receptors potentiate nmda-mediated excitability increase in layer
V prefrontal cortical pyramidal neurons. Cereb Cortex. 2001; 11:452–462. [PubMed: 11313297]

Wang XJ. Neurophysiological and Computational Principles of Cortical Rhythms in Cognition.

Physiological Reviews. (In Press).

Wegner DM. Precis of the illusion of conscious will. Behav Brain Sci. 2004; 27:649–659. discussion

659–692. [PubMed: 15895616]

Weiller C, Juptner M, Fellows S, Rijntjes M, Leonhardt G, Kiebel S, Muller S, Diener HC, Thilmann
AF. Brain representation of active and passive movements. Neuroimage. 1996; 4:105–110.
[PubMed: 9345502]

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
Corlett et al.

Page 47

Weiskrantz L, Elliott J, Darlington C. Preliminary observations on tickling oneself. Nature. 1971;

230:598–599. [PubMed: 4928671]

Whalen PJ, Rauch SL, Etcoff NL, McInerney SC, Lee MB, Jenike MA. Masked presentations of

emotional facial expressions modulate amygdala activity without explicit knowledge. J Neurosci.
1998; 18:411–418. [PubMed: 9412517]

Whalen PJ, Shin LM, McInerney SC, Fischer H, Wright CI, Rauch SL. A functional MRI study of

human amygdala responses to facial expressions of fear versus anger. Emotion. 2001; 1:70–83.
[PubMed: 12894812]

Whitson JA, Galinsky AD. Lacking control increases illusory pattern perception. Science. 2008;

322:115–117. [PubMed: 18832647]

Winterer G. Cortical microcircuits in schizophrenia--the dopamine hypothesis revisited.

Pharmacopsychiatry. 2006; 39(Suppl 1):S68–71. [PubMed: 16508900]

Wolff G, McKenzie K. Capgras, Fregoli and Cotard’s syndromes and Koro in folie a deux. Br J

Psychiatry. 1994; 165:842. [PubMed: 7881797]

Wolpert DM, Ghahramani Z, Jordan MI. An internal model for sensorimotor integration. Science.

1995; 269:1880–1882. [PubMed: 7569931]

Wolpert DM, Miall RC. Forward Models for Physiological Motor Control. Neural Netw. 1996;

9:1265–1279. [PubMed: 12662535]

Woodward TS, Moritz S, Chen EY. The contribution of a cognitive bias against disconfirmatory
evidence (BADE) to delusions: a study in an Asian sample with first episode schizophrenia
spectrum disorders. Schizophr Res. 2006; 83:297–298. [PubMed: 16513331]

Yin HH, Knowlton BJ, Balleine BW. Lesions of dorsolateral striatum preserve outcome expectancy
but disrupt habit formation in instrumental learning. Eur J Neurosci. 2004; 19:181–189.
[PubMed: 14750976]

Yoo SS, Freeman DK, McCarthy JJ 3rd, Jolesz FA. Neural substrates of tactile imagery: a functional

MRI study. Neuroreport. 2003; 14:581–585. [PubMed: 12657890]

Young AW, Robertson IH, Hellawell DJ, de Pauw KW, Pentland B. Cotard delusion after brain injury.

Psychol Med. 1992; 22:799–804. [PubMed: 1410102]

Young G. Capgras delusion: an interactionist model. Conscious Cogn. 2008; 17:863–876. [PubMed:

18314350]

Yu AJ, Dayan P. Uncertainty, neuromodulation, and attention. Neuron. 2005; 46:681–692. [PubMed:

15944135]

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
Corlett et al.

Page 48

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Figure 1. Neural Instantiation of predictive learning and belief
Theoretical model: Schematic of reward prediction error signals before learning, following
learning and during extinction
Health: Right DLPFC prediction error response during casual learning in healthy subjects
(Corlett et al, 2004) – V: Violation of expectancy, C: Confirmation of expectancy
Disease: Aberrant right frontal prediction error response in patients with first episode
psychosis. The more profound the disruption, the more severe the delusions (Corlett et al,
2007b) - C: Controls, P: Patients with Psychosis

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
Corlett et al.

Page 49

Figure 2. Learning Memory and Belief Alter Perception
Theoretical model: Feedforward and feedback thalamocortical projections (adapted from
http://wiki.tkk.fi/display/SYNB/Neocortex).
Health: The rotating hollow mask is continuously perceived as convex due to our consistent
experience of faces as convex.
Disease: Individuals prone to or experiencing psychosis report the hollow mask as a hollow
percept (Emrich et al, 1988).

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
Corlett et al.

Page 50

Figure 3. Neural Circuitry of Goal Directedness (knowledge) and habit (belief)
With repetition, rumination and reconsolidation, the control of behavior shifts from flexible
goal-directed ventral cortcostriatal control toward control by the inflexible dorsal striatum
and motor cortex.

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.

 
 
 
 
 
 
Corlett et al.

Page 51

Figure 4. Putative Delusion Circuits
Salience/Reference: A circuit incorporating the midbrain dopaminergic nuclei, the
associative striatum and frontal cortex. Aberrant prediction errors in midbrain update
expectancies in the frontal cortex leading to aberrantly salient percepts.
Agency/others: The midbrain, PFC, Parietal cortex and cerebellum as well as the bimodal
cells of the putamen. This circuit describes forward model predictions used to discern
whether sensory stimulation was internally of externally generated. A breakdown in this
predictive mechanism would manifest as hallucinatory tactile percepts and inferences of
external control of intentional action.
Fear/Paranoia: A circuit incorporating the midbrain, amygdala, frontal and parietal
cortices. Here, neutral or irelevent stimuli, thoughts and percepts come to engender fear and
anxiety. A dysfunction in frontoparietal circuitry engenders inappropriate social predictions
and maladaptive inferences about the intentions of others.
Interaction between circuits: These circuits interact and likely mutually reinforce one
another.

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

I

-

N
H
P
A
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Prog Neurobiol. Author manuscript; available in PMC 2013 June 09.
