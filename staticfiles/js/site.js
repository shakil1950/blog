$(document).ready(function() {
    $(document).on('click', '.save-btn', function(e) {
        e.preventDefault();
        
        var id = $(this).data('id'); // সেভ বাটন থেকে ID নিল
        
        // সব এডিট বাটন থেকে নির্দিষ্ট আইডি ওয়ালা বাটনটির URL খুঁজে বের করা
        var editButton = $('.edit-btn[data-id="' + id + '"]');
        var url = editButton.attr('data-url');

        console.log("Post ID:", id);
        console.log("Target URL:", url);

        if (!url || url === "") {
            alert("Error: URL not found! বাটনে data-url ঠিকমতো আসেনি।");
            return;
        }

        // ফর্ম ডাটা এবং ইমেজ হ্যান্ডলিং
        var formElement = document.getElementById('form' + id);
        var formData = new FormData(formElement); // ইমেজের জন্য এটিই সেরা

        $.ajax({
            url: url,
            type: "POST",
            data: formData,
            processData: false, // ইমেজের জন্য এটি false থাকতে হবে
            contentType: false, // ইমেজের জন্য এটি false থাকতে হবে
            headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
            success: function(response) {
                if(response.status === 'success') {
                    alert("Post successfully updated");
                    location.reload();
                }
            },
            error: function(xhr) {
                // ভ্যালিডেশন এরর দেখার জন্য
                console.log("Validation Errors:", xhr.responseJSON.errors);
                alert("সেভ করা সম্ভব হয়নি। ডাটা ঠিকমতো দিয়েছেন তো?");
            }
        });
    });

    //  Sweet alert
            $(document).on('click', '.delete-btn', function(e) {
                e.preventDefault(); // বাটনের ডিফল্ট কাজ বন্ধ করা
                
                var btn = $(this);
                var id = btn.attr('data-id'); 
                var url = btn.attr('data-url');

                console.log("Clicked! ID:", id, "URL:", url); // এটি আপনার কনসোলে চেক করার জন্য

                if (!url) {
                    alert("URL পাওয়া যাচ্ছে না!");
                    return;
                }

                if (confirm('Are you sure to delete this post?')) { // আপাতত সহজ কনফার্মেশন দিয়ে টেস্ট করুন
                    $.ajax({
                        url: url,
                        type: "POST",
                        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
                        success: function(response) {
                            if(response.status === 'success') {
                                alert("Successfully deleted!");
                                location.reload();
                            } else {
                                alert("Error: " + response.status);
                            }
                        },
                        error: function(xhr) {
                            console.log(xhr.responseText);
                            alert("Delete fail।");
                        }
                    });
                }
            });
    // End of alert
    // Profile Update
   $(document).on('submit', '#profileUpdateForm', function(e) {
        e.preventDefault(); // ব্রাউজারের ডিরেক্ট সাবমিট আটকাবে
        console.log("AJAX Form Submit Triggered!");

        let form = $(this);
        let formData = new FormData(this);

        $.ajax({
            url: form.attr('action'),
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            headers: {
                "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
            },
            success: function(response) {
                console.log("Server response:", response);
                if (response.status === 'success') {
                    $('.modal').modal('hide');
                    Swal.fire({
                        icon: 'success',
                        title: 'অভিনন্দন!',
                        text: 'প্রোফাইল আপডেট হয়েছে।',
                        timer: 2000,
                        showConfirmButton: false
                    }).then(() => {
                        location.reload();
                    });
                }
            },
            error: function(xhr) {
                console.error("Error:", xhr.responseText);
                alert("ভুল হয়েছে! কনসোল চেক করুন।");
            }
        });
    });
});


function previewImage(input, id) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function(e) {
            // প্রিভিউ ইমেজের সোর্স পরিবর্তন করা
            $('#preview' + id).attr('src', e.target.result).show();
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}