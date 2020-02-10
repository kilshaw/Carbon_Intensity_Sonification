# Carbon_Intensity_Sonification
Sonification of realtime carbon intensity, and fuel usage (percentage), regional UK.


UK regional Carbon Intensity FM Synthesiser. Simon Kilshaw
Carbon Intensity API. Sonification of energy consumption of biomass, coal, gas, nuclear, hydro, solar and wind, in different regions of the UK. 
Data retrieved 3rd February 2020 at 9.40am
Python, json, puredata. 

# How to use:
Run/ execute the python script. Launch puredata patch. 
The patch sends back regional requests from the radio button selector via UdpSend, 
and receives the pulled requests back from python via multiple  Udpreveice.

Some puredata dependencies: moocow, mrpeach


simon.kilshaw@uwtsd.ac.uk
