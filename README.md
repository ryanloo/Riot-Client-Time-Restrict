# 🎮 Riot Client Time Restrict

## 🔥 What’s This?

Hey, gamer! This script is your **game-time bouncer**—it only lets you launch Riot Client (for Valorant & LoL) during the hours you allow. Trying to grind outside your set time? Nah, this script says, "Go touch some grass." 🌱

## 🎯 How It Works

1. You set your game time window in the **config.ini** file.
2. Try launching Riot Client outside of that time? Boom. **Blocked.** 🚫
3. If there’s an issue with your config the program will let you know.

## 🛠 Setup & Usage

1. Extract the file to any location on your computer.
2. Open **config.ini** (create it if it doesn’t exist) and add this:
   ```ini
   [Settings]
   exe_path = C:\Riot Games\Riot Client\RiotClientServices.exe
   start_time = 18:00  # 6:00 PM
   end_time = 23:00  # 11:00 PM
   ```
2. Create a shortcut of main.exe (You can rename it to Riot Client).
3. Update the shortcut icon to the one in the Icons folder.
4. Move the shortcut to your desktop.
4. Run Riot Client through the shortcut.
5. If it’s **game time**, Riot Client launches. If not then its time to **lock in**. 💀

## 📥 Download

Get all the files you need here: [Download Now](https://drive.google.com/file/d/1QBxmc9qXljZZ-_CFJF-NB5iihuglaoMK/view?usp=drive_link)

## 📝 Notes

- Time is in **24-hour format** .
- If your config is messed up, the program will call you out.
- Works best if you set up a **scheduled task** to enforce the script.
- No more "one last game" at 3 AM—stick to your schedule and rank up smart! 📈

GLHF, but at the **right time.** 🏆

