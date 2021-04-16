#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:14:36 2021

@author: kritikaversha
"""

from mesa_geo.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter
from model import SchellingModel
from mesa_geo.visualization.MapModule import MapModule


class HappyElement(TextElement):
    """
    Display a text count of how many happy agents there are.
    """

    def __init__(self):
        pass

    def render(self, model):
        return "Happy agents: " + 


# Change the default model params 
model_params = {
    "density": UserSettableParameter("slider", "Agent density", 0.6, 0.1, 1.0, 0.1),
    "minority_pc": UserSettableParameter(
        "slider", "Fraction minority", 0.2, 0.00, 1.0, 0.05
    ),
}


def schelling_draw(agent):
    """
    Portrayal Method for canvas based on agent type
    """
    portrayal = dict()
    if agent.atype is None:
        portrayal["color"] = 
    elif agent.atype == 0:
        portrayal["color"] = 
    else:
        portrayal["color"] = 
    return portrayal


happy_element = # Initiate an object of HappyElement
map_element = MapModule(schelling_draw, [37.8, -96], 2, 500, 500)
happy_chart = ChartModule([{"Label": "happy", "Color": "Black"}])

# Use ModularServer to visualize schelling model
server = ModularServer(
)
server.launch()
