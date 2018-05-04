//SCRIPT CON FUNCIONES DEL CRUD DE BENEFICIOS Y TIPO DE BENEFICIOS, ADEMAS DE LAS CONFIGURACIONES DE LA TABLA
$(document).ready(function(){
//Función para mostrar la tabla del plan indicativo

$("select").addClass("form-control input-sm");
$("input").addClass("form-control input-sm");
$("modal").css("width","90%");
$('.datepicker').datepicker();

var datatable = $('#infoTipoBeneficio').DataTable({
  "ordering": false,
        lengthChange: false,
        dom: 'Bfrtip',
        lengthMenu: [
            [ 10, 25, 50, -1 ],
            [ '10 items', '25 items', '50 items', 'Mostrar Todo' ]
        ],
        buttons: [
            'pageLength',
            {
            extend: 'colvis',
            postfixButtons: [ 'colvisRestore' ],
            collectionLayout: 'fixed four-column'
            },

            {
            extend:    'copyHtml5',
            text:      '<i class="fa fa-files-o"></i>',
            titleAttr: 'Copiar Datos'
            },

            {
            extend:    'csvHtml5',
            text:      '<i class="fa fa-file-text-o"></i>',
            titleAttr: 'CSV'
            },

            {
            extend:    'excelHtml5',
            text:      '<i class="fa fa-file-excel-o"></i>',
            titleAttr: 'Excel'
            },

            {
            extend:    'pdfHtml5',
            text:      '<i class="fa fa-file-pdf-o"></i>',
            titleAttr: 'PDF'
            },

            {
            extend:    'pdfHtml5',
            text:      '<i class="fa fa-print" aria-hidden="true"></i>',
            titleAttr: 'Imprimir'
            }
        ],
        language: {
            buttons: {
                colvis: 'Seleccionar Columnas',
                copy:'Copiar Datos',
                csv: 'Exportar CSV',
                excel:'Exportar Excel',
                pdf:'Exportar PDF',
                print:'Imprimir'
            }
        }
    });
  });

    function editarTipoBeneficio(sender){

        var fila = $(sender).closest("tr");
        var id = $("td:eq(0)",$(fila)).html();
        var nombre = $("td:eq(1)",$(fila)).html();
        var descripcion = $("td:eq(2)",$(fila)).html();
        var activo = $("td:eq(4)",$(fila)).html();

        $('#id_tipobeneficio').val(id);
        $('#nombre_tipobeneficio').val(nombre);
        $('#descripcion_tipobeneficio').val(descripcion);
        $('#activo_tipobeneficio').val(activo);
    }

    function editarBeneficio(sender){

        var fila = $(sender).closest("tr");
        var id = $("td:eq(0)",$(fila)).html();
        var nombre = $("td:eq(1)",$(fila)).html();
        var descripcion = $("td:eq(2)",$(fila)).html();
        var cantidad = $("td:eq(3)",$(fila)).html();
        var valor_unitario = $("td:eq(6)",$(fila)).html();
        var valor_total = $("td:eq(5)",$(fila)).html();
        var vigencia = $("td:eq(7)",$(fila)).html();

        $('#id_beneficio').val(id);
        $('#nombre_beneficio').val(nombre);
        $('#descripcion_beneficio').val(descripcion);
        $('#cantidad_beneficio').val(cantidad);
        $('#valor_unitario_beneficio').val(valor_unitario);
        $('#valor_total_beneficio').val(valor_total);
        $('#vigencia_beneficio').val(vigencia);
    }

    $( function() {
      var $list = $('#infoTipoBeneficio');
      $list.find("tr").not('.accordion').hide();
      $list.find("tr").eq(0).show();
      var $accord;
      $list.find('.accordion').mouseover(function(){
        $accord = $(this);
        });
      $list.find('.fa-plus','fa-minus').click(function(){
        var id_accord = "#accord_"+$("td:eq(0)",$accord.context).html();
        var $acordeon = $(id_accord);
        $acordeon.siblings().fadeToggle(0);
        $acordeon.addClass('active');
        var id_plus = "#plus_"+$("td:eq(0)",$accord.context).html();
        if ($(id_plus).hasClass('fa-plus')){
          $(id_plus).removeClass('fa-plus').addClass('fa-minus');
        }else{
          $(id_plus).removeClass('fa-minus').addClass('fa-plus');
        }
      });
    } );
