/* Table initialisation */
$(document).ready(function() {
    
    $('.dataTable').dataTable( {
        "paginate": false,
        "filter": false,
        "sort": true,
        "autoWidth": false,
        "stateSave":true
    } );
    
    $('.dataTableFiltered').dataTable( {
        "paginate": false,
        "filter": true,
        "sort": true,
        "autoWidth": false,
        "stateSave":true
    } );
} );