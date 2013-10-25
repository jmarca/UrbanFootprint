/* 
* UrbanFootprint-California, Scenario Planning Model
* 
* Copyright (C) 2012-2013 Calthorpe Associates
* 
* This program is free software: you can redistribute it and/or modify it under the terms of the
* GNU General Public License as published by the Free Software Foundation, version 3 of the License.
* 
* This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
* without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
* See the GNU General Public License for more details.
* 
* You should have received a copy of the GNU General Public License along with this program.
* If not, see <http://www.gnu.org/licenses/>.
* 
* Contact: Calthorpe Associates (urbanfootprint@calthorpe.com)
* Firm contact: 2095 Rose Street Suite 201, Berkeley CA 94709.
* Phone: (510) 548-6800.      Web: www.calthorpe.com
* 
 */

/**
 *
 * Created with PyCharm.
 * User: calthorpe
 * Date: 9/9/13
 * Time: 11:53 AM
 * To change this template use File | Settings | File Templates.
 */

function isLightColor(color) {
    var rVal = color.substring(1,3);
    var gVal = color.substring(3,5);
    var bVal = color.substring(5,7);

    var grayscale = (parseInt(rVal,16) + parseInt(gVal,16) + parseInt(bVal,16))/3;
    return (grayscale < 150) ? false : true;
}
