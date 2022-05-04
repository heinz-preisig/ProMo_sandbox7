

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

ontology = OntologyContainer("ProMo_sandbox7") #'flash_03')


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

# functions assignments

#1

V_1.has_function = []
#2

V_2.has_function = []
incidence_list = []
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
incidence_list.append( V_1 )
F_ID = "F_3"
F_3 = onto.function( F_ID )
F_3.is_function_of = incidence_list
V_4.has_function.append( F_3 )
#5

V_5.has_function = []
incidence_list = []
incidence_list.append( V_3 )
F_ID = "F_4"
F_4 = onto.function( F_ID )
F_4.is_function_of = incidence_list
V_5.has_function.append( F_4 )
#6

V_6.has_function = []
incidence_list = []
incidence_list.append( V_3 )
F_ID = "F_5"
F_5 = onto.function( F_ID )
F_5.is_function_of = incidence_list
V_6.has_function.append( F_5 )
#7

V_7.has_function = []
incidence_list = []
incidence_list.append( V_3 )
F_ID = "F_6"
F_6 = onto.function( F_ID )
F_6.is_function_of = incidence_list
V_7.has_function.append( F_6 )

onto.save("variables.owl")
