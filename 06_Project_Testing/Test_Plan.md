# Phase 6 – Project Testing

## Automated tests

From `05_Project_Development`:

```powershell
pytest -q
```

Tests cover root, health, document types, validation, generation, TXT, DOCX and PDF exports.

## Manual UI test

1. Start FastAPI.
2. Start Streamlit.
3. Select Employment Contract.
4. Enter parties.
5. Enter terms separated by semicolons.
6. Enter effective date.
7. Click Generate Legal Document.
8. Confirm preview.
9. Edit one sentence.
10. Download TXT, DOCX and PDF.
11. Open each file and verify content.

## Gemini test

Add a valid Gemini API key to `.env`, restart FastAPI, generate a document, and verify that the sidebar reports Gemini as configured and the source is `gemini`.
