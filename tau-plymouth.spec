Summary:        tauOS Plymouth Theme
Name:           tau-plymouth
Version:        2
Release:        1
License:        GPLv3
URL:            https://tauos.co
Source0:        https://github.com/tau-OS/tau-plymouth/archive/refs/heads/main.zip
BuildArch:      noarch

Requires:       plymouth-scripts
Requires:       plymouth-plugin-script

%description
A nice looking Plymouth theme for tauOS

%prep
%setup -q -n tau-plymouth-main
%build
%install

# Install licenses
mkdir -p licenses
install -pm 0644 LICENSE licenses/LICENSE

mkdir -p %{buildroot}%{_datadir}/plymouth/themes/tau
install -D *.png %{buildroot}%{_datadir}/plymouth/themes/tau
install tau.plymouth -t %{buildroot}%{_datadir}/plymouth/themes/tau
install tau.script -t %{buildroot}%{_datadir}/plymouth/themes/tau

%post
if [ $1 -gt 1 ] && [ -e /boot/vmlinuz-$(uname -r) ] && [ -e /sbin/depmod ] && [ -x %{_sbindir}/dracut ]; then
  plymouth-set-default-theme tau -R
else
  plymouth-set-default-theme tau
fi

%files
%doc README.md
%license licenses/LICENSE
%dir %{_datadir}/plymouth/themes/tau
%{_datadir}/plymouth/themes/tau/*

%changelog
* Thu Dec 29 2022 Jaiden Riordan <jade@fyralabs.com> - 2-1
- Initial Release
* Fri Apr 8 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Initial Release
