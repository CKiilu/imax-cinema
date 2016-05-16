function custom_ajax(path, csrf) {
    $('.action--buy').click(function() {
        $.ajax({
            url: path,
            type: "POST",
            data: {
                seats: seating(),
                csrfmiddlewaretoken: csrf,
            },
            success: function(data) {
                succeed(data);
            },
            error: function(jqXHR, textStatus) {
                console.log("Request failed: " + textStatus);
            }
        });
    });
}

function seating() {
    $('.tooltip').click(function() {
        getSeats(getBookedSeats());
    });
    return getSeats(getBookedSeats());
}

function getSeats(booked_seats) {
    var seatValues = [];
    var seat = $('.row').find('.row__seat--selected');
    $(seat).each(function(index, data) {
        if ($.inArray($(data).attr('data-tooltip'), booked_seats) == -1) {
            seatValues.push($(data).attr('data-tooltip'));
        }
    });
    return seatValues;
}

function getBookedSeats() {
    var seats = $('.row').find('.booked');
    seatValues = []
    $(seats).each(function() {
        seatValues.push($(this).attr('data-tooltip'));
    });
    return seatValues;
}

function succeed(data) {
    var reg_tkts = $('#id_number_of_regular_tickets');
    var stu_tkts = $('#id_number_of_student_tickets');
    var num_tkts = $('#num_tkt');
    var tk_tkts = $('#tk_tkt');
    var ticketing = $('.ticketing');
    var reg_id = reg_tkts.attr('id');
    var stu_id = stu_tkts.attr('id');
    $('.price').css({
        'height': '100px',
        'overflow-y': 'scroll'
    });
    $('p').css({
        'color': '#000'
    });
    $('span').css({
        'color': '#000'
    });


    var num_seats = data.seats.length;
    $('#seating').text(data.seats.toString());
    ticketing.attr('max', num_seats.toString())
    num_tkts.text(num_seats);
    num_tkts.val(num_seats);
    var total = 0;
    ticketing.change(function() {
        var stu = stu_tkts.val();
        var reg = reg_tkts.val();
        var current = $(this);
        total = +stu + +reg;
        if (reg_id === current.attr('id')) {
            var remaining_tkts = (num_seats - +stu);
            stu_tkts.attr('max', remaining_tkts.toString());
            if (total > num_seats) {
                total = num_seats;
                current.val(remaining_tkts);
            }
            else {
                tk_tkts.text(total);
            }
        }
        else if (stu_id === current.attr('id')) {
            var remaining_tkts = (num_seats - +reg);
            reg_tkts.attr('max', remaining_tkts.toString());
            if (total > num_seats) {
                total = num_seats;
                current.val(remaining_tkts);
            }
            else {
                tk_tkts.text(total);
            }
        }
    });
}

function getTotalPrice(path) {
    $('#total').css('color', 'black')
    $('.total').css('color', 'black')
    $('.ticketing').change(function() {
        var price_id = $('select').val();
        console.log('id: ', price_id)
        var reg_tkts = $('#id_number_of_regular_tickets').val();
        var stu_tkts = $('#id_number_of_student_tickets').val();
        $.ajax({
            url: path,
            type: "GET",
            data: {
                stu_tkts: stu_tkts,
                reg_tkts: reg_tkts,
                price_id: price_id,
            },
            success: function(data) {
                console.log($('#total').text())
                $('#total').text(data.total);
            }
        });
    });
}