%define	pname	rssgrab
Summary:	RSS/RDF contents viewer
Summary(pl):	Przegl±darka zawarto¶ci RSS/RDF
Name:		gDesklets-%{pname}
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname}-%{version}.tar.bz2
# Source0-md5:	e21e70a2a2b872690576b2ffc6a025ad
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=101
BuildRequires:	python >= 2.3
BuildRequires:	python-pygtk >= 1.99.18
Requires:	gDesklets
Requires:	gDesklets-PsiSensorPackage
Requires:	gDesklets-DisplayConstraints
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sensorsdir	%{_datadir}/gdesklets/Sensors
%define _displaysdir	%{_datadir}/gdesklets/Displays

%description
This desklet allows you to viw the contents of an RSS/RDF feed.

%description -l pl
Ten desklet pozwala przegl±daæ informacje w formacie RSS/RDF.

%prep
%setup -q -n %{pname}-%{version}

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
