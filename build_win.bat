python -m venv env
call ./env/Scripts/activate.bat
pip install git+https://github.com/aforren1/mglg
pip install pyinstaller
pyinstaller jamboree_win.spec --noconfirm
cp Jamboree.cs dist/Jamboree.cs
cd dist
call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\Tools\VsDevCmd.bat"
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\VsDevCmd.bat"
csc.exe /target:winexe Jamboree.cs
dir
rm Jamboree.cs
cd ..
