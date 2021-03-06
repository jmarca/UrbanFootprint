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

# coding=utf-8
#
from django.contrib.gis.geos import MultiPolygon
from footprint.models.config.global_config import global_config_singleton
from footprint.lib.functions import flat_map, remove_keys, merge, unique
from footprint.models.config.config_entity import ConfigEntity

__author__ = 'calthorpe'


class CombinedConfigEntity(ConfigEntity):
    """
        A ConfigEntity subclass that is used to combine several ConfigEntities, such as sibling Scenarios, to use as
        the basis of a Presentation
    """

    config_entities = []

    def __init__(self, *args, **kwargs):
        # Remove any kwargs specific to this class before calling super
        new_kwargs = merge(
            remove_keys(
                kwargs,
                ['config_entities', 'parent_config_entity']),
            {'parent_config_entity': kwargs.get('parent_config_entity', global_config_singleton())})
        super(CombinedConfigEntity, self).__init__(*args, **new_kwargs)
        # Set the parent_config_entity, which will function as the parent, if needed. Also reference the config
        # entities whose combined data will makeup this instances ConfigEntity properties
        if kwargs['parent_config_entity']:
            self.config_entities = kwargs['parent_config_entity'].children()
        elif 'config_entities' in kwargs:
            # Just default to the GlobalConfig singleton. This could be smarter and traverse up all the config_entity
            # parents to find the common one.
            self.config_entities = kwargs['config_entities']

    def save(self, force_insert=False, force_update=False, using=None):
        """
            Overrides the default save to merge the self.config_entities properties after doing an initial save
        :param force_insert:
        :param force_update:
        :param using:
        :return:
        """

        # First save to create a pk
        super(CombinedConfigEntity, self).save(force_insert, force_update, using)
        # Add unique instances to each collection from the config_entities. References to the parent_config_entity's
        # instances will automatically be adopted first.
        for method in ConfigEntity.INHERITABLE_COLLECTIONS:
            # get the add_method or add_method_through method name
            getattr(self, '_add_{0}'.format(method))(
                *unique(
                    flat_map(
                        lambda config_entity: getattr(config_entity, 'computed_{0}'.format(method))(),
                        self.config_entities),
                    lambda instance: instance.pk))

        # Combine the bounds of the config_entities to make this instance's bounds
        self.bounds = MultiPolygon(map(lambda config_entity: config_entity.bounds.cascaded_union, self.config_entities))

    @classmethod
    def lineage(cls):
        """
            A PresentationConfig can have any ConfigEntity for a parent
        :param cls:
        :return:
        """
        return ConfigEntity.__subclasses__()

    class Meta(object):
        app_label = 'footprint'
