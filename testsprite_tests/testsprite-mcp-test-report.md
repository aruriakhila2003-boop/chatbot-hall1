# TestSprite AI Testing Report(MCP)

---

## 1️⃣ Document Metadata
- **Project Name:** edureach-agentic-colleage-chatbot
- **Date:** 2026-10-06
- **Prepared by:** TestSprite AI Team
- **Scope:** Frontend, full codebase (production preview on port 4173)
- **Executed:** 30 of 32 planned tests (TC031 and TC032 skipped as Low priority under the production cap)
- **Account:** Akhila Aruri's workspace (Free plan)

---

## 2️⃣ Requirement Validation Summary

### Requirement: College Home Page
- **Description:** Public landing page shows EduReach branding, hero content, and a CTA to explore programs.

#### Test TC001 Homepage renders hero and key branding
- **Test Code:** [TC001_Homepage_renders_hero_and_key_branding.py](./TC001_Homepage_renders_hero_and_key_branding.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/73ed490f-b31a-4fd7-b14c-b220017fc97f
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Homepage loads with navbar brand `EduReach` and the hero CTA `Explore Programs of the college`.
---

#### Test TC002 Open the homepage and reach the courses section
- **Test Code:** [TC002_Open_the_homepage_and_reach_the_courses_section.py](./TC002_Open_the_homepage_and_reach_the_courses_section.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/7bf5e66b-9217-42f9-96d1-d2137828921e
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Hero CTA updates the URL to `#courses` as expected.
---

#### Test TC005 Explore Programs CTA opens the courses area
- **Test Code:** [TC005_Explore_Programs_CTA_opens_the_courses_area.py](./TC005_Explore_Programs_CTA_opens_the_courses_area.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/f763ab70-56f5-40b9-bfe2-04d43e2d65f9
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** After the CTA, program cards with seat counts are visible in the courses section.
---

### Requirement: Sticky Navigation
- **Description:** Navbar section links scroll the single-page site to About, Courses, Mentors, Campus, and Placements.

#### Test TC004 Sticky navigation jumps to the About section
- **Test Code:** [TC004_Sticky_navigation_jumps_to_the_About_section.py](./TC004_Sticky_navigation_jumps_to_the_About_section.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/bf920f58-24e2-41f1-a9b6-9e7bf0cad06d
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** About nav link sets `#about`.
---

#### Test TC007 Use the sticky navigation to reach the About section
- **Test Code:** [TC007_Use_the_sticky_navigation_to_reach_the_About_section.py](./TC007_Use_the_sticky_navigation_to_reach_the_About_section.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/dedf7bcd-727e-417b-9114-cc780339219d
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Duplicate coverage of About navigation; behavior is consistent.
---

#### Test TC010 Use the sticky navigation to reach the Courses section
- **Test Code:** [TC010_Use_the_sticky_navigation_to_reach_the_Courses_section.py](./TC010_Use_the_sticky_navigation_to_reach_the_Courses_section.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/9eb1ce6f-9a2a-42da-ab72-714031739392
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Courses nav link shows course cards (seat counts).
---

#### Test TC014 Use the sticky navigation to reach the Placements section
- **Test Code:** [TC014_Use_the_sticky_navigation_to_reach_the_Placements_section.py](./TC014_Use_the_sticky_navigation_to_reach_the_Placements_section.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/5531423e-9ebd-42fd-b008-e83fc0df7f1c
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Placements nav link lands on hiring/placement content.
---

#### Test TC017 Use the sticky navigation to reach the Mentors section
- **Test Code:** [TC017_Use_the_sticky_navigation_to_reach_the_Mentors_section.py](./TC017_Use_the_sticky_navigation_to_reach_the_Mentors_section.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/7ded924e-67cc-45b5-94b4-17d6ff0eb731
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Mentors nav link reaches faculty content.
---

#### Test TC018 Use the sticky navigation to reach the Campus section
- **Test Code:** [TC018_Use_the_sticky_navigation_to_reach_the_Campus_section.py](./TC018_Use_the_sticky_navigation_to_reach_the_Campus_section.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/24bb0e65-437d-4cc2-be47-9736c6b29b69
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Campus nav link reaches campus-life content.
---

#### Test TC023 Continue browsing after choosing a section from the navigation menu
- **Test Code:** [TC023_Continue_browsing_after_choosing_a_section_from_the_navigation_menu.py](./TC023_Continue_browsing_after_choosing_a_section_from_the_navigation_menu.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/be93ea90-35ee-4bd4-964f-b6803329b2e1
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** After a section jump, the visitor can keep browsing without a broken layout or lost header.
---

### Requirement: About and Achievements
- **Description:** About copy and placement/achievement figures are visible on the homepage.

#### Test TC019 Read the college overview and achievement figures
- **Test Code:** [TC019_Read_the_college_overview_and_achievement_figures.py](./TC019_Read_the_college_overview_and_achievement_figures.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/3f66ff98-da9d-469f-894c-15f2e9c524c9
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** College overview and achievement stats render as static marketing content.
---

### Requirement: Courses Catalog
- **Description:** B.Tech / M.Tech / MBA listings show specializations and program metrics.

#### Test TC016 Courses section shows degrees specializations and program metrics
- **Test Code:** [TC016_Courses_section_shows_degrees_specializations_and_program_metrics.py](./TC016_Courses_section_shows_degrees_specializations_and_program_metrics.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/cb4f5dfe-e85c-4e71-addf-2daff8fb288f
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Degree programs, specializations, and seat/package metrics are visible.
---

### Requirement: Mentors, Campus Life, and Events
- **Description:** Faculty, campus, and events sections are reachable in sequence.

#### Test TC020 Mentors Campus and Events content is accessible in sequence
- **Test Code:** [TC020_Mentors_Campus_and_Events_content_is_accessible_in_sequence.py](./TC020_Mentors_Campus_and_Events_content_is_accessible_in_sequence.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/3866373a-6185-48a2-b344-05a8fdd32c01
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Mentors, campus, and events content can be viewed in one browsing session.
---

### Requirement: Placements and Footer
- **Description:** Recruiter/placement stats and footer contact plus quick links.

#### Test TC012 Placements section shows recruiters and achievement stats
- **Test Code:** [TC012_Placements_section_shows_recruiters_and_achievement_stats.py](./TC012_Placements_section_shows_recruiters_and_achievement_stats.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/7aed1d05-332d-4a6a-bc83-9e5a5eeb7d7c
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Placement credibility content (recruiters and stats) is present.
---

#### Test TC022 Contact details are visible in the footer
- **Test Code:** [TC022_Contact_details_are_visible_in_the_footer.py](./TC022_Contact_details_are_visible_in_the_footer.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/4e0e2000-247c-4a6c-857c-026763c9b266
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Footer shows contact email, phone, and address.
---

#### Test TC024 Footer quick links jump to each major section
- **Test Code:** [TC024_Footer_quick_links_jump_to_each_major_section.py](./TC024_Footer_quick_links_jump_to_each_major_section.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/ee97198a-1ebe-4f92-b0f5-4e2739bb958a
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Footer anchors to About, Programs, Faculty, Campus Life, and Placements work.
---

### Requirement: AI College Chatbot
- **Description:** Floating EduReach Bot drawer: open/close, suggested questions, custom input, and API replies.

#### Test TC003 Ask the chatbot a suggested question about courses
- **Test Code:** [TC003_Ask_the_chatbot_a_suggested_question_about_courses.py](./TC003_Ask_the_chatbot_a_suggested_question_about_courses.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/ed062acc-9d81-49bc-9943-913a276628d4
- **Status:** ✅ Passed
- **Severity:** MEDIUM
- **Analysis / Findings:** Drawer opened and a bot reply container was detected. The generated script notes an error-style reply rather than a successful RAG answer, so this pass proves a response appeared, not that course content was returned.
---

#### Test TC006 Ask the chatbot a custom admissions or fees question
- **Test Code:** [TC006_Ask_the_chatbot_a_custom_admissions_or_fees_question.py](./TC006_Ask_the_chatbot_a_custom_admissions_or_fees_question.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/d9c18d42-94b6-49af-a872-6efa0a3c729f
- **Status:** ✅ Passed
- **Severity:** MEDIUM
- **Analysis / Findings:** Custom question submitted. Observed reply was `Sorry, something went wrong. Please try again.` The UI error path works; the backend/API often did not return a successful RAG message from the tunneled preview (CORS origin is `http://localhost:5173` while preview is `4173`, and TestSprite cannot reach `localhost:5000` from the tunnel).
---

#### Test TC008 Chatbot answers a suggested question about courses
- **Test Code:** [TC008_Chatbot_answers_a_suggested_question_about_courses.py](./TC008_Chatbot_answers_a_suggested_question_about_courses.py)
- **Test Error:** TEST BLOCKED — after clicking `What courses do you offer?` a typing indicator stayed on screen and no bot reply appeared; send control remained disabled.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/e18f4e18-85e7-4824-9af1-a029eac1d794
- **Status:** ❌ Failed (blocked)
- **Severity:** HIGH
- **Analysis / Findings:** Chat request can hang without a timeout/fallback. `ChatDrawer` only shows the generic error after `sendMessage` rejects; a hung `fetch` to `http://localhost:5000/api/chat/message` leaves `sending` true. Engineering should add a request timeout and keep the user-visible error path.
---

#### Test TC009 Open chatbot and view suggested questions
- **Test Code:** [TC009_Open_chatbot_and_view_suggested_questions.py](./TC009_Open_chatbot_and_view_suggested_questions.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/45f79154-e563-4468-9eb3-6cfe7255226d
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Welcome message and suggested questions (`What courses do you offer?`, `Tell me about placements`) are visible.
---

#### Test TC011 Chatbot accepts and answers a custom admissions question
- **Test Code:** [TC011_Chatbot_accepts_and_answers_a_custom_admissions_question.py](./TC011_Chatbot_accepts_and_answers_a_custom_admissions_question.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/b1e8c8ab-a8a4-4c2b-87f5-5356234577af
- **Status:** ✅ Passed
- **Severity:** MEDIUM
- **Analysis / Findings:** Input and send work. The visible assistant message in this run was the generic error, not an admissions answer.
---

#### Test TC013 Ask a suggested course question in chat
- **Test Code:** [TC013_Ask_a_suggested_course_question_in_chat.py](./TC013_Ask_a_suggested_course_question_in_chat.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/c3c7e225-e19a-47aa-8f13-43f8d5e6af5c
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Suggested course question can be submitted from the drawer.
---

#### Test TC015 Submit a custom admissions question in chat
- **Test Code:** [TC015_Submit_a_custom_admissions_question_in_chat.py](./TC015_Submit_a_custom_admissions_question_in_chat.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/a1c92d80-032c-4316-bdd3-4428358d64ed
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Custom admissions text can be typed and sent.
---

#### Test TC021 Submit a custom question with the keyboard
- **Test Code:** [TC021_Submit_a_custom_question_with_the_keyboard.py](./TC021_Submit_a_custom_question_with_the_keyboard.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/bc09b1b0-821b-4eb5-88f5-9a554b325bde
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Enter-to-send on the chat input works.
---

#### Test TC025 Dismiss the chatbot after opening it
- **Test Code:** [TC025_Dismiss_the_chatbot_after_opening_it.py](./TC025_Dismiss_the_chatbot_after_opening_it.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/5a7ad382-3a3a-4066-9cd3-cd12eb3c2086
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Drawer can be dismissed after open.
---

#### Test TC026 Chatbot drawer can be closed after opening
- **Test Code:** [TC026_Chatbot_drawer_can_be_closed_after_opening.py](./TC026_Chatbot_drawer_can_be_closed_after_opening.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/6ddfb37c-880e-49cb-bda4-95cdfaa56f7a
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Close control hides the drawer.
---

#### Test TC027 Handle an unprocessed chat message gracefully
- **Test Code:** [TC027_Handle_an_unprocessed_chat_message_gracefully.py](./TC027_Handle_an_unprocessed_chat_message_gracefully.py)
- **Test Error:** TEST BLOCKED — typing indicator shown; no visible error such as `error`, `unable`, or `service unavailable`.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/90bc4502-a136-4761-ac77-80a914b74ee9
- **Status:** ❌ Failed (blocked)
- **Severity:** HIGH
- **Analysis / Findings:** Failure UX is inconsistent. When `fetch` rejects, the copy is `Sorry, something went wrong. Please try again.` When the request hangs, the user only sees a spinner. There is no way in the UI to inject a backend failure, and there is no timeout. Recommend AbortController timeout plus a distinct, always-visible error state.
---

#### Test TC028 Close the chatbot drawer
- **Test Code:** [TC028_Close_the_chatbot_drawer.py](./TC028_Close_the_chatbot_drawer.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/8ceebfc8-3457-4161-aeb3-3a415508238b
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Header close (X) works.
---

#### Test TC029 Minimize and reopen the chatbot drawer
- **Test Code:** [TC029_Minimize_and_reopen_the_chatbot_drawer.py](./TC029_Minimize_and_reopen_the_chatbot_drawer.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/28474a46-3613-4067-a3b4-2a76fa4d6dc5
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Minimize and reopen via the floating button work. Note: minimize and close both call the same `onClose` handler, so conversation state is not separately persisted vs closed.
---

### Requirement: Unknown Route Redirect
- **Description:** Unmatched paths should redirect to `/` and show the homepage.

#### Test TC030 Redirect unknown routes to the homepage
- **Test Code:** [TC030_Redirect_unknown_routes_to_the_homepage.py](./TC030_Redirect_unknown_routes_to_the_homepage.py)
- **Test Error:** TEST BLOCKED — browser `ERR_EMPTY_RESPONSE` / "This page isn’t working" on the unknown URL; homepage branding never appeared.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8d0efacc-162e-564f-ae5f-e96e301578d8/test/505d4637-3003-4d40-b0eb-ff3e194f9b43
- **Status:** ❌ Failed (blocked)
- **Severity:** MEDIUM
- **Analysis / Findings:** React Router in `App.jsx` does redirect `*` to `/`, but Vite preview does not always serve `index.html` for arbitrary paths, so a hard navigation to an unknown route can get an empty response instead of the SPA. Fix: configure `vite preview` / hosting with SPA fallback (`appType: 'spa'` or equivalent rewrite to `index.html`).
---

## 3️⃣ Coverage & Matching Metrics

- **90% of tests passed** (27 passed, 3 blocked/failed of 30 executed)

| Requirement | Total Tests | ✅ Passed | ❌ Failed |
|--------------------|-------------|-----------|------------|
| College Home Page | 3 | 3 | 0 |
| Sticky Navigation | 7 | 7 | 0 |
| About and Achievements | 1 | 1 | 0 |
| Courses Catalog | 1 | 1 | 0 |
| Mentors, Campus Life, and Events | 1 | 1 | 0 |
| Placements and Footer | 3 | 3 | 0 |
| AI College Chatbot | 13 | 11 | 2 |
| Unknown Route Redirect | 1 | 0 | 1 |
| **Total executed** | **30** | **27** | **3** |

Skipped (production cap): TC031, TC032 (Low priority).

Login/Sign Up were not treated as a working auth requirement (navbar buttons are UI-only).

---

## 4️⃣ Key Gaps / Risks

> 90% of executed frontend tests passed. Marketing pages, section navigation, footer, and chatbot chrome (open/close/suggestions/input) are solid.

> Highest product risk is chat reliability: several "passed" chat tests accepted a generic error bubble as a reply, while TC008/TC027 hung on the typing indicator. `POST /api/chat/message` is a separate server on port 5000 with CORS locked to `http://localhost:5173`. The preview origin is `http://127.0.0.1:4173`, so successful RAG answers are not reliably available in this environment.

> Unknown-route handling in React is correct, but production preview/hosting needs an SPA fallback so deep links do not return `ERR_EMPTY_RESPONSE`.

> Other known gaps not covered as passing product behavior: Login/Sign Up do nothing; leftover `hello` heading in `App.jsx`.
---
