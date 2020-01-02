#!/bin/sh

function start() {
  if [ -f /tmp/wol.pid ];then
    echo "wol is already running..."
    exit 1;
  fi
  echo "starting wol..."
  /usr/bin/env gunicorn -w 1 -b 0.0.0.0:50005 --threads 2 app:app --pid /tmp/wol.pid --daemon
  if [ -f /tmp/wol.pid ];then
    pid_num=`cat /tmp/wol.pid`
    echo "wol is running ${pid_num}..."
  fi
}

function stop() {
  if [ -f /tmp/wol.pid ];then
    echo "stopping wol..."
    cat /tmp/wol.pid | xargs kill -15
  else
    echo "wol is not running."
  fi
}

function status() {
  if [ -f /tmp/wol.pid ];then
    echo "wol is already running..."
  else
    echo "wol is not running..."
  fi
}

function help() {
  echo "input: ./wol.sh [start|stop|status|help]" >&2
  echo "                                 "
}

command=$1
case $command in
  start)
    start;
  ;;
  stop)
    stop;
	;;
  status)
    status;
	;;
	*)
    help;
		exit 1;
	;;
esac
