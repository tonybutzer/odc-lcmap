# 2018 ODC/LCMAP Special Study Annual Report

## Ongoing Research Questions

- **Should LCMAP use ODC?** -- Should USGS EROS use the Open Data Cube [framework, library, preparation scripts, and persistent postgresql database] as a cloud based infrastructure replacing (or doing the same job as) the on-premise infrastructure consisting of a Science Execution Engine and Information Warehouse and Data Store?

``` White paper to be delivered in June of 2019. ```

* How do we "Place our Big Data in cloud object storage in a self-describing, cloud-optimized format." ?

[Pangeo's Answer](https://medium.com/pangeo/step-by-step-guide-to-building-a-big-data-portal-e262af1c2977)

```Place your Big Data in cloud object storage in a self-describing, cloud-optimized format.```

> " In the cloud, users bring the computing to your data, not the other way around."

> "So if your data are self-describing, cloud-optimized, and stored in cloud object storage, you don’t actually need a portal. The data are already ready for direct access and scientific use. That’s great news, because portals take work to create and maintain. And despite the best intentions of data providers, portals are usually annoying. As a user of scientific data, whenever I encounter a fancy portal, the first thing I do is just look for the link to the FTP server where I can access the raw files. Then I use wget to suck them out into my personal dark replica." - Ryan Abernathey Assistant Professor, Earth & Environmental Sciences, Columbia University



* What would an ODC as a Service Architecture Look like in the cloud supporting emerging Collection 2 Landsat Data?
  * Develop a Conops for ODC as an USGS Landsat Delivery Service?

## Accomplishments

### USGS ODC Special Study Web Site Version 1.0 Completed 
1. Delivered on time and within budget

### LCMAP Accomplishments

1. Began code study of lcmap-pyccd
2. Began code study of lcmap-chipmunk
3. Began cody study of lcmap-merlin
4. Studied rationale for using functional programming methods over object oriented or structured (top-down) techniques
5. Acquired test data over Oregon as processed by the USGS EROS mesos cluster
6. Completed a **pyccd** prototype supported on top of a AWS hosted **Open Data Cube instance** for Oregon tiles and chips consistent with on premise pyccd calculations.  This supports the premise that pyccd can be run above ODC as a proof of concept and supporting smaller AOI specific science investigations
7. Developed code to decompose xarrays into component band single pixel rod time-series for all of the required pyccd input bands.

### ODC Accomplishments

### Open Data Cube Instances

1. Running on single Linux box discrete hardware.
2. Running on an open source libvirt/kvm virtual machine
3. Running on a vmware virtual machine
4. Running in the CHS restricted cloud environment
5. Running on the GA/USGS shared AWS project hosts
6. Running in the SGT cloud referencing the Development Seed COGs.

#### Steering Council Participation (On-going)

1. Attend monthly telecoms to discuss ODC strategy and developments

``` GA's ODC strategy, milestones and deliverables still largely outside of my circle of influence. ```

#### ODC Data Curation Accomplishments

1. Data Sets Delivered:
    1. **Oregon** - Landsat Level 1, Tier 1 Scene Based Oregon Data
    2. **Oregon** - Landsat USARD Oregon Gridded/Tiled Data
    3. **Rwanda**/Burundi - Landsat Level 2, [ESPA] Surface Reflectance, Rwanda, Africa ODC International Sandbox, supporting the United Nations Sustainable Development Goals.
    4. **Mexico** - Landsat Level 2, [ESPA] Surface Reflectance (Albers and UTM), Mexico City, Mexico supporting the CEOS 20 by 2020 Initiative.
    5. **California** - Landsat Level 2, [ESPA] Surface Reflectance, California, United States (JSON Metadata) supporting ODC and Development Seed prototype and collaboration activities.
    6. **South Dakota** - Single scene ESPA generated imagery for testing ODC over SD.
2. Data Ordering and Download
    1. completed **dataDog** software for automated delivery of Level 1, Landsat Data from Earth Explorer.
    2. Completed **espaDog** for automated sorting of Landsat Tier 1 data and subsequent automated ordering and downloading of associated on-the-fly ESPA processed data.
3. Data Extraction and Formatting
    1. Developed python code to untar USGS delivered data tarballs in parallel when warranted
    2. Wrote python code to **create COGs** from the delivered, untarred geotiffs

#### Completed Landsat MetaData Indexing for ODC (L1 and L2)
1. Decomposed the indexing algorithm the associated database records storing the metadata
2. Wrote code to parse metadata (stored in json, xml and MTL) formats
3. Wrote Jupyter notebooks to validate indexed data cubes and display the resultant python objects


#### Architecture Study and Documentation Completed
1. Developed several views of the ODC architecture
2. Examined the relationship between the architectural intent of ODC and the actual directory tree of the ODC python code
3. Detailed findings to be itemized on this web site (time permitting).

#### Documentation and Reporting

1. Reviewed and edited the ODC documentation set
2. Provide monthly status reports and technical demonstrations
3. Provided data support to ODC researchers

#### Examined ODC as a Service Prototypes

1. ODC Sandbox
2. Testing of ODC Dashboards
3. Standing up ODC in SGT Cloud


#### Visualization (Data[ARD] and Science)

1. LCMAP Model visualization Jupyter notebooks
2. Created USARD browse and thumbnails and indexed these in the cloud
3. Created Animations using animated GIFs of band combinations and indexes

[Notional Example Visualization](https://apps.sentinel-hub.com/eo-browser/?lat=-2.18965&lng=30.23326&zoom=14&time=2017-07-01&preset=3_FALSE_COLOR&datasource=Landsat%208%20USGS)

#### Evaluation Criteria Study

1. Formulated an ODC specific technology reading list and initiated the study plan for this material
2. What is a clean architecture?
3. What is clean code?
4. Software Development Styles and Languages
5. What does it mean to be cloud ready and what are the process and re-engineering steps associated with this migration?

#### Tooling and Infrastructure

Developed the requisite skills for using Open Data Cube and contributing to the open source shared project including:

1. Jupyter Notebooks
2. Typora markdown editing
3. Sphinx documentation platform
4. Read-the-docs style sheets
5. Python
6. Functional Programming
7. Postgres Databases
8. Design Specific Languages
9. AWS services
10. Infrastructure as code
11. Logging
12. Orchestration
13. Docker
14. Git

### Project Goals Traceability

This section remembers some of the objectives from last February as they were documented in goals and actions from the Confluence and other sources.

#### Confluence

**Objectives:**
1. World-class provider of Landsat Data including global data exploitation.
2. Access feasibility and utility of OpenDataCube (ODC) in LCMAP architecture.
    - LCMAP to leverage: All of ODC; part of ODC; no ODC,
    - ODC as an USGS hosted service for science and cloud based data exploitation

USGS Modernization OpsCon includes ODC

USGS continues to finalize the ODC OpsCon and as a starting point is considering the following scenarios:

    On premises ODC implementation into LCMAP (unlikely at this point in time)
    Full ODC implementation into LCMAP in the cloud
    Partial (component) ODC implementation into LCMAP in the cloud

USGS continues to use cloud and on-prem ODC setups and has developed a makefile for building ODC and associated notebook libraries for detailed analysis of ODC and LCMAP intersections. (10-31-2018)


    USGS/Kline's team to standup a cloud instance of ODC in the SGT realm for examining the California Data Lake collection. - Several detailed technical coordination efforts will arise from this collaboration.

USGS has written a series of exploratory notebooks as proofs for the following LCMAP sub-concepts.(10-31-2018)

    dc.load of USARD L5,L7,L8 (Oregon USA)
    built interface from xarray → ccd.detect()
    created simple visualizations of pixel_qa and ccd probabilities:
    recently (pickled/serialized) ccd.detct output models to local files and therefor S3 storage.

Each of these incremental proofs will add up to quantifiable, objective, benchmarked decisions on where to place data, output models and processing in the evolving hybrid cloud architecture for LCMAP. (10-31-2018) tb



#### GA USGS Collaboration Annual Report

- Under the Sustained Earth Observation (EO) Collaborative Program
    - Established in 2015
    - to exploit land remote sensing data to monitor the Earth and detect change as it happens.
    - funding will support GA’s ongoing contributions to the development of the Open Data Cube platform, as well international collaboration on analysis-ready data.  
    - USGS confirmed that Analysis Ready Data will be the standard product of the Landsat program beginning with Collection 2, and that production of these products is formally a part of the Landsat 9 development project.

    - Both parties continue to engage with the impact of cloud technology on their future architecture, noting that access to data and functionality in the cloud greatly expands the potential user base in a way that is not possible with internal or restricted systems.  

    - The importance of cloud computing to their future strategies was increasing. Both parties noted, however, that existing infrastructures (such as the National Computational Infrastructure in the case of GA and the Cassandra system in the case of USGS) would remain important assets for the next few years, and that roadmaps needed to take a long-term view.

> The desire to establish ‘predictive’ systems for environmental data was increasing, and that
this would require comprehensive cross-disciplinary collaboration, and assimilation of
heterogeneous data sets derived from remote and in-situ observations. GA noted Australian
Government funding for scoping of an ‘environmental prediction system’, and USGS noted
that projection was a key element of their LCMAP program that would require significant
attention over coming years. Both agencies noted rapidly increasing interest in systems for
monitoring and predicting water quality.

> The USGS formally joined the Open Data Cube initiative, contributing to the leadership of
the program and making technical contributions that will ensure that Landsat data was more
easily accessible to the 40+ countries using the open-source platform to exploit Earth
observation data.

> The USGS benefited from expert Australian input on the definition of its future Analysis-
Ready Data products. This dialogue increases the likelihood that products generated by
USGS will be directly usable in Australian systems, reducing the need for costly custom
processing by GA.

- Open Data Cube is the conversational framework where the above discussions and documented findings will be solidified and demonstrated in practical ways.

#### Data Cube & Access

- Development of information warehouse technologies to support time series data exploitation and innovation
  - Understanding of how best to leverage commercial cloud computing to achieve organisational objectives.

    - Increased access to open platforms that support local, national, regional, and global projects increases the use of Landsat data.
      - Support for multi-mission application development by the
      broader user community, by providing a tool that is designed from this perspective from the beginning.
      - Easier portability of algorithms, science code, products, and tools between GA, USGS, and the broader community.
    - Increased sharing of data by partners, such as CISRO, who's data can complement baseline data streams such as Landsat and Sentinel data.
    - The international community and private sector adopts concepts of ARD, producing data that is more easily usable alongside Landsat data.
        - Easier portability of algorithms, science code, products, and tools between GA, USGS, and the broader international community, including to/from partner systems via uptake of the Open Data Cube.


 - Identifying the functionality in the USGS LCMAP system that GA could interface or ‘port’ to
the Open Data Cube project. Availability of this functionality would benefit the user
communities of Digital Earth Australia and Landsat data, and ensure the Open Data Cube
moves towards supporting internal USGS needs.

- Ensuring that the Open Data Cube project provides a platform that is easier to install, easier
to customise, and easier to contribute both science algorithms and code to. A key priority
will be ensuring users can more easily ingest authoritative Landsat data for their areas of
interest.


## Practical Implications of this Study

The above steps were necessary to understand the entire ODC landscape, evaluate ODC's components and develop strategies and tactics that help accelerate EROS cloud developments. Additionally, these activities allow us to establish common context among the development groups in L2PGS, LSAA, ODC and Development Seed to blend the concepts when designing data exploitation schemes for the cloud.

The quality and versatility of the Collection 2 data as manifested in the cloud will improve as a result of this study and the practical experiments as illustrated/demonstrated by Jupyter notebooks.


