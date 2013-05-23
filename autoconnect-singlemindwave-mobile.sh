echo Please put device in pairing mode and
echo immediately disconnect the first time you are connected
sudo bluetoothd 0000 
sudo bluetoothd restart
echo Auto-discovering the MindWave Mobile hardware address
ADDRESS=$(hcitool scan | grep -i mindwave | cut -f2)
echo Using address: $ADDRESS
echo =================================================================
echo  Establishing first time connection with address $ADDRESS 
echo  Please type Ctrl-C \(hangup\) if this succeeds.
echo =================================================================
sudo rfcomm connect rfcomm0 $ADDRESS
echo Releasing first time connection.
sudo rfcomm release /dev/rfcomm0
echo Restarting bluetooth daemon
sudo service bluetooth restart
sudo bluetoothd 0000 
sudo bluetoothd restart
echo Establishing second time connection with address $ADDRESS
echo Do not disconnect as long as you need it.
sudo rfcomm connect rfcomm0 $ADDRESS

