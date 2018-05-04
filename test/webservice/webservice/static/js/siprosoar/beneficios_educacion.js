/**
 * Created by jaquinonesg on 17/05/17.
 */
$(document).ready(function() {
    $('#basecertificada-form').on('submit', function(event) {
        var html = '<div class="alert alert-info alert-dismissible text-center" role="alert"> <i class="fa fa-circle-o-notch fa-spin"></i> Cargando archivo...</div>';
        $('#basecertificada-box').append(html);
    });

    $('.migration-btn').on('click', function(event) {
        var html = '<div class="alert alert-info alert-dismissible text-center" role="alert"> <i class="fa fa-circle-o-notch fa-spin"></i> Migrando archivo...</div>';
        $('#basecertificada-box').append(html);
    });
});