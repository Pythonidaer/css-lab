import json,re,pathlib,html
p=pathlib.Path(__file__).parent;x=json.load(open(p/'collected.json'));w3=x['w3'];mdn=x['mdn'];defs=x['specdefs']
rules=[('Custom properties & cascade',r'^(--|all$)|Cascading|Custom Properties'),('Flexbox',r'^flex|Flexbox|Flexible Box'),('Grid',r'^grid|Grid Layout'),('Alignment & gaps',r'^(align|justify|place|gap$|row-gap|column-gap)|Box Alignment'),('Positioning & anchors',r'^(position|anchor|inset|top$|left$|right$|bottom$|z-index)|Positioned|Anchor Position'),('Size & spacing',r'^(margin|padding|width|height|min-|max-|block-size|inline-size|box-sizing|aspect-ratio)|Box Model|Box Sizing'),('Fonts',r'^font|Fonts'),('Text & inline layout',r'^(text|line-|letter|word|white-space|hyphen|tab-size|vertical-align|initial-letter|ruby)|Text |Inline|Ruby'),('Colors & backgrounds',r'^(background|color$|opacity$)|Color Module|Background'),('Borders & shadows',r'^(border|outline|box-shadow|corner)|Borders'),('Transforms & perspective',r'^(transform|translate|rotate|scale|perspective|backface)|Transforms'),('Animation & transitions',r'^(animation|transition|view-transition)|Animations|Transitions'),('Scroll & overflow',r'^(scroll|overflow|overscroll)|Scroll|Overflow'),('Images & objects',r'^(object|image)|Images'),('Masks, filters & blending',r'^(mask|clip|filter|backdrop|mix-blend|isolation)|Masking|Filter'),('SVG & vector graphics',r'^(fill|stroke|cx$|cy$|r$|rx$|ry$|d$|x$|y$|marker|paint-order|flood|lighting|stop-|vector|shape-rendering|color-interpolation)|SVG'),('Interaction & form controls',r'^(cursor|pointer|user-|touch|resize|appearance|accent|caret|ime|input|nav-)|User Interface|Pointer|UI '),('Writing direction & logical layout',r'^(direction|unicode-bidi|writing-mode)|Writing Modes|Logical'),('Lists & counters',r'^(list|counter)|Lists|Counters'),('Columns & gap decoration',r'^(column|row-rule|rule-)|Multi-column|Gap Decoration'),('Tables',r'^(table|caption|empty-cells)|Tables'),('Printing & fragmentation',r'^(page|break|orphans|widows|marks|bleed|size$)|Paged|Fragmentation|Page '),('Generated content',r'^(content|quotes|string-set)|Generated Content'),('Containment & rendering',r'^(contain|content-visibility|will-change)|Containment'),('Speech & audio',r'^(speak|speech|voice|pitch|volume|azimuth|elevation|pause|cue|play-during|richness|stress)|Speech|Aural'),('Display & flow',r'^(display|float|clear|order|reading-flow)|Display|Exclusions|Flow')]
category_notes={
'Size & spacing':'Compare the highlighted box with the available space. Dimensions and percentages can depend on the containing block; padding and borders interact with box-sizing.',
'Flexbox':'The example is a flex container. Container properties arrange children; flex-grow, flex-shrink, and flex-basis belong on the children.',
'Grid':'The example uses grid. Track sizes belong on the container; grid placement belongs on an item. Change the context if you are testing an item property.',
'Alignment & gaps':'Alignment depends on the layout mode and available free space. Try flex and grid contexts, and compare the main axis with the cross axis.',
'Text & inline layout':'Notice wrapping, spacing, and the baseline. Some text properties affect inline boxes or particular scripts rather than every block of text.',
'Fonts':'Compare the shapes, weight, and width of the letters. Font features require a font that contains them; a missing font falls back to another face.',
'Animation & transitions':'Use Play motion to start the sample keyframes. Transitions need a changing state; edit the supporting CSS to create a hover or focus state. Reduced-motion preferences pause the example initially.',
'Printing & fragmentation':'Printing properties require a paged context. The on-screen preview cannot verify pagination. Use the example CSS in a print stylesheet and check the browser print preview.',
'Speech & audio':'Speech properties target aural rendering and are often unsupported in current browsers. The visual preview does not synthesize speech.',
'SVG & vector graphics':'The declaration is applied to an SVG shape. Many SVG presentation properties have no effect on ordinary HTML boxes.',
'Interaction & form controls':'Hover, focus, select, or interact with the example. Some effects appear only during interaction or on native controls.',
'Scroll & overflow':'Scroll inside the example. Scroll behavior and snapping need overflowing content; some settings also need a matching property on the children.',
'Custom properties & cascade':'Custom properties store values for var(). In this example --lab-color changes the target background. Cascade keywords can reset several values at once.',
}
props=[]
for name in sorted(set(w3)|set(mdn)):
 m=mdn.get(name,{});d=defs.get(name,{})
 plain=re.sub(r'^-(webkit|moz|ms|o)-','',name)
 cat=next((label for label,pat in rules if re.search(pat,plain,re.I)),None)
 corpus=name+' '+ ' '.join(m.get('groups',[]))
 if not cat:cat=next((label for label,pat in rules if re.search(pat,corpus,re.I)),None)
 if not cat:
  corpus+=' '+' '.join(r['spec'] for r in w3.get(name,[]));cat=next((label for label,pat in rules if re.search(pat,corpus,re.I)),'Specialized & experimental')
 description=x['descriptions'].get(name) or d.get('description')
 if not description and plain in mdn and x['descriptions'].get(plain):description=f'{name} is a vendor-prefixed variant related to {plain}. '+x['descriptions'][plain]
 if not description:description=f'{name} is a property in {cat.lower()}. Its declaration controls the behavior defined in the linked specification; availability and effects depend on the rendering context.'
 if name=='--*':description='Custom properties are names you choose beginning with two hyphens. They store values for reuse through var(), inherit by default, and can connect many styles to one shared setting.'
 if name.startswith('grid-') and 'gap' in name:description=description.replace('Its declaration controls the behavior defined in the linked specification; availability and effects depend on the rendering context.','It controls the space between grid tracks. The older grid-gap names are aliases for gap, row-gap, and column-gap.')
 if plain in ['azimuth','elevation','pitch','pitch-range','volume','stress','richness','speech-rate','play-during','speak-header','speak-numeral','speak-punctuation']:
  meaning={'azimuth':'the horizontal direction of a sound','elevation':'the vertical direction of a sound','pitch':'the pitch of a speaking voice','pitch-range':'the variation in a speaking voice’s pitch','volume':'the loudness of speech','stress':'the stress applied to speech','richness':'the richness of a speaking voice','speech-rate':'the speed of speech','play-during':'a background audio resource','speak-header':'when table headers are spoken','speak-numeral':'how numbers are spoken','speak-punctuation':'whether punctuation is spoken'}[plain]
  description=f'{name} controls {meaning} in historical aural CSS. Current visual browsers generally do not implement this output behavior.'
 description=html.unescape(description)
 sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z])',description)
 description=' '.join(sentences[:2])
 syntax=m.get('syntax') or d.get('syntax','')
 props.append({'name':name,'category':cat,'description':description,'syntax':syntax,'specSyntax':d.get('syntax') if d.get('syntax') and d.get('syntax')!=syntax else '', 'initial':m.get('initial',d.get('initial','Not specified in snapshot')),'inherited':m.get('inherited',d.get('inherited',False)),'appliesTo':m.get('appliesto',d.get('appliesto','')),'status':m.get('status','draft / specification entry'),'mdn':m.get('mdn_url',''),'refs':w3.get(name,[]),'notice':category_notes.get(cat,'Compare the highlighted element before and after your change. The declaration can depend on surrounding elements, other properties, and the rendering context. Edit the supporting CSS when a prerequisite is needed.')})
data={'properties':props,'syntaxes':x['syntaxes'],'categories':[a for a,b in rules]+['Specialized & experimental'],'snapshot':'2026-10-04','w3Count':len(w3),'w3Reported':732,'mdnCount':len(mdn),'total':len(props)}
(p/'dist/data.js').write_text('window.CSS_LAB_DATA='+json.dumps(data,separators=(',',':'))+';')
print('Properties',len(props),'with grammar',sum(bool(p['syntax']) for p in props),'types',len(x['syntaxes']))
