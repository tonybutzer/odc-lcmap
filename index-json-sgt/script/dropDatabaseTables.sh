PGPASSWORD=localuser1234 psql -U dc_user datacube <dropTable.sql

# localuser1234

# -- list tables to be truncated
# \dt agdc.*


# -- actually truncate them
# Truncate agdc.dataset, agdc.dataset_location, agdc.dataset_source, agdc.dataset_type ;
