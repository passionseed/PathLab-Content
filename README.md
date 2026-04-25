# PathLab Content

Structured learning content for [PassionSeed](https://passionseed.io) — a gamified mobile learning platform where students discover their passions through interactive paths, AI conversations, and achievement-based progression.

## What is PathLab?

PathLab is PassionSeed's core learning delivery system. It transforms traditional coursework into **gamified learning paths** where students progress through daily activities, unlock nodes on visual learning maps, and engage with AI tutors and NPC characters.

Think of it as a learning management system meets RPG progression — complete with sprites, boss nodes, branching dialogues, and AI-powered coaching.

---

## Content Types

PathLab supports two main categories of activities: **Content** (learning material) and **Assessment** (evaluation).

### Content Activities

| Type | Description | Example |
|------|-------------|---------|
| `video` / `short_video` | Embedded video content | Tutorial walkthroughs, lectures |
| `text` / `daily_prompt` | Articles, prompts, written content | Reading assignments, daily questions |
| `image` | Image-based learning material | Diagrams, infographics |
| `pdf` | PDF documents | Worksheets, reading packets |
| `canva_slide` | Canva presentations | Slide decks, visual guides |
| `resource_link` | External links | Reference materials, tools |
| `npc_chat` | Branching NPC conversations | Scenario-based roleplay, guided decision trees |
| `ai_chat` | Dynamic AI tutoring | Career exploration, brainstorming, reflection |

### Assessment Activities

| Type | Description | Grading |
|------|-------------|---------|
| `quiz` | Multiple choice questions | Auto-graded |
| `daily_reflection` | Guided reflection prompts | Instructor/TA graded |
| `text_answer` | Long-form written responses | Instructor/TA graded |
| `file_upload` | Project submissions, documents | Instructor/TA graded |
| `checklist` | Task completion lists | Auto-checked |

---

## System Architecture

### Learning Maps (Visual Pathways)

Interactive node-based maps built with React Flow:

- **Nodes** — Individual learning topics with content and assessments
- **Paths** — Connections defining prerequisite relationships
- **Sprites** — Gamified visuals for nodes (crystals, bosses, custom images)
- **Unlocking** — Nodes unlock based on completion of prerequisites

### Activity Structure

```
Path
├── Path Days (daily lessons)
│   ├── Activities
│   │   ├── Content (video, text, ai_chat, npc_chat, etc.)
│   │   └── Assessment (quiz, reflection, file_upload, etc.)
│   └── Progress Tracking
└── Cohort Enrollments
```

### Progress & Gamification

- **Status States**: `locked` → `unlocked` → `in_progress` → `submitted` → `passed`/`failed`
- **Leaderboards**: Rank students by completion speed and grades
- **Visual Feedback**: Color-coded nodes (green=passed, red=failed, blue=submitted, orange=in-progress)
- **Time Tracking**: Estimated minutes per activity, actual time spent

---

## Key Features

### 🤖 AI Chat Activities
Objective-driven conversations with AI tutors:
- Custom system prompts define the AI's role (career counselor, study coach, etc.)
- Real-time progress analysis (0-100% completion)
- Automatic completion detection when objectives are met
- Full conversation history persistence

### 🎭 NPC Conversation System
Branching dialogue trees for scenario-based learning:
- Question nodes, statement nodes, and endings
- Conditional choices based on previous selections
- NPC avatars with emotions and personality
- Progress tracking through choice history

### 📝 Draft Activity System
Work-in-progress workflow for content creators:
- Save incomplete activities as drafts
- Visual draft badges and missing-field indicators
- RLS policies protect students from accessing unfinished content
- Automatic completeness validation

### 🗺️ Map Editor
Visual drag-and-drop editor for building learning paths:
- Create nodes, connect with paths, arrange layouts
- Configure content and assessments per node
- Batch operations for complex map updates
- Real-time preview of student experience

---

## Database Schema (Summary)

### Core Tables
- `paths` — Learning paths/curricula
- `path_days` — Daily lessons within a path
- `path_activities` — Individual learning activities
- `path_content` — Activity content (video, text, AI config, etc.)
- `path_assessment` — Activity assessments (quizzes, reflections, etc.)

### Progress Tracking
- `path_activity_progress` — Student activity completion status
- `path_ai_chat_sessions` — AI chat session state
- `path_npc_conversation_progress` — NPC dialogue progress

### Map System
- `learning_maps` — Top-level learning maps
- `map_nodes` — Individual nodes
- `node_paths` — Connections between nodes
- `student_node_progress` — Node completion tracking

---

## Activity Configuration

### AI Chat Metadata
```json
{
  "system_prompt": "You are a supportive career counselor...",
  "objective": "Help student identify 3 potential career paths",
  "completion_criteria": "Student has listed 3 careers with explanations",
  "model": "passion-6",
  "max_messages": 30
}
```

### NPC Chat Metadata
```json
{
  "conversation_id": "uuid-of-conversation-tree",
  "allow_restart": false,
  "show_history": true
}
```

### Quiz Assessment
```json
{
  "assessment_type": "quiz",
  "points_possible": 100,
  "quiz_questions": [
    {
      "question_text": "What is a variable?",
      "options": ["A storage location", "A function", "A loop"],
      "correct_answer": 0
    }
  ]
}
```

---

## Content Creation Workflow

1. **Create a Path** — Define the learning journey
2. **Add Path Days** — Structure into daily lessons
3. **Create Activities** — Add content and assessments per day
4. **Configure Content** — Set up videos, AI prompts, NPC conversations
5. **Set Assessments** — Define quizzes, reflections, or submissions
6. **Enroll Cohorts** — Assign student groups to the path
7. **Publish** — Make activities live (non-draft) for students

---

## Tech Stack

- **Frontend**: Next.js 15, React, TypeScript, Tailwind CSS
- **Visualization**: React Flow (node-based maps)
- **Backend**: Supabase (PostgreSQL, Auth, Real-time)
- **AI**: Custom models (passion-6) for chat activities
- **Mobile**: React Native with Expo

---

## Related Repositories

- `passionseed/docs` — System documentation and design specs
- `passionseed/mobile` — React Native mobile app
- `passionseed/web` — Next.js web dashboard

---

*Part of the [PassionSeed](https://passionseed.io) learning platform — Discover Your Passion, Ignite Your Potential.*
