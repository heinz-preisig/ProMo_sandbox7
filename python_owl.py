

#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 Ontology design facility
===============================================================================

This program is part of the ProcessModelling suite

"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "16.09.2019"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "5.04"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"


import sys
import os

ProMo_path = os.path.join("../../","ProMo")



root = os.path.abspath(ProMo_path)      #os.path.join("../../"{{ProMo}}) #ProcessModeller_v7_04"))

ext = [root, os.path.join(root, 'packages'), \
             os.path.join(root, 'tasks'), \
             os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration')
       ]
# print(os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration'))

# emmo = "/home/heinz/1_Gits/ProcessModeller/ProcessModeller_v7_04/packages/OntologyBuilder/EMMO_Integration/"

sys.path.extend(ext)
from OntologyBuilder.EMMO_Integration.emmo_attach import ProMoOwlOntology
from Common.ontology_container import OntologyContainer

from owlready2 import *

ontology = OntologyContainer("ProMo_sandbox6") #'flash_03')


variables = ontology.variables

name = "play"
owlfile = name+".owl"

# onto  = O.setup_ontology(name)
o = ProMoOwlOntology()
onto = o.setupOnto()

with onto:
  class ProMoVar(onto.VAR):
    pass

  class has_function(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

  class function(Thing):
    domain  = [ProMoVar]
    range   = [ProMoVar]
    pass

  class is_function_of(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

# 1
label = variables[1]["label"]
network = variables[1]["network"]
variable_type = variables[1]["type"]
label = variables[1]["label"]
doc = variables[1]["doc"]
onto_ID = "V_1"
V_1 = onto.ProMoVar( onto_ID )
V_1.label = label
V_1.network = network
V_1.variable_type = variable_type
V_1.comment = doc

units = variables[1]["units"].asList()
V_1.time = [ units[0] ]
V_1.length = [ units[1] ]
V_1.amount = [ units[2] ]
V_1.mass = [ units[3] ]
V_1.temperature = [ units[4] ]
V_1.current = [ units[5] ]
V_1.light = [ units[6] ]

# 2
label = variables[2]["label"]
network = variables[2]["network"]
variable_type = variables[2]["type"]
label = variables[2]["label"]
doc = variables[2]["doc"]
onto_ID = "V_2"
V_2 = onto.ProMoVar( onto_ID )
V_2.label = label
V_2.network = network
V_2.variable_type = variable_type
V_2.comment = doc

units = variables[2]["units"].asList()
V_2.time = [ units[0] ]
V_2.length = [ units[1] ]
V_2.amount = [ units[2] ]
V_2.mass = [ units[3] ]
V_2.temperature = [ units[4] ]
V_2.current = [ units[5] ]
V_2.light = [ units[6] ]

# 3
label = variables[3]["label"]
network = variables[3]["network"]
variable_type = variables[3]["type"]
label = variables[3]["label"]
doc = variables[3]["doc"]
onto_ID = "V_3"
V_3 = onto.ProMoVar( onto_ID )
V_3.label = label
V_3.network = network
V_3.variable_type = variable_type
V_3.comment = doc

units = variables[3]["units"].asList()
V_3.time = [ units[0] ]
V_3.length = [ units[1] ]
V_3.amount = [ units[2] ]
V_3.mass = [ units[3] ]
V_3.temperature = [ units[4] ]
V_3.current = [ units[5] ]
V_3.light = [ units[6] ]

# 4
label = variables[4]["label"]
network = variables[4]["network"]
variable_type = variables[4]["type"]
label = variables[4]["label"]
doc = variables[4]["doc"]
onto_ID = "V_4"
V_4 = onto.ProMoVar( onto_ID )
V_4.label = label
V_4.network = network
V_4.variable_type = variable_type
V_4.comment = doc

units = variables[4]["units"].asList()
V_4.time = [ units[0] ]
V_4.length = [ units[1] ]
V_4.amount = [ units[2] ]
V_4.mass = [ units[3] ]
V_4.temperature = [ units[4] ]
V_4.current = [ units[5] ]
V_4.light = [ units[6] ]

# 5
label = variables[5]["label"]
network = variables[5]["network"]
variable_type = variables[5]["type"]
label = variables[5]["label"]
doc = variables[5]["doc"]
onto_ID = "V_5"
V_5 = onto.ProMoVar( onto_ID )
V_5.label = label
V_5.network = network
V_5.variable_type = variable_type
V_5.comment = doc

units = variables[5]["units"].asList()
V_5.time = [ units[0] ]
V_5.length = [ units[1] ]
V_5.amount = [ units[2] ]
V_5.mass = [ units[3] ]
V_5.temperature = [ units[4] ]
V_5.current = [ units[5] ]
V_5.light = [ units[6] ]

# 6
label = variables[6]["label"]
network = variables[6]["network"]
variable_type = variables[6]["type"]
label = variables[6]["label"]
doc = variables[6]["doc"]
onto_ID = "V_6"
V_6 = onto.ProMoVar( onto_ID )
V_6.label = label
V_6.network = network
V_6.variable_type = variable_type
V_6.comment = doc

units = variables[6]["units"].asList()
V_6.time = [ units[0] ]
V_6.length = [ units[1] ]
V_6.amount = [ units[2] ]
V_6.mass = [ units[3] ]
V_6.temperature = [ units[4] ]
V_6.current = [ units[5] ]
V_6.light = [ units[6] ]

# 7
label = variables[7]["label"]
network = variables[7]["network"]
variable_type = variables[7]["type"]
label = variables[7]["label"]
doc = variables[7]["doc"]
onto_ID = "V_7"
V_7 = onto.ProMoVar( onto_ID )
V_7.label = label
V_7.network = network
V_7.variable_type = variable_type
V_7.comment = doc

units = variables[7]["units"].asList()
V_7.time = [ units[0] ]
V_7.length = [ units[1] ]
V_7.amount = [ units[2] ]
V_7.mass = [ units[3] ]
V_7.temperature = [ units[4] ]
V_7.current = [ units[5] ]
V_7.light = [ units[6] ]

# 8
label = variables[8]["label"]
network = variables[8]["network"]
variable_type = variables[8]["type"]
label = variables[8]["label"]
doc = variables[8]["doc"]
onto_ID = "V_8"
V_8 = onto.ProMoVar( onto_ID )
V_8.label = label
V_8.network = network
V_8.variable_type = variable_type
V_8.comment = doc

units = variables[8]["units"].asList()
V_8.time = [ units[0] ]
V_8.length = [ units[1] ]
V_8.amount = [ units[2] ]
V_8.mass = [ units[3] ]
V_8.temperature = [ units[4] ]
V_8.current = [ units[5] ]
V_8.light = [ units[6] ]

# 9
label = variables[9]["label"]
network = variables[9]["network"]
variable_type = variables[9]["type"]
label = variables[9]["label"]
doc = variables[9]["doc"]
onto_ID = "V_9"
V_9 = onto.ProMoVar( onto_ID )
V_9.label = label
V_9.network = network
V_9.variable_type = variable_type
V_9.comment = doc

units = variables[9]["units"].asList()
V_9.time = [ units[0] ]
V_9.length = [ units[1] ]
V_9.amount = [ units[2] ]
V_9.mass = [ units[3] ]
V_9.temperature = [ units[4] ]
V_9.current = [ units[5] ]
V_9.light = [ units[6] ]

# 10
label = variables[10]["label"]
network = variables[10]["network"]
variable_type = variables[10]["type"]
label = variables[10]["label"]
doc = variables[10]["doc"]
onto_ID = "V_10"
V_10 = onto.ProMoVar( onto_ID )
V_10.label = label
V_10.network = network
V_10.variable_type = variable_type
V_10.comment = doc

units = variables[10]["units"].asList()
V_10.time = [ units[0] ]
V_10.length = [ units[1] ]
V_10.amount = [ units[2] ]
V_10.mass = [ units[3] ]
V_10.temperature = [ units[4] ]
V_10.current = [ units[5] ]
V_10.light = [ units[6] ]

# 11
label = variables[11]["label"]
network = variables[11]["network"]
variable_type = variables[11]["type"]
label = variables[11]["label"]
doc = variables[11]["doc"]
onto_ID = "V_11"
V_11 = onto.ProMoVar( onto_ID )
V_11.label = label
V_11.network = network
V_11.variable_type = variable_type
V_11.comment = doc

units = variables[11]["units"].asList()
V_11.time = [ units[0] ]
V_11.length = [ units[1] ]
V_11.amount = [ units[2] ]
V_11.mass = [ units[3] ]
V_11.temperature = [ units[4] ]
V_11.current = [ units[5] ]
V_11.light = [ units[6] ]

# 12
label = variables[12]["label"]
network = variables[12]["network"]
variable_type = variables[12]["type"]
label = variables[12]["label"]
doc = variables[12]["doc"]
onto_ID = "V_12"
V_12 = onto.ProMoVar( onto_ID )
V_12.label = label
V_12.network = network
V_12.variable_type = variable_type
V_12.comment = doc

units = variables[12]["units"].asList()
V_12.time = [ units[0] ]
V_12.length = [ units[1] ]
V_12.amount = [ units[2] ]
V_12.mass = [ units[3] ]
V_12.temperature = [ units[4] ]
V_12.current = [ units[5] ]
V_12.light = [ units[6] ]

# 13
label = variables[13]["label"]
network = variables[13]["network"]
variable_type = variables[13]["type"]
label = variables[13]["label"]
doc = variables[13]["doc"]
onto_ID = "V_13"
V_13 = onto.ProMoVar( onto_ID )
V_13.label = label
V_13.network = network
V_13.variable_type = variable_type
V_13.comment = doc

units = variables[13]["units"].asList()
V_13.time = [ units[0] ]
V_13.length = [ units[1] ]
V_13.amount = [ units[2] ]
V_13.mass = [ units[3] ]
V_13.temperature = [ units[4] ]
V_13.current = [ units[5] ]
V_13.light = [ units[6] ]

# 15
label = variables[15]["label"]
network = variables[15]["network"]
variable_type = variables[15]["type"]
label = variables[15]["label"]
doc = variables[15]["doc"]
onto_ID = "V_15"
V_15 = onto.ProMoVar( onto_ID )
V_15.label = label
V_15.network = network
V_15.variable_type = variable_type
V_15.comment = doc

units = variables[15]["units"].asList()
V_15.time = [ units[0] ]
V_15.length = [ units[1] ]
V_15.amount = [ units[2] ]
V_15.mass = [ units[3] ]
V_15.temperature = [ units[4] ]
V_15.current = [ units[5] ]
V_15.light = [ units[6] ]

# 16
label = variables[16]["label"]
network = variables[16]["network"]
variable_type = variables[16]["type"]
label = variables[16]["label"]
doc = variables[16]["doc"]
onto_ID = "V_16"
V_16 = onto.ProMoVar( onto_ID )
V_16.label = label
V_16.network = network
V_16.variable_type = variable_type
V_16.comment = doc

units = variables[16]["units"].asList()
V_16.time = [ units[0] ]
V_16.length = [ units[1] ]
V_16.amount = [ units[2] ]
V_16.mass = [ units[3] ]
V_16.temperature = [ units[4] ]
V_16.current = [ units[5] ]
V_16.light = [ units[6] ]

# 18
label = variables[18]["label"]
network = variables[18]["network"]
variable_type = variables[18]["type"]
label = variables[18]["label"]
doc = variables[18]["doc"]
onto_ID = "V_18"
V_18 = onto.ProMoVar( onto_ID )
V_18.label = label
V_18.network = network
V_18.variable_type = variable_type
V_18.comment = doc

units = variables[18]["units"].asList()
V_18.time = [ units[0] ]
V_18.length = [ units[1] ]
V_18.amount = [ units[2] ]
V_18.mass = [ units[3] ]
V_18.temperature = [ units[4] ]
V_18.current = [ units[5] ]
V_18.light = [ units[6] ]

# 19
label = variables[19]["label"]
network = variables[19]["network"]
variable_type = variables[19]["type"]
label = variables[19]["label"]
doc = variables[19]["doc"]
onto_ID = "V_19"
V_19 = onto.ProMoVar( onto_ID )
V_19.label = label
V_19.network = network
V_19.variable_type = variable_type
V_19.comment = doc

units = variables[19]["units"].asList()
V_19.time = [ units[0] ]
V_19.length = [ units[1] ]
V_19.amount = [ units[2] ]
V_19.mass = [ units[3] ]
V_19.temperature = [ units[4] ]
V_19.current = [ units[5] ]
V_19.light = [ units[6] ]

# 20
label = variables[20]["label"]
network = variables[20]["network"]
variable_type = variables[20]["type"]
label = variables[20]["label"]
doc = variables[20]["doc"]
onto_ID = "V_20"
V_20 = onto.ProMoVar( onto_ID )
V_20.label = label
V_20.network = network
V_20.variable_type = variable_type
V_20.comment = doc

units = variables[20]["units"].asList()
V_20.time = [ units[0] ]
V_20.length = [ units[1] ]
V_20.amount = [ units[2] ]
V_20.mass = [ units[3] ]
V_20.temperature = [ units[4] ]
V_20.current = [ units[5] ]
V_20.light = [ units[6] ]

# 21
label = variables[21]["label"]
network = variables[21]["network"]
variable_type = variables[21]["type"]
label = variables[21]["label"]
doc = variables[21]["doc"]
onto_ID = "V_21"
V_21 = onto.ProMoVar( onto_ID )
V_21.label = label
V_21.network = network
V_21.variable_type = variable_type
V_21.comment = doc

units = variables[21]["units"].asList()
V_21.time = [ units[0] ]
V_21.length = [ units[1] ]
V_21.amount = [ units[2] ]
V_21.mass = [ units[3] ]
V_21.temperature = [ units[4] ]
V_21.current = [ units[5] ]
V_21.light = [ units[6] ]

# 22
label = variables[22]["label"]
network = variables[22]["network"]
variable_type = variables[22]["type"]
label = variables[22]["label"]
doc = variables[22]["doc"]
onto_ID = "V_22"
V_22 = onto.ProMoVar( onto_ID )
V_22.label = label
V_22.network = network
V_22.variable_type = variable_type
V_22.comment = doc

units = variables[22]["units"].asList()
V_22.time = [ units[0] ]
V_22.length = [ units[1] ]
V_22.amount = [ units[2] ]
V_22.mass = [ units[3] ]
V_22.temperature = [ units[4] ]
V_22.current = [ units[5] ]
V_22.light = [ units[6] ]

# 23
label = variables[23]["label"]
network = variables[23]["network"]
variable_type = variables[23]["type"]
label = variables[23]["label"]
doc = variables[23]["doc"]
onto_ID = "V_23"
V_23 = onto.ProMoVar( onto_ID )
V_23.label = label
V_23.network = network
V_23.variable_type = variable_type
V_23.comment = doc

units = variables[23]["units"].asList()
V_23.time = [ units[0] ]
V_23.length = [ units[1] ]
V_23.amount = [ units[2] ]
V_23.mass = [ units[3] ]
V_23.temperature = [ units[4] ]
V_23.current = [ units[5] ]
V_23.light = [ units[6] ]

# 24
label = variables[24]["label"]
network = variables[24]["network"]
variable_type = variables[24]["type"]
label = variables[24]["label"]
doc = variables[24]["doc"]
onto_ID = "V_24"
V_24 = onto.ProMoVar( onto_ID )
V_24.label = label
V_24.network = network
V_24.variable_type = variable_type
V_24.comment = doc

units = variables[24]["units"].asList()
V_24.time = [ units[0] ]
V_24.length = [ units[1] ]
V_24.amount = [ units[2] ]
V_24.mass = [ units[3] ]
V_24.temperature = [ units[4] ]
V_24.current = [ units[5] ]
V_24.light = [ units[6] ]

# 25
label = variables[25]["label"]
network = variables[25]["network"]
variable_type = variables[25]["type"]
label = variables[25]["label"]
doc = variables[25]["doc"]
onto_ID = "V_25"
V_25 = onto.ProMoVar( onto_ID )
V_25.label = label
V_25.network = network
V_25.variable_type = variable_type
V_25.comment = doc

units = variables[25]["units"].asList()
V_25.time = [ units[0] ]
V_25.length = [ units[1] ]
V_25.amount = [ units[2] ]
V_25.mass = [ units[3] ]
V_25.temperature = [ units[4] ]
V_25.current = [ units[5] ]
V_25.light = [ units[6] ]

# 26
label = variables[26]["label"]
network = variables[26]["network"]
variable_type = variables[26]["type"]
label = variables[26]["label"]
doc = variables[26]["doc"]
onto_ID = "V_26"
V_26 = onto.ProMoVar( onto_ID )
V_26.label = label
V_26.network = network
V_26.variable_type = variable_type
V_26.comment = doc

units = variables[26]["units"].asList()
V_26.time = [ units[0] ]
V_26.length = [ units[1] ]
V_26.amount = [ units[2] ]
V_26.mass = [ units[3] ]
V_26.temperature = [ units[4] ]
V_26.current = [ units[5] ]
V_26.light = [ units[6] ]

# 27
label = variables[27]["label"]
network = variables[27]["network"]
variable_type = variables[27]["type"]
label = variables[27]["label"]
doc = variables[27]["doc"]
onto_ID = "V_27"
V_27 = onto.ProMoVar( onto_ID )
V_27.label = label
V_27.network = network
V_27.variable_type = variable_type
V_27.comment = doc

units = variables[27]["units"].asList()
V_27.time = [ units[0] ]
V_27.length = [ units[1] ]
V_27.amount = [ units[2] ]
V_27.mass = [ units[3] ]
V_27.temperature = [ units[4] ]
V_27.current = [ units[5] ]
V_27.light = [ units[6] ]

# 28
label = variables[28]["label"]
network = variables[28]["network"]
variable_type = variables[28]["type"]
label = variables[28]["label"]
doc = variables[28]["doc"]
onto_ID = "V_28"
V_28 = onto.ProMoVar( onto_ID )
V_28.label = label
V_28.network = network
V_28.variable_type = variable_type
V_28.comment = doc

units = variables[28]["units"].asList()
V_28.time = [ units[0] ]
V_28.length = [ units[1] ]
V_28.amount = [ units[2] ]
V_28.mass = [ units[3] ]
V_28.temperature = [ units[4] ]
V_28.current = [ units[5] ]
V_28.light = [ units[6] ]

# 29
label = variables[29]["label"]
network = variables[29]["network"]
variable_type = variables[29]["type"]
label = variables[29]["label"]
doc = variables[29]["doc"]
onto_ID = "V_29"
V_29 = onto.ProMoVar( onto_ID )
V_29.label = label
V_29.network = network
V_29.variable_type = variable_type
V_29.comment = doc

units = variables[29]["units"].asList()
V_29.time = [ units[0] ]
V_29.length = [ units[1] ]
V_29.amount = [ units[2] ]
V_29.mass = [ units[3] ]
V_29.temperature = [ units[4] ]
V_29.current = [ units[5] ]
V_29.light = [ units[6] ]

# 30
label = variables[30]["label"]
network = variables[30]["network"]
variable_type = variables[30]["type"]
label = variables[30]["label"]
doc = variables[30]["doc"]
onto_ID = "V_30"
V_30 = onto.ProMoVar( onto_ID )
V_30.label = label
V_30.network = network
V_30.variable_type = variable_type
V_30.comment = doc

units = variables[30]["units"].asList()
V_30.time = [ units[0] ]
V_30.length = [ units[1] ]
V_30.amount = [ units[2] ]
V_30.mass = [ units[3] ]
V_30.temperature = [ units[4] ]
V_30.current = [ units[5] ]
V_30.light = [ units[6] ]

# 31
label = variables[31]["label"]
network = variables[31]["network"]
variable_type = variables[31]["type"]
label = variables[31]["label"]
doc = variables[31]["doc"]
onto_ID = "V_31"
V_31 = onto.ProMoVar( onto_ID )
V_31.label = label
V_31.network = network
V_31.variable_type = variable_type
V_31.comment = doc

units = variables[31]["units"].asList()
V_31.time = [ units[0] ]
V_31.length = [ units[1] ]
V_31.amount = [ units[2] ]
V_31.mass = [ units[3] ]
V_31.temperature = [ units[4] ]
V_31.current = [ units[5] ]
V_31.light = [ units[6] ]

# 34
label = variables[34]["label"]
network = variables[34]["network"]
variable_type = variables[34]["type"]
label = variables[34]["label"]
doc = variables[34]["doc"]
onto_ID = "V_34"
V_34 = onto.ProMoVar( onto_ID )
V_34.label = label
V_34.network = network
V_34.variable_type = variable_type
V_34.comment = doc

units = variables[34]["units"].asList()
V_34.time = [ units[0] ]
V_34.length = [ units[1] ]
V_34.amount = [ units[2] ]
V_34.mass = [ units[3] ]
V_34.temperature = [ units[4] ]
V_34.current = [ units[5] ]
V_34.light = [ units[6] ]

# 35
label = variables[35]["label"]
network = variables[35]["network"]
variable_type = variables[35]["type"]
label = variables[35]["label"]
doc = variables[35]["doc"]
onto_ID = "V_35"
V_35 = onto.ProMoVar( onto_ID )
V_35.label = label
V_35.network = network
V_35.variable_type = variable_type
V_35.comment = doc

units = variables[35]["units"].asList()
V_35.time = [ units[0] ]
V_35.length = [ units[1] ]
V_35.amount = [ units[2] ]
V_35.mass = [ units[3] ]
V_35.temperature = [ units[4] ]
V_35.current = [ units[5] ]
V_35.light = [ units[6] ]

# 36
label = variables[36]["label"]
network = variables[36]["network"]
variable_type = variables[36]["type"]
label = variables[36]["label"]
doc = variables[36]["doc"]
onto_ID = "V_36"
V_36 = onto.ProMoVar( onto_ID )
V_36.label = label
V_36.network = network
V_36.variable_type = variable_type
V_36.comment = doc

units = variables[36]["units"].asList()
V_36.time = [ units[0] ]
V_36.length = [ units[1] ]
V_36.amount = [ units[2] ]
V_36.mass = [ units[3] ]
V_36.temperature = [ units[4] ]
V_36.current = [ units[5] ]
V_36.light = [ units[6] ]

# 37
label = variables[37]["label"]
network = variables[37]["network"]
variable_type = variables[37]["type"]
label = variables[37]["label"]
doc = variables[37]["doc"]
onto_ID = "V_37"
V_37 = onto.ProMoVar( onto_ID )
V_37.label = label
V_37.network = network
V_37.variable_type = variable_type
V_37.comment = doc

units = variables[37]["units"].asList()
V_37.time = [ units[0] ]
V_37.length = [ units[1] ]
V_37.amount = [ units[2] ]
V_37.mass = [ units[3] ]
V_37.temperature = [ units[4] ]
V_37.current = [ units[5] ]
V_37.light = [ units[6] ]

# 42
label = variables[42]["label"]
network = variables[42]["network"]
variable_type = variables[42]["type"]
label = variables[42]["label"]
doc = variables[42]["doc"]
onto_ID = "V_42"
V_42 = onto.ProMoVar( onto_ID )
V_42.label = label
V_42.network = network
V_42.variable_type = variable_type
V_42.comment = doc

units = variables[42]["units"].asList()
V_42.time = [ units[0] ]
V_42.length = [ units[1] ]
V_42.amount = [ units[2] ]
V_42.mass = [ units[3] ]
V_42.temperature = [ units[4] ]
V_42.current = [ units[5] ]
V_42.light = [ units[6] ]

# 45
label = variables[45]["label"]
network = variables[45]["network"]
variable_type = variables[45]["type"]
label = variables[45]["label"]
doc = variables[45]["doc"]
onto_ID = "V_45"
V_45 = onto.ProMoVar( onto_ID )
V_45.label = label
V_45.network = network
V_45.variable_type = variable_type
V_45.comment = doc

units = variables[45]["units"].asList()
V_45.time = [ units[0] ]
V_45.length = [ units[1] ]
V_45.amount = [ units[2] ]
V_45.mass = [ units[3] ]
V_45.temperature = [ units[4] ]
V_45.current = [ units[5] ]
V_45.light = [ units[6] ]

# 50
label = variables[50]["label"]
network = variables[50]["network"]
variable_type = variables[50]["type"]
label = variables[50]["label"]
doc = variables[50]["doc"]
onto_ID = "V_50"
V_50 = onto.ProMoVar( onto_ID )
V_50.label = label
V_50.network = network
V_50.variable_type = variable_type
V_50.comment = doc

units = variables[50]["units"].asList()
V_50.time = [ units[0] ]
V_50.length = [ units[1] ]
V_50.amount = [ units[2] ]
V_50.mass = [ units[3] ]
V_50.temperature = [ units[4] ]
V_50.current = [ units[5] ]
V_50.light = [ units[6] ]

# 51
label = variables[51]["label"]
network = variables[51]["network"]
variable_type = variables[51]["type"]
label = variables[51]["label"]
doc = variables[51]["doc"]
onto_ID = "V_51"
V_51 = onto.ProMoVar( onto_ID )
V_51.label = label
V_51.network = network
V_51.variable_type = variable_type
V_51.comment = doc

units = variables[51]["units"].asList()
V_51.time = [ units[0] ]
V_51.length = [ units[1] ]
V_51.amount = [ units[2] ]
V_51.mass = [ units[3] ]
V_51.temperature = [ units[4] ]
V_51.current = [ units[5] ]
V_51.light = [ units[6] ]

# 52
label = variables[52]["label"]
network = variables[52]["network"]
variable_type = variables[52]["type"]
label = variables[52]["label"]
doc = variables[52]["doc"]
onto_ID = "V_52"
V_52 = onto.ProMoVar( onto_ID )
V_52.label = label
V_52.network = network
V_52.variable_type = variable_type
V_52.comment = doc

units = variables[52]["units"].asList()
V_52.time = [ units[0] ]
V_52.length = [ units[1] ]
V_52.amount = [ units[2] ]
V_52.mass = [ units[3] ]
V_52.temperature = [ units[4] ]
V_52.current = [ units[5] ]
V_52.light = [ units[6] ]

# 53
label = variables[53]["label"]
network = variables[53]["network"]
variable_type = variables[53]["type"]
label = variables[53]["label"]
doc = variables[53]["doc"]
onto_ID = "V_53"
V_53 = onto.ProMoVar( onto_ID )
V_53.label = label
V_53.network = network
V_53.variable_type = variable_type
V_53.comment = doc

units = variables[53]["units"].asList()
V_53.time = [ units[0] ]
V_53.length = [ units[1] ]
V_53.amount = [ units[2] ]
V_53.mass = [ units[3] ]
V_53.temperature = [ units[4] ]
V_53.current = [ units[5] ]
V_53.light = [ units[6] ]

# 54
label = variables[54]["label"]
network = variables[54]["network"]
variable_type = variables[54]["type"]
label = variables[54]["label"]
doc = variables[54]["doc"]
onto_ID = "V_54"
V_54 = onto.ProMoVar( onto_ID )
V_54.label = label
V_54.network = network
V_54.variable_type = variable_type
V_54.comment = doc

units = variables[54]["units"].asList()
V_54.time = [ units[0] ]
V_54.length = [ units[1] ]
V_54.amount = [ units[2] ]
V_54.mass = [ units[3] ]
V_54.temperature = [ units[4] ]
V_54.current = [ units[5] ]
V_54.light = [ units[6] ]

# 55
label = variables[55]["label"]
network = variables[55]["network"]
variable_type = variables[55]["type"]
label = variables[55]["label"]
doc = variables[55]["doc"]
onto_ID = "V_55"
V_55 = onto.ProMoVar( onto_ID )
V_55.label = label
V_55.network = network
V_55.variable_type = variable_type
V_55.comment = doc

units = variables[55]["units"].asList()
V_55.time = [ units[0] ]
V_55.length = [ units[1] ]
V_55.amount = [ units[2] ]
V_55.mass = [ units[3] ]
V_55.temperature = [ units[4] ]
V_55.current = [ units[5] ]
V_55.light = [ units[6] ]

# 56
label = variables[56]["label"]
network = variables[56]["network"]
variable_type = variables[56]["type"]
label = variables[56]["label"]
doc = variables[56]["doc"]
onto_ID = "V_56"
V_56 = onto.ProMoVar( onto_ID )
V_56.label = label
V_56.network = network
V_56.variable_type = variable_type
V_56.comment = doc

units = variables[56]["units"].asList()
V_56.time = [ units[0] ]
V_56.length = [ units[1] ]
V_56.amount = [ units[2] ]
V_56.mass = [ units[3] ]
V_56.temperature = [ units[4] ]
V_56.current = [ units[5] ]
V_56.light = [ units[6] ]

# 57
label = variables[57]["label"]
network = variables[57]["network"]
variable_type = variables[57]["type"]
label = variables[57]["label"]
doc = variables[57]["doc"]
onto_ID = "V_57"
V_57 = onto.ProMoVar( onto_ID )
V_57.label = label
V_57.network = network
V_57.variable_type = variable_type
V_57.comment = doc

units = variables[57]["units"].asList()
V_57.time = [ units[0] ]
V_57.length = [ units[1] ]
V_57.amount = [ units[2] ]
V_57.mass = [ units[3] ]
V_57.temperature = [ units[4] ]
V_57.current = [ units[5] ]
V_57.light = [ units[6] ]

# 58
label = variables[58]["label"]
network = variables[58]["network"]
variable_type = variables[58]["type"]
label = variables[58]["label"]
doc = variables[58]["doc"]
onto_ID = "V_58"
V_58 = onto.ProMoVar( onto_ID )
V_58.label = label
V_58.network = network
V_58.variable_type = variable_type
V_58.comment = doc

units = variables[58]["units"].asList()
V_58.time = [ units[0] ]
V_58.length = [ units[1] ]
V_58.amount = [ units[2] ]
V_58.mass = [ units[3] ]
V_58.temperature = [ units[4] ]
V_58.current = [ units[5] ]
V_58.light = [ units[6] ]

# 59
label = variables[59]["label"]
network = variables[59]["network"]
variable_type = variables[59]["type"]
label = variables[59]["label"]
doc = variables[59]["doc"]
onto_ID = "V_59"
V_59 = onto.ProMoVar( onto_ID )
V_59.label = label
V_59.network = network
V_59.variable_type = variable_type
V_59.comment = doc

units = variables[59]["units"].asList()
V_59.time = [ units[0] ]
V_59.length = [ units[1] ]
V_59.amount = [ units[2] ]
V_59.mass = [ units[3] ]
V_59.temperature = [ units[4] ]
V_59.current = [ units[5] ]
V_59.light = [ units[6] ]

# 60
label = variables[60]["label"]
network = variables[60]["network"]
variable_type = variables[60]["type"]
label = variables[60]["label"]
doc = variables[60]["doc"]
onto_ID = "V_60"
V_60 = onto.ProMoVar( onto_ID )
V_60.label = label
V_60.network = network
V_60.variable_type = variable_type
V_60.comment = doc

units = variables[60]["units"].asList()
V_60.time = [ units[0] ]
V_60.length = [ units[1] ]
V_60.amount = [ units[2] ]
V_60.mass = [ units[3] ]
V_60.temperature = [ units[4] ]
V_60.current = [ units[5] ]
V_60.light = [ units[6] ]

# 61
label = variables[61]["label"]
network = variables[61]["network"]
variable_type = variables[61]["type"]
label = variables[61]["label"]
doc = variables[61]["doc"]
onto_ID = "V_61"
V_61 = onto.ProMoVar( onto_ID )
V_61.label = label
V_61.network = network
V_61.variable_type = variable_type
V_61.comment = doc

units = variables[61]["units"].asList()
V_61.time = [ units[0] ]
V_61.length = [ units[1] ]
V_61.amount = [ units[2] ]
V_61.mass = [ units[3] ]
V_61.temperature = [ units[4] ]
V_61.current = [ units[5] ]
V_61.light = [ units[6] ]

# 62
label = variables[62]["label"]
network = variables[62]["network"]
variable_type = variables[62]["type"]
label = variables[62]["label"]
doc = variables[62]["doc"]
onto_ID = "V_62"
V_62 = onto.ProMoVar( onto_ID )
V_62.label = label
V_62.network = network
V_62.variable_type = variable_type
V_62.comment = doc

units = variables[62]["units"].asList()
V_62.time = [ units[0] ]
V_62.length = [ units[1] ]
V_62.amount = [ units[2] ]
V_62.mass = [ units[3] ]
V_62.temperature = [ units[4] ]
V_62.current = [ units[5] ]
V_62.light = [ units[6] ]

# 63
label = variables[63]["label"]
network = variables[63]["network"]
variable_type = variables[63]["type"]
label = variables[63]["label"]
doc = variables[63]["doc"]
onto_ID = "V_63"
V_63 = onto.ProMoVar( onto_ID )
V_63.label = label
V_63.network = network
V_63.variable_type = variable_type
V_63.comment = doc

units = variables[63]["units"].asList()
V_63.time = [ units[0] ]
V_63.length = [ units[1] ]
V_63.amount = [ units[2] ]
V_63.mass = [ units[3] ]
V_63.temperature = [ units[4] ]
V_63.current = [ units[5] ]
V_63.light = [ units[6] ]

# 64
label = variables[64]["label"]
network = variables[64]["network"]
variable_type = variables[64]["type"]
label = variables[64]["label"]
doc = variables[64]["doc"]
onto_ID = "V_64"
V_64 = onto.ProMoVar( onto_ID )
V_64.label = label
V_64.network = network
V_64.variable_type = variable_type
V_64.comment = doc

units = variables[64]["units"].asList()
V_64.time = [ units[0] ]
V_64.length = [ units[1] ]
V_64.amount = [ units[2] ]
V_64.mass = [ units[3] ]
V_64.temperature = [ units[4] ]
V_64.current = [ units[5] ]
V_64.light = [ units[6] ]

# 65
label = variables[65]["label"]
network = variables[65]["network"]
variable_type = variables[65]["type"]
label = variables[65]["label"]
doc = variables[65]["doc"]
onto_ID = "V_65"
V_65 = onto.ProMoVar( onto_ID )
V_65.label = label
V_65.network = network
V_65.variable_type = variable_type
V_65.comment = doc

units = variables[65]["units"].asList()
V_65.time = [ units[0] ]
V_65.length = [ units[1] ]
V_65.amount = [ units[2] ]
V_65.mass = [ units[3] ]
V_65.temperature = [ units[4] ]
V_65.current = [ units[5] ]
V_65.light = [ units[6] ]

# 69
label = variables[69]["label"]
network = variables[69]["network"]
variable_type = variables[69]["type"]
label = variables[69]["label"]
doc = variables[69]["doc"]
onto_ID = "V_69"
V_69 = onto.ProMoVar( onto_ID )
V_69.label = label
V_69.network = network
V_69.variable_type = variable_type
V_69.comment = doc

units = variables[69]["units"].asList()
V_69.time = [ units[0] ]
V_69.length = [ units[1] ]
V_69.amount = [ units[2] ]
V_69.mass = [ units[3] ]
V_69.temperature = [ units[4] ]
V_69.current = [ units[5] ]
V_69.light = [ units[6] ]

# 71
label = variables[71]["label"]
network = variables[71]["network"]
variable_type = variables[71]["type"]
label = variables[71]["label"]
doc = variables[71]["doc"]
onto_ID = "V_71"
V_71 = onto.ProMoVar( onto_ID )
V_71.label = label
V_71.network = network
V_71.variable_type = variable_type
V_71.comment = doc

units = variables[71]["units"].asList()
V_71.time = [ units[0] ]
V_71.length = [ units[1] ]
V_71.amount = [ units[2] ]
V_71.mass = [ units[3] ]
V_71.temperature = [ units[4] ]
V_71.current = [ units[5] ]
V_71.light = [ units[6] ]

# 73
label = variables[73]["label"]
network = variables[73]["network"]
variable_type = variables[73]["type"]
label = variables[73]["label"]
doc = variables[73]["doc"]
onto_ID = "V_73"
V_73 = onto.ProMoVar( onto_ID )
V_73.label = label
V_73.network = network
V_73.variable_type = variable_type
V_73.comment = doc

units = variables[73]["units"].asList()
V_73.time = [ units[0] ]
V_73.length = [ units[1] ]
V_73.amount = [ units[2] ]
V_73.mass = [ units[3] ]
V_73.temperature = [ units[4] ]
V_73.current = [ units[5] ]
V_73.light = [ units[6] ]

# 77
label = variables[77]["label"]
network = variables[77]["network"]
variable_type = variables[77]["type"]
label = variables[77]["label"]
doc = variables[77]["doc"]
onto_ID = "V_77"
V_77 = onto.ProMoVar( onto_ID )
V_77.label = label
V_77.network = network
V_77.variable_type = variable_type
V_77.comment = doc

units = variables[77]["units"].asList()
V_77.time = [ units[0] ]
V_77.length = [ units[1] ]
V_77.amount = [ units[2] ]
V_77.mass = [ units[3] ]
V_77.temperature = [ units[4] ]
V_77.current = [ units[5] ]
V_77.light = [ units[6] ]

# 86
label = variables[86]["label"]
network = variables[86]["network"]
variable_type = variables[86]["type"]
label = variables[86]["label"]
doc = variables[86]["doc"]
onto_ID = "V_86"
V_86 = onto.ProMoVar( onto_ID )
V_86.label = label
V_86.network = network
V_86.variable_type = variable_type
V_86.comment = doc

units = variables[86]["units"].asList()
V_86.time = [ units[0] ]
V_86.length = [ units[1] ]
V_86.amount = [ units[2] ]
V_86.mass = [ units[3] ]
V_86.temperature = [ units[4] ]
V_86.current = [ units[5] ]
V_86.light = [ units[6] ]

# 87
label = variables[87]["label"]
network = variables[87]["network"]
variable_type = variables[87]["type"]
label = variables[87]["label"]
doc = variables[87]["doc"]
onto_ID = "V_87"
V_87 = onto.ProMoVar( onto_ID )
V_87.label = label
V_87.network = network
V_87.variable_type = variable_type
V_87.comment = doc

units = variables[87]["units"].asList()
V_87.time = [ units[0] ]
V_87.length = [ units[1] ]
V_87.amount = [ units[2] ]
V_87.mass = [ units[3] ]
V_87.temperature = [ units[4] ]
V_87.current = [ units[5] ]
V_87.light = [ units[6] ]

# 88
label = variables[88]["label"]
network = variables[88]["network"]
variable_type = variables[88]["type"]
label = variables[88]["label"]
doc = variables[88]["doc"]
onto_ID = "V_88"
V_88 = onto.ProMoVar( onto_ID )
V_88.label = label
V_88.network = network
V_88.variable_type = variable_type
V_88.comment = doc

units = variables[88]["units"].asList()
V_88.time = [ units[0] ]
V_88.length = [ units[1] ]
V_88.amount = [ units[2] ]
V_88.mass = [ units[3] ]
V_88.temperature = [ units[4] ]
V_88.current = [ units[5] ]
V_88.light = [ units[6] ]

# 89
label = variables[89]["label"]
network = variables[89]["network"]
variable_type = variables[89]["type"]
label = variables[89]["label"]
doc = variables[89]["doc"]
onto_ID = "V_89"
V_89 = onto.ProMoVar( onto_ID )
V_89.label = label
V_89.network = network
V_89.variable_type = variable_type
V_89.comment = doc

units = variables[89]["units"].asList()
V_89.time = [ units[0] ]
V_89.length = [ units[1] ]
V_89.amount = [ units[2] ]
V_89.mass = [ units[3] ]
V_89.temperature = [ units[4] ]
V_89.current = [ units[5] ]
V_89.light = [ units[6] ]

# 93
label = variables[93]["label"]
network = variables[93]["network"]
variable_type = variables[93]["type"]
label = variables[93]["label"]
doc = variables[93]["doc"]
onto_ID = "V_93"
V_93 = onto.ProMoVar( onto_ID )
V_93.label = label
V_93.network = network
V_93.variable_type = variable_type
V_93.comment = doc

units = variables[93]["units"].asList()
V_93.time = [ units[0] ]
V_93.length = [ units[1] ]
V_93.amount = [ units[2] ]
V_93.mass = [ units[3] ]
V_93.temperature = [ units[4] ]
V_93.current = [ units[5] ]
V_93.light = [ units[6] ]

# 95
label = variables[95]["label"]
network = variables[95]["network"]
variable_type = variables[95]["type"]
label = variables[95]["label"]
doc = variables[95]["doc"]
onto_ID = "V_95"
V_95 = onto.ProMoVar( onto_ID )
V_95.label = label
V_95.network = network
V_95.variable_type = variable_type
V_95.comment = doc

units = variables[95]["units"].asList()
V_95.time = [ units[0] ]
V_95.length = [ units[1] ]
V_95.amount = [ units[2] ]
V_95.mass = [ units[3] ]
V_95.temperature = [ units[4] ]
V_95.current = [ units[5] ]
V_95.light = [ units[6] ]

# 96
label = variables[96]["label"]
network = variables[96]["network"]
variable_type = variables[96]["type"]
label = variables[96]["label"]
doc = variables[96]["doc"]
onto_ID = "V_96"
V_96 = onto.ProMoVar( onto_ID )
V_96.label = label
V_96.network = network
V_96.variable_type = variable_type
V_96.comment = doc

units = variables[96]["units"].asList()
V_96.time = [ units[0] ]
V_96.length = [ units[1] ]
V_96.amount = [ units[2] ]
V_96.mass = [ units[3] ]
V_96.temperature = [ units[4] ]
V_96.current = [ units[5] ]
V_96.light = [ units[6] ]

# 97
label = variables[97]["label"]
network = variables[97]["network"]
variable_type = variables[97]["type"]
label = variables[97]["label"]
doc = variables[97]["doc"]
onto_ID = "V_97"
V_97 = onto.ProMoVar( onto_ID )
V_97.label = label
V_97.network = network
V_97.variable_type = variable_type
V_97.comment = doc

units = variables[97]["units"].asList()
V_97.time = [ units[0] ]
V_97.length = [ units[1] ]
V_97.amount = [ units[2] ]
V_97.mass = [ units[3] ]
V_97.temperature = [ units[4] ]
V_97.current = [ units[5] ]
V_97.light = [ units[6] ]

# 98
label = variables[98]["label"]
network = variables[98]["network"]
variable_type = variables[98]["type"]
label = variables[98]["label"]
doc = variables[98]["doc"]
onto_ID = "V_98"
V_98 = onto.ProMoVar( onto_ID )
V_98.label = label
V_98.network = network
V_98.variable_type = variable_type
V_98.comment = doc

units = variables[98]["units"].asList()
V_98.time = [ units[0] ]
V_98.length = [ units[1] ]
V_98.amount = [ units[2] ]
V_98.mass = [ units[3] ]
V_98.temperature = [ units[4] ]
V_98.current = [ units[5] ]
V_98.light = [ units[6] ]

# 104
label = variables[104]["label"]
network = variables[104]["network"]
variable_type = variables[104]["type"]
label = variables[104]["label"]
doc = variables[104]["doc"]
onto_ID = "V_104"
V_104 = onto.ProMoVar( onto_ID )
V_104.label = label
V_104.network = network
V_104.variable_type = variable_type
V_104.comment = doc

units = variables[104]["units"].asList()
V_104.time = [ units[0] ]
V_104.length = [ units[1] ]
V_104.amount = [ units[2] ]
V_104.mass = [ units[3] ]
V_104.temperature = [ units[4] ]
V_104.current = [ units[5] ]
V_104.light = [ units[6] ]

# 105
label = variables[105]["label"]
network = variables[105]["network"]
variable_type = variables[105]["type"]
label = variables[105]["label"]
doc = variables[105]["doc"]
onto_ID = "V_105"
V_105 = onto.ProMoVar( onto_ID )
V_105.label = label
V_105.network = network
V_105.variable_type = variable_type
V_105.comment = doc

units = variables[105]["units"].asList()
V_105.time = [ units[0] ]
V_105.length = [ units[1] ]
V_105.amount = [ units[2] ]
V_105.mass = [ units[3] ]
V_105.temperature = [ units[4] ]
V_105.current = [ units[5] ]
V_105.light = [ units[6] ]

# 106
label = variables[106]["label"]
network = variables[106]["network"]
variable_type = variables[106]["type"]
label = variables[106]["label"]
doc = variables[106]["doc"]
onto_ID = "V_106"
V_106 = onto.ProMoVar( onto_ID )
V_106.label = label
V_106.network = network
V_106.variable_type = variable_type
V_106.comment = doc

units = variables[106]["units"].asList()
V_106.time = [ units[0] ]
V_106.length = [ units[1] ]
V_106.amount = [ units[2] ]
V_106.mass = [ units[3] ]
V_106.temperature = [ units[4] ]
V_106.current = [ units[5] ]
V_106.light = [ units[6] ]

# 107
label = variables[107]["label"]
network = variables[107]["network"]
variable_type = variables[107]["type"]
label = variables[107]["label"]
doc = variables[107]["doc"]
onto_ID = "V_107"
V_107 = onto.ProMoVar( onto_ID )
V_107.label = label
V_107.network = network
V_107.variable_type = variable_type
V_107.comment = doc

units = variables[107]["units"].asList()
V_107.time = [ units[0] ]
V_107.length = [ units[1] ]
V_107.amount = [ units[2] ]
V_107.mass = [ units[3] ]
V_107.temperature = [ units[4] ]
V_107.current = [ units[5] ]
V_107.light = [ units[6] ]

# 108
label = variables[108]["label"]
network = variables[108]["network"]
variable_type = variables[108]["type"]
label = variables[108]["label"]
doc = variables[108]["doc"]
onto_ID = "V_108"
V_108 = onto.ProMoVar( onto_ID )
V_108.label = label
V_108.network = network
V_108.variable_type = variable_type
V_108.comment = doc

units = variables[108]["units"].asList()
V_108.time = [ units[0] ]
V_108.length = [ units[1] ]
V_108.amount = [ units[2] ]
V_108.mass = [ units[3] ]
V_108.temperature = [ units[4] ]
V_108.current = [ units[5] ]
V_108.light = [ units[6] ]

# 109
label = variables[109]["label"]
network = variables[109]["network"]
variable_type = variables[109]["type"]
label = variables[109]["label"]
doc = variables[109]["doc"]
onto_ID = "V_109"
V_109 = onto.ProMoVar( onto_ID )
V_109.label = label
V_109.network = network
V_109.variable_type = variable_type
V_109.comment = doc

units = variables[109]["units"].asList()
V_109.time = [ units[0] ]
V_109.length = [ units[1] ]
V_109.amount = [ units[2] ]
V_109.mass = [ units[3] ]
V_109.temperature = [ units[4] ]
V_109.current = [ units[5] ]
V_109.light = [ units[6] ]

# 110
label = variables[110]["label"]
network = variables[110]["network"]
variable_type = variables[110]["type"]
label = variables[110]["label"]
doc = variables[110]["doc"]
onto_ID = "V_110"
V_110 = onto.ProMoVar( onto_ID )
V_110.label = label
V_110.network = network
V_110.variable_type = variable_type
V_110.comment = doc

units = variables[110]["units"].asList()
V_110.time = [ units[0] ]
V_110.length = [ units[1] ]
V_110.amount = [ units[2] ]
V_110.mass = [ units[3] ]
V_110.temperature = [ units[4] ]
V_110.current = [ units[5] ]
V_110.light = [ units[6] ]

# 111
label = variables[111]["label"]
network = variables[111]["network"]
variable_type = variables[111]["type"]
label = variables[111]["label"]
doc = variables[111]["doc"]
onto_ID = "V_111"
V_111 = onto.ProMoVar( onto_ID )
V_111.label = label
V_111.network = network
V_111.variable_type = variable_type
V_111.comment = doc

units = variables[111]["units"].asList()
V_111.time = [ units[0] ]
V_111.length = [ units[1] ]
V_111.amount = [ units[2] ]
V_111.mass = [ units[3] ]
V_111.temperature = [ units[4] ]
V_111.current = [ units[5] ]
V_111.light = [ units[6] ]

# 114
label = variables[114]["label"]
network = variables[114]["network"]
variable_type = variables[114]["type"]
label = variables[114]["label"]
doc = variables[114]["doc"]
onto_ID = "V_114"
V_114 = onto.ProMoVar( onto_ID )
V_114.label = label
V_114.network = network
V_114.variable_type = variable_type
V_114.comment = doc

units = variables[114]["units"].asList()
V_114.time = [ units[0] ]
V_114.length = [ units[1] ]
V_114.amount = [ units[2] ]
V_114.mass = [ units[3] ]
V_114.temperature = [ units[4] ]
V_114.current = [ units[5] ]
V_114.light = [ units[6] ]

# 115
label = variables[115]["label"]
network = variables[115]["network"]
variable_type = variables[115]["type"]
label = variables[115]["label"]
doc = variables[115]["doc"]
onto_ID = "V_115"
V_115 = onto.ProMoVar( onto_ID )
V_115.label = label
V_115.network = network
V_115.variable_type = variable_type
V_115.comment = doc

units = variables[115]["units"].asList()
V_115.time = [ units[0] ]
V_115.length = [ units[1] ]
V_115.amount = [ units[2] ]
V_115.mass = [ units[3] ]
V_115.temperature = [ units[4] ]
V_115.current = [ units[5] ]
V_115.light = [ units[6] ]

# 116
label = variables[116]["label"]
network = variables[116]["network"]
variable_type = variables[116]["type"]
label = variables[116]["label"]
doc = variables[116]["doc"]
onto_ID = "V_116"
V_116 = onto.ProMoVar( onto_ID )
V_116.label = label
V_116.network = network
V_116.variable_type = variable_type
V_116.comment = doc

units = variables[116]["units"].asList()
V_116.time = [ units[0] ]
V_116.length = [ units[1] ]
V_116.amount = [ units[2] ]
V_116.mass = [ units[3] ]
V_116.temperature = [ units[4] ]
V_116.current = [ units[5] ]
V_116.light = [ units[6] ]

# 117
label = variables[117]["label"]
network = variables[117]["network"]
variable_type = variables[117]["type"]
label = variables[117]["label"]
doc = variables[117]["doc"]
onto_ID = "V_117"
V_117 = onto.ProMoVar( onto_ID )
V_117.label = label
V_117.network = network
V_117.variable_type = variable_type
V_117.comment = doc

units = variables[117]["units"].asList()
V_117.time = [ units[0] ]
V_117.length = [ units[1] ]
V_117.amount = [ units[2] ]
V_117.mass = [ units[3] ]
V_117.temperature = [ units[4] ]
V_117.current = [ units[5] ]
V_117.light = [ units[6] ]

# 118
label = variables[118]["label"]
network = variables[118]["network"]
variable_type = variables[118]["type"]
label = variables[118]["label"]
doc = variables[118]["doc"]
onto_ID = "V_118"
V_118 = onto.ProMoVar( onto_ID )
V_118.label = label
V_118.network = network
V_118.variable_type = variable_type
V_118.comment = doc

units = variables[118]["units"].asList()
V_118.time = [ units[0] ]
V_118.length = [ units[1] ]
V_118.amount = [ units[2] ]
V_118.mass = [ units[3] ]
V_118.temperature = [ units[4] ]
V_118.current = [ units[5] ]
V_118.light = [ units[6] ]

# 119
label = variables[119]["label"]
network = variables[119]["network"]
variable_type = variables[119]["type"]
label = variables[119]["label"]
doc = variables[119]["doc"]
onto_ID = "V_119"
V_119 = onto.ProMoVar( onto_ID )
V_119.label = label
V_119.network = network
V_119.variable_type = variable_type
V_119.comment = doc

units = variables[119]["units"].asList()
V_119.time = [ units[0] ]
V_119.length = [ units[1] ]
V_119.amount = [ units[2] ]
V_119.mass = [ units[3] ]
V_119.temperature = [ units[4] ]
V_119.current = [ units[5] ]
V_119.light = [ units[6] ]

# 120
label = variables[120]["label"]
network = variables[120]["network"]
variable_type = variables[120]["type"]
label = variables[120]["label"]
doc = variables[120]["doc"]
onto_ID = "V_120"
V_120 = onto.ProMoVar( onto_ID )
V_120.label = label
V_120.network = network
V_120.variable_type = variable_type
V_120.comment = doc

units = variables[120]["units"].asList()
V_120.time = [ units[0] ]
V_120.length = [ units[1] ]
V_120.amount = [ units[2] ]
V_120.mass = [ units[3] ]
V_120.temperature = [ units[4] ]
V_120.current = [ units[5] ]
V_120.light = [ units[6] ]

# 121
label = variables[121]["label"]
network = variables[121]["network"]
variable_type = variables[121]["type"]
label = variables[121]["label"]
doc = variables[121]["doc"]
onto_ID = "V_121"
V_121 = onto.ProMoVar( onto_ID )
V_121.label = label
V_121.network = network
V_121.variable_type = variable_type
V_121.comment = doc

units = variables[121]["units"].asList()
V_121.time = [ units[0] ]
V_121.length = [ units[1] ]
V_121.amount = [ units[2] ]
V_121.mass = [ units[3] ]
V_121.temperature = [ units[4] ]
V_121.current = [ units[5] ]
V_121.light = [ units[6] ]

# 122
label = variables[122]["label"]
network = variables[122]["network"]
variable_type = variables[122]["type"]
label = variables[122]["label"]
doc = variables[122]["doc"]
onto_ID = "V_122"
V_122 = onto.ProMoVar( onto_ID )
V_122.label = label
V_122.network = network
V_122.variable_type = variable_type
V_122.comment = doc

units = variables[122]["units"].asList()
V_122.time = [ units[0] ]
V_122.length = [ units[1] ]
V_122.amount = [ units[2] ]
V_122.mass = [ units[3] ]
V_122.temperature = [ units[4] ]
V_122.current = [ units[5] ]
V_122.light = [ units[6] ]

# 123
label = variables[123]["label"]
network = variables[123]["network"]
variable_type = variables[123]["type"]
label = variables[123]["label"]
doc = variables[123]["doc"]
onto_ID = "V_123"
V_123 = onto.ProMoVar( onto_ID )
V_123.label = label
V_123.network = network
V_123.variable_type = variable_type
V_123.comment = doc

units = variables[123]["units"].asList()
V_123.time = [ units[0] ]
V_123.length = [ units[1] ]
V_123.amount = [ units[2] ]
V_123.mass = [ units[3] ]
V_123.temperature = [ units[4] ]
V_123.current = [ units[5] ]
V_123.light = [ units[6] ]

# 124
label = variables[124]["label"]
network = variables[124]["network"]
variable_type = variables[124]["type"]
label = variables[124]["label"]
doc = variables[124]["doc"]
onto_ID = "V_124"
V_124 = onto.ProMoVar( onto_ID )
V_124.label = label
V_124.network = network
V_124.variable_type = variable_type
V_124.comment = doc

units = variables[124]["units"].asList()
V_124.time = [ units[0] ]
V_124.length = [ units[1] ]
V_124.amount = [ units[2] ]
V_124.mass = [ units[3] ]
V_124.temperature = [ units[4] ]
V_124.current = [ units[5] ]
V_124.light = [ units[6] ]

# 125
label = variables[125]["label"]
network = variables[125]["network"]
variable_type = variables[125]["type"]
label = variables[125]["label"]
doc = variables[125]["doc"]
onto_ID = "V_125"
V_125 = onto.ProMoVar( onto_ID )
V_125.label = label
V_125.network = network
V_125.variable_type = variable_type
V_125.comment = doc

units = variables[125]["units"].asList()
V_125.time = [ units[0] ]
V_125.length = [ units[1] ]
V_125.amount = [ units[2] ]
V_125.mass = [ units[3] ]
V_125.temperature = [ units[4] ]
V_125.current = [ units[5] ]
V_125.light = [ units[6] ]

# 126
label = variables[126]["label"]
network = variables[126]["network"]
variable_type = variables[126]["type"]
label = variables[126]["label"]
doc = variables[126]["doc"]
onto_ID = "V_126"
V_126 = onto.ProMoVar( onto_ID )
V_126.label = label
V_126.network = network
V_126.variable_type = variable_type
V_126.comment = doc

units = variables[126]["units"].asList()
V_126.time = [ units[0] ]
V_126.length = [ units[1] ]
V_126.amount = [ units[2] ]
V_126.mass = [ units[3] ]
V_126.temperature = [ units[4] ]
V_126.current = [ units[5] ]
V_126.light = [ units[6] ]

# 127
label = variables[127]["label"]
network = variables[127]["network"]
variable_type = variables[127]["type"]
label = variables[127]["label"]
doc = variables[127]["doc"]
onto_ID = "V_127"
V_127 = onto.ProMoVar( onto_ID )
V_127.label = label
V_127.network = network
V_127.variable_type = variable_type
V_127.comment = doc

units = variables[127]["units"].asList()
V_127.time = [ units[0] ]
V_127.length = [ units[1] ]
V_127.amount = [ units[2] ]
V_127.mass = [ units[3] ]
V_127.temperature = [ units[4] ]
V_127.current = [ units[5] ]
V_127.light = [ units[6] ]

# 128
label = variables[128]["label"]
network = variables[128]["network"]
variable_type = variables[128]["type"]
label = variables[128]["label"]
doc = variables[128]["doc"]
onto_ID = "V_128"
V_128 = onto.ProMoVar( onto_ID )
V_128.label = label
V_128.network = network
V_128.variable_type = variable_type
V_128.comment = doc

units = variables[128]["units"].asList()
V_128.time = [ units[0] ]
V_128.length = [ units[1] ]
V_128.amount = [ units[2] ]
V_128.mass = [ units[3] ]
V_128.temperature = [ units[4] ]
V_128.current = [ units[5] ]
V_128.light = [ units[6] ]

# 129
label = variables[129]["label"]
network = variables[129]["network"]
variable_type = variables[129]["type"]
label = variables[129]["label"]
doc = variables[129]["doc"]
onto_ID = "V_129"
V_129 = onto.ProMoVar( onto_ID )
V_129.label = label
V_129.network = network
V_129.variable_type = variable_type
V_129.comment = doc

units = variables[129]["units"].asList()
V_129.time = [ units[0] ]
V_129.length = [ units[1] ]
V_129.amount = [ units[2] ]
V_129.mass = [ units[3] ]
V_129.temperature = [ units[4] ]
V_129.current = [ units[5] ]
V_129.light = [ units[6] ]

# 130
label = variables[130]["label"]
network = variables[130]["network"]
variable_type = variables[130]["type"]
label = variables[130]["label"]
doc = variables[130]["doc"]
onto_ID = "V_130"
V_130 = onto.ProMoVar( onto_ID )
V_130.label = label
V_130.network = network
V_130.variable_type = variable_type
V_130.comment = doc

units = variables[130]["units"].asList()
V_130.time = [ units[0] ]
V_130.length = [ units[1] ]
V_130.amount = [ units[2] ]
V_130.mass = [ units[3] ]
V_130.temperature = [ units[4] ]
V_130.current = [ units[5] ]
V_130.light = [ units[6] ]

# 133
label = variables[133]["label"]
network = variables[133]["network"]
variable_type = variables[133]["type"]
label = variables[133]["label"]
doc = variables[133]["doc"]
onto_ID = "V_133"
V_133 = onto.ProMoVar( onto_ID )
V_133.label = label
V_133.network = network
V_133.variable_type = variable_type
V_133.comment = doc

units = variables[133]["units"].asList()
V_133.time = [ units[0] ]
V_133.length = [ units[1] ]
V_133.amount = [ units[2] ]
V_133.mass = [ units[3] ]
V_133.temperature = [ units[4] ]
V_133.current = [ units[5] ]
V_133.light = [ units[6] ]

# 134
label = variables[134]["label"]
network = variables[134]["network"]
variable_type = variables[134]["type"]
label = variables[134]["label"]
doc = variables[134]["doc"]
onto_ID = "V_134"
V_134 = onto.ProMoVar( onto_ID )
V_134.label = label
V_134.network = network
V_134.variable_type = variable_type
V_134.comment = doc

units = variables[134]["units"].asList()
V_134.time = [ units[0] ]
V_134.length = [ units[1] ]
V_134.amount = [ units[2] ]
V_134.mass = [ units[3] ]
V_134.temperature = [ units[4] ]
V_134.current = [ units[5] ]
V_134.light = [ units[6] ]

# 135
label = variables[135]["label"]
network = variables[135]["network"]
variable_type = variables[135]["type"]
label = variables[135]["label"]
doc = variables[135]["doc"]
onto_ID = "V_135"
V_135 = onto.ProMoVar( onto_ID )
V_135.label = label
V_135.network = network
V_135.variable_type = variable_type
V_135.comment = doc

units = variables[135]["units"].asList()
V_135.time = [ units[0] ]
V_135.length = [ units[1] ]
V_135.amount = [ units[2] ]
V_135.mass = [ units[3] ]
V_135.temperature = [ units[4] ]
V_135.current = [ units[5] ]
V_135.light = [ units[6] ]

# 136
label = variables[136]["label"]
network = variables[136]["network"]
variable_type = variables[136]["type"]
label = variables[136]["label"]
doc = variables[136]["doc"]
onto_ID = "V_136"
V_136 = onto.ProMoVar( onto_ID )
V_136.label = label
V_136.network = network
V_136.variable_type = variable_type
V_136.comment = doc

units = variables[136]["units"].asList()
V_136.time = [ units[0] ]
V_136.length = [ units[1] ]
V_136.amount = [ units[2] ]
V_136.mass = [ units[3] ]
V_136.temperature = [ units[4] ]
V_136.current = [ units[5] ]
V_136.light = [ units[6] ]

# 137
label = variables[137]["label"]
network = variables[137]["network"]
variable_type = variables[137]["type"]
label = variables[137]["label"]
doc = variables[137]["doc"]
onto_ID = "V_137"
V_137 = onto.ProMoVar( onto_ID )
V_137.label = label
V_137.network = network
V_137.variable_type = variable_type
V_137.comment = doc

units = variables[137]["units"].asList()
V_137.time = [ units[0] ]
V_137.length = [ units[1] ]
V_137.amount = [ units[2] ]
V_137.mass = [ units[3] ]
V_137.temperature = [ units[4] ]
V_137.current = [ units[5] ]
V_137.light = [ units[6] ]

# 138
label = variables[138]["label"]
network = variables[138]["network"]
variable_type = variables[138]["type"]
label = variables[138]["label"]
doc = variables[138]["doc"]
onto_ID = "V_138"
V_138 = onto.ProMoVar( onto_ID )
V_138.label = label
V_138.network = network
V_138.variable_type = variable_type
V_138.comment = doc

units = variables[138]["units"].asList()
V_138.time = [ units[0] ]
V_138.length = [ units[1] ]
V_138.amount = [ units[2] ]
V_138.mass = [ units[3] ]
V_138.temperature = [ units[4] ]
V_138.current = [ units[5] ]
V_138.light = [ units[6] ]

# 139
label = variables[139]["label"]
network = variables[139]["network"]
variable_type = variables[139]["type"]
label = variables[139]["label"]
doc = variables[139]["doc"]
onto_ID = "V_139"
V_139 = onto.ProMoVar( onto_ID )
V_139.label = label
V_139.network = network
V_139.variable_type = variable_type
V_139.comment = doc

units = variables[139]["units"].asList()
V_139.time = [ units[0] ]
V_139.length = [ units[1] ]
V_139.amount = [ units[2] ]
V_139.mass = [ units[3] ]
V_139.temperature = [ units[4] ]
V_139.current = [ units[5] ]
V_139.light = [ units[6] ]

# 140
label = variables[140]["label"]
network = variables[140]["network"]
variable_type = variables[140]["type"]
label = variables[140]["label"]
doc = variables[140]["doc"]
onto_ID = "V_140"
V_140 = onto.ProMoVar( onto_ID )
V_140.label = label
V_140.network = network
V_140.variable_type = variable_type
V_140.comment = doc

units = variables[140]["units"].asList()
V_140.time = [ units[0] ]
V_140.length = [ units[1] ]
V_140.amount = [ units[2] ]
V_140.mass = [ units[3] ]
V_140.temperature = [ units[4] ]
V_140.current = [ units[5] ]
V_140.light = [ units[6] ]

# 142
label = variables[142]["label"]
network = variables[142]["network"]
variable_type = variables[142]["type"]
label = variables[142]["label"]
doc = variables[142]["doc"]
onto_ID = "V_142"
V_142 = onto.ProMoVar( onto_ID )
V_142.label = label
V_142.network = network
V_142.variable_type = variable_type
V_142.comment = doc

units = variables[142]["units"].asList()
V_142.time = [ units[0] ]
V_142.length = [ units[1] ]
V_142.amount = [ units[2] ]
V_142.mass = [ units[3] ]
V_142.temperature = [ units[4] ]
V_142.current = [ units[5] ]
V_142.light = [ units[6] ]

# 143
label = variables[143]["label"]
network = variables[143]["network"]
variable_type = variables[143]["type"]
label = variables[143]["label"]
doc = variables[143]["doc"]
onto_ID = "V_143"
V_143 = onto.ProMoVar( onto_ID )
V_143.label = label
V_143.network = network
V_143.variable_type = variable_type
V_143.comment = doc

units = variables[143]["units"].asList()
V_143.time = [ units[0] ]
V_143.length = [ units[1] ]
V_143.amount = [ units[2] ]
V_143.mass = [ units[3] ]
V_143.temperature = [ units[4] ]
V_143.current = [ units[5] ]
V_143.light = [ units[6] ]

# 144
label = variables[144]["label"]
network = variables[144]["network"]
variable_type = variables[144]["type"]
label = variables[144]["label"]
doc = variables[144]["doc"]
onto_ID = "V_144"
V_144 = onto.ProMoVar( onto_ID )
V_144.label = label
V_144.network = network
V_144.variable_type = variable_type
V_144.comment = doc

units = variables[144]["units"].asList()
V_144.time = [ units[0] ]
V_144.length = [ units[1] ]
V_144.amount = [ units[2] ]
V_144.mass = [ units[3] ]
V_144.temperature = [ units[4] ]
V_144.current = [ units[5] ]
V_144.light = [ units[6] ]

# 145
label = variables[145]["label"]
network = variables[145]["network"]
variable_type = variables[145]["type"]
label = variables[145]["label"]
doc = variables[145]["doc"]
onto_ID = "V_145"
V_145 = onto.ProMoVar( onto_ID )
V_145.label = label
V_145.network = network
V_145.variable_type = variable_type
V_145.comment = doc

units = variables[145]["units"].asList()
V_145.time = [ units[0] ]
V_145.length = [ units[1] ]
V_145.amount = [ units[2] ]
V_145.mass = [ units[3] ]
V_145.temperature = [ units[4] ]
V_145.current = [ units[5] ]
V_145.light = [ units[6] ]

# 148
label = variables[148]["label"]
network = variables[148]["network"]
variable_type = variables[148]["type"]
label = variables[148]["label"]
doc = variables[148]["doc"]
onto_ID = "V_148"
V_148 = onto.ProMoVar( onto_ID )
V_148.label = label
V_148.network = network
V_148.variable_type = variable_type
V_148.comment = doc

units = variables[148]["units"].asList()
V_148.time = [ units[0] ]
V_148.length = [ units[1] ]
V_148.amount = [ units[2] ]
V_148.mass = [ units[3] ]
V_148.temperature = [ units[4] ]
V_148.current = [ units[5] ]
V_148.light = [ units[6] ]

# 149
label = variables[149]["label"]
network = variables[149]["network"]
variable_type = variables[149]["type"]
label = variables[149]["label"]
doc = variables[149]["doc"]
onto_ID = "V_149"
V_149 = onto.ProMoVar( onto_ID )
V_149.label = label
V_149.network = network
V_149.variable_type = variable_type
V_149.comment = doc

units = variables[149]["units"].asList()
V_149.time = [ units[0] ]
V_149.length = [ units[1] ]
V_149.amount = [ units[2] ]
V_149.mass = [ units[3] ]
V_149.temperature = [ units[4] ]
V_149.current = [ units[5] ]
V_149.light = [ units[6] ]

# 150
label = variables[150]["label"]
network = variables[150]["network"]
variable_type = variables[150]["type"]
label = variables[150]["label"]
doc = variables[150]["doc"]
onto_ID = "V_150"
V_150 = onto.ProMoVar( onto_ID )
V_150.label = label
V_150.network = network
V_150.variable_type = variable_type
V_150.comment = doc

units = variables[150]["units"].asList()
V_150.time = [ units[0] ]
V_150.length = [ units[1] ]
V_150.amount = [ units[2] ]
V_150.mass = [ units[3] ]
V_150.temperature = [ units[4] ]
V_150.current = [ units[5] ]
V_150.light = [ units[6] ]

# 151
label = variables[151]["label"]
network = variables[151]["network"]
variable_type = variables[151]["type"]
label = variables[151]["label"]
doc = variables[151]["doc"]
onto_ID = "V_151"
V_151 = onto.ProMoVar( onto_ID )
V_151.label = label
V_151.network = network
V_151.variable_type = variable_type
V_151.comment = doc

units = variables[151]["units"].asList()
V_151.time = [ units[0] ]
V_151.length = [ units[1] ]
V_151.amount = [ units[2] ]
V_151.mass = [ units[3] ]
V_151.temperature = [ units[4] ]
V_151.current = [ units[5] ]
V_151.light = [ units[6] ]

# 152
label = variables[152]["label"]
network = variables[152]["network"]
variable_type = variables[152]["type"]
label = variables[152]["label"]
doc = variables[152]["doc"]
onto_ID = "V_152"
V_152 = onto.ProMoVar( onto_ID )
V_152.label = label
V_152.network = network
V_152.variable_type = variable_type
V_152.comment = doc

units = variables[152]["units"].asList()
V_152.time = [ units[0] ]
V_152.length = [ units[1] ]
V_152.amount = [ units[2] ]
V_152.mass = [ units[3] ]
V_152.temperature = [ units[4] ]
V_152.current = [ units[5] ]
V_152.light = [ units[6] ]

# 153
label = variables[153]["label"]
network = variables[153]["network"]
variable_type = variables[153]["type"]
label = variables[153]["label"]
doc = variables[153]["doc"]
onto_ID = "V_153"
V_153 = onto.ProMoVar( onto_ID )
V_153.label = label
V_153.network = network
V_153.variable_type = variable_type
V_153.comment = doc

units = variables[153]["units"].asList()
V_153.time = [ units[0] ]
V_153.length = [ units[1] ]
V_153.amount = [ units[2] ]
V_153.mass = [ units[3] ]
V_153.temperature = [ units[4] ]
V_153.current = [ units[5] ]
V_153.light = [ units[6] ]

# 154
label = variables[154]["label"]
network = variables[154]["network"]
variable_type = variables[154]["type"]
label = variables[154]["label"]
doc = variables[154]["doc"]
onto_ID = "V_154"
V_154 = onto.ProMoVar( onto_ID )
V_154.label = label
V_154.network = network
V_154.variable_type = variable_type
V_154.comment = doc

units = variables[154]["units"].asList()
V_154.time = [ units[0] ]
V_154.length = [ units[1] ]
V_154.amount = [ units[2] ]
V_154.mass = [ units[3] ]
V_154.temperature = [ units[4] ]
V_154.current = [ units[5] ]
V_154.light = [ units[6] ]

# 155
label = variables[155]["label"]
network = variables[155]["network"]
variable_type = variables[155]["type"]
label = variables[155]["label"]
doc = variables[155]["doc"]
onto_ID = "V_155"
V_155 = onto.ProMoVar( onto_ID )
V_155.label = label
V_155.network = network
V_155.variable_type = variable_type
V_155.comment = doc

units = variables[155]["units"].asList()
V_155.time = [ units[0] ]
V_155.length = [ units[1] ]
V_155.amount = [ units[2] ]
V_155.mass = [ units[3] ]
V_155.temperature = [ units[4] ]
V_155.current = [ units[5] ]
V_155.light = [ units[6] ]

# 158
label = variables[158]["label"]
network = variables[158]["network"]
variable_type = variables[158]["type"]
label = variables[158]["label"]
doc = variables[158]["doc"]
onto_ID = "V_158"
V_158 = onto.ProMoVar( onto_ID )
V_158.label = label
V_158.network = network
V_158.variable_type = variable_type
V_158.comment = doc

units = variables[158]["units"].asList()
V_158.time = [ units[0] ]
V_158.length = [ units[1] ]
V_158.amount = [ units[2] ]
V_158.mass = [ units[3] ]
V_158.temperature = [ units[4] ]
V_158.current = [ units[5] ]
V_158.light = [ units[6] ]

# 161
label = variables[161]["label"]
network = variables[161]["network"]
variable_type = variables[161]["type"]
label = variables[161]["label"]
doc = variables[161]["doc"]
onto_ID = "V_161"
V_161 = onto.ProMoVar( onto_ID )
V_161.label = label
V_161.network = network
V_161.variable_type = variable_type
V_161.comment = doc

units = variables[161]["units"].asList()
V_161.time = [ units[0] ]
V_161.length = [ units[1] ]
V_161.amount = [ units[2] ]
V_161.mass = [ units[3] ]
V_161.temperature = [ units[4] ]
V_161.current = [ units[5] ]
V_161.light = [ units[6] ]

# 164
label = variables[164]["label"]
network = variables[164]["network"]
variable_type = variables[164]["type"]
label = variables[164]["label"]
doc = variables[164]["doc"]
onto_ID = "V_164"
V_164 = onto.ProMoVar( onto_ID )
V_164.label = label
V_164.network = network
V_164.variable_type = variable_type
V_164.comment = doc

units = variables[164]["units"].asList()
V_164.time = [ units[0] ]
V_164.length = [ units[1] ]
V_164.amount = [ units[2] ]
V_164.mass = [ units[3] ]
V_164.temperature = [ units[4] ]
V_164.current = [ units[5] ]
V_164.light = [ units[6] ]

# 165
label = variables[165]["label"]
network = variables[165]["network"]
variable_type = variables[165]["type"]
label = variables[165]["label"]
doc = variables[165]["doc"]
onto_ID = "V_165"
V_165 = onto.ProMoVar( onto_ID )
V_165.label = label
V_165.network = network
V_165.variable_type = variable_type
V_165.comment = doc

units = variables[165]["units"].asList()
V_165.time = [ units[0] ]
V_165.length = [ units[1] ]
V_165.amount = [ units[2] ]
V_165.mass = [ units[3] ]
V_165.temperature = [ units[4] ]
V_165.current = [ units[5] ]
V_165.light = [ units[6] ]

# 166
label = variables[166]["label"]
network = variables[166]["network"]
variable_type = variables[166]["type"]
label = variables[166]["label"]
doc = variables[166]["doc"]
onto_ID = "V_166"
V_166 = onto.ProMoVar( onto_ID )
V_166.label = label
V_166.network = network
V_166.variable_type = variable_type
V_166.comment = doc

units = variables[166]["units"].asList()
V_166.time = [ units[0] ]
V_166.length = [ units[1] ]
V_166.amount = [ units[2] ]
V_166.mass = [ units[3] ]
V_166.temperature = [ units[4] ]
V_166.current = [ units[5] ]
V_166.light = [ units[6] ]

# 168
label = variables[168]["label"]
network = variables[168]["network"]
variable_type = variables[168]["type"]
label = variables[168]["label"]
doc = variables[168]["doc"]
onto_ID = "V_168"
V_168 = onto.ProMoVar( onto_ID )
V_168.label = label
V_168.network = network
V_168.variable_type = variable_type
V_168.comment = doc

units = variables[168]["units"].asList()
V_168.time = [ units[0] ]
V_168.length = [ units[1] ]
V_168.amount = [ units[2] ]
V_168.mass = [ units[3] ]
V_168.temperature = [ units[4] ]
V_168.current = [ units[5] ]
V_168.light = [ units[6] ]

# 170
label = variables[170]["label"]
network = variables[170]["network"]
variable_type = variables[170]["type"]
label = variables[170]["label"]
doc = variables[170]["doc"]
onto_ID = "V_170"
V_170 = onto.ProMoVar( onto_ID )
V_170.label = label
V_170.network = network
V_170.variable_type = variable_type
V_170.comment = doc

units = variables[170]["units"].asList()
V_170.time = [ units[0] ]
V_170.length = [ units[1] ]
V_170.amount = [ units[2] ]
V_170.mass = [ units[3] ]
V_170.temperature = [ units[4] ]
V_170.current = [ units[5] ]
V_170.light = [ units[6] ]

# 175
label = variables[175]["label"]
network = variables[175]["network"]
variable_type = variables[175]["type"]
label = variables[175]["label"]
doc = variables[175]["doc"]
onto_ID = "V_175"
V_175 = onto.ProMoVar( onto_ID )
V_175.label = label
V_175.network = network
V_175.variable_type = variable_type
V_175.comment = doc

units = variables[175]["units"].asList()
V_175.time = [ units[0] ]
V_175.length = [ units[1] ]
V_175.amount = [ units[2] ]
V_175.mass = [ units[3] ]
V_175.temperature = [ units[4] ]
V_175.current = [ units[5] ]
V_175.light = [ units[6] ]

# 177
label = variables[177]["label"]
network = variables[177]["network"]
variable_type = variables[177]["type"]
label = variables[177]["label"]
doc = variables[177]["doc"]
onto_ID = "V_177"
V_177 = onto.ProMoVar( onto_ID )
V_177.label = label
V_177.network = network
V_177.variable_type = variable_type
V_177.comment = doc

units = variables[177]["units"].asList()
V_177.time = [ units[0] ]
V_177.length = [ units[1] ]
V_177.amount = [ units[2] ]
V_177.mass = [ units[3] ]
V_177.temperature = [ units[4] ]
V_177.current = [ units[5] ]
V_177.light = [ units[6] ]

# 179
label = variables[179]["label"]
network = variables[179]["network"]
variable_type = variables[179]["type"]
label = variables[179]["label"]
doc = variables[179]["doc"]
onto_ID = "V_179"
V_179 = onto.ProMoVar( onto_ID )
V_179.label = label
V_179.network = network
V_179.variable_type = variable_type
V_179.comment = doc

units = variables[179]["units"].asList()
V_179.time = [ units[0] ]
V_179.length = [ units[1] ]
V_179.amount = [ units[2] ]
V_179.mass = [ units[3] ]
V_179.temperature = [ units[4] ]
V_179.current = [ units[5] ]
V_179.light = [ units[6] ]

# 180
label = variables[180]["label"]
network = variables[180]["network"]
variable_type = variables[180]["type"]
label = variables[180]["label"]
doc = variables[180]["doc"]
onto_ID = "V_180"
V_180 = onto.ProMoVar( onto_ID )
V_180.label = label
V_180.network = network
V_180.variable_type = variable_type
V_180.comment = doc

units = variables[180]["units"].asList()
V_180.time = [ units[0] ]
V_180.length = [ units[1] ]
V_180.amount = [ units[2] ]
V_180.mass = [ units[3] ]
V_180.temperature = [ units[4] ]
V_180.current = [ units[5] ]
V_180.light = [ units[6] ]

# 181
label = variables[181]["label"]
network = variables[181]["network"]
variable_type = variables[181]["type"]
label = variables[181]["label"]
doc = variables[181]["doc"]
onto_ID = "V_181"
V_181 = onto.ProMoVar( onto_ID )
V_181.label = label
V_181.network = network
V_181.variable_type = variable_type
V_181.comment = doc

units = variables[181]["units"].asList()
V_181.time = [ units[0] ]
V_181.length = [ units[1] ]
V_181.amount = [ units[2] ]
V_181.mass = [ units[3] ]
V_181.temperature = [ units[4] ]
V_181.current = [ units[5] ]
V_181.light = [ units[6] ]

# 182
label = variables[182]["label"]
network = variables[182]["network"]
variable_type = variables[182]["type"]
label = variables[182]["label"]
doc = variables[182]["doc"]
onto_ID = "V_182"
V_182 = onto.ProMoVar( onto_ID )
V_182.label = label
V_182.network = network
V_182.variable_type = variable_type
V_182.comment = doc

units = variables[182]["units"].asList()
V_182.time = [ units[0] ]
V_182.length = [ units[1] ]
V_182.amount = [ units[2] ]
V_182.mass = [ units[3] ]
V_182.temperature = [ units[4] ]
V_182.current = [ units[5] ]
V_182.light = [ units[6] ]

# 183
label = variables[183]["label"]
network = variables[183]["network"]
variable_type = variables[183]["type"]
label = variables[183]["label"]
doc = variables[183]["doc"]
onto_ID = "V_183"
V_183 = onto.ProMoVar( onto_ID )
V_183.label = label
V_183.network = network
V_183.variable_type = variable_type
V_183.comment = doc

units = variables[183]["units"].asList()
V_183.time = [ units[0] ]
V_183.length = [ units[1] ]
V_183.amount = [ units[2] ]
V_183.mass = [ units[3] ]
V_183.temperature = [ units[4] ]
V_183.current = [ units[5] ]
V_183.light = [ units[6] ]

# 184
label = variables[184]["label"]
network = variables[184]["network"]
variable_type = variables[184]["type"]
label = variables[184]["label"]
doc = variables[184]["doc"]
onto_ID = "V_184"
V_184 = onto.ProMoVar( onto_ID )
V_184.label = label
V_184.network = network
V_184.variable_type = variable_type
V_184.comment = doc

units = variables[184]["units"].asList()
V_184.time = [ units[0] ]
V_184.length = [ units[1] ]
V_184.amount = [ units[2] ]
V_184.mass = [ units[3] ]
V_184.temperature = [ units[4] ]
V_184.current = [ units[5] ]
V_184.light = [ units[6] ]

# 185
label = variables[185]["label"]
network = variables[185]["network"]
variable_type = variables[185]["type"]
label = variables[185]["label"]
doc = variables[185]["doc"]
onto_ID = "V_185"
V_185 = onto.ProMoVar( onto_ID )
V_185.label = label
V_185.network = network
V_185.variable_type = variable_type
V_185.comment = doc

units = variables[185]["units"].asList()
V_185.time = [ units[0] ]
V_185.length = [ units[1] ]
V_185.amount = [ units[2] ]
V_185.mass = [ units[3] ]
V_185.temperature = [ units[4] ]
V_185.current = [ units[5] ]
V_185.light = [ units[6] ]

# 186
label = variables[186]["label"]
network = variables[186]["network"]
variable_type = variables[186]["type"]
label = variables[186]["label"]
doc = variables[186]["doc"]
onto_ID = "V_186"
V_186 = onto.ProMoVar( onto_ID )
V_186.label = label
V_186.network = network
V_186.variable_type = variable_type
V_186.comment = doc

units = variables[186]["units"].asList()
V_186.time = [ units[0] ]
V_186.length = [ units[1] ]
V_186.amount = [ units[2] ]
V_186.mass = [ units[3] ]
V_186.temperature = [ units[4] ]
V_186.current = [ units[5] ]
V_186.light = [ units[6] ]

# 187
label = variables[187]["label"]
network = variables[187]["network"]
variable_type = variables[187]["type"]
label = variables[187]["label"]
doc = variables[187]["doc"]
onto_ID = "V_187"
V_187 = onto.ProMoVar( onto_ID )
V_187.label = label
V_187.network = network
V_187.variable_type = variable_type
V_187.comment = doc

units = variables[187]["units"].asList()
V_187.time = [ units[0] ]
V_187.length = [ units[1] ]
V_187.amount = [ units[2] ]
V_187.mass = [ units[3] ]
V_187.temperature = [ units[4] ]
V_187.current = [ units[5] ]
V_187.light = [ units[6] ]

# 188
label = variables[188]["label"]
network = variables[188]["network"]
variable_type = variables[188]["type"]
label = variables[188]["label"]
doc = variables[188]["doc"]
onto_ID = "V_188"
V_188 = onto.ProMoVar( onto_ID )
V_188.label = label
V_188.network = network
V_188.variable_type = variable_type
V_188.comment = doc

units = variables[188]["units"].asList()
V_188.time = [ units[0] ]
V_188.length = [ units[1] ]
V_188.amount = [ units[2] ]
V_188.mass = [ units[3] ]
V_188.temperature = [ units[4] ]
V_188.current = [ units[5] ]
V_188.light = [ units[6] ]

# 189
label = variables[189]["label"]
network = variables[189]["network"]
variable_type = variables[189]["type"]
label = variables[189]["label"]
doc = variables[189]["doc"]
onto_ID = "V_189"
V_189 = onto.ProMoVar( onto_ID )
V_189.label = label
V_189.network = network
V_189.variable_type = variable_type
V_189.comment = doc

units = variables[189]["units"].asList()
V_189.time = [ units[0] ]
V_189.length = [ units[1] ]
V_189.amount = [ units[2] ]
V_189.mass = [ units[3] ]
V_189.temperature = [ units[4] ]
V_189.current = [ units[5] ]
V_189.light = [ units[6] ]

# 190
label = variables[190]["label"]
network = variables[190]["network"]
variable_type = variables[190]["type"]
label = variables[190]["label"]
doc = variables[190]["doc"]
onto_ID = "V_190"
V_190 = onto.ProMoVar( onto_ID )
V_190.label = label
V_190.network = network
V_190.variable_type = variable_type
V_190.comment = doc

units = variables[190]["units"].asList()
V_190.time = [ units[0] ]
V_190.length = [ units[1] ]
V_190.amount = [ units[2] ]
V_190.mass = [ units[3] ]
V_190.temperature = [ units[4] ]
V_190.current = [ units[5] ]
V_190.light = [ units[6] ]

# 191
label = variables[191]["label"]
network = variables[191]["network"]
variable_type = variables[191]["type"]
label = variables[191]["label"]
doc = variables[191]["doc"]
onto_ID = "V_191"
V_191 = onto.ProMoVar( onto_ID )
V_191.label = label
V_191.network = network
V_191.variable_type = variable_type
V_191.comment = doc

units = variables[191]["units"].asList()
V_191.time = [ units[0] ]
V_191.length = [ units[1] ]
V_191.amount = [ units[2] ]
V_191.mass = [ units[3] ]
V_191.temperature = [ units[4] ]
V_191.current = [ units[5] ]
V_191.light = [ units[6] ]

# functions assignments

#1

V_1.has_function = []
#2

V_2.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_1 )
F_ID = "F_1"
F_1 = onto.function( F_ID )
F_1.is_function_of = incidence_list
V_2.has_function.append( F_1 )
#3

V_3.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_1 )
F_ID = "F_2"
F_2 = onto.function( F_ID )
F_2.is_function_of = incidence_list
V_3.has_function.append( F_2 )
#4

V_4.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_1 )
F_ID = "F_3"
F_3 = onto.function( F_ID )
F_3.is_function_of = incidence_list
V_4.has_function.append( F_3 )
#5

V_5.has_function = []
#6

V_6.has_function = []
#7

V_7.has_function = []
incidence_list = []
incidence_list.append( V_6 )
incidence_list.append( V_1 )
F_ID = "F_4"
F_4 = onto.function( F_ID )
F_4.is_function_of = incidence_list
V_7.has_function.append( F_4 )
#8

V_8.has_function = []
incidence_list = []
incidence_list.append( V_6 )
incidence_list.append( V_1 )
F_ID = "F_5"
F_5 = onto.function( F_ID )
F_5.is_function_of = incidence_list
V_8.has_function.append( F_5 )
#9

V_9.has_function = []
#10

V_10.has_function = []
#11

V_11.has_function = []
#12

V_12.has_function = []
#13

V_13.has_function = []
#15

V_15.has_function = []
incidence_list = []
incidence_list.append( V_11 )
incidence_list.append( V_13 )
F_ID = "F_6"
F_6 = onto.function( F_ID )
F_6.is_function_of = incidence_list
V_15.has_function.append( F_6 )
incidence_list = []
incidence_list.append( V_15 )
incidence_list.append( V_1 )
F_ID = "F_115"
F_115 = onto.function( F_ID )
F_115.is_function_of = incidence_list
V_15.has_function.append( F_115 )
#16

V_16.has_function = []
incidence_list = []
incidence_list.append( V_11 )
incidence_list.append( V_12 )
F_ID = "F_7"
F_7 = onto.function( F_ID )
F_7.is_function_of = incidence_list
V_16.has_function.append( F_7 )
incidence_list = []
incidence_list.append( V_16 )
incidence_list.append( V_1 )
F_ID = "F_113"
F_113 = onto.function( F_ID )
F_113.is_function_of = incidence_list
V_16.has_function.append( F_113 )
#18

V_18.has_function = []
incidence_list = []
incidence_list.append( V_11 )
incidence_list.append( V_15 )
incidence_list.append( V_13 )
F_ID = "F_9"
F_9 = onto.function( F_ID )
F_9.is_function_of = incidence_list
V_18.has_function.append( F_9 )
incidence_list = []
incidence_list.append( V_69 )
incidence_list.append( V_148 )
incidence_list.append( V_16 )
incidence_list.append( V_145 )
incidence_list.append( V_16 )
F_ID = "F_122"
F_122 = onto.function( F_ID )
F_122.is_function_of = incidence_list
V_18.has_function.append( F_122 )
incidence_list = []
incidence_list.append( V_126 )
incidence_list.append( V_6 )
incidence_list.append( V_7 )
incidence_list.append( V_8 )
incidence_list.append( V_151 )
F_ID = "F_123"
F_123 = onto.function( F_ID )
F_123.is_function_of = incidence_list
V_18.has_function.append( F_123 )
#19

V_19.has_function = []
incidence_list = []
incidence_list.append( V_11 )
incidence_list.append( V_16 )
incidence_list.append( V_12 )
F_ID = "F_10"
F_10 = onto.function( F_ID )
F_10.is_function_of = incidence_list
V_19.has_function.append( F_10 )
#20

V_20.has_function = []
incidence_list = []
incidence_list.append( V_11 )
incidence_list.append( V_15 )
incidence_list.append( V_13 )
incidence_list.append( V_16 )
incidence_list.append( V_12 )
F_ID = "F_11"
F_11 = onto.function( F_ID )
F_11.is_function_of = incidence_list
V_20.has_function.append( F_11 )
#21

V_21.has_function = []
incidence_list = []
incidence_list.append( V_9 )
incidence_list.append( V_6 )
F_ID = "F_12"
F_12 = onto.function( F_ID )
F_12.is_function_of = incidence_list
V_21.has_function.append( F_12 )
#22

V_22.has_function = []
incidence_list = []
incidence_list.append( V_10 )
incidence_list.append( V_6 )
F_ID = "F_13"
F_13 = onto.function( F_ID )
F_13.is_function_of = incidence_list
V_22.has_function.append( F_13 )
#23

V_23.has_function = []
#24

V_24.has_function = []
incidence_list = []
incidence_list.append( V_23 )
incidence_list.append( V_6 )
F_ID = "F_14"
F_14 = onto.function( F_ID )
F_14.is_function_of = incidence_list
V_24.has_function.append( F_14 )
#25

V_25.has_function = []
incidence_list = []
incidence_list.append( V_21 )
incidence_list.append( V_22 )
incidence_list.append( V_24 )
F_ID = "F_15"
F_15 = onto.function( F_ID )
F_15.is_function_of = incidence_list
V_25.has_function.append( F_15 )
#26

V_26.has_function = []
#27

V_27.has_function = []
incidence_list = []
incidence_list.append( V_12 )
incidence_list.append( V_1 )
F_ID = "F_16"
F_16 = onto.function( F_ID )
F_16.is_function_of = incidence_list
V_27.has_function.append( F_16 )
#28

V_28.has_function = []
incidence_list = []
incidence_list.append( V_26 )
incidence_list.append( V_27 )
F_ID = "F_17"
F_17 = onto.function( F_ID )
F_17.is_function_of = incidence_list
V_28.has_function.append( F_17 )
#29

V_29.has_function = []
incidence_list = []
incidence_list.append( V_29 )
incidence_list.append( V_1 )
F_ID = "F_142"
F_142 = onto.function( F_ID )
F_142.is_function_of = incidence_list
V_29.has_function.append( F_142 )
#30

V_30.has_function = []
incidence_list = []
incidence_list.append( V_18 )
incidence_list.append( V_16 )
F_ID = "F_18"
F_18 = onto.function( F_ID )
F_18.is_function_of = incidence_list
V_30.has_function.append( F_18 )
#31

V_31.has_function = []
incidence_list = []
incidence_list.append( V_11 )
incidence_list.append( V_16 )
F_ID = "F_19"
F_19 = onto.function( F_ID )
F_19.is_function_of = incidence_list
V_31.has_function.append( F_19 )
#34

V_34.has_function = []
incidence_list = []
incidence_list.append( V_13 )
incidence_list.append( V_11 )
incidence_list.append( V_16 )
incidence_list.append( V_21 )
F_ID = "F_22"
F_22 = onto.function( F_ID )
F_22.is_function_of = incidence_list
V_34.has_function.append( F_22 )
incidence_list = []
incidence_list.append( V_34 )
incidence_list.append( V_1 )
F_ID = "F_131"
F_131 = onto.function( F_ID )
F_131.is_function_of = incidence_list
V_34.has_function.append( F_131 )
#35

V_35.has_function = []
incidence_list = []
incidence_list.append( V_13 )
incidence_list.append( V_11 )
incidence_list.append( V_16 )
incidence_list.append( V_22 )
F_ID = "F_23"
F_23 = onto.function( F_ID )
F_23.is_function_of = incidence_list
V_35.has_function.append( F_23 )
incidence_list = []
incidence_list.append( V_35 )
incidence_list.append( V_1 )
F_ID = "F_132"
F_132 = onto.function( F_ID )
F_132.is_function_of = incidence_list
V_35.has_function.append( F_132 )
#36

V_36.has_function = []
incidence_list = []
incidence_list.append( V_13 )
incidence_list.append( V_11 )
incidence_list.append( V_16 )
incidence_list.append( V_24 )
F_ID = "F_24"
F_24 = onto.function( F_ID )
F_24.is_function_of = incidence_list
V_36.has_function.append( F_24 )
incidence_list = []
incidence_list.append( V_36 )
incidence_list.append( V_1 )
F_ID = "F_133"
F_133 = onto.function( F_ID )
F_133.is_function_of = incidence_list
V_36.has_function.append( F_133 )
#37

V_37.has_function = []
incidence_list = []
incidence_list.append( V_34 )
incidence_list.append( V_35 )
incidence_list.append( V_36 )
F_ID = "F_25"
F_25 = onto.function( F_ID )
F_25.is_function_of = incidence_list
V_37.has_function.append( F_25 )
#42

V_42.has_function = []
incidence_list = []
incidence_list.append( V_119 )
incidence_list.append( V_6 )
incidence_list.append( V_7 )
incidence_list.append( V_8 )
incidence_list.append( V_150 )
F_ID = "F_116"
F_116 = onto.function( F_ID )
F_116.is_function_of = incidence_list
V_42.has_function.append( F_116 )
#45

V_45.has_function = []
incidence_list = []
incidence_list.append( V_11 )
incidence_list.append( V_42 )
F_ID = "F_32"
F_32 = onto.function( F_ID )
F_32.is_function_of = incidence_list
V_45.has_function.append( F_32 )
incidence_list = []
incidence_list.append( V_45 )
incidence_list.append( V_1 )
F_ID = "F_114"
F_114 = onto.function( F_ID )
F_114.is_function_of = incidence_list
V_45.has_function.append( F_114 )
#50

V_50.has_function = []
incidence_list = []
incidence_list.append( V_29 )
incidence_list.append( V_45 )
incidence_list.append( V_13 )
incidence_list.append( V_11 )
incidence_list.append( V_15 )
incidence_list.append( V_21 )
F_ID = "F_37"
F_37 = onto.function( F_ID )
F_37.is_function_of = incidence_list
V_50.has_function.append( F_37 )
incidence_list = []
incidence_list.append( V_50 )
incidence_list.append( V_1 )
F_ID = "F_134"
F_134 = onto.function( F_ID )
F_134.is_function_of = incidence_list
V_50.has_function.append( F_134 )
#51

V_51.has_function = []
incidence_list = []
incidence_list.append( V_29 )
incidence_list.append( V_45 )
incidence_list.append( V_13 )
incidence_list.append( V_11 )
incidence_list.append( V_15 )
incidence_list.append( V_22 )
F_ID = "F_38"
F_38 = onto.function( F_ID )
F_38.is_function_of = incidence_list
V_51.has_function.append( F_38 )
incidence_list = []
incidence_list.append( V_51 )
incidence_list.append( V_1 )
F_ID = "F_135"
F_135 = onto.function( F_ID )
F_135.is_function_of = incidence_list
V_51.has_function.append( F_135 )
#52

V_52.has_function = []
incidence_list = []
incidence_list.append( V_29 )
incidence_list.append( V_45 )
incidence_list.append( V_13 )
incidence_list.append( V_11 )
incidence_list.append( V_15 )
incidence_list.append( V_24 )
F_ID = "F_39"
F_39 = onto.function( F_ID )
F_39.is_function_of = incidence_list
V_52.has_function.append( F_39 )
incidence_list = []
incidence_list.append( V_52 )
incidence_list.append( V_1 )
F_ID = "F_136"
F_136 = onto.function( F_ID )
F_136.is_function_of = incidence_list
V_52.has_function.append( F_136 )
#53

V_53.has_function = []
incidence_list = []
incidence_list.append( V_50 )
incidence_list.append( V_51 )
incidence_list.append( V_52 )
F_ID = "F_40"
F_40 = onto.function( F_ID )
F_40.is_function_of = incidence_list
V_53.has_function.append( F_40 )
#54

V_54.has_function = []
incidence_list = []
incidence_list.append( V_45 )
incidence_list.append( V_21 )
incidence_list.append( V_13 )
incidence_list.append( V_11 )
incidence_list.append( V_45 )
F_ID = "F_41"
F_41 = onto.function( F_ID )
F_41.is_function_of = incidence_list
V_54.has_function.append( F_41 )
incidence_list = []
incidence_list.append( V_54 )
incidence_list.append( V_1 )
F_ID = "F_137"
F_137 = onto.function( F_ID )
F_137.is_function_of = incidence_list
V_54.has_function.append( F_137 )
#55

V_55.has_function = []
incidence_list = []
incidence_list.append( V_45 )
incidence_list.append( V_22 )
incidence_list.append( V_13 )
incidence_list.append( V_11 )
incidence_list.append( V_45 )
F_ID = "F_42"
F_42 = onto.function( F_ID )
F_42.is_function_of = incidence_list
V_55.has_function.append( F_42 )
incidence_list = []
incidence_list.append( V_55 )
incidence_list.append( V_1 )
F_ID = "F_138"
F_138 = onto.function( F_ID )
F_138.is_function_of = incidence_list
V_55.has_function.append( F_138 )
#56

V_56.has_function = []
incidence_list = []
incidence_list.append( V_45 )
incidence_list.append( V_24 )
incidence_list.append( V_13 )
incidence_list.append( V_11 )
incidence_list.append( V_45 )
F_ID = "F_43"
F_43 = onto.function( F_ID )
F_43.is_function_of = incidence_list
V_56.has_function.append( F_43 )
#57

V_57.has_function = []
incidence_list = []
incidence_list.append( V_54 )
incidence_list.append( V_55 )
incidence_list.append( V_56 )
F_ID = "F_44"
F_44 = onto.function( F_ID )
F_44.is_function_of = incidence_list
V_57.has_function.append( F_44 )
#58

V_58.has_function = []
incidence_list = []
incidence_list.append( V_18 )
incidence_list.append( V_42 )
F_ID = "F_45"
F_45 = onto.function( F_ID )
F_45.is_function_of = incidence_list
V_58.has_function.append( F_45 )
incidence_list = []
incidence_list.append( V_58 )
incidence_list.append( V_1 )
F_ID = "F_139"
F_139 = onto.function( F_ID )
F_139.is_function_of = incidence_list
V_58.has_function.append( F_139 )
#59

V_59.has_function = []
#60

V_60.has_function = []
#61

V_61.has_function = []
#62

V_62.has_function = []
#63

V_63.has_function = []
#64

V_64.has_function = []
#65

V_65.has_function = []
incidence_list = []
incidence_list.append( V_5 )
incidence_list.append( V_15 )
F_ID = "F_46"
F_46 = onto.function( F_ID )
F_46.is_function_of = incidence_list
V_65.has_function.append( F_46 )
#69

V_69.has_function = []
incidence_list = []
incidence_list.append( V_29 )
incidence_list.append( V_42 )
F_ID = "F_47"
F_47 = onto.function( F_ID )
F_47.is_function_of = incidence_list
V_69.has_function.append( F_47 )
#71

V_71.has_function = []
incidence_list = []
incidence_list.append( V_69 )
incidence_list.append( V_13 )
F_ID = "F_49"
F_49 = onto.function( F_ID )
F_49.is_function_of = incidence_list
V_71.has_function.append( F_49 )
incidence_list = []
incidence_list.append( V_71 )
incidence_list.append( V_1 )
F_ID = "F_154"
F_154 = onto.function( F_ID )
F_154.is_function_of = incidence_list
V_71.has_function.append( F_154 )
#73

V_73.has_function = []
incidence_list = []
incidence_list.append( V_5 )
incidence_list.append( V_59 )
F_ID = "F_51"
F_51 = onto.function( F_ID )
F_51.is_function_of = incidence_list
V_73.has_function.append( F_51 )
#77

V_77.has_function = []
incidence_list = []
incidence_list.append( V_62 )
incidence_list.append( V_16 )
F_ID = "F_55"
F_55 = onto.function( F_ID )
F_55.is_function_of = incidence_list
V_77.has_function.append( F_55 )
#86

V_86.has_function = []
#87

V_87.has_function = []
incidence_list = []
incidence_list.append( V_62 )
incidence_list.append( V_28 )
incidence_list.append( V_77 )
incidence_list.append( V_1 )
F_ID = "F_64"
F_64 = onto.function( F_ID )
F_64.is_function_of = incidence_list
V_87.has_function.append( F_64 )
#88

V_88.has_function = []
#89

V_89.has_function = []
incidence_list = []
incidence_list.append( V_88 )
incidence_list.append( V_87 )
incidence_list.append( V_28 )
incidence_list.append( V_62 )
incidence_list.append( V_77 )
F_ID = "F_65"
F_65 = onto.function( F_ID )
F_65.is_function_of = incidence_list
V_89.has_function.append( F_65 )
#93

V_93.has_function = []
incidence_list = []
incidence_list.append( V_61 )
incidence_list.append( V_60 )
incidence_list.append( V_77 )
incidence_list.append( V_77 )
incidence_list.append( V_86 )
F_ID = "F_69"
F_69 = onto.function( F_ID )
F_69.is_function_of = incidence_list
V_93.has_function.append( F_69 )
#95

V_95.has_function = []
incidence_list = []
incidence_list.append( V_10 )
incidence_list.append( V_23 )
F_ID = "F_71"
F_71 = onto.function( F_ID )
F_71.is_function_of = incidence_list
V_95.has_function.append( F_71 )
#96

V_96.has_function = []
incidence_list = []
incidence_list.append( V_9 )
incidence_list.append( V_23 )
F_ID = "F_72"
F_72 = onto.function( F_ID )
F_72.is_function_of = incidence_list
V_96.has_function.append( F_72 )
#97

V_97.has_function = []
incidence_list = []
incidence_list.append( V_9 )
incidence_list.append( V_10 )
F_ID = "F_73"
F_73 = onto.function( F_ID )
F_73.is_function_of = incidence_list
V_97.has_function.append( F_73 )
#98

V_98.has_function = []
incidence_list = []
incidence_list.append( V_71 )
incidence_list.append( V_50 )
incidence_list.append( V_95 )
incidence_list.append( V_127 )
incidence_list.append( V_15 )
F_ID = "F_74"
F_74 = onto.function( F_ID )
F_74.is_function_of = incidence_list
V_98.has_function.append( F_74 )
#104

V_104.has_function = []
incidence_list = []
incidence_list.append( V_95 )
incidence_list.append( V_54 )
incidence_list.append( V_128 )
incidence_list.append( V_45 )
F_ID = "F_80"
F_80 = onto.function( F_ID )
F_80.is_function_of = incidence_list
V_104.has_function.append( F_80 )
#105

V_105.has_function = []
incidence_list = []
incidence_list.append( V_73 )
incidence_list.append( V_104 )
F_ID = "F_81"
F_81 = onto.function( F_ID )
F_81.is_function_of = incidence_list
V_105.has_function.append( F_81 )
#106

V_106.has_function = []
incidence_list = []
incidence_list.append( V_73 )
incidence_list.append( V_58 )
incidence_list.append( V_104 )
F_ID = "F_82"
F_82 = onto.function( F_ID )
F_82.is_function_of = incidence_list
V_106.has_function.append( F_82 )
#107

V_107.has_function = []
incidence_list = []
incidence_list.append( V_5 )
incidence_list.append( V_106 )
F_ID = "F_83"
F_83 = onto.function( F_ID )
F_83.is_function_of = incidence_list
V_107.has_function.append( F_83 )
#108

V_108.has_function = []
incidence_list = []
incidence_list.append( V_13 )
incidence_list.append( V_42 )
F_ID = "F_84"
F_84 = onto.function( F_ID )
F_84.is_function_of = incidence_list
V_108.has_function.append( F_84 )
incidence_list = []
incidence_list.append( V_108 )
incidence_list.append( V_1 )
F_ID = "F_127"
F_127 = onto.function( F_ID )
F_127.is_function_of = incidence_list
V_108.has_function.append( F_127 )
#109

V_109.has_function = []
incidence_list = []
incidence_list.append( V_4 )
incidence_list.append( V_73 )
incidence_list.append( V_65 )
incidence_list.append( V_73 )
incidence_list.append( V_108 )
F_ID = "F_85"
F_85 = onto.function( F_ID )
F_85.is_function_of = incidence_list
V_109.has_function.append( F_85 )
#110

V_110.has_function = []
incidence_list = []
incidence_list.append( V_98 )
incidence_list.append( V_109 )
F_ID = "F_86"
F_86 = onto.function( F_ID )
F_86.is_function_of = incidence_list
V_110.has_function.append( F_86 )
#111

V_111.has_function = []
incidence_list = []
incidence_list.append( V_73 )
incidence_list.append( V_110 )
F_ID = "F_87"
F_87 = onto.function( F_ID )
F_87.is_function_of = incidence_list
V_111.has_function.append( F_87 )
#114

V_114.has_function = []
incidence_list = []
incidence_list.append( V_108 )
incidence_list.append( V_64 )
F_ID = "F_90"
F_90 = onto.function( F_ID )
F_90.is_function_of = incidence_list
V_114.has_function.append( F_90 )
#115

V_115.has_function = []
incidence_list = []
incidence_list.append( V_114 )
incidence_list.append( V_1 )
F_ID = "F_91"
F_91 = onto.function( F_ID )
F_91.is_function_of = incidence_list
V_115.has_function.append( F_91 )
#116

V_116.has_function = []
incidence_list = []
incidence_list.append( V_114 )
incidence_list.append( V_115 )
incidence_list.append( V_86 )
F_ID = "F_92"
F_92 = onto.function( F_ID )
F_92.is_function_of = incidence_list
V_116.has_function.append( F_92 )
#117

V_117.has_function = []
incidence_list = []
incidence_list.append( V_89 )
incidence_list.append( V_63 )
incidence_list.append( V_116 )
F_ID = "F_93"
F_93 = onto.function( F_ID )
F_93.is_function_of = incidence_list
V_117.has_function.append( F_93 )
#118

V_118.has_function = []
incidence_list = []
incidence_list.append( V_13 )
incidence_list.append( V_93 )
incidence_list.append( V_117 )
F_ID = "F_94"
F_94 = onto.function( F_ID )
F_94.is_function_of = incidence_list
V_118.has_function.append( F_94 )
#119

V_119.has_function = []
incidence_list = []
incidence_list.append( V_111 )
incidence_list.append( V_105 )
incidence_list.append( V_118 )
F_ID = "F_95"
F_95 = onto.function( F_ID )
F_95.is_function_of = incidence_list
V_119.has_function.append( F_95 )
incidence_list = []
incidence_list.append( V_119 )
incidence_list.append( V_2 )
F_ID = "F_129"
F_129 = onto.function( F_ID )
F_129.is_function_of = incidence_list
V_119.has_function.append( F_129 )
#120

V_120.has_function = []
incidence_list = []
incidence_list.append( V_73 )
incidence_list.append( V_58 )
incidence_list.append( V_110 )
F_ID = "F_96"
F_96 = onto.function( F_ID )
F_96.is_function_of = incidence_list
V_120.has_function.append( F_96 )
#121

V_121.has_function = []
incidence_list = []
incidence_list.append( V_5 )
incidence_list.append( V_120 )
F_ID = "F_97"
F_97 = onto.function( F_ID )
F_97.is_function_of = incidence_list
V_121.has_function.append( F_97 )
#122

V_122.has_function = []
incidence_list = []
incidence_list.append( V_120 )
incidence_list.append( V_1 )
F_ID = "F_98"
F_98 = onto.function( F_ID )
F_98.is_function_of = incidence_list
V_122.has_function.append( F_98 )
#123

V_123.has_function = []
incidence_list = []
incidence_list.append( V_5 )
incidence_list.append( V_122 )
F_ID = "F_99"
F_99 = onto.function( F_ID )
F_99.is_function_of = incidence_list
V_123.has_function.append( F_99 )
#124

V_124.has_function = []
incidence_list = []
incidence_list.append( V_95 )
incidence_list.append( V_34 )
incidence_list.append( V_127 )
incidence_list.append( V_16 )
F_ID = "F_100"
F_100 = onto.function( F_ID )
F_100.is_function_of = incidence_list
V_124.has_function.append( F_100 )
#125

V_125.has_function = []
incidence_list = []
incidence_list.append( V_5 )
incidence_list.append( V_124 )
F_ID = "F_101"
F_101 = onto.function( F_ID )
F_101.is_function_of = incidence_list
V_125.has_function.append( F_101 )
#126

V_126.has_function = []
incidence_list = []
incidence_list.append( V_121 )
incidence_list.append( V_107 )
incidence_list.append( V_125 )
incidence_list.append( V_123 )
F_ID = "F_102"
F_102 = onto.function( F_ID )
F_102.is_function_of = incidence_list
V_126.has_function.append( F_102 )
incidence_list = []
incidence_list.append( V_126 )
incidence_list.append( V_2 )
F_ID = "F_128"
F_128 = onto.function( F_ID )
F_128.is_function_of = incidence_list
V_126.has_function.append( F_128 )
#127

V_127.has_function = []
#128

V_128.has_function = []
#129

V_129.has_function = []
#130

V_130.has_function = []
#133

V_133.has_function = []
incidence_list = []
incidence_list.append( V_133 )
incidence_list.append( V_1 )
F_ID = "F_144"
F_144 = onto.function( F_ID )
F_144.is_function_of = incidence_list
V_133.has_function.append( F_144 )
#134

V_134.has_function = []
incidence_list = []
incidence_list.append( V_134 )
incidence_list.append( V_1 )
F_ID = "F_145"
F_145 = onto.function( F_ID )
F_145.is_function_of = incidence_list
V_134.has_function.append( F_145 )
#135

V_135.has_function = []
incidence_list = []
incidence_list.append( V_135 )
incidence_list.append( V_1 )
F_ID = "F_146"
F_146 = onto.function( F_ID )
F_146.is_function_of = incidence_list
V_135.has_function.append( F_146 )
#136

V_136.has_function = []
incidence_list = []
incidence_list.append( V_136 )
incidence_list.append( V_1 )
F_ID = "F_147"
F_147 = onto.function( F_ID )
F_147.is_function_of = incidence_list
V_136.has_function.append( F_147 )
#137

V_137.has_function = []
incidence_list = []
incidence_list.append( V_129 )
incidence_list.append( V_144 )
incidence_list.append( V_6 )
incidence_list.append( V_7 )
incidence_list.append( V_8 )
F_ID = "F_112"
F_112 = onto.function( F_ID )
F_112.is_function_of = incidence_list
V_137.has_function.append( F_112 )
#138

V_138.has_function = []
incidence_list = []
incidence_list.append( V_137 )
incidence_list.append( V_1 )
F_ID = "F_103"
F_103 = onto.function( F_ID )
F_103.is_function_of = incidence_list
V_138.has_function.append( F_103 )
#139

V_139.has_function = []
#140

V_140.has_function = []
incidence_list = []
incidence_list.append( V_139 )
incidence_list.append( V_135 )
F_ID = "F_104"
F_104 = onto.function( F_ID )
F_104.is_function_of = incidence_list
V_140.has_function.append( F_104 )
#142

V_142.has_function = []
incidence_list = []
incidence_list.append( V_142 )
incidence_list.append( V_1 )
F_ID = "F_148"
F_148 = onto.function( F_ID )
F_148.is_function_of = incidence_list
V_142.has_function.append( F_148 )
#143

V_143.has_function = []
incidence_list = []
incidence_list.append( V_143 )
incidence_list.append( V_1 )
F_ID = "F_149"
F_149 = onto.function( F_ID )
F_149.is_function_of = incidence_list
V_143.has_function.append( F_149 )
#144

V_144.has_function = []
incidence_list = []
incidence_list.append( V_142 )
incidence_list.append( V_137 )
incidence_list.append( V_143 )
incidence_list.append( V_140 )
F_ID = "F_106"
F_106 = onto.function( F_ID )
F_106.is_function_of = incidence_list
V_144.has_function.append( F_106 )
#145

V_145.has_function = []
incidence_list = []
incidence_list.append( V_16 )
incidence_list.append( V_1 )
F_ID = "F_117"
F_117 = onto.function( F_ID )
F_117.is_function_of = incidence_list
V_145.has_function.append( F_117 )
#148

V_148.has_function = []
incidence_list = []
incidence_list.append( V_30 )
incidence_list.append( V_69 )
F_ID = "F_120"
F_120 = onto.function( F_ID )
F_120.is_function_of = incidence_list
V_148.has_function.append( F_120 )
incidence_list = []
incidence_list.append( V_148 )
incidence_list.append( V_1 )
F_ID = "F_140"
F_140 = onto.function( F_ID )
F_140.is_function_of = incidence_list
V_148.has_function.append( F_140 )
#149

V_149.has_function = []
incidence_list = []
incidence_list.append( V_31 )
incidence_list.append( V_69 )
F_ID = "F_121"
F_121 = onto.function( F_ID )
F_121.is_function_of = incidence_list
V_149.has_function.append( F_121 )
incidence_list = []
incidence_list.append( V_149 )
incidence_list.append( V_1 )
F_ID = "F_141"
F_141 = onto.function( F_ID )
F_141.is_function_of = incidence_list
V_149.has_function.append( F_141 )
#150

V_150.has_function = []
incidence_list = []
incidence_list.append( V_42 )
incidence_list.append( V_1 )
F_ID = "F_124"
F_124 = onto.function( F_ID )
F_124.is_function_of = incidence_list
V_150.has_function.append( F_124 )
#151

V_151.has_function = []
incidence_list = []
incidence_list.append( V_18 )
incidence_list.append( V_1 )
F_ID = "F_125"
F_125 = onto.function( F_ID )
F_125.is_function_of = incidence_list
V_151.has_function.append( F_125 )
#152

V_152.has_function = []
incidence_list = []
incidence_list.append( V_15 )
incidence_list.append( V_16 )
incidence_list.append( V_45 )
incidence_list.append( V_108 )
F_ID = "F_126"
F_126 = onto.function( F_ID )
F_126.is_function_of = incidence_list
V_152.has_function.append( F_126 )
#153

V_153.has_function = []
incidence_list = []
incidence_list.append( V_42 )
incidence_list.append( V_18 )
F_ID = "F_130"
F_130 = onto.function( F_ID )
F_130.is_function_of = incidence_list
V_153.has_function.append( F_130 )
#154

V_154.has_function = []
incidence_list = []
incidence_list.append( V_37 )
incidence_list.append( V_53 )
incidence_list.append( V_57 )
incidence_list.append( V_58 )
incidence_list.append( V_148 )
incidence_list.append( V_149 )
incidence_list.append( V_29 )
incidence_list.append( V_71 )
F_ID = "F_143"
F_143 = onto.function( F_ID )
F_143.is_function_of = incidence_list
V_154.has_function.append( F_143 )
#155

V_155.has_function = []
incidence_list = []
incidence_list.append( V_133 )
incidence_list.append( V_137 )
incidence_list.append( V_136 )
incidence_list.append( V_140 )
F_ID = "F_150"
F_150 = onto.function( F_ID )
F_150.is_function_of = incidence_list
V_155.has_function.append( F_150 )
incidence_list = []
incidence_list.append( V_136 )
incidence_list.append( V_140 )
F_ID = "F_153"
F_153 = onto.function( F_ID )
F_153.is_function_of = incidence_list
V_155.has_function.append( F_153 )
#158

V_158.has_function = []
incidence_list = []
incidence_list.append( V_3 )
incidence_list.append( V_155 )
F_ID = "F_155"
F_155 = onto.function( F_ID )
F_155.is_function_of = incidence_list
V_158.has_function.append( F_155 )
#161

V_161.has_function = []
#164

V_164.has_function = []
#165

V_165.has_function = []
incidence_list = []
incidence_list.append( V_164 )
incidence_list.append( V_108 )
F_ID = "F_161"
F_161 = onto.function( F_ID )
F_161.is_function_of = incidence_list
V_165.has_function.append( F_161 )
#166

V_166.has_function = []
incidence_list = []
incidence_list.append( V_165 )
incidence_list.append( V_108 )
F_ID = "F_162"
F_162 = onto.function( F_ID )
F_162.is_function_of = incidence_list
V_166.has_function.append( F_162 )
#168

V_168.has_function = []
#170

V_170.has_function = []
#175

V_175.has_function = []
incidence_list = []
incidence_list.append( V_175 )
incidence_list.append( V_1 )
F_ID = "F_171"
F_171 = onto.function( F_ID )
F_171.is_function_of = incidence_list
V_175.has_function.append( F_171 )
#177

V_177.has_function = []
#179

V_179.has_function = []
incidence_list = []
incidence_list.append( V_170 )
incidence_list.append( V_11 )
F_ID = "F_176"
F_176 = onto.function( F_ID )
F_176.is_function_of = incidence_list
V_179.has_function.append( F_176 )
incidence_list = []
incidence_list.append( V_182 )
incidence_list.append( V_180 )
F_ID = "F_181"
F_181 = onto.function( F_ID )
F_181.is_function_of = incidence_list
V_179.has_function.append( F_181 )
incidence_list = []
incidence_list.append( V_181 )
incidence_list.append( V_180 )
F_ID = "F_188"
F_188 = onto.function( F_ID )
F_188.is_function_of = incidence_list
V_179.has_function.append( F_188 )
incidence_list = []
incidence_list.append( V_179 )
incidence_list.append( V_1 )
F_ID = "F_195"
F_195 = onto.function( F_ID )
F_195.is_function_of = incidence_list
V_179.has_function.append( F_195 )
#180

V_180.has_function = []
incidence_list = []
incidence_list.append( V_170 )
incidence_list.append( V_6 )
F_ID = "F_177"
F_177 = onto.function( F_ID )
F_177.is_function_of = incidence_list
V_180.has_function.append( F_177 )
incidence_list = []
incidence_list.append( V_183 )
F_ID = "F_185"
F_185 = onto.function( F_ID )
F_185.is_function_of = incidence_list
V_180.has_function.append( F_185 )
incidence_list = []
incidence_list.append( V_179 )
F_ID = "F_189"
F_189 = onto.function( F_ID )
F_189.is_function_of = incidence_list
V_180.has_function.append( F_189 )
#181

V_181.has_function = []
incidence_list = []
incidence_list.append( V_180 )
incidence_list.append( V_179 )
F_ID = "F_178"
F_178 = onto.function( F_ID )
F_178.is_function_of = incidence_list
V_181.has_function.append( F_178 )
incidence_list = []
incidence_list.append( V_181 )
incidence_list.append( V_1 )
F_ID = "F_180"
F_180 = onto.function( F_ID )
F_180.is_function_of = incidence_list
V_181.has_function.append( F_180 )
#182

V_182.has_function = []
incidence_list = []
incidence_list.append( V_181 )
incidence_list.append( V_175 )
F_ID = "F_179"
F_179 = onto.function( F_ID )
F_179.is_function_of = incidence_list
V_182.has_function.append( F_179 )
#183

V_183.has_function = []
incidence_list = []
incidence_list.append( V_177 )
incidence_list.append( V_179 )
F_ID = "F_182"
F_182 = onto.function( F_ID )
F_182.is_function_of = incidence_list
V_183.has_function.append( F_182 )
incidence_list = []
incidence_list.append( V_183 )
incidence_list.append( V_2 )
F_ID = "F_183"
F_183 = onto.function( F_ID )
F_183.is_function_of = incidence_list
V_183.has_function.append( F_183 )
#184

V_184.has_function = []
#185

V_185.has_function = []
incidence_list = []
incidence_list.append( V_184 )
incidence_list.append( V_180 )
F_ID = "F_186"
F_186 = onto.function( F_ID )
F_186.is_function_of = incidence_list
V_185.has_function.append( F_186 )
#186

V_186.has_function = []
incidence_list = []
incidence_list.append( V_181 )
F_ID = "F_187"
F_187 = onto.function( F_ID )
F_187.is_function_of = incidence_list
V_186.has_function.append( F_187 )
#187

V_187.has_function = []
incidence_list = []
incidence_list.append( V_180 )
F_ID = "F_190"
F_190 = onto.function( F_ID )
F_190.is_function_of = incidence_list
V_187.has_function.append( F_190 )
#188

V_188.has_function = []
incidence_list = []
incidence_list.append( V_179 )
F_ID = "F_191"
F_191 = onto.function( F_ID )
F_191.is_function_of = incidence_list
V_188.has_function.append( F_191 )
#189

V_189.has_function = []
incidence_list = []
incidence_list.append( V_175 )
F_ID = "F_192"
F_192 = onto.function( F_ID )
F_192.is_function_of = incidence_list
V_189.has_function.append( F_192 )
#190

V_190.has_function = []
incidence_list = []
incidence_list.append( V_187 )
incidence_list.append( V_188 )
F_ID = "F_193"
F_193 = onto.function( F_ID )
F_193.is_function_of = incidence_list
V_190.has_function.append( F_193 )
#191

V_191.has_function = []
incidence_list = []
incidence_list.append( V_187 )
incidence_list.append( V_188 )
incidence_list.append( V_190 )
incidence_list.append( V_189 )
F_ID = "F_194"
F_194 = onto.function( F_ID )
F_194.is_function_of = incidence_list
V_191.has_function.append( F_194 )

onto.save("variables.owl")
