(function() {
  if (window.Templates == null) {
    window.Templates = {};
  }

  window.Templates['home'] = function(context) {
    return (function() {
      var $o;
      $o = [];
      $o.push("<h1>HELLO WORLD</h1>");
      return $o.join("\n");
    }).call(context);
  };

}).call(this);
