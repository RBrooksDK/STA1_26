window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    // arithmatex wraps .md math; mkdocs-jupyter leaves $…$ in notebook HTML.
    ignoreHtmlClass: "tex2jax_ignore|html",
    processHtmlClass:
      "arithmatex|jp-Notebook|jp-RenderedMarkdown|jp-RenderedHTMLCommon",
  },
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
