# Users

The **Users** section allows administrators to manage accounts that can access the XAUTOMATA platform.

Users represent individual operators who can log into the system and interact with dashboards, monitoring data, and administrative features.

User accounts define:

- authentication credentials
- contact information
- access permissions
- relationships with platform entities such as dashboards or groups

---

## Accessing the Users Section

Users are managed from:

```

Administration → Users

```

The page opens with a **pre-filter dialog** that allows administrators to limit the set of users displayed in the table.

---

## User Filters

The filter dialog includes the following fields:

| Field | Description |
|------|-------------|
| User | Username identifier |
| Email | User email address |
| Phone | Contact phone number |
| Email status | Indicates whether the user has verified their email address |
| Status | User account state (Active or Disabled) |
| ACL override | Optional override profile applied to the user |

Possible values include:

- **Email status**
  - Verified
  - Not verified

- **Status**
  - Active
  - Disabled

Filters allow administrators to quickly locate specific accounts in large environments.

---

## Users Table

After applying filters, the system displays a table of users.

Typical columns include:

| Column | Description |
|------|-------------|
| User | Unique identifier of the account |
| Email | User email address |
| Phone | Phone contact |
| Status | Indicates whether the account is active |

Each row provides quick access to two actions:

- **Connections view** (left icon) – opens the relationships of the user with other entities
- **Search / View** (magnifier icon) – opens the user record in a CRUD dialog

---

## Creating a User

To create a new account, click the **Add (+)** button in the page toolbar.

The creation dialog includes fields such as:

| Field | Description |
|------|-------------|
| User | Unique username |
| Email | User email address |
| Password | Initial password |
| Phone | Optional phone number |
| Email status | Whether the email is verified |
| Status | Active or disabled account |

When creating a user, administrators must also configure the user's **ACL permissions**.

---

## Editing a User

Opening a user record displays the **User Details dialog**.

The dialog allows administrators to:

- update contact information
- enable or disable the account
- modify access permissions
- optionally change the user's password

When editing a user, an additional option appears:

```

Edit password

```

If enabled, the administrator can update the password.

The dialog also displays:

- **Last change** – timestamp of the last password modification.

---

## Access Control (ACL)

Each user is assigned an **ACL configuration** that defines the permissions available within the platform.

ACL permissions are organized into logical domains such as:

- Main
- Tracking
- Admin

Within each domain, permissions typically include:

- read
- create
- update
- delete

A user may also have an **ACL override**, which applies a predefined permission profile.

The detailed access control model is described in the **Access Control** section of this documentation.

---

## User Connections

Users can be associated with several platform entities.

The **Connections View** allows administrators to manage these relationships.

Available connections include:

- Dashboards
- Groups
- Virtual Domains
- Customers
- Widget Groups

These relationships determine what data and dashboards a user can access.

For example:

- assigning dashboards defines what the user can see
- linking groups or customers restricts the scope of monitored infrastructure
- assigning widget groups controls available visual components

---

## Security Considerations

User accounts play a critical role in platform security.

Administrators should:

- ensure strong passwords
- regularly review ACL permissions
- disable accounts that are no longer in use
- verify user email addresses

Proper user management helps maintain a secure and controlled monitoring environment.