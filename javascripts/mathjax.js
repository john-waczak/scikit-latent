window.MathJax = {
  tex: {
    //inlineMath: [['\(', '\)']],
    //displayMath: [['\[', '\]']],
    processEscapes: true,
    processEnvironments: true, 
    tags: 'ams' // Enables AMS equation numbering
  },
  options: {
    ignoreHtmlClass: '.*|',
    processHtmlClass: 'arithmatex'
  }
};
document$.subscribe(() => {
  MathJax.typesetPromise();
});
