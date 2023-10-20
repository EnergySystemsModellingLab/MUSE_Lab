*********
Name: Reference
Description: It represents how capacities would develop in case all technology costs (cap_par, fix_par), their performance in fuel consumption (CommIn.csv), their performance in emissions (CommOut.csv), and fuel prices (Projections.csv) remain the same as in 2020.
Carbon price: None (set to zero: CO2f, CH4, and N2O)
CapacityAddition: Technology investments limited for the older vehicle categories: no new Standard Efficiency or Medium Efficiency diesel and gasoline trucks (i.e., EURO I-IV) from 2025.
Solver: lpsolver = adhoc
Agents: 1
Objective: LCOE
*********


*********
Name: Efficiency
Description: It represents how capacities would develop in case all technology costs (cap_par, fix_par) and fuel prices (Projections.csv) remain the same as in 2020. Their performance in fuel consumption (CommIn.csv) and their performance in emissions (CommOut.csv) vary with time according to the efficiency improvements reported in the literature.
Carbon price: None (set to zero: CO2f, CH4, and N2O)
CapacityAddition: Technology investments limited for the older vehicle categories: no new Standard Efficiency or Medium Efficiency diesel and gasoline trucks (i.e., EURO I-IV) from 2025.
Solver: lpsolver = adhoc
Agents: 1
Objective: LCOE
*********

*********
Name: TechCosts
Description: It represents how capacities would develop in case fuel prices (Projections.csv) remain the same as in 2020. The technology costs (cap_par, fix_par), their performance in fuel consumption (CommIn.csv), and their performance in emissions (CommOut.csv) vary with time according to the efficiency improvements reported in the literature.
Carbon price: None (set to zero: CO2f, CH4, and N2O)
CapacityAddition: Technology investments limited for the older vehicle categories: no new Standard Efficiency or Medium Efficiency diesel and gasoline trucks (i.e., EURO I-IV) from 2025.
Solver: lpsolver = adhoc
Agents: 1
Objective: LCOE
*********

*********
Name: FuelProjections
Description: It represents how capacities would develop in case the technology costs (cap_par, fix_par), their performance in fuel consumption (CommIn.csv), and their performance in emissions (CommOut.csv) vary with time according to the efficiency improvements reported in the literature. Fuel prices are set to vary according to the projections reported in Projections.csv.
Carbon price: None (set to zero: CO2f, CH4, and N2O)
CapacityAddition: Technology investments limited for the older vehicle categories: no new Standard Efficiency or Medium Efficiency diesel and gasoline trucks (i.e., EURO I-IV) from 2025.
Solver: lpsolver = adhoc
Agents: 1
Objective: LCOE
*********

*********
Name: CarbonPrice
Description: It represents how capacities would develop in case the technology costs (cap_par, fix_par), their performance in fuel consumption (CommIn.csv), and their performance in emissions (CommOut.csv) vary with time according to the efficiency improvements reported in the literature. Fuel prices are set to vary according to the projections reported in Projections.csv.
Carbon price: Yes (CO2f, CH4, and N2O)
CapacityAddition: Technology investments limited for the older vehicle categories: no new Standard Efficiency or Medium Efficiency diesel and gasoline trucks (i.e., EURO I-IV) from 2025.
Solver: lpsolver = adhoc
Agents: 1
Objective: LCOE
*********

*********
Name: 2040ICEBan
Description: It represents how capacities would develop in case the technology costs (cap_par, fix_par), their performance in fuel consumption (CommIn.csv), and their performance in emissions (CommOut.csv) vary with time according to the efficiency improvements reported in the literature. Fuel prices are set to vary according to the projections reported in Projections.csv.
Carbon price: Yes (CO2f, CH4, and N2O)
CapacityAddition: Technology investments limited for the older vehicle categories: no new Standard Efficiency or Medium Efficiency diesel and gasoline trucks (i.e., EURO I-IV) from 2025. Ban on new ICE vehicles from 2040 onwards.
Solver: lpsolver = adhoc
Agents: 1
Objective: LCOE
*********

*********
Name: 2030ICEBan
Description: It represents how capacities would develop in case the technology costs (cap_par, fix_par), their performance in fuel consumption (CommIn.csv), and their performance in emissions (CommOut.csv) vary with time according to the efficiency improvements reported in the literature. Fuel prices are set to vary according to the projections reported in Projections.csv.
Carbon price: Yes (CO2f, CH4, and N2O)
CapacityAddition: Technology investments limited for the older vehicle categories: no new Standard Efficiency or Medium Efficiency diesel and gasoline trucks (i.e., EURO I-IV) from 2025. Ban on new ICE vehicles from 2030 onwards.
Solver: lpsolver = adhoc
Agents: 1
Objective: LCOE
*********