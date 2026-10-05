# Chatterboxes

Pallavi Khanna

# Part 1

## A. Text to Speech

Your Pi can speak in several quite different ways, and the differences are audible in a way that matters for design. In `speech-scripts/` there are shell scripts for each.

### The classic engines

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

[My shell file for Pi greeting me](speech-scripts/pallavi_greeting.sh) 

\*\***Then answer: Is the same greeting, in these different voices, the same greeting? Describe one concrete way the voice changed what the utterance seemed to mean or who seemed to be speaking.**\*\*

No, the same greeting is not the same greeting because some of the voices are more enthusiasitic than others signifying who you are communicating to. For instance, more enthuisiastic tones can be a friend versus more solemn tones can be a coworker/professional interaction. Some the tones in this part are also more robotic, signifying that you’re talking to a computer.

## B. Speech to Text

\*\***Record a few seconds of your own speech (`arecord -d 5 -f cd -c 1 -r 16000 test.wav`) and transcribe it with at least two model sizes. Report the real-time factor for each. At what point does the accuracy improvement stop being worth the delay, for a system that has to answer you?**\*\*

Tiny.en - 0.22x
Small. en - 1.27x
Base.en - 0.44x
Medium.en - 3.51x

The small.en took a reasonable amount of time and also produced one of the most accurate results. Even though medium.en produced the most accurate answer, it took too long to load. When a user is interacting with a product that uses medium.en, they may not have enough patience to wait that long or think the deviced crashed and end up existing out.

\*\***Write your own script that verbally asks for a numerical input (a phone number, zipcode, number of pets) and records the answer the respondent provides.**\*\* Numbers are a good stress test — transcription systems make characteristic errors on digit strings, and you will want to know what they are before you design around them.

[Script asking for a numerical input](speech-scripts/zipcode_question.sh) 

## C. Turn-taking: knowing when someone has stopped talking

\*\***Try both extremes, and something in between. Describe what each one feels like to talk to. Note specifically: at 0.2s, what kinds of normal speech get cut off? At 1.5s, what does the delay make the system seem like?**\*\*

When I tried the 0.2, the system cut me off when I was taking a breath in the middle of my sentence. On the other hand, when I tried 1.5, the system cut me off when I deliberately paused to think what else to say. Lastly, 0.7 cut me off when I finished a sentence. From this, I felt as if the endpointing threshold with the lower values were transcribing my answers and giving feedback in real-time, while the thresholds with the higher values waited till I was finished with my thought to fully transcribe what I was saying.

There is no correct value. A system that takes drink orders and a system that listens to someone think out loud want very different thresholds, and the right one depends on what your users are doing with their pauses.

## D. Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.)

**Speech-Enabled Medicine/Vitamin Schedule Assistant:** For this lab, I decided to create an assistant where the user can input the schedule of the medicines/vitamins they plan to take throughout the week and the speech-enabled device reminds them to take which medicine and when. I decided to make two possible scenarios:

1. Device-initiated - Where the device initiates the interaction at a specific time.
2. User-initiated - Where the user, themselves, asks which medicine/vitamin they are currently scheduled to take.

<img width="2466" height="2250" alt="speech-enabled medication vitamin schedule Assistant" src="https://github.com/user-attachments/assets/6ced23b3-e17f-4524-96a4-71ef307d5a21" />

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses.

<img width="666" height="692" alt="Screenshot 2026-09-28 at 10 09 11 PM" src="https://github.com/user-attachments/assets/a70b4049-4454-4097-8733-c61b1a0419a9" />
<img width="644" height="258" alt="Screenshot 2026-09-28 at 10 12 05 PM" src="https://github.com/user-attachments/assets/0c34789e-4a61-4030-9494-4ec2c5c0d08e" />

The Script

<img width="630" height="244" alt="Screenshot 2026-09-28 at 10 12 18 PM" src="https://github.com/user-attachments/assets/d2ccfaf4-8d7e-4213-9f11-8b3c70612d74" />

## E. Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing. Please record this interaction (for example, using Zoom's record feature).

When deciding which dialogue to test out, I actually re-visited the device-initiated dialogue and tested that one out as well.

Scenario 1 - Starts with user picking up the wrong medication
https://github.com/user-attachments/assets/ec49aab1-d4bc-4565-b5ea-5d7b387b01d1

Scenario 2 - Device-Initiated - Device wakes up the user/interrupts whatever task they’re doing and tells them to take medication
https://github.com/user-attachments/assets/cef8ed50-eedf-404f-b474-ddc50de0f420

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

When we acted out the dialogue, I found that were actually going faster than the 1.2 second parameter that I added between the user and device dialogues. Considering how short the interaction and user dialogue was, the device does not have to spend a long time processing what the user is saying. So the parameter between dialogues should be smaller.

---

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings.

Something I could improve are the timing by decreasing the parameter between each dialogue to make the prototype more efficient and engaging, so users don't get impatient and give up on the device. Another thing I would improve is the device anticipating different ways users say the same thing. This would allow the interaction to feel more natural and accessible to users with different dialects.

3. What are other modes of interaction *beyond speech* that you might also use to clarify how to interact? In particular: how does someone know when the device is listening, and when it is thinking? You have a screen and an LED.

I could use the screen to indicate what the device is saying, and what it's doing when the user is talking or when the device is processing.

5. Make a new storyboard, diagram and/or script based on these reflections.

For my final script, I decided to merge the two dialogues I tested out. In a real world situation, the device-initiated scenario would be applicable to more users, however, I also wanted to highlight the device's ability to proactively correct the user when they are about to take the wrong medication.

So this is the final script I ended up with:

Device: Good morning! Reminder to take your medication.

User: What medication do I take?

    [Device waits 0.6 seconds]
    
Device: You have Vitamin D scheduled for this morning.

User: I thought I was supposed to take folic acid.

    [Device waits 0.6 seconds]
    
Device: Folic acid is scheduled for this evening. Please take Vitamin D.

User: Done.

    [Device waits 0.6 seconds]
    
Device: Great! Recorded that you have taken Vitamin D.

## Prototype your system

The system should:
* use the Raspberry Pi
* use one or more sensors
* require participants to speak to it

*Document how the system works.*
This device is MedSched, a voice assistant that reminds users to take their medication according to their pre-set medication schedule. The device starts the interaction by reminding the user to take their medication. If users aren't sure which medication they should take and when, they can ask the voice assistant. If the voice assistant detects that the user is about to take the wrong medication at the wrong time, it corrects the user and tells them which medication they should take instead.

The system leverages speech recognition to transcribe users' verbal responses and provide a response based on their input. The device also has a user interface that communicates what the device is saying, when it is listening, and when it is preparing a response. This provides users with visual feedback in addition to the voice interaction.

The user flow of the system:
MedSched reminder --> User responds (The device shows "listening" on the UI) --> the system transcribes the user response --> Process the information the user provided (shows "thinking") --> MedSched responds and shows its response on the screen 

To create this I made two python files - 
[MedSched Voice Assistant0]([Lab 3/medsched_assistant.py](https://github.com/pk633-cu/Interactive-Lab-Hub/blob/Fall2026/Lab%203/medsched_assistant.py)) 
[MedSched UI](https://github.com/pk633-cu/Interactive-Lab-Hub/blob/Fall2026/Lab%203/medsched_screen.py)

*Include videos or screencaptures of both the system and the controller.*
The Interaction 
https://github.com/user-attachments/assets/e6f49826-00b8-4b99-9075-5df05ad787d3

User interacting with the device
https://github.com/user-attachments/assets/b99f72e4-ab81-44fe-8163-5cb98184bb30

The system UI 
https://github.com/user-attachments/assets/6e612b88-691b-4155-9d5e-ac4502d4d813

The controller - shows the terminal executing the interaction and recognizing/transcribing users' speech
https://github.com/user-attachments/assets/2c9edef2-18f9-4453-812d-a9641d393686

## Test the system

Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard *after* the interaction, but we recognize that can be hard.)

### What worked well about the system and what didn't?
What worked well was that the screen provided constant feedback to the user, like when it was listening and once it was processing what the user said. Another thing that worked well was that the device anticipated users saying the same thing in different ways. 

What didn't work well was users sometimes had to annunciate what they were saying as the speech recognition was not always accurate. Another thing that could have been improved is that the captions generally appeared way earlier than when the device actually started speaking.

### What worked well about the controller and what didn't?
Things that worked well about the controller were that it showed what the user said and whether the device was thinking, listening, or speaking. This made it easy to understand what was happening behind the scenes and when the system recognized speech incorrectly. However, since I programmed it to anticipate for different words and different variations of phrases, it only recognizes those phrases/words.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
Something I learned from WoZ interactions is the importance of understanding how users naturally interact with a system before building the device. Users can speak or behave differently than expected which can reveal things that were not initially considered. Additionally, it's also important to provide clear feedback to the user through the interaction, like communicating what the system is doing behind the scenes, to help users plan their next course of action.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
Some data I could collect is recording a diverse set of users' speech and how the system transcribes the responses to help improve accuracy of speech recognition. Additionally, I could also collect data on how long users take to respond, how long pauses are, and how long the interactions last along with at which point users decide to end the interaction. This could help improve the time in between each response and increase the amount of users that stay through the whole interaction. Another modality I can use is a camera, for instances where users accidentally pick up the wrong medication and to capture facial expressions where users may be confused about what medication they should take - signaling an automatic response from the device.

<details>
  <summary><strong>Submission Cleanup Reminder (Click to Expand)</strong></summary>

  **Before submitting your README.md:**
  - This readme.md file has a lot of extra text for guidance.
  - Remove all instructional text and example prompts from this file.
  - You may either delete these sections or use the toggle/hide feature in VS Code to collapse them for a cleaner look.
  - Your final submission should be neat, focused on your own work, and easy to read for grading.
</details>
