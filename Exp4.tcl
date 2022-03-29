#Create a simulator object
set ns [new simulator]
# Open trace files
set f [open out.tr w]
$ns trace-all $f
#open nam file
set nf [open out.nam w]
$ns namtrace-all $nf
#Define a 'finish' procedure
proc finish{} {
    global ns f nf
    $ns flush-trace
    close $f
    close $nf
    exec nam out.nam &
    exit 0
}
