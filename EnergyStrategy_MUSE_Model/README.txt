The folder demonstration-1 contains a three-sector, one-region MUSE model. The sectors modelled are supply, power, and residential.
Four cases are presented changing the agent population characteristics in the residential sector. 
Below, the corresponding TOML file of the four cases are presented: 
settings_SOS_37_Budget.TOML models a population where 30 % of consumers use as investment goal the levelised cost of energy (LCOE), whereas remaining 70 % of consumers use fuel consumption as investment goal; 
settings_SOS_73_Budget.TOML models a population where 70 % of consumers use as investment goal the levelised cost of energy (LCOE), whereas remaining 30 % of consumers use fuel consumption as investment goal;  
settings_SOS_LCOE_Budget.TOML models a population where 100 % of consumers use as investment goal the levelised cost of energy (LCOE); 
settings_SOS_FUEL_Budget.TOML models builds a population 100 % of consumers use fuel consumption as investment goal; 


The folder demonstration-2 contains a three-sector, one-region MUSE model. The sectors modelled are supply, power, and residential.
One case is presented with the population in the residential sector using equivalent annual cost (EAC) as investment goal. 
The TOML file (settings_SOS_EAC_budget.TOML) models a population in the residential sector where:
40 % of consumers have no limits on spending and can choose from all the technologies in the system; 
30 % of consumers can choose only technologies with a certain market share; 
and remaining 30 % of consumers have spending constraints.
