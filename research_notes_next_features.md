# Research Notes: Next FocusForge Features

## Sources reviewed

- Google Android Help, *Manage how you spend time on your Android phone with Digital Wellbeing*: Android can expose app-use information, app limits, app-limit PINs, temporary distracting-app pauses, and interruption controls. Device support varies. https://support.google.com/android/answer/9346420?hl=en
- Frontiers in Psychology, *Ace your self-study: A mobile application to support self-regulated learning*: the cited mobile-learning work frames planning, monitoring, and reflection as central self-regulated-learning processes. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.793042/full
- Search results also identified research on retrieval practice and self-regulated planning as complementary study strategies. These should be presented as optional learning workflow features rather than medical or academic guarantees.

## Implications for FocusForge

1. A low-friction session intention and short reflection would complete the existing subject, timer, goal, and analytics loop.
2. A separate Android Digital Wellbeing setup/checklist could guide user-controlled app timers and Focus mode rather than falsely claiming the app can universally block apps.
3. Retrieval-practice prompts, a review queue, and structured study planning are complementary to a focus timer and do not duplicate its current functionality.

## Prioritized opportunities

| Priority | Opportunity | Why it complements the existing app | Scope |
|---|---|---|---|
| 1 | Session intention and two-question closeout | Completes the plan → focus → reflect loop around the existing rhythm, subject selector, and history. | Small, local-only |
| 2 | Upcoming review queue | Lets users turn a completed topic into a scheduled active-recall review without making FocusForge a full flashcard platform. | Medium, local-only |
| 3 | Study plan and time-block view | Converts weekly goals and subject history into an actionable week plan and places a session on the calendar. | Medium, local-only |
| 4 | Smart, evidence-aware insights | Uses existing event and subject data to suggest a rhythm, session length, or break timing with clear explanations and no unsupported claim of certainty. | Medium |
| 5 | Android Digital Wellbeing companion checklist | Helps users configure system app limits, Focus Mode, and PINs, respecting Android boundaries rather than overstating app-blocking capabilities. | Small |
| 6 | Backup and export | Enables JSON or CSV export and local restore for user ownership and safe device migration. | Medium |
| 7 | Accessibility and reliability suite | Adds large-text layout checks, reduced-motion mode, haptic-only cue options, and a notification/audio diagnostic page for dependable daily use. | Medium |
| 8 | Optional accountability sharing | Share a privacy-preserving daily or weekly study summary as an image or text, without needing an account system. | Small to medium |

## Features intentionally not prioritized

- Third-party app or call-blocking promises: Android permissions and device differences make this unreliable and potentially misleading.
- A full notes editor, flashcard platform, or social feed: each would compete with dedicated tools and make the focused timer heavier.
- Cloud accounts by default: local data and offline operation suit the current app; backup and export should come first.
