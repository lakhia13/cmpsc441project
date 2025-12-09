# Kadirvelu_2023_Mindcraft, a Mobile Mental Health Monitoring Platform for Children and Young People Development and Acceptability Pilot Study.

JMIR FORMATIVE RESEARCH

Original Paper

Kadirvelu et al

Mindcraft, a Mobile Mental Health Monitoring Platform for Children
and Young People: Development and Acceptability Pilot Study

Balasundaram Kadirvelu1, PhD; Teresa Bellido Bel2*, MSc; Xiaofei Wu1*; Victoria Burmester2, PhD; Shayma Ananth2,
BSc; Bianca Cabral C C Branco1, MSc; Braulio Girela-Serrano2, MD; Julia Gledhill2, MD; Martina Di Simplicio2,
MD, PhD; Dasha Nicholls2, MD; A Aldo Faisal1,3, PhD
1Brain & Behaviour Lab, Department of Computing and Department of Bioengineering, Imperial College London, London, United Kingdom
2Division of Psychiatry, Department of Brain Sciences, Imperial College London, London, United Kingdom
3Chair in Digital Health, Faculty of Life Sciences, University of Bayreuth, Bayreuth, Germany
*these authors contributed equally

Corresponding Author:
A Aldo Faisal, PhD
Brain & Behaviour Lab
Department of Computing and Department of Bioengineering
Imperial College London
Royal School of Mines
London, SW7 2AZ
United Kingdom
Phone: 44 20 7594 6373
Email: a.faisal@imperial.ac.uk

Abstract

Background:  Children and young people's mental health is a growing public health concern, which is further exacerbated by
the COVID-19 pandemic. Mobile health apps, particularly those using passive smartphone sensor data, present an opportunity
to address this issue and support mental well-being.

Objective:  This study aimed to develop and evaluate a mobile mental health platform for children and young people, Mindcraft,
which integrates passive sensor data monitoring with active self-reported updates through an engaging user interface to monitor
their well-being.

Methods:  A user-centered design approach was used to develop Mindcraft, incorporating feedback from potential users. User
acceptance testing was conducted with a group of 8 young people aged 15-17 years, followed by a pilot test with 39 secondary
school students aged 14-18 years, which was conducted for a 2-week period.

Results:  Mindcraft showed encouraging user engagement and retention. Users reported that they found the app to be a friendly
tool helping them to increase their emotional awareness and gain a better understanding of themselves. Over 90% of users (36/39,
92.5%) answered all active data questions on the days they used the app. Passive data collection facilitated the gathering of a
broader range of well-being metrics over time, with minimal user intervention.

Conclusions:  The  Mindcraft  app  has  shown  promising  results  in  monitoring  mental  health  symptoms  and  promoting  user
engagement among children and young people during its development and initial testing. The app's user-centered design, the
focus on privacy and transparency, and a combination of active and passive data collection strategies have all contributed to its
efficacy and receptiveness among the target demographic. By continuing to refine and expand the app, the Mindcraft platform
has the potential to contribute meaningfully to the field of mental health care for young people.

(JMIR Form Res 2023;7:e44877)  doi: 10.2196/44877

KEYWORDS
mobile mental health; passive sensing; smartphone apps for mental health; children and young people; adolescents; digital tools;
mobile apps

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

JMIR Form Res 2023 | vol. 7 | e44877 | p. 1
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

Introduction

Mental health issues among children and young people (CYP)
have emerged as a significant public health concern [1]. A 2021
NHS digital survey in the United Kingdom revealed that 17.4%
of CYP aged 6-16 years experienced at least 1 mental disorder,
with a rising trend in emotional disorders such as depression
and anxiety since 2017 [2]. The COVID-19 pandemic and its
associated  social  isolation,  public  health  disruptions,  and
economic  decline  are  expected  to  exacerbate  these  issues,  as
seen in previous large-scale disasters [3]. Peer-to-peer contact
is  critical  for  social  species  [4],  especially  for  young  people
who  may  be  more  affected  by  social  distancing  due  to
COVID-19. Research shows that isolation and deprivation of
social  interaction  during  adolescence  can  cause  behaviors
resembling depression, anxiety, and even impairment of certain
cognitive skills [5-7]. A mental illness epidemic is predicted to
emerge  following  the  extended  period  of  COVID-19–related
behavioral  changes  [8],  making  prompt  and  comprehensive
mitigation planning essential to address long-term mental health
consequences.

Smartphone usage is widespread among CYP, with 88% of 13-
to 18-year-olds in the United States owning smartphones [9].
This ubiquity makes smartphone apps a promising option for
supporting CYP's mental health [10,11]. To reduce the widening
mental  health  treatment  gap  and  supplement  in-person
treatments,  further  research  and  investment  in  mobile  health
apps are increasingly necessary.

In recent years, the mental health field has experienced a surge
in applications designed for monitoring mental health [12]. A
limitation  of  many  of  these  applications  is  their  reliance  on
self-reported data, often referred to as active data, which may
be subjected to personal biases and potentially lead to misleading
conclusions in decision-making [13,14]. To address this issue,
researchers  have  explored  the  usage  of  mobile  phone  sensor
data,  such  as  GPS,  accelerometer,  microphone,  and  battery
usage.  These  data  can  be  collected  passively,  without  active
user participation (hence referred to as passive data) and with
minimal user burden.

passive 

capabilities 

Smartphones' 
facilitate
sensing 
understanding  of  user  behavior  and  automatic  personality
detection, eliminating the need for investigating hard-to-measure
characteristics.  Studies  have  showed  that  passive  data  can
objectively reflect users' emotional state and generate profiles
of temperament and behavior [15,16]. One study used various
smartphone data from 83 individuals over 8 months to predict
Big  Five  personality  traits  with  69%-76%  accuracy  [17].
Another study used passive data to classify 166 users from 5
countries into Big Five traits with 63%-71% accuracy, observing
increased accuracy in gender- and country-specific models [18].
The potential for passive data to predict personality traits renders
smartphone  apps  a  promising  avenue  for  influencing  user
behavior and providing personalized mental health support.

Most studies investigating passive data use in apps have focused
on adult populations, with limited research on youth [19,20].
Furthermore,  given  the  rising  concerns  about  data  privacy,

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

especially  among  young  adults  [21],  understanding  how
adolescents engage with mental health apps, particularly how
comfortable would this population be in terms of passive data
sharing to monitor and improve their mental health, is essential.
Consequently, we have developed Mindcraft, a mobile mental
health platform for CYP, which integrates passive sensor data
monitoring with self-reported updates through an engaging user
interface (UI). By developing such a tool, we aim to enhance
mental  health  monitoring  and  empower  young  adults  to
proactively manage their mental well-being.

This  paper  details  the  design  and  development  of  Mindcraft,
along with the results obtained from a pilot study assessing the
app's usability and functionality. These findings will contribute
to the refinement of the platform and inform future research in
the realm of mental health applications for young adults.

Methods

The Mindcraft App

Overview
The  Mindcraft  app  (Figure  1)  is  a  user-friendly  mobile  app
designed specifically for CYP to effectively monitor their mental
well-being.  The  app  provides  a  modern  and  appealing  user
experience to encourage participation and is designed with a
to  facilitate  future
modular  and  adaptable  framework 
improvements and support various study questions. The primary
objectives of the Mindcraft app are (1) combining self-reported
well-being updates (active data) with phone sensor data (passive
data) for effective monitoring of mental health–related behavior,
(2) providing an easy-to-use and intuitive UI that promotes user
participation and facilitates data collection, (3) ensuring user
data are handled according to good clinical practice standards
[22] for privacy and security, and (4) continuously developing
and updating the app based on participant feedback and usage
patterns.

The Mindcraft app features a modular design, enhancing user
engagement  by  providing  customization  options  to  meet
individual  needs  and  interests.  This  design  contributes  to
improved  user  experience  and  overall  app  effectiveness.  The
key modular components include:

1. Customizable active questions: Mindcraft targets a general
population, so users have different well-being goals. The
app allows users to select daily active questions tailored to
their unique mental health objectives.

2. Configurable passive data: Users can choose which passive
data they wish to share, ensuring that they have control over
their privacy.

Users can set their active and passive data sharing preferences
during the initial onboarding process and also can modify them
at any time through the app's settings. Mindcraft app is available
for free download from the App Store [23] and Google Play
Store [24]. A valid study ID code is required to use the app.
The  Mindcraft  app  comprises  3  main  tabs  in  its  UI  (Figure
2A-E): the main tab, the progress tab, and the settings tab, which
are described below.

JMIR Form Res 2023 | vol. 7 | e44877 | p. 2
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

Figure 1.  Overview of Mindcraft, a mobile mental health monitoring platform that combines self-reported questionnaire data with passive mobile
sensors to monitor mental well-being markers of children and young people.

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

JMIR Form Res 2023 | vol. 7 | e44877 | p. 3
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

Figure 2.  User interface of the Mindcraft app. (A) Login tab, (B) main tab, (C) example of an active questionnaire involving slider-based data entry,
(D) progress tab, (E) settings tab, and (F) optional data collection settings allowing users to control what information is collected (actively and passively).

Main Tab
Mindcraft is easy to use and features an attractive design that
incorporates  visual
captures  users'  attention.  The  app 
representations of users' mood and mental well-being markers,
which have been shown to increase engagement [25,26]. The
main tab, illustrated in Figure 2B, is the first view of the app
when  launched  by  a  registered  user.  Here,  the  user  can
self-report a questionnaire related to their mood and well-being.
The  questionnaire  contains  7  compulsory  questions  (sleep
quality, sleep quantity, mood, motivation, loneliness, appetite,
and exercise), as well as 11 optional questions (racing thoughts,
negative 
irritability,
thinking,  hopefulness,  headaches, 
confidence,  sociability,  energy  levels,  productivity,  self-care,
leisure, and a custom metric called “your measure”). The user
can manage the optional questions through the settings tab. Each
question can only be answered once a day; thus, the question
will disappear after each submission. Most of the self-reported
questions (such as mood and sleep quality) are on a scale of 1-7
and contain a slider. An example of such a question is shown

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

in  Figure  2C.  Other  questions  (such  as  sleep  quantity  and
exercise time) collect numerical data from textboxes, and the
input is type-checked to ensure only valid inputs are stored (eg,
numerical numbers and not text).

Progress Tab
The progress tab (shown in Figure 2D) charts the self-reported
updates given by the user throughout the study. Selecting the
data of interest causes the graph view to display the historical
data and the average score for the selected period.

Settings Tab
In the settings tab (illustrated in Figure 2E), the user can manage
the active and passive data settings, read the privacy policy, as
well as withdraw from the study. As shown in Figure 2F, the
app allows the user to enable or disable the optional active data
questions most relevant to them. Although the focus of the app
is helping the users to develop better habits of self-care, the app
must not delay seeking for professional help. The help option
under the settings tab provides the ability for the user to seek

JMIR Form Res 2023 | vol. 7 | e44877 | p. 4
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

support when needed. To facilitate this, Mindcraft lists 4 external
organizations—Shout  [27],  YoungMinds  [28],  Best  For  You
NHS [29], and Kooth [30]—along with a brief description of
each organization and links to their websites.

Figure 3.  Overview of the system architecture of the Mindcraft platform.

System Architecture

Overview
The system architecture of Mindcraft is presented in Figure 3.

App
Mindcraft  is  a  cross-platform  smartphone  app  with  a  single
codebase that runs on iOS and Android. The app was developed
using  the  ionic  framework  as  a  hybrid  app.  Functionalities
common to both mobile operating systems (user login, active
data collection and transmission, progress display, and settings)

were written with web technologies (TypeScript, HTML, and
cascading  style  sheets).  Mobile  operating  system–specific
functionalities (passive data collection and local notifications)
were developed, using native plugins that used Capacitor written
in Swift for iOS and Java for Android. Most passive data are
collected every 15 minutes, and Table 1 lists the passive data
collected on each mobile operating system.

Table 1.  Passive sensing data collected by the Mindcraft app.

Passive sensor data

Locationa

Step count

Background noise levelsb

Ambient light

Battery level

App usage on the phone

Mobile operating system supported

iOS and Android

iOS and Android

iOS and Android

iOS and Android

iOS and Android

Android only

aiOS: collected when there is a significant change in the user's location.
biOS: collected only when the app is in the foreground.

Server
The backend server has a 3-layer architecture: web server layer,
application layer, and database layer (Figure 3). We used Nginx
as the web server to support reverse proxy and load balancing
to  increase  the  security  and  scalability  of  the  app.  For  the
application  layer,  we  used  Apollo  Server,  an  open-source
GraphQL server, to process the entire backend application logic.
PostgreSQL  is  used  as  the  database  layer  to  store  user
information, active data, and passive data. The 3 layers are also
containerized using separate docker containers to simplify the
deployment procedure and to make the backend portable across
host servers.

Server Security and Privacy
The app handles a large amount of sensitive data, which must
be  stored  and  transferred  securely.  User  data  were  handled
according to good clinical practice standards, with users being
given  unique  anonymous  identifier  numbers  when  the  app  is
first launched on a new device. For secure data transmission,

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

we require the use of HTTPS across all our end points, which
makes tampering with requests and responses significantly more
difficult.  To  authorize  clients,  we  implemented  a  time-based
token system where the server and client have a shared secret,
which is then combined with a timestamp and hashed, and then
sent over the network to authenticate the user.

Device Testing
The app was tested on multiple devices for a range of parameters
to establish its suitability for and performance on a diverse range
of hardware. The iOS app was tested on iPhone 6S (iOS 13.6),
iPhone 6 Plus (iOS 13.2), iPhone 11 (iOS 13.7), iPhone 12 (iOS
14.6), and iPhone 13 (iOS 14.8). The Android version was tested
on a range of devices including Google Pixel 4a (Android 13),
Samsung Galaxy A32 (Android 12), Realme 5 Pro (Android
11), Huawei P20 Pro (Android 10), and Redmi 7 (Android 10).
The app worked on all devices smoothly. Based on qualitative
human experience, the app operations on the older phone models
were  as  good  as  on  the  newer  models,  highlighting  the  low
degree by which the app taxed the system's resources.

JMIR Form Res 2023 | vol. 7 | e44877 | p. 5
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

Performance  testing  was  done  using  Xcode  (for  iOS)  and
Android Studio Profile (for Android) to ensure that the app does
not disrupt the normal performance of the phone. During normal
use, we observed that memory consumption was constant with
no memory leaks, and CPU usage remained low, with the CPU
only being used during tab switches and submissions.

We tested the app for battery usage on an iPhone 6 Plus and
Redmi 7 for 2 months as development was carried out and for
2 weeks following installation of the finalized version of the
app bundle. We deliberately chose older model phones, as they
have less battery capacity, less energy-optimized hardware, and
smaller batteries than more recent models. During normal use
of the app, the battery consumption was mostly in the low to
medium range.

User-Centered Design Approach
Throughout  the  design  and  development  process,  we  used  a
user-centered design approach [31] to ensure a user-focused,
cocreation-driven app and followed a 3-step process:

1. User  research:  To  understand  the  unique  mental  health
needs, preferences, and experiences of our target users, we
conducted small focus groups even during the design stage
of 
the  app.  These  discussions  provided  valuable
requirements  for  various  aspects  of  app  design,  such  as
sensor access, privacy concerns, user experience, and push
notification preferences. By capturing this information early
in the design process, we were able to ensure that our app
would  be  both  relevant  and  engaging  for  our  target
audience.

2. Design and prototyping: Drawing from the user research
findings,  our 
team  developed  design  concepts  for
Mindcraft's visual design, UI, and key features. We created
a series of low-fidelity prototypes to test and refine the app's
design and functionality, ensuring that our design choices
were aligned with user preferences and needs. This iterative
process allowed us to optimize the app's design, making it
more user-friendly and intuitive for CYP.
Iterative  testing:  To  further  refine  Mindcraft,  we  held
multiple user testing sessions with focus group participants.
These sessions involved real-time feedback, which we used
to  make  informed  decisions  about  changes  to  the  app's
design  and  functionality.  Notable  decisions  made  during
this  process 
limiting
notifications to once a day, and prioritizing the development
of the progress tab.

reworking 

the  UI, 

included 

3.

By involving users early in the design process and maintaining
open  communication  throughout,  the  user-centered  design
approach  resulted  in  an  app  that  is  not  only  effective  and
engaging but also addresses the needs of our target audience.

Ethics Approval
Ethics  approval  for  the  study  was  granted  by  the  Imperial
College  London  Research  Ethics  Committee 
(ICREC
20IC6132).

Informed Consent
Informed consent was obtained at the start of the study, with
parents providing consent for those aged younger than 16 years.

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

Only  once  the  participant  understood  the  privacy  policy  and
accepted the terms and conditions of the study in the app were
they able to proceed through the app and partake in the study.
The privacy policy and information storage practices were also
accessible within the app.

Privacy and Confidentiality
We ensured European Union General Data Protection Regulation
compliance with data retrieval, anonymization, and a withdrawal
process.  All  participants  were  informed,  in  the  terms  and
conditions, of where and how the data they provided would be
used. Users had full control over the data that were collected
and could opt out of any single type of data collection at any
time. Users had the option to delete the entirety of their data
and withdraw from the study via the settings option in the app.

Compensation
Participation was incentivized with a prize draw for a £30 (US
$37) voucher and an educational session.

Study Procedure
For user acceptance testing, participants were recruited via social
media platforms (Twitter and Nextdoor, a local neighborhood
site). The inclusion criteria included being aged 14-18 years,
fluency in English, access to a video and audio-enabled device,
and possession of a smartphone. The exclusion criterion was
insufficient language skills. Participants were instructed to use
the app for 3 days, explore its various features, and share their
experience of using the app with the researchers following the
evaluation period.

For  the  pilot  study,  we  reached  out  to  many  secondary
educational establishments via email and chose the first school
that  expressed  interest  in  participating.  Participants  were
recruited via this secondary school, which promoted the study
directly  to  students  through  emails  sent  home.  Inclusion  and
exclusion  criteria  for  pilot  testing  were  identical  to  those  for
user acceptance testing. The school forwarded information on
the app to year 10, 11, 12, and 13 pupils.

Interested pupils voluntarily completed a web-based survey via
a  link  provided  in  the  promotional  information.  Informed
consent was obtained digitally, with parents providing consent
for those aged younger than 16 years. Upon completion of the
survey, participants received a link to download the app from
the App Store or Play Store, along with a unique login for the
app. Participants were asked to use the app for 2 weeks. Upon
completion of the 2-week testing period, user engagement data
and the types of active and passive data shared by the users were
analyzed to evaluate the app's performance.

Results

User Acceptance Testing
After  the  app's  development,  user  acceptance  testing  was
conducted with a recruited patient and public involvement group.
We carried out an exploratory qualitative study with this group
to understand the target audience's user experience and identify
barriers to adopting Mindcraft. Eight young people (including
4 female individuals) aged 15-17 years, with a mean age of 15.9

JMIR Form Res 2023 | vol. 7 | e44877 | p. 6
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

(SD 0.9) years were invited to download the app and use it for
a 3-day evaluation period. Two researchers conducted 2 digital
patient  and  public  involvement  groups  via  Microsoft  Teams
(Microsoft), each comprising 4 participants, lasting 180 minutes.
The semistructured interview explored their experience using
the app.

The  qualitative 
feedback  was  predominantly  positive.
Discussions with study participants revealed that some viewed
the app as a friendly tool promoting self-awareness and personal
growth.  They  found  the  app  enabled  them  to  increase  their
emotional  awareness  and  gain  a  better  understanding  of
themselves, as reported in previous studies on self-monitoring
tools  [32,33].  Participants  perceived  the  app  interface  as
engaging and less clinical. Although they expressed concerns
regarding data privacy and sharing (particularly passive data)
and  desired  greater  control,  they  were  relatively  more
comfortable  sharing  passive  data  for  mental  health.  Our  test
users did not consider social competition a motivator in mental
health apps, which contrasts with the findings of other studies
[34,35].

Based on user feedback, we revised the app's text prompts and
updated the UI to offer more control over passive sensor data
collection. The updated app was uploaded to the App Store and
Play Store for the pilot study with a larger user group.

Pilot Study
The  app  was  advertised  to  students  from  a  secondary  school
across  4-year  groups  (aged  14-18  years)  for  a  2-week  trial
period. A total of 39 students (20 male students and 19 female

students), with a mean age of 15.74 (SD 1.09) years, volunteered
and downloaded the app. Of these, 32 used the app on iPhones,
while the rest used Android phones.

We  calculated  user  engagement  over  time  by  analyzing  the
number of users who used the app over the 2-week evaluation
period (Figure 4). Out of the 39 users, 16 (41%) used the app
after  7  days,  while  9  (23%)  used  it  after  14  days.  The  mean
number of days the app was used during the first 14 days was
5.76 (SD 4.48). Passive data collection allowed the app to gather
more well-being metrics over time without user intervention.
While the number of users sharing active data decreased after
the first week probably because of the app's novelty wearing
off, the number of users sharing passive data remained steady
in  the  second  week  (Figure  4),  indicating  that  passive  data
collection may offer a more sustainable data collection method
in the long term.

Seven  active  data  questions  were  mandatory,  while  the  other
12 were optional (enabled by default). Although users had the
option to disable optional active data questions, 92.5% (36/39)
left them enabled. Over 90% of users (36/39, 92.5%) answered
all  active  data  questions  (except  for  the  customizable  Your
Measure) on the days they used the app (Figure 5A). Loneliness,
appetite, and sleep quality were the most frequently answered
active data questions. Concerning passive trackers, users favored
sharing noninvasive data, such as step count and battery levels
(Figure  5B).  However,  they  were  reluctant  to  share  intrusive
passive data, like location and background noise levels, because
of privacy concerns.

Figure 4.  User engagement plot showing the number of users using the app (sharing active and passive data) over the 2-week period.

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

JMIR Form Res 2023 | vol. 7 | e44877 | p. 7
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

Figure 5.  Data sharing preferences of the users. (A) Bar chart of the percentage of users sharing different types of active data. (B) Bar chart of the
percentage of users sharing different types of passive data.

Discussion

Principal Findings
The development and initial testing of the Mindcraft app have
shown promising results in monitoring mental health. The pilot
study found good user retention and engagement, with 23.07%
of users (9/39) using the app after 14 days. While Mindcraft's
effectiveness and acceptability among the target population to
track their mental health may be attributed to its user-centered
design,  the  emphasis  on  transparency  and  privacy,  and  the
customizable  use  of  both  active  and  passive  data  collection
strategies,  we  recognize  that  our  study's  good  retention  rates
should be interpreted with caution. The rates may be influenced
by  participants'  awareness  of  being  part  of  a  research  study,
potentially leading to increased engagement compared to the
naturalistic app user retention rate of 4% over a 15-day period
[36,37].

Our results support previous findings [38-40], indicating that
passive data collection can provide a sustainable and effective
way to monitor mental health symptoms over time. We found
that  passive  data  collection  reduced  user  burden  while  also
enabling the collection of a wider range of well-being metrics.
These  benefits  have  important  implications  for  the  design  of
mental health monitoring apps, as app developers can leverage
the advantages of passive data collection. By prioritizing user
privacy,  transparency,  and  customizability  of  data  sharing,
developers  can  design  apps  that  foster  user  trust  and
engagement.

acknowledge 

Comparison With Prior Work
We 
apps
that  numerous 
[11,14,19,41-55] use passive sensing to support mental health
and well-being. However, the majority of these studies target
adult  populations,  while  research  on  CYP  remains  limited
[19,20]. Our study aims to address this gap by focusing on the

studies 

and 

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

mental well-being of the general adolescent population using a
combined  active-passive  data  approach.  A  few  studies
[19,43,54,55] have investigated passive sensing for adolescent
mental  health.  Maharjan  et  al  [55]  evaluated  passive  sensing
for  predicting  maternal  depression  in  young  mothers  in  a
low-resource  setting.  Cao  et  al  [43]  and  Mullick  et  al  [54]
examined  the  effectiveness  of  passive  sensing  in  tracking
depression symptoms in clinically depressed adolescents. The
study by MacLeod et al [19] is the closest to our study, as it
involved adolescents from both clinical and nonclinical settings.
However,  it  exclusively  used  passive  sensing,  and  the
participants  had  no  interactions  with  the  study  app  after  the
initial setup. In comparison, our study focuses on monitoring
the mental well-being of the general adolescent population by
integrating both active and passive data. Our app enables users
to  decide  which  active  and  passive  data  they  want  to  share,
providing them with control over their privacy, a key factor for
real-world  deployment 
the  general  population.  We
demonstrate  that  combining  both  active  and  passive  data
collection strategies, with an emphasis on privacy, transparency,
and  an  engaging  design,  effectively  promotes  sustained
engagement with the app and improves long-term data collection
from  the  general  adolescent  population.  Additionally,  we
incorporated  a  user-centered  design  approach,  gathering  end
user feedback during the development process, an element often
neglected  in  mental  health  app  studies  [56,57].  It  is  worth
mentioning that, given the lack of regulatory oversight in the
mental health app market [10,58], Mindcraft's development was
guided  by  a  team  of  experienced  clinicians,  ensuring
evidence-based  and  clinically  relevant  content.  In  summary,
although Mindcraft shares some similarities with other mental
health  apps  and  studies,  its  focus  on  the  general  adolescent
population through an integrated active-passive data approach,
user-centered design, and clinically relevant content highlights
its potential to contribute meaningfully to the field.

to 

JMIR Form Res 2023 | vol. 7 | e44877 | p. 8
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

Limitations
Our study has some limitations that suggest directions for future
research. Although positive results about the user engagement
were observed, the conclusions must be considered preliminary
because of the relatively small sample size, and larger samples
are needed to validate the acceptability of the platform among
the target population. Additionally, the pilot study users used
the app for a limited period of 2 weeks, making it necessary to
investigate  its  usage  over  a  longer  period  to  assess  its
effectiveness.  Another  limitation  to  consider  is  the  potential
impact of the research study environment on our retention and
engagement  rates.  The  heightened  engagement  we  observed
might be partly attributed to the participants' awareness of their
involvement in a study. Therefore, future studies should aim to
assess Mindcraft's retention rates in real-world settings outside
the research context, to provide a more accurate reflection of
its performance.

Future Research
Throughout the study, we recognized opportunities to improve
Mindcraft's  user  experience  and  capability  to  build  a  more
comprehensive  user  behavior  profile  in  its  future  version.
Potential future enhancements could include gamification, which
has been shown to increase user engagement in therapeutic apps
[59] and mental health interventions for adolescents [60]. The
app may also benefit from new passive data sources like voice
recordings  for  speech  emotion  recognition  and  continuous
accelerometer and gyroscope data for more meaningful activity
measures  and  sleep  monitoring.  Integrating  music  listening
patterns,  as  shown  by  Rickard  et  al  [11],  could  further  help
Mindcraft better track users' emotional well-being over longer
periods without being too intrusive.

Although  the  potential  of  recommended  systems  has  been
occasionally  explored  in  health  care  research  [61-63],  the
possibility of taking advantage of this technology to improve
mental health care is yet to be sufficiently explored. Mindcraft

presents  the  opportunity  for  an  enhanced  recommendation
system  to  be  developed  where  recommendations  may  be
delivered based on personality, along with other factors such
as demographics, behavior, and self-reported scores for specific
symptoms.  Future  versions  of  Mindcraft  could  integrate  a
reinforcement  learning–based  personalized  recommendation
system,  where  an  agent  may  be  trained  to  work  toward
recommending  activities  [64,65]  or  mental  imagery  [66]  to
increase mood and mental health scores while being penalized
and rewarded accordingly based on score variations and user
feedback.

While  platforms  such  as  Kooth  and  Childline  provide
comprehensive coverage for those seeking help, these services
require  CYP  to  be  motivated  to  engage  with  a  counselor.
Mindcraft can help overcome this motivation barrier by using
passive  tracking  data  to  detect  early  indicators  of  poor
well-being  and  mental  health  issues,  triggering  them  to  seek
counseling help. Alternatively, the Mindcraft app could also be
extended to serve as an intervention system by incorporating
in-app counseling services based on the active and passive data
collected. This would be a step toward achieving the goal of
self-service mental health services and improving access to care
for those who may not otherwise seek help.

initial 

its  development  and 

Conclusions
The Mindcraft app has shown promising results in monitoring
mental  health  and  promoting  user  engagement  among  CYP
during 
testing.  The  app's
user-centered  design,  the  focus  on  privacy  and  transparency,
and a combination of active and passive data collection strategies
have contributed to its effectiveness and acceptability among
the  target  population.  Future  enhancements  could  include
gamification,  additional  sensor  data,  and  personalized
interventions  to  improve  user  engagement  and  mental  health
outcomes.  By  continuing  to  refine  and  expand  the  app,  the
Mindcraft platform has the potential to contribute meaningfully
to the field of mental health care for young people.

Acknowledgments
AAF acknowledges his support for United Kingdom Research and Innovation Turing AI Fellowship (EP/V025449/1). DN is
supported by the National Institute for Health Research (NIHR) Northwest London Applied Research Collaboration (ARC) and
the NIHR Biomedical Research Centre at Imperial College Healthcare NHS Trust. The views expressed are those of the authors
and not necessarily those of the NIHR or the Department of Health and Social Care. TBB has been supported by an Advanced
Research Fellowship in Child and Adolescent Psychiatry from the Alicia Koplowitz Foundation, Spain.

Data Availability
The study data are not publicly available because of the General Data Protection Regulation restrictions and privacy policies
outlined in the participant recruitment. The data sets generated during this study are available from the corresponding author upon
reasonable request.

Authors' Contributions
AAF conceptualized the study. App design and development were done by XW, BK, BCCCB, and AAF. App design feedback
was done by MDS, VB, and DN. Focus groups were classified by SA, VB, and DN. Pilot testing was done by TBB, BK, JG,
MDS, and DN. Data analysis was performed by BK and AAF. BK, BCCCB, and SA wrote the original draft. Manuscript review
and editing were done by BK, BCCCB, VB, BGS, TBB, JG, MDS, DN, and AAF. All authors have read and agreed to the
published version of the manuscript.

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

JMIR Form Res 2023 | vol. 7 | e44877 | p. 9
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

Conflicts of Interest
None declared.

References

1. Westberg KH, Nyholm M, Nygren JM, Svedberg P. Mental health problems among young people: a scoping review of

help-seeking. Int J Environ Res Public Health 2022;19(3):1430 [FREE Full text] [doi: 10.3390/ijerph19031430] [Medline:
35162452]

3.

6.

4.

5.

2. Mental health of children and young people in England. NHS Digital. 2021. URL: https://digital.nhs.uk/data-and-information/
publications/statistical/mental-health-of-children-and-young-people-in-england/2021-follow-up-to-the-2017-survey/copyright
[accessed 2022-11-01]
Golberstein E, Wen H, Miller BF. Coronavirus disease 2019 (COVID-19) and mental health for children and adolescents.
JAMA Pediatr 2020;174(9):819-820 [FREE Full text] [doi: 10.1001/jamapediatrics.2020.1456] [Medline: 32286618]
Petrovich SB, Gewirtz JL. The attachment learning process and its relation to cultural and biological evolution: proximate
and ultimate considerations. In: The Psychobiology of Attachment and Separation. Orlando, Florida: Academic Press, Inc;
1985:259-291
Burke AR, McCormick CM, Pellis SM, Lukkes JL. Impact of adolescent social experiences on behavior and neural circuits
implicated in mental illnesses. Neurosci Biobehav Rev 2017;76(Pt B):280-300 [FREE Full text] [doi:
10.1016/j.neubiorev.2017.01.018] [Medline: 28111268]
Teicher MH, Andersen SL, Polcari A, Anderson CM, Navalta CP. Developmental neurobiology of childhood stress and
trauma. Psychiatr Clin North Am 2002;25(2):397-426 [FREE Full text] [doi: 10.1016/s0193-953x(01)00003-x] [Medline:
12136507]
Novick AM, Levandowski ML, Laumann LE, Philip NS, Price LH, Tyrka AR. The effects of early life stress on reward
processing. J Psychiatr Res 2018;101:80-103 [FREE Full text] [doi: 10.1016/j.jpsychires.2018.02.002] [Medline: 29567510]
Galea S, Merchant RM, Lurie N. The mental health consequences of COVID-19 and physical distancing: the need for
prevention and early intervention. JAMA Intern Med 2020;180(6):817-818 [FREE Full text] [doi:
10.1001/jamainternmed.2020.1562] [Medline: 32275292]
Rideout V, Peebles A, Mann S, Robb MB. The CommonSense census: media use by tweens and teens. CommonSenseMedia.
2021. URL: https://www.commonsensemedia.org/sites/default/files/research/report/8-18-census-integrated-report-final-web_0.
pdf [accessed 2022-11-01]
Punukollu M, Marques M. Use of mobile apps and technologies in child and adolescent mental health: a systematic review.
Evid Based Ment Health 2019;22(4):161-166 [FREE Full text] [doi: 10.1136/ebmental-2019-300093] [Medline: 31358537]
11. Rickard N, Arjmand HA, Bakker D, Seabrook E. Development of a mobile phone app to support self-monitoring of emotional
well-being: a mental health digital innovation. JMIR Ment Health 2016;3(4):e49 [FREE Full text] [doi: 10.2196/mental.6202]
[Medline: 27881358]

10.

8.

9.

7.

12. Donker T, Petrie K, Proudfoot J, Clarke J, Birch MR, Christensen H. Smartphones for smarter delivery of mental health

programs: a systematic review. J Med Internet Res 2013;15(11):e247 [FREE Full text] [doi: 10.2196/jmir.2791] [Medline:
24240579]

13. Gloster AT, Richard DCS, Himle J, Koch E, Anson H, Lokers L, et al. Accuracy of retrospective memory and covariation

estimation in patients with obsessive-compulsive disorder. Behav Res Ther 2008;46(5):642-655 [FREE Full text] [doi:
10.1016/j.brat.2008.02.010] [Medline: 18417100]

14. Ben-Zeev D, Scherer EA, Wang R, Xie H, Campbell AT. Next-generation psychiatric assessment: using smartphone sensors
to monitor behavior and mental health. Psychiatr Rehabil J 2015;38(3):218-226 [FREE Full text] [doi: 10.1037/prj0000130]
[Medline: 25844912]

15. Canzian L, Musolesi M. Trajectories of depression: unobtrusive monitoring of depressive states by means of smartphone

mobility traces analysis. New York, NY: Association for Computing Machinery; 2015 Presented at: Proceedings of the
2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing; September 7-11, 2015; Osaka, Japan
p. 1293-1304 URL: https://dl.acm.org/doi/abs/10.1145/2750858.2805845 [doi: 10.1145/2750858.2805845]

16. Khwaja M, Pieritz S, Faisal AA, Matic A. Personality and engagement with digital mental health interventions. New York,
NY: Association for Computing Machinery; 2021 Presented at: Proceedings of the 29th ACM Conference on User Modeling,
Adaptation and Personalization; June 21-25, 2021; Utrecht Netherlands p. 235-239 URL: https://dl.acm.org/doi/abs/10.1145/
3450613.3456823 [doi: 10.1145/3450613.3456823]

17. Chittaranjan G, Blom J, Gatica-Perez D. Who's who with big-five: analyzing and classifying personality traits with

smartphones. : IEEE; 2011 Presented at: Proceedings of 15th Annual International Symposium on Wearable Computers;
June 12-15, 2011; San Francisco, CA, USA p. 29-36 URL: https://ieeexplore.ieee.org/abstract/document/5959587 [doi:
10.1109/iswc.2011.29]

18. Khwaja M, Vaid SS, Zannone S, Harari GM, Faisal AA, Matic A. Modeling personality vs. modeling personalidad. Proc

ACM Interact Mob Wearable Ubiquitous Technol 2019;3(3):1-24 [FREE Full text] [doi: 10.1145/3351246]

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

JMIR Form Res 2023 | vol. 7 | e44877 | p. 10
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

19. MacLeod L, Suruliraj B, Gall D, Bessenyei K, Hamm S, Romkey I, et al. A mobile sensing app to monitor youth mental

health: observational pilot study. JMIR Mhealth Uhealth 2021;9(10):e20638 [FREE Full text] [doi: 10.2196/20638] [Medline:
34698650]

20. Melbye S, Kessing LV, Bardram JE, Faurholt-Jepsen M. Smartphone-based self-monitoring, treatment, and automatically
generated data in children, adolescents, and young adults with psychiatric disorders: systematic review. JMIR Ment Health
2020;7(10):e17453 [FREE Full text] [doi: 10.2196/17453] [Medline: 33118950]

21. Livingstone S, Stoilova M, Nandagiri R. Children's data and privacy online: growing up in a digital age: an evidence review.

In: LSE Research Online. London: London School of Economics and Political Science; 2019.
22.
ICH Harmonised Guideline. Guideline for good clinical practice. J Postgrad Med 2001;47(3):199-203
ioS - Apple. Apple Inc. 2021. URL: https://www.apple.com/uk/ios/ios-15/ [accessed 2022-11-01]
23.
24. Android - Open Handset Alliance. Google Inc. URL: https://www.android.com/ [accessed 2022-11-01]
25. Chandrashekar P. Do mental health mobile apps work: evidence and recommendations for designing high-efficacy mental
health mobile apps. Mhealth 2018;4:6 [FREE Full text] [doi: 10.21037/mhealth.2018.03.02] [Medline: 29682510]
26. Lau N, O'Daffer A, Yi-Frazier JP, Rosenberg AR. Popular evidence-based commercial mental health apps: analysis of

engagement, functionality, aesthetics, and information quality. JMIR Mhealth Uhealth 2021;9(7):e29689 [FREE Full text]
[doi: 10.2196/29689] [Medline: 34259639]

27. Mental health innovations. Shout. URL: https://www.giveusashout.org/ [accessed 2022-11-01]
28. YoungMinds. YoungMinds. URL: https://youngminds.org.uk/ [accessed 2022-11-01]
29. Best For You. NHS. URL: https://bestforyou.org.uk/ [accessed 2022-11-01]
30. Kooth PLC. Kooth. URL: https://www.kooth.com/ [accessed 2022-11-01]
31. Norman DA, Draper SW, editors. User Centered System Design: New Perspectives on Human-Computer Interaction.

Hillsdale, NJ: Lawrence Erlbaum Associates; 1986.

32. Kauer SD, Reid SC, Crooke AHD, Khor A, Hearps SJC, Jorm AF, et al. Self-monitoring using mobile phones in the early

stages of adolescent depression: randomized controlled trial. J Med Internet Res 2012;14(3):e67 [FREE Full text] [doi:
10.2196/jmir.1858] [Medline: 22732135]

33. Kenny R, Dooley B, Fitzgerald A. Feasibility of "CopeSmart": a telemental health app for adolescents. JMIR Ment Health

34.

2015;2(3):e22 [FREE Full text] [doi: 10.2196/mental.4370] [Medline: 26552425]
Peng W, Kanthawala S, Yuan S, Hussain SA. A qualitative study of user perceptions of mobile health apps. BMC Public
Health 2016;16(1):1158 [FREE Full text] [doi: 10.1186/s12889-016-3808-0] [Medline: 27842533]

35. Anderson K, Burford O, Emmerton L. Mobile health apps to facilitate self-care: a qualitative study of user experiences.

PLoS One 2016;11(5):e0156164 [FREE Full text] [doi: 10.1371/journal.pone.0156164] [Medline: 27214203]
36. Baumel A, Muench F, Edan S, Kane JM. Objective user engagement with mental health apps: systematic search and
panel-based usage analysis. J Med Internet Res 2019;21(9):e14567 [FREE Full text] [doi: 10.2196/14567] [Medline:
31573916]

37. Kaveladze BT, Wasil AR, Bunyi JB, Ramirez V, Schueller SM. User experience, engagement, and popularity in mental

health apps: secondary analysis of app analytics and expert app reviews. JMIR Hum Factors 2022;9(1):e30766 [FREE Full
text] [doi: 10.2196/30766] [Medline: 35099398]

38. Torous J, Staples P, Onnela JP. Realizing the potential of mobile mental health: new methods for new data in psychiatry.

Curr Psychiatry Rep 2015;17(8):602 [FREE Full text] [doi: 10.1007/s11920-015-0602-0] [Medline: 26073363]
39. Rabbi M, Ali S, Choudhury T, Berke E. Passive and in-situ assessment of mental and physical well-being using mobile

sensors. New York, NY, United States: Association for Computing Machinery; 2011 Presented at: Proceedings of the 13th
International Conference on Ubiquitous Computing; September 17-21, 2011; Beijing, China p. 385-394 URL: https://dl.
acm.org/doi/abs/10.1145/2030112.2030164 [doi: 10.1145/2030112.2030164]
Insel TR. Digital phenotyping: technology for a new science of behavior. JAMA 2017;318(13):1215-1216 [FREE Full text]
[doi: 10.1001/jama.2017.11295] [Medline: 28973224]

40.

41. Wahle F, Kowatsch T, Fleisch E, Rufer M, Weidt S. Mobile sensing and support for people with depression: a pilot trial
in the wild. JMIR Mhealth Uhealth 2016;4(3):e111 [FREE Full text] [doi: 10.2196/mhealth.5960] [Medline: 27655245]
42. DeMasi O, Feygin S, Dembo A, Aguilera A, Recht B. Well-being tracking via smartphone-measured activity and sleep:

cohort study. JMIR Mhealth Uhealth 2017;5(10):e137 [FREE Full text] [doi: 10.2196/mhealth.7820] [Medline: 28982643]

43. Cao J, Truong AL, Banu S, Shah AA, Sabharwal A, Moukaddam N. Tracking and predicting depressive symptoms of

adolescents using smartphone-based self-reports, parental evaluations, and passive phone sensor data: development and
usability study. JMIR Ment Health 2020;7(1):e14045 [FREE Full text] [doi: 10.2196/14045] [Medline: 32012072]

44. Matthews M, Abdullah S, Murnane E, Voida S, Choudhury T, Gay G, et al. Development and evaluation of a

45.

smartphone-based measure of social rhythms for bipolar disorder. Assessment 2016;23(4):472-483 [FREE Full text] [doi:
10.1177/1073191116656794] [Medline: 27358214]
Faurholt-Jepsen M, Vinberg M, Frost M, Christensen EM, Bardram J, Kessing LV. Daily electronic monitoring of subjective
and objective measures of illness activity in bipolar disorder using smartphones– the MONARCA II trial protocol: a
randomized controlled single-blind parallel-group trial. BMC Psychiatry 2014;14(1):309 [FREE Full text] [doi:
10.1186/s12888-014-0309-5] [Medline: 25420431]

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

JMIR Form Res 2023 | vol. 7 | e44877 | p. 11
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

46. Berrouiguet S, Ramírez D, Barrigón ML, Moreno-Muñoz P, Carmona Camacho R, Baca-García E, et al. Combining
continuous smartphone native sensors data capture and unsupervised data mining techniques for behavioral changes
detection: a case series of the evidence-based behavior (eb2) study. JMIR Mhealth Uhealth 2018;6(12):e197 [FREE Full
text] [doi: 10.2196/mhealth.9472] [Medline: 30530465]

47. Wang R, Aung MS, Abdullah S, Brian R, Campbell AT, Choudhury T, et al. CrossCheck: toward passive sensing and

detection of mental health changes in people with schizophrenia. New York, NY: Association for Computing Machinery;
2016 Presented at: Proceedings of the 2016 ACM International Joint Conference on Pervasive and Ubiquitous Computing;
September 12-16, 2016; Heidelberg, Germany p. 886-897 URL: https://dl.acm.org/doi/abs/10.1145/2971648.2971740 [doi:
10.1145/2971648.2971740]

49.

48. Beiwinkel T, Kindermann S, Maier A, Kerl C, Moock J, Barbian G, et al. Using smartphones to monitor bipolar disorder
symptoms: a pilot study. JMIR Mental Health 2016;3(1):e2 [FREE Full text] [doi: 10.2196/mental.4560] [Medline: 26740354]
Jacobson NC, Chung YJ. Passive sensing of prediction of moment-to-moment depressed mood among undergraduates with
clinical levels of depression sample using smartphones. Sensors (Basel) 2020;20(12):3572 [FREE Full text] [doi:
10.3390/s20123572] [Medline: 32599801]
Schueller SM, Begale M, Penedo FJ, Mohr DC. Purple: a modular system for developing and deploying behavioral
intervention technologies. J Med Internet Res 2014;16(7):e181 [FREE Full text] [doi: 10.2196/jmir.3376] [Medline:
25079298]

50.

51. Gideon J, Provost EM, McInnis M. Mood state prediction from speech of varying acoustic quality for individuals with

bipolar disorder. : IEEE; 2016 Presented at: Proceeding of 2016 IEEE International Conference on Acoustics, Speech and
Signal Processing (ICASSP); March 20-25, 2016; Shanghai, China p. 2359-2363 URL: https://ieeexplore.ieee.org/document/
7472099 [doi: 10.1109/icassp.2016.7472099]

52. Opoku AK, Visuri A, Ferreira DS. Towards early detection of depression through smartphone sensing. New York, NY,

United States: Association for Computing Machinery; 2019 Presented at: Adjunct Proceedings of the 2019 ACM International
Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2019 ACM International Symposium
on Wearable Computers; September 9-13, 2019; London, United Kingdom p. 1158-1161 URL: https://doi.org/10.1145/
3341162.3347075 [doi: 10.1145/3341162.3347075]

53. Dargél AA, Mosconi E, Masson M, Plaze M, Taieb F, Von Platen C, et al. Toi Même, a mobile health platform for measuring
bipolar illness activity: protocol for a feasibility study. JMIR Res Protoc 2020;9(8):e18818 [FREE Full text] [doi:
10.2196/18818] [Medline: 32638703]

54. Mullick T, Radovic A, Shaaban S, Doryab A. Predicting depression in adolescents using mobile and wearable sensors:
multimodal machine learning-based exploratory study. JMIR Form Res 2022;6(6):e35807 [FREE Full text] [doi:
10.2196/35807] [Medline: 35749157]

55. Maharjan SM, Poudyal A, van Heerden A, Byanjankar P, Thapa A, Islam C, et al. Passive sensing on mobile devices to

improve mental health services with adolescent and young mothers in low-resource settings: the role of families in feasibility
and acceptability. BMC Med Inform Decis Mak 2021;21(1):117 [FREE Full text] [doi: 10.1186/s12911-021-01473-2]
[Medline: 33827552]

56. Aryana B, Brewster L, Nocera JA. Design for mobile mental health: an exploratory review. Health Technol 2018;9(4):401-424

[FREE Full text] [doi: 10.1007/s12553-018-0271-1]

57. Vial S, Boudhraâ S, Dumont M. Human-centered design approaches in digital mental health interventions: exploratory

mapping review. JMIR Ment Health 2022;9(6):e35591 [FREE Full text] [doi: 10.2196/35591] [Medline: 35671081]

58. Grist R, Porter J, Stallard P. Mental health mobile apps for preadolescents and adolescents: a systematic review. J Med

59.

Internet Res 2017;19(5):e176 [FREE Full text] [doi: 10.2196/jmir.7332] [Medline: 28546138]
Sardi L, Idri A, Fernández-Alemán JL. A systematic review of gamification in e-Health. J Biomed Inform 2017;71:31-48
[FREE Full text] [doi: 10.1016/j.jbi.2017.05.011] [Medline: 28536062]

60. Merry SN, Stasiak K, Shepherd M, Frampton C, Fleming T, Lucassen MFG. The effectiveness of SPARX, a computerised
self help intervention for adolescents seeking help for depression: randomised controlled non-inferiority trial. BMJ
2012;344:e2598 [FREE Full text] [doi: 10.1136/bmj.e2598] [Medline: 22517917]

61. Duan L, Street WN, Xu E. Healthcare information systems: data mining methods in the creation of a clinical recommender

system. Enterp Inf Syst 2011;5(2):169-181 [FREE Full text] [doi: 10.1080/17517575.2010.541287]

62. Rabbi M, Aung MH, Zhang M, Choudhury T. MyBehavior: automatic personalized health feedback from user behaviors
and preferences using smartphones. New York, NY, United States: Association for Computing Machinery; 2015 Presented
at: Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing; September 7-11,
2015; Osaka, Japan p. 707-718 URL: https://dl.acm.org/doi/10.1145/2750858.2805840 [doi: 10.1145/2750858.2805840]
63. Khwaja M, Ferrer M, Iglesias JO, Faisal AA, Matic A. Aligning daily activities with personality: towards a recommender

system for improving wellbeing. New York, NY, United States: Association for Computing Machinery; 2019 Presented
at: Proceedings of the 13th ACM Conference on Recommender Systems; September 16-20, 2019; Copenhagen, Denmark
p. 368-372 URL: https://dl.acm.org/doi/10.1145/3298689.3347020 [doi: 10.1145/3298689.3347020]

64. Mulani J, Heda S, Tumdi K, Patel J, Chhinkaniwala H, Patel J. Deep reinforcement learning based personalized health

recommendations. In: Deep Learning Techniques for Biomedical and Health Informatics. Cham: Springer; 2020:231-255

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

JMIR Form Res 2023 | vol. 7 | e44877 | p. 12
(page number not for citation purposes)

JMIR FORMATIVE RESEARCH

Kadirvelu et al

65.

66.

Pieritz S, Khwaja M, Faisal AA, Matic A. Personalised recommendations in mental health apps: the impact of autonomy
and data sharing. New York, NY, United States: Association for Computing Machinery; 2021 Presented at: Proceedings
of the 2021 CHI Conference on Human Factors in Computing System; May 8-13, 2021; Yokohama, Japan p. 1-12 URL:
https://dl.acm.org/doi/abs/10.1145/3411764.3445523 [doi: 10.1145/3411764.3445523]
Pearson J, Naselaris T, Holmes EA, Kosslyn SM. Mental imagery: functional mechanisms and clinical applications. Trends
Cogn Sci 2015;19(10):590-602 [FREE Full text] [doi: 10.1016/j.tics.2015.08.003] [Medline: 26412097]

Abbreviations

CYP:  children and young people
UI:  user interface

Edited by A Mavragani; submitted 07.12.22; peer-reviewed by Y Khazaal, D Bakker; comments to author 02.02.23; revised version
received 24.04.23; accepted 15.05.23; published 26.06.23

Please cite as:
Kadirvelu  B,  Bellido  Bel  T,  Wu  X,  Burmester  V,  Ananth  S,  Cabral  C  C  Branco  B,  Girela-Serrano  B,  Gledhill  J,  Di  Simplicio  M,
Nicholls D, Faisal AA
Mindcraft, a Mobile Mental Health Monitoring Platform for Children and Young People: Development and Acceptability Pilot Study
JMIR Form Res 2023;7:e44877
URL: https://formative.jmir.org/2023/1/e44877
doi: 10.2196/44877
PMID:

©Balasundaram Kadirvelu, Teresa Bellido Bel, Xiaofei Wu, Victoria Burmester, Shayma Ananth, Bianca Cabral C C Branco,
Braulio  Girela-Serrano,  Julia  Gledhill,  Martina  Di  Simplicio,  Dasha  Nicholls,  A  Aldo  Faisal.  Originally  published  in  JMIR
Formative Research (https://formative.jmir.org), 26.06.2023. This is an open-access article distributed under the terms of the
Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution,
and reproduction in any medium, provided the original work, first published in JMIR Formative Research, is properly cited. The
complete bibliographic information, a link to the original publication on https://formative.jmir.org, as well as this copyright and
license information must be included.

https://formative.jmir.org/2023/1/e44877

XSL•FO
RenderX

JMIR Form Res 2023 | vol. 7 | e44877 | p. 13
(page number not for citation purposes)
