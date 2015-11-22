%define _use_internal_dependency_generator 0

Summary:	Chapeau meta-package for the legacy nvidia proprietary drivers
Name:		chapeau-nvidia-legacy
Version:	1
Release:	1%{?dist}
License:	distributable
Group:		Chapeau
URL:		http://chapeaulinux.org
BuildArch:	x86_64

Requires:	akmod-nvidia-340xx
Requires:	xorg-x11-drv-nvidia-340xx-libs.i686

%description
A meta package for the legacy nvidia drivers packages from RPMFusion

%prep

%build

%clean 

%install

%post

%preun
[ $1 =0 ] && rpm -e akmod-nvidia-340xx xorg-x11-drv-nvidia-340xx-libs.i686

%files 


%changelog
* Fri Nov 20 2014 Vince Pooley <vince@chapeaulinux.org>
- initial release

