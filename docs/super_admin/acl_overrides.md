# ACL Overrides

The **ACL Overrides** section manages reusable permission profiles that can be applied to users to restrict or modify their default access behavior.

An ACL override defines endpoint-specific rules that take precedence over a user's base permissions — restricting operations, hiding fields, or applying default values on specific sections of the platform.

!!! warning
    This section is reserved for **Super Admin** users. ACL overrides affect the interface experience and available actions for all users they are assigned to.

---

## Opening the section

From the main navigation menu, go to **Administration → Super Admin → ACL Overrides**.

The interface opens with a table listing all defined override profiles.

| Column | Description |
|---|---|
| Code | Unique identifier of the override profile |

---

## Override details

Click the **search icon (🔍)** on any row to open the override record.

| Field | Description |
|---|---|
| Code | Unique identifier of the profile |
| Override Rules | JSON configuration defining the permission rules |

The **Override Rules** field contains the actual permission configuration as a JSON structure. Each key in the JSON targets a specific API endpoint, and the associated values define the permissions and field restrictions for that endpoint.

### Override Rules structure

```json
{
  "/objects/": {
    "acl": {
      "read": true,
      "create": false,
      "delete": false,
      "update": true
    },
    "fields": [
      {
        "key": "name",
        "editable": false
      },
      {
        "key": "description",
        "editable": false
      }
    ]
  }
}
```

In this example, for the `/objects/` endpoint:
- read and update are allowed
- create and delete are disabled
- the `name` and `description` fields are visible but not editable

### Field-level restrictions

| Restriction | Effect in the interface |
|---|---|
| `editable: false` | Field is visible but cannot be modified |
| `hidden: true` | Field is not displayed in the form |
| `default` | A default value is applied automatically |

---

## Connections View

Click the **link icon (🔗)** on any row to open the Connections View.

| Tab | Description |
|---|---|
| Users | Users this override profile is currently assigned to |

Use this tab to see which users are affected by the selected override, or to assign it to additional users.

!!! note
    An override profile can also be assigned directly from the user record.
    See the **ACL Override** field in [Users](../administration/users.md).

---

## How overrides interact with base permissions

When a user tries to perform an action, the platform evaluates permissions in this order:

1. Check if an ACL override is assigned to the user for the requested endpoint.
2. If yes — apply the override rules. The user's base permissions are superseded for that endpoint.
3. If no — apply the user's base domain permissions.

This means an override can restrict access the user would otherwise have based on their domain permissions alone.

For the full permission model, see [Access Control](../administration/access_control.md).
