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
 * Created with PyCharm.
 * User: calthorpe
 * Date: 10/21/13
 * Time: 10:23 AM
 * To change this template use File | Settings | File Templates.
 */

sc_require('views/editable_model_string_view');
sc_require('views/info_views/info_view');
sc_require('views/info_views/range_item_view');

Footprint.EditableStringView = Footprint.InfoView.extend({
    classNames:'footprint-editable-string-view'.w(),
    value:null,
    contentStatus:null,
    contentStatusBinding:SC.Binding.oneWay('*content.status'),

    contentView: Footprint.EditableModelStringView.extend({
        layout: {width:.99, height: 0.99},
        isEditableBinding: parentViewPath(1, '.isEditable'),
        valueBinding: parentViewPath(1, '*value')
    }),

    // Don't use the range to display string ranges
    initBindings: function() {
        this.bind('value', this, "%@".fmt(this.get('attribute')));
    }
});


Footprint.StringRangeItemView = Footprint.RangeItemView.extend({
    classNames:'footprint-string-range-item-view'.w(),
    contentView: Footprint.EditableModelStringView.extend({
        layout: {width:.99, height: 0.99},
        isEditableBinding: parentViewPath(1, '.isEditable'),
        valueBinding: parentViewPath(1, '*value')
    }),

    // Don't use the range to display string ranges
    initBindings: function() {
        this.bind('value', this, "%@".fmt(this.get('attribute')));
    }

});
