# Montague_2012_Computational psychiatry.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

NIH Public Access
Author Manuscript
Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

Published in final edited form as:

Trends Cogn Sci. 2012 January ; 16(1): 72–80. doi:10.1016/j.tics.2011.11.018.

Computational psychiatry

P. Read Montague1,2, Raymond J. Dolan2, Karl J. Friston2, and Peter Dayan3
1Virginia Tech Carilion Research Institute and Department of Physics, Virginia Tech, 2 Riverside
Circle, Roanoke, VA 24016, USA

2Wellcome Trust Centre for Neuroimaging, University College London, 12 Queen Square,
London, WC1N 3BG, UK

3Gatsby Computational Neuroscience Unit, Alexandra House, 17 Queen Square, London, WC1N
3AR, UK

Abstract

Computational ideas pervade many areas of science and have an integrative explanatory role in
neuroscience and cognitive science. However, computational depictions of cognitive function
have had surprisingly little impact on the way we assess mental illness because diseases of the
mind have not been systematically conceptualized in computational terms. Here, we outline goals
and nascent efforts in the new field of computational psychiatry, which seeks to characterize
mental dysfunction in terms of aberrant computations over multiple scales. We highlight early
efforts in this area that employ reinforcement learning and game theoretic frameworks to elucidate
decision-making in health and disease. Looking forwards, we emphasize a need for theory
development and large-scale computational phenotyping in human subjects.

The explanatory gap

The idea of biological psychiatry seems simple and compelling: the brain is the organ that
generates, sustains and supports mental function, and modern psychiatry seeks the biological
basis of mental illnesses. This approach has been a primary driver behind the development
of generations of anti-psychotic, anti-depressant, and anti-anxiety drugs that enjoy
widespread clinical use. Despite this progress, biological psychiatry and neuroscience face
an enormous explanatory gap. This gap represents a lack of appropriate intermediate levels
of description that bind ideas articulated at the molecular level to those expressed at the level
of descriptive clinical entities, such as schizophrenia, depression and anxiety. In general, we
lack a sufficient understanding of human cognition (and cognitive phenotypes) to provide a
bridge between the molecular and the phenomenological. This is reflected in questions and
concerns regarding the classification of psychiatric diseases themselves, notably, each time
the Diagnostic and Statistical Manual of Mental Disorders (DSM) of the American
Psychiatric Association is revised [1].

While multiple causes are likely to account for the current state of affairs, one contributor to
this gap is the (almost) unreasonable effectiveness of psychotropic medication. These
medications are of great benefit to a substantial number of patients; however, our
understanding of why they work on mental function remains rudimentary. For example,
receptors are understood as molecular motifs (encoded by genes) that shuttle information
from one cellular site to another. Receptor ligands, whose blockade or activation relieves

© 2011 Elsevier Ltd. All rights reserved.
Corresponding author: Montague, P.R. (read@vt.edu).

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 2

psychiatric symptoms, furnished a kind of conceptual leap that seemed to obviate the need to
account for the numerous layers of representation intervening between receptor function and
behavioral change. This, in turn, spawned explanations of mental phenomena in simplistic
terms that invoked a direct mapping from receptor activation to complex changes in mental
status. We are all participants in this state of affairs, since symptom relief in severe mental
disease is sufficient from a clinical perspective, irrespective of whether there are models that
connect underlying biological phenomena to the damaged mental function. A medication
that relieves or removes symptoms in a large population of subjects is unquestionably of
great utility, even if the explanation for why it works is lacking. However, significant gaps
in the effectiveness of medications for different mental illness mean we should look to
advances in modern neuroscience and cognitive science to deliver more.

We believe that advances in human neuroscience can bridge parts of the explanatory gap.
One area where there has been substantial progress is in the field of decision-making.
Aberrant decision-making is central to the majority of psychiatric conditions and this
provides a unique opportunity for progress. It is the computational revolution in cognitive
neuroscience that underpins this opportunity and argues strongly for the application of
computational approaches to psychiatry. This is the basis of computational psychiatry [2–4]
(Figure 1). In this article, we consider this emerging field and outline central challenges for
the immediate future.

Contrasting mathematical and computational modeling

Mathematical modeling

To define computational modeling, we must first distinguish it from its close cousin,
mathematical or biophysical modeling. Mathematical modeling provides a quantitative
expression for natural phenomena. This may involve building multi-level (unifying)
reductive accounts of natural phenomena. The reductions involve explanatory models at one
level of description that are based on models at finer levels, and are ubiquitous in everything
from treatments of action potentials [5] (see also [6] for a broader view) to the dynamical
activity of populations of recurrently connected neurons [7]. Biophysical realism, however,
is a harsh taskmaster, particularly in the face of incomplete or sparse data. For example, in
humans, there seems to be little point in building a biophysically detailed model of the
dendrite of single neurons if one can only measure synaptic responses averaged over
millions of neurons and billions of synapses using functional magnetic resonance imaging
(fMRI) or electroencephalography (EEG).

Biophysical modeling is important for elucidating key relationships in a hugely complex
system [8] and thus predicting the possible effects of therapeutic interventions (see [9] for an
example using dynamic causal modeling). For example, it is well known that critical
mechanisms within neuromodulatory systems, such as dopamine, serotonin, norepinephrine
and acetylcholine, are subject to intricate patterns of feedback and interactive control, with
autoreceptors regulating the activity of the very neurons that release neuromodulators.
Moreover, this feedback often includes the effects of one neuromodulator (e.g., serotonin)
on the release and impact of others (e.g., dopamine) [10]. These neuromodulators are
implicated in many psychiatric and neurological conditions. The fact that they play key roles
in so many critical functions may explain the fact, if not the nature, of this exquisite
regulation. It is the complexity of these interactions that invites biophysical modeling and
simulation, for instance, to predict the effect of medication with known effects on receptors
or uptake mechanisms. Moreover, the capacity to perform fast biophysical simulations is
essential for evidence-based model comparison using empirical data [11] and the exploration
of emergent behaviors (e.g., [12]). Simulation has become vital to vast areas of science and
it will be central in computational psychiatry. Mathematical predictions based on real neural

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 3

and biophysical data are important; however, they are not equivalent to a computational
account of mental or neural function.

Computational modeling

Computational modeling seeks normative computational accounts of neural and cognitive
function. Such accounts start from the premise that the brain solves computational problems
and indeed has evolved to do so. One of the pioneers of computing theory, Alan Turing,
conceived of mental function in exactly this fashion – the mind was cast as specific patterns
of information processing supported by a particular kind of hardware (the brain) [13]. This
notion implies key constraints on mental phenomena – in particular constraints on
computational complexity that limit the power of any device, neural or mechanical, to solve
a wide range of problems [14]. This idea is commonplace today but in the 1930s the idea of
computation and its limits underwent a revolution [15–17] (see also [18]).

Currently, computational accounts of elements of mental and neural function exist, and in
each case, typically some constraint is found that guides the discovery of the computational
model. Some of the most important constraints come from optimality assumptions – the idea
that the brain is organized to maximize or minimize quantities of external and internal
importance (e.g., [6,19]). One set of optimality constraints emerges naturally from behaviors
that support survival, such as foraging for food or responding appropriately to prospects of
danger [20]. A wide range of ideas, proofs, methods and algorithms for executing such
behaviors can be found in many fields, including engineering, economics, operations
research, control theory, statistics, artificial intelligence and computer science. In fact, these
fields provide a formal foundation for the interpretation of many cognitive and neural
phenomena [6]. This foundation can span important levels of description, for instance,
offering accounts of the representational semantics of the population activity of neurons [21]
or of the firing of neuromodulatory neurons in the context of tasks involving predictions of
reward [22–26]. This type of computational modeling can thus provide one explanatory
framework for the reductive mathematical modeling discussed above.

Computational modeling in decision-making

The field of decision-making has been a particular target for computational modeling.
Decision-making involves the accumulation of evidence associated with the utilities of
possible options and then the choice of one of them, given the evidence. Decision-making
problems in natural environments are extremely complex. One difficulty arises from the
balance models must strike between built-in information acquired over the course of
evolution about the nature of the decision-making environment (ultimate constraints) versus
what can be learned over the course of moment-to-moment experience (proximate
constraints). A second difficulty arises because of the inherent computational complexity of
the problem: certain types of optimal decision-making appear intractable for any
computational system. This fact motivates the search for approximations that underlie
mechanisms actually used in animals. Reinforcement learning is one area where such
approximations have been used to guide the discovery of neural and behavioral mechanisms.
Box 1 provides a brief description of the modern view of neural reinforcement learning.

Many psychiatric conditions are associated not only with abnormal subjective states, such as
moods, but also with aberrant decisions. Patients make choices: in depression, not to
explore; in obsessive compulsive disorder, to repeat endlessly a behavior (such as hand-
washing) that has no apparent basis in rational fact (such as having dirty hands); in
addiction, to seek and take a drug, despite explicitly acknowledging the damage that
follows. Key to the initial form of computational psychiatry is the premise that, if the
psychology and neurobiology of normative decision-making can be characterized and

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 4

parameterized via a multi-level computational framework, it will be possible to understand
the many ways in which decision-making can go wrong. However, we should first consider
an important earlier tradition of modeling in psychiatry.

Early connectionist models of mental dysfunction

There is an old idea in brain science, namely, that complex functions emerge from
networked interactions of relatively simple parts [27,28]. In the brain, the most conspicuous
physical substrates for this idea are the networks of neurons connected by synapses. This
perspective has been termed ‘connectionism’. One modern expression of connectionism
began with the work of Rumelhart, McClelland and the parallel distributed processing
research group [29] (but now see [30]), which applied this approach to both brain and
cognition in the early and mid-1980s, building upon the earlier pioneering work [27,28]. The
basic concept underlying connectionism involves taking simple, neuron-like, units and
connecting in them in ways that are either biologically plausible based on brain data or
capable of performing important cognitive or behavioral functions. At approximately the
same time and parallel to this work, three key publications emerged from physicists John
Hopfield and David Tank, which showed how a connectionist-like network can have
properties equivalent to those pertaining to the dynamics of a physical system [31–33].
Inspired by Hopfield’s work and the seminal (and still classic) work of Stuart and Donald
Geman on Gibbs sampling and Bayesian approaches to image analysis, Hinton and
Sejnowski [34] showed that probabilistic activation in simple units could perform a
sophisticated Bayesian style of inference. Collectively, this work addressed memory states,
constraint satisfaction, pattern recognition and a host of other cognitive functions [29], thus
suggesting that these models might aid in understanding mental disease.

Through the 1990s, connectionist models turned their sights on psychopathologies, such as
schizophrenia [35–39]. These models primarily addressed issues related to cognitive control
and neuromodulation [35–38], with a particular focus on neural systems that could support
these functions [40–44]. These and other models offered plausible solutions for how
networks of neurons could implement functions, such as cognitive control and memory, and
offered new abstractions for how such functions go awry in specific pathologies. This work
leans heavily on the neurally-plausible aspect of connectionist models, a feature that now
finds more biological support, as neuroscience has produced enormous amounts of new data
that can be fit into such frameworks [42–44].

Recent efforts toward computational characterization of mental

dysfunction

In this section, we review recent efforts to develop and test computational models of mental
dysfunction and to extract behavioral phenotypes relevant for building computationally-
principled models of mental disease. The examples discussed are intended to provide
insights into healthy mental function but in a fashion designed to inform the diagnosis and
treatment of mental disease. Along with the pioneering earlier studies [35–40], there have
been recent treatments and reports of work along these lines on schizophrenia [3,45,46],
addiction [47], Parkinson’s disease, Tourette’s syndrome, and attention-deficit hyperactivity
disorder [3]. Here, we concentrate on two areas that have not been recently reviewed in this
context, namely depression and autism.

The efforts discussed here are now collectively blossoming into programmatic efforts in
computational psychiatry (for example, the joint initiative of the Max Planck Society and
University College London: Computational Psychiatry and Aging Research). It is our
opinion that such efforts must reach further and strive to extract normative computational

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 5

accounts of healthy and pathological cognition useful for building predictive models of
individuals. Consequently, we emphasize for computational psychiatry the goal of extracting
computational principles around which human cognition and its supporting biological
apparatus is organized. Achieving this goal will require new types of phenotyping
approaches, in which computational parameters are estimated (neurally and behaviorally)
from human subjects and used to inform the models. This type of large-scale computational
phenotyping of human behavior does not yet exist.

Reinforcement learning (RL) models of mood disorders and anxiety

Box 1 notes three different, albeit interacting, control systems within the context of RL:
model-based, model-free, and Pavlovian. Model-based and model-free systems link the
choice of actions directly to affective consequences. The Pavlovian system determines
involuntary actions on the basis of predictions of outcomes, whether or not deployed actions
are actually appropriate for gaining or avoiding those outcomes. Pavlovian control appears
completely automated in this description. However, it is known that other brain systems can
interact with Pavlovian control, hence, it is at this level that such control can be sensitive to
ongoing valuations in other parts of the brain.

These types of controllers and their interactions have been the subject of computational
modeling in the context of mood disorders, especially depression [4,48–50]. First, let us
consider the role of serotonin in clinical depression. In many patients, one effective
treatment involves the use of a selective serotonin reuptake inhibitor (SSRI), which prolongs
the action of serotonin at target sites. Data from animals suggests that serotonin release is
involved in (learned) behavioral inhibition [50–53], associated with the prediction of
aversive outcomes [54,55]. Computational modeling inspired by these data suggests that
serotonin’s role in behavioral inhibition may reflect a Pavlovian effect: subjects do not have
to learn explicitly what (not) to do in the face of possible future trouble. This effect could be
called the ‘serotonergic crutch’. Problems with the operation of this crutch can lead to
behavior in which poor choices are made because they have not been learned to be
inappropriate. In this framework, punishments are experienced or imagined even if the
choices concern internal trains of thought rather than external events [50]. Restoration of the
crutch is considered to improve matters again. The logic here is that the more an individual’s
behavior is determined in a Pavlovian manner, the more devastating is the likely
consequence of any problem with the serotonergic crutch. This is an account of vulnerability
(analogous to the incentive sensitization theory of drug addiction; see [56–58]).

Conversely, model-based RL has been used to capture another feature of some forms of
anxiety and depression: learned helplessness [59–61]. Animals can be made helpless when
provided with uncontrollable rewards as well as uncontrollable punishments [62] and, thus,
learning that their actions do not consistently predict outcomes. In these experiments, one
way to demonstrate the onset of learned helplessness is to show that the animals do not
explore or try to escape when placed in new environments (e.g. [63]).

A natural computational account is to treat the helplessness training in the first part of
learned helplessness as inducing a prior probability distribution over possible future
environments, indicating that the animal can expect to have little influence over its fate, that
is, little controllability. This hypothesis is based on the expectation that related environments
have similar properties. Exploration in a new environment is only worthwhile only if it is
expected that good outcomes can be reliably achieved given appropriate actions. Thus, a
prior belief implying that the environment is unlikely to afford substantial controllability
will discourage exploration. Prior distributions are under active examination in Bayesian
approaches to cognitive science and are offering substantial explanations for a broad range
of developmental and adult behaviors [64]. Only model-based RL is capable of

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 6

incorporating such rich priors, even though model-free control can be induced to behave in
similar ways by simpler mechanisms [65,66]. This computational interpretation of
uncontrollability provides a new way to understand the role that environments can play in
etiology. It also provides a way of formalizing the complex interaction between model-
based, model-free and Pavlovian systems, when not only might one controller directly
influence the training signal of the other controllers [67] but also the very experience other
controllers require in order to learn their own predictions or courses of action.

Using games to phenotype autism spectrum disorder

A defining feature of human cognition is the capacity to model and understand the intentions
(and emotions) of other humans. This extends to an ability to forecast into the near-term
future, for example, how someone else will feel should they experience a consequence of an
action that we might take. Sophisticated capacities such as these lie at the heart of our ability
to cooperate, compete and communicate with others. One of the defining features of autism
spectrum disorder (ASD) is a diminished capacity for socio-emotional reciprocity – the
social back-and-forth engagement associated with all human interaction [1,68–70]. Recent
modeling and neuroimaging work has used two-agent interactions, typically in the form of
some game, to parameterize and probe this social give-and-take [71–81]. This work, along
with other efforts [82–85], has collectively launched a computational neuroscience
perspective on inter-personal exchange – a first step toward identifying computational
phenotypes in human interactions that are underwritten by both behavioral and neural
responses.

Game theory is the study of mathematical models of interacting rational agents. It is used in
many domains and in recent years has been increasingly applied to common behavioral
interactions in humans. Two game-theoretic approaches have recently been used to probe
ASD and other psychopathological populations directly: the stag hunt game and the multi-
round trust game (Figure 2). Although the behavioral probes are different, the two games
share the feature that it is advantageous for a human player to make inferences about their
partner’s likely mental state during the game. These inferences are recursive: my model of
you incorporates my model of your model of me, and so on. Both approaches have built
computational models around this central idea of recursion [78,79], thereby furnishing
component computations required for healthy human exchange.

Yoshida et al. [79–81] used the stag hunt game (Figure 2a) to probe mental state inferences
in ASD versus control subjects. The stag hunt game is a classic two-player game (in this
case involving a human player and a computer agent), where players can cooperate to hunt
and acquire high yield stags, or act alone and hunt low yield rabbits. The model developed
by Yoshida et al. [79] used the human player’s observed behavior to estimate the
sophistication level (depth of recursion) of their inference about the computer agent’s beliefs
(theory of mind). This estimate is necessary if the human player is to cooperate successfully
with the computer agent – the human must believe that the agent believes that the human
will also cooperate, and so on.

Behavioral results that exploited this model pointed to a higher probability for a theory-of-
mind model (versus fixed-strategy) for control subjects. The opposite was true for ASD
subjects (~78% probability for fixed-strategy). However, as one might expect, there was
heterogeneity in these estimates, with some ASD subjects (n=5) displaying higher
probability for the theory-of-mind model compared to a fixed-strategy model (n=12).
Intriguingly, ASD subjects with a higher probability for a fixed-strategy model showed
higher ratings on two ASD rating scales (ADI-R, ASDI). These results are preliminary and
the sample of ASD subjects small. However, the crucial point is that the model allows for a
principled parameterization of important cognitive components (e.g., depth of recursion in

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 7

modeling one’s partner). The use of such a model provides a way to formalize the cognitive
components of ASD in computational terms. By collecting much more normative data, this
type of approach could serve to differentiate ASD along these newly defined computational
dimensions to improve diagnosis, guide other modes of investigation and help tailor
treatments.

The multi-round trust game has also been used to probe a range of psychopathologic
populations including ASD and borderline personality disorder [2,75,77]. The game is a
sequential fairness game involving reciprocation, where performance is determined by
whether players think through the impact of their actions on their partner. In the game, a
proposer (called the investor) is endowed with $20 and chooses to send some fraction I to
their partner. This fraction is tripled (to 3*I) on the way to the responder (called the trustee),
who then chooses to send back some fraction of the tripled amount. Subjects play 10 rounds
and know this beforehand. Cooperation earns both players the most money. Even when
playing with an anonymous partner, investors do send money, a fact that challenges rational
agent accounts of such exchanges. One way to conceptualize this willingness to send money
was proposed by Fehr and Schmidt [86], who suggested that in such a social setting a
player’s utility for money depends on the fairness of the split across the two players. Based
on this model of fair exchange between humans, Ray and colleagues developed a Bayesian
model of how one player ‘mentalizes’ the impact of their actions (money split with partner)
on their partner [78]. The key feature is for each player to observe monetary exchanges with
their partner and estimate in a Bayesian manner the ‘fairness type’ of their partner, that is,
the degree to which the partner is sensitive to an inequitable split.

This model was able to ‘type’ players reliably from 8 rounds of monetary exchange in the
game. These types can be used to seek type-specific (fairness sensitivity) neural correlates.
More importantly, the model can be used to phenotype individuals according to
computational parameters important in this simple game-theoretic model of human
exchange. This is an important new possibility. Using this same game, Koshelev and
colleagues showed that healthy investors playing with a range of psychopathological groups
in the trustee role can be clustered in a manner that reflects that type of psychopathology
acting as the trustee [87]. This model used a Bayesian clustering approach to observations of
the healthy investors’ behavior as induced by interactions with different psychopathology
groups. These preliminary results suggest that parameters extracted from staged (normative)
game-theoretic exchanges could be used profitably as a new phenotyping tool for humans,
where the phenotypes are defined by computational parameters extracted using models.

Computational phenotyping of human cognitive function

Computational models of human mental function present more general possibilities for
producing new and useful human phenotypes. These phenotypes can then structure the
search for genetic and neural contributions to healthy and diseased cognition. We do not
expect such an approach to supplant current descriptive nosologies; instead, they will be an
adjunct, where the nature of the computational characterization offers a new lexicon for
understanding mental function in humans. Moreover, this approach can start with humans,
define a computational phenotype, seek neural and genetic correlates of this phenotype and
then turn to animal models for deeper biological study.

Under the restricted decision-making landscape that we have painted, RL models provide a
natural example of a type of computational model that could be used in such phenotyping.
Moreover, we sketched briefly how game-theoretic probes also allow for new forms of
computational modeling and hence new ways to computationally phenotype humans.
Through their built-in principles of operation and notions of optimal performance, RL

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 8

models provide constraints that help bridge the aforementioned gap between molecular and
behavioral levels of description. However, the behavioral underpinning of these models is
extremely shallow at present, especially in human subjects. As suggested by the examples
above, the estimation and use of computational variables, such as these, will require new
kinds of behavioral probes, combined with an ever-evolving capacity to make neural
measurements in healthy human brains. Not only is better phenotyping through the
development of new probes needed, but also unprecedented levels of phenotyping of
cognitive function. Many of the best ideas about mental performance and function derive
primarily from studies in other species. While these animal models have been strikingly
successful at uncovering the biology underlying learning, memory and behavioral choice,
the human behavioral ‘software’ is likely to be significantly different in important ways that
the probes will need to capture. Large-scale computational phenotyping will require radical
levels of openness across scientific disciplines and successful models for data exchange and
data sharing.

Concluding remarks

If the computational approaches we have outlined turn out to be effective in psychiatry, then
what might one expect? The large-scale behavioral phenotyping project sketched above
involves substantial aspects of data analysis and computational modeling. The aim of the
data analysis will be to link precise elements of the models to measurable aspects of
behavior and to molecular and neural substrates that can be independently measured. A
strong likelihood here is that the models will offer a set of categories for dysfunction that are
related to, but different from, existing notions of disease and this will lead to a need for
translation.

Although we did not focus on them here, there are also implications for mathematical
modeling. A simulation-based account of measurable brain dynamics, anatomical pathways
and brain regions could be expected, equipped with visualization and analysis methods to
help make sense of the output. The ultimate hope is for a detailed, multi-level, model that
allows prediction of the effects of malfunctions and manipulations. However, making this
sufficiently accurate at the scales that matter for cognition and behavior is a long way off.
One critical, though as yet unproven, possibility is that a computational understanding will
provide its own kind of short-circuit, with, for instance, rules of self-organization of neural
elements based on achieving particular computational endpoints, thereby removing the
requirement for detailed specification.

Finally, the most pressing requirement is for training. Broad and deep skills across cognitive
neuroscience, computational neuroscience, cellular and molecular neuroscience,
pharmacology, neurology, and psychiatry itself, in addition to computer science and
engineering, are required for the emergence of the richly interdisciplinary field of
computational psychiatry. Optimistically, how to achieve this may become clearer as
thoughts mature about restructuring education to achieve breadth across the brain-related
clinical disciplines of neurology and psychiatry [88].

Glossary

Cognitive
phenotype

a phenotype is a measureable trait of an organism. Although easy
to state in this manner, the idea of a phenotype can become subtle
and contentious. Phenotypes include different morphology,
biochemical cascades, neural connection patterns, behavioral
patterns and so on. Phenotypic variation is a term used to refer to

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 9

Computational
phenotyping

Game theory

Instrumental
controller

Neuromodulatory
systems

Pavlovian
controller

Serotonin

those variations in some trait on which natural selection could act.
A cognitive phenotype is a pattern of cognitive functioning in some
domain that could be used to classify styles of cognition. By
analogy, variations in cognitive phenotypes would be subject to
natural selection.

a computational phenotype is a measurable behavioral or neural
type defined in terms of some computational model. By analogy
with other phenotypes, a computational phenotype should show
variation across individuals and natural selection could act on this
variation. Large-scale computational phenotyping in humans has
not been carried out; therefore, the ultimate utility of this idea has
not been rigorously tested.

the study of mathematical models of interactions between rational
agents.

instrumental conditioning is the process by which reward and
punishment are used in a contingent fashion to increase or decrease
the likelihood that some behavior will occur again in the future. An
instrumental controller is one whose control over behavior can be
conditioned in exactly the same fashion. It is an operational term
used in the reinforcement learning approach to motivated behavior
to refer to any controller whose influence over behavior shows the
dependence on rewards and punishments typical of instrumental
conditioning.

systems of neurons that project to broad regions of target neural
tissue to modulate subsequent neural responses in those regions.
Neuromodulatory systems typically have cell bodies situated in the
brainstem and basal forebrain and deliver neurotransmitters, such
as serotonin, dopamine, acetylcholine and norepinephrine, to target
regions. They are called modulatory because their impact is
typically much longer-lasting than fast synaptic effects mediated by
glutamate and they are much more widely distributed.

an operational name for a behavioral controller that is Pavlovian in
the normal psychological use of this term – that is, the controller
mediates involuntary responses to situations or stimuli. Pavlovian
control can be demonstrated behaviorally and modern work is
focused on identifying the neural substrates that contribute to this
function.

a neuromodulator common to many neurons in the raphe nuclei.
Serotonin has a presumed role in clinical depression because of the
efficacy of medications that selectively block its reuptake into
neurons after its release from synaptic terminals (so-called SSRI’ s
– selective serotonin reuptake inhibitors).

References

1. American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders (DSM-

IV). American Psychiatric Association; 2000.

2. Kishida KT, et al. Neuroeconomic approaches to mental disorders. Neuron. 2010; 67:543–554.

[PubMed: 20797532]

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 10

3. Maia T, Frank MJ. From reinforcement learning models to psychiatric and neurological disorders.

Nat. Neurosci. 2011; 14:154–162. [PubMed: 21270784]

4. Huys QJM, et al. Are computational models useful for psychiatry? Neur. Netw. 2011; 24:544–551.
5. Hodgkin AL, Huxley AF. A quantitative description of membrane current and its application to

conduction and excitation in nerve. J. Physiol. 1952; 117:500–544. [PubMed: 12991237]

6. Dayan, P.; Abbott, LF. Theoretical Neuroscience. MIT Press; 2001.
7. Marreiros AC, et al. Population dynamics under the Laplace assumption. Neuroimage. 2009;

44:701–714. [PubMed: 19013532]

8. Tretter F, et al. Affective disorders as complex dynamic diseases: a perspective from systems

biology. Pharmacopsychiatry. 2011; 44(Suppl. 1):S2–S8. [PubMed: 21544742]

9. Moran RJ, et al. Alterations in brain connectivity underlying Beta oscillations in parkinsonism.

PLoS Comput. Biol. 2011; 7 e1002124.

10. Wood MD, Wren PB. Serotonin-dopamine interactions: implications for the design of novel
therapeutic agents for psychiatric disorders. Prog. Brain Res. 2008; 172:213–230. [PubMed:
18772035]

11. Friston KJ, Dolan RJ. Computational and dynamic models in neuroimaging. Neuroimage. 2010;

52:752–765. [PubMed: 20036335]

12. Honey CJ, et al. Network structure of cerebral cortex shapes functional connectivity on multiple
time scales. Proc. Natl. Acad. Sci. U.S.A. 2007; 104:10240–10245. [PubMed: 17548818]

13. Turing AM. Computing machinery and intelligence. Mind. 1950; 59:433–460.
14. Gödel K. Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme,

I. Monatshefte für Mathematik und Physik. 1931; 38:173–198.

15. Turing AM. On computable numbers, with an application to the entscheidungsproblem. Proc.

Lond. Math. Soc. 1936; 42:230–265.

16. Church A. An unsolvable problem of elementary number theory. Am. J. Math. 1936; 58:345–363.
17. Nagel, E.; Newman, JR. Gödel’s Proof. New York University Press; 1958.
18. Garey, MR.; Johnson, DS. Computers and Intractability: A Guide to the Theory of NP-

Completeness. W.H. Freeman; 1979.

19. Friston KJ. The free-energy principle: a unified brain theory? Nat. Rev. Neurosci. 2010; 11:127–

138. [PubMed: 20068583]

20. Kamil, AC., et al. Foraging Behavior. Plenum Press; 1987.
21. Uhlhaas PJ, Singer W. The development of neural synchrony and large-scale cortical networks

during adolescence: relevance for the pathophysiology of schizophrenia and neurodevelopmental
hypothesis. Schizophr Bull. 2011; 37:514–523. [PubMed: 21505118]

22. Servan-Schreiber D, et al. A network model of catecholamine effects: gain, signal-to-noise ratio,

and behavior. Science. 1990; 249:892–895. [PubMed: 2392679]

23. Montague PR, et al. Foraging in an uncertain environment using predictive Hebbian learning. Adv.

Neural Inform. Proc. Sys. 1994; 6:598–605.

24. Montague PR, et al. Bee foraging in uncertain environments using predictive Hebbian learning.

Nature. 1995; 377:725–728. [PubMed: 7477260]

25. Montague PR, et al. A framework for mesencephalic dopamine systems based on predictive

Hebbian learning. J. Neurosci. 1996; 16:1936–1947. [PubMed: 8774460]

26. Montague PR, et al. Computational roles for dopamine in behavioral control. Nature. 2004;

431:760–767. [PubMed: 15483596]

27. McCulloch W, Pitts W. A logical calculus of the ideas immanent in nervous activity. Bull. Math.

Biophys. 1943; 5:115–133.

28. Rosenblatt F. The perceptron: a probabilistic model for information storage and organization in the

brain. Psychol. Rev. 1958; 65:386–408. [PubMed: 13602029]

29. McClelland, J.; Rumelhart, D. Explorations in Parallel Distributed Processing: A Handbook of

Models, Programs, and Exercises. MIT Press; 1989.

30. O’Reilly, R.; Munakata, Y. Computational Explorations in Cognitive Neuroscience: Understanding

the Mind by Simulating the Brain. MIT Press; 2000.

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 11

31. Hopfield JJ. Neural networks and physical systems with emergent collective computational

abilities. Proc. Natl. Acad. Sci. U.S.A. 1982; 79:2554–2558. [PubMed: 6953413]

32. Hopfield JJ. Neurons with graded response have collective computational properties like those of
two-state neurons. Proc. Natl. Acad. Sci. U.S.A. 1984; 81:3088–3092. [PubMed: 6587342]
33. Hopfield JJ, Tank DW. Computing with neural circuits: a model. Science. 1986; 233:625–633.

[PubMed: 3755256]

34. Hinton, GE.; Sejnowski, TJ. Optimal perceptual inference. Proceedings of the IEEE Conference on

Computer Vision and Pattern Recognition; Washington DC. 1983. p. 448-453.

35. Cohen JD, Servan-Schreiber D. Context, cortex and dopamine: a connectionist approach to
behavior and biology in schizophrenia. Psychol. Rev. 1992; 99:45–77. [PubMed: 1546118]

36. Cohen JD, Servan-Schreiber D. A theory of dopamine function and cognitive deficits in

schizophrenia. Schizophr. Bull. 1993; 19:85–104. [PubMed: 8095737]

37. Cohen JD, et al. A computational approach to prefrontal cortex, cognitive control, and

schizophrenia: Recent developments and current challenges. Phil. Trans. R. Soc. Lond. B: Biol.
Sci. 1996; 351:1515–1527. [PubMed: 8941963]

38. Braver TS, et al. Cognition and control in schizophrenia: a computational model of dopamine and

prefrontal function. Biol. Psychiatry. 1999; 46:312–328. [PubMed: 10435197]

39. Carter CS, et al. Anterior cingulate cortex, error detection, and the on line monitoring of

performance. Science. 1998; 280:747–749. [PubMed: 9563953]

40. Carter CS, et al. Anterior cingulate cortex and impaired self-monitoring of performance in patients
with schizophrenia: an event-related fMRI study. Am. J. Psychiatry. 2001:1423–1428. [PubMed:
11532726]

41. Frank MJ, et al. By carrot or by stick: cognitive reinforcement learning in Parkinsonism. Science.

2004; 306:1940–1943. [PubMed: 15528409]

42. O’Reilly RC. Biologically-based computational models of high-level cognition. Science. 2006;

314:91–94. [PubMed: 17023651]

43. O’Reilly RC, Frank MJ. Making working memory work: a computational model of learning in the
prefrontal cortex and basal ganglia. Neural Comput. 2006; 18:283–328. [PubMed: 16378516]

44. Hazy TE, et al. Toward an executive without a homunculus: bomputational models of the

prefrontal cortex/basal ganglia system. Philos. Trans. R. Soc. Lond. B: Biol. Sci. 2007; 362:1601–
1613. [PubMed: 17428778]

45. Smith AJ, et al. Linking animal models of psychosis to computational models of dopamine

function. Neuropsychopharmacology. 2007; 32:54–66. [PubMed: 16710321]

46. Corlett PR, et al. Glutamatergic model psychoses: prediction error, learning, and inference.

Neuropsychopharmacology. 2011; 36:294–315. [PubMed: 20861831]

47. Redish AD, et al. A unified framework for addiction: vulnerabilities in the decision process.
Behav. Brain Sci. 2008; 31:415–437. (discussion pp. 437–487). [PubMed: 18662461]

48. Kumar P, et al. Abnormal temporal difference reward-learning signals in major depression. Brain.

2009; 131:2084–2093. [PubMed: 18579575]

49. Gradin VB, et al. Expected value and prediction error abnormalities in depression and

schizophrenia. Brain. 2011

50. Dayan P, Huys QJM. Serotonin in affective control. Annu. Rev. Neurosci. 2009; 32:95–126.

[PubMed: 19400722]

51. Soubrie P. Reconciling the role of central serotonin neurons in human and animal behavior. Behav.

Brain Res. 1986; 9:319–364.

52. Boureau Y-L, Dayan P. Opponency revisited: competition and cooperation between dopamine and

serotonin. Neuropsychopharmacology. 2011

53. Cools R, et al. Acute tryptophan depletion in healthy volunteers enhances punishment prediction

but does not affect reward prediction. Neuropsychopharmacology. 2008; 33:2291–2299. [PubMed:
17940553]

54. Deakin JFW. Roles of brain serotonergic neurons in escape, avoidance and other behaviors. J.

Psychopharmacol. 1983; 43:563–577.

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 12

55. Deakin JFW, Graeff FG. 5-HT and mechanisms of defense. J. Psychopharmacol. 1991; 5:305–316.

[PubMed: 22282829]

56. Robinson TE, Berridge KC. The psychology and neurobiology of addiction: an incentive-

sensitization view. Addiction. 2000; 95:s91–s117. [PubMed: 11002906]

57. Robinson TE, Berridge KC. The incentive sensitization theory of addiction: some current issues.

Philos. Trans. R. Soc. Lond. B: Biol. Sci. 2008; 363:3137–3146. [PubMed: 18640920]

58. Flagel SB, et al. Individual differences in the attribution of incentive salience to reward-related
cues: implications for addiction. Neuropharmacology. 2009; 56(Supp. 1):139–148. [PubMed:
18619474]

59. Seligman, MEP. Helplessness on Depression, Development and Death. W.H. Freeman & Co.;

1975.

60. Maier S, Seligman M. Learned helplessness: Theory and evidence. J. Exp. Psychol. Gen. 1976;

105:3–46.

61. Miller WR, Seligman ME. Depression and learned helplessness in man. J. Abnorm. Psychol. 1975;

84:228–238. [PubMed: 1169264]

62. Goodkin F. Rats learn the relationship between responding and environmental events: An

expansion of the learned helplessness hypothesis. Learn. Motiv. 1976; 7:382–393.

63. Maier SF, Watkins LR. Stressor controllability and learned helplessness: The roles of the dorsal
raphe nucleus, serotonin, and corticotropin-releasing factor. Neurosci. Biobehav. Rev. 2005;
29:829–841. [PubMed: 15893820]

64. Tenenbaum JB, et al. How to grow a mind: statistics, structure, and abstraction. Science. 2011;

331:1279–1285. [PubMed: 21393536]

65. Sutton, RS. Integrated architectures for learning, planning, and reacting based on approximating
dynamic programming. Proceedings of the 7th International Conference on Machine Learning;
Morgan Kaufmann. 1990. p. 216-224.

66. Kakade S, Dayan P. Dopamine: generalization and bonuses. Neur. Netw. 2002; 15:549–559.
67. Daw ND, et al. Model-based influences on humans’ choices and striatal prediction errors. Neuron.

2011; 69:1204–1215. [PubMed: 21435563]

68. Baron-Cohen S. Theory of mind and autism: a review. Int. Rev. Res. Ment. Retard. 2001; 23:169–

184.

69. Frith CD, Frith U. Interacting minds – a biological basis. Science. 1999; 286:692–1695.
70. Gallagher HL, Frith CD. Functional imaging of ‘theory of mind’. Trends Cogn. Sci. 2003; 7:77–

83. [PubMed: 12584026]

71. Rilling JK, et al. A neural basis for social cooperation. Neuron. 2002; 35:395–405. [PubMed:

12160756]

72. Rilling JK, Sanfey AG. The neuroscience of social decision-making. Annu. Rev. Psychol. 2011;

62:23–48. [PubMed: 20822437]

73. King-Casas B, et al. Getting to know you: reputation and trust in a two-person economic exchange.

Science. 2005; 308:78–83. [PubMed: 15802598]

74. Tomlin D, et al. Agent-specific responses in cingulate cortex during economic exchanges. Science.

2006; 312:1047–1050. [PubMed: 16709783]

75. Chiu PH, et al. Self responses along cingulate cortex reveal quantitative neural phenotype for high-

functioning autism. Neuron. 2008; 57:463–473. [PubMed: 18255038]

76. Hampton AN, et al. Neural correlates of mentalizing-related computations during strategic

interactions in humans. Proc. Natl. Acad. Sci. U.S.A. 2008; 105:6741–6746. [PubMed: 18427116]

77. King-Casas B, et al. The rupture and repair of cooperation in borderline personality disorder.

Science. 2008; 321:806–810. [PubMed: 18687957]

78. Ray D, et al. Bayesian model of behavior in economic games. Adv. Neural Inform. Proc. Sys.

2008; 21:1345–1353.

79. Yoshida W, et al. Game theory of mind. PLoS Comput. Biol. 2008; 4
80. Yoshida W, et al. Neural mechanisms of belief inference during cooperative games. J. Neurosci.

2010; 30:10744–10751. [PubMed: 20702705]

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

Montague et al.

Page 13

81. Yoshida W, et al. Cooperation and heterogeneity of the autistic mind. J. Neurosci. 2010; 30:8815–

8818. [PubMed: 20592203]

82. Bhatt M, Camerer C. Self-referential thinking and equilibrium as states of minds in games: FMRI

evidence. Games Econ. Behav. 2005; 52:424–459.

83. Coricelli G, Nagel R. Neural correlates of depth of strategic reasoning in medial prefrontal cortex.

Proc. Natl. Acad. Sci. U.S.A. 2009; 106:9163–9168. [PubMed: 19470476]

84. Bhatt MA, et al. Neural signatures of strategic types in a two-person bargaining game. Proc. Natl.

Acad. Sci. U.S.A. 2010; 107:19720–19725. [PubMed: 21041646]

85. Lee D. Game theory and neural basis of social decision making. Nat. Neurosci. 2008; 11:404–409.

[PubMed: 18368047]

86. Fehr E, Schmidt KM. A theory of fairness, competition, and cooperation. Q. J. Econ. 1999;

114:817–868.

87. Koshelev M, et al. Biosensor approach to psychopathology classification. PLoS Comput. Biol.

2010; 6 e1000966.

88. Insel TR, Wang PS. Rethinking mental illness. JAMA. 2010; 303:1970–1971. [PubMed:

20483974]

89. Sutton, RS.; Barto, AG. Reinforcement Learning. MIT Press; 1998.
90. Daw ND, Doya K. The computational neurobiology of learning and reward. Curr. Opin. Neurobiol.

2006; 16:199–204. [PubMed: 16563737]

91. Dayan P, Daw ND. Decision theory, reinforcement learning, and the brain. Cogn. Affect. Behav.

Neurosci. 2008; 8:429–453. [PubMed: 19033240]

92. Tolman EC. Cognitive maps in rats and men. Psychol. Rev. 1948; 55:189–208. [PubMed:

18870876]

93. Doya K. What are the computations of the cerebellum, the basal ganglia, and the cerebral cortex.

Neural Netw. 1999; 12:961–974. [PubMed: 12662639]

94. Dickinson, A.; Balleine, B. The role of learning in motivation. In: Gallistel, CR., editor. Stevens’

Handbook of Experimental Psychology, vol: 3: Learning, Motivation and Emotion. 3rd ed. Wiley;
2002. p. 497-533.

95. Killcross S, Coutureau E. Coordination of actions and habits in the medial prefrontal cortex of rats.

Cereb. Cortex. 2003; 13:400–408. [PubMed: 12631569]

96. Daw ND, et al. Uncertainty-based competition between prefrontal and dorsolateral striatal systems

for behavioral control. Nat. Neurosci. 2005; 8:1704–1711. [PubMed: 16286932]

97. Glascher J, et al. States versus rewards: dissociable neural prediction error signals underlying

model-based and model-free reinforcement learning. Neuron. 2010; 66:585–595. [PubMed:
20510862]

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Montague et al.

Page 14

Box 1. Reinforcement learning

Reinforcement learning (RL) is a field, partly spawned by mathematical psychology, that
spans artificial intelligence, operations research, statistics and control theory (for a good
introductory account of RL, see [89]). RL addresses how systems of any sort, be they
artificial or natural, can learn to gain rewards and avoid punishments in what might be
very complicated environments, involving states (such as locations in a maze) and
transitions between states. The field of neural RL maps RL concepts and algorithms onto
aspects of the neural substrate of affective decision-making [90,91]. One important
feature of this framework is that the majority of its models can be derived from a
normative model of how an agent ‘should’ behave under some explicit notion of what
that agent is trying to optimize [89].

Conventional and neural RL include two very broad classes of method: model-based and
model-free. Model-based RL involves building a statistical model of the environment (a
form of cognitive map; see [92]) and then using it to (i) choose actions based on
predicted outcomes and (ii) improve predictions by optimizing the model. Acquiring such
models from experience can be enhanced by sophisticated prior expectations (a facet that
we relate to the phenomena of learned helplessness). In other words, an agent
significantly enhances the models it can build based on experience if it already starts with
a good characterization of its environment. In turn, these models enable moment-to-
moment prediction and planning. Except in very simple environments, prediction and
planning consume enormous memory and computational resources – a fact has inspired
much work on approximations and the search for biological work-arounds.

Model-free RL involves learning exactly the same predictions and preferences as model-
based RL, but without building a model. Instead, model-free RL learns predictions about
the environment by enforcing a strong consistency constraint: successive predictions
about the same future outcomes should be the same. Actions are chosen based on the
simple principle that actions which lead to better predicted outcomes are preferred.
Model-free RL imposes much lower demands on computation and memory because it
depends on past learning rather than present inference. However, this makes it less
flexible to changes in the environment.

The conceptual differences between model-based and model-free RL suggest that
correlates can be sought in real-world neural and behavioral data. There are ample results
from animal and human experiments to suggest that both model-free and model-based
RL systems exist in partially distinct regions of the brain [67,93–97] and that there is a
rich panoply of competitive and cooperative interactions between them [67]. Model-free
RL has a particularly close association with the activity of the dopamine
neuromodulatory system, especially in the context of appetitive outcomes and
predictions.

Finally, model-based and model-free RL are both instrumental in the sense that actions
are chosen because of their consequences [94]. Animals are also endowed with extremely
sophisticated Pavlovian controllers (see main text), where outcomes and predictions of
those outcomes directly elicit a set of species-typical choices apparently not under
voluntary control. One important example related to predictions of future negative
outcomes is behavioral inhibition (learning not to do something), which may be related to
serotonin [51].

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

Montague et al.

Page 15

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Figure 1.
Components of Computational Psychiatry.

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.

Montague et al.

Page 16

Figure 2. Economic games requiring theory-of-mind modeling
(a) The stag-hunt game. A two-player game, where players can cooperate to hunt and trap
high yield stags or act alone and hunt low yield rabbits. A human subject (red circle) plays
the game with a computer agent partner (green circle) to acquire either a (high value) mobile
stag (larger gray square) or a (low value) rabbit sitting at a fixed position (smaller gray
square). The hunters can catch a rabbit simply by moving onto its fixed location or they can
catch a stag together by cooperatively trapping it somewhere on the open grid. (b) The
multi-round trust game. A game of reciprocation that lasts 10 rounds. In each round, the
proposer (the investor) is engaged with 20 monetary units. The investor any fraction of this
(I) to the responder (the trustee). On the way to the trustee the amount triples and the trustee
can repay any fraction R of the tripled amount. Players who think through the impact of their
actions on their partner make more money than those who do not [73,78].

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

$
w
a
t
e
r
m
a
r
k
-
t
e
x
t

Trends Cogn Sci. Author manuscript; available in PMC 2013 January 28.
