/**
 * Created by asakb on 14/03/2016.
 */
$('.participante').on("click","#participanteUm", function() {
    var Ativo = $('#participanteUm').hasClass("participanteSelecionado");
    if(!Ativo) {
        $('#participanteUm').addClass("participanteSelecionado")
        $('#participanteId').val('1');
        $('#participanteDois').removeClass("participanteSelecionado")
    } else {
        $('#participanteId').val('');
        $('#participanteUm').removeClass("participanteSelecionado")
        $('#participanteDois').removeClass("participanteSelecionado")
    }
});

$('.participante').on("click","#participanteDois", function() {
    var Ativo = $('#participanteDois').hasClass("participanteSelecionado");
    if(!Ativo) {
        $('#participanteDois').addClass("participanteSelecionado")
        $('#participanteId').val('2');
        $('#participanteUm').removeClass("participanteSelecionado")
    } else {
        $('#participanteId').val('');
        $('#participanteUm').removeClass("participanteSelecionado")
        $('#participanteDois').removeClass("participanteSelecionado")
    }
});

$('#votarBtn').click(function(){
    $.get("{% url votar %}", function(data, status){
        alert("Data: " + data + "\nStatus: " + status)
    })
})