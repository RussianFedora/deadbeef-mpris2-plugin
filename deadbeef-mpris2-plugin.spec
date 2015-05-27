Name:           deadbeef-mpris2-plugin
Version:        1.8
Release:        1%{?dist}
Summary:        MPRISv2 plugin for the DeaDBeeF music player

License:        GPLv3
URL:            https://github.com/Serranya/deadbeef-mpris2-plugin
Source0:        https://github.com/Serranya/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  deadbeef-devel
BuildRequires:  glib2-devel
BuildRequires:  libtool
Requires:       deadbeef

Obsoletes:      deadbeef-MPRIS-plugin

%description
This plugin aims to implement the MPRISv2 for DeaDBeeF.

The original MPRIS plugin for DeaDBeef does not work anymore and seems
to be orphaned. The original plugin supported MPRISv1 AND MPRISv2. This plugin
will only support version two.

%prep
%setup -q -n deadbeef-%{version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm %{buildroot}%{_libdir}/deadbeef/mpris.*a


%files
%doc
%{_libdir}/deadbeef/mpris.*


%changelog
* Wed May 27 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.8-1.R
- Initial release for fedora
