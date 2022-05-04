Summary:        tauOS Plymouth Theme
Name:           tau-plymouth
Version:        1.1
Release:        2
License:        GPLv3
URL:            https://tauos.co
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       plymouth-scripts

%description
A nice looking Plymouth theme for tauOS

%prep
%setup -q
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
plymouth-set-default-theme tau -R

%files
%doc README.md
%license licenses/LICENSE
%dir %{_datadir}/plymouth/themes/tau
%{_datadir}/plymouth/themes/tau/*

%changelog
* Wed May 4 2022 Jaiden Riordan <jade@fyralabs.com> 1.1-2
- Fork from elementaryOS for firmware support
* Fri Apr 8 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Initial Release
