$(document).ready(function(){
    $("#myTab a").click(function(e){
    	e.preventDefault();
    	$(this).tab('show');
    });
    $("#btn-small").click(function(e){
        e.preventDefault();
        $("#bg").width(320).height(240);
        $("#stream").toggle();
    });
    $("#btn-med").click(function(e){
        e.preventDefault();
        $("#bg").width(640).height(480);
        $("#stream").toggle();
    });
     $("#btn-lg").click(function(e){
        e.preventDefault();
        $("#bg").width(1024).height(768);
        $("#stream").toggle();
    });
    $("#btn-image").click(function(e){
        e.preventDefault();
        alert("image saved at server");
      });
      $("#btn-toggle-video").click(function(e){
        e.preventDefault();

        if ($( "#btn-toggle-video" ).hasClass("btn-success"))
            document.location.href='?options=record';
        else
            document.location.href='stopV';
      });
});