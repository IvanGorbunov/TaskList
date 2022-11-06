$(document).ready(function (){

    let csrfToken = $("input[name=csrfmiddlewaretoken]").val();

    $("#createButton").click(function (){
        let serializedData = $("#createTaskForm").serialize();
        $.ajax({
            url: $("createTaskForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function(response) {
                $("#taskList").append('<div class="card mb-1" id="taskCard" data-id="' + response.task.id + '">\n' +
                    '            <div class="row g-0">\n' +
                    '            <div class="card-body  mb-0">\n' +
                    '                <div class="d-flex flex-row align-middle">\n' +
                    '                    <div class="align-middle">\n' +
                    response.task.title +
                    '                        <button type="button" class="close float-right" data-id="' + response.task.id + '"><span aria-hidden="true">&times;</span></button>\n' +
                    '                    </div>\n' +
                    '                </div>\n' +
                    '            </div>\n' +
                    '            </div>\n' +
                    '        </div>')
            }
        })

        $("#createTaskForm")[0].reset();
    });

    $("#taskList").on('click', '.card', function () {
        let dataId = $(this).data('id');

        $.ajax({
           url: '/tasks/' + dataId + '/completed/',
           data: {
               csrfmiddlewaretoken: csrfToken,
               id: dataId,
           },
           type: 'post',
           success: function () {
               let cardItem =  $('#taskCard[data-id="' + dataId + '"]');
               cardItem.css('text-decoration', 'line-through').hide().slideDown();
               $("#taskList").append(cardItem);
           }
        });
    }).on('click', 'button.close', function (event) {
        event.stopPropagation();

        let dataId = $(this).data('id');

        $.ajax({
            url: '/tasks/' + dataId + '/delete/',
            data: {
               csrfmiddlewaretoken: csrfToken,
               id: dataId,
            },
            type: 'post',
            dataType: 'json',
            success: function () {
                $('#taskCard[data-id="' + dataId + '"]').remove();
            }
        })
    });


});