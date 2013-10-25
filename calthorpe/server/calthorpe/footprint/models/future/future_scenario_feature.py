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
from django.db import models
from footprint.managers.geo_inheritance_manager import GeoInheritanceManager
from footprint.models.config.built_form_feature import BuiltFormFeature
from footprint.models.geospatial.feature import Feature

__author__ = 'calthorpe'


class FutureScenarioFeature(Feature, BuiltFormFeature):
    """
        A dynamically subclassed abstract class that represents the canvas table for a specific Scenerio. Hence
        instances of subclasses of this class correspond to geography rows of the canvas table
    """
    objects = GeoInheritanceManager()

    dev_pct = models.DecimalField(max_digits=8, decimal_places=4, default=1.0000)
    density_pct = models.DecimalField(max_digits=8, decimal_places=4, default=1.0000)
    total_redev = models.BooleanField(default=False)
    dirty_flag = models.BooleanField(default=False)
    refill_flag = models.BooleanField(default=False)
    acres_gross = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_developable = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_developing = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_res = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_res_detsf_ll = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_res_detsf_sl = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_res_attsf = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_res_mf = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_emp = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_emp_ret = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_emp_off = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_emp_ind = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_emp_ag = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_emp_mixed = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_mixed = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_mixed_w_off = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_parcel_mixed_no_off = models.DecimalField(max_digits=14, decimal_places=4, default=0)

    pop = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    hh = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    du = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    du_detsf_ll = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    du_detsf_sl = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    du_attsf = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    du_mf = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_ret = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_retail_services = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_restaurant = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_accommodation = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_arts_entertainment = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_other_services = models.DecimalField(max_digits=14, decimal_places=4, default=0)

    emp_off = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_office_services = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_education = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_public_admin = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_medical_services = models.DecimalField(max_digits=14, decimal_places=4, default=0)

    emp_ind = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_wholesale = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_transport_warehousing = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_manufacturing = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_construction_utilities = models.DecimalField(max_digits=14, decimal_places=4, default=0)

    emp_ag = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_agriculture = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_extraction = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    emp_military = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_detsf_ll = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_detsf_sl = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_attsf = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_mf = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_retail_services = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_restaurant = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_accommodation = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_arts_entertainment = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_other_services = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_office_services = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_public_admin = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_medical_services = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_education = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_wholesale = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    bldg_sqft_transport_warehousing = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    commercial_irrigated_sqft = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    residential_irrigated_sqft = models.DecimalField(max_digits=14, decimal_places=4, default=0)

    class Meta(object):
        app_label = 'footprint'
        abstract = True


class TemplateScenarioBuiltFormFeature(FutureScenarioFeature):
    """
        Template subclass so that south generates migrations that we can apply to the dynamically generated subclasses
    """
    objects = GeoInheritanceManager()

    class Meta(object):
        app_label = 'footprint'
        abstract = False
