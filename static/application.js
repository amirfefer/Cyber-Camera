$(document).ready(function(){
    $("#cloud-note").hide();
    $("#myTab a").click(function(e){
    	e.preventDefault();
    	$(this).tab('show');
    });
    $("#btn-small").click(function(e){
        e.preventDefault();
        $("#bg").width(320).height(240);
        $("#imagewrap").hide(100);
        $("#imagewrap").show(100);

    });

     $("#toggle-bars").click(function(e){
        $("#btn-cloud").toggle("slow");
        $('#btn-toggle-video').toggle("slow");
        $('#btn-image').toggle("slow");
        $('#btn-sound').toggle("slow");
        $("#btn-lg2").toggle("slow");
        $("#navbar-bottom").toggle("slow");
    });

     $("#btn-full-sc").click(function(e){
        e.preventDefault();
        $( '#' ).toggleClass("overlay")
    });

    $('.test-popup-link').magnificPopup({
        type:'image',
         verticalFit: true,
         midClick: true // Allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source in href.
    });


    $("#btn-med").click(function(e){
        e.preventDefault();
        $("#bg").width(640).height(480);
        $("#imagewrap").hide();
        $("#imagewrap").show();
    });
     $("#btn-lg").click(function(e){
        e.preventDefault();
        $("#bg").width(800).height(600);
        $("#imagewrap").hide();
        $("#imagewrap").show();
    });
    $("#btn-image").click(function(e){
        e.preventDefault();
        alert("image saved at server");
      });
      $("#btn-toggle-video").click(function(e){
        e.preventDefault();
        var url;
        if ($( "#btn-toggle-video" ).hasClass("btn-warning")){
            if ($("#btn-cloud").hasClass("btn-info"))
                url = '?options=record&cloud=true';
            else
                url = "?options=record";
        }
        if ($( "#btn-toggle-video" ).hasClass("btn-primary"))
            url = "stopV";
        $.ajax({url: window.location.href +url,
         beforeSend: function() {
            $("#bg").attr("src","static/spinner.gif");
            },
        success: function(result){
            $( "#btn-toggle-video" ).toggleClass("btn-warning btn-primary")
            $("#stream").html(result);
         }});

      });
      $("#btn-cloud").click(function(e){
        e.preventDefault();
        $("#btn-cloud").toggleClass('btn-warning btn-info');
        $("#cloud-note").toggle("slow");
      });
      var recordRTC = null;
       $("#btn-sound").click(function(e){
        e.preventDefault();

        if ($("#btn-sound").hasClass('btn-danger')){
            recordRTC.stopRecording(function(audioURL) {
            var formData = new FormData();
            formData.append('edition[audio]', recordRTC.getBlob())
            var uri = location.href + 'audio';

            $.ajax({
                type: 'POST',
                url: uri,
                 data: formData,
                 contentType: false,
                 cache: false,
                 processData: false,
             })
            });
        }
        else
        {
            var session = {
                audio: true,
                video: false
            };

            navigator.getUserMedia(session, function (MediaStream) {
                recordRTC = RecordRTC(MediaStream,{  recorderType: StereoAudioRecorder});
                recordRTC.startRecording();
                }, onError);
        }
       $("#btn-sound").toggleClass('btn-warning btn-primary');
        })
});
function onError() {
console.log("ERROR");
}