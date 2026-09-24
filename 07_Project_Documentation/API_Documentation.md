# LegalEase API Documentation

## GET /
Checks that the backend is running.

## GET /api/health
Returns backend status and whether Gemini is configured.

## GET /api/document-types
Returns supported document types.

## POST /api/generate

```json
{
  "document_type": "Employment Contract",
  "parties": "ABC Pvt Ltd (Employer); Jane Doe (Employee)",
  "terms": "Salary is INR 40,000 per month; Confidentiality applies",
  "dates": "1 October 2026",
  "jurisdiction": "Tamil Nadu, India"
}
```

## POST /api/export/txt
## POST /api/export/docx
## POST /api/export/pdf

```json
{
  "document_type": "Employment Contract",
  "document": "EMPLOYMENT CONTRACT\n\n1. PARTIES\n..."
}
```
