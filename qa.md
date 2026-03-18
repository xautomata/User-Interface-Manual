# Q&A — Open Questions for Domain Experts

This file tracks questions that emerged during documentation writing and need verification by a domain expert.
Answers will be used to refine the operational manual.

---

## Format

Each entry includes:
- **Context** — which page or topic the question relates to
- **Question** — what needs to be clarified
- **Answer** — filled in after expert review
- **Action** — what changes in the manual once answered

---

## Open Questions

---

### Q1 — Users without customer connections: scope visibility

**Context:** `administration/users.md`, Access Control model

**Question:**
A Super Admin user with no customers linked in the Connections View appears to see **all customers** in the platform — rather than none.
Does the same behavior apply to **Tenant Admin** users with no customer connections?
Is this "no filter = see all" behavior intentional and documented, or is it a known edge case?

**Answer:**
Confirmed. The behavior is **intentional**:
- A user with **no customer connections** is treated as a **Super User** by the backend, which returns `super=true` under the `admin` key. This grants visibility over all customers.
- This applies regardless of admin level — any user (including Tenant Admin profiles) with no customer links gets this visibility automatically.
- The Super User status is **not a toggle** — it is derived automatically from the absence of customer connections. It cannot be set directly in the interface.
- Linking even one customer removes the super visibility and restricts scope to that customer.

**Action:**
- ✅ Updated `access_control.md` — rewrote User Types section with accurate descriptions of Operator, Admin, Tenant Admin, and Super User.
- ✅ Updated `users.md` — added Customer Admin flag description in ACL section; replaced the Connections View warning with accurate Super User behavior explanation.
- ✅ Q1 closed.

---

### Q2 — Origin of Azure resource tags in Cost Views

**Context:** `cost_management/cost_views.md`, Azure Tags cost view type

**Question:**
The Cost Views of type **Azure Tags** reference tags associated with cloud resources.
Where do these tags originate? Are they Azure resource tags defined directly in the Azure portal by the customer, or are they generated/imported by XAUTOMATA during billing data ingestion?
Does the same tag mechanism apply to AWS and Google Cloud, or is it Azure-specific?

**Answer:**
*(pending)*

**Action:**
- Add a note to `cost_views.md` explaining the origin of tags and how customers should manage them in the cloud provider console.

---

### Q3 — Child node resource filtering in Cost Views (Nodes Tree)

**Context:** `cost_management/cost_views.md`, Nodes Tree editor

**Question:**
When adding a child node to a parent node in the Nodes Tree editor (via the 🌿 icon), can the child node only filter among the resources already assigned to the parent node, or can it independently select any resource from the full billing dataset?
Is the resource scope of a child node always a subset of the parent's resources?

**Answer:**
*(pending)*

**Action:**
- Clarify the child node resource scoping behavior in `cost_views.md` (Resources Definition section).
- If child nodes are constrained to parent resources, document this as an important rule when designing the tree structure.

---
