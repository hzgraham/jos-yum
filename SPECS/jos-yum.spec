Name:		jos-yum
Version:	1.0.0
Release:	1%{?dist}
Summary:	Add JOS Repositories

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/hzgraham/jos-yum
Source0:	jos-yum.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	yum, yum-plugin-priorities


%description
Adds JOS's RPM Package Repositories and configures yum


%prep
%setup -q -c -n %{name}-src-base-%{version}


%build
echo "Build OK"

%install
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p $RPM_BUILD_ROOT/etc/cron.hourly
install -p -m 0755 JOS-Stable.repo $RPM_BUILD_ROOT/etc/yum.repos.d
install -p -m 0755 JOS-Unstable.repo $RPM_BUILD_ROOT/etc/yum.repos.d
install -p -m 0755 YUM-Update.sh $RPM_BUILD_ROOT/etc/cron.hourly

%post
clear

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/yum.repos.d/JOS-Stable.repo
/etc/yum.repos.d/JOS-Unstable.repo
/etc/cron.hourly/YUM-Update.sh


%changelog
* Sat Sep 7 2013 - hgraham@redhat.com
- Initial release
- RT3:207080
