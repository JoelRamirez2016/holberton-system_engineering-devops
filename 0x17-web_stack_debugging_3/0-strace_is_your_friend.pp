# Using Puppet, create a manifest that change phpp -> php in wp-settings
exec {
    "sed -i 's/phpp/php/' /var/www/html/wp-settings.php":
    path => '/usr/bin/:/usr/local/bin/:/bin/'
}
