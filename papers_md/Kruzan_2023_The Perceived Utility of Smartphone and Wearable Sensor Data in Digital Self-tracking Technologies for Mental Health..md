# Kruzan_2023_The Perceived Utility of Smartphone and Wearable Sensor Data in Digital Self-tracking Technologies for Mental Health.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
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
Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 
June 13.

Published in final edited form as:

Proc SIGCHI Conf Hum Factor Comput Syst. 2023 April ; 2023: . doi:10.1145/3544548.3581209.

The Perceived Utility of Smartphone and Wearable Sensor Data 
in Digital Self-tracking Technologies for Mental Health

Kaylee Payne Kruzan,
Northwestern University, Illinois, USA

Ada Ng,
Northwestern University, Illinois, USA

Colleen Stiles-Shields,
University of Illinois at Chicago, Illinois, USA

Emily G. Lattie,
Northwestern University, Illinois, USA

David C. Mohr,
Northwestern University, Illinois, USA

Madhu Reddy
University of California Irvine, Irvine, USA

Abstract

Mental health symptoms are commonly discovered in primary care. Yet, these settings are not 
set up to provide psychological treatment. Digital interventions can play a crucial role in stepped 
care management of patients’ symptoms where patients are offered a low intensity intervention, 
and treatment evolves to incorporate providers if needed. Though digital interventions often use 
smartphone and wearable sensor data, little is known about patients’ desires to use these data to 
manage mental health symptoms. In 10 interviews with patients with symptoms of depression and 
anxiety, we explored their: symptom self-management, current and desired use of sensor data, 
and comfort sharing such data with providers. Findings support the use digital interventions to 
manage mental health, yet they also highlight a misalignment in patient needs and current efforts 
to use sensors. We outline considerations for future research, including extending design thinking 
to wraparound services that may be necessary to truly reduce healthcare burden.

Keywords

digital mental health; mobile phone app; sensing; tracking; self-management; depression; anxiety; 
primary care

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided 
that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the 
first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is 
permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. 
Request permissions from permissions@acm.org.

kaylee.kruzan@northwestern.edu . 

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

1 

INTRODUCTION

Page 2

Mental health conditions like depression and anxiety are common, yet an estimated 30% of 
people with these conditions receive no treatment, and many in treatment receive inadequate 
care [47, 98]. Though these conditions are often first identified within primary care settings 
(including primary care and family medicine clinics) when patients come in for routine 
check-ups, the healthcare system is not set up to provide the psychological treatment 
indicated. Healthcare providers are limited in their ability to provide adequate treatment 
due to constraints of time, training, and resources. As a result, patients are often referred to 
outside mental health providers at which point they encounter barriers due to the shortage 
of psychologists, counselors, and social workers who can deliver psychological treatment, 
as well as transportation problems, cost, and other factors impacting the desire for formal 
treatment (e.g., stigma) [69, 70, 75].

One way to buffer the loss in this transition from diagnosis to securing treatment may be to 
offer or deploy low-cost, evidence-based digital mental health interventions (DMHIs) at this 
opportune point of care [25, 37]. DMHIs are highly flexible and offer myriad opportunities 
to bridge gaps in care for patients on wait-lists or those who prefer to self-manage. They 
can also be used to augment services by providing clinicians and other healthcare providers 
with access to specific and granular data about patient symptoms between visits. Indeed, 
multiple meta-analyses have shown that DMHIs focused on improving mental health can be 
efficacious [33, 36]. DMHIs have particular promise as low-intensity interventions within 
stepped care treatment models, which aim to deliver minimally time and resource intensive 
treatments before higher intensity treatments in healthcare settings that are overburdened, 
like primary care.

Increasingly, DMHIs incorporate smartphone and wearable sensors which provide 
continuous data streams that can be leveraged by providers or patients to understand and 
improve symptoms without placing significant burden on users. Yet, to date little is known 
about how individuals with common mental health conditions currently use smartphone 
and wearable technologies to manage their symptoms, and whether the data these devices 
produce align with their mental health goals. Such an understanding is necessary if we are 
to develop DMHIs that are usable and acceptable to primary care patients with symptoms 
of depression and anxiety. The overarching goal of this project was identify the mental 
health self-management needs of patients whose symptoms of depression and anxiety are 
discovered in primary care, with the intention of developing a DMHI that contributes 
little additional burden to this healthcare setting and supports patients’ self-management of 
symptoms. We explored self-tracking technologies, in particular, due to their ubiquity, their 
prior use for behavior change [43, 61, 88], and the potential for the data generated from 
these devices to be of value in patient self-management. We specifically aimed to explore 
(1) patients’ mental health self-management, (2) their interest in, and preferences for, a 
self-tracking technology to assist in mental health self-management, and (3) their comfort 
with sharing data from such a technology with primary care providers.

This paper makes four contributions in service of exploring the potential use of DMHIs that 
leverage sensors to support primary care patients managing mental health symptoms as part 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 3

of an early stage of a stepped care program. First, we provide a descriptive understanding of 
primary care patients’ diverse experiences of mental health symptoms and self-management. 
In general, mental health symptoms made it difficult for participants to engage in activities 
that brought them enjoyment and a sense of accomplishment. Maintaining mental health 
involved striking a comfortable balance between engaging in valued activities and doing so 
with a sense of ease. Though technologies were not central to participants’ experiences of 
mental health self-management, they were a common resource to access beneficial activities 
and social support, underscoring their potential as an accessible and acceptable means of 
intervention. Second, we identify their needs and preferences regarding self-tracking for 
mental health, including what types of tracked information would be helpful, and when 
it would be most helpful. Participants were particularly interested in tracking behavioral 
markers of mental health, including engagement in beneficial activities, if it could help them 
to better manage symptoms during periods of high symptomology. Third, we identify ways 
smartphone and wearable sensor and self-report data can be leveraged to support mental 
health maintenance and active symptom management, which participants experienced as 
two distinct periods in need of different technological support. Finally, given participant 
receptivity to sharing DMHI data with their providers, we consider structures and services 
that would need to be in place in order for a DMHI to successfully integrate within primary 
care and reduce burden in this setting.

2  RELATED WORK

2.1  Depression and Anxiety in a Primary Care Context

Depression and anxiety are two of the most prevalent mental health conditions [47, 64]. 
Left untreated they can have long-term consequences for physical and psychological health 
and contribute significantly to rates of global disability [19, 31, 78]. Highly efficacious 
and evidence-based treatments for both depression and anxiety exist such as cognitive 
behavior therapy (CBT) which focuses on identifying and changing thoughts, attitudes, 
beliefs and behaviors that negatively impact mental health [21, 41]. However, most people 
with these conditions do not receive any mental health treatment [97], and even fewer 
receive evidence-based mental health treatment [34]. Structural (cost, time, geography), 
systemic (structures built within racism, ableism), and attitudinal barriers (stigma, mental 
health literacy) impact access and uptake of mental health care [69, 70, 75]. Further, many 
individuals with symptoms of depression or anxiety do not identify them as meriting care, 
reducing the likelihood of them seeking, and benefiting from, support [35, 38, 84]. Early 
identification and referrals to accessible and acceptable treatments for these common mental 
health conditions are needed.

Recognizing the value of early identification, the U.S. Preventive Services Task Force 
recommends systematic screening for depression in adults and adolescents in primary care 
settings, and that adequate systems are in place to ensure those with positive screens receive 
appropriate treatment [90, 91]. Though rates of diagnoses increase as more patients are 
screened, there is not a similar trend for mental healthcare service utilization [16, 86], with 
some studies showing 2/3rds of those screened for depression do not receive treatment [79]. 
Moreover, primary care physicians can, and do, prescribe medications for mental health 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 4

conditions, but studies have shown that up to 2/3rds of patients prefer psychotherapy, to 
pharmacological treatment [18, 26, 82].

There are not nearly enough mental healthcare providers to respond to those who already 
seek mental health treatment, however, which means that even when individuals are 
identified within our healthcare systems, they are unlikely to receive quality mental 
healthcare [45]. For example, in a large national survey of over 9,000 individuals, just 21.5% 
with a psychiatric disorder received treatment from a qualified mental health professional, 
with other studies similarly reporting around 30% of people with a mental health diagnoses 
receiving treatment [47, 98]. The percentage of people receiving care is even lower among 
marginalized communities and those in high hardship areas, in part because they are less 
likely to initiate mental health treatment, and more likely to drop out from treatment [76]. 
Low-intensity services that can be recommended or delivered to people when their mental 
health symptoms are first identified could increase the likelihood that they will gain access 
to evidence-based resources, and possibly prevent the worsening of symptoms.

2.1.1  Mental Health Treatment Under Constrained Resources.—In response to 
the aforementioned shortages, several models of condition management have been used 
in primary care to more adequately and efficiently address the needs of individuals with 
depression and anxiety, including stepped care treatment models [23, 95]. In traditional 
stepped care, patients begin with a low intensity treatment and their symptoms are monitored 
on a routine basis. Patients that do not respond, or do not show meaningful improvement in 
symptoms with the lowest intensity intervention, “step up” to higher intensity interventions 
until improvement is seen. In general, research has shown that stepped care models can 
be effective in the treatment of depression [95], and meta-analyses have shown that 
stepped care models have similar effect sizes to other care models for depression like 
collaborative care [5]. A typical first step in a stepped care program would be to monitor 
for symptoms through regular assessment. This is already commonly done by administering 
the depression and anxiety screeners in routine care. When symptoms are detected and 
intervention is indicated a second step may be to recommend patients a self-management or 
self-help intervention. Often these early interventions include pamphlets or online sources 
of information to reduce burden on healthcare providers. If symptoms do not improve 
with DMHI self-management, more intensive interventions such as facilitated or guided 
self-management, where a care manager offers low intensity support to increase adherence 
and motivation or face-to-face intervention with a provider, an so on until there is symptom 
improvement. Among the benefits of stepped care models are the ability to provide 
evidence-based resources in a way that does not overly burden the healthcare system, and 
the ability to scale services to more patients in need. Digital interventions can play a crucial 
role in the early steps of stepped care.

2.2  Digital Mental Health Interventions

Digital mental health interventions are tools that leverage commonly available technologies 
such as apps and websites to deliver mental health treatment in alignment with the Task 
Force’s call for “adequate” care [77]. DMHIs are a promising method to address the 
need for services as they enable expeditious delivery of evidence-based treatments to 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 5

individuals in a scalable and cost-effective manner. In addition to studies showing that 
individuals with psychiatric conditions have interest in using DMHIs to improve their mental 
health [54, 92], several meta-analyses have shown that DMHIs are efficacious [32, 33]. 
Further these tools are flexible as they can be designed to help individuals self-manage 
their symptoms by providing psychoeducation on their illness, coping strategies, and tools 
for tracking symptoms/progress or to augment existing treatment, by providing support 
to patients between treatment sessions [54]. For example, Intellicare is a mobile app 
intervention that focuses on self-management of depression and anxiety symptoms through 
interactive cognitive and behavioral skills training [72, 73], whereas ACT skills in a mobile 
app designed to support patients with Generalized Anxiety Disorder between sessions of 
Acceptance and Commitment Therapy [51]. This flexibility of DMHIs to both facilitate 
self-management and augment traditional mental health treatment, make them uniquely 
suited as a modality for integration within early stages of stepped care programs to provide 
quality care and reduce burden in primary care.

2.3  Self-Tracking for Self-Management

Increasingly, systems that support self-tracking are used as a means to support health and 
mental health self-management [49, 59]. Self-tracking systems have long been a focus 
of empirical study in the HCI community, with research identifying overall self-tracking 
practices, and tracking for chronic illness management [27, 30, 55]. Some self-tracking 
systems are specifically designed to closely align with CBT’s emphasis on increasing 
individuals’ awareness of thoughts, attitudes, and behaviors that impact mental health and 
well-being [28–30, 46]. For example, Mobilyze! is a CBT mobile intervention that collects 
data on the users’ self-reported mood as well as their activities and provides feedback based 
on correlations in data and depression scores [12]. Self-tracking is conducted primarily in 
two ways: (1) manually via patient self-report and (2) passively using built in smartphone 
sensors or commercial wearables.

2.3.1  Manual Symptom Tracking.—Given the subjective nature of mental health 
experiences, self-tracking systems have often relied on symptom self-report [13]. Indeed, in 
CBT for depression and anxiety, clinicians commonly ask patients to track their symptoms 
and thoughts, behaviors, and emotions related to symptoms between appointments. DMHIs 
can easily facilitate this type of tracking through repeated prompts of standardized clinical 
measures or informal mood tracking through emojis [62] or colors associated with mood 
[17]. As an example, IntelliCare allows users to track mood after completing specific 
mood-boosting activities [73]. Though manual tracking enables systematic evaluation of 
mental health over time, systems that rely on manual logging are burdensome and are 
therefore often unsustainable for users with chronic conditions, like depression or anxiety. 
Prior research has shown that overly relying on manual inputs can result in gaps in data [88] 
or no tracking at all [63]. Alternatively, tracking behaviors such as the amount of physical 
activity one has had in a day or the minutes spent inside one’s home, both of which can be 
correlated with depression and anxiety, can be virtually effortless with the use of sensors [7].

2.3.2  Passive Behavioral Sensing.—DMHIs that incorporate passive sensing 
typically collect continuous data on several behavioral and physiological markers of mental 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 6

state including sleep, physical exercise, and arousal, through accelerometers, location, 
and audio sensors [6, 94]. Due to the large complement of sensors built into everyday 
technologies, like smartphones and smartwatches, interest has grown around the use of 
sensor data to passively monitor and intervene on symptoms of depression and anxiety [7, 
14, 83, 99]. Work in this area has indeed provided evidence for several sensor-based features 
that relate to these conditions. For example, studies have shown relationships between 
depression and anxiety and mobility data, physical activity, speech patterns, sleep duration, 
mobility, and general phone usage [20, 58, 66, 80, 85, 87]. While sensor data have increased 
opportunities for researchers to understand these conditions and detect new digital signals 
reflecting behaviors that are related to mental health symptoms, there are several known 
limitations that impact the potential for these tools to improve symptoms in the wild.

First, self-tracking tools have the potential to increase a person’s awareness of symptoms, 
but research has shown that this awareness can be overwhelming or discouraging for 
users [28, 29, 46, 88], and can ultimately lead to lapses in technology use making gains 
unlikely. Secondly, behavioral markers are understood to be proxies for users’ experiences 
of depression and anxiety; however, little work has focused on which signals users need 
from sensors and, equally critical, when. Finally, sensor data do not often provide clear 
information on what a person can do to improve symptoms without further interpretation 
or clinician feedback, yet these tools are often designed for self-management with limited 
support from providers or other trained personnel. Understanding how to best support the 
general primary care patient population with these technologies is subject to empirical 
attention.

2.4  Summary

To understand the value of DMHIs that incorporate sensor data for primary care patients 
with symptoms of depression or anxiety, we need to understand how these individuals 
envision these data could be used to support their mental health and if, or how, these 
data relate to their personal mental health goals and existing self-management practices. 
Understanding that primary care is a common touchpoint for mental health screening and 
diagnosis, it is also imperative to understand users’ comfort with sharing tracked data with 
their providers as well as the perceived benefits and expectations users may have, if and 
when more intensive intervention is indicated. This understanding could help us develop 
a low-intensity digital intervention designed to address the needs of the large number of 
patients with depression and anxiety symptoms in a way that is acceptable to users and 
feasible in primary care.

3  METHODS

3.1  Recruitment and procedure

Participants were recruited from primary care and family medicine clinics housed within an 
urban healthcare system serving communities with high hardship indexes [52]. Recruitment 
involved the distribution of flyers in clinics and community organizations, as well as email 
and MyChart messages to patients within the care system. Interested individuals completed 
an online questionnaire to determine eligibility. Those meeting the following inclusion 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 7

criteria were eligible to participate: English speaking, over 12 years old, US citizen/resident, 
and self-reported depression or anxiety symptoms. The age range of interest shifted over 
the course of our early elicitation work as we became more familiar with our clinical 
stakeholders’ needs. Noting that an app could be useful for a younger cohort of users we 
extended our recruitment from an adult population to adolescents. While we were open to 
younger adolescents, the youngest participant we recruited was 17 years old. Also, to ensure 
access to a smartphone device (which is the technology of interest in this study), all eligible 
participants needed to indicate that someone in their family owned a smartphone. The 
study team settled on this criterion instead of individual smartphone ownership to ensure 
that younger adolescents could participate. We intentionally sampled broadly to reflect the 
diverse population (in terms of age, race, ethnicity, and mental health symptom severity) 
served through the healthcare system.

All eligible participants were contacted via phone or email by a member of the research 
team to alert them to their eligibility and initiate the consent process. Participants that 
were interested in providing consent were sent a link to an online consent document 
and were asked to provide their digital signature. Participants that provided consent then 
scheduled an interview time with the study research assistant and completed a baseline 
survey which included questions on demographics, and symptoms of depression (via 
Patient Health Questionnaire, PHQ-9) and anxiety (via the Generalized Anxiety Disorder 
Questionnaire, GAD-7). Ten individuals participated in semi-structured interviews with a 
PhD-level research assistant trained in the study procedure. One-on-one virtual interviews 
were conducted over zoom to ensure participant comfort speaking about their experiences 
of mental health symptoms (a potentially stigmatized topic) and to ensure participant 
safety, since the study took place during the Covid-19 pandemic. The interview guide 
was developed and iteratively refined by multiple members of the research team including 
a clinical psychologist, a qualitative researcher, and two PhD-level trainees. The guide 
included questions and probes focused on understanding participants’ mental health needs 
and preferences (e.g., How does your mental health, like feeling stressed, nervous, or down, 
affect your life? How do you choose the strategy you’ll use to manage your mental health 
in any particular instance?), their current self-management strategies (e.g., Can you tell 
me about a recent day when you were feeling stressed, anxious, or down and what you 
did to try to make yourself feel better?), and their current use of technologies, including 
self-tracking devices, in self-management (e.g., Which technologies are particularly helpful 
for your mental health?). Interviews lasted between 45 and 65 minutes for a total of 586 
minutes (9.77 hours) of audio.

3.2  Data analysis

Interviews were audio-recorded and transcribed. Data were analyzed through a conventional 
qualitative content analysis approach, as defined by [42]. This process included data 
familiarization, identification of individual codes, grouping codes into categories based on 
conceptual similarity, reviewing and refining categories to reduce overlap and redundancy, 
defining and naming final groupings common across the whole dataset, and selecting 
examples from the data to accurately illustrate each.

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 8

Two authors read through the transcripts in full to familiarize themselves with the data. 
Then, these authors applied codes to two transcripts independently to identify an initial set 
of open codes (e.g., playlists to manage mood, group chats for support, Netflix to distract). 
They met to discuss these codes for face validity and conceptual clarity. Then the two 
authors conducted axial coding to group open codes into categories based on conceptual 
similarity (e.g., media use). At this stage and onward, discrepant codes were discussed 
and resolved via a consensus process [39]. This hierarchical code structure was revised to 
reduce overlap, and the remaining transcripts were divided evenly among the two authors 
to code independently. Finally, the authors organized categories under broader clusters of 
shared meaning (e.g., mental health self-management practices). Once these clusters were 
solidified, examples were drawn from the data for the write-up. All analyses were conducted 
in Dedoose, a qualitative data analysis software.

3.3  Study ethics and reflexivity statement

We recognize our responsibility, as researchers, to ensure participant comfort in discussing 
factors related to their mental health. We sought to create a safe environment for participants 
to share their personal experiences. This included reiterating at multiple points that 
they could discontinue the interview or skip over questions that they felt uncomfortable 
answering or reflecting on. Participants were also able to keep their camera off on zoom to 
increase comfort during the interview itself.

The research team included several clinical psychologists who provided clinical guidance 
throughout the study design and data collection periods. In addition, individuals with lived 
experience of some of the mental health concerns addressed here were part of the research 
team. Our team aimed to support participants in sharing their lived experiences of mental 
health and their perceptions, and did so through a human-centered design approach. All 
study procedures were approved by our human subjects board.

3.4  Participant demographics

Table 1 includes participant demographics. Participants in our sample were mostly female 
(n=8, 80%), and were racially diverse: Asian (n=3), American Indian (n=2), African 
American or Black (n=2), White (n=2), and more than one race (n=1). Four participants 
identified as Hispanic. On average, participants reported mild to moderate symptoms of 
depression (PHQ-9=6.56) and anxiety (GAD-7=7.25).

4  FINDINGS

Our findings are organized under five main headings: (1) Experiences with mental health 
symptoms, (2) Mental health self-management practices, (3) Histories with self-tracking 
technologies, (4) Desired self-tracking for mental health and (5) Comfort with, and 
expectations for, sharing data with providers. Overall, participants described that their 
mental health symptoms made it difficult for them to engage in activities that typically 
brought them a sense of enjoyment and accomplishment. To maintain good mental health, 
participants made proactive and intentional efforts to balance valued activities with task-
oriented activities in their daily life. When this balance was disrupted, either due to 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 9

symptoms (e.g., lethargy, motivation) or external and environmental factors outside of 
participants’ control (e.g., lack of access, Covid pandemic), they experienced difficulties re-
establishing equilibrium and a need to shift their focus to more manageable goals. Notably, 
in these periods of high symptomology, participants reported different needs relative to 
periods of low symptomology, which has important implications for the design of supportive 
self-tracking technologies for this population. Many participants were also comfortable 
sharing data from a self-tracking technology with their providers in service of more 
personalized treatment, and saw the sharing of data as a way to initiate conversations and 
enable timely interventions, underscoring the potential to integrate support from providers 
if, and when, indicated. We expand upon these findings below, beginning with patients’ 
experiences of mental health symptoms, and progressing to the use of, and interest in, 
technology for symptom management.

4.1  Experiences with mental health symptoms

Participants’ experiences of depression and anxiety included changes in mood, blunted 
enjoyment, and lack of motivation which resulted in difficulties completing routine 
activities. The presence of these symptoms was a reminder to participants that their mental 
health required their attention, and was often a source of further stress. The three most 
common experiences participants described were: (1) decreased enjoyment and motivation 
in daily life, (2) a sense of internal uneasiness, and (3) increased difficulty relating to and 
interacting with others.

Changes in mood, enjoyment, and motivation were highly salient in participant experiences, 
and a significant source of distress in daily life. For example, Participant 10 described that 
exercise was something he did to lift his mood when he was feeling relatively well; however, 
he struggled to initiate physical activity when his symptom load was high. Reflecting on 
these periods of high symptomology, Participant 10 described:

“My mind feels like – I’m thinking about something else when I’m doing a certain 
task or I’m just not as motivated. So, when I was feeling down, for example, I just 
wasn’t motivated to exercise like I usually would be, regardless of it’s just two days 
a week, I still wouldn’t want to do those two days. So, I feel like … the drive is not 
the same.” (P10)

Other participants similarly commented on the impact motivation has on their pursuit of 
activities that they usually enjoy when they are experiencing mental health symptoms. 
For example, Participant 6 described that needing to put energy towards mitigating his 
symptoms of anxiety, stunted his motivation to pursue pleasurable activities that were 
necessary for depression management. Specifically, Participant 6 said that he was: “less 
motivated to engage in enjoyable activities in the sense that I might feel like I have to devote 
extra time towards those important responsibilities and matters in the hopes that doing so 
will decrease the source or mitigate the source of that stress and anxiety.” (P6)

Relatedly, some participants described specific activities that they used to like, but that 
they lost interest in over periods of time managing symptoms. Participant 5 described that 
she “…used to love to write poems, but I stopped that maybe a year ago,” when her 
symptoms of depression increased. In these periods of poor mental health, participants 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 10

needed to re-prioritize their efforts towards activities that were manageable and that could 
quell symptoms.

In addition to noticeable shifts in motivation which impacted how, and what, activities 
participants engaged in daily, they also described an internal discomfort that came from 
noticing symptoms in daily life. For example, Participant 10 felt “a sense of uneasiness, just 
internally” when he recognized that he didn’t “get the same joy out of things,” like eating his 
favorite foods. Similarly, Participant 8 described feeling “listless” when reflecting on how it 
was “hard to get up in the morning.” And, Participant 4 reported feeling “out of place” when 
experiencing difficulties completing routine work:

“I feel like I’m slowed down. I can’t get anything done and I just feel really 
distracted especially when it comes to work. Just like it’s like I’ll be doing 
something that I know I can do incredibly well or really easily. I’ve done it 
hundreds of times before and I’ll mess it up or what have you or I’ll type my name 
on something. Small, little things like that, it’s just like…It’s so frustrating because 
it’s like I know I can do this.” (P4)

Though many of the symptoms participants described were experienced internally, they also 
contributed to a growing strain on interpersonal relationships. For example, Participant 8 
described changes in how she related to others like this: “I’m not appreciative of just general 
things happening around me or people. I’m maybe more snappish,” and Participant 10 said: 
“I think it really comes through with how I interact with people. So, if I am feeling a certain 
way, it definitely [affects] how I communicate.” Implicit in these comments was the sense 
that internal changes in mood, and the sense of uneasiness it caused, made for difficult 
interactions that could cause further tension and impact the support they were able to receive 
from close others.

Overall, shifts in motivation and how participants related to, and experienced, important 
activities and people in their lives were central to their experiences of mental health 
symptoms. Though participants could easily identify these symptoms when they were 
present, and were aware of the impact they had on their day-to-day existence, addressing 
them required consistent effort and energy, which was particularly limited in periods when 
their symptoms were highly salient.

4.2  Mental health self-management practices

When recounting experiences of mental health self-management, participants described 
periods of poor mental health (characterized by active symptom management) relative to 
periods of good mental health (mental health maintenance). In periods of good mental 
health, participants more regularly engaged in activities that lifted their mood like exercise, 
connecting with others socially, and eating and sleeping well. The ease with which 
participants engaged in these activities was a sign of health, and critical to mental 
health maintenance. Periods of poor mental health, in contrast, were characterized by 
symptoms that made it difficult for participants to engage in these activities, and often 
required participants to take action in other ways to rebuild momentum. Specifically, 
participants described engaging in focused activities that brought them a sense of 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 11

accomplishment, productivity, or enjoyment as being most helpful when they experienced 
high symptomology.

Participant 10 describes their process of goal setting when they experience symptoms like 
this:

“On a recent day where I have been feeling down, I would say that the thing that I 
did to feel better – I would try to engage myself in some activity where I felt some 
sense of accomplishment to get me out of the doldrum that I was in.” (P10)

Similarly, Participant 4 described how setting incremental goals and providing self-
affirmations or rewards to reinforce her efforts was helpful:

“I won’t set up a big, hard goal for myself. I’ll just be like, ‘Okay, we’ll just 
reorganize the desk’ and then once I’m done with the desk I’ll be like, ‘Okay, you 
did so good. Great. Let’s go reorganize the bookshelves’ and then I’ll just do small 
goals like that and then a nice, little easy reward system to give myself perks or 
little pep talks like, ‘Hey, there you go. That’s what you did’ and then it helps 
motivate me to do the next item.” (P4)

Participants were generally in agreement that pursuing intentional practices that were goal-
oriented and attainable helped them restore good mental health in a period characterized by 
many symptoms. For example, Participant 6 described the importance of intentionality in 
pursuing meaningful activities like this: “It can be any activity, it just has to be something 
that ideally you’ve chosen actively to do.” What participants defined as meaningful activities 
varied, however. Some participants undertook task-oriented projects at home or work where 
it was easy to track progress. For example, Participant 4 described: “One of the things I like 
to do is either throw myself into work and/or a new project at home – it makes me feel good 
when I do something successfully or do it well.” While others set intentions to pursue new 
hobbies or do something they enjoyed. For Participant 7, that activity was learning to bake: 
“I’m learning how to make a cake. That is something that I wanted to achieve. I definitely 
want to be able to know how to make a cake. So, that is what I’m working on now.” 
Participant 1 described painting: “My painting. I would like to get that done.” Notably, 
these activities supported both the desire to intentionally do something for oneself and feel 
productive. Participant 1 described it like this: “I feel accomplished like I did something for 
myself that day. So, I would be feeling happy that I did that for myself.”

Though all participants described personal activities and goals as part of their self-
management of mental health symptoms, several also acknowledged the importance of 
checking in with others. Participant 4 described how her boyfriend provided accountability 
and validation when things weren’t going so well symptom-wise: “my boyfriend really helps 
me manage my mental health. He’ll be the one who will sometimes see how I am that day. 
If I’m really stressed or I’m really sad that day, he’ll be like, “Hey, let’s go on a walk or 
let’s do this or let’s do that” (P4). Participant 2 similarly described that he checked in with 
a therapist when he was in treatment and he purposefully scheduled “meetings with her 
just to keep myself accountable for my mental health.” Now that Participant 2 is no longer 
seeing therapist he described “self check-ins” as a way to take stock in his mental health. 
While social accountability was important for mental health management, and so was social 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 12

support. For example, Participant 10 described that talking to his wife helped him to: “think 
through why I was feeling the way I was. So, I think that too was probably the bigger help 
than just thinking through the tasks” (P10). Participant 8 similarly noted that she often felt 
better after “sharing with sister and husband.” Though participants reported strategies to 
manage their mental health alone, for some support from others was essential to motivate to 
follow through on activities and to help them reflect on their symptoms.

In general, participants’ experience of mental health included periods of low and high 
symptomology. When asked to reflect on activities that helped them overcome symptoms 
when they experienced more symptoms, or poor mental health, they described activities 
that provided them with a sense of accomplishment or enjoyment. Notably, these activities 
were highly variable across participants and differed from those that we typically attribute 
to mental and physical health like physical activity, eating behaviors, and sleep. Instead, 
they were “simplified,” shorter-term goals that provided participants with more immediate 
and tangible satisfaction. Family and significant others were also important to mental health 
maintenance – providing both accountability and support.

4.3  Experiences with self-tracking technologies

Participants were asked about their use of self-tracking technologies with smartphone or 
wearable sensors as part of their efforts to self-manage mental health symptoms. Though 
many participants described using devices like Apple Watch and Fitbit to track metrics 
related to physical health and well-being, very few endorsed the use of self-tracking 
technologies for mental health specifically.

In regard to physical health, participants most often described how they used and reflected 
on data from sensors embedded within technologies they used every day. They noted that 
these technologies helped them to identify and reflect on patterns, set goals, and send 
reminders to help them accomplish goals. For example, Participant 6 described how data 
from his wearable made him more aware of his poor sleep hygiene, and motivated him to set 
incremental goals to get to bed earlier:

“I think I use it to motivate myself to sleep better. I mean, without having 
documentation of it, I wouldn’t be able to say, “Oh, for the early weeks of January, 
I didn’t sleep that much,” or, “In the past week, I’ve been going to sleep past 4:00 
a.m. Let’s try to pull that back to 3:00 a.m. or 2:00 a.m. or let’s go to bed at 12:00 
every day now, and let’s see if I can keep that up.” (P6)

One of the features that facilitated self-tracking for Participant 6 was the way data was 
stored and easily accessible through his online calendar: “I can pull up my calendar and it’ll 
be there automatically just makes it seem nice and easy to track. So, it doesn’t require much 
effort at all.” Being able to visualize this information in a system that he already engaged 
with daily without requiring extra steps was important.

Participants also described and appreciated self-tracking technologies that reminded them 
to engage in activities that were beneficial, and/or provided insight into behaviors that felt 
actionable. For example, Participant 4 described:

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 13

“I recently got an Apple watch and it’s been really neat because it has … I got an 
older model but it still has all these really neat apps for tracking how much you 
move in a day and it’s cool because it reminds you every hour like, “Hey, you’ve 
been sitting down for too long. Stand up and stretch” So, I really like that. I’ve had 
it for six months now.” (P4)

These reminders helped several participants to maintain good habits targeting physical 
health, which may as a result help with mental health.

By contrast, very few participants described using self-tracking technologies for mental 
health. Of those who had used technologies to self-track mental health data in the past, 
journaling, mood tracking, or meditation apps were most common. However, all but one 
participant reported discontinuing use because the apps did not feel useful and they failed to 
capture nuance in participants’ experiences, or they did not provide workable insights. For 
example, Participant 6 described his experience using a journaling app like this:

“[It] wasn’t that useful for me, and then I just kind of fell off and didn’t use as 
much. It wasn’t as granular as I think I wanted it to be, and because it wasn’t 
granular, I couldn’t picture a situation in which looking back on it would be useful 
for me, because I would always pick “today was okay” versus “today was good”, 
and there’s nothing to correlate with that, so it wasn’t personally useful.” (P6)

This lack of perceived usefulness was a shared concern across several participants with prior 
self-tracking experience. Participant 5 described a mood tracking app like this:

“I felt like I was putting the same emotion every day. Sometimes [I found it 
helpful], but not really because I felt like I was just being the same emotional 
person that I am all the time and it’s just reminding me that I’m being the same 
emotional person every day.” (P5)

In this participant’s experience, the app emphasized a lack of change in symptoms rather 
than offering actionable strategies or insights to better support her mental health, which, 
ultimately, made her feel worse and led her to disengage with the app.

Boredom and lack of interest were other attitudinal barriers to mental health self-tracking. 
When discussing the mood tracking app mentioned above, Participant 5 said: “I’ll just end 
up getting bored of it so I’ll stop doing it.” Similarly, Participant 10 noted that his Apple 
Watch had some features that could be of value to mental health: “it has this breathing thing 
on it – I used to have it scheduled when I first got my watch,” but that he hadn’t used it on 
over a year because he tends to get “caught up in whatever I’m doing and I don’t prioritize.”

As mentioned, one exception to the negative experiences most participants described 
regarding prior mental health tracking, was Participant 2 who self-described as an “app 
girl.” She was currently using mediation apps to help her with sleep and anxiety, and her use 
increased through the pandemic: “There are even five to ten minute ones during the day that 
you can just use for yourself to calm down, and feel a little re-centered, and refocused.” She 
most appreciated the variety of meditations offered and the ability to easily access and use 
them throughout her day. Rather than manually tracking symptoms, the systems Participant 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 14

2 described involved tracking engagement in activities (e.g., meditations) and collecting 
passive behavioral data for sleep.

In sum, participants’ prior experiences with self-tracking varied. Most participants reported 
some form of self-tracking with smartphone or smartwatch sensor data for physical health, 
but the majority of participants were not currently engaged in self-tracking for mental 
health. Participants that had prior experiences with self-tracking technologies for mental 
health, largely discontinued use because the tools they used were not perceived to be useful, 
suggesting the importance of re-evaluating participants’ wants and needs for self-tracking 
for future design.

4.4  Desired self-tracking for mental health

Most participants expressed interest in, or curiosity about, a self-tracking tool that could help 
them better manage their mental health symptoms. They were particularly interested in a 
smartphone-app that could: (1) quantify the good things that they do for themselves daily, 
and (2) help them discern patterns that they could change to improve their mental health 
when they experienced many symptoms.

Though participants could easily identify symptoms associated with poor mental health, 
it was difficult to initiate activities to improve mental health, and to recognize the small 
things they do to improve mental health day-to-day. Participants imagined an app feature 
that would help them to take stock of the small things they do to improve mental health, and 
reflect on this data in aggregate. For example, Participant 2 imagined a way for her phone to 
help her to reflect on her weekly accomplishments:

“I think sometimes it would be nice to – if I had an option of – like, if my phone 
just popped up, and was like, “What did you do to take care of yourself today?” 
And, I could be like, “Oh, I did this.” And, then, if I get to see I’ve done x, y and z 
for the past week, like, wow That’s cool.” (P2)

For this participant, being able to see what they did to care for themselves on a weekly basis 
provided evidence and needed validation for their efforts. Participant 2 goes on to describe:

“I think it’s just another way of laying out the progress, and taking care of myself 
that I do. I feel like a lot of times, I don’t give myself enough credit for what I do 
for myself. So, getting to see it reflected on a table, or something would be effective 
for me.” (P2)

Other participants similarly described a desire for brief interactions with a DMHI through 
a prompt or nudge that would require little daily effort. Participant 4 mentioned “if there 
is something as simple as my pill app with clicking and stuff like that, I think that would 
be really good for being a “How am I feeling today?” tracker.” Importantly, check-ins like 
this were perceived to be helpful if they increased awareness of moments when they pursued 
activities that made them feel good and could facilitate reflection to discern patterns that 
were unhelpful.

Identifying potentially unhelpful patterns was important to many participants, but only if the 
app also provided insights on how to make changes to prevent further declines in mental 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 15

health. Participant 3 thought that an app may be able to “help me understand what was going 
on in my brain, but then also, the best way to go about fixing it if there were things that 
needed to be fixed.” Participant 3 similarly imagined that a self-tracking app would help 
them to take a “look at the grand scheme of things” and highlight things that accumulate 
over time. Another participant had a similar reflection, describing that an app could help her 
to identify common triggers (or situations that were bad for their mental health) so she could 
better understand them and intervene. Participant 9 commented that she’d like to see: “how 
many times that actually my triggers kicked in and I was able to balance it out. I know that’s 
a trigger. Now, what did I do? I know that’s a trigger. So, why am I frustrated? And why do I 
let that frustrate me? That’s what I would learn if I had history” (P9).

Interestingly, most participants wanted to notice or reflect on the accumulation of many 
things over time. While it felt comfortable to reflect on proactive activities for mental health 
daily, they were more interested in reflecting on actions, behaviors, and experiences that 
may contribute to more symptoms historically. In this way an app could be useful to prevent 
declines in mental health through increasing one’s awareness and knowledge of patterns.

While many participants were interested in the potential usefulness of an app for mental 
health, several were more ambivalent either due to past experiences with ineffective apps, 
or uncertainty around what to track. For example, Participant 10 described that couldn’t 
imagine what to track:

“I just don’t know what the right metric is for me to pay attention to. Or I don’t 
know what should I be doing better to improve it? So, I don’t know, mental health 
is so hard to nail down, so you either feel a certain way or you don’t, broadly 
speaking. So, I just don’t know if you can unpack those steps and there’s some kind 
of outcome associated with it that you can track or activities, then maybe, yeah.” 
(P10)

Despite this, Participant 10 was interested in tracking activities over time in service of 
pattern recognition or uncovering “steps” they could take to improve their well-being.

Although most participants were not using smartphone or wearable sensor technologies to 
self-track mental health symptoms, they expressed interest in tracking behavioral markers 
of mental health if they could quantify the good things they do for themselves and make 
patterns salient for change and/or intervention. Notably, participants were more interested 
in tracking things that were within their control (activities, tasks), and less interested in 
tracking things that were perceived to be outside of their control (heart rate, quality of sleep).

4.5  Comfort with, and expectations for, sharing data with providers

As mentioned one common problem with self-tracking technologies is the interpretability 
of information to direct action. One way around this is to deliver feedback to providers 
who can assist users in interpreting data and provide recommendations. To this end, we 
wanted to get a sense of how comfortable participants would be with sharing information 
from the self-tracking tool with their provider, as well as what they expected from sharing 
that information. Interestingly, despite being recruited from primary care settings, most 
participants reported that their primary care providers did not speak with them in depth 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 16

about their mental health. A few participants mentioned that their providers asked screening 
questions without much follow-up, and several mentioned being unsure whether their 
provider would be the right person to discuss mental health with. For example, Participant 7 
described that when providers “don’t ask questions, it’s very uncomfortable for you to just 
ask – how you’re supposed to manage your mental health, what activities can you sort of 
engage in so that you’re able to better your mental health?”

When participants were asked if they would be comfortable sharing information gathered 
from a self-tracking DMHI with their healthcare provider, most described that they would 
be, and they had specific ideas about how that information may be used. For some 
participants, they imagined that sharing mood or passive sensor data with their provider 
would help the provider to alert them to declining mental health, and provide guidance on 
problem solving. For example, Participant 9 imagined that providers would be “better able 
to evaluate your well-being… just like any other test. It’s like, ‘These numbers don’t look 
good.’” Moreover Participant 9 described:

“[A provider could] help you know that you’re either near the end of your rope or 
you about to get to the end of your rope, I would think. Or they want to help you 
not get to the end of your rope, so they could have a picture that they could see 
where you’re headed to and help you see if you don’t know you’re getting there.” 
(P9)

Participant 6 imagined sharing data may result in better treatment. They described 
“By sharing it with my PCP or healthcare providers, they have additional insight and 
theoretically would be able to provide me more personalized treatment or response, and 
there’s nothing indicating harm to myself or others” (P6). In these cases, the provider’s 
role was to monitor the data, interpret it, notice patterns, and provide recommendations to 
improve patients’ mental health.

By contrast, other participants imagined that sharing data could help them to initiate 
conversations with their primary care provider. Participant 8, for example, described that 
it had been difficult for them to have conversations about mental health with their provider, 
and that they often felt like conversations about mental health were not welcomed: “it’s 
hard to be – completely frank with your healthcare provider” and “I get the feeling that 
the healthcare providers don’t have time for – to be with my emotions, they just talk about 
my emotions.” In cases like this, data was seen as a catalyst to both initiate and legitimize 
conversations about mental health symptoms. Similarly, Participant 3 hoped that sharing 
data from a smartphone app might also help them to get better support from their provider 
because they had trouble describing their symptoms: “I would be very willing to share that 
because sometimes it’s hard to explain it, just because you don’t know how to explain it or 
because you don’t want to explain it, even though you want the help” (P3).

Finally, participants were unanimous in their belief that if they shared information with 
their provider there would need to be transparency in both how it would be used, and 
how it would benefit them. On this, Participant 10 described: “I’d be comfortable sharing 
information with a healthcare provider if there’s some kind of outcome for me.” Moreover, 
participants were most comfortable sharing information if they knew who would have access 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 17

to it and how they would use that information. Participants described some concerns around 
specific data such as search behavior (which felt too personal) and greater comfort with 
other data, like exercise, mood, and activity data.

In sum, participants were interested in sharing data from a self-tracking DMHI with their 
provider if it would benefit them directly. They imagined that sharing data would help them 
to initiate conversations, provide their clinician with a more accurate understanding of their 
symptoms, and enable close monitoring for changes in treatment planning. This receptivity 
to sharing data provides some initial evidence for the possible integration of a self-tracking 
DMHI within primary care.

5  DISCUSSION

There is a need to bridge gaps in services between screening in primary care settings 
to acquiring mental health treatment. A DMHI deployed at this critical juncture, as part 
of self-management in early stages of stepped care, has the potential to provide evidence-
based resources to individuals who may otherwise go without care. To date, DMHIs for 
self-management often involve manual self-tracking, however very little is known about 
how DMHIs designed with automated tracking can best support patients’ existing self-
management processes. In the current study, we sought to explore this potential through 
gaining an understanding of the self-management practices of patients recruited from 
primary care settings with symptoms of depression and anxiety, their needs and preferences 
for self-tracking technologies for mental health management, and their current and desired 
use of smartphone and wearable sensors to support their mental health journeys. Though 
our findings highlight the potential utility of self-tracking technologies to support people 
in contact with primary care providers, they also call attention to some misalignments 
in current efforts to leverage sensor data in DMHIs, and our participants’ expressed 
needs. Additionally, consistent with past literature, we also found that participants were 
overwhelmingly supportive of sharing data with providers if it would directly benefit them 
[46, 100] underscoring the potential future integration of a self-management tool within 
clinical services, if and when a higher-intensity treatment is indicated.

In the discussion, we first describe technology needs supported by our findings and 
highlight some proposed, and new, solutions. Recognizing that our participants struggled 
with motivation and action as part of their symptoms of depression and anxiety, along 
with the consistent finding that DMHIs often have low engagement [92], we focused on 
self-management needs with an eye towards addressing these concerns if they should arise 
with a stepped care approach. We thus introduce an opportunity for the HCI community 
to extend focus to wraparound services alongside the self-management technology, as a 
means for healthcare providers to support use of the DMHI, and provide light-weight care 
aligned with the data. We argue that both technology and service designs may be necessary 
to sustainably bridge gaps in our healthcare system.

5.1  Self-management technology needs

As in other HCI studies, our findings underscored the need for a DMHI for primary 
care patients to support the personalization of goals, activities, and feedback, and to 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 18

accommodate shifts in user needs overtime. Consistent with both clinical understandings 
of the chronic and episodic nature of depression and anxiety [24] and prior research on 
depression from the HCI community [50], our participants characterized their experiences 
of mental health symptoms dichotomously. Specifically, they referred to periods of low 
and high symptomology, which corresponded to mental health maintenance and active 
symptom management. Participants had good insight on the types of activities that 
supported mental health when they were feeling well (e.g., exercise, eating and sleeping 
well), and many of these activities corresponded to behavioral markers captured by sensors 
in self-tracking tools for physical health. Yet, when reflecting on the things they do to help 
themselves when they actively manage symptoms, participants described needing to shift 
from their usual routines to accommodate changes in energy, focus, and motivation. In these 
periods, participants reported that smaller, focused tasks helped because they were more 
manageable and brought them a sense of enjoyment or accomplishment. In the following, 
we aim to translate the contrasting needs and activities perceived to be supportive when 
participants were maintaining mental health versus managing symptoms into considerations 
for technology design.

5.1.1  Mental health maintenance versus active symptom management.—
During mental health maintenance - when participants experienced few symptoms - little 
support was perceived to be necessary from a sensor-based self-tracking technology for 
mental health. Some participants already described using tracking tools, like Fitbits or 
smartwatches, to monitor and reflect on their physical health. For most, this was a way for 
them to keep track of physical activity or sleep patterns, and the ubiquity of these devices 
provided a subtle reminder to stay active and engage in healthy sleep hygiene. Though 
participants did not believe a tracking tool could offer more support during these periods, 
they consistently reported a desire to identify patterns in their mental health symptoms and 
to learn about potential triggers in order to take preventive action if declines in mental 
health were forecasted. These goals - to monitor their health and learn about triggers – 
commonly come up in work with people managing chronic conditions [60]. Some of this 
work has found that learning goals require more effort, and more intensive data collection, 
than monitoring goals [88]. Knowing that participant energy was limited in periods of high 
symptoms, it may be most feasible to leverage periods of good mental health to learn, while 
simultaneously collecting data for future forecasting in an unobtrusive way that would place 
little burden on the user. In line with prior research, our work underscores the opportunity to 
leverage periods with higher energy and motivation for the future [48, 50].

During active symptom management participants could envision a greater need for 
support from a self-tracking technology. When actively managing symptoms, participants 
focused on shortterm, well-defined activities that were perceived to be within their control. 
Despite knowing that small, manageable goals were helpful when symptom load was 
high, participants expressed difficulty following through on intentions and struggled to 
acknowledge their efforts and successes on a daily basis. Participants imagined that a 
self-tracking technology could help them to follow through on their intentions and take stock 
of their efforts to manage mental health through regular check-ins and validating messages. 
Interestingly, in this way, the imagined DMHI served a similar role to trusted peers and 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 19

significant others - as a resource to draw attention to symptoms, offer solutions, and keep 
them accountable. The social nature of behavior change and goal setting has been observed 
in prior HCI studies [2, 56] and studies specifically focused on the self-management of 
depression [10, 11]. However, here it seems that patients imagined the DMHI providing 
opportunities for self-guided reflection and action based on the collection of data. From the 
participants’ perspectives, recording and reflecting on these small steps had the potential 
to reinforce self-efficacy and prevent them from feeling like they were “wasting time.” 
Notably, this inclination to set intentions and pursue activities that were pleasurable or 
provided a sense of accomplishment during periods of high symptomology, aligns with 
behavioral activation - an empirically supported treatment that teaches patients to monitor 
mood and daily activities to identify things that bring them pleasure to increase positive 
interactions, and to increase those activities [22]. Treatment plans for behavioral activation 
are goal-focused, highly customizable and among the key components are monitoring 
and scheduling pleasurable activities. However, because the types of activities that were 
pleasurable, and supportive, to participants shifted with with ebbs and flows in their 
symptoms, DMHIs incorporating behavioral activation should be tailored to users’ symptom 
presentations.

In sum, our findings suggest that during periods of mental health maintenence (low 
symptomology), patients may find more value in engaging with patterns surfaced from 
sensor data, while during periods of active symptom management, their needs would be 
better met through a DMHI providing guidance over education. There are at least two key 
design implications for the self-management DMHI for patients with depression and anxiety. 
The DMHI would need to: (1) accommodate shifts in needs over time and in response to 
symptoms and (2) identify and support personalized goals, activities, and feedback.

5.1.2  Using smartphone and wearable sensor data to accommodating shifts 
in needs over time and in response to symptoms load.—Smartphone and 
wearable sensor data may be particularly useful to detect shifts in needs over time. As our 
interviews highlight, symptom presentation was characterized by different needs including 
shifts in what activities, levels of support, and goals (e.g., monitoring, learning, activating) 
were desired and perceived to be most useful. Importantly, the ways in which smartphone 
sensor data could facilitate these needs also differed. In digital mental health, sensor data 
has typically been used to send users insights during periods of poor health in an effort to 
empower them to make changes that support health and well-being. In most cases, these 
data are then summarized and displayed back to users as an association or correlation to 
mental health status. Counter-intuitively, however, behavioral markers from sensor data were 
perceived to be most valued by participants when they were maintaining mental health. 
Indeed, our participants described that in past experiences with self-tracking technologies, 
direct feedback from sensor data was not appreciated during periods of active symptom 
management, in part, because the user was already acutely aware of the behavioral markers 
sensors often capture (e.g., sleep, exercise). Feedback generated by sensor data was also 
perceived to be out of reach and outside of their immediate control because decreased 
motivation, fatigue, and anxiety made it more difficult for users to engage in activities, like 
physical activity. This is consistent with a trend in the broader literature around how the 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 20

feedback users receive from self-tracking technologies can be discouraging to users who 
have chronic conditions and are engaging in symptom management [3, 65].

While the mismatches in data that automated self-tracking systems commonly capture and 
participants’ individual needs and goals are unsurprising, here we find that mismatches are 
particularly problematic during periods when users are actively managing symptoms and in 
need of the most support. This underscores the potential importance of reconsidering the 
role of sensor data in DMHIs for this population based on the data’s utility in periods of 
high versus low symptomology. For example, sensor data may be particularly helpful to 
deliver feedback and visualizations when users are maintaining their mental health, but play 
a less prominent role when they are actively managing symptoms. Because sensor data are 
dynamic by nature, they also provide opportunities to detect changes in behavioral markers 
related to mental health which can automatically signal the need for a different configuration 
of the DMHI content or functionality, or a new protocol to support user needs. If these shifts 
cannot be feasibly detected purely through sensing, DMHIs nonetheless need to strike an 
appropriate balance between passive and active tracking to reduce participant burden while 
enabling accurate detection [15]. To identify ways design could address the challenges we 
identified a need for tools to support personalization and an evolution in needs [29, 88].

Identifying and supporting personalized goals, activities, and feedback.

5.1.3 
—The HCI community has discussed approaches to elicit personalized activities and goals 
from technology users, as well as how to support users’ evolving goals over time. While 
there has been extensive conversation and consideration of these topics, we still have many 
mental health self-tracking technologies that fail to meet user needs, and, in some cases, 
that exacerbate user symptoms [28, 29, 46]. We believe this may be, in part, because our 
orientation and efforts around DMHIs have largely been focused on their value to track and 
predict symptoms, with less attention to how they can support individuals to pursue activities 
of value in their daily life.

Goal directed self-tracking is an approach that focuses on matching user goals with the 
underlying data collected by self-tracking tools and can easily be used to encourage users 
in pursuit of behavioral activation [88]. This approach was developed in the context of 
migraine management, which like depression and anxiety, is often a chronic condition 
requiring periods of maintenance and active symptom management. Migraine experiences 
are also highly variable between individuals, and symptoms can be triggered by physical, 
psychological or emotional factors making personalized treatment necessary. To address 
the complexity underlying chronic illnesses, goal-directed self-tracking suggests that tools 
should be designed to recommend what, when, and how to track goals based on what is 
already known about the condition, while also being flexible enough to support users in 
tracking activities or behavioral markers that they find to be most useful. Giving the user 
agency over the types of data they track (e.g., activities, symptoms, moods, sleep), and 
when, may help address some of the between-participant variability we observed.

Interestingly, in studies of migraine management, Schroeder and colleagues [88] found that 
user goals typically fell into three main categories: to learn about symptoms, to predict 
symptoms, or to monitor symptoms. Each of these goal categories was associated with a 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 21

different level of granularity and effort in tracking activities. Based on these findings, a 
prototype was developed with question-based prompting as well as a “help me” button 
scaffold users in the goal-setting process by suggesting specific behavioral markers to track 
based on whether the user’s goal was to learn, predict, or monitor symptoms. Because 
what was perceived to be supportive by our participants during periods of active versus 
management would likely require different ways of capturing and aggregating data, a similar 
model could assist users in personalizing the self-tracking technology for their unique 
mental health symptoms. For example, based on our participants’ comments, a range of 
continuous data describing patterns and enabling users to learn about correlates to mental 
health over a longer time frame may be more desirable when participants are maintaining 
mental health and interested in monitoring, which is similar to the feedback they’d receive 
from Fitbit and smartwatch applications.

By contrast, during periods of active management, users may prefer a simple checklist of 
activities or tasks to be completed in pursuit of accomplishment, or enjoyment. The DMHI 
could make suggestions aligned with a behavioral activation approach, but ultimately allow 
users to make their own selections based on their desired outcome. Most importantly, sensor 
data can play a key role in re-configuring the technology to meet the changing needs of the 
user.

Though personalization is often desired, it often requires heavy effort from users. One way 
to simplify such a system may be through semi-automated tracking [15]. Similar to what 
some of our participants described in their use of technologies for physical health, a wrist 
wearable could automatically prompt the user to do some valued activity (e.g., painting) and 
detect how much time was spent on that activity. In this way, the user would only need to 
manually input how they felt after completing the activity, reducing the burden of tracking 
without compromising on data quantity or quality Alternatively, in line with prior work, 
participants of our study described utilizing their peer support system to suggest activities 
for them to do during periods of high symptomology, suggesting that it may be feasible for 
those that have a close network to depend on [11].

In sum, using a goal-oriented self-tracking approach to the design of DMHIs can increase 
the level of personalization, and a semi-automated approach can balance manual efforts with 
passive tracking to ensure the burden on the user is manageable. This approach affords great 
flexibility as the DMHI could come with suggested parameters that can be modified based 
on user needs, or the user could walk through the set-up with their healthcare provider.

5.2  Stepped Care Service Needs

In the prior section, we discussed meeting participants’ needs through designing a self-
guided intervention, which is a natural first step in a stepped care model of treatment 
delivery since it is scalable and requires no, or little, resources from healthcare systems. 
However, our participants described symptoms that affected motivation and ability to engage 
in activities that they know are useful to their mental health maintenance. This, coupled with 
the longstanding concerns around DMHI engagement [93], make it imperative for us, as 
designers and researchers, to explore ways of supporting user engagement with treatment. 
HCI researchers have typically approached issues of engagement through identifying unmet 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 22

user needs and evaluating the usability and usefulness of a tool. However, as we reflected 
on our participants’ experiences and how to best address their needs, it became clear that 
it is likely not enough to design a tool for self-management, without also considering ways 
of sharing insights with a care supporter. In the clinical literature, it is common to consider 
technologies as services rather than products [74], which require additional support for 
delivery and sustainment. When it comes to DMHIs within HCI however, there has been 
little attention on what additional support may be needed to ensure engagement with the 
DMHI in the wild.

Our participants’ willingness to share data with their providers opens up opportunities to 
design for providers’ (or other care supporters’) access to data to support user engagement if 
more intensive intervention is indicated. In this case, rather than designing new technologies, 
we argue that this requires designing new services - which we call “wraparound services” 
–since they are meant to support the patient in using, and interpreting data from, the 
intervention with the ultimate goal of increasing clinical gains. In the sections to follow, we 
outline an opportunity for HCI researchers to extend design thinking to infrastructure needs 
and wraparound services and see this extension in thinking as critical to improve real-world 
use of technologies.

5.2.1  Wraparound Services.—Wraparound services originated in community-based 
mental health programs as a way to meet the complex needs of children in treatment 
and their families [9, 96]. Over the years, wraparound services have come to refer to 
services that support the client in attending and getting the most out of treatment, including 
transportation, childcare, and legal services, for example. Thinking about wraparounds in 
the DMHI context may help shift focus from an individual level – designing and evaluating 
a product for an individual/population – to a systems level which considers strengths and 
challenges individuals are presented with, which may ultimately impact their ability to use 
and reap benefit from a technology. For example, participants were particularly concerned 
about the interpretability of DMHI data, and imagined that their provider could help provide 
them with a critical translation of data into actionable feedback. In this way, the provider 
may become part of the DMHI, an additional service needed to ensure clinical gains.

Studies in the clinical sciences literature have consistently found that DMHIs are more 
efficacious at improving mental health outcomes when they involve low-intensity human 
support [44, 57]. We argue that by considering the design of services as adjuncts to 
technologies, researchers may be better able to serve the communities and populations that 
they design for, in the contexts where the technology is meant to be deployed. We briefly 
define low-intensity coaching as one example of a valuable wraparound service, that could 
be used as a “step-up” from self-management, and could increase data interpretability and 
communication channels within primary care. Then we discuss implications for this focus 
and feasibility moving forward.

5.2.2  Low-intensity Coaching.—Low-intensity coaching is to facilitate the use of 
a supportive technology and provide the user with a sense of accountability. Coaching 
protocols vary, but often involve a motivational interviewing approach with goal setting and 
encouragement that accounts for the uniqueness of patient needs [4, 53, 67, 89]. Coaches 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 23

help patients translate findings into actions and serve as a source of motivation and escalate 
patients to higher levels of care. They also work with the patient to develop a set of tasks 
or activities in support of reaching their goals and can monitor data to detect a need to 
shift goals to make them more manageable, and adapt feedback so it is more meaningful, 
when symptoms increased [1]. This is most often enabled with a coach facing tool (e.g., 
a portal) that provides coaches with incoming data and diagnostics. Being able to discuss 
mental health and receive feedback from a provider was appreciated by participants in our 
study. Designing technologies that enable two-way communication and passive monitoring 
can enable both self-management and clinical monitoring to prevent symptoms worsening 
and potentially acute need for visits.

5.2.3  Challenges and Future Directions.—If we are to make a difference in mental 
health conditions at a population level, and reduce burden on an overtaxed healthcare 
system, we must think more deeply about the infrastructure needed to deliver evidence-
based resources in a way that is expeditious and efficacious. DMHIs offer a potential 
solution but to make measureable gains we will need to address issues that come 
with DMHIs, including engagement [68]. Low-intensity coaching works well to improve 
engagement, and is feasible, in research environments as evidenced through many trials 
with different coaching protocols. Coaches often receive minimal training on the technology 
and strategies to increase engagement, troubleshoot, motivate users and identify barriers to 
use. Hiring an external coach, however, comes at a cost and may not be practical as a first 
step in care within primary care settings. Indeed, designing for intervention deployment 
in primary care settings is a challenge since digital tools rarely fit within providers’ 
existing workflows and require extra labor, training, and personnel. We suggest that using 
a completely self-guided self-management intervention as a first step in primary care, and 
supported self-management with low-intensity coaching as a next step for patients who do 
not respond, may be more feasible.

Dissemination strategies must also be at the forefront of designers’ minds in DMHI. One 
barrier to implementing DMHIs more broadly is that they are not yet reimbursable. Indeed, 
most DMHIs are on a direct-to-consumer payment model, requiring users to subscribe 
to the service [81], which limits the user base to those who can afford the service [89]. 
Proper implementation within primary care would likely require users to pay for services, 
or for broader structural changes. Payment models that are more similar to traditional 
healthcare interventions, with reimbursement for human-in-the loop time would make 
these interventions more accessible and scalable. Additionally this would resolve some of 
the issues with integrating DMHIs in healthcare settings, since this would provide some 
financial incentive for training in DMHI and enable clinicians to bill for their time [8, 71].

Another way to make coaching financially viable at scale may be to use a paraprofessional 
model of service delivery like the crisis textline or to have other supportive peers or family 
members serve as coaches. Crisis lines are able to support millions of people in crisis year 
after year through volunteers who provide basic support and safety planning to individuals 
who call and/or text in [40]. Interactions through crisis lines are also typically under 30 
minutes, and crisis counselors keep a detailed record of each call which they can then 
reference for repeat callers. Low-intensity coaching similarly requires very minimal contact 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 24

with users but potentially over a longer period of time (e.g., several months). A related 
opportunity that may fit within patients existing self-management of systems, could be for 
patients to elect an individual in their life to serve as a coach, or offer check-ins as a way 
to stay on track towards their mental health practices and goals. Other studies in HCI have 
similarly discussed the value of peers and other social actors for behavior change, and have 
offered solutions such as “peer-sourcing” or peer-driven planning where peers provide direct 
feedback on strategies for change. [2, 56]. Given that participants in our study mentioned 
that family members and significant others were frequently a source of accountability for 
them in symptom management, this may have significant potential. In sum, leveraging a 
model like crisis line or peer-based support for DMHIs meant to bridge a gap in healthcare 
services, may have significant potential.

We have suggested that in order for the HCI community to make an impact on real-world 
mental health conditions we need to think more about building low-intensity digital 
treatment options into existing services, and, as part of this, developing services that enhance 
technology use and provide more intensive support if, or when, indicated. In many ways, 
how to do this effectively in the current environment is an open question but one that 
the HCI community has a stake in, and is well-positioned to contribute meaningfully to. 
Facilitating engagement with technologies will likely require creating novel pathways to 
share with providers, and structural changes. We offer low-intensity coaching as one service 
that can enhance engagement and potentially be integrated into healthcare systems as a 
stepped care option. Future work will need to extend these conjectures to get input from 
clinical stakeholders to determine the ways in which they would like to, or could feasibility, 
be involved in the use of DMHIs at this point of care.

6  LIMITATIONS

This study has several limitations. While we attempted to recruit a representative sample 
from primary care, we recognize that those who engage in research may still have been more 
motivated than individuals who choose not to engage in research. We also have relatively 
small (n=10) and predominantly female sample, which is common in mental health research, 
but speaks to the need to better engage male-identified patients. It may be necessary to 
tailor recruitment language to male audiences or to pause recruitment of female participants 
and leave recruitment open to male participants longer in future studies. Additionally, our 
sample endorsed relatively low symptomology at the time of enrollment and most did not 
have prior experience receiving clinical mental health care. Though this can be a strength 
in that it enabled them to reflect retrospectively on periods of more symptomology with the 
mental health literacy of the general population, it is also possible that a sample with greater 
symptom severity or the experience of clinically effective mental health treatment methods 
would endorse different needs. Finally, while we discuss design for the primary care context 
we focused exclusively on patient perspectives. Provider perspectives should be explored in 
future work.

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

7  CONCLUSION

Page 25

In this study, we interviewed 10 individuals with symptoms of depression and anxiety as 
identified through primary care. We aimed to understand how a self-tracking technology 
may fill a gap in care by providing support to individuals who are not treatment engaged, 
in the period between diagnosis and treatment, where many get lost. We used a stepped 
care framework as inspiration for the delivery model – where a self-management technology 
could be augmented by additional supports to deliver evidence-based support in the most 
efficacious and expeditious way. Based on our participants’ experiences of managing mental 
health symptoms, we argued that the way HCI has typically approached, and designed, 
sensing technologies for affective symptoms (depression, anxiety), in particular, does not 
closely align with this population’s needs. What became clear in our conversations with 
participants was the need to design for their complex needs in a more nuanced way. To do 
so, we argue that this may mean reconsidering the use of sensor data within DMHIs, and 
thinking more deeply about the additional services that might be needed to properly augment 
DMHIs, and have a lasting impact on mental health overtime. We describe implications for 
design drawing from both clinical and HCI literatures.

ACKNOWLEDGMENTS

This work was funded by the National Institute for Mental Health (T32MH115882, P50MH119029, and 
K08MH125069).

REFERENCES

[1]. AGAPIE ELENA, AREÁN PATRICIAA, HSIEH GARY, and MUNSON SEANA. 2022. A 

Longitudinal Goal Setting Model for Addressing Complex Personal Problems in Mental Health. 
(2022).

[2]. Agapie Elena, Colusso Lucas, Munson Sean A, and Hsieh Gary. 2016. Plansourcing: Generating 
behavior change plans with friends and crowds. In Proceedings of the 19th ACM Conference on 
Computer-Supported Cooperative Work & Social Computing. 119–133.

[3]. Ancker Jessica S, Witteman Holly O, Hafeez Baria, Provencher Thierry, Van de Graaf Mary, and 
Wei Esther. 2015. “You get reminded you’re a sick person”: personal data tracking and patients 
with multiple chronic conditions. Journal of medical Internet research 17, 8 (2015), e4209.

[4]. Andersson Gerhard, Bergström Jan, Buhrman Monica, Carlbring Per, Holländare Fredrik, 

Kaldo Viktor, Nilsson-Ihrfelt Elisabeth, Paxling Björn, Ström Lars, and Waara Johan. 2008. 
Development of a new approach to guided self-help via the Internet: The Swedish experience. 
Journal of Technology in Human Services 26, 2-4 (2008), 161–181.

[5]. Archer Janine, Bower Peter, Gilbody Simon, Lovell Karina, Richards David, Gask Linda, Dickens 
Chris, and Coventry Peter. 2012. Collaborative care for depression and anxiety problems. 
Cochrane Database of Systematic Reviews 10 (2012).

[6]. Aung Min Hane, Matthews Mark, and Choudhury Tanzeem. 2017. Sensing behavioral symptoms 

of mental health and delivering personalized interventions using mobile technologies. Depression 
and anxiety 34, 7 (2017), 603–609. [PubMed: 28661072] 

[7]. Ben-Zeev Dror, Scherer Emily A, Wang Rui, Xie Haiyi, and Campbell Andrew T. 2015. Next-
generation psychiatric assessment: Using smartphone sensors to monitor behavior and mental 
health. Psychiatric rehabilitation journal 38, 3 (2015), 218. [PubMed: 25844912] 

[8]. Berry Natalie, Bucci Sandra, Lobban Fiona, et al. 2017. Use of the internet and mobile phones for 
self-management of severe mental health problems: qualitative study of staff views. JMIR mental 
health 4, 4 (2017), e8311.

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 26

[9]. Bruns Eric J and Walker Janet S. 2010. Defining practice: Flexibility, legitimacy, and the nature 
of systems of care and wraparound. Evaluation and Program Planning 33, 1 (2010), 45–48. 
[PubMed: 19589600] 

[10]. Burgess Eleanor R, Reddy Madhu C, and Mohr David C. 2022. I Just Can’t Help But 

Smile Sometimes”: Collaborative Self-Management of Depression. Proceedings of the ACM 
on Human-Computer Interaction 6, CSCW1 (2022), 1–32.

[11]. Burgess Eleanor R, Ringland Kathryn E, Nicholas Jennifer, Knapp Ashley A, Eschler Jordan, 
Mohr David C, and Reddy Madhu C. 2019. “I think people are powerful” The Sociality of 
Individuals Managing Depression. Proceedings of the ACM on Human-Computer Interaction 3, 
CSCW (2019), 1–29.

[12]. Burns Michelle Nicole, Begale Mark, Duffecy Jennifer, Gergle Darren, Karr Chris J, Giangrande 
Emily, and Mohr David C. 2011. Harnessing context sensing to develop a mobile intervention for 
depression. Journal of medical Internet research 13, 3 (2011), e1838.

[13]. Caldeira Clara, Chen Yu, Chan Lesley, Pham Vivian, Chen Yunan, and Zheng Kai. 2017. Mobile 
apps for mood tracking: an analysis of features and user reviews. In AMIA Annual Symposium 
Proceedings, Vol. 2017. American Medical Informatics Association, 495.

[14]. Canzian Luca and Musolesi Mirco. 2015. Trajectories of depression: unobtrusive monitoring of 
depressive states by means of smartphone mobility traces analysis. In Proceedings of the 2015 
ACM international joint conference on pervasive and ubiquitous computing. 1293–1304.

[15]. Choe Eun Kyoung, Abdullah Saeed, Rabbi Mashfiqui, Thomaz Edison, Epstein Daniel A, 

Cordeiro Felicia, Kay Matthew, Abowd Gregory D, Choudhury Tanzeem, Fogarty James, et 
al. 2017. Semi-automated tracking: a balanced approach for self-monitoring applications. IEEE 
Pervasive Computing 16, 1 (2017), 74–84.

[16]. Chowdhury Taskina and Champion Jane Dimmitt. 2020. Outcomes of depression screening for 

adolescents accessing pediatric primary care-based services. Journal of Pediatric Nursing 52 
(2020), 25–29. [PubMed: 32135479] 

[17]. Church Karen, Hoggan Eve, and Oliver Nuria. 2010. A study of mobile mood awareness and 
communication through MobiMood. In Proceedings of the 6th Nordic conference on human-
computer interaction: extending boundaries. 128–137.

[18]. Churchill Richard, Khaira Mandip, Gretton Virginia, Chilvers Clair, Dewey Michael, Duggan 
Conor, Lee Alan, Antidepressants in Primary Care (CAPC) Study Group, et al. 2000. Treating 
depression in general practice: factors affecting patients’ treatment preferences. British Journal of 
General Practice 50, 460 (2000), 905–906.

[19]. Copeland William E, Wolke Dieter, Shanahan Lilly, and Costello E Jane. 2015. Adult functional 
outcomes of common childhood psychiatric problems: a prospective, longitudinal study. JAMA 
psychiatry 72, 9 (2015), 892–899. [PubMed: 26176785] 

[20]. Cornet Victor P and Holden Richard J. 2018. Systematic review of smartphone-based passive 
sensing for health and wellbeing. Journal of biomedical informatics 77 (2018), 120–132. 
[PubMed: 29248628] 

[21]. Cuijpers Pim, Berking Matthias, Andersson Gerhard, Quigley Leanne, Kleiboer Annet, and 

Dobson Keith S. 2013. A meta-analysis of cognitive-behavioural therapy for adult depression, 
alone and in comparison with other treatments. The Canadian Journal of Psychiatry 58, 7 (2013), 
376–385. [PubMed: 23870719] 

[22]. Cuijpers Pim, Van Straten Annemieke, and Warmerdam Lisanne. 2007. Behavioral activation 
treatments of depression: A meta-analysis. Clinical psychology review 27, 3 (2007), 318–326. 
[PubMed: 17184887] 

[23]. Davison Gerald C. 2000. Stepped care: doing more with less? Journal of consulting and clinical 

psychology 68, 4 (2000), 580. [PubMed: 10965633] 

[24]. de Zwart Paul L, Jeronimus Bertus F, and de Jonge Peter. 2019. Empirical evidence for 

definitions of episode, remission, recovery, relapse and recurrence in depression: a systematic 
review. Epidemiology and psychiatric sciences 28, 5 (2019), 544–562. [PubMed: 29769159] 

[25]. Dinkel Danae, Caspari Jennifer Harsh, Fok Louis, Notice Maxine, Johnson David J, Watanabe-

Galloway Shinobu, and Emerson Margaret. 2021. A qualitative exploration of the feasibility 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 27

of incorporating depression apps into integrated primary care clinics. Translational behavioral 
medicine 11, 9 (2021), 1708–1716. [PubMed: 34231855] 

[26]. Dwight-Johnson Megan, Sherbourne Cathy D, Liao Diana, and Wells Kenneth B. 2000. 

Treatment preferences among depressed primary care patients. Journal of general internal 
medicine 15, 8 (2000), 527–534. [PubMed: 10940143] 

[27]. Epstein Daniel A, Caldeira Clara, Figueiredo Mayara Costa, Lu Xi, Silva Lucas M, Williams 

Lucretia, Lee Jong Ho, Li Qingyang, Ahuja Simran, Chen Qiuer, et al. 2020. Mapping and taking 
stock of the personal informatics literature. Proceedings of the ACM on Interactive, Mobile, 
Wearable and Ubiquitous Technologies 4, 4 (2020), 1–38.

[28]. Epstein Daniel A, Caraway Monica, Johnston Chuck, Ping An, Fogarty James, and Munson Sean 
A. 2016. Beyond abandonment to next steps: understanding and designing for life after personal 
informatics tool use. In Proceedings of the 2016 CHI conference on human factors in computing 
systems. 1109–1113.

[29]. Epstein Daniel A, Ping An, Fogarty James, and Munson Sean A. 2015. A lived informatics 

model of personal informatics. In Proceedings of the 2015 ACM international joint conference on 
pervasive and ubiquitous computing. 731–742.

[30]. Feng Shan, Mäntymäki Matti, Dhir Amandeep, Salmela Hannu, et al. 2021. How self-tracking 

and the quantified self promote health and well-being: systematic review. Journal of Medical 
Internet Research 23, 9 (2021), e25171. [PubMed: 34546176] 

[31]. Fergusson David M, Woodward Lianne J, and Horwood L John. 2000. Risk factors and life 

processes associated with the onset of suicidal behaviour during adolescence and early adulthood. 
Psychological medicine 30, 1 (2000), 23–39. [PubMed: 10722173] 

[32]. Firth Joseph,Cotter Jack, Elliott Rebecca, French Paul, and Yung Alison R. 2015. A systematic 
review and meta-analysis of exercise interventions in schizophrenia patients. Psychological 
medicine 45, 7 (2015), 1343–1361. [PubMed: 25650668] 

[33]. Firth Joseph, Torous John, Nicholas Jennifer, Carney Rebekah, Rosenbaum Simon, and Sarris 

Jerome. 2017. Can smartphone mental health interventions reduce symptoms of anxiety? A 
meta-analysis of randomized controlled trials. Journal of affective disorders 218 (2017), 15–22. 
[PubMed: 28456072] 

[34]. Frank Richard G, Huskamp Haiden A, and Pincus Harold Alan. 2003. Aligning incentives in the 
treatment of depression in primary care with evidence-based practice. Psychiatric Services 54, 5 
(2003), 682–687. [PubMed: 12719498] 

[35]. Furnham Adrian and Swami Viren. 2018. Mental health literacy: A review of what it is and why 

it matters. International Perspectives in Psychology: Research, Practice, Consultation 7, 4 (2018), 
240.

[36]. Goldberg Simon B, Lam Sin U, Simonsson Otto, Torous John, and Sun Shufang. 2022. Mobile 
phone-based interventions for mental health: A systematic metareview of 14 meta-analyses of 
randomized controlled trials. PLOS digital health 1, 1 (2022), e0000002. [PubMed: 35224559] 
[37]. Graham Andrea K, Greene Carolyn J, Kwasny Mary J, Kaiser Susan M, Lieponis Paul, Powell 

Thomas, and Mohr David C. 2020. Coached mobile app platform for the treatment of depression 
and anxiety among primary care patients: a randomized clinical trial. JAMA psychiatry 77, 9 
(2020), 906–914. [PubMed: 32432695] 

[38]. Gulliver Amelia, Griffiths Kathleen M, and Christensen Helen. 2010. Perceived barriers and 

facilitators to mental health help-seeking in young people: a systematic review. BMC psychiatry 
10, 1 (2010), 1–9. [PubMed: 20055988] 

[39]. Hill Clara E, Knox Sarah, Thompson Barbara J, Williams Elizabeth Nutt, Hess Shirley A, 

and Ladany Nicholas. 2005. Consensual qualitative research: An update. Journal of counseling 
psychology 52, 2 (2005), 196.

[40]. Hoffberg Adam S, Stearns-Yoder Kelly A, and Brenner Lisa A. 2020. The effectiveness of crisis 
line services: a systematic review. Frontiers in public health 7 (2020), 399. [PubMed: 32010655] 

[41]. Hofmann Stefan G and Smits Jasper AJ. 2008. Cognitive-behavioral therapy for adult anxiety 

disorders: a meta-analysis of randomized placebo-controlled trials. Journal of clinical psychiatry 
69, 4 (2008), 621. [PubMed: 18363421] 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 28

[42]. Hsieh Hsiu-Fang and Shannon Sarah E. 2005. Three approaches to qualitative content analysis. 

Qualitative health research 15, 9 (2005), 1277–1288. [PubMed: 16204405] 

[43]. Jin Daoyan, Halvari Hallgeir, Maehle Natalia, and Olafsen Anja H. 2022. Self-tracking behaviour 
in physical activity: a systematic review of drivers and outcomes of fitness tracking. Behaviour & 
Information Technology 41, 2 (2022), 242–261.

[44]. Karyotaki Eirini, Efthimiou Orestis, Miguel Clara, genannt Bermpohl Frederic Maas, Furukawa 
Toshi A, Cuijpers Pim, Riper Heleen, Patel Vikram, Mira Adriana, Gemmil Alan W, et al. 2021. 
Internet-based cognitive behavioral therapy for depression: a systematic review and individual 
patient data network meta-analysis. JAMA psychiatry 78, 4 (2021), 361–371. [PubMed: 
33471111] 

[45]. Kazdin Alan E. 2017. Addressing the treatment gap: A key challenge for extending evidence-
based psychosocial interventions. Behaviour research and therapy 88 (2017), 7–18. [PubMed: 
28110678] 

[46]. Kelley Christina, Lee Bongshin, and Wilcox Lauren. 2017. Self-tracking for mental wellness: 

understanding expert perspectives and student experiences. In Proceedings of the 2017 CHI 
conference on human factors in computing systems. 629–641.

[47]. Kessler Ronald C, Berglund Patricia, Demler Olga, Jin Robert, Merikangas Kathleen R, and 

Walters Ellen E. 2005. Lifetime prevalence and age-of-onset distributions of DSM-IV disorders 
in the National Comorbidity Survey Replication. Archives of general psychiatry 62, 6 (2005), 
593–602. [PubMed: 15939837] 

[48]. Kim Taewan, Kim Haesoo, Lee Ha Yeon, Goh Hwarang, Abdigapporov Shakhboz, Jeong 

Mingon, Cho Hyunsung, Han Kyungsik, Noh Youngtae, Lee Sung-Ju, et al. 2022. Prediction for 
Retrospection: Integrating Algorithmic Stress Prediction into Personal Informatics Systems for 
College Students’ Mental Health. In CHI Conference on Human Factors in Computing Systems. 
1–20.

[49]. Kolenik Tine. 2022. Methods in digital mental health: smartphone-based assessment and 

intervention for stress, anxiety, and depression. In Integrating Artificial Intelligence and IoT 
for Advanced Health Informatics. Springer, 105–128.

[50]. Kornfield Rachel, Zhang Renwen, Nicholas Jennifer, Schueller Stephen M, Cambo Scott A, 

Mohr David C, and Reddy Madhu. 2020. “Energy is a Finite Resource”: Designing Technology 
to Support Individuals across Fluctuating Symptoms of Depression. In Proceedings of the 2020 
CHI Conference on Human factors in Computing systems. 1–17.

[51]. Krafft Jennifer, Ong Clarissa W, Davis Carter H, Petersen Julie M, Levin Michael E, and Twohig 
Michael P. 2022. An open trial of group acceptance and commitment therapy with an adjunctive 
mobile app for generalized anxiety disorder. Cognitive and Behavioral Practice 29, 4 (2022), 
846–859.

[52]. Lange-Maia Brittney S, De Maio Fernando, Avery Elizabeth F, Lynch Elizabeth B, Laflamme 
Emily M, Ansell David A, and Shah Raj C. 2018. Association of community-level inequities 
and premature mortality: Chicago, 2011–2015. J Epidemiol Community Health 72, 12 (2018), 
1099–1103. [PubMed: 30171083] 

[53]. Lattie Emily G, Graham Andrea K, Hadjistavropoulos Heather D, Dear Blake F, Titov 

Nickolai, and Mohr David C. 2019. Guidance on defining the scope and development of 
text-based coaching protocols for digital mental health interventions. Digital Health 5 (2019), 
2055207619896145. [PubMed: 31897306] 

[54]. Lattie Emily G, Stiles-Shields Colleen, and Graham Andrea K. 2022. An overview of and 

recommendations for more accessible digital mental health services. Nature Reviews Psychology 
1, 2 (2022), 87–100.

[55]. Lee Jong Ho, Schroeder Jessica, and Epstein Daniel A. 2021. Understanding and Supporting 
Self-Tracking App Selection. Proceedings of the ACM on Interactive, Mobile, Wearable and 
Ubiquitous Technologies 5, 4 (2021), 1–25.

[56]. Lee Kwangyoung and Hong Hwajung. 2018. MindNavigator: Exploring the stress and self-

interventions for mental wellness. In Proceedings of the 2018 CHI Conference on Human Factors 
in Computing Systems. 1–14.

[57]. Linardon Jake, Cuijpers Pim, Carlbring Per, Messer Mariel, and Fuller-Tyszkiewicz Matthew. 

2019. The efficacy of app-supported smartphone interventions for mental health problems: 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 29

A meta-analysis of randomized controlled trials. World Psychiatry 18, 3 (2019), 325–336. 
[PubMed: 31496095] 

[58]. Liu Tony, Meyerhoff Jonah, Eichstaedt Johannes C, Karr Chris J, Kaiser Susan M, Kording 
Konrad P, Mohr David C, and Ungar Lyle H. 2022. The relationship between text message 
sentiment and self-reported depression. Journal of affective disorders 302 (2022), 7–14. 
[PubMed: 34963643] 

[59]. Liverpool Shaun, Mota Catarina Pinheiro, Sales Célia MD, Čuš Anja, Carletto Sara, Hancheva 

Camellia, Sousa Sónia, Cerón Sonia Conejo, Moreno-Peral Patricia, Pietrabissa Giada, et al. 
2020. Engaging children and young people in digital mental health interventions: systematic 
review of modes of delivery, facilitators, and barriers. Journal of medical Internet research 22, 6 
(2020), e16317. [PubMed: 32442160] 

[60]. MacLeod Haley, Tang Anthony, and Carpendale Sheelagh. 2013. Personal informatics in chronic 

illness management. In Proceedings of Graphics Interface 2013. Citeseer, 149–156.

[61]. Mamykina Lena, Mynatt Elizabeth, Davidson Patricia, and Greenblatt Daniel. 2008. MAHI: 

investigation of social scaffolding for reflective thinking in diabetes management. In Proceedings 
of the SIGCHI Conference on Human Factors in Computing Systems. 477–486.

[62]. Matthews Mark, Doherty Gavin, Sharry John, and Fitzpatrick Carol. 2008. Mobile phone mood 
charting for adolescents. British Journal of Guidance & Counselling 36, 2 (2008), 113–129.
[63]. Matthews Mark, Murnane Elizabeth, and Snyder Jaime. 2017. Quantifying the Changeable 

Self: The role of self-tracking in coming to terms with and managing bipolar disorder. Human–
Computer Interaction 32, 5-6 (2017), 413–446.

[64]. Mekonen Tesfa, Chan Gary CK, Connor Jason P, Hides Leanne, and Leung Janni. 2021. 

Estimating the global treatment rates for depression: a systematic review and meta-analysis. 
Journal of Affective Disorders 295 (2021), 1234–1242. [PubMed: 34665135] 

[65]. Meng Jingbo, Hussain Syed Ali, Mohr David C, Czerwinski Mary, Zhang Mi, et al. 2018. 

Exploring user needs for a mobile behavioral-sensing technology for depression management: 
qualitative study. Journal of medical Internet research 20, 7 (2018), e10139. [PubMed: 30021710] 

[66]. Meyerhoff Jonah, Liu Tony, Kording Konrad P, Ungar Lyle H, Kaiser Susan M, Karr Chris J, 

Mohr David C, et al. 2021. Evaluation of changes in depression, anxiety, and social anxiety using 
smartphone sensor features: longitudinal cohort study. Journal of medical Internet research 23, 9 
(2021), e22844. [PubMed: 34477562] 

[67]. Mohr David, Cuijpers Pim, Lehman Kenneth, et al. 2011. Supportive accountability: a model 

for providing human support to enhance adherence to eHealth interventions. Journal of medical 
Internet research 13, 1 (2011), e1602.

[68]. Mohr David C, Azocar Francisca, Bertagnolli Andrew, Choudhury Tanzeem, Chrisp Paul, Frank 
Richard, Harbin Henry, Histon Trina, Kaysen Debra, Nebeker Camille, et al. 2021. Banbury 
forum consensus statement on the path forward for digital mental health treatment. Psychiatric 
Services 72, 6 (2021), 677–683. [PubMed: 33467872] 

[69]. Mohr David C, Hart Stacey L, Howard Isa, Julian Laura, Vella Lea, Catledge Claudine, and 

Feldman Mitchell D. 2006. Barriers to psychotherapy among depressed and nondepressed 
primary care patients. Annals of Behavioral Medicine 32, 3 (2006), 254–258. [PubMed: 
17107299] 

[70]. Mohr David C, Ho Joyce, Duffecy Jenna, Baron Kelly G, Lehman Kenneth A, Jin Ling, and 

Reifler Douglas. 2010. Perceived barriers to psychological treatments and their relationship to 
depression. Journal of clinical psychology 66, 4 (2010), 394–409. [PubMed: 20127795] 
[71]. Mohr David C, Lyon Aaron R, Lattie Emily G, Reddy Madhu, and Schueller Stephen M. 

2017. Accelerating digital mental health research from early design and creation to successful 
implementation and sustainment. Journal of medical Internet research 19, 5 (2017), e7725.
[72]. Mohr David C, Schueller Stephen M, Tomasino Kathryn Noth, Kaiser Susan M, Alam Nameyeh, 
Karr Chris, Vergara Jessica L, Gray Elizabeth L, Kwasny Mary J, and Lattie Emily G. 2019. 
Comparison of the effects of coaching and receipt of app recommendations on depression, 
anxiety, and engagement in the IntelliCare platform: factorial randomized controlled trial. Journal 
of medical Internet research 21, 8 (2019), e13609. [PubMed: 31464192] 

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 30

[73]. Mohr David C, Tomasino Kathryn Noth, Lattie Emily G, Palac Hannah L, Kwasny Mary J, 

Weingardt Kenneth, Karr Chris J, Kaiser Susan M, Rossom Rebecca C, Bardsley Leland R, et al. 
2017. IntelliCare: an eclectic, skills-based app suite for the treatment of depression and anxiety. 
Journal of medical Internet research 19, 1 (2017), e6645.

[74]. Mohr David C, Weingardt Ken R, Reddy Madhu, and Schueller Stephen M. 2017. Three 

problems with current digital mental health research… and three things we can do about them. 
Psychiatric services 68, 5 (2017), 427–429. [PubMed: 28412890] 

[75]. Mojtabai Ramin, Olfson Mark, Sampson Nancy A, Jin Robert, Druss Benjamin, Wang Philip 
S, Wells Kenneth B, Pincus Harold A, and Kessler Ronald C. 2011. Barriers to mental health 
treatment: results from the National Comorbidity Survey Replication. Psychological medicine 41, 
8 (2011), 1751–1761. [PubMed: 21134315] 

[76]. Mongelli Francesca, Georgakopoulos Penelope, and Pato Michele T. 2020. Challenges and 

opportunities to meet the mental health needs of underserved and disenfranchised populations in 
the United States. Focus 18, 1 (2020), 16–24. [PubMed: 32047393] 

[77]. Mughal Faraz, Hossain Muhammad Z, Brady Angela, Samuel Judy, and Chew-Graham Carolyn 

A. 2021. Mental health support through primary care during and after covid-19.

[78]. Naicker Kiyuri, Galambos Nancy L, Zeng Yiye, Senthilselvan Ambikaipakan, and Colman Ian. 

2013. Social, demographic, and health outcomes in the 10 years following adolescent depression. 
Journal of Adolescent Health 52, 5 (2013), 533–538.

[79]. Olfson Mark, Blanco Carlos, and Marcus Steven C. 2016. Treatment of adult depression in the 
United States. JAMA internal medicine 176, 10 (2016), 1482–1491. [PubMed: 27571438] 
[80]. Place S, Blanch-Hartigan DL, Rubin C, Gorrostieta C, Mead C, Kane J, Marx BP, Feast J, and 

Deckersbach T. 2017. Survey Instrument (appears in: Behavioral Indicators on a Mobile Sensing 
Platform Predict Clinically Validated Psychiatric Symptoms of Mood and Anxiety Disorders). 
Copyright: Creative Commons License. (2017).

[81]. Powell Adam C, Yue Zongyang, Shan Chenglei, and Torous John B. 2019. The monetization 

strategies of apps for anxiety management: an international comparison. Journal of Technology in 
Behavioral Science 4, 2 (2019), 67–72.

[82]. Priest Robert G, Vize Christine, Roberts Ann, Roberts Megan, and Tylee Andre. 1996. Lay 
people’s attitudes to treatment of depression: results of opinion poll for Defeat Depression 
Campaign just before its launch. Bmj 313, 7061 (1996), 858–859. [PubMed: 8870574] 
[83]. Rabbi Mashfiqui, Ali Shahid, Choudhury Tanzeem, and Berke Ethan. 2011. Passive and in-situ 
assessment of mental and physical well-being using mobile sensors. In Proceedings of the 13th 
international conference on Ubiquitous computing. 385–394.

[84]. Radez Jerica, Reardon Tessa, Creswell Cathy, Lawrence Peter J, Evdoka-Burton Georgina, and 
Waite Polly. 2021. Why do children and adolescents (not) seek and access professional help 
for their mental health problems? A systematic review of quantitative and qualitative studies. 
European child & adolescent psychiatry 30, 2 (2021), 183–211. [PubMed: 31965309] 

[85]. Renn Brenna N, Pratap Abhishek, Atkins David C, Mooney Sean D, and Areán Patricia A. 2018. 

Smartphone-based passive assessment of mobility in depression: Challenges and opportunities. 
Mental health and physical activity 14 (2018), 136–139. [PubMed: 30123324] 

[86]. Riehm Kira E, Brignone Emily, Stuart Elizabeth A, Gallo Joseph J, and Mojtabai Ramin. 2022. 
Diagnoses and Treatment After Depression Screening in Primary Care Among Youth. American 
journal of preventive medicine 62, 4 (2022), 511–518. [PubMed: 34801332] 

[87]. Saeb Sohrab, Zhang Mi, Karr Christopher J, Schueller Stephen M, Corden Marya E, Kording 
Konrad P, Mohr David C, et al. 2015. Mobile phone sensor correlates of depressive symptom 
severity in daily-life behavior: an exploratory study. Journal of medical Internet research 17, 7 
(2015), e4273.

[88]. Schroeder Jessica, Karkar Ravi, Murinova Natalia, Fogarty James, and Munson Sean A. 

2019. Examining opportunities for goal-directed self-tracking to support chronic condition 
management. Proceedings of the ACM on interactive, mobile, wearable and ubiquitous 
technologies 3, 4 (2019), 1–26.

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 31

[89]. Schueller Stephen M, Tomasino Kathryn Noth, and Mohr David C. 2017. Integrating human 
support into behavioral intervention technologies: The efficiency model of support. Clinical 
Psychology: Science and Practice 24, 1 (2017), 27.
[90]. Siu Albert. 2016. Follow-up After Screening Response.
[91]. Siu Albert L, Bibbins-Domingo Kirsten, Grossman David C, Baumann Linda Ciofu, Davidson 
Karina W, Ebell Mark, García Francisco AR, Gillman Matthew, Herzstein Jessica, Kemper 
Alex R, et al. 2016. Screening for depression in adults: US Preventive Services Task Force 
recommendation statement. Jama 315, 4 (2016), 380–387. [PubMed: 26813211] 

[92]. Torous John, Chan Steven Richard, Tan Shih Yee-Marie, Behrens Jacob, Mathew Ian, Conrad 
Erich J, Hinton Ladson, Yellowlees Peter, Keshavan Matcheri, et al. 2014. Patient smartphone 
ownership and interest in mobile apps to monitor symptoms of mental health conditions: a survey 
in four geographically distinct psychiatric clinics. JMIR mental health 1, 1 (2014), e4004.

[93]. Torous John, Michalak Erin E, and O’Brien Heather L. 2020. Digital health and engagement
—looking behind the measures and methods. JAMA Network Open 3, 7 (2020), e2010918–
e2010918. [PubMed: 32678446] 

[94]. Trifan Alina, Oliveira Maryse, Oliveira José Luís, et al. 2019. Passive sensing of health outcomes 
through smartphones: systematic review of current solutions and possible limitations. JMIR 
mHealth and uHealth 7, 8 (2019), e12649. [PubMed: 31444874] 

[95]. Van Straten Annemieke, Seekles Wike, Van ‘t Veer-Tazelaar Nelleke J, Beekman Aartjan TF, and 
Cuijpers Pim. 2010. Stepped care for depression in primary care: what should be offered and 
how? Medical Journal of Australia 192 (2010), S36–S39. [PubMed: 20528706] 

[96]. VanDenBerg John E and Grealish E Mary. 1996. Individualized services and supports through 
the wraparound process: Philosophy and procedures. Journal of Child and Family Studies 5, 1 
(1996), 7–21.

[97]. Walker Elizabeth Reisinger, Cummings Janet R, Hockenberry Jason M, and Druss Benjamin G. 
2015. Insurance status, use of mental health services, and unmet need for mental health care in 
the United States. Psychiatric Services 66, 6 (2015), 578–584. [PubMed: 25726980] 

[98]. Wang Philip S, Lane Michael, Olfson Mark, Pincus Harold A, Wells Kenneth B, and Kessler 

Ronald C. 2005. Twelve-month use of mental health services in the United States: results from 
the National Comorbidity Survey Replication. Archives of general psychiatry 62, 6 (2005), 629–
640. [PubMed: 15939840] 

[99]. Wang Rui, Wang Weichen, DaSilva Alex, Huckins Jeremy F, Kelley William M, Heatherton 

Todd F, and Campbell Andrew T. 2018. Tracking depression dynamics in college students using 
mobile phone and wearable sensing. Proceedings of the ACM on Interactive, Mobile, Wearable 
and Ubiquitous Technologies 2, 1 (2018), 1–26.

[100]. Zhu Haining, Colgan Joanna, Reddy Madhu, and Choe Eun Kyoung. 2016. Sharing 

patient-generated data in clinical practices: an interview study. In AMIA Annual Symposium 
Proceedings, Vol. 2016. American Medical Informatics Association, 1303.

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

Kruzan et al.

Page 32

•

Human-centered computing;

CCS CONCEPTS

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

 
 
 
 
Kruzan et al.

Page 33

Participant demographics. PHQ9 scores of 5, 10, 15, and 20 represent cutpoints for mild, moderate, 
moderately severe and severe depression, respectively. GAD7 scores of 5, 10, and 15 represent cutpoints for 
mild, moderate, and severe anxiety, respectively.

Table 1:

P#

Age Gender

Race

PHQ9 GAD7

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

22

24

26

25

26

26

17

31

55

42

F

F

F

F

F

M

F

F

F

M

More than one race

White

White

American Indian or Alaskan Native

American Indian or Alaskan Native

Asian

African American or Black

Asian

African American or Black

Asian

8

4

8

11

14

2

8

2

4

4

13

11

6

16

10

NA

8

5

2

1

Proc SIGCHI Conf Hum Factor Comput Syst. Author manuscript; available in PMC 2024 June 13.

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t

A
u
t
h
o
r

M
a
n
u
s
c
r
i
p
t
