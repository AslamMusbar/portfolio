/**
 *
 * -----------------------------------------------------------------------------
 *
 * Template : Reeni Personal Portfolio HTML Template
 * Author : themes-park
 * Author URI : https://themes-park.com/
 *
 * -----------------------------------------------------------------------------
 *
 **/

(function ($) {
    'use strict';

    var form = $('#contact-form');
    var formMessages = $('#form-messages');

    $(form).submit(function (e) {
        e.preventDefault();

        var formData = $(form).serialize();

        $.ajax({
            type: 'POST',
            url: $(form).attr('action'),
            data: formData
        })
        .done(function (response) {
            $(formMessages)
                .removeClass('error')
                .addClass('success')
                .css({
                    'display': 'block',
                    'padding': '15px',
                    'margin-bottom': '20px',
                    'border-radius': '5px',
                    'background-color': '#d4edda',
                    'color': '#155724',
                    'border': '1px solid #c3e6cb'
                })
                .text(response);

            // Clear input fields
            $('#contact-name, #contact-email, #subject, #contact-message, #contact-phone').val('');

            // Scroll to message
            $('html, body').animate({
                scrollTop: $(formMessages).offset().top - 100
            }, 500);
        })
        .fail(function (data) {
            $(formMessages)
                .removeClass('success')
                .addClass('error')
                .css({
                    'display': 'block',
                    'padding': '15px',
                    'margin-bottom': '20px',
                    'border-radius': '5px',
                    'background-color': '#f8d7da',
                    'color': '#721c24',
                    'border': '1px solid #f5c6cb'
                });

            if (data.responseText !== '') {
                $(formMessages).text(data.responseText);
            } else {
                $(formMessages).text('Oops! An error occurred and your message could not be sent.');
            }

            // Scroll to message
            $('html, body').animate({
                scrollTop: $(formMessages).offset().top - 100
            }, 500);
        });
    });

})(jQuery);
