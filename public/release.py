import markdown2

markdown2.markdownFromFile(
    input = ('page1.md', 'page2.md'),
    output = ('page1.html', 'page2.html'),
    encoding = 'utf8',
)