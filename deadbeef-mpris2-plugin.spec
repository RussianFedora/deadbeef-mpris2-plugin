Name:           deadbeef-mpris2-plugin
Version:        1.10
Release:        1%{?dist}
Summary:        MPRISv2 plugin for the DeaDBeeF music player

License:        GPLv3
URL:            https://github.com/Serranya/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  deadbeef-devel

Requires:       deadbeef%{?_isa}

%description
This plugin aims to implement the MPRISv2 for DeaDBeeF.

The original MPRIS plugin for DeaDBeef does not work anymore and seems
to be orphaned. The original plugin supported MPRISv1 AND MPRISv2. This plugin
will only support version two.

%prep
%autosetup -n deadbeef-%{version}


%build
%configure \
 --disable-silent-rules \
 --disable-static
%{make_build}


%install
%{make_install}
rm %{buildroot}%{_libdir}/deadbeef/mpris.*a


%files
%doc README
%{_libdir}/deadbeef/mpris.*


%changelog
* Tue May 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.10-1
- Update to latest release

* Wed May 27 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.8-1
- Initial release for fedora
