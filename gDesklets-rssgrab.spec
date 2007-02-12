%define		pname	rssgrab
Summary:	RSS/RDF contents viewer
Summary(pl.UTF-8):   Przeglądarka treści RSS/RDF
Name:		gDesklets-%{pname}
Version:	0.6.4
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname}-%{version}.tar.gz
# Source0-md5:	48a16405abd3c796a259d4d4c4d1a0b0
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=101
BuildRequires:	python >= 1:2.3
BuildRequires:	python-pygtk-gtk >= 1.99.18
BuildRequires:	rpm-pythonprov
Requires:	gDesklets
Requires:	gDesklets-PsiSensorPackage
Requires:	gDesklets-DisplayConstraints
%pyrequires_eq	python-libs
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sensorsdir	%{_datadir}/gdesklets/Sensors
%define		_displaysdir	%{_datadir}/gdesklets/Displays

%description
This desklet allows you to view the contents of an RSS/RDF feed.

%description -l pl.UTF-8
Ten desklet pozwala przeglądać informacje w formacie RSS/RDF.

%prep
%setup -q -n %{pname}-%{version}
chmod u+w gfx/bg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

cp -R gfx *.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sensorsdir}/*
%{_displaysdir}/*
