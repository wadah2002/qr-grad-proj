{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  packages = with pkgs; [
    python3Packages.flask
    python3Packages.qrcode
  ];
  FLASK_APP = "main.py";
}
