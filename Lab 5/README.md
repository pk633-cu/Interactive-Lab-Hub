# Observant Systems: Overnight Sensation

Abiola Bolaji (ab3394), Pallavi Srinivas (ps2269), Pallavi Khanna (pk633)

---

# Part 1

## Part A. 
### Set up your Pi for on-device AI

\*\*\***Include a screenshot of `ollama list` showing your models, and the `bus.jpg` result and your own photo with their boxes.**\*\*\*

bus.jpg Results

<img width="560" height="746" alt="Screenshot 2026-10-21 at 7 28 44 PM" src="https://github.com/user-attachments/assets/1579abe6-af64-47a5-bd3c-db586758b77a" />

My photo

<img width="1208" height="906" alt="Screenshot 2026-10-21 at 7 28 53 PM" src="https://github.com/user-attachments/assets/4090ad95-d323-4e8f-9d8a-f41cab831aa4" />

'ollama list'
<img width="1060" height="150" alt="Screenshot 2026-10-21 at 7 31 07 PM" src="https://github.com/user-attachments/assets/acb7813b-2347-4584-b6fc-23cc890a3116" />

## Part B. 
### See: recognize people in real time with YOLO

\*\*\***Include a short video or screenshots of the person detection. Write down three situations where it did not see you, or saw a person who was not there, and what you think the cause was.**\*\*\*

https://github.com/user-attachments/assets/df576105-af74-4f45-83bd-5d3d23cb406b

https://github.com/user-attachments/assets/7e35b8ff-4723-4b04-8aae-043d2c977be8

https://github.com/user-attachments/assets/c746388e-c541-4893-b5c3-8cb092499369

<img width="1284" height="1020" alt="Screenshot 2026-10-25 at 7 42 40 PM" src="https://github.com/user-attachments/assets/7238b749-4652-46a9-91a8-2e636f5aef73" />

Three situations in which YOLO struggled to detect a person accurately were:

1. **Photo of my dog:** When I showed a photo of my dog, it took some adjusting for the model to detect a "person." I believe this could have been because the photo was displayed on my phone, and factors such as lighting and image quality may have affected the model's detection.

2. **Standing farther away:** Another time YOLO struggled to detect me was when I stood farther back from the camera. I noticed that the detection box flickered. In this instance, I used the `--conf 0.2` setting, which requires a higher confidence score for detections to appear. Since I was farther away, the model may have been less confident in identifying me.

3. **Only part of my body visible:** Although YOLO was generally good at detecting me when my full body wasn't in the frame, I noticed that it stopped detecting me at a certain point. In this instance, only a small portion of my arm was visible, which may not have provided enough visual information for the model to recognize a person.


## Part C. 
### See more: hands and pose with MediaPipe

\*\*\***Include a screenshot or short video of the hand pose demo, and write how you might use face, hand or body pose tracking in your observant system.**\*\*\*

https://github.com/user-attachments/assets/8eca6862-aa09-4bcf-a5b3-d987f2e60d2a

For the observant system, one of the ideas we were considering was tracking movement during our sleep to help us understand our sleep patterns. We might use body pose tracking to capture the different poses we sleep in throughout the night, whether we sleep walked, or even which pose we slept the longest in.

<img width="2162" height="620" alt="Screenshot 2026-10-25 at 8 58 15 PM" src="https://github.com/user-attachments/assets/7be4768c-fa06-4302-b692-263ed78bb8e2" />

## Part D. 
### Reason: run Qwen on the Pi with Ollama

\*\*\***Ask Qwen three questions a bedside device might need to answer. Paste the questions, the answers and how long each took. Try one of them with `qwen3:0.6b` and compare.**\*\*\*

<img width="2162" height="620" alt="Screenshot 2026-10-25 at 8 58 15 PM" src="https://github.com/user-attachments/assets/7ba8aa6b-96b7-4851-ab79-f13b5475bc56" />

<img width="1284" height="416" alt="Screenshot 2026-10-25 at 9 12 37 PM" src="https://github.com/user-attachments/assets/74e72810-2276-41f1-904f-00be3d146403" />

I noticed when we didn't use `qwen3:0.6b` the model provided direct answers to our questions, however, when we did use `qwen3:0.6b` the model produced more human-like and engaging text. For instance, it starts with "Absolutely!" which is more conversational than just listing three proposed steps for our bedtime routine.  


## Part E. 
### Connect: from YOLO readings to Qwen reasoning

\*\*\***Document the pipeline: at least three runs with the log, the question, Qwen's answer, and whether it was right. Include one case where Qwen got it wrong, and say what you changed in the interpreter and why.**\*\*\*

We ran `yolo_to_qwen.py` three times with people walking in and out of the frame. Each run used the same default interpreter but a different question. Full logs and answers are in the screenshots.

**Run 1: "Did anyone leave?"** (33 log lines in 43 s, Qwen took 21.7 s)

<img width="1554" height="777" alt="pipeline_run1_did_anyone_leave" src="https://github.com/user-attachments/assets/3af7b6a3-3990-4edb-9a12-ac418e89325f" />

```
16:59:32 1 person(s) at center/close
16:59:36 nobody
16:59:37 1 person(s) at right/far
16:59:40 3 person(s) at center/far, right/far, center/far
...
17:00:12 2 person(s) at center/close, right/close
```

Qwen: "Yes, several people were seen leaving the room during the 43-second observation period. The log indicates that multiple individuals moved from their initial positions to new locations such as "right/far," "left/close," or "center/close" throughout the entire duration, with some instances showing a transition from one person count to another (e.g., dropping from 2 to 1)."

**Partly right.** People did move around, but "several people leaving" overstates it. Most of the count changes (2 → 1 → 2 within a second) come from YOLO losing someone for one frame, not from anyone walking out.

**Run 2: "Should I be worried?"** (16 log lines, Qwen took 22.9 s)

<img width="1555" height="821" alt="pipeline_run2_should_i_be_worried" src="https://github.com/user-attachments/assets/3c022ec6-5e46-4fd9-a5d5-68ade1b2f419" />

```
17:05:01 1 person(s) at center/close
17:05:13 nobody
17:05:14 1 person(s) at center/close
17:05:20 nobody
...
17:05:29 nobody
17:05:30 1 person(s) at left/close
```

Qwen: "Yes, you should be worried because there are two instances where no one was present (17:05:13 and 17:05:29), which indicates a potential safety or occupancy issue in the room. Additionally, the log shows multiple people moving around the space over time, suggesting activity that could indicate an emergency or disturbance."

**Wrong.** Nothing alarming happened. The `nobody` lines last one second each, and someone shows up again on the very next line. They are detection dropouts, but the model reads them as real events and turns them into a "safety issue". A small model also tends to say yes to a leading question.

**Run 3: "Write one sentence a sleepy person would want to hear."** (28 log lines in 56 s, Qwen took 15.4 s)

<img width="1555" height="821" alt="pipeline_run3_sleepy_sentence" src="https://github.com/user-attachments/assets/09fef069-78a0-43ce-acaf-f6b928bd0bb5" />

Qwen: "The log indicates that there are no people sleeping or resting in the room during this 56-second observation period; instead, it shows a mix of people moving around and being absent (nobody). Therefore, a sleepy person would likely want to hear about the activity taking place rather than sleep."

**Right about the facts, wrong about the job.** The room really was full of people moving around, but the model gave two sentences of analysis instead of one soothing sentence.

**What we changed and why.** All three runs went wrong in the same way: the interpreter writes a new line whenever the person count changes, so one-frame dropouts become "nobody" events, and Qwen treats each one as real. For our night-time version (sleep_watch.py) we rebuilt the interpreter around that problem:

- We lowered YOLO's confidence to 0.3, because a sleeper under a blanket is half hidden.
- We stopped logging counts and positions and logged **how much of the person's box changed** between looks. A look counts as a "toss" only when more than 4% of the pixels changed or the box jumped or changed shape.
- Tosses less than 30 s apart count once (`--cooldown`), so one turn over is not logged as five.
- We flag a look as `light` when almost the whole frame changes (a lamp switching on) instead of counting it as movement.
- The arithmetic is done in Python and Qwen only gets the totals, because the model is unreliable at counting over a long log.

---

# Lab 5 Part 2: Overnight Sensation

## Part F. 
### Read Part 2 and storyboard your night-time interaction

**Initial storyboard.** We picked sense all night. Before bed, the camera is placed near the bed. While asleep, it records tossing and turning. After bed, a web interface shows a graph of movement during sleep.

<img width="1536" height="2048" alt="storyboard_initial" src="https://github.com/user-attachments/assets/e81d67ba-5125-4fe2-8373-3b531f8dba9f" />

Our initial storyboards were not as creative as we could have made them. When coming up with our ideas we were thinking very small and one-dimensional: we were so focused on capturing the movement the user made during their sleep and reporting it back to them. We didn't recognize how we could make a story that is 1) worth capturing and processing and 2) worth buying. The important question we needed to ask was "Why us?" Why should a user go out of their way to buy our device?

## Prep for Part 2

1. Look at and give feedback on the Part F storyboards.
**Nishant Ray (nr487@cornell.edu):** "I like the idea of checking how someone is sleeping or if they move around during their sleep. It   seems useful and would be something that I would actually use. I think one requirement from the README instructions say to not just have a camera pointing at the bed. Maybe there could be another form of interaction to see if they wake up during their sleep. Perhaps with any of the other sensors we received?"
2. [Update your Lab Hub](prep.md#get-the-latest-content) to get the latest content for Part 2.
3. Decide where the device will spend the night and who else lives there. Get their OK before the first run.
4. Revise your storyboard with the feedback and with what you learned in Part E about where the pipeline breaks.

**Revised Storyboard**

<img width="1179" height="847" alt="storyboard_revised" src="https://github.com/user-attachments/assets/b7ad1d00-86cc-49e2-8200-7024805906a3" />

**Before bed:** The user places the device on a desk or nightstand with the camera facing the bed and makes sure the mic is on.
**While asleep:** The device takes in the video feed and records the user's movement (tossing and turning, changing sleeping positions). It also records audio from the room: cars and other vehicles, roommates, doors, and so on.
**When awake:** By the time the user wakes up, the data has been processed. A dashboard shows information about their sleep quality: how many times they moved, how many of those moves came after a noise, and a graph with movement and noise as two lines on the same plot, spiking at the times with the most of each.

Our revised storyboard combines several factors that each affect sleep quality. It also tells people about their surroundings so they can make meaningful decisions to improve them.

We already knew from our first storyboards that we wanted to capture live data on how often, and when, a person tosses and turns during the night. We wanted to take it further and work out what would make someone buy a separate device. On its own, the number of times a person tosses and turns doesn't tell them anything useful. It also doesn't point them toward anything they could change about their sleeping habits or personal life.

One of us mentioned that their room at the House faces the Queensboro Bridge, which can be distracting at night because of the lights on the bridge and the lights and sounds of the cars. We realized there could be a correlation between how much light a person is exposed to while trying to rest and how much they toss and turn. We decided the visualization would be a graph showing tossing and turning in one color and the device's light exposure in another.

**Revision from the feedback.** Nishant pointed out that Part 2 asks us not to just point a camera at the bed, and suggested using one of the other sensors to tell when the sleeper wakes or moves. In response, the revised design adds a **motion sensor under the bed** (from the Lab 4 sensor kit). It feels the mattress move when the person tosses and turns, so movement can be detected without relying only on the camera, and it keeps working in the dark, when the webcam struggles. The camera stays as a second signal, and it saves no images, only numbers. _Status: planned. The current `sleep_watch.py` still detects movement with the camera only; the sensor is the next step._

## Part G. 
### Design the interaction before bed

\*\*\***Describe the bedtime interaction and include a short video of someone handing the night over to the device.**\*\*\*

**Video:** [Bedtime hand-off (Google Drive)](https://drive.google.com/file/d/1y_KTMdEgEXjUukbvKvR_lEX8_eBrvzo9/view)

****My bedtime hand-off:** the sleep watcher [sleep_watch.py](http://github.com/9JAyemi/Interactive-Lab-Hub/blob/Fall2026/Lab%205/sleep_watch.py)**. Before bed the person asks the Pi to watch their sleep. The Pi asks out loud (espeak-ng), _"What would you like me to watch tonight?"_, and the person types or says their question, for example _"Do I toss and turn more when the room is noisier?"_ (pressing Enter uses that question as the default). The Pi answers, "_Okay. I will count your tossing and turning and listen to the room... Good night,"_ then waits a settling period so getting into bed is not counted.

```
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ tmux new -s night
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ python sleep_watch.py --until 07:00     # type the question
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ python sleep_watch.py --voice           # or say it (needs faster-whisper from Lab 3)
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ python sleep_watch.py --settle 300      # 5 minutes to fall asleep before counting (default 120 s)
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ python sleep_watch.py --quiet           # no spoken acknowledgement
```

The Pi waits **2 minutes** after the hand-off before it starts counting (a countdown prints every 30 s), so getting into bed is not counted as tossing.

Detach from tmux with `Ctrl-b` then `d`; the night keeps running after the ssh session closes. With `--voice` the Pi listens for up to 15 seconds and stops early once you have spoken and paused for 1.5 seconds (change the limit with `--listen 30`). Without `--voice` the script falls back to typing, so it still works if faster-whisper is not installed in the Lab 5 venv.



## Part H. 
### Incorporate the observant system during sleep

\*\*\***Run the system for at least one real night. Include the log (or an excerpt) and a few sentences on what broke or surprised you.**\*\*\*

**My night shift.** `sleep_watch.py` replaces `overnight.py` for my interaction. It uses the webcam and the microphone together and takes one look every 5 seconds (`--interval`):

- **Movement (tossing and turning):** YOLO (the `model` from `yolo_to_qwen.py`, people only, confidence 0.3 because a sleeper is half hidden) finds the person. The frame is compared with the previous look inside the person's box, padded by 15%, or the whole frame if YOLO cannot find them under the blanket. If more than `--motion` (default 0.04, i.e. 4%) of those pixels changed, or the box jumped sideways or changed shape (lying on the back vs. the side), that look counts as a toss. Tosses closer than `--cooldown` seconds (default 30) count once. If nearly the whole frame changes (a lamp switched on), the look is marked `light` and not counted.
- **Sound level:** the microphone is read continuously in 0.1 s blocks and converted to loudness in dBFS. Each look records the average (`db`) and the peak (`peak`) since the previous look. dBFS is relative to the mic, not a calibrated sound meter: about -60 is a silent room, about -30 is talking nearby, and 0 is the loudest the mic can record. If no mic is found the night still runs and sound is logged as `null.`
- **Privacy:** no photos are saved, only numbers.
  
Everything goes into `sleep_log.jsonl,` one JSON object per look (a new night overwrites the previous log):

```
{"t": "2026-10-27T23:00:00", "start": true, "request": "Do I toss and turn more when the room is noisier?", "interval": 5}
{"t": "2026-10-27T23:03:15", "person": true, "motion": 0.071, "toss": true, "db": -57.8, "peak": -38.2}
{"t": "2026-10-27T23:03:20", "person": true, "motion": 0.009, "toss": false, "db": -58.4, "peak": -55.1}
```

Fake a night first: run `python sleep_watch.py --settle 5 --verbose,` toss around in view of the camera, clap a few times, then press Ctrl-C and check the report. Tuning tips:

- If breathing or camera noise is counted as tossing, raise `--motion` (e.g. `--motion 0.08`); if real turns are missed, lower it.
- A completely dark room makes YOLO and the motion detection unreliable. A dim night light helps.
- Point the camera at the bed from the side or the foot, far enough away that the whole body is in the frame.
- Check that the webcam and the mic show up first: `ls /dev/video0` and `arecord -l.`

**The real nights.** We ran the system overnight on 30 October 2026, with the question _"Do I toss and turn more when the room is noisier?"_.

**Night 1, 01:13 to 07:00 ([sleep_log_night1.jsonl](https://github.com/9JAyemi/Interactive-Lab-Hub/blob/Fall2026/Lab%205/sleep_log_night1.jsonl)):** **a failure.** The room was completely dark. In 3,981 looks YOLO never found a person and the motion check counted **0 tosses,** so the morning report honestly said there was nothing to report. The microphone worked all night, with peaks between -39 and -16 dBFS.

```
{"t": "2026-10-30T01:13:15", "start": true, "request": "Do I toss and turn more when the room is noisier?", "interval": 5}
{"t": "2026-10-30T01:15:18", "person": false, "motion": 0.0, "toss": false, "db": -33.1, "peak": -29.6, "dark": true}
{"t": "2026-10-30T01:15:23", "person": false, "motion": 0.0, "toss": false, "db": -33.4, "peak": -29.9, "dark": true}
```

**The fix.** In a dark room the webcam image is almost black, so every frame looked the same. We added a low-light step (`--dark,` `--gamma`) that brightens frames whose average brightness is below 40/255 with a gamma curve. A gamma curve lifts the shadows without amplifying sensor noise as much as a plain gain would. Each brightened look is tagged `"dark": true.`

**Night 2, 07:19 to 09:38 ([sleep_log.jsonl](https://github.com/9JAyemi/Interactive-Lab-Hub/blob/Fall2026/Lab%205/sleep_log.jsonl)):** **it worked.** It counted 76 tosses in 1,584 looks, and the verdict was that the sleeper **tossed MORE when it was noisy.**

```
{"t": "2026-10-30T07:28:11", "person": false, "motion": 0.023, "toss": false, "db": -36.8, "peak": -32.7}
{"t": "2026-10-30T07:28:16", "person": true,  "motion": 0.082, "toss": true,  "db": -35.3, "peak": -31.8}
{"t": "2026-10-30T07:28:22", "person": false, "motion": 0.08,  "toss": false, "db": -33.6, "peak": -29.6}
{"t": "2026-10-30T07:28:53", "person": false, "motion": 0.104, "toss": true,  "db": -37.3, "peak": -34.3}
```

<img width="1139" height="568" alt="sleep_20261030-0721" src="https://github.com/user-attachments/assets/a2ebed7d-fd01-4fbc-8af2-a363f89e3eaa" />

**What surprised us:**

- The camera was the weak link, not the AI. A dark bedroom gave the camera nothing to see, and we only found out in the morning. Next time we will do a dark-room test before the first real night.
- YOLO rarely sees a sleeper under a blanket: person was true in only 80 of the 1,584 looks. Most tosses were caught by the whole-frame fallback, which is also why we plan to add a bed-mounted motion sensor (see the feedback above).
- The cooldown matters. At 07:28:22 the motion was still 8% one look after a toss, and without the cooldown it would have counted as a second toss.


## Part I. 
### Design the interaction when awake

**Video:** 
[Morning Video Reveal](https://drive.google.com/file/d/1Ky8sTSRQfp5FFDRM9t4lTQcOSCZAVzpp/view?usp=sharing) 

**My morning reveal.** When the night ends (Ctrl-C in the tmux window, or automatically at the --until time), sleep_watch.py gives the report straight away. To see it again, or to report on another log:

```
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ tmux attach -t night                     # get back to the night window, then Ctrl-C
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ python sleep_watch.py --morning          # report on the last sleep_log.jsonl
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ python sleep_watch.py --morning --say    # and read it aloud
(.venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 5 $ python sleep_watch.py --morning --log fake.jsonl
```

The arithmetic is done in Python, not by Qwen, because a 0.8B model is bad at maths. The script prints all the facts first, then asks Qwen (qwen3.5:0.8b, change with --model) to turn them into a report of at most four sentences:

- **Movement:** total tosses, tosses per hour, tosses in each hour of the night, and how much of the night the person was seen in bed.
Sound: when the room was noisiest and the quietest 10 minutes of the night. The report gives times, not decibel numbers; the dB values are only in the printout and the graph.
- **Noise vs. movement:** a look counts as noisy when its peak is more than --noisy-margin dB (default 15) above the quiet baseline. The script compares how often the person tossed in noisy vs. quiet looks, counts the tosses that came within one minute after a noise, and computes the correlation between loudness and movement over 10-minute bins. From that it states a verdict: tossed MORE / LESS / about the SAME when it was noisy, or "not enough data to compare" (fewer than 3 tosses or no noisy moments).

**The graph.** Every morning report also saves a picture of the night next to the log, sleep_YYYYMMDD-HHMM.png (the date and time the night started). Movement and noise are drawn as two overlapping lines on one chart, so you can see whether they spike together:

- **Movement (blue):** how much of the picture changed (the biggest change per minute; per look for short test nights), with a dot for each counted toss.
- **Noise (orange):** the loudest sound each minute, with a dashed line for the noisy threshold.
- The two lines have different units (% of the picture vs. dB), so each one is scaled to its own range for the night: the bottom of the chart is that line's lowest point and the top its highest. The real ranges are in the legend.
- The **three moments with the most movement** are shaded and labelled with their time and how loud the room was then.

Open it over VNC, or copy it to your laptop with scp pi@raspberrypi:"~/Interactive-Lab-Hub/Lab\ 5/sleep_*.png" .

It is honest about empty nights: if nothing was logged, or the camera never saw anyone in bed, it says so and does not ask Qwen. Qwen can still add small invented details (e.g. a time of day), so the printed numbers are the ground truth and the spoken report is the friendly version.

## Final documentation

- **Bedtime hand-off:** [Video](https://drive.google.com/file/d/1y_KTMdEgEXjUukbvKvR_lEX8_eBrvzo9/view?usp=sharing)
- **The night:** See the log excerpts in Part H, plus [sleep_log.jsonl](https://github.com/9JAyemi/Interactive-Lab-Hub/blob/Fall2026/Lab%205/sleep_log.jsonl) and [sleep_log_night1.jsonl](https://github.com/9JAyemi/Interactive-Lab-Hub/blob/Fall2026/Lab%205/sleep_log_night1.jsonl)
- **Morning reveal:**  [Morning Video Reveal](https://drive.google.com/file/d/1Ky8sTSRQfp5FFDRM9t4lTQcOSCZAVzpp/view?usp=sharing). Report from `sleep_watch.py --morning --say` and graph [sleep_20261030-0721.png](https://github.com/9JAyemi/Interactive-Lab-Hub/blob/Fall2026/Lab%205/sleep_20261030-0721.png), both from Run 2 (a daytime run)

**What we learned.** The full pipeline runs from hand-off to spoken report, and it is honest when it sees nothing. We do not yet have a trustworthy answer to our question: the one overnight run missed the bed, and the noise link in the daytime run is weak. Light exposure, the idea behind our Queensboro Bridge story, is still a hypothesis because the system does not log it. If a properly aimed overnight run shows a real pattern, users could act on it with curtains, earplugs, or by moving the bed.

[Full System Video](https://drive.google.com/file/d/1pfw7xsKaY9CakAqYPnWPGsEjjmr7br9D/view?usp=sharing)
