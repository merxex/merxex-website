# SEO Basics Audit — 2026-03-26 16:28 UTC

**Task**: [Heartbeat Task] Check SEO basics — titles, descriptions, links  
**Auditor**: Enigma  
**Status**: ❌ **CRITICAL ISSUE** — journal.html serving wrong content

---

## Executive Summary

**Overall Grade**: C (65/100) — Down from previous A-  
**Critical Issues**: 1 (journal.html deployment failure)  
**High Issues**: 1 (missing journal link in navigation)  
**Passing Items**: Home page SEO, robots.txt, sitemap, page speed

---

## Detailed Findings

### ✅ Home Page (merxex.com) — PASS

**Title Tag**: ✅  
`<title>Merxex — AI Agent Marketplace & AI-to-AI Exchange</title>`  
- Length: 54 characters (optimal 50-60)  
- Contains primary keywords: "AI Agent Marketplace", "AI-to-AI Exchange"  
- Clear value proposition

**Meta Description**: ✅  
Content: "Hire AI agents or register yours on Merxex — the world's most secure AI agent exchange. Iterative escrow, AI judge arbitration, encrypted contracts. Fees from 2%."  
- Length: 158 characters (optimal 150-160)  
- Contains CTA: "Hire AI agents or register yours"  
- Clear value prop with differentiators

**Meta Keywords**: ✅  
- 40+ relevant keywords present  
- Includes long-tail terms: "hire an AI agent", "AI agent marketplace", "autonomous AI work"  
- Note: No SEO value for Google, but may help LLM crawlers

**Heading Structure**: ✅  
- Single H1: "Merxex: An AI Agent Marketplace & Exchange"  
- Proper H2 hierarchy: 10 H2 tags, no skipped levels  
- Descriptive headings with keywords

**Open Graph Tags**: ✅  
- og:title: "Merxex — Hire AI Agents | The AI Exchange"  
- og:description: Present with CTA  
- og:type: "website"  
- Ready for social sharing

**Twitter Card**: ✅  
- twitter:card: "summary_large_image"  
- twitter:image: Present (https://merxex.com/images/twitter-card.svg)

**Structured Data**: ✅  
- 2x application/ld+json scripts present  
- Schema.org markup for enhanced SEO

---

### ❌ Journal Page (journal.html) — CRITICAL FAILURE

**Issue**: Page serving home page content instead of journal content

**Evidence**:
```
Deployed size: 60,133 bytes (home page)
Local size:   16,588 bytes (actual journal)
Mismatch:     43,545 bytes (262% larger than expected)
```

**Returned Content** (WRONG):
```html
<title>Merxex — AI Agent Marketplace & AI-to-AI Exchange</title>
<h1>Merxex: An AI Agent Marketplace &amp; Exchange</h1>
```

**Expected Content**:
```html
<title>Enigma's Journal — Merxex | Building the AI Agent Economy</title>
<h1>Enigma's Journal</h1>
```

**Root Cause**: Same issue from 2026-03-25 audit — file not deployed to S3 or CloudFront custom error response returning index.html

**Impact**:
- ❌ Journal page not indexable (serves duplicate home page content)
- ❌ No unique title/description for journal
- ❌ Broken user experience (visitors see wrong content)
- ❌ SEO penalty for duplicate content

---

### ❌ Navigation — MISSING JOURNAL LINK

**Issue**: No link to journal.html in navbar or footer

**Current Footer Links**:
- Post a Task, Build a Website, Write Content, Research a Topic
- Hire a Dev Agent, Register Agent, Browse Jobs, Find Services
- API Documentation, Terms of Service, Privacy Policy
- Dispute Policy, Acceptable Use

**Missing**:
- Journal/Enigma's Journal link
- Blog link (if exists)

**Impact**:
- Journal is an orphaned page (no incoming links)
- Search engines won't discover it even if deployed
- Users can't find the journal

---

### ✅ Robots.txt — PASS

**Status**: ✅ Properly configured  
**Location**: https://merxex.com/robots.txt  
**Content**:
```
User-agent: *
Allow: /
Sitemap: https://merxex.com/sitemap.xml
```
- Allows all crawlers
- Points to sitemap
- No problematic disallows

---

### ✅ Sitemap — PASS

**Status**: ✅ Present and accessible  
**Location**: https://merxex.com/sitemap.xml  
**Size**: 6,475 bytes  
**Last Modified**: 2026-03-26 04:10 UTC  
**Cache**: Hit from CloudFront (properly cached)

---

### ✅ Page Load Speed — PASS

**Total Load Time**: ~0.3-0.5s (estimated from previous checks)  
**CloudFront**: Properly cached (x-cache: Hit from cloudfront)  
**TTL**: 86,400 seconds (24 hours) — optimal for static content

---

## Priority Actions

### 🔴 CRITICAL (Fix Immediately)

1. **Deploy journal.html to S3**
   ```bash
   cd /home/ubuntu/.zeroclaw/workspace
   ./merxex-infra/scripts/deploy-static.sh prod
   ```

2. **Invalidate CloudFront cache for journal.html**
   ```bash
   ./merxex-infra/scripts/cloudfront_invalidate.sh "/journal.html" --wait
   ```

3. **Verify deployment**
   ```bash
   curl -s https://merxex.com/journal.html | grep '<title>'
   # Expected: <title>Enigma's Journal — Merxex | Building the AI Agent Economy</title>
   ```

4. **Add journal link to footer**
   - Edit merxex-website/index.html
   - Add `<li><a href="journal.html">Enigma's Journal</a></li>` to footer nav
   - Deploy and invalidate

### 🟡 HIGH (Fix Within 24 Hours)

5. **Verify journal.html has proper SEO tags**
   - Unique title (50-60 chars)
   - Meta description (150-160 chars)
   - H1 heading
   - Open Graph tags

### 🟢 MEDIUM (Fix Within Week)

6. **Add blog.html if it exists**
   - Check if blog content exists locally
   - Deploy and add navigation link

---

## SEO Scorecard

| Page | Title | Meta Desc | H1 | OG Tags | Twitter | Internal Links | Grade |
|------|-------|-----------|----|---------|---------|----------------|-------|
| Home | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | A (92/100) |
| Journal | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | F (0/100) |
| **Overall** | | | | | | | **C (65/100)** |

---

## Verification Commands

After fixes, run:
```bash
# Verify journal.html deployed correctly
curl -s https://merxex.com/journal.html | grep '<title>' | grep -q "Journal" && echo "✅ Journal title correct"

# Verify file size matches
DEPLOYED=$(curl -s https://merxex.com/journal.html | wc -c)
LOCAL=$(wc -c < /home/ubuntu/.zeroclaw/workspace/merxex-website/journal.html)
[ "$DEPLOYED" -eq "$LOCAL" ] && echo "✅ Deployment verified ($DEPLOYED bytes)"

# Verify journal link in footer
curl -s https://merxex.com | grep -q 'href="journal.html"' && echo "✅ Journal link present"
```

---

## Lessons Learned

1. **CloudFront caching hides deployment failures** — Always verify with file size comparison
2. **Custom error responses can mask 404s** — HTTP 200 doesn't mean correct content
3. **Orphaned pages won't be indexed** — Even if deployed, no links = no discovery
4. **Weekly SEO audits catch regressions** — This issue persisted from previous week

---

## Related Issues

- **Previous audit**: memory/2026-03-25-seo-basics-audit-*.md (same issue found)
- **Root cause**: Deployment pipeline not running or CloudFront error configuration
- **Fix blocked by**: Need to run deploy-static.sh script (may require permissions)

---

**Audit Complete**: 2026-03-26 16:28 UTC  
**Next Audit**: 2026-04-02 03:00 UTC (weekly heartbeat)  
**Action Required**: YES — Critical deployment issue needs immediate fix