{pkgs}: {
  deps = [
    pkgs.libmysqlclient
    pkgs.libev
    pkgs.python311Packages.flask
  ];
}
