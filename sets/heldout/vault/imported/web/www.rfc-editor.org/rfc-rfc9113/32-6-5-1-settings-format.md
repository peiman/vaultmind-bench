---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#32-6-5-1-settings-format.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-32-6-5-1-settings-format
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.5. SETTINGS › 6.5.1. SETTINGS Format'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#32-6-5-1-settings-format
source_hash: 21070ffd04cf36579575d291a1550df73189affaeb29b9f125496942a98137f2
---
The frame payload of a SETTINGS frame consists of zero or more settings, each consisting of an unsigned 16-bit setting identifier and an unsigned 32-bit value.[¶](#section-6.5.1-1)

```
SETTINGS Frame {
  Length (24),
  Type (8) = 0x04,

  Unused Flags (7),
  ACK Flag (1),

  Reserved (1),
  Stream Identifier (31) = 0,

  Setting (48) ...,
}

Setting {
  Identifier (16),
  Value (32),
}
```

[Figure 7](#figure-7): [SETTINGS Frame Format](#name-settings-frame-format)

The Length, Type, Unused Flag(s), Reserved, and Stream Identifier fields are described in [Section 4](#FramingLayer). The frame payload of a SETTINGS frame contains any number of Setting fields, each of which consists of:[¶](#section-6.5.1-3)

Identifier:

A 16-bit setting identifier; see [Section 6.5.2](#SettingValues).[¶](#section-6.5.1-4.2)

Value:

A 32-bit value for the setting.[¶](#section-6.5.1-4.4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
