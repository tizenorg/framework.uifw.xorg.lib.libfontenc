# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       libfontenc
Summary:    X.Org X11 libfontenc runtime library
Version:    1.1.0
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source100:  libfontenc.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  zlib-devel
BuildRequires:  autoconf


%description
font encoding library


%package devel
Summary:    X.Org X11 libfontenc development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
font encoding library development package


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --with-encodingsdir=%{_datadir}/fonts/X11/encodings

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc COPYING README ChangeLog
%{_libdir}/libfontenc.so.1
%{_libdir}/libfontenc.so.1.0.0
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%dir %{_includedir}/X11
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/fontenc.h
%{_libdir}/libfontenc.so
%{_libdir}/pkgconfig/fontenc.pc
# << files devel

