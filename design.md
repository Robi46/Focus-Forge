# FocusForge Mobile Design Plan

## Product Intent

FocusForge is a portrait-first study companion for a self-directed focus ritual: a single chime every five minutes, a three-chime checkpoint every twenty minutes, and a visible 120-second reset before the next focus block begins. The interface should feel calm, deliberate, and touchable with one hand, rather than resemble a dense productivity dashboard.

## Platform Boundary

Android does not permit a normal third-party application to universally block the Home or Recents controls, silence every other app while selectively allowing WhatsApp or Messenger calls, or bypass the device owner’s notification policy. FocusForge therefore provides a **Focus Shield** that keeps an active session recoverable, offers a full-screen study view, guides the user to Android’s Screen Pinning and Do Not Disturb controls, and keeps locally scheduled study cues working when the display is off. Phone and messaging emergency exceptions remain under the user’s Android-level Focus/Do Not Disturb configuration.

## Screen List

| Screen | Primary content and functionality | One-handed layout |
| --- | --- | --- |
| Focus | A large circular countdown, current phase, next cue, session progress dots, a primary Start/Pause/Resume control, and a stop affordance protected by confirmation. | Primary control rests in the lower thumb zone; session status is readable at a glance. |
| Session setup sheet | Adjustable focus block, micro-cue interval, reset duration, single/triple chime selection, and a start-session summary. | Bottom sheet with steppers and an anchored Start Session button. |
| Focus Shield | Status of cue permissions, background behavior, display behavior, notification guidance, Do Not Disturb guidance, and Screen Pinning guidance. | Compact status rows with clear user-initiated actions and explanations. |
| History | Current-day focus total, completed block count, recent session records, and a minimal weekly study rhythm. | Scannable list with summary cards and no deep nesting. |
| Settings | Sound/haptic choices, cue volume, screen-awake preference, theme preference, default timer values, and reset-session behavior. | Grouped iOS-style setting cards with toggles, selectors, and concise helper text. |

## Key User Flows

| Flow | Steps |
| --- | --- |
| Start a session | Focus screen → open session setup → set defaults or adjust duration → grant notification permission if requested → Start Session → timer enters Focus phase. |
| Receive study cues | At 5, 10, and 15 minutes, a single local cue occurs → at 20 minutes, three cues occur → timer enters a 120-second Reset phase → on reset completion, the following focus block begins automatically. |
| Continue with screen off | User starts session → locks display → system-scheduled local cue fires → user returns later → timer derives the correct phase from the saved session timeline. |
| Strengthen distraction resistance | Focus Shield → review guide → enable Android Do Not Disturb and Screen Pinning in system settings → return to FocusForge → begin or resume session. |
| End a session | Tap End → confirmation sheet → save completed time and blocks locally → return to ready state with a session summary. |

## Color and Surface System

FocusForge uses an ink-like navy base, a luminous blue focus accent, and a warm reset accent. The visual language is intentionally dark-first for long study sessions and easy night viewing.

| Token | Hex value | Intended use |
| --- | --- | --- |
| Midnight | `#081120` | Root canvas and timer surround. |
| Deep Slate | `#111E31` | Raised cards, controls, and sheets. |
| Focus Blue | `#4DA3FF` | Start action, progress ring, selection states. |
| Electric Mint | `#5FE0B6` | Completed blocks and positive status. |
| Reset Amber | `#FFB55F` | 120-second reset phase and attention cues. |
| Mist | `#EAF2FF` | Primary typography. |
| Steel | `#9BAEC9` | Secondary labels and helper text. |

## Interaction and Motion

The countdown ring uses subtle, continuous progress rather than conspicuous animation. Buttons acknowledge a press with a 0.97 scale and light haptic response. Screen changes use short fades or sheets of 180–260 ms. Motion is never required to understand the timer state; phase color, labels, and explicit time values always carry the same information.

## Local Data Model

```ts
type StudySettings = {
  focusMinutes: number;
  cueMinutes: number;
  resetSeconds: number;
  soundEnabled: boolean;
  hapticsEnabled: boolean;
  keepScreenAwake: boolean;
  darkTheme: boolean;
};

type ActiveSession = {
  id: string;
  startedAtMs: number;
  phase: "focus" | "reset" | "paused";
  phaseStartedAtMs: number;
  pausedAtMs?: number;
  accumulatedPausedMs: number;
  blocksCompleted: number;
};

type SessionRecord = {
  id: string;
  startedAtMs: number;
  endedAtMs: number;
  focusedSeconds: number;
  completedBlocks: number;
};
```
