SELECT country_code, country_name, official_country_name, capital,
       united_nation_members, startOfWeek, independence, common_native_name, languages
FROM {{ref("bronze_layer")}}
