# Phase 8 – Project Demonstration Script

## Suggested 3–5 minute demo

### 1. Introduction
Say:
> This is LegalEase, an AI-Powered Legal Document Generator. It accepts basic legal-document information, generates an AI-assisted draft, lets the user edit the result, and exports the document as TXT, DOCX, or PDF.

### 2. Show project phases
Show the eight phase folders.

### 3. Run backend
Show FastAPI starting on port 8000.

### 4. Run frontend
Show Streamlit in the browser.

### 5. Generate
Use Employment Contract, ABC Pvt Ltd (Employer), Jane Doe (Employee), salary INR 40,000/month, confidentiality, 30-day notice, and 1 October 2026.

### 6. Edit
Change one sentence in the preview.

### 7. Export
Download TXT, DOCX and PDF and open at least one file.

### 8. Explain AI
When `GEMINI_API_KEY` is configured, the backend sends a structured prompt to Gemini. Without a key, the local fallback keeps the application testable.

### 9. Legal safety
> LegalEase produces AI-assisted drafts and does not replace professional legal advice. Users should review the output with a qualified legal professional before real-world use.
