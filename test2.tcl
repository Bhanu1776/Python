set ns [new Simulator]
set f [open out.tr w]
$ns trace-all $f
set nr [open out.nam w]
$ns namtrace-all $nr
proc finish {} {
	global ns f nr
	$ns flush-trace
	close $f
	close $nr
	exec nam out.nam &
	exit 0
}
set n0 [$ns node]
set n1 [$ns node]
$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns at 5.0 "finish"
$ns run
