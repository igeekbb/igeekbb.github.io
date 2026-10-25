hexo.extend.filter.register('after_render:html', function (html) {
  return html.replace(/aria-label="搜索 Command K"/g, 'aria-label="搜索 ⌘K"')
})
