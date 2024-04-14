var contrib_interval, contrib_clear_timeout, contrib_items;
var contrib_cycle = 1;

Signals.watch( 'slideshow-loaded', function( ) {
	/* Allow using arrow keys in slide navigation */
	$( document ).keydown( function( e ) {
		if( e.keyCode == 37 && $( '#prev-slide' ).is( ':visible' ) ) {
			$( '#prev-slide' ).click( );
		} else if( e.keyCode == 39 && $( '#next-slide' ).is( ':visible' ) ) {
			$( '#next-slide' ).click( );
		}
	} );

	/* Fill div's with data from inline attribute */
	$( '#support-live .data-fill' ).each( function( e ) {
		$( this ).html( $( this ).attr( 'data-content' ) );
	} );

	/* Watch opening, opened and closing slides for some effects */
	Signals.watch( 'slide-opened', function( slide ) {
		current = slide.find( '.slide' );

		/* Welcome */
		if( current.attr( 'id' ) == 'welcome' ) {
			current.find( '#logos div' ).each( function( e ) {
				$( this ).find( 'span' ).css( 'opacity', '0.5' );
				$( this ).find( 'img' ).delay( 600 ).fadeIn( 'slow' );
				$( this ).find( 'span' ).delay( 1200 ).fadeIn( 'slow' );
			} );
		}

		/* Desktop */
		if( current.attr( 'id' ) == 'desktop' ) {
			current.find( '.panel img' ).css( 'top', '0' );
			$( '#hilight' ).css( 'background-color', 'rgba( 230, 30, 160, 0.4 )' ).fadeIn( 10000 );
		}

		/* Live support */
		if( current.attr( 'id' ) == 'support-live' ) {
			current.find( '.local-de' ).fadeIn( );
			current.find( '.local-jp' ).delay( 300 ).fadeIn( );
			current.find( '.local-fr' ).delay( 700 ).fadeIn( );
			current.find( '.local-fi' ).delay( 850 ).fadeIn( );
			current.find( '.local-cat' ).delay( 3000 ).fadeIn( );
		}

	} );

	Signals.watch( 'slide-closing', function( slide ) {
		current = slide.find( '.slide' );

		/* Common classes */
		$( '.fo' ).clearQueue( ).stop( ).fadeOut( 200 ).css( 'opacity', '1' );
	} );
} );
