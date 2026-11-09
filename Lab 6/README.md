# Distributed Interaction

Abiola Bolaji (ab3394), Pallavi Srinivas (ps2269), Pallavi Khanna (pk633)

---

## Part A: MQTT Messaging

**5 ideas for messaging between devices**

- **Uno**: Users can play Uno through their Pi's.
- **Collaborative Mood Ring**: Users choose a color that represents their mood, shows it to a sensor, and then an interface demonstrates a combined color of their moods.
- **Virtual Pet:** Each device sends an interaction or command to a model or screen that shows a pet and the pet reacts. This is shown to the other user and they have a chance to respond.
- **Interactive Light Show:** Each device controls a different part of the light or color and communicates with others to create a light display.
- **Digital Aurora:** Raspberry Pis exchange color and movement information to create a synchronized aurora animation across their displays.

MQTT agrees on almost nothing in advance: you invent the topics and what the messages mean. Smart-home standards like Matter fix the vocabulary instead (every "light" behaves the same). Keep this trade-off in mind when you design your topics in Part C.

---

## Part B: Collaborative Pixel Grid

Each Pi = one pixel, controlled by RGB sensor, displayed in real-time grid.

**Architecture:** `Pi (sensor) → MQTT → Server → Web Browser`

**Setup:**

1. **Sensor**

#### Light/Proximity/Gesture sensor (APDS-9960)
We use this sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595) for this exmaple to detect light (also RGB)
 
<img src="https://cdn-shop.adafruit.com/970x728/3595-06.jpg" width=200>

Connect it to your pi with Qwiic connector


<img src="imgs/IMG_0270.jpg" height="200" />
We need to use the screen to display the color detection, so we need to stop the running piscreen.service to make your screen available again

```bash
# stop the screen service
sudo systemctl stop piscreen.service
```

if you want to restart the screen service
```bash
# start the screen service
sudo systemctl start piscreen.service
```
 
2. **Server** (one person on laptop):
```bash
cd "Lab 6"
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-server.txt
python app.py
```

2. **View in browser:**
   - Grid: `http://farlab.infosci.cornell.edu:5000`
   - Controller: `http://farlab.infosci.cornell.edu:5000/controller`

3. **Pi publisher** (everyone on their Pi):
```bash
# First time setup - create virtual environment
cd "Lab 6"
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-pi.txt

# Run the publisher
python pixel_grid_publisher.py
```

Hold colored objects near sensor to change your pixel!

![Pixel grid with two devices](imgs/two-devices-grid.png)

**📸 Include: Screenshot of grid + photo of your Pi setup**

<img width="1511" height="939" alt="699136847-9c0b3e8f-570a-4ec0-8b09-58ee901598c5" src="https://github.com/user-attachments/assets/3a77fdb1-df11-40bc-b13f-76745fd7ea2d" />

<img width="5712" height="4284" alt="699138073-0f58c72e-ea3b-4b6f-8aa8-e6f1097c5f92" src="https://github.com/user-attachments/assets/27ea73af-36f9-4557-a9d6-9f942517674e" />

<img width="5712" height="4284" alt="699138506-84fd8fe5-13b7-4afc-a1c7-9a2c7a5351df" src="https://github.com/user-attachments/assets/085d9619-d8f7-43aa-841d-11a72ad3b7db" />

---

## Part C: Make Your Own

### Deliverables

**1. Project Description**

Our project that we chose to make is a Mood Ring simulation that essentially aims to gauge the collective “mood” of a group of people; by averaging the RGB values of all of the Raspberry Pi’s together, we get a brand new color that we deem to be the overall mood. It is interesting because it is interesting to see how colors provide meaningful data regarding human emotion. The user experience depicts a mystical ring that updates smoothly, adding to the seamless experience.

It also encourages users to communicate with their friends about how they are feeling. With the advancement of social media and tech, social isolation has significantly increased. Implementing this can encourage users to maintain healthy relationships with their friends and maintain long distance friendships or relationships through communicating and expressing their feelings.


**2. Architecture Diagram**
- Hardware, connections, data flow
- Label input/computation/output

**3. Build Documentation**
- Photos of each Pi + sensors

Each Pi was setup with a proximity/gesture sensor:

<img width="3024" height="4032" alt="IMG_3933" src="https://github.com/user-attachments/assets/ec8a09bb-3233-4128-a99a-71cf6981fd50" />

The webpage showed the colors of the two users (the left circle demonstrated the left user’s mood and the right circle demonstrated the right user’s mood)

<img width="5712" height="4284" alt="699138073-0f58c72e-ea3b-4b6f-8aa8-e6f1097c5f92" src="https://github.com/user-attachments/assets/c5fd1176-9d83-4640-8c86-973a815a9775" />

- MQTT topics used

```
TEAM = os.environ.get('MOODRING_TEAM', 'moodring')
COLOR_TOPIC = f'IDD/{TEAM}/colors'
IDD/moodring/colors
```

- Code snippets with explanations

```
def snapshot():
    """Average the Pis that published within STALE_SECONDS."""
    now = time.time()
    with lock:
        stale = [key for key, value in devices.items() if now - value['seen'] > STALE_SECONDS]
        for key in stale:
            del devices[key]
        live = [
            {'id': key, 'r': value['r'], 'g': value['g'], 'b': value['b']}
            for key, value in sorted(devices.items())
        ]

    if not live:
        return {'count': 0, 'average': None, 'devices': []}

    count = len(live)
    average = [
        sum(item['r'] for item in live) // count,
        sum(item['g'] for item in live) // count,
        sum(item['b'] for item in live) // count,
    ]
    return {'count': count, 'average': average, 'devices': live}
```

This code snippet contains the function snapshot which implements main mechanism that is averaging the RGB values across all of the Pi’s that are connected to the Mood Ring server. By deriving the live RGB values of all of the devices that are providing input, the live [averaged] RGB values of the singular color of the Mood Ring change in response to its environment.

```
while True:
        if sensor is None:
            red, green, blue = fake_color
        else:
            raw_red, raw_green, raw_blue, _clear = sensor.color_data
            red, green, blue = scale_sensor_color(raw_red, raw_green, raw_blue)

        payload = json.dumps({
            'id': device_id,
            'r': red,
            'g': green,
            'b': blue,
            'timestamp': int(time.time()),
        })
```

The while True loop in mood_ring_publisher.py receives the live color data the user provides the sensor. The loop then converts these values into usable RGB values so that they can be provided to the server script. As stated previously, these RGB values are averaged across all connected Pi’s to provide the color of the Mood Ring.

The final code scripts: https://github.com/pk633-cu/Interactive-Lab-Hub/tree/Fall2026/Lab%206/Mood%20Ring%20Scripts


**4. User Testing**

https://github.com/user-attachments/assets/b79e0ba7-6ea9-49d7-8dc6-30d1e2a98334

Initially, when we asked the users to try, they were not sure what to do and asked for clarification as the interface only demonstrated the users’ moods and a large circle demonstrating the combined colors. At the same time, they were intrigued by the combined color of all the users and how certain colors overpowered others. This could help start conversations and encourage individuals to communicate their feelings with long-distance partners or friends, strengthening relationships. One thing they recommended to change was adding more instructions on the interface to indicate how to operate the interaction.

**5. Reflection**

The overall user experience is very smooth and aesthetically pleasing, which makes the device much more fun to use. The main focus of our device was the UX as the input of data across all of the Pi’s was pretty much the exact same mechanism we employed as we were prepping/setting up our hardware.

The sensor event worked by each user showing a color that represented their mood to the sensor. Then the webpage we developed receives the colors and demonstrates each color on the screen. Since we used Cursor to create the webpage, Cursor computes the combination of both the colors and then demonstrates the resulting color on the webpage. The model that computed the resulting color had to re-run on every event, because every event had to be treated independently as users may choose a different color to express their feelings. This would mean that the model would have to recalculate the color every time a different color is presented.

Even though we got positive feedback regarding the overall experience, there are still some areas of improvement. For instance, we can improve the user interface by adding more instructions and also make the UI more engaging. One thing I noticed when testing the interaction is that it took a while for the model to sense the right shade of the color. So another thing we could improve is finding a way to make the sensor identify and demonstrate the color faster.
