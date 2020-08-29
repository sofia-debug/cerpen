var $ = require('jQuery')
jQuery(document).ready(function (){
    $("#morePoss").click(function (){
        $("#morePoss").html("<p> SOBAKY</p>");
    })()
})();










$("#lessPoss").click(function (){
        $("#lessPoss").html("<span id='morePoss'> more...</span>");
    })();

toggle + hide chi sho 