Abstract
Given the advancements in autonomous technology being developed in a wide-ranging fields from automotive, cleaning systems, 
and to even cooking devices, it is clear that the development of a proper lawn maintenance system will prove popular within 
the current market if done properly. Currently, there does exist autonomous lawn management systems on the market. However, 
the current products are rather expensive and do not provide an exceptionally clean mowing pattern, whereas they mow in a 
random pattern that is based only upon how the mower rebounds off of the boundary and turns away much like the Roomba vacuum 
currently on the market.

Introduction
The goal of this project was to design, build and test an autonomous lawn mower that is capable of producing an appealing cut 
pattern on the grass. The inspiration for this project were the long days spent mowing lawns in the Las Vegas summer. 
By implementing a semi-autonomous lawn mower time could be saved to participate in activities more enjoyable. The physical 
design of the mower has been through a few rounds of revisions whereas the electrical and controls design of the mower has 
stayed relatively constant. The changes made to the physical design of the mower were born out of three ideas. The first was 
to make the design more efficient. The second was to reduce the cost. The last, and most important to us, was to increase the 
skills learned while completing the project. The goal was to find a middle ground that limited the need to large and expensive
machinery as well as would provide an interesting challenge to build. This resulted in the final design constructed out of 
aluminum square tubing and plexiglass. The revision made to the controls portion of the system were made early in the design 
stage. The change that was made changed the basic phenomenon that was used to guide the mower. Originally, the plan was to 
bury a conductor in the lawn that would act as a source of power to charge as well as to guide the mower. This was changed 
to implementing a GPS unit for guidance.

Goals
The goals of our design are as follows:

Size mower to limit the time needed to mow an average size lawn.
Size the motors so that they are capable of handing the weight of mower on both flat and sloped lawns.
Be able to mow a 20’ x 20’ area on a single charge.
Include safety features such as:
Irregular motion detection
Object detection
Obstacle detection
Communication with weather services.
Schedulable cycles.
Base with charging functionality.
Given the nature of the project, there was little constraints in the construction or design of the mower, other than being 
able to keep the budget under $2,000.

Design
The main outcome of SCABY was to design and build an autonomous lawn mower that required no input from the user beyond the 
initial set up and installation. To achieve this, we chose to utilize a GPS navigation system called MarvelMind. MarvelMind 
is a complete time-of-flight tracking system that is accurate to within ±2cm. The program used for this algorithm works by 
using four stationary perimeter beacons and two mobile beacons mounted on SCABY. While the mower is moving, the mobile beacons 
are able to communicate with one another through a Raspberry Pi and pinpoint its position on the lawn by using the stationary
beacons.

Future Enhancements
The original objective of this project was to design and build a lawn mower that can cut a unique pattern on a desired area 
of grass. SCABY currently operates using remote control capabilities. Some advancements to SCABY include the ability to 
control the mower from your phone or being able to connect it to Alexa. Another enhancement is the ability to be able to 
cut any type of pattern and the ability to customize coordinate or cut creative shapes and deigns. Currently SCABY is 
equipped with a gyroscope that allows it to safely turn off the power to the cutting blade when the body of the mower is 
lifted off the ground. Other safety measures can also be like obstacle avoidance and an alarm system. The navigation system 
was meant to use a tracking algorithm to pinpoint its position on the lawn. One potential improvement is to switch to another 
system to be able to complete a unique pattern. An example of a different system is image recognition. This type of system 
would eliminate the need for any type or perimeter wire or beacons.
