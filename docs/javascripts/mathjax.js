window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true, // Crucial for environments like align, equation
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
