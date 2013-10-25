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

from footprint.initialization.fixture import LandUseSymbologyFixture

__author__ = 'calthorpe'


class ScagLandUseSymbology(LandUseSymbologyFixture):
    """
    a resource for translating SACOG's land uses into UF Built Forms
    """
    def land_use_color_lookup(self):
        return {
            '1000': '#CD6666',
            '1100': '#E3C400',
            '1110': '#FFFF00',
            '1111': '#FFFF00',
            '1112': '#FFFF00',
            '1113': '#FFFF00',
            '1120': '#FFAA00',
            '1121': '#FFAA00',
            '1122': '#FFAA00',
            '1123': '#FFAA00',
            '1124': '#FFAA00',
            '1125': '#FFAA00',
            '1130': '#FFEBAA',
            '1131': '#FFEBAA',
            '1132': '#FFEBAA',
            '1140': '#E3C400',
            '1200': '#FF0000',
            '1210': '#9C0000',
            '1211': '#9C0000',
            '1212': '#9C0000',
            '1213': '#9C0000',
            '1220': '#FF0000',
            '1221': '#FF0000',
            '1222': '#FF0000',
            '1223': '#FF0000',
            '1230': '#FF0000',
            '1231': '#FF0000',
            '1232': '#FF0000',
            '1233': '#FF0000',
            '1240': '#7A8EF5',
            '1241': '#7A8EF5',
            '1242': '#7A8EF5',
            '1243': '#7A8EF5',
            '1244': '#7A8EF5',
            '1245': '#7A8EF5',
            '1246': '#7A8EF5',
            '1247': '#7A8EF5',
            '1250': '#7A8EF5',
            '1251': '#7A8EF5',
            '1252': '#7A8EF5',
            '1253': '#7A8EF5',
            '1260': '#77B3D7',
            '1261': '#77B3D7',
            '1262': '#77B3D7',
            '1263': '#77B3D7',
            '1264': '#77B3D7',
            '1265': '#77B3D7',
            '1266': '#77B3D7',
            '1270': '#8400A8',
            '1271': '#8400A8',
            '1272': '#8400A8',
            '1273': '#8400A8',
            '1274': '#8400A8',
            '1275': '#8400A8',
            '1276': '#8400A8',
            '1300': '#0033CF',
            '1310': '#0033CF',
            '1311': '#0033CF',
            '1312': '#0033CF',
            '1313': '#0033CF',
            '1314': '#0033CF',
            '1320': '#0033CF',
            '1321': '#0033CF',
            '1322': '#0033CF',
            '1323': '#0033CF',
            '1324': '#0033CF',
            '1325': '#0033CF',
            '1330': '#0033CF',
            '1331': '#0033CF',
            '1332': '#0033CF',
            '1340': '#0033CF',
            '1400': '#9C9C9C',
            '1410': '#9C9C9C',
            '1411': '#9C9C9C',
            '1412': '#9C9C9C',
            '1413': '#9C9C9C',
            '1414': '#9C9C9C',
            '1415': '#9C9C9C',
            '1416': '#9C9C9C',
            '1417': '#9C9C9C',
            '1418': '#9C9C9C',
            '1420': '#9C9C9C',
            '1430': '#9C9C9C',
            '1431': '#9C9C9C',
            '1432': '#9C9C9C',
            '1433': '#9C9C9C',
            '1434': '#9C9C9C',
            '1435': '#9C9C9C',
            '1436': '#9C9C9C',
            '1437': '#9C9C9C',
            '1438': '#9C9C9C',
            '1440': '#9C9C9C',
            '1441': '#9C9C9C',
            '1442': '#9C9C9C',
            '1450': '#9C9C9C',
            '1460': '#9C9C9C',
            '1500': '#DF73FF',
            '1600': '#A87000',
            '1700': '#595959',
            '1800': '#4CE600',
            '1810': '#4CE600',
            '1820': '#4CE600',
            '1830': '#4CE600',
            '1840': '#4CE600',
            '1850': '#4CE600',
            '1860': '#4CE600',
            '1870': '#4CE600',
            '1880': '#4CE600',
            '1900': '#A8A800',
            '2000': '#267300',
            '2100': '#267300',
            '2110': '#267300',
            '2120': '#267300',
            '2200': '#267300',
            '2300': '#267300',
            '2400': '#267300',
            '2500': '#267300',
            '2600': '#267300',
            '2700': '#267300',
            '3000': '#A8A800',
            '3100': '#A8A800',
            '3200': '#A8A800',
            '3300': '#A8A800',
            '3400': '#A8A800',
            '4000': '#BEFFE8',
            '4100': '#BEFFE8',
            '4200': '#BEFFE8',
            '4300': '#BEFFE8',
            '4400': '#BEFFE8',
            '4500': '#BEFFE8',
            '8888': '#D1FF73',
            '9999': '#CCCCCC'
        }
