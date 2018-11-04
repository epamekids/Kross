$( document ).ready(function() {
   $("input").each(function (num, item) {
    $(item).addClass("mdl-textfield__input")
  })
  $("label").each(function (num, item) {
   $(item).addClass("mdl-textfield__label")
 })
  $("#data").each(function (num, item) {
   $(item).addClass("mdl-textfield mdl-js-textfield")
 })
});
