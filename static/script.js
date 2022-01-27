function selected(bool) {
   if (bool == 'False') {
       $(".incorrect").show();
       $(".correct_answer").show();
       $(".artist-row").hide();
   }
   else {
       $(".correct").show();
       $(".correct_answer").show();
       $(".artist-row").hide();
   }
};
