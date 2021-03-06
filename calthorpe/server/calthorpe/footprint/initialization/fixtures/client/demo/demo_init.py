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

#
from footprint.initialization.fixture import InitFixture


class DemoInitFixture(InitFixture):
    def model_class_modules(self):
        """
            SACOG defines additional concrete model classes in the following modules
        :return:
        """
        return [
            ("built_form", "land_use_definition"),
            ("built_form", "land_use")
        ]

    def import_database(self):
        return dict(
            host='10.0.0.133',
            database='urbanfootprint_demo',
            user='calthorpe',
            password='Calthorpe123'
        )
