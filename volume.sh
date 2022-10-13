#!/bin/bash

# Get Volume
get_volume() {
	status=`amixer -D pulse get Master | tail -n1 | grep -wo 'on'`

	if [[ "$status" == "on" ]]; then
		volume=`amixer -D pulse get Master | tail -n1 | awk -F ' ' '{print $5}' | tr -d '[%]'`
		echo "$volume"
	else
		echo "Mute"
	fi
}

# Get Mic
get_mic() {
	status=`amixer -D pulse get Capture | tail -n1 | grep -wo 'on'`

	if [[ "$status" == "on" ]]; then
		mic=`amixer -D pulse get Capture | tail -n1 | awk -F ' ' '{print $5}' | tr -d '[%]'`
		echo "$mic"
	else
		echo "0"
	fi
}

# Get icons
get_vol_icon() {
	vol="$(get_volume)"
	current="${vol%%%}"
	status=`amixer -D pulse get Master | tail -n1 | grep -wo 'on'`

	if [[ "$status" == "on" ]]; then
		if [[ "$current" -eq "0" ]]; then
			echo "images/icons/mute.png"
		elif [[ ("$current" -ge "0") && ("$current" -le "30") ]]; then
			echo "images/icons/volume.png"
		elif [[ ("$current" -ge "30") && ("$current" -le "60") ]]; then
			echo "images/icons/volume.png"
		elif [[ ("$current" -ge "60") && ("$current" -le "100") ]]; then
			echo "images/icons/volume.png"
		fi
	else
		echo "images/icons/mute.png"
	fi
}

# Get icons
get_mic_icon() {
	vol="$(get_mic)"
	current="${vol%%%}"
	status=`amixer -D pulse get Capture | tail -n1 | grep -wo 'on'`

	if [[ "$status" == "on" ]]; then
		if [[ "$current" -eq "0" ]]; then
			echo "images/icons/mute-mic.png"
		elif [[ ("$current" -ge "0") && ("$current" -le "30") ]]; then
			echo "images/icons/microphone.png"
		elif [[ ("$current" -ge "30") && ("$current" -le "60") ]]; then
			echo "images/icons/microphone.png"
		elif [[ ("$current" -ge "60") && ("$current" -le "100") ]]; then
			echo "images/icons/microphone.png"
		fi
	else
		echo "images/icons/mute-mic.png"
	fi
}

# Execute accordingly
if [[ "$1" == "--vol" ]]; then
	get_volume
elif [[ "$1" == "--vol-icon" ]]; then
	get_vol_icon
elif [[ "$1" == "--vol-tog" ]]; then
	amixer -D pulse set Master toggle
elif [[ "$1" == "--vol-set" ]]; then
	amixer -D pulse sset Master $2% unmute
elif [[ "$1" == "--mic" ]]; then
	get_mic
elif [[ "$1" == "--mic-icon" ]]; then
	get_mic_icon
elif [[ "$1" == "--mic-tog" ]]; then
	amixer -D pulse set Capture toggle
elif [[ "$1" == "--mic-set" ]]; then
	amixer -D pulse sset Capture $2% unmute
else
	get_volume
fi

