# Administration Overview

The **Administration** section provides the tools to configure and manage the platform itself — user access, monitoring agents, notification channels, and security policies.

While the **Data Manager** focuses on what is monitored, the Administration section focuses on **who can access the platform** and **how the platform communicates with the outside world**.

---

## What You Can Do Here

| Area | Purpose |
|---|---|
| [Users](users.md) | Create and manage user accounts, configure permissions |
| [Access Control](access_control.md) | Understand and configure the ACL permission model |
| [Virtual Domains](virtual_domains.md) | Organize users, groups, and probes into logical scopes |
| [Probes](probes.md) | Manage monitoring agents and diagnose collection issues |
| [Probe Types](probe_types.md) | View the available monitoring integration types |
| [Messages](messages.md) | Configure notification content templates |
| [Notification Providers](notification_providers.md) | Configure external delivery channels (email, webhook, ticketing) |
| [Notification Provider Types](notification_provider_types.md) | View the available notification integration types |

---

## Two Main Responsibilities

### Access management

User accounts control who can log into the platform and what they can see and do.
Permissions are configured through the **ACL model** directly on each user record.
For environments requiring fine-grained control, **ACL Override** profiles (managed in Super Admin) can restrict specific operations or fields for groups of users.

See [Users](users.md) and [Access Control](access_control.md).

### Notification and automation delivery

When a monitoring event triggers a Dispatcher, the platform needs to know what to send and where to send it.

- **Messages** define the notification content templates.
- **Notification Providers** define the delivery channels.
- **Notification Provider Types** define the available integration models.

These three entities work together as the outbound communication layer of the platform.

See [Messages](messages.md), [Notification Providers](notification_providers.md), and [Dispatchers](../tracking/dispatchers.md).

---

!!! note
    Probes and Probe Types are also managed here, but are typically configured during onboarding by the XAUTOMATA delivery team.
    The Administration section is mainly used day-to-day for user and notification management.
