
# get our code
          wget https://github.com/crc-si/opendatacube-cloudformation-testing/archive/master.zip -O /tmp/archive.zip
          unzip /tmp/archive.zip
          sudo mv  opendatacube-cloudformation-testing-master /opt/odc


	sudo mkdir -p /opt/odc/data
	sudo chown ubuntu /opt/odc/data
          wget https://landsat.usgs.gov/sites/default/files/documents/wrs2_asc_desc.zip -O /opt/odc/data/wrs2_asc_desc.zip

