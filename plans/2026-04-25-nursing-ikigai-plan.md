---
status: ACTIVE
created: 2026-04-25
based_on: CEO Plan 2026-04-24-pathlab-ikigai-hypothesis.md
---

# PathLab Content Plan: Nursing (Ikigai Hypothesis Test)

## Overview

This is the content implementation plan for the **5-Day Nursing PathLab** — the first test of the Ikigai Hypothesis: *"Students can't visualize their option space. They think the choice is binary (A vs B) when real life is combinatorial."*

The PathLab introduces students to nursing not as a single track, but as a **craft that can be combined** with passions and community impact. Through a hybrid practitioner story, students discover that life design is about combination, not compromise.

---

## Content Architecture

```
Path: "พยาบาล: มากกว่าอาชีพ คือการออกแบบชีวิต"
├── Day 0: Values Card Sort (Pre-assessment)
├── Day 1: ลองเป็นพยาบาล 1 วัน (Simulation)
├── Day 2: 3 แบบ 3 สไตล์ (Practitioner Archetypes)
├── Day 3: เรื่องจริงของพี่น้ำ (Hybrid Practitioner Story)
├── Day 4: ลองจัดชีวิตตัวเอง (Design Exercise)
└── Day 5: ประกาศเจตนารมณ์ (Declaration + Next Path)
```

---

## Day 0: Values Card Sort

**Purpose:** Surface the "A vs B" tension before the PathLab begins. Give students language for their internal conflict.

**Activity Type:** `daily_reflection` (checklist + ranking)

**Content:**
- 5 value cards: ความมั่นคง | ความคิดสร้างสรรค์ | การช่วยเหลือผู้อื่น | อิสระ | การเติบโต
- Drag-to-rank: "เรียงลำดับ 5 ค่านี้จากสำคัญที่สุด"
- Reflection prompt: "มีช่วงไหนที่รู้สึกต้องเลือกระหว่าง 2 ค่านี้?"

**Storage:** `path_reflections` table with `day_number: 0`, `metadata.values_ranking`

---

## Day 1: ลองเป็นพยาบาล 1 วัน

**Purpose:** Immersive simulation to understand the craft before seeing possibilities.

**Activities:**
1. **Morning Briefing** (text): "คุณคือพยาบาลวันแรก นี่คือรายชื่อผู้ป่วย 10 คน"
2. **Triage Simulation** (npc_chat): ผู้ป่วยเข้ามา 3 คน พยาบาลต้องตัดสินใจใครก่อน
3. **Afternoon Round** (text): เรื่องราวจากผู้ป่วยแต่ละคน
4. **End of Shift Reflection** (daily_reflection): "วันนี้รู้สึกอย่างไร? อะไรที่ท้าทายที่สุด?"

**Assessment:** `text_answer` — "ถ้าคุณเป็นพยาบาวันนี้จริง ๆ คุณภูมิใจที่สุดตอนไหน?"

---

## Day 2: 3 แบบ 3 สไตล์

**Purpose:** Show that nursing has multiple forms — not just hospital.

**Activities:**
1. **Archetype A: สายมั่นคง** (text) — พยาบาลโรงพยาบาลรัฐ 20 ปี, มีครอบครัว, สบายใจ
2. **Archetype B: สายอิสระ** (text) — พยาบาลสวยงามเดินทาง, ทำงานต่างประเทศ, ฟรีแลนซ์
3. **Archetype C: สายสร้างสรรค์** (text) — พยาบาล + คอนเทนต์ครีเอเตอร์, สอนออนไลน์, ทำคอร์ส
4. **But wait...** (text): "These are 3 possible versions. You might be a 4th, 5th, 10th."

**Reflection:** "แบบไหนที่คุณรู้สึก 'อื้ม น่าสนใจ' มากที่สุด?"

---

## Day 3: เรื่องจริงของพี่น้ำ

**Purpose:** The core hypothesis test — a real hybrid practitioner story that makes combination feel possible, not anomalous.

**Activities:**
1. **Meet P'Nam** (text): พี่น้ำ — พยาบาล 10 ปี ที่ทำงานโรงพยาบาล 3 วัน/สัปดาห์ + ร้านเบเกอรี่ + สอนพยาบาลออนไลน์
2. **Day in Her Life** (text + image): ตารางเวลาจริงของพี่น้ำ
3. **The Table** (text):
   | Craft | Passion | Impact |
   |-------|---------|--------|
   | พยาบาล 3 วัน/สัปดาห์ | เบเกอรี่ | สุขภาพชุมชน |
   | สอนออนไลน์ | ทำคอนเทนต์ | ให้ความรู้ |
   | | | |
   | **พยาบาล + อะไรสักอย่าง** | | |

   *"Don't optimize. Notice what your body feels."*

4. **Q&A with P'Nam** (ai_chat):
   - System prompt: "คุณคือพี่น้ำ พยาบาลที่ออกแบบชีวิตแบบไฮบริด..."
   - Objective: "ให้นักเรียนถามคำถามเกี่ยวกับการผสมผสานอาชีพได้อย่างสบายใจ"
   - Max messages: 15

**Assessment:** `text_answer` (auto-save enabled):
"ถ้าคุณเป็น 'พี่น้ำคนต่อไป' Craft + Passion + Impact ของคุณจะเป็นอะไร?"

---

## Day 4: ลองจัดชีวิตตัวเอง

**Purpose:** Agency-building exercise — students design their own hybrid.

**Activities:**
1. **Your Values Review** (text): แสดงผลลัพธ์จาก Values Card Sort (Day 0)
2. **The Hybrid Canvas** (text + interactive):
   - ช่อง 1: อาชีพหลัก (craft) — "อะไรที่คุณทำได้ดี?"
   - ช่อง 2: ความชอบ (passion) — "อะไรที่ทำแล้วลืมเวลา?"
   - ช่อง 3: ผลกระทบ (impact) — "ใครที่คุณอยากช่วย?"
   - ช่อง 4: "ชื่อเล่น" ของไลฟ์สไตล์นี้
3. **Reality Check** (text): "ไม่ต้องสมบูรณ์ ไม่ต้องถูกต้อง นี่คือ draft แรก"

**Assessment:** `text_answer` (auto-save enabled):
"ออกแบบชีวิตตัวเองใน 3 บรรทัด: 'ฉันทำ ___ + ฉันชอบ ___ + ฉันช่วย ___ = ___'"

---

## Day 5: ประกาศเจตนารมณ์

**Purpose:** Declaration + commitment to next exploration. The "loop" moment.

**Activities:**
1. **Your Journey Map** (text): สรุปสิ่งที่เรียนรู้ 5 วัน
2. **The Declaration** (text_answer):
   - "ฉันประกาศว่าฉันจะ..." (ลองทำอะไรต่อ)
   - "ฉันอยากรู้เพิ่มเรื่อง..." (topic ที่สนใจ)
   - "Path ต่อไปที่ฉันอยากลอง..." (เลือกจากรายการ หรือ เสนอเอง)
3. **Closing Message** (text):
   "You've completed 1 of 3 recommended explorations. ชีวิตไม่ใช่การเลือกครั้งเดียว แต่เป็นการลองไปเรื่อย ๆ"

**Assessment:** `text_answer` — "Path ต่อไปที่อยากลอง" (primary output)

---

## Database Seed Plan

### Tables to Populate

```sql
-- 1. Create Path
INSERT INTO paths (title, description, duration_days, category, is_published, visibility)
VALUES (
  'พยาบาล: มากกว่าอาชีพ คือการออกแบบชีวิต',
  '5 วันลองเป็นพยาบาล และค้นพบว่าอาชีพคือจุดเริ่มต้น ไม่ใช่จุดจบ',
  5,
  'healthcare',
  false,  -- hidden until ready
  'draft' -- CEO plan: feature flag via seed visibility
);

-- 2. Create 5 Path Days (+ Day 0 for values)
INSERT INTO path_days (path_id, day_number, title, description)
VALUES 
  (path_id, 0, 'ค่าของคุณคืออะไร?', 'เรียนรู้ตัวเองก่อนเริ่ม'),
  (path_id, 1, 'ลองเป็นพยาบาล 1 วัน', 'Simulation ชีวิตพยาบาล'),
  (path_id, 2, '3 แบบ 3 สไตล์', 'พยาบาลมีหลายหน้า'),
  (path_id, 3, 'เรื่องจริงของพี่น้ำ', 'ไฮบริดที่เป็นไปได้'),
  (path_id, 4, 'ลองจัดชีวิตตัวเอง', 'ออกแบบชีวิตตัวเอง'),
  (path_id, 5, 'ประกาศเจตนารมณ์', 'วันประกาศและ Path ต่อไป');

-- 3. Create Activities (~15 activities across 5 days)
-- See detailed activity list below

-- 4. Create Content (path_content rows)
-- text, npc_chat, ai_chat, video placeholders

-- 5. Create Assessments (path_assessments rows)
-- text_answer for Day 1, 3, 4, 5

-- 6. Create AI Chat Configuration (Day 3)
-- system_prompt, objective, completion_criteria in path_content.metadata

-- 7. Create NPC Conversation (Day 1 Triage)
-- path_npc_conversations + nodes + choices
```

### Activity Count per Day

| Day | Activities | Content Types | Assessments |
|-----|-----------|---------------|-------------|
| 0 | 1 | checklist | - |
| 1 | 4 | text, npc_chat | text_answer |
| 2 | 4 | text (3 archetypes) | text_answer |
| 3 | 4 | text, ai_chat | text_answer (auto-save) |
| 4 | 3 | text, interactive | text_answer (auto-save) |
| 5 | 3 | text | text_answer |

**Total: ~19 activities, 6 assessments, 3 AI/NPC interactions**

---

## Content Style Guide

### Tone
- **Conversational Thai** — "พี่น้ำ" ไม่ใช่ "คุณน้ำ"
- **Agency-building** — "คุณออกแบบได้" ไม่ใช่ "คุณต้องเลือก"
- **Possibility-oriented** — "อาจจะ" ไม่ใช่ "ต้อง"
- **Authentic** — เรื่องจริงของคนจริง

### Key Phrases (from CEO plan)
- "These are 3 possible versions. You might be a 4th, 5th, 10th."
- "Don't optimize. Notice what your body feels."
- "พยาบาล + อะไรสักอย่าง"
- "You've completed 1 of 3 recommended explorations"
- "ชีวิตไม่ใช่การเลือกครั้งเดียว แต่เป็นการลองไปเรื่อย ๆ"

---

## Implementation Checklist

### Content Creation
- [ ] Day 0: Values card sort content + 5 value definitions
- [ ] Day 1: Morning briefing text + patient list
- [ ] Day 1: Triage NPC conversation tree (5-7 nodes)
- [ ] Day 1: Afternoon round stories (3 patient stories)
- [ ] Day 2: Archetype A content (สายมั่นคง)
- [ ] Day 2: Archetype B content (สายอิสระ)
- [ ] Day 2: Archetype C content (สายสร้างสรรค์)
- [ ] Day 3: P'Nam profile + day-in-life
- [ ] Day 3: Hybrid table (4 columns)
- [ ] Day 3: AI chat system prompt + objective
- [ ] Day 4: Values review (reference Day 0)
- [ ] Day 4: Hybrid canvas instructions
- [ ] Day 5: Journey map summary
- [ ] Day 5: Declaration prompts
- [ ] Day 5: Closing message + next path suggestions

### Technical Setup
- [ ] Seed script for all content
- [ ] Auto-save implementation for Day 3/5 text answers
- [ ] AI chat configuration (passion-6 model)
- [ ] NPC conversation tree for triage
- [ ] Values card sort storage (path_reflections JSONB)
- [ ] Feature flag: visibility = 'draft'

### Testing
- [ ] Internal review: read all content end-to-end
- [ ] Test AI chat with sample messages
- [ ] Test NPC conversation all paths
- [ ] Test auto-save behavior
- [ ] Test values ranking storage
- [ ] Pilot: 3 students

---

## Success Metrics (from CEO Plan)

| Metric | Target | How to Track |
|--------|--------|-------------|
| Day 5 completion | >70% | `path_activity_progress.status = 'completed'` |
| Mention "combination" or "hybrid" in Day 5 | >30% | Text analysis of Day 5 submission |
| Want to try another PathLab | >50% | Day 5 "Path ต่อไป" is non-empty |
| Values card sort completion | >80% | `path_reflections` where day_number = 0 |

---

## Files to Create

```
/pathlab-content/
├── README.md (existing)
├── plans/
│   └── 2026-04-25-nursing-ikigai-plan.md (this file)
├── seeds/
│   └── nursing-path-seed.sql
├── content/
│   ├── day-0-values-card.md
│   ├── day-1-simulation/
│   │   ├── morning-briefing.md
│   │   ├── triage-npc-tree.md
│   │   └── afternoon-rounds.md
│   ├── day-2-archetypes/
│   │   ├── archetype-a-stable.md
│   │   ├── archetype-b-free.md
│   │   └── archetype-c-creative.md
│   ├── day-3-pnam-story/
│   │   ├── pnam-profile.md
│   │   ├── day-in-life.md
│   │   └── ai-chat-prompt.md
│   ├── day-4-design/
│   │   ├── hybrid-canvas.md
│   │   └── design-exercise.md
│   └── day-5-declaration/
│       ├── journey-summary.md
│       └── declaration-prompts.md
```

---

## Next Steps

1. **This week:** Create all content files
2. **Next week:** Build seed script + test internally
3. **Week 3:** Pilot with 3 students
4. **Week 4:** Analyze metrics + decide next PathLab topic

---

*Based on CEO Plan: PathLab Ikigai Hypothesis Test (2026-04-24)*
*Hypothesis: Students can't visualize their option space. Real life is combinatorial, not binary.*
