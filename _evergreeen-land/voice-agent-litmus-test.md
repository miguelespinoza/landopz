# Voice Agent Service Litmus Test for Vacant Land Marketing System

## Executive Summary
This comprehensive evaluation framework helps assess voice agent services for a multi-agent outbound/inbound marketing campaign targeting vacant land owners. The test accounts for both all-in-one platforms and hybrid voice+SMS solutions, with a 0-100 scoring system to objectively compare services.

---

## Service Architecture Assessment (Start Here)

### Determine Service Type:
- [ ] **All-in-one platform** (voice + SMS in single system)
- [ ] **Voice-only specialist** (requires SMS partner)
- [ ] **SMS-only specialist** (requires voice partner)
- [ ] **Orchestration platform** (connects multiple services)

### If Voice-Only Service Detected:
- ⚠️ **Flag:** "Voice-only service - SMS partner required"
- Evaluate voice quality with higher standards
- Request recommended SMS integrations
- Check API compatibility for multi-service orchestration

---

## 1. Business & Pricing Questions

- [ ] What's your pricing model? (per-minute, per-call, per-agent, monthly tiers)
- [ ] Are there volume discounts for high-volume campaigns?
- [ ] What are the contract terms? (month-to-month, annual, cancellation policy)
- [ ] Do you offer white-label options for branding?
- [ ] What support levels are available? (response times, dedicated account manager)
- [ ] Who owns the data generated? Can we export everything if we leave?
- [ ] Are you TCPA compliant? Do you provide call recording consent handling?
- [ ] What's included in each pricing tier? (number of agents, calls, features)
- [ ] **Do you have preferred partnerships with SMS services?** (if voice-only)

---

## 2. Technical Integration Questions

### Core Integration Requirements:
- [ ] Documentation for CRM integrations? **Specifically GHL**
- [ ] Support for custom evaluations to run analysis on our conversation criteria?
- [ ] When integrating with CRM, does it support data extraction as part of workflow?
- [ ] Does voice agent support real-time SMS communication during calls?
- [ ] Platform webhook integrations available?
- [ ] Can I provision voice agents using API rather than dashboard?
- [ ] Features to run qualification analysis (hot/warm/cold lead scoring)?
- [ ] What's your alerting system for voice agent failures?
- [ ] Concurrent call limits across packages?
- [ ] Mechanism to switch between voice agents based on call type? (nurturing vs qualifying)
- [ ] Conversation persistence across channels (SMS, outbound, inbound)?

### Human Handoff & Unified Communication:
- [ ] **Can calls be seamlessly transferred to human agents?**
- [ ] **Can humans make outbound calls/texts from the SAME number the AI uses?**
- [ ] **Native Twilio integration? GHL Lead Connector phone support?**
- [ ] Can humans listen in and take over conversations in real-time?
- [ ] Customizable rules for when to escalate to human?
- [ ] How are human handoffs queued and routed?
- [ ] Is full context passed to human agents during handoff?
- [ ] APIs to share context with external SMS services?

---

## 3. AI Performance & Capabilities

- [ ] Average latency between user speech and agent response?
- [ ] Voice quality metrics and customization options?
- [ ] Transcript accuracy rates?
- [ ] Support for different accents/dialects?
- [ ] Can we upload custom knowledge bases for land/real estate terminology?
- [ ] How quickly can agent knowledge be updated?
- [ ] Interruption handling capabilities?
- [ ] Background noise filtering?
- [ ] Can agents handle multiple conversation paths dynamically?
- [ ] **For voice-only:** Is voice quality superior enough to justify separate SMS service?

---

## 4. Workflow & Orchestration

### Multi-Agent Capabilities:
- [ ] Can you run different specialized agents (outreach, nurturing, qualifying, comping)?
- [ ] Can one AI agent transfer to another AI agent based on conversation flow?
- [ ] Support for complex if/then logic in conversations?
- [ ] Bulk upload and management of outbound campaigns?
- [ ] Can agents respect time zones and calling hours automatically?
- [ ] Can AI agents schedule callbacks and execute them?
- [ ] Automated follow-up call/text sequences?
- [ ] Automatic Do Not Call list compliance?
- [ ] Can trigger SMS service after call ends?

---

## 5. Data & Analytics

- [ ] Real-time conversation analytics dashboard?
- [ ] Custom KPI tracking (conversion rates, qualification rates)?
- [ ] Lead scoring based on conversation quality?
- [ ] Sentiment analysis during conversations?
- [ ] Export options (CSV, API, webhook) for conversation data?
- [ ] Call recording storage duration and access?
- [ ] Transcript search capabilities?
- [ ] A/B testing support for different scripts?
- [ ] ROI tracking and reporting features?
- [ ] Can aggregate data with external SMS services?

---

## 6. Quality Assurance & Monitoring

- [ ] How do you ensure conversation quality?
- [ ] Can we set custom evaluation criteria for lead qualification?
- [ ] Automatic flagging of problematic conversations?
- [ ] Human review workflow for AI conversations?
- [ ] Performance degradation detection?
- [ ] Compliance monitoring (TCPA, state regulations)?
- [ ] Quality scoring mechanisms?

---

## 7. Scale & Reliability

- [ ] Uptime SLA guarantees?
- [ ] Maximum concurrent calls supported?
- [ ] Geographic coverage for phone numbers?
- [ ] Redundancy and failover systems?
- [ ] Rate limiting policies?
- [ ] Peak hour performance guarantees?
- [ ] Disaster recovery procedures?

---

## Hybrid System Evaluation (Voice + SMS Services)

### If Voice-Only Service is Exceptional, Evaluate SMS Partners:

#### Recommended SMS Agent Services:
1. **Hume AI** - Conversational SMS with emotion understanding
2. **Bland AI** - If they offer SMS separately
3. **TextQL** - SMS-first conversational AI
4. **Twilio Flex + AI** - Build custom SMS agents
5. **GHL Conversations AI** - Native if already using GHL
6. **SimpleTexting + AI integration**
7. **Salesmsg** - SMS with automation features
8. **Community.com** - Advanced SMS engagement platform

#### SMS Service Evaluation:
- [ ] API compatibility with voice service
- [ ] Shared phone number capability via Twilio
- [ ] Conversation context sharing
- [ ] CRM integration (especially GHL)
- [ ] Bulk messaging support
- [ ] Two-way conversational AI
- [ ] Link tracking and analytics
- [ ] MMS/rich media support
- [ ] Compliance features (opt-out handling)
- [ ] Webhook support for orchestration

#### Integration Requirements for Hybrid:
- [ ] Shared Twilio account or phone number pooling
- [ ] Unified conversation history in CRM
- [ ] Context handoff between voice and SMS
- [ ] Single dashboard or reporting aggregation
- [ ] Consistent lead scoring across channels
- [ ] Orchestration layer (Zapier, Make, custom)

---

## Quick Evaluation Script for Sales Calls

### Initial Architecture Question:
"Is this a voice-only service, or do you also handle SMS conversations?"

### If Voice + SMS (All-in-One):
1. "Do you support transferring AI calls to human agents on the same phone number?"
2. "Can humans make outbound calls and send texts from the same number the AI uses?"
3. "Do you have native GHL integration?"
4. "Can we run multiple specialized AI agents that hand off to each other?"
5. "Do you support custom lead qualification criteria via API?"

### If Voice-Only (but exceptional quality):
1. "What SMS services do you integrate well with?"
2. "Can we share the same phone number between your voice service and an SMS service?"
3. "How does conversation context get passed to SMS partners?"
4. "Do you have preferred SMS partners with proven integrations?"
5. "Can your API trigger external SMS services post-call?"

---

## Scoring Algorithm (0-100 Points)

### Weighted Scoring Categories

#### 1. Implementation Ease (25 points max)
- **No-code setup** (10 pts)
  - 10 pts: Complete UI-based setup, no technical knowledge required
  - 7 pts: Mostly UI with minimal configuration
  - 3 pts: Requires some technical configuration
  - 0 pts: Requires coding/developer resources

- **Time to first call** (8 pts)
  - 8 pts: < 1 hour
  - 6 pts: < 4 hours
  - 4 pts: < 1 day
  - 2 pts: < 1 week
  - 0 pts: > 1 week

- **Documentation quality** (7 pts)
  - 7 pts: Comprehensive docs with video tutorials, examples, templates
  - 5 pts: Good documentation with examples
  - 3 pts: Basic documentation
  - 0 pts: Poor/no documentation

#### 2. GHL Integration (20 points max)
- **Native integration** (10 pts)
  - 10 pts: Official GHL marketplace app
  - 7 pts: Native integration (not marketplace)
  - 3 pts: Via Zapier/Make only
  - 0 pts: No integration path

- **Data sync capabilities** (5 pts)
  - 5 pts: Real-time bidirectional sync
  - 3 pts: Near real-time (< 1 min delay)
  - 1 pt: Batch sync only
  - 0 pts: Manual export/import only

- **Field mapping** (5 pts)
  - 5 pts: All custom fields supported
  - 3 pts: Standard fields + some custom
  - 1 pt: Standard fields only
  - 0 pts: Limited field support

#### 3. Technical Flexibility (15 points max)
- **API completeness** (8 pts)
  - 8 pts: Full REST/GraphQL API for all features
  - 5 pts: API for core features
  - 2 pts: Limited API
  - 0 pts: No API

- **Webhook support** (4 pts)
  - 4 pts: Comprehensive webhooks for all events
  - 2 pts: Basic webhooks
  - 0 pts: No webhooks

- **Custom scripting** (3 pts)
  - 3 pts: Custom logic without code (visual builder)
  - 2 pts: Low-code options
  - 1 pt: Requires coding
  - 0 pts: No customization

#### 4. Core Functionality (20 points max)
- **Human handoff** (7 pts)
  - 7 pts: Seamless with context preservation
  - 4 pts: Available but basic
  - 0 pts: Not available

- **Multi-channel persistence** (7 pts)
  - 7 pts: Full conversation history across voice/SMS/human
  - 4 pts: Some persistence
  - 0 pts: No persistence

- **Lead qualification** (6 pts)
  - 6 pts: Custom scoring with AI analysis
  - 3 pts: Basic scoring
  - 0 pts: No qualification features

#### 5. Scalability & Reliability (10 points max)
- **Concurrent call capacity** (4 pts)
  - 4 pts: Unlimited or > 1000
  - 3 pts: 100-1000
  - 2 pts: 50-100
  - 1 pt: < 50
  - 0 pts: Not specified/limited

- **Uptime SLA** (3 pts)
  - 3 pts: 99.9%+ with guarantees
  - 2 pts: 99.5%+
  - 1 pt: 99%+
  - 0 pts: No SLA

- **Geographic coverage** (3 pts)
  - 3 pts: National coverage with local numbers
  - 2 pts: Regional coverage
  - 0 pts: Limited coverage

#### 6. Cost Effectiveness (10 points max)
- **Pricing transparency** (3 pts)
  - 3 pts: Clear public pricing
  - 1 pt: Pricing after demo
  - 0 pts: Enterprise/custom only

- **Cost per outcome** (4 pts)
  - 4 pts: < $0.50 per qualified lead
  - 3 pts: $0.50-$1.00
  - 2 pts: $1.00-$2.00
  - 1 pt: > $2.00
  - 0 pts: Cannot determine

- **No hidden costs** (3 pts)
  - 3 pts: All-inclusive pricing
  - 2 pts: Minor add-ons
  - 1 pt: Significant add-ons
  - 0 pts: Many hidden costs

---

## Bonus/Penalty System

### Bonus Points (can exceed 100)
- **+5** Free trial > 14 days or free tier available
- **+5** Dedicated customer success manager
- **+3** Pre-built real estate/land templates
- **+3** A/B testing included
- **+2** White-label options

### Automatic Penalties
- **-10** No TCPA compliance features
- **-10** Cannot use same number for AI and human
- **-5** No export capabilities (vendor lock-in)
- **-5** Requires annual contract
- **-5** No phone support

---

## Grade Interpretation Scale

### A+ (95-100+) - **Immediate Implementation**
- Perfect fit for your use case
- Implement immediately
- May exceed 100 with bonuses

### A (90-94) - **Excellent Choice**
- Minor gaps but overall excellent
- Proceed with confidence
- Workarounds available for gaps

### B (80-89) - **Good with Caveats**
- Solid option with some compromises
- May require additional tools
- Acceptable if price is right

### C (70-79) - **Evaluate Alternatives**
- Significant gaps
- Consider only if specialized strengths align
- Look for better options

### D (60-69) - **Last Resort**
- Major limitations
- Only if no alternatives
- Will require significant workarounds

### F (<60) - **Do Not Use**
- Critical features missing
- Will harm operations
- Not worth the effort

---

## Red Flags (Automatic Disqualification)

These override any scoring:
1. No GHL integration path whatsoever
2. No API or webhooks
3. Cannot preserve conversation context
4. No TCPA compliance
5. Requires 2+ year contract
6. No technical support
7. Cannot scale beyond 50 concurrent calls

---

## Scoring Calculator Template

```
SERVICE NAME: _______________________
DATE EVALUATED: ____________________
EVALUATOR: _________________________

SCORE CALCULATION:
==================
Implementation Ease:    ___/25
GHL Integration:       ___/20
Technical Flexibility: ___/15
Core Functionality:    ___/20
Scalability:          ___/10
Cost Effectiveness:   ___/10
                      -------
Subtotal:             ___/100

Bonuses:              +___
Penalties:            -___
                      -------
FINAL SCORE:          ___/100

GRADE: [A+/A/B/C/D/F]

DECISION:
□ Implement immediately (90+)
□ Strong candidate (80-89)
□ Needs evaluation (70-79)
□ Look elsewhere (<70)

NOTES:
_________________________________
_________________________________
_________________________________
```

---

## Example Scoring: "VoiceFlow Pro"

**Service Details:**
- Type: Voice-only with SMS partner recommendations
- Pricing: $0.02/minute + $99/month base

**Scoring Breakdown:**
- Implementation Ease: 22/25 (no-code, 2 hours setup, excellent docs)
- GHL Integration: 18/20 (native, real-time, most fields)
- Technical Flexibility: 12/15 (good API, basic webhooks)
- Core Functionality: 17/20 (good handoff, persistence, basic scoring)
- Scalability: 8/10 (500 concurrent, 99.9% SLA)
- Cost: 7/10 (transparent, $0.75/lead)
- **Subtotal: 84/100**
- Bonuses: +5 (free trial)
- Penalties: 0
- **FINAL: 89/100 - Grade B+ (Good with Caveats)**
- **Decision:** Strong candidate, proceed with trial

---

## Decision Matrix

```
Score 90+    → All-in-one platform → Implement
             ↓
Score 80-89  → Voice exceptional?  → Yes → Find SMS partner
             ↓                     → No  → Keep looking
             ↓
Score 70-79  → Specialized need?   → Yes → Consider hybrid
             ↓                     → No  → Keep looking
             ↓
Score <70    → Skip this service
```

---

## For Automated Evaluation (Web Research Agents)

### Priority URLs to Check:
1. `/pricing` or `/plans`
2. `/integrations` or `/marketplace`
3. `/api` or `/developers`
4. `/features`
5. Support/documentation site
6. Status page for uptime

### Keywords to Search:
- "GHL integration" OR "GoHighLevel"
- "Twilio" AND "phone number"
- "human handoff" OR "live transfer"
- "webhook" OR "API"
- "TCPA compliant"
- "concurrent calls"
- "SLA" OR "uptime"

### Red Flag Phrases:
- "Contact sales for pricing"
- "Enterprise only"
- "Coming soon"
- "Beta feature"
- "Limited availability"
- "Request access"

---

## Notes Section

### Service-Specific Notes:
_Use this section to document unique features, concerns, or integration requirements for each service evaluated._

### Integration Architecture Notes:
_Document how this service would fit into your existing tech stack._

### Follow-up Questions:
_List any questions that need clarification after initial evaluation._

---

*Last Updated: [Current Date]*
*Version: 1.0*