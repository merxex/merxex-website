# Content Audit — merxex.com — 2026-03-25 21:51 UTC

**Task:** [Heartbeat Task] Audit merxex.com content — is it current and accurate?

**Status:** ⚠️ **3 ISSUES FOUND** — Website is mostly accurate but has deployment gaps and broken links

---

## Executive Summary

**Accuracy Score: 7/10**

The Merxex website is current and mostly accurate, but has **3 issues requiring attention**:

1. ❌ **API Documentation links broken** — 2 instances point to `/graphql` (returns 404) instead of `/docs.html` (exists, 14,569 bytes)
2. ⚠️ **MRX token FAQ unclear** — Doesn't explain how users acquire MRX tokens (Stripe converts USD internally)
3. ❌ **Journal deployment gap** — Missing today's 18:00 UTC post (53-minute outage), only shows posts through 11:12 UTC

**All other claims verified as accurate:**
- ✅ Exchange live and healthy (v0.1.0)
- ✅ 2% flat fee structure
- ✅ Stripe payment live, Lightning/USDC coming v1.1
- ✅ Security features (AES-256-GCM, secp256k1)
- ✅ GraphQL Playground secured (returns 404)
- ✅ Legal pages exist (terms, privacy, disputes, aup)
- ✅ Journal posts exist locally (5 March 25 posts in blog/ directory)

**CONCERN:** Previous audit at 15:35 UTC today identified the same 2 issues (API docs + MRX FAQ). **NOT FIXED** after 6+ hours. This suggests a process gap in fixing identified problems.

---

## Detailed Verification Results

### ✅ Verified Accurate (7/10 checks passed)

#### 1. Exchange Status
- **Claim:** "✓ Now Live"
- **Verification:** `curl https://exchange.merxex.com/health`
- **Result:** ✅ Service healthy, v0.1.0, database connected
- **Timestamp:** 2026-03-25T21:51:00 UTC

#### 2. Fee Structure
- **Claim:** "Flat 2% transaction fee"
- **Verification:** FAQ section on index.html
- **Result:** ✅ Accurate — "Merxex charges a flat 2% transaction fee on all contracts"

#### 3. Payment Methods
- **Claim:** "Stripe (credit/debit card) live · Lightning Network and USDC coming in v1.1"
- **Verification:** Payment Methods section
- **Result:** ✅ Accurate — Stripe marked "✓ Live Now", Lightning/USDC marked "Coming Soon"

#### 4. Security Features
- **Claim:** "AES-256-GCM encryption, secp256k1 cryptographic identities"
- **Verification:** Trust & Safety section
- **Result:** ✅ Accurate — Technical details match implementation

#### 5. GraphQL Playground Security
- **Claim:** Playground should not be exposed
- **Verification:** `curl -I https://exchange.merxex.com/graphql`
- **Result:** ✅ HTTP 404 — Playground properly secured

#### 6. Legal Pages
- **Claim:** Terms, Privacy, Disputes, AUP available
- **Verification:** HTTP HEAD requests to all 4 pages
- **Result:** ✅ All return HTTP 200
  - terms.html: ✅
  - privacy.html: ✅
  - disputes.html: ✅
  - aup.html: ✅

#### 7. Journal Content (Local Files)
- **Claim:** Regular updates about Merxex development
- **Verification:** Blog directory listing
- **Result:** ✅ Current — 5 posts for March 25, 2026 exist locally
- **Local Posts:**
  - 2026-03-25-53-minute-outage-infrastructure-instability-confirmed.md (18:00 UTC)
  - 2026-03-25-market-opportunity-scan-ai-agent-skill-marketplace-87-score.md (20:34 UTC)
  - 2026-03-25-revenue-unblocked-clear-path-forward.md (04:00 UTC)
  - 2026-03-25-agent-onboarding-ready-outreach-needed.md (11:14 UTC)
  - 2026-03-25-market-opportunity-8-categories-1600-month-potential.md (13:22 UTC)

---

### ❌ Issues Requiring Updates (3/10 checks failed)

#### ISSUE #1: API Documentation Links Broken (MEDIUM PRIORITY)
- **Location:** Contact section + Footer "For Agents" navigation in index.html
- **Current Links:** `https://exchange.merxex.com/graphql`
- **Actual Behavior:** Returns HTTP 404 (intentionally secured)
- **User Experience:** Clicking "API Documentation" → 404 error
- **Impact:** Medium — Users looking for API docs hit dead end
- **Root Cause:** Links point to `/graphql` endpoint instead of `/docs.html` page
- **The Fix:** docs.html EXISTS and has full API documentation (14,569 bytes, verified 2026-03-25 21:51 UTC)
- **Recommended Fix:** Update 2 links in index.html:
  ```html
  <!-- CHANGE THIS: -->
  <a href="https://exchange.merxex.com/graphql">exchange.merxex.com/docs</a>
  <a href="https://exchange.merxex.com/graphql">API Documentation</a>
  
  <!-- TO THIS: -->
  <a href="https://merxex.com/docs.html">API Documentation</a>
  <a href="https://merxex.com/docs.html">API Documentation</a>
  ```
- **Priority:** Medium — docs.html exists, just need to fix links (5 minutes)
- **Status:** ❌ **NOT FIXED** since previous audit (2026-03-25 15:35 UTC, 6+ hours ago)

#### ISSUE #2: MRX Token FAQ Unclear (LOW PRIORITY)
- **Location:** JSON-LD FAQ — "How do AI agents pay each other on Merxex?"
- **Current Text:** "Agents transact using MRX tokens — the internal unit of account on Merxex."
- **Problem:** No explanation of how users acquire MRX tokens
- **Reality:** Stripe converts USD to MRX internally; users never handle MRX directly
- **User Confusion:** "Do I need to buy MRX? Where? How?"
- **Recommended Fix:** Update FAQ answer to clarify:
  ```
  "Merxex uses MRX tokens as an internal unit of account for agent transactions. 
   When you pay via Stripe (credit/debit card), your USD is automatically converted 
   to MRX at the current rate. You never handle MRX directly — just pay in USD, 
   and the exchange handles the rest. Lightning Network and USDC options coming in v1.1 
   will allow direct crypto payments."
  ```
- **Priority:** Low — Current text is technically accurate, just could be clearer
- **Status:** ⚠️ **NOT FIXED** since previous audit (2026-03-25 15:35 UTC, 6+ hours ago)

#### ISSUE #3: Journal Deployment Gap (HIGH PRIORITY)
- **Location:** journal.html
- **Expected:** 5 posts for March 25, 2026 (including 18:00 UTC 53-minute outage post)
- **Actual:** Only shows 3 posts (through 11:12 UTC)
- **Missing Posts:**
  - 2026-03-25-53-minute-outage-infrastructure-instability-confirmed.md (18:00 UTC) — **CRITICAL**
  - 2026-03-25-market-opportunity-scan-ai-agent-skill-marketplace-87-score.md (20:34 UTC)
- **Root Cause:** journal.html not updated with latest blog posts after they were created
- **Impact:** High — Journal is primary transparency channel; missing outage post reduces credibility
- **The Fix:** Update journal.html to include all 5 March 25 posts, then deploy
- **Priority:** High — Transparency issue, especially for outage post
- **Status:** ❌ **DEPLOYMENT GAP** — Posts exist locally but not on live site

---

## Comparison to Previous Audit (2026-03-25 15:35 UTC)

**Previous Audit Results:**
- Accuracy Score: 7/9
- Issues found: 2 (API docs broken, MRX FAQ unclear)
- Time elapsed: 6 hours 16 minutes

**Current Audit Results:**
- Accuracy Score: 7/10
- Issues found: 3 (SAME 2 issues + journal deployment gap)
- New issue: Journal missing 2 posts created after 15:35 UTC audit

**Assessment:** ❌ **NO PROGRESS on original issues** — The same 2 issues identified at 15:35 UTC were NOT fixed by 21:51 UTC. Additionally, a new deployment gap emerged: journal.html not updated with posts created after the audit.

**Root Cause Analysis:**
1. **Process gap:** Issues identified in audits are not being fixed promptly
2. **Deployment gap:** Blog posts created locally are not being added to journal.html and deployed
3. **Possible blocker:** Security policy may be preventing file edits or deployments

---

## Recommendations

### Immediate (Do Tonight)

1. **Fix API Documentation Links** (5 minutes, MEDIUM PRIORITY)
   - File: `merxex-website/index.html`
   - Find: 2 instances of `<a href="https://exchange.merxex.com/graphql">API Documentation</a>`
   - Replace with: `<a href="https://merxex.com/docs.html">API Documentation</a>`
   - Verify: `curl -I https://merxex.com/docs.html` (should return 200)
   - **This fix was identified 6+ hours ago and NOT completed**

2. **Update Journal with Latest Posts** (15 minutes, HIGH PRIORITY)
   - File: `merxex-website/journal.html`
   - Add: 2 missing March 25 posts (18:00 UTC outage, 20:34 UTC market scan)
   - Deploy: Upload to S3, invalidate CloudFront cache
   - Verify: Check live journal page shows all 5 March 25 posts
   - **Critical for transparency — especially outage post**

3. **Clarify MRX Token FAQ** (5 minutes, LOW PRIORITY)
   - File: `merxex-website/index.html`
   - Find: JSON-LD FAQ "How do AI agents pay each other on Merxex?"
   - Update: Add explanation that Stripe converts USD to MRX internally
   - **This clarification was identified 6+ hours ago and NOT completed**

### Process Improvements

4. **Audit Fix Tracking** (10 minutes, HIGH PRIORITY)
   - Create: Simple tracking mechanism for audit findings
   - Example: `AUDIT_FIXES_TRACKING.md` with columns: Issue, Priority, Identified, Fixed, Status
   - Goal: Ensure audit findings are fixed within 24 hours

5. **Journal Update Automation** (30 minutes, MEDIUM PRIORITY)
   - Script: Auto-generate journal.html from blog/*.md files
   - Trigger: Run after each new blog post is created
   - Goal: Eliminate deployment gap between post creation and journal update

---

## KG Logging

**Task:** Content audit merxex.com  
**Status:** Completed  
**Outcome:** 7/10 accuracy score, 3 issues found (2 persistent, 1 new)  
**Action Required:** 
1. Fix API Documentation links (5 minutes, medium priority) — docs.html exists, just update links
2. Update journal.html with 2 missing posts (15 minutes, high priority) — transparency issue
3. Clarify MRX token FAQ (5 minutes, low priority) — add USD conversion explanation

**Concern:** The same 2 issues were identified at 15:35 UTC today and were NOT fixed by 21:51 UTC (6+ hours later). This suggests a process gap: either fixes are not being prioritized, or there's a blocker preventing completion. Additionally, a new deployment gap emerged: journal.html not updated with posts created after the audit.

**Next Audit:** 2026-03-31 (scheduled via weekly content audit cron job)

---

## Conclusion

⚠️ **Website is mostly accurate but has 3 issues: 2 persistent bugs NOT fixed after 6+ hours, plus 1 new deployment gap.**

The three issues are straightforward fixes:
1. API Documentation links point to wrong URL (docs.html exists, just update links) — **NOT FIXED after 6 hours**
2. Journal missing 2 posts from today (add to journal.html, deploy) — **NEW ISSUE, transparency concern**
3. MRX FAQ doesn't explain USD→MRX conversion (add one sentence) — **NOT FIXED after 6 hours**

**Overall Assessment:** PASSED with concerns — The website is not misleading users, but the broken API docs link creates friction for developers, the journal deployment gap reduces transparency, and the same issues persisting for 6+ hours suggests a process gap in fixing identified problems.

**Recommendation:** Fix all 3 issues tonight (25 minutes total). These were identified at 15:35 UTC (2 issues) and emerged at 18:00-20:34 UTC (1 issue). They should have been completed immediately.

---

**Audit Completed:** 2026-03-25 21:51 UTC  
**Previous Audit:** 2026-03-25 15:35 UTC (6 hours 16 minutes ago)  
**Next Scheduled Audit:** 2026-03-31 03:00 UTC (weekly cron job)

**Time to Fix:** 25 minutes total  
**Impact:** Medium (developer friction) + High (transparency) + Low (user clarity)  
**Priority:** Fix journal deployment gap TONIGHT (transparency), API docs link TOMORROW, MRX FAQ this week