<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', '');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'UGk)}LjSx{cV?JU{5n6rfF5][C&N@OHM0*}]4gZ?j:swm>{VCz~g;9PgC!OBg&Xk');
define('SECURE_AUTH_KEY',  'XJJr=-/I.L_lCUPayI/:1a>q8CVv)IBbi[G!@BdVda7.0^/G*4x~(#~^Oal(QXx6');
define('LOGGED_IN_KEY',    '0lF&KWGV)c-D#Lq4&R [gR}m=0*p${[VK9LbvVoKXOV9{`.ii{xWI*XVXJa$2kRm');
define('NONCE_KEY',        ';=rUny0#c^3_GLofV;TIe)VZ*/=P^=B]&q=p% ;!kgL3JCVjZxpC-O|Z00@A(Fb,');
define('AUTH_SALT',        'xvp;JPjeJlA&,MRKI]>P~dKSE~kP^;9/9<:^y J,?|uT%*gceIs!{_<myG`Ei7h9');
define('SECURE_AUTH_SALT', 'u|xd)qX!,0:~M5EfU?MW]=}me_EhNzo-7-Q=_Bgb{{Ox@q:NuSK^%Vm/kRW.:>Mx');
define('LOGGED_IN_SALT',   'xTg:ezV){B:(g&j5Qhe/TElP$ `@%JqEYG7bHcRNO~V].@>}i{R CK0u2Oi0=SZC');
define('NONCE_SALT',       'G7HlsAT4G!6((i1=(ynIS;lC=_q(!NYm6[]C)z]NI`P`>3u>gt[>@T{xIlBrMR(f');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
