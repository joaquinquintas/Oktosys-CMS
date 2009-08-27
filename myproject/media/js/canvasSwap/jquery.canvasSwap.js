/**
 * --------------------------------------------------------------------
 * jQuery-Plugin "canvasSwap"
 * 
 * Version: 1.0 Beta, 05.22.2009
 * by Trevor Sheridan, trevorsheridan@mac.com
 *                      http://www.trevorsheridan.com/
 *
 * Copyright (c) 2009 Trevor Sheridan
 * Licensed under GPL (http://www.opensource.org/licenses/gpl-license.php)
 *
 * --------------------------------------------------------------------
 * Description
 * 
 * jQuery plugin to do an image swap for another image. Includes IE6 PNG support.
 * --------------------------------------------------------------------
 * Options
 * 
 * @ suffix (str) - DEFAULTS TO: '_over' - Suffix for your swap image.
 * eg: Current file is: my_image_1.jpg. Swap file is: my_image_1_hover.jpg.
 * Suffix will be: _hover.
 *
 * @ ie6_support (boolean) - DEFAULTS TO: false - enable/disable ie6 support. (In order for this script to
 * work properly you must have a png transparency script installed. I recommend including
 * "pngFix" by Andreas Eberhard - http://jquery.andreaseberhard.de/
 *
 * --------------------------------------------------------------------
 * Considerations
 * 
 * It is recommended that you install an image preload plugin such as "Preload 1.0.8".
 *
 * IE6 png support has a difficult time with images over 1000px.
 *
 * --------------------------------------------------------------------
 * Example usage (included in your external js file or script tags)
 * 
 * //Swap images with the class of 'myswap', a suffix of '_over', and ie 6 png support enabled
 * $.fn.canvasSwap.defaults.suffix = '_over';
 * $.fn.canvasSwap.defaults.ie6_support = true;
 * $('img.myswap').canvasSwap();
 * 
 * --------------------------------------------------------------------
 */

(function($) {

jQuery.fn.canvasSwap = function(options) {
    	
    var options = jQuery.extend({}, jQuery.fn.canvasSwap.defaults, options);
    
    jQuery(this).hover (
    
    	function () {
    		
    		var thesrc = $(this).attr('src');
    	
    		var name = thesrc.substring(0, thesrc.lastIndexOf('.'));
    	
    		var extension = thesrc.substring(thesrc.lastIndexOf('.'));
    		
    		$(this).attr('src', name + options.suffix + extension);
    		
    	}, function () {
    		
    		var thesrc = $(this).attr('src');
    		
    		var name = thesrc.substring(0, thesrc.lastIndexOf('.') - options.suffix.length);
    		
    		var extension = thesrc.substring(thesrc.lastIndexOf('.'));
    		
    		$(this).attr('src', name + extension);
    		
    	}
    	
    );
    
    if(options.ie6_support == true) {
    	
    	if(jQuery.browser.version == "5.5" || jQuery.browser.version == "6.0") {
    	
    		jQuery(this).next().hover (
    		
    			function () {
    			
    				var thefilter = $(this).css('filter').substring(56);
        	
        			var thesrc = thefilter.substring(0, thefilter.length-24);
        	
        			var name = thesrc.substring(0, thesrc.lastIndexOf('.'));
        		
        			var extension = thesrc.substring(thesrc.lastIndexOf('.'));
        		
        			$(this).css('filter', 'progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\'' + name + options.suffix + extension + '\', sizingMethod=\'scale\')');
    				
    			}, function () {
    			
    				var thefilter = $(this).css('filter').substring(56);
        	
        			var thesrc = thefilter.substring(0, thefilter.length-24);
        			
        			var name = thesrc.substring(0, thesrc.lastIndexOf('.') - options.suffix.length);
    		
    				var extension = thesrc.substring(thesrc.lastIndexOf('.'));
        	
        			$(this).css('filter', 'progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\'' + name + extension + '\', sizingMethod=\'scale\')');
    				
    			}
    			
    		);
    		
    	}
    	
    }
    
};

jQuery.fn.canvasSwap.defaults = {
	
	suffix: '_over',
	
	ie6_support: false
	
}

})(jQuery);