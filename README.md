# Voice-Based Hindi Government Scheme Agent

This project is a **voice-first, agentic AI system** that helps users identify and apply for government/public welfare schemes in Hindi. It uses a **Planner–Executor–Evaluator loop**, maintains **conversation memory**, handles **contradictions and incomplete info**, and supports **voice input/output**.

---

## Features

- Voice input (STT) using **Whisper**
- Voice output (TTS) using **gTTS**
- Native Hindi interaction end-to-end
- Planner–Executor–Evaluator workflow
- Conversation memory with contradiction handling
- Tool integration:
  - `eligibility_tool` – determines eligibility for schemes
  - `scheme_info_tool` – fetches scheme information
- Failure handling for misheard inputs or missing data
- Frontend interface with **recording and audio playback**

---

## Folder Structure

```
Mayank_Bharti_AI_ML/backend/
├── main.py/
├── agent.py/
├── memory.py/
├── test_agent.py/
├── tools.py/
├── tests.py/
├── upload_api.py/

Frontend/
 ├── index.html/

README.md

```

---

## Requirements

````bash
pip install fastapi uvicorn whisper gtts python-multipart

uvicorn backend.main:app --reload

```

---


## Memory Handling

- Stores fields: `age`, `income`, `occupation`
- `expected_field` tracks what info is missing
- Handles contradictions:
  ```python
  if memory[key] != new_value:
      ask user for confirmation
````

---
