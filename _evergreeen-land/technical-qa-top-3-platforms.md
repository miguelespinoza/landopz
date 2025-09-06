# Technical Q&A: Top 3 Outbound Voice Agent Platforms

## Questions for Evaluation

1. Do you have documentation for CRM integrations? Specifically GHL
2. Does your product support custom evaluations to run analysis on our criteria of a good conversation
3. When integrating with a CRM, does it support data extraction as part of the workflow?
4. Does the voice agent support real-time SMS communication? like say to send a text message of the companies website?
5. Does the platform allow webhook integrations?
6. Can I provision voice agents using an API, rather than through the dashboard manually?
7. Are there features to run a qualification analysis on a conversation, to check if it's a hot, warm, or cold lead?
8. What's your alerting system when there's a failure with a voice agent?
9. What are your limits for concurrent calls across different packages?
10. Is there a mechanism/workflow with voice agents to switch between voice agents depending on the type of inbound call? nurturing vs qualifying for example
11. Does the voice agent have support to track conversations/threads with a lead throughout multiple touch-points? (aka outbound agent starts lead conversation, lead calls inbound voice agent, and inbound voice agent knows who it is and has full context)

---

## 1. Synthflow

### Q1: GHL Documentation
✅ **Yes** - Native GoHighLevel marketplace app with extensive documentation
- Direct installation from GHL app store
- 21-day typical deployment with guided setup documentation
- Complete workflow automation guides

### Q2: Custom Conversation Evaluations
⚠️ **Partial** - Pre-built templates with some customization
- Industry-specific templates available
- Basic sentiment analysis included
- Limited custom evaluation framework

### Q3: CRM Data Extraction
✅ **Yes** - Full bi-directional data flow
- Real-time sync with all GHL objects
- Custom field mapping supported
- Post-call data extraction and updates

### Q4: Real-time SMS Support
✅ **Yes** - Through GHL integration
- Can trigger SMS workflows in GHL
- Send links, appointment confirmations
- Multi-channel orchestration supported

### Q5: Webhook Integrations
✅ **Yes** - Extensive webhook support
- Native webhook sync with GHL
- Custom triggers and workflows
- Real-time event notifications

### Q6: API Provisioning
❌ **No** - Dashboard-only provisioning
- No-code platform design
- Manual agent creation required
- Bulk provisioning not documented

### Q7: Lead Qualification Analysis
✅ **Yes** - Built-in lead scoring
- Automatic lead scoring based on conversation
- Hot/warm/cold categorization
- Integration with GHL lead scoring

### Q8: Failure Alerting
⚠️ **Limited** - Basic alerting
- Dashboard notifications
- Email alerts for failures
- Limited real-time monitoring

### Q9: Concurrent Call Limits
- **Starter**: Not specified
- **Pro**: Not specified  
- **Agency**: 100 concurrent calls
- **Enterprise**: Custom limits

### Q10: Agent Switching/Routing
⚠️ **Partial** - Through workflow builder
- Can route based on initial inputs
- Limited dynamic switching mid-call
- Workflow-based routing available

### Q11: Conversation Threading
✅ **Yes** - Through GHL integration with custom fields
- **Implementation**: Uses custom fields (Agent Triggered, Booking Status, Property Details) to track context
- **Multi-Assistant Support**: Different AI assistants can handle different stages (screening, appointment setting, reminders)
- **Data Persistence**: Custom field matching ensures context accuracy across calls
- **Workflow Integration**: Webhook-based data capture maintains conversation state
- **Limitation**: Context primarily stored in GHL, not native to Synthflow

---

## 2. SimpleTalk.ai

### Q1: GHL Documentation
⚠️ **Limited** - Native integration advertised but limited docs
- API key authentication documented
- Limited public documentation available
- Setup complexity not well documented

### Q2: Custom Conversation Evaluations
✅ **Yes** - Advanced analytics capabilities
- Custom evaluation criteria supported
- Real-time conversation analysis
- Performance metrics tracking

### Q3: CRM Data Extraction
✅ **Yes** - Bi-directional data flow
- Custom field mapping
- Post-call data sync
- Real-time updates during calls

### Q4: Real-time SMS Support
✅ **Yes** - Multi-channel capabilities
- Can trigger SMS during calls
- Send follow-up messages
- Integrated with communication workflows

### Q5: Webhook Integrations
✅ **Yes** - Webhook-based triggers
- Custom webhook endpoints
- Real-time event notifications
- Workflow automation support

### Q6: API Provisioning
⚠️ **Unknown** - Not documented
- API capabilities mentioned but unclear
- May support programmatic provisioning
- Contact sales for details

### Q7: Lead Qualification Analysis
✅ **Yes** - Advanced qualification features
- Multi-stage follow-up logic
- Lead scoring capabilities
- Automated qualification workflows

### Q8: Failure Alerting
⚠️ **Unknown** - Not documented
- Basic monitoring assumed
- Alert system details not public
- Enterprise features may include advanced alerting

### Q9: Concurrent Call Limits
- **Business Plan**: Up to 1,800 calls/minute
- **Agency Plan**: Up to 1,800 calls/minute
- **Enterprise**: Custom scaling
- Highest capacity in market

### Q10: Agent Switching/Routing
✅ **Yes** - Intelligent routing
- Round-robin support
- Phone tree navigation
- Dynamic routing capabilities

### Q11: Conversation Threading
✅ **Yes** - Native persistent context feature
- **Persistent Context**: AI remembers past conversations across multiple interactions automatically
- **Multi-Channel Memory**: Context maintained across voice, text, email, and social channels
- **CRM Integration**: Uses unique contact identifiers to link all conversations to specific individuals
- **Dynamic Personalization**: Pulls CRM data for context-aware interactions
- **Real-time Updates**: Tags and updates contact status based on conversation outcomes
- **Transcript Storage**: Converts all conversations to searchable text for comprehensive history
- **95% Accuracy**: In detecting and maintaining context across multi-tiered call sequences

---

## 3. Retell AI

### Q1: GHL Documentation
❌ **No Native** - Requires middleware
- Integration via Make.com or n8n
- API documentation available
- Custom integration required

### Q2: Custom Conversation Evaluations
✅ **Yes** - Full customization
- API-based evaluation framework
- Custom analysis criteria
- Multiple LLM options for analysis

### Q3: CRM Data Extraction
✅ **Yes** - Through API
- Fully customizable data extraction
- Real-time data flow via webhooks
- Complete control over data mapping

### Q4: Real-time SMS Support
✅ **Yes** - Via API integration
- Can trigger any external API
- Real-time action execution
- Full programmable control

### Q5: Webhook Integrations
✅ **Yes** - Extensive webhook support
- Custom webhook endpoints
- Real-time event streaming
- Complete API control

### Q6: API Provisioning
✅ **Yes** - Full API support
- Complete programmatic control
- Batch provisioning supported
- Infrastructure as code friendly

### Q7: Lead Qualification Analysis
✅ **Yes** - Customizable analysis
- Multiple LLM options for scoring
- Custom qualification logic
- API-based scoring system

### Q8: Failure Alerting
✅ **Yes** - Enterprise-grade monitoring
- 99.99% uptime guarantee
- Real-time alerting via API
- Custom alert routing

### Q9: Concurrent Call Limits
- **Pay-as-you-go**: 20 base concurrent calls
- **Additional**: $8 per concurrent call
- **Enterprise**: Unlimited concurrent calls
- No platform-imposed limits

### Q10: Agent Switching/Routing
✅ **Yes** - Full programmable control
- Dynamic agent switching via API
- Custom routing logic
- Real-time decision making

### Q11: Conversation Threading
✅ **Yes** - Advanced API-based state management
- **Agent Transfer with Context**: Seamless switching between agents with full context inheritance
- **State Tracking**: Tracks conversation flow transitions through each node
- **API Integration**: Real-time data exchange and context sync with backend systems
- **Model Context Protocol (MCP)**: Supports any HTTP-based service for dynamic context
- **Warm Transfer**: Built-in capabilities for human handoffs with full context
- **CRM Syncing**: Real-time synchronization with ticketing and service management systems
- **Modular Agents**: Reusable agents for specific tasks (language routing, CSAT, payments)
- **Persistent Logic**: Maintains context for aged leads and follow-up sequences

---

## Summary Comparison

| Feature | Synthflow | SimpleTalk.ai | Retell AI |
|---------|-----------|---------------|-----------|
| **GHL Native Integration** | ✅ Excellent | ⚠️ Advertised | ❌ API Only |
| **Custom Evaluations** | ⚠️ Limited | ✅ Yes | ✅ Full |
| **CRM Data Extraction** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Real-time SMS** | ✅ Via GHL | ✅ Yes | ✅ Via API |
| **Webhooks** | ✅ Yes | ✅ Yes | ✅ Extensive |
| **API Provisioning** | ❌ No | ⚠️ Unknown | ✅ Yes |
| **Lead Qualification** | ✅ Yes | ✅ Yes | ✅ Custom |
| **Failure Alerts** | ⚠️ Basic | ⚠️ Unknown | ✅ Enterprise |
| **Max Concurrent Calls** | 100 | 1,800/min | Unlimited |
| **Agent Switching** | ⚠️ Partial | ✅ Yes | ✅ Full |
| **Conversation Threading** | ✅ Via GHL | ✅ Yes | ✅ Custom |

## Technical Recommendations

### Choose Synthflow if:
- You need native GHL integration without technical complexity
- Your team lacks development resources
- You want quick deployment (< 21 days)
- 100 concurrent calls is sufficient

### Choose SimpleTalk.ai if:
- You need maximum call volume (1,800/minute)
- Multi-language support is critical
- You can work with limited documentation
- High-volume calling is your primary need

### Choose Retell AI if:
- You have strong technical resources
- You need complete customization control
- API provisioning is required
- You want unlimited concurrent calls
- Lowest per-minute cost is priority

## Critical Technical Gaps

### Synthflow Gaps:
- No API provisioning
- Limited custom evaluations
- 100 concurrent call ceiling

### SimpleTalk.ai Gaps:
- Poor documentation
- Unknown API provisioning status
- Unclear failure alerting

### Retell AI Gaps:
- No native GHL integration
- Requires development expertise
- Longer implementation timeline

## Conversation Threading Deep Dive

### Threading Architecture Comparison

| Aspect | Synthflow | SimpleTalk.ai | Retell AI |
|--------|-----------|---------------|-----------|
| **Threading Type** | CRM-dependent | Native persistent | API-based state |
| **Context Storage** | GHL custom fields | Platform native | Flexible (API/CRM) |
| **Multi-Agent Support** | Sequential stages | Unified memory | Modular with transfer |
| **Cross-Channel** | Via GHL workflows | Native multi-channel | API integration |
| **Context Inheritance** | Field matching | Automatic | Full transfer support |
| **History Access** | GHL database | Built-in transcripts | API accessible |

### Key Threading Insights

**Synthflow**:
- Relies heavily on GoHighLevel for context persistence
- Uses custom fields as the primary threading mechanism
- Best for businesses already using GHL as their primary CRM
- Limited native threading without GHL

**SimpleTalk.ai**:
- Most robust native threading with "Persistent Context" feature
- Automatically maintains conversation memory across all interactions
- 95% accuracy in context detection and maintenance
- Best for businesses wanting out-of-the-box threading

**Retell AI**:
- Most flexible and sophisticated threading via API
- Supports complex agent transfers with full context
- Can track conversation state through flow nodes
- Best for custom implementations and complex workflows

### Threading Use Case Recommendations

**For Simple Linear Conversations**: Synthflow (if using GHL)
**For Multi-Channel Continuity**: SimpleTalk.ai
**For Complex Agent Handoffs**: Retell AI

## Next Steps for Evaluation

1. **Synthflow**: Start 14-day free trial to test GHL integration
2. **SimpleTalk.ai**: Request technical documentation and demo
3. **Retell AI**: Evaluate development resources needed for integration

## Integration Effort Comparison

- **Synthflow**: 1-3 weeks (no-code setup)
- **SimpleTalk.ai**: 2-4 weeks (limited docs)
- **Retell AI**: 2-6 weeks (custom development)

---

## Research Resources & Documentation Links

### Synthflow Resources
- **Official Website**: [https://synthflow.ai/](https://synthflow.ai/)
- **GoHighLevel Integration Docs**: [https://docs.synthflow.ai/gohighlevel](https://docs.synthflow.ai/gohighlevel)
- **GHL Snapshot Setup**: [https://docs.synthflow.ai/docs/gohighlevel-snapshots-synthflow](https://docs.synthflow.ai/docs/gohighlevel-snapshots-synthflow)
- **Real-time Voice Assistant**: [https://help.synthflow.ai/fine-tuner.ai/real-time-voice-assistant-beta/gohighlevel-integration](https://help.synthflow.ai/fine-tuner.ai/real-time-voice-assistant-beta/gohighlevel-integration)
- **Outbound Call Setup**: [https://docs.synthflow.ai/docs/setup-an-outbound-call-gohighlevel](https://docs.synthflow.ai/docs/setup-an-outbound-call-gohighlevel)
- **GHL Connection Guide**: [https://docs.synthflow.ai/docs/integrate-with-gohighlevel](https://docs.synthflow.ai/docs/integrate-with-gohighlevel)

### SimpleTalk.ai Resources
- **Official Website**: [https://www.simpletalk.ai/](https://www.simpletalk.ai/)
- **Technical Overview**: [https://docs.simpletalk.ai/reference/simpletalk-tech-overview](https://docs.simpletalk.ai/reference/simpletalk-tech-overview)
- **Features Page**: [https://www.simpletalk.ai/features](https://www.simpletalk.ai/features)
- **CRM Integration Docs**: [https://docs.simpletalk.ai/reference/crm-integration](https://docs.simpletalk.ai/reference/crm-integration)
- **GHL Launch Guide**: [https://docs.simpletalk.ai/docs/how-to-launch-calls-from-ghl](https://docs.simpletalk.ai/docs/how-to-launch-calls-from-ghl)
- **Press Release (Aug 2025)**: [SimpleTalk Custom AI Sales System](https://www.globenewswire.com/news-release/2025/08/20/3136148/0/en/SimpleTalk-Introduces-Custom-AI-Sales-System-for-U-S-Businesses-Seeking-Automation-Efficiency.html)

### Retell AI Resources
- **Official Website**: [https://www.retellai.com/](https://www.retellai.com/)
- **Documentation Hub**: [https://docs.retellai.com/general/introduction](https://docs.retellai.com/general/introduction)
- **API Integration Guide**: [https://www.retellai.com/glossary/api-integration](https://www.retellai.com/glossary/api-integration)
- **Voice API Blog**: [https://www.retellai.com/blog/how-to-integrate-phone-ai-agents-with-your-existing-api-systems](https://www.retellai.com/blog/how-to-integrate-phone-ai-agents-with-your-existing-api-systems)
- **Platform Changelogs**: [https://www.retellai.com/changelog](https://www.retellai.com/changelog)
- **B2B Guide to AI Phone Calls**: [https://www.retellai.com/blog/b2b-guide-to-ai-phone-calls](https://www.retellai.com/blog/b2b-guide-to-ai-phone-calls)
- **Inside Retell AI**: [https://www.retellai.com/blog/inside-retell-ai-conversational-ai-phone-system](https://www.retellai.com/blog/inside-retell-ai-conversational-ai-phone-system)
- **Y Combinator Profile**: [https://www.ycombinator.com/companies/retell-ai](https://www.ycombinator.com/companies/retell-ai)
- **OpenAI Case Study**: [https://openai.com/index/retell-ai/](https://openai.com/index/retell-ai/)

### GoHighLevel Voice AI Resources
- **Setting Up Conversation AI**: [https://help.gohighlevel.com/support/solutions/articles/155000004401-setting-up-conversation-ai](https://help.gohighlevel.com/support/solutions/articles/155000004401-setting-up-conversation-ai)
- **AI Tools in HighLevel**: [https://help.gohighlevel.com/support/solutions/articles/155000002166-ai-tools-in-highlevel](https://help.gohighlevel.com/support/solutions/articles/155000002166-ai-tools-in-highlevel)
- **Multiple Messages in Workflows**: [https://help.gohighlevel.com/support/solutions/articles/155000003207-conversation-ai-multiple-messages-in-one-workflow-action](https://help.gohighlevel.com/support/solutions/articles/155000003207-conversation-ai-multiple-messages-in-one-workflow-action)
- **Voice AI Course (Coursera)**: [https://www.coursera.org/projects/rudi-hinds-gohighlevel-for-beginners-voice-ai-automated-appointments](https://www.coursera.org/projects/rudi-hinds-gohighlevel-for-beginners-voice-ai-automated-appointments)

### Additional Industry Resources
- **JustCall AI**: Contact sales for documentation
- **Autocalls.ai**: [https://autocalls.ai/](https://autocalls.ai/) (Euro-based platform)
- **Air AI**: ⚠️ Under FTC investigation - avoid
- **Bland AI**: [https://bland.ai/](https://bland.ai/) (No cold calling allowed)

### Community & Discussion
- **Hacker News - Retell AI Launch**: [https://news.ycombinator.com/item?id=39453402](https://news.ycombinator.com/item?id=39453402)
- **HubSpot Community - SimpleTalk Integration**: [https://community.hubspot.com/t5/HubSpot-Ideas/App-integration-to-Simpletalk-ai/idi-p/1080136](https://community.hubspot.com/t5/HubSpot-Ideas/App-integration-to-Simpletalk-ai/idi-p/1080136)