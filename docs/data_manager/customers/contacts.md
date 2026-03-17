# Contacts
# Contacts

The **Contacts** section manages the people associated with customers and sites monitored by XAUTOMATA.
Use it to maintain a directory of technical, operational, and administrative contacts for each organization.

---

## Opening the Contacts Section

From the main navigation menu, go to **Customers → Client Repository → Contacts**.

The interface opens with a **pre-filter dialog**. Fill in one or more fields to narrow the search, then click **APPLY**.

| Filter field | Description |
|---|---|
| Name | First or last name of the contact |
| Surname | Last name |
| Company | Organization the contact belongs to |
| Email | Primary or secondary email address |
| Status | Active or Disabled |

Leave all fields empty and click **APPLY** to load all available contacts.

![Contacts pre-filter](../images/data_manager/contacts/contacts_prefilter.png)
/// caption
Fig.1 - Contacts pre-filter dialog (screenshot pending)
///

---

## Contacts Table

After applying the filter, the results appear in a table where each row represents a contact.

Typical columns include:

- Name and Surname
- Company
- Email
- Phone
- Status

![Contacts table](../images/data_manager/contacts/contacts_table.png)
/// caption
Fig.2 - Contacts results table (screenshot pending)
///

---

## Contact Details

Click the **search icon (🔍)** on any row to open the contact record.

The CRUD dialog displays the full set of information for the contact:

| Field | Description |
|---|---|
| Name | First name |
| Surname | Last name |
| Qualification | Role or job title |
| Company | Organization |
| Department | Internal department or team |
| Email | Primary email address |
| Email 2 | Secondary email address |
| Mobile | Mobile phone number |
| Phone | Office phone number |
| Status | Active or Disabled |
| Notes | Optional notes |

From this dialog you can:

- edit the contact information
- duplicate the record
- delete the record

![Contact detail dialog](../images/data_manager/contacts/contacts_crud.png)
/// caption
Fig.3 - Contact detail dialog (screenshot pending)
///

---

## Creating a New Contact

To add a new contact, click **NEW** in the top-right area of the contacts table.

Fill in the fields in the CRUD dialog, then click **SAVE CHANGES**.

!!! note
    At minimum, fill in **Name**, **Surname**, and **Status**.
    Email and phone fields are optional but recommended to make the contact useful for operational purposes.

---

## Connections View

Click the **link icon (🔗)** on any row to open the **Connections View** for that contact.

This view shows the entities the contact is linked to, organized in tabs:

| Tab | Description |
|---|---|
| Customers | Organizations this contact is associated with |
| Sites | Sites this contact is responsible for |

![Contact connections view](../images/data_manager/contacts/contacts_connections.png)
/// caption
Fig.4 - Contact connections view (screenshot pending)
///

### Linking a contact to a customer or site

1. Open the **Connections View** for the contact.
2. Select the **Customers** or **Sites** tab.
3. Click **ADD** to create a new link.
4. Select the target entity from the list.
5. Specify the **relationship type** to describe the contact's role (for example: Technical Manager, Service Contact, Escalation Contact).
6. Click **SAVE CHANGES**.

### Removing a link

To remove an existing association, select the row in the connections tab and click **DELETE**.

!!! warning
    Removing a link does not delete the contact record — it only removes the association with that customer or site.

---

!!! note
    Contacts can also be linked from the customer or site side.
    See [Customers](customers.md) and [Sites](sites.md) for details.
