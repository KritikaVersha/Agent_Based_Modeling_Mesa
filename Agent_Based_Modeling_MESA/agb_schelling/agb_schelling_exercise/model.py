#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:12:04 2021

@author: kritikaversha
"""

from mesa.datacollection import DataCollector
from mesa import Model
from mesa.time import RandomActivation
from mesa_geo.geoagent import GeoAgent, AgentCreator
from mesa_geo import GeoSpace
import random
import requests
url = 'http://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_20m.json'
r = requests.get(url)
geojson_states = r.json()



class SchellingAgent(GeoAgent):
    """Schelling segregation agent."""

    def __init__(self, unique_id, model, shape, agent_type=None):
        """Create a new Schelling agent.
        Args:
            unique_id: Unique identifier for the agent.
            agent_type: Indicator for the agent's type (minority=1, majority=0)
        """
        super().__init__(unique_id, model, shape)
        self.atype = agent_type

    def step(self):
        """Advance agent one step."""
        similar = 0
        different = 0
        # Fetch neighbors
        neighbors = 
        if neighbors:
            for neighbor in neighbors:
                # If neighboring agent type is similar, increment similarity
                # If neighboring agent type is none, do nothing
                # If neigboring agent type is different, increment difference
                

        # If unhappy, move:
        if similar < different:
            # Select an empty region
            empties = 
            # Switch atypes and add/remove from scheduler
            new_region = random.choice(empties)
            new_region.atype = self.atype
            self.model.schedule.add()
            self.atype = None
            self.model.schedule.remove()
        else:
            self.model.happy += 1

    def __repr__(self):
        return "Agent " + str()


class SchellingModel(Model):
    """Model class for the Schelling segregation model."""

    def __init__(self, density, minority_pc):
        self.density = 
        self.minority_pc = 

        self.schedule = RandomActivation()
        self.grid = GeoSpace()

        self.happy = 0
        self.datacollector = DataCollector({"happy": "happy"})

        self.running = 

        # Set up the grid with patches for every NUTS region
        state_agent_kwargs = dict()
        AC = AgentCreator(agent_class=, agent_kwargs=state_agent_kwargs)
        agents = AC.from_GeoJSON(GeoJSON=, unique_id="")
        self.grid.add_agents()

        # Set up agents
        for agent in agents:
            if random.random() < self.density:
                if random.random() < self.minority_pc:
                    agent.atype = 1
                else:
                    agent.atype = 0
                self.schedule.add()

    def step(self):
        """Run one step of the model.
        If All agents are happy, halt the model.
        """
        self.happy = 0  # Reset counter of happy agents
        self.schedule.step()
        # self.datacollector.collect(self)

        if self.happy == self.schedule.get_agent_count():
            self.running = 
            
