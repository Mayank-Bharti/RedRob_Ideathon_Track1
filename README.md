# 🎙️ GovAssist: Voice-Based Government Scheme Assistant

![Ideathon Track](https://img.shields.io/badge/Track-1%3A%20The%20AI%20Systems%20Architect-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Prototype-success?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Hindi-orange?style=for-the-badge)

GovAssist is a **voice-first, autonomous AI system** designed to help Indian citizens (especially gig and blue-collar workers) discover and apply for government welfare schemes. By using a sophisticated **Planner–Executor–Evaluator** architecture, it replaces tedious manual web browsing and rule-reading with a simple, natural Hindi voice conversation.

This project was built for the **Redrob Ideathon (Challenge 1: The AI Systems Architect: Reimagining Work)**, transforming how social workers and citizens navigate complex bureaucracy.

---

## 📑 Table of Contents
1. [The Problem & Vision](#the-problem-vision)
2. [Key Features](#key-features)
3. [System Architecture](#system-architecture)
4. [Folder Structure](#folder-structure)
5. [Installation & Setup](#installation-setup)
6. [How to Run](#how-to-run)
7. [Future Roadmap](#future-roadmap)
8. [Demo Video](#demo-video)

---

<a id="the-problem-vision"></a>
## 🚨 The Problem & Vision
Discovering eligibility for government welfare schemes in India is incredibly manual. Millions of eligible citizens miss out on life-changing benefits due to low digital literacy, language barriers, and complex rulebooks. 

GovAssist acts as an **Intelligent Co-pilot**. Instead of typing into complex portals, a user simply speaks to the agent in Hindi. The AI automatically extracts their demographic data, resolves contradictions, checks eligibility tools, and responds with matched schemes via Voice.

---

<a id="key-features"></a>
## ✨ Key Features
- **Voice-Native Interaction:** End-to-end Hindi voice input (Whisper STT) and output (gTTS). No typing required.
- **Agentic Loop (Not a Chatbot):** Driven by a Planner-Executor-Evaluator pattern for deterministic, safe decision-making.
- **Stateful Memory Management:** Remembers user context (Age, Income, Occupation) across turns and intelligently prompts for missing data.
- **Contradiction Resolution:** Automatically detects if a user changes their story mid-conversation and prompts for clarification to prevent hallucinations.
- **Redrob Ecosystem Ready:** Designed as a modular microservice that can be integrated into HR/Gig-worker platforms to deliver "Welfare-as-a-Benefit."

---

<a id="system-architecture"></a>
## 🧠 System Architecture

The core of the system relies on an autonomous AI loop rather than simple prompt engineering:
1. **Planner:** Analyzes transcribed Hindi text. Extracts variables via deterministic/rule-based state management. Decides if more info is needed.
2. **Executor:** Once all required data (Age, Income, Occupation) is gathered, it invokes external eligibility tools to compute scheme matches.
3. **Evaluator:** Formats the final response logically and triggers the Text-to-Speech engine.

---

<a id="folder-structure"></a>
## 📂 Folder Structure

```text
RedRob_Ideathon_Track1/
│
├── Mayank_Bharti_AI_ML/
│   ├── backend/               # FastAPI backend and Agent logic
│   │   ├── main.py            # API entry point & audio routing
│   │   ├── agent.py           # Core Planner-Executor-Evaluator loop
│   │   ├── memory.py          # Stateful conversation memory & tracking
│   │   ├── tools.py           # Eligibility and scheme retrieval tools
│   │   ├── upload_api.py      # Audio upload handling
│   │   ├── test_agent.py      # Local testing scripts
│   │
│   ├── frontend/              
│   │   └── index.html         # Voice recording UI & Chat interface
│   │
│   └── transcripts.txt        # Stored conversation logs
│
├── Demo Video/                # Contains video walkthrough of the system
├── Document_folder/           # Architectural diagrams and PDFs
└── README.md                  # Project documentation
```

---

<a id="installation-setup"></a>
## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- [FFmpeg](https://ffmpeg.org/download.html) (Required by Whisper for audio processing)

### 1. Clone the repository
```bash
git clone https://github.com/Mayank-Bharti/RedRob_Ideathon_Track1.git
cd RedRob_Ideathon_Track1
```

### 2. Install dependencies
Install the required Python packages using pip:
```bash
pip install fastapi uvicorn openai-whisper gtts python-multipart
```
*(Note: Whisper may require PyTorch. If you encounter issues, install PyTorch separately based on your system specs from [pytorch.org](https://pytorch.org/)).*

---

<a id="how-to-run"></a>
## 🚀 How to Run

1. **Start the Backend Server**
   Navigate to the `backend` folder and start the FastAPI server:
   ```bash
   cd Mayank_Bharti_AI_ML/backend
   uvicorn main:app --reload
   ```

2. **Open the Frontend**
   Simply open the `Mayank_Bharti_AI_ML/frontend/index.html` file in any modern web browser (Chrome, Edge, Firefox).

3. **Start Talking!**
   - Click the record button and speak in Hindi (e.g., *"Main 30 saal ka kisan hoon, meri aamdani 2 lakh hai"*).
   - Wait for the agent to process the audio, extract your information, and reply with Voice!

---

<a id="future-roadmap"></a>
## 🔮 Future Roadmap
- **DPI Integration:** Linking with Aadhaar and DigiLocker for instant, document-free scheme applications.
- **Read-Write Capabilities:** Moving from just *finding* schemes to actually *applying* for them on behalf of the user via RPA.
- **WebSockets / Low-Latency Audio:** Upgrading from REST APIs to bidirectional streaming to achieve <500ms voice response times.

<a id="demo-video"></a>
## Demo Video
### [Click to see the working here:](https://drive.google.com/drive/folders/1h7-uB-zpBBxKAb4iJJHjq8bpMtfxS6Dl?usp=sharing)
