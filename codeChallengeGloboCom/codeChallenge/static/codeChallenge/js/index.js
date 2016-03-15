/**
 * Created by asakb on 14/03/2016.
 */
$('.participante').on("click","#participanteUm", function() {
    var Ativo = $('#participanteUm').hasClass("participanteSelecionado");
    if(!Ativo) {
        $('#participanteUm').addClass("participanteSelecionado")
        $('#participanteDois').removeClass("participanteSelecionado")
    } else {
        $('#participanteUm').removeClass("participanteSelecionado")
        $('#participanteDois').removeClass("participanteSelecionado")
    }
});

$('.participante').on("click","#participanteDois", function() {
    var Ativo = $('#participanteDois').hasClass("participanteSelecionado");
    if(!Ativo) {
        $('#participanteDois').addClass("participanteSelecionado")
        $('#participanteUm').removeClass("participanteSelecionado")
    } else {
        $('#participanteUm').removeClass("participanteSelecionado")
        $('#participanteDois').removeClass("participanteSelecionado")
    }
});