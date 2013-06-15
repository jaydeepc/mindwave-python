#!/bin/sh 
killall jackd
yoshimi -k -S./synthconfig/yoshimi.state &
python genconfig_linuxsampler.py
/usr/local/bin/qsampler ./synthconfig/linuxsampler.lscp &
qjackctl &
jack_connect LinuxSampler:0 system:playback_1
jack_connect LinuxSampler:1 system:playback_2



