This module removes the Odoo branding from the "Connect with your
software" dialog of the purchase order page of the vendor portal, the
counterpart of `sale_portal_debranding` (in 20.0 the sale portal no longer
has this dialog).

Specifically, it:

- removes the instructions to import the document in Odoo;
- keeps the REST URL of the document in UBL format, with a generic title
  and without the links to the Odoo documentation;
- removes the section suggesting to "Start on Odoo".
