# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RailwayPlatforms(FixtureTest):

    def test_hunterspoint_avenue_lirr(self):
        # Hunterspoint Avenue LIRR
        self.generate_fixtures(dsl.way(326365794, wkt_loads('POLYGON ((-73.94851711356741 40.74180091168019, -73.9482813956369 40.74187591553309, -73.94775839647841 40.7420464775191, -73.9471744017122 40.7422648860637, -73.9470544766218 40.74231198435318, -73.94669461151902 40.74245307483899, -73.94561303991689 40.74287239699069, -73.94558348534409 40.74283251351719, -73.94619056681309 40.7425957984846, -73.94646940387729 40.74248778591118, -73.94700084719929 40.74228088042879, -73.94765949196569 40.74202810094948, -73.94800246874109 40.74191328130491, -73.94824977493879 40.7418352147232, -73.9484960031582 40.74176266104377, -73.94851711356741 40.74180091168019))'), {u'source': u'openstreetmap.org', u'railway': u'platform', u'way_area': u'2476.46', u'public_transport': u'platform', u'area': u'yes'}))
        self.assert_has_feature(
            16, 19306, 24633, 'transit',
            {'kind': 'platform'})
