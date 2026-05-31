\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{SCWorks}[2024/01/01 Saratov State University Course Work Class]

\LoadClass[14pt,a4paper]{extarticle}

\RequirePackage[utf8]{inputenc}
\RequirePackage[T2A]{fontenc}
\RequirePackage[russian]{babel}
\RequirePackage{amsmath,amsfonts,amssymb}
\RequirePackage{graphicx}
\RequirePackage{array}
\RequirePackage[left=30mm,right=15mm,top=20mm,bottom=20mm]{geometry}
\RequirePackage{titlesec}
\RequirePackage{setspace}
\RequirePackage{hyperref}
\RequirePackage{float}
\RequirePackage{caption}
\RequirePackage{enumitem}
\RequirePackage{minted}
\RequirePackage{xcolor}
\RequirePackage{indentfirst}

\setlength{\parindent}{1.25cm}
\onehalfspacing

\titleformat{\section}{\normalfont\bfseries\large}{\thesection}{1em}{}
\titleformat{\subsection}{\normalfont\bfseries\normalsize}{\thesubsection}{1em}{}

\hypersetup{
	colorlinks=true,
	linkcolor=blue,
	citecolor=blue,
	urlcolor=blue
}

\setminted{
	style=vs,
	fontsize=\small,
	breaklines=true,
	frame=single,
	framesep=5mm,
	tabsize=4
}

\addto\captionsrussian{\renewcommand{\figurename}{Рисунок}}
\addto\captionsrussian{\renewcommand{\tablename}{Таблица}}