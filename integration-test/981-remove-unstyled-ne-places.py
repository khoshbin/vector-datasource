# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RemoveUnstyledNePlaces(FixtureTest):

    def setUp(self):
        super(RemoveUnstyledNePlaces, self).setUp()
        self.generate_fixtures(dsl.way(1, wkt_loads('POINT (17.93400361745574 62.63399703907514)'), {u'labelrank': 7, u'max_bbymin': 0.0, u'max_bbymax': 0.0, u'namediff': 1, u'max_areami': 0.0, u'pop1960': 0.0, u'pop1965': 0.0, u'min_perkm': 0.0, u'max_pop50': 0, u'source': u'naturalearthdata.com', u'latitude': 62.6339970391, u'elevation': 0.0, u'diffnote': u'Added missing admin-1 capital. Population from GeoNames.', u'min_areakm': 0, u'namealt': u'', u'rank_min': 6, u'sov0name': u'Sweden', u'cityalt': u'', u'name': u'Harnosand', u'pop1995': 0.0, u'max_natsca': 0, u'pop1990': 0.0, u'max_pop20': 0, u'min_bbxmin': 0.0, u'adm0cap': 0.0, u'max_areakm': 0.0, u'natscale': 1, u'pop2010': 0.0, u'pop2015': 0.0, u'pop1985': 0.0, u'pop1980': 0.0, u'sov_a3': u'SWE', u'un_adm0': u'', u'ls_match': 0, u'namepar': u'', u'min_areami': 0.0, u'adm0name': u'Sweden', u'un_lat': 0.0, u'min_permi': 0.0, u'pop2000': 0.0, u'pop2005': 0.0, u'changed': 4.0, u'nameascii': u'Harnosand', u'geonamesno': u'GeoNames match general.', u'meganame': u'', u'scalerank': 10, u'ls_name': u'', u'gtopo30': 25.0, u'mean_bbyc': 0.0, u'iso_a2': u'SE', u'max_permi': 0.0, u'feature_co': u'PPLA', u'feature_cl': u'P', u'rank_max': 6, u'geonameid': 2707684.0, u'diffascii': 0, u'max_pop10': 0, u'min_bbymin': 0.0, u'pop_max': 17016, u'min_bbymax': 0.0, u'capalt': 0.0, u'mean_bbxc': 0.0, u'checkme': 0, u'megacity': 0, u'capin': u'', u'pop_min': 17016, u'pop2020': 0.0, u'longitude': 17.9340036175, u'pop2025': 0.0, u'min_bbxmax': 0.0, u'adm1name': u'VWsternorrland', u'pop1950': 0.0, u'pop1955': 0.0, u'max_pop310': 0, u'compare': 0, u'max_perkm': 0.0, u'admin1_cod': 24.0, u'adm0_a3': u'SWE', u'timezone': u'Europe/Stockholm', u'note': u'', u'pop2050': 0.0, u'worldcity': 0.0, u'un_long': 0.0, u'max_pop300': 0, u'max_bbxmin': 0.0, u'featurecla': u'Admin-1 capital', u'pop1975': 0.0, u'gn_ascii': u'Harnosand', u'pop1970': 0.0, u'max_bbxmax': 0.0, u'un_fid': 0, u'pop_other': 0, u'gn_pop': 17016}),dsl.way(2, wkt_loads('POINT (-123.7994307880426 39.30776735336368)'), {u'labelrank': 1, u'max_bbymin': 39.3, u'max_bbymax': 39.30833333, u'namediff': 0, u'max_areami': 1.0, u'pop1960': 0.0, u'pop1965': 0.0, u'min_perkm': 5.0, u'max_pop50': 0, u'source': u'naturalearthdata.com', u'latitude': 39.3077673534, u'elevation': 0.0, u'diffnote': u'Location adjusted.', u'min_areakm': 1, u'namealt': u'', u'rank_min': 2, u'sov0name': u'United States', u'cityalt': u'', u'name': u'Mendocino', u'pop1995': 0.0, u'max_natsca': 10, u'pop1990': 0.0, u'max_pop20': 0, u'min_bbxmin': -123.80833333, u'adm0cap': 0.0, u'max_areakm': 1.0, u'natscale': 10, u'pop2010': 0.0, u'pop2015': 0.0, u'pop1985': 0.0, u'pop1980': 0.0, u'sov_a3': u'USA', u'un_adm0': u'', u'ls_match': 1, u'namepar': u'', u'min_areami': 1.0, u'adm0name': u'United States of America', u'un_lat': 0.0, u'min_permi': 3.0, u'pop2000': 0.0, u'pop2005': 0.0, u'changed': 4.0, u'nameascii': u'Mendocino', u'geonamesno': u'No GeoNames match due to small population, not in GeoNames, or poor NEV placement.', u'meganame': u'', u'scalerank': 8, u'ls_name': u'Mendocino', u'gtopo30': 0.0, u'mean_bbyc': 39.30416667, u'iso_a2': u'US', u'max_permi': 3.0, u'feature_co': u'', u'feature_cl': u'', u'rank_max': 2, u'geonameid': -1.0, u'diffascii': 0, u'max_pop10': 548, u'min_bbymin': 39.3, u'pop_max': 548, u'min_bbymax': 39.30833333, u'capalt': 0.0, u'mean_bbxc': -123.8, u'checkme': 0, u'megacity': 0, u'capin': u'', u'pop_min': 548, u'pop2020': 0.0, u'longitude': -123.799430788, u'pop2025': 0.0, u'min_bbxmax': -123.79166667, u'adm1name': u'California', u'pop1950': 0.0, u'pop1955': 0.0, u'max_pop310': 0, u'compare': 0, u'max_perkm': 5.0, u'admin1_cod': 0.0, u'adm0_a3': u'USA', u'timezone': u'', u'note': u'', u'pop2050': 0.0, u'worldcity': 0.0, u'un_long': 0.0, u'max_pop300': 0, u'max_bbxmin': -123.80833333, u'featurecla': u'Populated place', u'pop1975': 0.0, u'gn_ascii': u'', u'pop1970': 0.0, u'max_bbxmax': -123.79166667, u'un_fid': 0, u'pop_other': 548, u'gn_pop': 0}),dsl.way(3, wkt_loads('POINT (-62.08996749026979 -31.43003375369007)'), {u'labelrank': 3, u'max_bbymin': -31.45, u'max_bbymax': -31.40833333, u'namediff': 0, u'max_areami': 7.0, u'pop1960': 0.0, u'pop1965': 0.0, u'min_perkm': 21.0, u'max_pop50': 0, u'source': u'naturalearthdata.com', u'latitude': -31.4300337537, u'elevation': 0.0, u'diffnote': u'', u'min_areakm': 19, u'namealt': u'', u'rank_min': 7, u'sov0name': u'Argentina', u'cityalt': u'', u'name': u'San Francisco', u'pop1995': 0.0, u'max_natsca': 10, u'pop1990': 0.0, u'max_pop20': 0, u'min_bbxmin': -62.10833333, u'adm0cap': 0.0, u'max_areakm': 19.0, u'natscale': 10, u'pop2010': 0.0, u'pop2015': 0.0, u'pop1985': 0.0, u'pop1980': 0.0, u'sov_a3': u'ARG', u'un_adm0': u'', u'ls_match': 1, u'namepar': u'', u'min_areami': 7.0, u'adm0name': u'Argentina', u'un_lat': 0.0, u'min_permi': 13.0, u'pop2000': 0.0, u'pop2005': 0.0, u'changed': 0.0, u'nameascii': u'San Francisco', u'geonamesno': u'Geonames ascii name + lat.d + long.d matching.', u'meganame': u'', u'scalerank': 8, u'ls_name': u'San Francisco2', u'gtopo30': 123.0, u'mean_bbyc': -31.42948718, u'iso_a2': u'AR', u'max_permi': 13.0, u'feature_co': u'PPL', u'feature_cl': u'P', u'rank_max': 8, u'geonameid': 3837675.0, u'diffascii': 0, u'max_pop10': 27400, u'min_bbymin': -31.45, u'pop_max': 59062, u'min_bbymax': -31.40833333, u'capalt': 0.0, u'mean_bbxc': -62.08269231, u'checkme': 2, u'megacity': 0, u'capin': u'', u'pop_min': 27400, u'pop2020': 0.0, u'longitude': -62.0899674903, u'pop2025': 0.0, u'min_bbxmax': -62.05, u'adm1name': u'CRrdoba', u'pop1950': 0.0, u'pop1955': 0.0, u'max_pop310': 0, u'compare': 0, u'max_perkm': 21.0, u'admin1_cod': 5.0, u'adm0_a3': u'ARG', u'timezone': u'America/Argentina/Cordoba', u'note': u'', u'pop2050': 0.0, u'worldcity': 0.0, u'un_long': 0.0, u'max_pop300': 0, u'max_bbxmin': -62.10833333, u'featurecla': u'Populated place', u'pop1975': 0.0, u'gn_ascii': u'San Francisco', u'pop1970': 0.0, u'max_bbxmax': -62.05, u'un_fid': 0, u'pop_other': 27400, u'gn_pop': 59062}),dsl.way(4, wkt_loads('POINT (-124.0882245299058 40.88519044907326)'), {u'labelrank': 1, u'max_bbymin': 40.84166667, u'max_bbymax': 40.91666667, u'namediff': 0, u'max_areami': 8.0, u'pop1960': 0.0, u'pop1965': 0.0, u'min_perkm': 26.0, u'max_pop50': 0, u'source': u'naturalearthdata.com', u'latitude': 40.8851904491, u'elevation': 7.0, u'diffnote': u'Location adjusted. Changed scale rank.', u'min_areakm': 20, u'namealt': u'', u'rank_min': 6, u'sov0name': u'United States', u'cityalt': u'', u'name': u'Arcata', u'pop1995': 0.0, u'max_natsca': 10, u'pop1990': 0.0, u'max_pop20': 0, u'min_bbxmin': -124.10833333, u'adm0cap': 0.0, u'max_areakm': 20.0, u'natscale': 20, u'pop2010': 0.0, u'pop2015': 0.0, u'pop1985': 0.0, u'pop1980': 0.0, u'sov_a3': u'USA', u'un_adm0': u'', u'ls_match': 1, u'namepar': u'', u'min_areami': 8.0, u'adm0name': u'United States of America', u'un_lat': 0.0, u'min_permi': 16.0, u'pop2000': 0.0, u'pop2005': 0.0, u'changed': 4.0, u'nameascii': u'Arcata', u'geonamesno': u'Geonames ascii name + lat.d + long.d matching.', u'meganame': u'', u'scalerank': 7, u'ls_name': u'Arcata', u'gtopo30': 38.0, u'mean_bbyc': 40.87777778, u'iso_a2': u'US', u'max_permi': 16.0, u'feature_co': u'PPL', u'feature_cl': u'P', u'rank_max': 7, u'geonameid': 5558953.0, u'diffascii': 0, u'max_pop10': 20905, u'min_bbymin': 40.84166667, u'pop_max': 20905, u'min_bbymax': 40.91666667, u'capalt': 0.0, u'mean_bbxc': -124.08138889, u'checkme': 0, u'megacity': 0, u'capin': u'', u'pop_min': 17199, u'pop2020': 0.0, u'longitude': -124.08822453, u'pop2025': 0.0, u'min_bbxmax': -124.05833333, u'adm1name': u'California', u'pop1950': 0.0, u'pop1955': 0.0, u'max_pop310': 0, u'compare': 0, u'max_perkm': 26.0, u'admin1_cod': 0.0, u'adm0_a3': u'USA', u'timezone': u'America/Los_Angeles', u'note': u'', u'pop2050': 0.0, u'worldcity': 0.0, u'un_long': 0.0, u'max_pop300': 0, u'max_bbxmin': -124.10833333, u'featurecla': u'Populated place', u'pop1975': 0.0, u'gn_ascii': u'Arcata', u'pop1970': 0.0, u'max_bbxmax': -124.05833333, u'un_fid': 0, u'pop_other': 20774, u'gn_pop': 17199}),dsl.way(5, wkt_loads('POINT (-123.2108620624544 39.15423667302469)'), {u'labelrank': 1, u'max_bbymin': 39.1, u'max_bbymax': 39.21666667, u'namediff': 0, u'max_areami': 10.0, u'pop1960': 0.0, u'pop1965': 0.0, u'min_perkm': 35.0, u'max_pop50': 0, u'source': u'naturalearthdata.com', u'latitude': 39.154236673, u'elevation': 193.0, u'diffnote': u'Location adjusted.', u'min_areakm': 25, u'namealt': u'', u'rank_min': 6, u'sov0name': u'United States', u'cityalt': u'', u'name': u'Ukiah', u'pop1995': 0.0, u'max_natsca': 20, u'pop1990': 0.0, u'max_pop20': 27828, u'min_bbxmin': -123.23333333, u'adm0cap': 0.0, u'max_areakm': 25.0, u'natscale': 20, u'pop2010': 0.0, u'pop2015': 0.0, u'pop1985': 0.0, u'pop1980': 0.0, u'sov_a3': u'USA', u'un_adm0': u'', u'ls_match': 1, u'namepar': u'', u'min_areami': 10.0, u'adm0name': u'United States of America', u'un_lat': 0.0, u'min_permi': 22.0, u'pop2000': 0.0, u'pop2005': 0.0, u'changed': 4.0, u'nameascii': u'Ukiah', u'geonamesno': u'Geonames ascii name + lat.d + long.d matching.', u'meganame': u'', u'scalerank': 7, u'ls_name': u'Ukiah', u'gtopo30': 189.0, u'mean_bbyc': 39.1588964, u'iso_a2': u'US', u'max_permi': 22.0, u'feature_co': u'PPL', u'feature_cl': u'P', u'rank_max': 7, u'geonameid': 5404476.0, u'diffascii': 0, u'max_pop10': 27828, u'min_bbymin': 39.1, u'pop_max': 27828, u'min_bbymax': 39.21666667, u'capalt': 0.0, u'mean_bbxc': -123.20686937, u'checkme': 0, u'megacity': 0, u'capin': u'', u'pop_min': 15825, u'pop2020': 0.0, u'longitude': -123.210862062, u'pop2025': 0.0, u'min_bbxmax': -123.18333333, u'adm1name': u'California', u'pop1950': 0.0, u'pop1955': 0.0, u'max_pop310': 0, u'compare': 0, u'max_perkm': 35.0, u'admin1_cod': 0.0, u'adm0_a3': u'USA', u'timezone': u'America/Los_Angeles', u'note': u'', u'pop2050': 0.0, u'worldcity': 0.0, u'un_long': 0.0, u'max_pop300': 0, u'max_bbxmin': -123.23333333, u'featurecla': u'Populated place', u'pop1975': 0.0, u'gn_ascii': u'Ukiah', u'pop1970': 0.0, u'max_bbxmax': -123.18333333, u'un_fid': 0, u'pop_other': 27537, u'gn_pop': 15825}),dsl.way(6, wkt_loads('POINT (-122.8744226500182 42.32662701320668)'), {u'labelrank': 1, u'max_bbymin': 42.25833333, u'max_bbymax': 42.41666667, u'namediff': 0, u'max_areami': 33.0, u'pop1960': 0.0, u'pop1965': 0.0, u'min_perkm': 86.0, u'max_pop50': 0, u'source': u'naturalearthdata.com', u'latitude': 42.3266270132, u'elevation': 421.0, u'diffnote': u'Changed scale rank.', u'min_areakm': 85, u'namealt': u'', u'rank_min': 8, u'sov0name': u'United States', u'cityalt': u'', u'name': u'Medford', u'pop1995': 0.0, u'max_natsca': 10, u'pop1990': 0.0, u'max_pop20': 0, u'min_bbxmin': -122.93333333, u'adm0cap': 0.0, u'max_areakm': 85.0, u'natscale': 30, u'pop2010': 0.0, u'pop2015': 0.0, u'pop1985': 0.0, u'pop1980': 0.0, u'sov_a3': u'USA', u'un_adm0': u'', u'ls_match': 1, u'namepar': u'', u'min_areami': 33.0, u'adm0name': u'United States of America', u'un_lat': 0.0, u'min_permi': 54.0, u'pop2000': 0.0, u'pop2005': 0.0, u'changed': 1.0, u'nameascii': u'Medford', u'geonamesno': u'Geonames ascii name + lat.d + long.d matching.', u'meganame': u'', u'scalerank': 6, u'ls_name': u'Medford', u'gtopo30': 422.0, u'mean_bbyc': 42.33538557, u'iso_a2': u'US', u'max_permi': 54.0, u'feature_co': u'PPL', u'feature_cl': u'P', u'rank_max': 9, u'geonameid': 5740099.0, u'diffascii': 0, u'max_pop10': 108525, u'min_bbymin': 42.25833333, u'pop_max': 108525, u'min_bbymax': 42.41666667, u'capalt': 0.0, u'mean_bbxc': -122.86834577, u'checkme': 0, u'megacity': 0, u'capin': u'', u'pop_min': 69638, u'pop2020': 0.0, u'longitude': -122.87442265, u'pop2025': 0.0, u'min_bbxmax': -122.8, u'adm1name': u'Oregon', u'pop1950': 0.0, u'pop1955': 0.0, u'max_pop310': 0, u'compare': 0, u'max_perkm': 86.0, u'admin1_cod': 0.0, u'adm0_a3': u'USA', u'timezone': u'America/Los_Angeles', u'note': u'', u'pop2050': 0.0, u'worldcity': 0.0, u'un_long': 0.0, u'max_pop300': 0, u'max_bbxmin': -122.93333333, u'featurecla': u'Populated place', u'pop1975': 0.0, u'gn_ascii': u'Medford', u'pop1970': 0.0, u'max_bbxmax': -122.8, u'un_fid': 0, u'pop_other': 105789, u'gn_pop': 69638}),dsl.way(7, wkt_loads('POINT (-124.1474973977446 40.80222393702851)'), {u'labelrank': 1, u'max_bbymin': 40.725, u'max_bbymax': 40.80833333, u'namediff': 0, u'max_areami': 14.0, u'pop1960': 0.0, u'pop1965': 0.0, u'min_perkm': 39.0, u'max_pop50': 42398, u'source': u'naturalearthdata.com', u'latitude': 40.802223937, u'elevation': 12.0, u'diffnote': u'Location adjusted.', u'min_areakm': 36, u'namealt': u'', u'rank_min': 7, u'sov0name': u'United States', u'cityalt': u'', u'name': u'Eureka', u'pop1995': 0.0, u'max_natsca': 50, u'pop1990': 0.0, u'max_pop20': 42398, u'min_bbxmin': -124.2, u'adm0cap': 0.0, u'max_areakm': 36.0, u'natscale': 50, u'pop2010': 0.0, u'pop2015': 0.0, u'pop1985': 0.0, u'pop1980': 0.0, u'sov_a3': u'USA', u'un_adm0': u'', u'ls_match': 1, u'namepar': u'', u'min_areami': 14.0, u'adm0name': u'United States of America', u'un_lat': 0.0, u'min_permi': 24.0, u'pop2000': 0.0, u'pop2005': 0.0, u'changed': 4.0, u'nameascii': u'Eureka', u'geonamesno': u'Geonames ascii name + lat.d + long.d matching.', u'meganame': u'', u'scalerank': 4, u'ls_name': u'Eureka', u'gtopo30': 1.0, u'mean_bbyc': 40.77871212, u'iso_a2': u'US', u'max_permi': 24.0, u'feature_co': u'PPL', u'feature_cl': u'P', u'rank_max': 7, u'geonameid': 5563397.0, u'diffascii': 0, u'max_pop10': 42398, u'min_bbymin': 40.725, u'pop_max': 42398, u'min_bbymax': 40.80833333, u'capalt': 0.0, u'mean_bbxc': -124.15810606, u'checkme': 0, u'megacity': 0, u'capin': u'', u'pop_min': 25626, u'pop2020': 0.0, u'longitude': -124.147497398, u'pop2025': 0.0, u'min_bbxmax': -124.11666667, u'adm1name': u'California', u'pop1950': 0.0, u'pop1955': 0.0, u'max_pop310': 0, u'compare': 0, u'max_perkm': 39.0, u'admin1_cod': 0.0, u'adm0_a3': u'USA', u'timezone': u'America/Los_Angeles', u'note': u'', u'pop2050': 0.0, u'worldcity': 0.0, u'un_long': 0.0, u'max_pop300': 0, u'max_bbxmin': -124.2, u'featurecla': u'Populated place', u'pop1975': 0.0, u'gn_ascii': u'Eureka', u'pop1970': 0.0, u'max_bbxmax': -124.11666667, u'un_fid': 0, u'pop_other': 0, u'gn_pop': 25626}),dsl.way(8, wkt_loads('POINT (-122.3419308458685 47.57194791253073)'), {u'labelrank': 1, u'max_bbymin': 47.27965768, u'max_bbymax': 48.01666667, u'namediff': 0, u'max_areami': 759.0, u'pop1960': 1089.0, u'pop1965': 1305.0, u'min_perkm': 608.0, u'max_pop50': 2678987, u'source': u'naturalearthdata.com', u'latitude': 47.5700020539, u'elevation': 56.0, u'diffnote': u'Changed scale rank.', u'min_areakm': 977, u'namealt': u'', u'rank_min': 11, u'sov0name': u'United States', u'cityalt': u'', u'name': u'Seattle', u'pop1995': 2453.0, u'max_natsca': 100, u'pop1990': 2206.0, u'max_pop20': 1627475, u'min_bbxmin': -122.66666667, u'adm0cap': 0.0, u'max_areakm': 1966.0, u'natscale': 200, u'pop2010': 3074.0, u'pop2015': 3174.0, u'pop1985': 1982.0, u'pop1980': 1780.0, u'sov_a3': u'USA', u'un_adm0': u'United States of America', u'ls_match': 1, u'namepar': u'', u'min_areami': 377.0, u'adm0name': u'United States of America', u'un_lat': 47.58, u'min_permi': 378.0, u'pop2000': 2727.0, u'pop2005': 2991.0, u'changed': 5.0, u'nameascii': u'Seattle', u'geonamesno': u'Geonames ascii name + lat.d + long.d matching.', u'meganame': u'Seattle', u'scalerank': 2, u'ls_name': u'Seattle', u'gtopo30': 60.0, u'mean_bbyc': 47.5191207875, u'iso_a2': u'US', u'max_permi': 721.0, u'feature_co': u'PPL', u'feature_cl': u'P', u'rank_max': 12, u'geonameid': 5809844.0, u'diffascii': 0, u'max_pop10': 1627475, u'min_bbymin': 47.01666667, u'pop_max': 3074000, u'min_bbymax': 47.8087148, u'capalt': 0.0, u'mean_bbxc': -122.248573925, u'checkme': 0, u'megacity': 1, u'capin': u'', u'pop_min': 569369, u'pop2020': 3305.0, u'longitude': -122.339984987, u'pop2025': 3415.0, u'min_bbxmax': -121.96666667, u'adm1name': u'Washington', u'pop1950': 795.0, u'pop1955': 930.0, u'max_pop310': 0, u'compare': 0, u'max_perkm': 1161.0, u'admin1_cod': 0.0, u'adm0_a3': u'USA', u'timezone': u'America/Los_Angeles', u'note': u'', u'pop2050': 3503.0, u'worldcity': 0.0, u'un_long': -122.31, u'max_pop300': 2789620, u'max_bbxmin': -122.425, u'featurecla': u'Populated place', u'pop1975': 1663.0, u'gn_ascii': u'Seattle', u'pop1970': 1556.0, u'max_bbxmax': -121.96666667, u'un_fid': 572, u'pop_other': 1535603, u'gn_pop': 569369}),dsl.way(9, wkt_loads('POINT (-122.4171687735523 37.76919562968742)'), {u'labelrank': 1, u'max_bbymin': 37.575, u'max_bbymax': 38.04166667, u'namediff': 0, u'max_areami': 675.0, u'pop1960': 2200.0, u'pop1965': 2361.0, u'min_perkm': 126.0, u'max_pop50': 1371285, u'source': u'naturalearthdata.com', u'latitude': 37.7400077505, u'elevation': 16.0, u'diffnote': u'', u'min_areakm': 218, u'namealt': u'San Francisco-Oakland', u'rank_min': 11, u'sov0name': u'United States', u'cityalt': u'San Francisco', u'name': u'San Francisco', u'pop1995': 3095.0, u'max_natsca': 300, u'pop1990': 2961.0, u'max_pop20': 1130999, u'min_bbxmin': -122.51666667, u'adm0cap': 0.0, u'max_areakm': 1748.0, u'natscale': 300, u'pop2010': 3450.0, u'pop2015': 3544.0, u'pop1985': 2805.0, u'pop1980': 2656.0, u'sov_a3': u'USA', u'un_adm0': u'United States of America', u'ls_match': 1, u'namepar': u'', u'min_areami': 84.0, u'adm0name': u'United States of America', u'un_lat': 37.79, u'min_permi': 78.0, u'pop2000': 3236.0, u'pop2005': 3387.0, u'changed': 0.0, u'nameascii': u'San Francisco', u'geonamesno': u'GeoNames match with ascii name + lat + long whole numbers.', u'meganame': u'San Francisco-Oakland', u'scalerank': 1, u'ls_name': u'San Francisco1', u'gtopo30': 60.0, u'mean_bbyc': 37.62228831, u'iso_a2': u'US', u'max_permi': 469.0, u'feature_co': u'PPL', u'feature_cl': u'P', u'rank_max': 12, u'geonameid': 5391959.0, u'diffascii': 0, u'max_pop10': 988636, u'min_bbymin': 37.19166667, u'pop_max': 3450000, u'min_bbymax': 37.81666667, u'capalt': 0.0, u'mean_bbxc': -122.301354098, u'checkme': 0, u'megacity': 1, u'capin': u'', u'pop_min': 732072, u'pop2020': 3684.0, u'longitude': -122.459977663, u'pop2025': 3803.0, u'min_bbxmax': -122.35833333, u'adm1name': u'California', u'pop1950': 1855.0, u'pop1955': 2021.0, u'max_pop310': 4561697, u'compare': 0, u'max_perkm': 755.0, u'admin1_cod': 0.0, u'adm0_a3': u'USA', u'timezone': u'America/Los_Angeles', u'note': u'', u'pop2050': 3898.0, u'worldcity': 1.0, u'un_long': -122.38, u'max_pop300': 4561697, u'max_bbxmin': -122.51666667, u'featurecla': u'Populated place', u'pop1975': 2590.0, u'gn_ascii': u'San Francisco', u'pop1970': 2529.0, u'max_bbxmax': -121.73333333, u'un_fid': 570, u'pop_other': 27400, u'gn_pop': 732072}),dsl.way(10, wkt_loads('POINT (-73.98196278740683 40.75192492259462)'), {u'labelrank': 1, u'max_bbymin': 40.56666667, u'max_bbymax': 41.94166667, u'namediff': 0, u'max_areami': 3160.0, u'pop1960': 14164.0, u'pop1965': 15177.0, u'min_perkm': 497.0, u'max_pop50': 18788144, u'source': u'naturalearthdata.com', u'latitude': 40.749979064, u'elevation': 10.0, u'diffnote': u'', u'min_areakm': 1137, u'namealt': u'New York-Newark', u'rank_min': 13, u'sov0name': u'United States', u'cityalt': u'New York', u'name': u'New York', u'pop1995': 16943.0, u'max_natsca': 300, u'pop1990': 16086.0, u'max_pop20': 11947707, u'min_bbxmin': -74.75, u'adm0cap': 0.0, u'max_areakm': 8185.0, u'natscale': 600, u'pop2010': 19040.0, u'pop2015': 19441.0, u'pop1985': 15827.0, u'pop1980': 15601.0, u'sov_a3': u'USA', u'un_adm0': u'United States of America', u'ls_match': 1, u'namepar': u'', u'min_areami': 439.0, u'adm0name': u'United States of America', u'un_lat': 40.7, u'min_permi': 309.0, u'pop2000': 17846.0, u'pop2005': 18732.0, u'changed': 0.0, u'nameascii': u'New York', u'geonamesno': u'GeoNames spatial join with similar names only.', u'meganame': u'New York-Newark', u'scalerank': 0, u'ls_name': u'New York', u'gtopo30': 2.0, u'mean_bbyc': 40.813006048, u'iso_a2': u'US', u'max_permi': 3102.0, u'feature_co': u'PPL', u'feature_cl': u'P', u'rank_max': 14, u'geonameid': 5128581.0, u'diffascii': 0, u'max_pop10': 9376946, u'min_bbymin': 39.80833333, u'pop_max': 19040000, u'min_bbymax': 41.0572371, u'capalt': 0.0, u'mean_bbxc': -73.815782408, u'checkme': 0, u'megacity': 1, u'capin': u'UN Headquarters', u'pop_min': 8008278, u'pop2020': 19974.0, u'longitude': -73.9800169288, u'pop2025': 20370.0, u'min_bbxmax': -73.57494554, u'adm1name': u'New York', u'pop1950': 12338.0, u'pop1955': 13219.0, u'max_pop310': 18924578, u'compare': 0, u'max_perkm': 4993.0, u'admin1_cod': 0.0, u'adm0_a3': u'USA', u'timezone': u'America/New_York', u'note': u'', u'pop2050': 20628.0, u'worldcity': 1.0, u'un_long': -73.9, u'max_pop300': 18788144, u'max_bbxmin': -74.09143148, u'featurecla': u'Populated place', u'pop1975': 15880.0, u'gn_ascii': u'New York City', u'pop1970': 16191.0, u'max_bbxmax': -72.71666667, u'un_fid': 555, u'pop_other': 9292603, u'gn_pop': 8008278}))

    def assert_add_place(self, z, x, y, name):
        self.assert_has_feature(
            z, x, y, 'places',
            {'kind': 'locality', 'name': name,
             'source': 'naturalearthdata.com',
             'min_zoom': z})
        self.assert_no_matching_feature(
            z-1, x/2, y/2, 'places',
            {'kind': 'locality', 'name': name,
             'source': 'naturalearthdata.com'})

    def assert_remove_place(self, z, x, y, name):
        self.assert_no_matching_feature(
            z, x, y, 'places',
            {'kind': 'locality', 'name': name,
             'source': 'naturalearthdata.com'})
        self.assert_has_feature(
            z-1, x/2, y/2, 'places',
            {'kind': 'locality', 'name': name,
             'source': 'naturalearthdata.com'})

    def test_z2_add_nyc(self):
        # z2: Add New York City
        self.assert_add_place(2, 1, 1, 'New York')

    def test_z3_add_sf(self):
        # z3: Add San Francisco
        self.assert_add_place(3, 1, 3, 'San Francisco')

    def test_z4_add_seattle(self):
        # z4: Add Seattle
        self.assert_add_place(4, 2, 5, 'Seattle')

    def test_z5_add_eureka(self):
        # z5: Add Eureka, California
        self.assert_add_place(5, 4, 12, 'Eureka')

    def test_z6_add_medford(self):
        # z6: Add Medford, Oregon
        self.assert_add_place(6, 10, 23, 'Medford')

    def test_z7_add_arcata(self):
        # z7: Add Arcata, California
        self.assert_add_place(7, 19, 48, 'Arcata')
        self.assert_add_place(7, 20, 48, 'Ukiah')

    def test_z8_remove_nyc(self):
        # z8: Remainder Ukiah, California
        self.assert_remove_place(8, 75, 96, 'New York')
        self.assert_remove_place(8, 40, 94, 'Medford')

    def test_z9_add_mendocino(self):
        # z9: Remainder Mendocino, California
        self.assert_add_place(9, 79, 195, 'Mendocino')

    def test_z10_add_harnosand(self):
        # z10: Remainder Harnosand, Sweden (62.6339970391, 17.9340036175)
        self.assert_add_place(10, 563, 281, 'Harnosand')
        self.assert_remove_place(10, 159, 384, 'Arcata')
        self.assert_remove_place(10, 161, 390, 'Ukiah')

    def test_z11_mendocino_exists(self):
        # z11 Mendocino should still be here
        self.assert_has_feature(
            9, 79, 195, 'places',
            {'kind': 'locality', 'name': 'Mendocino',
             'source': 'naturalearthdata.com'})
