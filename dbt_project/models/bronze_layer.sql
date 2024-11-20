SELECT
    data:country_name::STRING AS country_name,
	data:independent::BOOLEAN AS independence,
    data:unMember::BOOLEAN AS united_nation_members,
	data:startOfWeek::STRING AS startOfWeek,
    data:official_country_name::STRING AS official_country_name,
	data:common_native_names::STRING AS common_native_name,
    data:currency_code::STRING AS currency_code,
	data:currency_name::STRING AS currency_name,
    data:currency_symbol::STRING AS currency_symbol,
	data:country_code::STRING AS country_code,
    data:capital::STRING AS capital,
	data:region::STRING AS region,
    data:subregion::STRING AS sub_region,
	data:languages::STRING AS languages,
    data:area::FLOAT AS area,
	data:population::INTEGER AS population,
    data:continents::STRING AS continents
FROM TRAVELS