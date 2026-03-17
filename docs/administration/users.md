# Users

The **Users** section manages the accounts that can access the XAUTOMATA platform.
Each user account defines authentication credentials, contact information, access permissions, and relationships with dashboards and infrastructure entities.

---

## Opening the Users Section

From the main navigation menu, go to **Administration → Users**.

The interface opens with a **pre-filter dialog**. Fill in one or more fields to narrow the search, then click **APPLY**.

| Filter field | Description |
|---|---|
| User | Username identifier |
| Email | User email address |
| Phone | Contact phone number |
| Email Status | Verified or Not verified |
| Status | Active or Disabled |
| ACL Override | Optional override profile applied to the user |

![Users pre-filter](../images/administration/users/users_prefilter.png)
/// caption
Fig.1 - Users pre-filter dialog (screenshot pending)
///

---

## Users Table

After applying the filter, the results appear in a table where each row represents a user account.

Typical columns include:

- User
- Email
- Phone
- Status

![Users table](../images/administration/users/users_table.png)
/// caption
Fig.2 - Users results table (screenshot pending)
///

---

## Creating a User

Click **NEW** to create a new user account. Fill in the fields in the dialog, then click **SAVE CHANGES**.

| Field | Description |
|---|---|
| User | Unique username for login |
| Email | User email address |
| Password | Initial password |
| Phone | Optional phone number |
| Email Status | Verified or Not verified |
| Status | Active or Disabled |

After creating the user, configure their **ACL permissions** (see below) and assign the relevant connections.

---

## User Details

Click the **search icon (🔍)** on any row to open the user record.

From this dialog you can:

- update contact information
- enable or disable the account
- modify ACL permissions
- change the password by enabling the **Edit password** option

The dialog also shows **Last change** — the timestamp of the last password modification.

![User detail dialog](../images/administration/users/users_crud.png)
/// caption
Fig.3 - User detail dialog (screenshot pending)
///

---

## Access Control (ACL)

Each user is assigned an **ACL configuration** that determines which actions they can perform in the platform.

Permissions are organized into three domains:

| Domain | Description |
|---|---|
| Main | Core platform entities and general operations |
| Tracking | Monitoring and tracking resources |
| Admin | Administrative configuration and management |

Within each domain, the following operations can be granted: **read**, **create**, **update**, **delete**.
The **Admin** domain also includes the special **super** operation, which grants full administrative access.

### ACL Overrides

In addition to the base permissions, a user can be assigned an **ACL Override** profile.
An override can restrict specific operations, hide form fields, or apply default values — without changing the user's base permission configuration.

ACL Overrides are managed in **Super Admin → ACL Overrides**.
For a full description of the permission model, see [Access Control](access_control.md).

---

## Connections View

Click the **link icon (🔗)** on any row to open the **Connections View** for that user.

This view shows the entities linked to the user:

| Tab | Description |
|---|---|
| Dashboards | Dashboards this user can access |
| Groups | Infrastructure groups scoped to this user |
| Virtual Domains | Administrative domains this user belongs to |
| Customers | Customers this user has access to |
| Widget Groups | Widget groups available to this user |

Use this view to control what data and dashboards a user can see after login.

!!! warning
    A user with no connections may see an empty interface after login.
    Always assign at least one dashboard and the relevant customers or groups.

![User connections view](../images/administration/users/users_connections.png)
/// caption
Fig.4 - User connections view (screenshot pending)
///

---

!!! note
    For the full description of the permission model and ACL evaluation logic, see [Access Control](access_control.md).
