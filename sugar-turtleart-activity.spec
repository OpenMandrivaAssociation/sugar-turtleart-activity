# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-turtleart-activity
Version: 210
Release: 1
Summary: Pseudo-Logo graphical programming language for Sugar
License: MIT
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/TurtleArt/TurtleBlocks-%{version}.tar.bz2

Requires: python-numpy  
Requires: python  
Requires: sugar-toolkit >= 0.88.0

BuildRequires: gettext  
BuildRequires: python-devel  
BuildRequires: sugar-toolkit >= 0.88.0

BuildArch: noarch

%description
Turtle Art is an activity with a Logo-inspired graphical "turtle"
that draws colorful art based on Scratch-like snap-together visual
programming elements.
There are many restrictions compared to LOGO. The two allowed user-defined
procedures can't have parameters. Only two numeric global variables
are available, no lists or other data-structures. You can't make user defined
functions which return a value. The conditionals and some of the functions
only take constants or variables, not expressions. Limited screen real-estate
makes building large programs unfeasible.

%prep
%setup -q -n TurtleBlocks-%{version}


%build

rm -f MANIFEST
python2 setup.py build

%install
python2 setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot} -name '*.py.orig' -print0 | xargs -0 rm -f
%find_lang org.laptop.TurtleArtActivity

%files -f org.laptop.TurtleArtActivity.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc NEWS



