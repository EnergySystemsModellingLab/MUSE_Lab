*********
Name: BAU Scenario (alias "BAU_51" in the paper)
Description: It represents how capacities would develop in case all technology prices (cap_par, fix_par) and fuel prices (Projections.csv) remain the same as in 2020.
Carbon price: None (set to zero: CO2f - CommOut.csv)
Projections: Follow a 51% increase from base year 2020.
CapacityAddition: Not limited for all technologies
Solver: lpsolver = scipy
Agents: 1
Objective: LCOE
*********


*********
Name: Scenario 1 (alias "S1_51" in the paper)
Description: It represents how capacities would develop in case FOM technology costs (var_par), capital costs (cap_par) and fuel prices (Projections.csv) follow forecasted trends from 2020 to 2050.
Carbon price: None (set to zero: CO2f - CommOut.csv)
Projections: Follow a 51% increase from base year 2020.
CapacityAddition: Not limited for all technologies
Solver: lpsolver = scipy
Agents: 1
Objective: LCOE
*********

*********
Name: Scenario 2 (alias "S2_51" in the paper)
Description: It represents how capacities would develop in case FOM technology costs (var_par), capital costs (cap_par) and fuel prices (Projections.csv) follow forecasted trends from 2020 to 2050.
Carbon price: Yes (CO2f - CommOut.csv)
Projections: Follow a 51% increase from base year 2020.
CapacityAddition: Not limited for all technologies
Solver: lpsolver = scipy
Agents: 1
Objective: LCOE
*********

*********
Name: Scenario 3 (alias "S3_51" in the paper)
Description: It represents how capacities would develop in case FOM technology costs (var_par), capital costs (cap_par) and fuel prices (Projections.csv) follow forecasted trends from 2020 to 2050.
Carbon price: Yes (CO2f - CommOut.csv)
Projections: Follow a 17% increase from base year 2020.
CapacityAddition: Set to zero for gasoline, diesel, and hybrid cars from 2030 onwards. Set to zero for PHEV from 2040 onwards.
Solver: lpsolver = scipy
Agents: 1
Objective: LCOE
*********