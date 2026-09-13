# FocusForge: Recommended Next Features

## Recommendation

FocusForge now has its core timer rhythm, subject-aware history, precision charts, Android focus guidance, custom rhythms, and local persistence. The most valuable next step is **not more timer controls**. It is a lightweight workflow that helps the user decide *what to study*, carry out the session, and capture a useful follow-up action.

> Self-regulated learning is commonly described as a cycle of forethought, performance, and reflection. In practice, the app should make that cycle quick rather than add a heavy study-management system. [1]

| Priority | Feature | What the user would do | Why it is worth adding | Estimated scope |
|---:|---|---|---|---|
| 1 | **Session intention + closeout** | Before starting, enter a one-line target such as “Solve 15 calculus problems.” After ending, answer “Finished?” and “Difficulty?” | Creates a plan → focus → reflect loop around the existing timer and subject data. It would also make History advice more useful. [1] | Small |
| 2 | **Review queue** | At session closeout, add a topic to review tomorrow, in 3 days, or next week. A compact “Due today” card appears on Focus. | Adds active recall and spacing without turning FocusForge into a full flashcard app. Retrieval and repeated review are established study strategies. [2] | Medium |
| 3 | **Weekly study plan / time blocks** | Choose subjects, target minutes, and preferred time blocks for the week; tap a block to start that subject’s session. | Turns the existing weekly goal and subject analytics into an actionable plan. It is the natural bridge between goal-setting and actual study sessions. [1] | Medium |
| 4 | **Explainable study insights** | After several sessions, see statements such as “Physics sessions average 28 focused minutes” or “Pauses rise after 45 minutes.” | Uses existing local data to suggest an appropriate rhythm or break—not to judge the user. Each insight should show the underlying sessions/events. | Medium |
| 5 | **Android Focus setup assistant** | Follow a device-specific checklist for Digital Wellbeing, app limits, app-limit PIN, Focus Mode, and Do Not Disturb. | Android provides these system controls but device support varies. A guided setup is more honest and useful than claiming universal in-app blocking. [3] | Small |
| 6 | **Local backup, restore, and CSV export** | Export history/settings to a file; restore after phone migration; export CSV for personal analysis. | Protects user-owned study data and makes the app safe to use long term without requiring an account or server. | Medium |
| 7 | **Reliability & accessibility panel** | Run a cue test, notification-permission check, large-text mode, reduced-motion mode, and haptic-only cue option. | Directly improves daily trust—especially because locked-screen cues and notifications depend on the installed Android build and device settings. | Medium |
| 8 | **Private accountability sharing** | Generate a share card with weekly focused time, completed sessions, and goals—without exposing event details or needing an account. | Gives optional motivation while keeping the product local-first and focused. | Small |

## Best First Release: “Study Loop”

I recommend implementing **Priority 1 and Priority 2 together** as one focused release:

1. The user selects a subject and enters a short session intention.
2. FocusForge runs its existing rhythm and collects its existing event data.
3. At the end, the user marks the intention as completed, partial, or deferred and rates difficulty.
4. The user may schedule one small review reminder for a future date.
5. History shows outcomes by subject and offers clear, evidence-based patterns rather than vague scores.

This is compact, offline-friendly, and directly builds on the app that already exists. It is also lower risk than adding cloud accounts, social feeds, or overly broad “blocking” features.

## What I Would Avoid for Now

Do not add a full notes editor, a competing flashcard system, or a social feed. These would make the app heavier while duplicating mature tools. I also would not promise that FocusForge can block all calls, messages, Home/Recents navigation, or third-party apps: Android’s system settings, permissions, and device manufacturers ultimately control those behaviors. [3]

## References

[1]: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.793042/full "Baars et al., Ace Your Self-Study: A Mobile Application to Support Self-Regulated Learning"
[2]: https://www.retrievalpractice.org/strategies/2019/6/19/tech "Agarwal, Recommended Tech Tools to Make Retrieval Practice Quick and Easy"
[3]: https://support.google.com/android/answer/9346420?hl=en "Google Android Help, Manage How You Spend Time on Your Android Phone with Digital Wellbeing"
