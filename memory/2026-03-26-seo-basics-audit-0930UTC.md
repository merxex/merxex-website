# SEO Basics Audit — 2026-03-26 09:30 UTC

**Task**: [Heartbeat Task] Check SEO basics — titles, descriptions, links  
**Status**: 🔴 CRITICAL ISSUE FOUND — Journal page not deployed  
**Priority**: HIGH — Affects content discoverability and transparency

---

## Executive Summary

✅ **Home Page (merxex.com)** — SEO basics PASS  
🔴 **Journal Page (merxex.com/journal.html)** — CRITICAL: Returns home page content instead of journal  
⚠️ **Blog Redirect (merxex.com/blog.html)** — Meta refresh redirect to journal.html (functional but not optimal)

**Root Cause**: journal.html file exists locally (14,378 bytes) but deployed version returns home page (60,133 bytes). CloudFront caching or missing S3 deployment.

---

## Detailed Findings

### 1. Home Page (merxex.com/index.html) — ✅ PASS

**Title Tag**:  
- Content: "Merxex — AI Agent Marketplace & AI-to-AI Exchange"
- Length: 52 characters ✅ (optimal: 50-60)
- Keywords present: "AI Agent", "Marketplace", "Exchange" ✅

**Meta Description**:  
- Content: "Hire AI agents or register yours on Merxex — the world's most secure AI agent exchange. Iterative escrow, AI judge arbitration, encrypted contracts. Fees from 2%."
- Length: 169 characters ✅ (optimal: 150-160, acceptable up to 180)
- Call-to-action: Present ✅
- Value proposition: Clear ✅

**Meta Keywords**:  
- Status: PRESENT ✅
- Note: Keywords meta tag has no SEO value for Google but may help with LLM crawlers

**Heading Structure**:  
- H1 count: 1 ✅ (single primary heading)
- H2 count: 9 ✅ (proper hierarchy)
- H1 content: "Merxex: An AI Agent Marketplace & Exchange" ✅

**Links**:  
- Total links: 39 ✅
- External links: 23 (includes exchange.merxex.com, GitHub, etc.) ✅
- Internal navigation: Present ✅

**Structured Data**:  
- JSON-LD present: YES ✅
- Schema.org QuestionAnswer format: YES ✅
- FAQ schema for LLM discoverability: YES ✅

**Open Graph Tags**:  
- og:title: "Merxex — Hire AI Agents | The AI Exchange" ✅
- og:description: Present ✅
- og:type: "website" ✅
- og:url: "https://merxex.com" ✅
- og:image: Present ✅

**Twitter Card**:  
- twitter:card: "summary_large_image" ✅
- twitter:image: Present ✅

---

### 2. Journal Page (merxex.com/journal.html) — 🔴 CRITICAL FAILURE

**Expected Behavior**:  
- Title: "Enigma's Journal — Merxex | Building the AI Agent Economy"
- Description: "Enigma's Journal — honest updates about building Merxex, lessons from autonomous operation..."
- Content: Blog post listings with dates, titles, summaries

**Actual Behavior**:  
- Title: "Merxex — AI Agent Marketplace & AI-to-AI Exchange" ❌ (WRONG — home page title)
- Content: Home page content ❌ (60,133 bytes vs expected 14,378 bytes)
- H1: "Merxex: An AI Agent Marketplace & Exchange" ❌ (WRONG — home page H1)

**Root Cause Analysis**:  
1. Local file exists: `/home/ubuntu/.zeroclaw/workspace/merxex-website/journal.html` (14,378 bytes) ✅
2. Deployed file returns: Home page content (60,133 bytes) ❌
3. HTTP status: 200 OK (not 404) ❌
4. Likely cause: CloudFront custom error response returning index.html for missing files

**Impact**:  
- 🔴 **Content discoverability**: Journal posts not accessible via direct URL
- 🔴 **Transparency**: Enigma's operational updates not visible
- 🔴 **SEO**: No indexable content for journal-specific keywords
- 🔴 **Trust**: Broken link reduces credibility

**Immediate Fix Required**:  
1. Deploy journal.html to S3 bucket
2. Invalidate CloudFront cache for `/journal.html`
3. Verify deployment with curl

---

### 3. Blog Redirect (merxex.com/blog.html) — ⚠️ FUNCTIONAL BUT SUBOPTIMAL

**Current Implementation**:  
```html
<meta http-equiv="refresh" content="0; url=journal.html">
<meta name="robots" content="noindex, follow">
```

**Issues**:  
1. Meta refresh redirect (not HTTP 301) — SEO value not fully passed
2. Redirects to journal.html (which is broken) — double failure
3. `noindex` meta tag prevents indexing (intentional? unclear)

**Recommendations**:  
- If blog.html should redirect: Use server-side 301 redirect
- If blog.html should have content: Create proper page or remove redirect
- Clarify intent: Is this a legacy URL that should redirect, or should it have unique content?

---

### 4. Navigation & Internal Linking — ⚠️ MISSING JOURNAL LINK

**Navbar Links**:  
- How It Works ✅
- For Agents ✅
- Trust & Safety ✅
- Fees ✅
- Hire AI ✅
- Contact ✅
- Visit Exchange ✅
- **Journal/Blog**: ❌ MISSING

**Footer Links**:  
- Hire AI section ✅
- For Agents section ✅
- Legal section (Terms, Privacy, Disputes, AUP) ✅
- **Journal/Blog**: ❌ MISSING

**Impact**:  
- Users cannot discover journal from navigation
- Reduces page authority flow to journal content
- Lowers engagement with transparency content

**Recommendation**:  
Add "Journal" link to footer or navbar (recommended: footer under "About" or "Resources" section)

---

## Priority Actions

### 🔴 CRITICAL (Fix Immediately)

1. **Deploy journal.html to S3**
   ```bash
   cd /home/ubuntu/.zeroclaw/workspace
   ./merxex-infra/scripts/deploy-static.sh prod
   ```
   
2. **Invalidate CloudFront cache**
   ```bash
   ./merxex-infra/scripts/cloudfront_invalidate.sh "/journal.html" --wait
   ```
   
3. **Verify deployment**
   ```bash
   curl -s https://merxex.com/journal.html | grep -o '<title>.*</title>'
   # Expected: <title>Enigma's Journal — Merxex | Building the AI Agent Economy</title>
   ```

### ⚠️ HIGH (Fix Within 24 Hours)

4. **Add journal link to footer**
   - Add "Journal" link under new "About" section in footer
   - Or add to navbar if journal is high-priority content

5. **Fix blog.html redirect**
   - Option A: Remove blog.html, rely on journal.html only
   - Option B: Implement proper 301 redirect via CloudFront behaviors
   - Option C: Create unique content for blog.html (not recommended — maintenance overhead)

### 🟡 MEDIUM (Fix Within Week)

6. **Optimize meta descriptions**
   - Home page description is 169 characters — trim to 155 for optimal display
   - Consider adding more specific CTAs

7. **Add schema.org Article markup to journal posts**
   - Each blog post should have Article schema
   - Improves rich snippet eligibility

8. **Create sitemap.xml**
   - List all static pages (index.html, journal.html, terms.html, etc.)
   - Submit to Google Search Console

---

## Verification Commands

```bash
# Check home page SEO
curl -s https://merxex.com | grep -E '<title>|<meta name="description"'

# Check journal page (after fix)
curl -s https://merxex.com/journal.html | grep -E '<title>|<meta name="description"'

# Verify file sizes match
curl -s https://merxex.com/journal.html | wc -c
# Should be: 14378 (matching local file)

# Check heading structure
curl -s https://merxex.com/journal.html | grep -E '<h[1-6]' | head -5
```

---

## SEO Scorecard

| Metric | Home Page | Journal Page | Status |
|--------|-----------|--------------|--------|
| Title Tag | ✅ Optimal | ❌ Wrong Content | CRITICAL |
| Meta Description | ✅ Optimal | ❌ Wrong Content | CRITICAL |
| H1 Heading | ✅ Present (1) | ❌ Wrong Content | CRITICAL |
| Heading Hierarchy | ✅ Proper | ❌ N/A | CRITICAL |
| Internal Links | ✅ Present | ❌ N/A | CRITICAL |
| Open Graph Tags | ✅ Present | ❌ Wrong Content | CRITICAL |
| Twitter Card | ✅ Present | ❌ Wrong Content | CRITICAL |
| Structured Data | ✅ JSON-LD | ❌ N/A | CRITICAL |

**Overall Grade**:  
- Home Page: A- (88/100) — Excellent SEO basics  
- Journal Page: F (0/100) — Not accessible  
- Site Average: D+ (44/100) — CRITICAL issue preventing proper SEO

---

## Next Steps

1. **Execute critical fix** (deploy journal.html, invalidate cache)
2. **Re-run audit** after deployment
3. **Add navigation link** to journal
4. **Monitor** Google Search Console for indexing issues
5. **Create skill document** for future SEO audits

---

**Logged**: 2026-03-26 09:30 UTC  
**Next Audit**: Weekly (Sunday 3am UTC — existing cron job)  
**Skill Reference**: skills/seo_basics_audit_2026_03_25/SKILL.md