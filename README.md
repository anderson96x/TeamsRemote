# TeamsRemote

Problem: Where I work, my Director usually has Teams meetings with other people at the meeting table. The thing is, his computer is a bit far from the table, and during the meeting, he should be able to control the 'mute' and 'camera' buttons on Teams.
<br>
<br>
<img src="https://github.com/anderson96x/TeamsRemote/assets/50344854/d9445726-1122-4a4d-ae4b-f3eb84ca9b65" alt="Directors room overview" width="500px">
- No, we do not have a laptop
<br>
<br>
Solution: So, we have a bunch of those presentation clickers around here. One day, I grabbed one of them and was like:
<br>
<br>

<img src="https://media.tenor.com/mm_2ABQapXkAAAAC/thinking-emoji.gif" alt="Thinking emoji" width="150px">



I ran a keyboard test to see which keys were associated with the physical buttons on the presentation clicker and found 'PageUp' and 'PageDown'. Then, I just needed to figure out how to remap them. Initially, I planned to code it using batch script or AutoHotKey, but since I'm learning Python, I decided to implement it in Python.

## What it does
- Remaps PageUp to 'CTRL + Shift + O' -> Camera control on Teams.
- Remaps PageDown to 'CTRL + Shift + M' -> Mic control on Teams.
- Remaps 'B' to 'CTRL + Shift + K' -> Raise / Lower hand (v1.2.0)
- Checks every 5 seconds to ensure the focus is on the Teams window (to avoid sending the hotkey to another application).

<img src="https://github.com/anderson96x/TeamsRemote/assets/50344854/5eb4ff64-c9d2-43da-b292-d7f574939630" alt="Presentation clicker showing that right button is mic control and left button is camera control" width="250px">
<br>
<img src="https://github.com/anderson96x/TeamsRemote/assets/50344854/7e81ac31-37b3-43e1-acba-a97c829a5478" alt="Teams Control" width="250px">

## Compatibility
Im using this model:
<br>
<img src="https://github.com/anderson96x/TeamsRemote/assets/50344854/69371884-080e-422e-9012-bccfdaf99fb2" alt="Presentation clicker" width="200px">
- It has no brand; it's just a generic presentation clicker.
- Since it's just a remap, I believe it might work with any presentation clicker that has 'PageUp' and 'PageDown' buttons. If you want to test, check it on https://keyboardchecker.com/
- It was designed to work with Teams Desktop
