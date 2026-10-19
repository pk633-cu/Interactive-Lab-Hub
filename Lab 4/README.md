# Ph-UI!!!

<details>
	<summary><strong>Instructions for Students (Click to Expand)</strong></summary>
  
	**Submission Cleanup Reminder:**
	- This README.md contains extra instructional text for guidance.
	- Before submitting, remove all instructional text and example prompts from this file.
	- You may delete these sections or use the toggle/hide feature in VS Code to collapse them for a cleaner look.
	- Your final submission should be neat, focused on your own work, and easy to read for grading.
  
	This helps ensure your README.md is clear, professional, and uniquely yours!
</details>

---

## Lab Overview
Members: Abiola Bolaji (ab3394), Pallavi Srinivas (ps2269), Pallavi Khanna (pk633)  
Project name: Snack Locker - A locker that holds someone's snack and only opens when the owner of the snack is detected.

---

## Part 1 Lab Preparation

---

**\*\*\*Draw 5 sketches that explore different physical arrangements for your sensing and actuation.\*\*\***

Before we drew the sketches, we came with potential ideas: 

- Snack guard/locker - Someone reaches for your snack, the machine slaps the hand or shuts the lid
- Last-slice decider - Device decides who gets the last piece 
- Secret Snack Drawer
- Takeout roulette
- Shared serving platter - hover your hand over your plate and the platter rotates towards you
- Water Alarm coaster
- Hot plate sensor

Our group decided to go with the snack guard. Here are some feature ideas we came up with:

<img width="2269" height="1021" alt="feastautomataideationsketches" src="https://github.com/user-attachments/assets/7427cff3-630a-4315-96ef-ccb72db1e78b" />

<img width="1080" height="582" alt="Screenshot 2026-10-18 at 6 24 44 PM" src="https://github.com/user-attachments/assets/122a5f97-5825-4299-9ddc-0e4c29780b3a" />


**\*\*\*What questions do these sketches raise? What do you need to physically prototype to answer them?\*\*\***

These sketches raises the question of what is the most effective combination of these features that make the interaction function properly and also help the user understand the interaction. To answer this, we needed to understand if we were only going to use a sensing device or have a container that would hold the snack. Since the only function the sensing device would perform is detecting if a hand was approaching, we decided the best approach was to create a container that controls the access to the snack where a door would open if the correct person was approaching. These are some additional questions that were raised and what we had to prototype to answer them:

- How are we going to create the door that controls the access the snack? We had to prototype how the door was going to open without someone physically controlling the door.

- Where the sensor should go so it effectively senses the hand? We had to prototype the location of the sensor so it not only senses hands approaching, but also is out of sight, so it gives the illusion of the locker automatically opening when the right user approaches.

- How will we provide feedback to the user? We also had to prototype ways in which the device would give feedback to the user so they understood how the device worked.

**\*\*\*Pick one design to prototype and explain why.\*\*\***

We decided to prototype sketches 1, 3, and 4 which detects the hand approaching, a container opening to give access to the snack, and an OLED that conveys to the user if "enjoy your snack" or "hands off!" depending if the right user is approaching. We chose these three sketches because together they cover the entire end-to-end interaction of detecting a hand approaching, giving access to the user or not, and also providing feedback to the user.

**\*\*\*Document your rough prototype with photos and/or video.\*\*\***

For this part, we created two rough prototypes. One where the door opens giving access to the snack (shows a green light indicating that users can grab their snack), another where the door stays shut when the wrong user tries to access the snack (shows a red light indicating the door cannot be opened and users do not have access to the snack). We also tried to avoid physically controlling the box with our hands to replicate the door opening automatically

Device giving access to the user:

https://drive.google.com/file/d/1QUiI4bw2iPvYt4MUyNlVRE55Xix_LRF7/view

Device NOT giving access to the user:

https://drive.google.com/file/d/1Cm143OVSPXO89pOUxttV00NQb47jOupo/view

---

## Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

---

### Part E/F

#### Build & Integrate: Sensing + Actuation

For Part 2, build the Feast Automata interaction you developed in Part D by connecting sensing/input to physical actuation.

**Your prototype should:**
- Use at least one sensing or input device.
- Use servo-based physical actuation.
- Connect sensing and actuation into a meaningful interaction around eating, drinking, cooking, serving, or sharing food.
- Additional inputs, displays, LEDs, buttons, or other outputs are optional extensions.

**Document your system with:**
- Code for your sensing + actuation prototype
- Photos and/or video of the working prototype in action
- A simple interaction diagram or sketch showing how sensing and actuation are connected
- Written reflection: What did you learn about connecting sensing, movement, and physical form? What was fun, surprising, or challenging?

**Questions to consider:**
- How does your chosen sensor or input shape the physical response?
- How does the physical arrangement of the sensor and actuator change the interaction?
- What thresholds, timing, or movement patterns make the interaction feel clear or playful?
- What changes when you adjust the sensor placement or servo motion?

#### Snack Guard/Locker

**Code:** https://github.com/pk633-cu/Interactive-Lab-Hub/blob/Fall2026/Lab%204/snack_guard.py 

First we figured out how our door should function:

https://github.com/user-attachments/assets/d267a7b1-15e9-4ae4-b2b2-6bd0cd530df8

Then we created our setup and also secured the door:

<img width="3024" height="4032" alt="IMG_3788" src="https://github.com/user-attachments/assets/de29c76f-8f8e-4dae-bd56-06d173ac8b91" />

After, we created the interaction where the device grants access to the user:

https://github.com/user-attachments/assets/4dda83be-843b-47bc-8511-4f93e2557a5c

Lastly, we created the interaction where the device closes when the wrong user approaches:

https://github.com/user-attachments/assets/69a3d8f9-f87b-4631-9f4c-28338ca30623

**Diagram - how sensing and actuation are connected**

```text
VCNL4040 proximity sensor ──► Raspberry Pi (snack_guard.py) ──► Servo pHAT ──► servo rotates door open/closed
                                         │
                                         └──► Qwiic OLED ──► "Hi Enjoy Your Snack!" / "THIS IS NOT YOUR SNACK!"

reading < 1      → nothing there: door closed, screen blank
reading 1–10     → one hand: door rotates open 90°, holds 5 s, then closes slowly
reading > 10     → more than one hand: door closes right away, warning on screen
```

**How does your chosen sensor or input shape the physical response?** The VCNL4040 proximity sensor gives a number that gets bigger as more stuff is in front of it. A reading of 1–10 counts as one hand, so the servo rotates the door open and the OLED says "Hi Enjoy Your Snack!" A reading above 10 means more than one hand (someone else is reaching in), so the door swings shut right away and the screen says "THIS IS NOT YOUR SNACK!" Since the sensor only measures how close and how much is in front of it, the response is based on how many hands are there, not on who they belong to.

**How does the physical arrangement of the sensor and actuator change the interaction?** The sensor is mounted on the side of the snack bowl, where a hand naturally reaches. The servo is attached to the door right next to it, so the door opens exactly where the hand is already reaching. Keeping the sensor, door, and screen close together makes cause and effect obvious: reach toward the snack, the door opens, and the message appears.

**What thresholds, timing, or movement patterns make the interaction feel clear or playful?**

Thresholds: 1–10 opens the door, above 10 triggers the warning, and below 1 clears the screen.
The door opens one degree at a time (about 1.8 s to go 90°). It feels like the door is welcoming you instead of snapping open.
The door stays open for 5 seconds so the user has time to grab a snack, then closes even more slowly.
The sensor keeps being read while the door moves, so a second hand can swing it shut mid-motion. That's the playful "caught you" moment.
What changes when you adjust the sensor placement or servo motion? If the sensor is too close to the door or angled up, the moving door or the snack itself can change the reading and trigger it by accident. Placing it farther from where people naturally reach makes it miss hands. Making the servo faster made the door feel abrupt and startling. Making it slower made it feel more deliberate and friendly, but if the close is too slow, someone else can still sneak a snack in.

**REFLECTION**

**What did you learn about connecting sensing, movement, and physical form? What was fun, surprising, or challenging?**

From this project, I learned how sensing, movement, and physical form work together to shape devices in modern day tech. Proximity and other types of sensors sense movement from users and the physical form or UI allows users to understand how to interact with the device. In this case, the proximity sensor sense hand movements and then prompts the servo motor to function/slide the door open, enabling access to the snack. One thing that we found particularly challenging was actually building the physical UI as we spent a lot of time trying to figure our how we would make the door function with the servo motor. However, once we figured that out, it was fun finding ways to enhance the prototype to make it easier and more fun for the user to interact with.
