# Access Control

This page explains how XAUTOMATA controls what each user can see and do in the platform.
Permissions are configured directly on user records through the interface, and can be refined with ACL Override profiles.

---

## How Permissions Work

Every user has an **ACL configuration** — a set of permission scopes that define which operations they can perform in which areas of the platform.

When a user tries to perform an action (open a page, create a record, delete an entity), the platform checks their ACL configuration. If the required permission is not present, the action is blocked or the relevant controls are hidden from the interface.

---

## Permission Domains and Operations

Permissions are organized into three **domains**, each covering a different area of the platform:

| Domain | What it covers |
|---|---|
| **Main** | Core entities — customers, objects, metrics, services, and most Data Manager sections |
| **Tracking** | Calendars, downtimes, and dispatchers |
| **Admin** | Administration section — users, probes, notification providers, and platform settings |

Within each domain, you can grant the following operations:

| Operation | Effect |
|---|---|
| **Read** | The user can view and search records |
| **Create** | The user can create new records |
| **Update** | The user can edit existing records |
| **Delete** | The user can delete records |

The **Admin** domain also includes a special operation:

| Operation | Effect |
|---|---|
| **Super** | Full administrative access — grants all permissions across all domains |

---

## Configuring Permissions on a User

Permissions are set directly in the user's CRUD dialog.

1. Go to **Administration → Users**.
2. Open the user record using the **search icon (🔍)**.
3. In the dialog, locate the **ACL** configuration section.
4. Enable or disable the permission scopes as needed.
5. Click **SAVE CHANGES**.

The interface presents the available scopes as toggles or checkboxes grouped by domain and operation. You do not need to type scope strings manually.

!!! note
    A user with no permissions granted will be able to log in but will see an empty interface with no accessible sections.
    Always configure at minimum **Main → Read** for standard operator accounts.

---

## User Types

The platform recognizes three administrative levels, defined by the permissions assigned:

| Type | Permissions | Typical use |
|---|---|---|
| **Operator** | Main read (and optionally tracking read/update) | Daily monitoring and analysis |
| **Tenant Admin** | Admin domain (partial) — `admin.customer` scope | Customer-scoped administration |
| **Super Admin / Super User** | `admin.super` — all domains, all operations | Full platform administration |

---

## ACL Overrides

In addition to the base domain permissions, a user can be assigned an **ACL Override** profile.

An override is a reusable configuration that applies additional, more specific rules on top of the user's base permissions. It can:

- restrict specific operations for individual sections (e.g. disable delete on objects)
- make specific form fields read-only or hidden
- apply default values to certain fields automatically

### How overrides work with base permissions

The platform evaluates permissions in this order:

1. Check if an ACL override is assigned to the user for the requested endpoint.
2. If yes — apply the override rules. The base permissions are superseded for that endpoint.
3. If no — apply the base domain permissions.

This means an override can both **restrict** a permission the user would otherwise have, and (in theory) **grant** access to specific endpoints even if the base permissions would not allow it.

### Assigning an override to a user

1. Go to **Administration → Users**.
2. Open the user record using the **search icon (🔍)**.
3. In the **ACL Override** field, select the override profile to apply.
4. Click **SAVE CHANGES**.

Override profiles are created and managed in **Super Admin → ACL Overrides**.

### Field-level restrictions

Overrides can also restrict individual fields within a form, independently of operation-level permissions.

| Restriction | Effect in the interface |
|---|---|
| `disabled` | The field is visible but cannot be edited |
| `hidden` | The field is not shown in the form |
| `default` | A default value is applied automatically |

This allows administrators to prevent modification of sensitive fields (for example the `name` of an object) even for users who have general update permissions.

---

## Practical Examples

**Standard operator** — can browse monitoring data but cannot modify infrastructure configuration:
- Main: read
- Tracking: read

**Operations team member** — can also manage downtimes and dispatchers:
- Main: read
- Tracking: read, create, update, delete

**Customer administrator** — can manage their own environment:
- Main: read, create, update, delete
- Tracking: read, create, update, delete
- Admin: read, update (with `admin.customer` scope)

**Read-only user with field restrictions** — standard read permissions plus an ACL override that hides sensitive configuration fields from all forms.

---

!!! note
    ACL Override profiles are managed in **Super Admin → ACL Overrides**, which is accessible only to Super Admin users.
    See [Users](users.md) for the full user management workflow.
