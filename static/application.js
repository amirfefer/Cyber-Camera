$(document).ready(function(){
    $("#cloud-note").hide();
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
        var url;
        if ($( "#btn-toggle-video" ).hasClass("btn-success")){
            if ($("#btn-cloud").hasClass("btn-info"))
                url = '?options=record&cloud=true';
            else
                url = "?options=record";
        }
        if ($( "#btn-toggle-video" ).hasClass("btn-danger"))
            url = "stopV";
        $.ajax({url: window.location.href +url, success: function(result){
            $( "#btn-toggle-video" ).toggleClass("btn-danger")
            $("#stream").html(result);
         }});
         /*
        if ($( "#btn-toggle-video" ).hasClass("btn-success")){
            if ($("#btn-cloud").hasClass("btn-info"))
                document.location.href='?options=record&cloud=true'
            else
                document.location.href='?options=record';
            }
        else
            document.location.href='stopV'; */
      });
      $("#btn-cloud").click(function(e){
        e.preventDefault();
        $("#btn-cloud").toggleClass('btn-info');
        $("#cloud-note").toggle("slow");
      });
});