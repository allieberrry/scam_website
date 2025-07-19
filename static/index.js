$(document).ready(function () { 

    //card animations
    const cards = $(".card");

    // Scroll to first card if cards exist 
    if (cards.length > 0) {
        $("html, body").animate({
            scrollTop: $(".card").first().offset().top - 30
        }, 600);
    }

    cards.hide().each(function (i) {

        $(this).delay(200 * i).slideDown().animate( //looping through all cards and the delay starts at 0s and adds 200s per card
            { opacity: 1 }, // opacity will be set to 1 after 400 milliseconds
            { duration: 400 }
        );
    });

    

    // functionality for the popular scam texts
    let tollScam = "Florida EZPass Alert \n \nFINAL REMINDER: Toll invoice #FL294301 remains unpaid. $6.50 due today to avoid $72 penalty. \n \nPay securely: https://ezpassfl-paytoll.com"
    $(".toll").click(function(){
        $(".scam_text").val(tollScam)
    })

    let addressScam = "USPS Delivery Notice: 2 failed delivery attempts due to incomplete address info. Your package is on hold and will be returned to sender in 48 hours. \n \nUpdate your address now to resume delivery: \n \nhttps://bit.ly/4dsxMqe?YmA=KuUw8W5m81 \n \nThank you for your understanding. Wishing you a wonderful day."
    $(".address").click(function(){
        $(".scam_text").val(addressScam)
    })

    let orderScam = "This is a courtesy call regarding a pending order on your Amazon account. \n \nAn unverified purchase of a MacBook Pro and AppleCare coverage totaling $1,349.99 has been placed. If you did not authorize this transaction, press 1 now to speak with a fraud specialist or call us back immediately to cancel the order and prevent your account from being charged."
    $(".order").click(function(){
        $(".scam_text").val(orderScam)
    })

    let loanScam = "IMPORTANT: This message concerns your mortgage with Summit Ridge Lending and a time-sensitive matter regarding your property at 1384 Maple Hollow Ln, Crestview Heights, CA 93012.\n \nAn allocated waiver check has been issued. To avoid delays or forfeiture, call 888-467-3210 immediately. Details cannot be disclosed via text due to privacy restrictions."
    $(".loan").click(function(){
        $(".scam_text").val(loanScam)
    })

    let jobScam = "Hi, this is Emily from Bonanza Support. Your resume was shared by our recruiting partners. We’re offering a remote position assisting Bonanza sellers with listings and visibility. Work 60–90 mins/day, earn $50–$500 daily. Base pay is $1,000 every 4 days. Includes 5-day paid trial.Text +1 (612) 267-0824 if interested."
    $(".job").click(function(){
        $(".scam_text").val(jobScam)
    })
});
