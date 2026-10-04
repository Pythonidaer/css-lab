# CSS Lab

An independent, buildless CSS property reference and playground.

https://pythonidaer.github.io/css-lab/

## Catalog

- 901 unique catalog entries across 27 categories.
- All 731 distinct names extracted from the downloaded W3C property table.
- 170 additional MDN names, including vendor-specific and legacy entries.
- The W3C page reports 732 although its downloaded table contains 731 unique names. The site explicitly discloses this difference.
- Every entry has a property value grammar; 398 named value grammars support recursive exploration.
- Custom properties are represented by `--*` and demonstrated as `--lab-color`.

Value sets are open-ended. Keywords, formal grammars, unit families, and representative samples are provided, together with arbitrary value input. The site does not claim to list every numerical value, name, URL, calculation, or combination.

## Browser support

`CSS.supports(property, "inherit")` checks whether a property name is recognized. Each entered value is checked with `CSS.supports(property, value)`. Syntax acceptance does not guarantee rendering, interoperability, complete implementation, or an observable effect in a particular context. Print and speech contexts are labeled separately.

Thirteen reusable example contexts demonstrate common properties. Users can edit the example HTML and supporting CSS to supply more specialized prerequisites. Preview documents are isolated in a sandboxed iframe with scripts disabled. Motion is paused until explicitly played.

## Files

`dist/index.html`, `dist/style.css`, `dist/app.js`, and `dist/data.js` form the complete static site. No installation or build is needed.

`collected.json` is the authoritative bundled reference snapshot. `build-data.py` regenerates `dist/data.js` from it. `w3-index.json` preserves all extracted W3C property references.

## Attribution

Sources: W3C CSS property index and linked specification definitions; MDN CSS data (CC0); adapted MDN content (CC BY-SA 2.5). Each property retains its authoritative source links. Source collection date: October 4, 2026 UTC.

## Verification

JavaScript syntax checks; browser checks for navigation, search, invalid values, unsupported properties, reset, catalog dialog, mobile overflow, and visible effects for border-radius, font-size, grid-template-columns, fill, and opacity.

## Future improvements

The next pass is a full run-through, not a visual redesign yet.

- Test each category for property values that do not work, then check that each property value works.
- Identify missing values and syntax for each property.
- Make sure every property and value can be tried in at least one example context.
- Decide whether new example contexts are needed, and whether each property can open on the correct context.
- Add example controls where one text field is not enough, such as radio choices.
- Find properties missing from a category or filed in the wrong one. Tables currently lists 3 properties and leaves out `border-collapse`; look for more gaps, and for clearer ways to present that information.
- Explain each property in the context of the HTML it applies to.
- Consider an HTML tab that shows the CSS declaration inside the example, and whether Example HTML should move there.
- Simplify the presentation in a Feynman style: shorter and clearer, without dropping the understanding that matters.

Many properties belong to more than one topic. Flexbox, tables, and the other categories can each be missing a property that only shows up when it is filed there, or that only has an effect with a particular HTML structure and with other CSS set alongside it. Whether a value works also depends on the browser. Those conditions multiply, so later passes should test the important crossings rather than every possible pairing. The items above are the start of that work.
