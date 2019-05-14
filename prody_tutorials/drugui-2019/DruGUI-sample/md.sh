NAMD="/path/to/namd2 +p4"
cd md_min
$NAMD min.conf > min.log
cd ../md_sim
$NAMD eq1.conf > eq1.log
$NAMD eq2.conf > eq2.log
$NAMD eq3.conf > eq3.log
$NAMD sim.conf > sim.log
#$NAMD simrestart.conf > simrestart.log
