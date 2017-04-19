# find . -mindepth 2 -maxdepth 2 -type d '!' -exec test -e "{}/main.fei" ';' -print


find . -type d -links 2 '!' -exec test -e "{}/main.fei" ';' -print
