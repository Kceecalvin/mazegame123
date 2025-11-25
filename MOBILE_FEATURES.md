# 📱 Maze Escape - Mobile Features

Your Maze Escape game is now fully optimized for mobile devices!

## 🎮 Mobile Controls

### Touch Controls (3 Ways to Play!)

1. **Swipe Gestures** (Most Natural)
   - Swipe UP on the maze area to move up
   - Swipe DOWN to move down
   - Swipe LEFT to move left
   - Swipe RIGHT to move right
   - Minimum swipe distance: 30dp (feels natural)

2. **Touch Buttons** (Large & Easy to Tap)
   - ↑ UP button (top center)
   - ↓ DOWN button (bottom center)
   - ← LEFT button (middle left)
   - → RIGHT button (middle right)
   - Button size: 60dp minimum (easy to tap)
   - Font size: 32sp (large arrows)

3. **Keyboard Controls** (For PC Testing)
   - Arrow keys: ↑, ↓, ←, →
   - WASD keys: W, A, S, D
   - H key: Toggle hint
   - R key: Restart level

## 🎯 Game Features

### Levels
- **10 Progressive Levels** with increasing difficulty
- Levels 1-3: Small mazes (11-15 cells)
- Levels 4-6: Medium mazes (15-19 cells)
- Levels 7-10: Large mazes (21-27 cells)

### Gameplay Elements
- **Maze Generation**: Multiple algorithms (DFS, Prim's, Division)
- **Enemy Snake**: Chases you using pathfinding
- **Snake Activation Delay**: 10 seconds (Level 1) to 1 second (Level 10)
- **Hint System**: Shows optimal path to exit
- **Move Counter**: Tracks your efficiency
- **Timer**: Measures completion time

### UI Elements
- **Level Selection Screen**: Grid of 10 level buttons
- **Hint Button**: Toggle solution path visibility
- **Restart Button**: Restart current level
- **Menu Button**: Return to level selection
- **Win Screen**: Shows moves and time
- **Game Over Screen**: When caught by snake

## 🔋 Mobile Optimizations

### Performance
- **Smooth Animations**: 60 FPS update loop
- **Responsive Touch**: Immediate feedback
- **Optimized Rendering**: Canvas-based drawing
- **Memory Efficient**: Lightweight game logic

### Power Management
- **Wake Lock**: Screen stays on during gameplay
- **Multitouch Support**: Better touch handling
- **Portrait Orientation**: Optimized for one-hand play

### Screen Adaptation
- **Dynamic Sizing**: Uses `dp()` for density-independent pixels
- **Scalable Fonts**: Uses `sp()` for text
- **Responsive Layout**: Adapts to different screen sizes
- **Centered Maze**: Always fits on screen

## 📐 Layout Structure

```
┌─────────────────────────┐
│     Maze Escape         │ ← Title (10% height)
├─────────────────────────┤
│                         │
│      Maze Display       │ ← Game area (70% height)
│      (Swipeable)        │
│                         │
├─────────────────────────┤
│      [  ↑  ]           │
│   [←] info [→]         │ ← Arrow buttons
│      [  ↓  ]           │
├─────────────────────────┤
│ [Hint][Restart][Menu]  │ ← Action buttons
└─────────────────────────┘
```

## 🎨 Visual Design

### Colors
- **Player**: Blue (#4169E1 - Royal Blue)
- **Snake**: Green (#32CD32 - Lime Green when active)
- **Walls**: Dark Gray (#333333)
- **Paths**: Light Gray (#F5F5FF)
- **Start**: Green (#228B22 - Forest Green)
- **Exit**: Red (#DC143C - Crimson)
- **Hint Path**: Gold (#FFD700 with transparency)
- **Buttons**: Blue (#4169E1)

### Sizes
- **Minimum Button Size**: 60dp (easy to tap)
- **Arrow Font Size**: 32sp (large and visible)
- **Title Font Size**: 24sp
- **Button Font Size**: 16sp
- **Cell Size**: Dynamic (fits screen)

## 🚀 Performance Specs

- **Target API**: Android 13 (API 33)
- **Minimum API**: Android 5.0 (API 21)
- **Architecture**: ARM64-v8a, ARMv7a
- **Frame Rate**: 60 FPS
- **Update Interval**: ~16.67ms per frame

## 🎯 Gameplay Tips

1. **Use Swipes**: Faster than tapping buttons
2. **Watch the Snake**: It activates after a delay
3. **Plan Ahead**: Use the hint to learn the path
4. **Move Quickly**: Snake gets faster in higher levels
5. **Corner Strategy**: Snakes can get stuck in corners

## 📊 Difficulty Progression

| Level | Maze Size | Algorithm | Snake Speed | Delay (sec) |
|-------|-----------|-----------|-------------|-------------|
| 1     | 11x11     | DFS       | Slow        | 10          |
| 2     | 11x11     | DFS       | Slow        | 9           |
| 3     | 15x15     | DFS       | Medium      | 8           |
| 4     | 15x15     | Prim's    | Medium      | 7           |
| 5     | 19x19     | Prim's    | Medium      | 6           |
| 6     | 19x19     | Prim's    | Fast        | 5           |
| 7     | 21x21     | Division  | Fast        | 4           |
| 8     | 23x23     | Division  | Faster      | 3           |
| 9     | 25x25     | Division  | Very Fast   | 2           |
| 10    | 27x27     | Division  | Extreme     | 1           |

## 🔧 Technical Details

### Input Handling
- **Touch Events**: `on_touch_down`, `on_touch_up`
- **Swipe Detection**: Distance-based (30dp minimum)
- **Direction Calculation**: Compares horizontal vs vertical delta
- **Collision Detection**: Point-in-widget testing

### Game Loop
- **Clock Scheduler**: Kivy's Clock.schedule_interval
- **Fixed Timestep**: 1/60 seconds (60 FPS)
- **State Management**: "menu", "playing", "level_complete", "game_over"

### Platform Support
- **Android**: Primary target (touch optimized)
- **Desktop**: Full keyboard support for testing
- **Tablet**: Works great with larger screens

## 📱 Testing on Device

### Installation
1. Download APK from GitHub Actions
2. Enable "Install Unknown Apps" in Android settings
3. Open APK file to install
4. Launch "Maze Escape" from app drawer

### Permissions Required
- **INTERNET**: For future online features (not used yet)
- **VIBRATE**: For haptic feedback (can be added)
- **WAKE_LOCK**: Keeps screen on during gameplay

## 🎮 How to Play

1. **Start**: Select a level from the menu
2. **Objective**: Reach the red exit square
3. **Avoid**: Don't let the green snake catch you
4. **Controls**: Swipe or tap arrow buttons
5. **Hint**: Tap "Hint" to see the optimal path
6. **Win**: Reach the exit before the snake catches you!

---

**Enjoy your mobile maze adventure! 🎉**
