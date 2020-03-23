
"onedir" pyinstaller outside the directory (aka "libdir", sort of). 
See https://github.com/pyinstaller/pyinstaller/issues/1048, but that was recently closed.

Essentially, we go through the motions of using pyinstaller + onedir, then make a separate executable to launch the "real" executable. This makes pyinstaller happy (none of the paths change), and scripting ought to be straightforward enough.

This also tries to work out some of the trickier pyinstaller things (i.e. DLLs and other external files).

Notes:
 - Use a virtual environment to keep stuff clean/out of the bundled version
 - A batch file to launch the exe was fine, but less polished looking.
 - 

Pain points:
 - How do I find the right csc.exe? Is there even a right answer, or can I take the first one?
 - Discoverability of files within bundle is limited, but does that really matter?
 - Just remember that if using Anaconda, avoid the conda numpy (which brings in MKL, which is large).
 
## Steps (so far):

1. python -m venv env
2. '.\env\Scripts\activate.bat'
3. pip install git+https://github.com/aforren1/mglg
4. pip install pyinstaller
5. pyinstaller jamboree.spec
6. cp Jamboree.cs dist/Jamboree.cs && cd dist
7. C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /target:winexe Jamboree.cs
