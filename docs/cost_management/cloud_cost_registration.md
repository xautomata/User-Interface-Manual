# Cloud Cost Registration
# Cloud Cost Registration

The **Cloud Cost Registration** section is where administrators configure the connections between XAUTOMATA and supported cloud providers.
Once configured, the platform periodically retrieves billing data from the provider APIs and makes it available for analysis in dashboards and widgets.

!!! info
    Cloud Cost Registration is typically set up during onboarding by the XAUTOMATA delivery team.
    This section is primarily used to review existing configurations or add new provider accounts.

---

## Supported providers

| Provider | Notes |
|---|---|
| **Azure CSP** | Azure Cloud Solution Provider accounts |
| **Azure** | Standard Azure subscriptions |
| **AWS** | Amazon Web Services accounts |
| **Google Cloud** | Google Cloud Platform billing accounts |

---

## Opening the section

From the main navigation menu, go to **Administration → Cloud Cost Registration**.

The interface opens with a table listing the configured provider registrations.

![Cloud Cost Registration table](../images/cost_management/cloud_cost_registration/registration_table.png)
/// caption
Fig.1 - Cloud Cost Registration table (screenshot pending)
///

---

## Registration details

Click the **search icon (🔍)** on any row to open the registration record.

The fields displayed depend on the provider type. Typical fields include:

| Field | Description |
|---|---|
| Name | Identifier for this registration |
| Provider | Cloud provider type (Azure CSP, Azure, AWS, Google Cloud) |
| Customer | Customer the billing data is associated with |
| Credentials / Token | Authentication details for the provider API |
| Status | Active or Disabled |

!!! warning
    Credential fields contain sensitive information. Only administrators with appropriate permissions should access or modify these records.

---

## What happens after registration

Once a provider is registered and active, XAUTOMATA:

1. Connects to the provider API using the configured credentials.
2. Retrieves the available billing data for the associated subscription or account.
3. Stores the raw cost data in the platform.

The imported data is then available in:

- the **Cloud Cost dashboard** — for direct analysis of raw billing data
- the **Cloud Cost widgets** — trends, breakdowns, forecasts, and anomalies
- the **Analytical Accounting widgets** — when costs are organized through [Cost Views](cost_views.md)

---

!!! note
    Raw billing data reflects the provider's own structure — subscriptions, resource groups, categories, locations.
    To reorganize costs according to your internal accounting model, see [Cost Views](cost_views.md).
