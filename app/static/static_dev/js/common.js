jQuery(function($){
	$(document).mouseup(function (e){
		var div = $(".popup .window");
		if (!div.is(e.target)
		    && div.has(e.target).length === 0) {
			$('.popup').fadeOut();
		}
	});
});
jQuery(function($){
	$(document).mouseup(function (e){
		var div = $(".catalog-page .content .sort .sub");
		if (!div.is(e.target)
		    && div.has(e.target).length === 0) {
			$('.catalog-page .content .sort .sub').fadeOut();
		}
	});
});

$(function () {
    var tabContainers = $('div.tabs > div');
    tabContainers.hide().filter(':first').show();
    $('div.tabs ul.tabNavigation a').click(function () {
        tabContainers.hide();
        tabContainers.filter(this.hash).show();
        $('div.tabs ul.tabNavigation a').removeClass('selected');
        $(this).addClass('selected');
        return false;
    }).filter(':first').click();
});

$(function(){
	$('.catalog-page .content .list .item .content button.b1,.right-block button').on('click', function() {
		$('.popup.added').fadeIn();
	});
	$('.header button.b2, .footer .col .button button, .index-faq-block .content button').on('click', function() {
		$('.popup.callback').fadeIn();
	});
	$('.index-tabs .tabNavigation li a').on('click', function() {
		$('.popular-slider').slick('setPosition');
	});
	$('.catalog-page .filtr .close').click(function() {
		$('.catalog-page .filtr').fadeOut();
	});
	$('.filtr-btn').click(function() {
		$('.catalog-page .filtr').fadeIn();
	});
	$(window).scroll(function() {
		if($(this).scrollTop() > 180) {
			$('.fixed-header').addClass('opened');
		} else {
			$('.fixed-header').removeClass('opened');
		}
	});
	$('.fixed-header .right-block .link').click(function() {
		$(this).toggleClass('active');
		$('.fixed-header .top-menu').slideToggle();
	});
	$('.top-line .city .sub .close').click(function() {
		$('.top-line .city .sub').fadeOut();
	});
	$('.top-line .city .link').click(function() {
		$('.top-line .city .sub').fadeIn();
	});
	$('.cabinet-orders .more-link a').click(function() {
		$(this).toggleClass('active');
		$(this).parent().next('.cabinet-orders table.hidden').toggle();
	});
	$('.catalog-page .filtr .name').click(function() {
		$('.catalog-page .filtr .items').toggleClass('opened');
	});
	$('.catalog-page .content .top-texts .item .close').click(function() {
		$('.catalog-page .content .top-text-menu a').removeClass('active');
		$('.catalog-page .content .top-texts .item').hide();
	});
	$('.catalog-page .content .top-text-menu a').click(function() {
		$('.catalog-page .content .top-text-menu a').removeClass('active');
		$(this).addClass('active');
		$('.catalog-page .content .top-texts .item').hide();
	});
	$('.catalog-page .content .top-text-menu a.a1').click(function() {
		$('.catalog-page .content .top-texts .item.item1').show();
	});
	$('.catalog-page .content .top-text-menu a.a2').click(function() {
		$('.catalog-page .content .top-texts .item.item2').show();
	});
	$('.catalog-page .content .top-text-menu a.a3').click(function() {
		$('.catalog-page .content .top-texts .item.item3').show();
	});
	$('.catalog-page .content .top-text-menu a.a4').click(function() {
		$('.catalog-page .content .top-texts .item.item4').show();
	});
	$('.catalog-page .content .sort').click(function() {
		$('.catalog-page .content .sort .sub').fadeIn();
	});
	$('.catalog-page .filtr .item .n').click(function() {
		$(this).toggleClass('active');
		$(this).next('.catalog-page .filtr .item .content').slideToggle();
	});
	$('.catalog-page .filtr .item .select a').click(function() {
		$(this).toggleClass('active');
		$(this).prev('.catalog-page .filtr .item .select .hidden').toggle();
	});
	$('.catalog-page .filtr .item .color-select .color').click(function() {
		$('.catalog-page .filtr .item .color-select .color').removeClass('active');
		$(this).addClass('active');
	});
    $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });
	$('.faq-page .item .name').click(function() {
		$(this).toggleClass('active');
		$(this).next('.faq-page .item .text').slideToggle();
	});
	$('.mobile-menu .close').click(function() {
		$('.mobile-menu').fadeOut();
	});
	$('.top-line .menu-button, .fixed-header .menu-button').click(function() {
		$('.mobile-menu').fadeIn();
	});
	$('.slider-for').slick({
	  slidesToShow: 1,
	  slidesToScroll: 1,
	  arrows: false,
	  asNavFor: '.slider-nav'
	});
	$('.slider-nav').slick({
	  slidesToShow: 3,
	  slidesToScroll: 1,
	  asNavFor: '.slider-for',
	  focusOnSelect: true
	});
	$('.brands').slick({
	  speed: 300,
	  slidesToShow: 5,
	  slidesToScroll: 1,
	  responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        slidesToShow: 4
	      }
	    },
	    {
	      breakpoint: 767,
	      settings: {
	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 540,
	      settings: {
	        slidesToShow: 2
	      }
	    }
	  ]
	});
	$('.popular-slider').slick({
	  speed: 300,
	  slidesToShow: 4,
	  slidesToScroll: 1,
	  responsive: [
	    {
	      breakpoint: 991,
	      settings: {
	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 767,
	      settings: {
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 540,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});
});