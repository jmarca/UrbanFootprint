# UrbanFootprint-California, Scenario Planning Model
# 
# Copyright (C) 2012-2013 Calthorpe Associates
# 
# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, version 3 of the License.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
# 
# Contact: Calthorpe Associates (urbanfootprint@calthorpe.com)
# Firm contact: 2095 Rose Street Suite 201, Berkeley CA 94709.
# Phone: (510) 548-6800.      Web: www.calthorpe.com
# 

#
# 

#
# 

from footprint.initialization.fixture import ConfigEntitiesFixture, MediumFixture
from footprint.initialization.fixtures.client.default.config_entity.default_config_entities import ConfigEntityMediumKey
from footprint.lib.functions import flatten
from footprint.models.config.scenario import BaseScenario, FutureScenario
from settings import CLIENT

__author__ = 'calthorpe'
from django.contrib.gis.geos import MultiPolygon, Polygon
from footprint.mixins.category import Category


class SacogConfigEntitiesFixture(ConfigEntitiesFixture):
    def regions(self):
        return [
            {
                'key': 'sandag',
                'name': 'SANDAG',
                'description': 'The San Diego region',
                'bounds': MultiPolygon([Polygon((
                    (-122.719, 37.394),  # bottom left
                    (-122.719, 38.059),  # top left
                    (-121.603, 38.059),  # top right
                    (-121.603, 37.394),  # bottom right
                    (-122.719, 37.394),  # bottom leftsample_config_entities
                ))])
            },
        ]

    def projects(self, region=None):
        return [

            {
                'key': 'sandag',
                'name': 'SANDAG Scenarios',
                'description': "The San Diego Region",
                'base_year': 2012,
                'region_index': 0,
                'media': [
                    MediumFixture(key=ConfigEntityMediumKey.Fab.ricate('sandag_logo'), name='Sandag Logo',
                                  url='/static/client/{0}/logos/sandag.png'.format(CLIENT))
                ],
                'bounds': MultiPolygon([Polygon(
                    (
                        # TODO: decide if this needs updating or if it's taken care of by the project method
                        # Sacramento County bounds
                        (-121.862622000787, 38.018420999589),  # bottom left
                        (-121.862622000787, 38.7364049988308),  # top left
                        (-121.027084001338, 38.7364049988308),  # top right
                        (-121.027084001338, 38.018420999589),  # top right
                        (-121.862622000787, 38.018420999589)   # bottom left
                    )
                )])
            }
        ]

    def scenarios(self, project=None, class_scope=None):
        return self.matching_scope([
            {
                'class_scope': BaseScenario,
                'key': '{0}_base'.format(project.key),
                'scope': project.schema(),
                'name': 'Base',
                'description': '{0} Base Scenario {1}'.format('2012', project.name),
                'year': 2012,
                'selections': dict(),
                'categories': [Category(key='category', value='Base')]
            },

            {
                'class_scope': FutureScenario,
                'key': '{0}_series13'.format(project.key),
                'scope': project.schema(),
                'name': 'Series 13',
                'description': '{0} Future Scenario Series13 for {1}'.format('2050', project.name),
                'year': 2050,
                'selections': dict(),
                'categories': [Category(key='category', value='Future')]
            },

            {
                'class_scope': FutureScenario,
                'key': '{0}_scenario_b'.format(project.key),
                'scope': project.schema(),
                'name': 'Scenario B',
                'description': '{0} Future Scenario Alternative B for {1}'.format('2050', project.name),
                'year': 2050,
                'selections': dict(),
                'categories': [Category(key='category', value='Future')]
            },
            {
                'class_scope': FutureScenario,
                'key': '{0}_scenario_c'.format(project.key),
                'scope': project.schema(),
                'name': 'Scenario C'.format(project.name),
                'description': '{0} Future Scenario Alternative C for {1}'.format('2050', project.name),
                'year': 2050,
                'selections': dict(),
                'categories': [Category(key='category', value='Future')]
            },
            {
                'class_scope': FutureScenario,
                'key': '{0}_series9'.format(project.key),
                'scope': project.schema(),
                'name': 'Series 9',
                'description': '{0} Future Scenario Series9 for {1}'.format('2050', project.name),
                'year': 2050,
                'selections': dict(),
                'categories': [Category(key='category', value='Future')]
            },
        ], project_key=project.key if project else None, class_scope=class_scope)

