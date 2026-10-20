---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#01-what-requests-use-cors.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-01-what-requests-use-cors
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › What requests use CORS?
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#01-what-requests-use-cors
source_hash: 33dfac117cc691aac49fae4d12f02ed1cc2d77715bb33c8e37c8b9380e9832f0
---
This [cross-origin sharing standard](https://fetch.spec.whatwg.org/#http-cors-protocol "External link (opens in new tab)") can enable cross-origin HTTP requests for:

- Invocations of `fetch()` or `XMLHttpRequest`, as discussed above.
- Web Fonts (for cross-domain font usage in `@font-face` within CSS), as described in the [font fetching requirements](https://drafts.csswg.org/css-fonts/#font-fetching-requirements "External link (opens in new tab)"), so that servers can deploy TrueType fonts that can only be loaded cross-origin and used by websites that are permitted to do so.
- [WebGL textures](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Using_textures_in_WebGL).
- Images/video frames drawn to a canvas using [`drawImage()`](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/drawImage "drawImage()").
- [CSS Shapes from images.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_images)

This is a general article about Cross-Origin Resource Sharing and includes a discussion of the necessary HTTP headers.

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
