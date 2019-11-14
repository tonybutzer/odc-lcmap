
.. ODC-LCMAP documentation master file, created by
   sphinx-quickstart on Mon Dec 10 11:51:55 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ODC-LCMAP Special Study Documentation
=====================================

This documentation represents a living document for the USGS ODC Collaboration initiative formalized as the Task Plan 114 -- subtask titled 

* "Open Data Cube and LCMAP technologies special study including derived science products from ARD (see LSIS PWBS) (FY2019 Q1)"

Objectives
++++++++++

1. Establish a USGS supported consistent engineering effort in the Open Data Cube project to collaborate with global engineers and customers promoting the use of remotely sensed data (notably Landsat Level 1 and Level 2 products and time series) for the benefit of mankind as outlined by the United Nation's Sustainable Development Goals (SDGs)

"Applying free and open satellite data to environmental, economic and social challenges has the potential to deliver information and applications that have great impact at local, regional and global scales. Advances in cloud computing, and the availability of free and open technologies such as the Open Data Cube, mean that developing countries without the local infrastructure to process large volumes of satellite data can access data and computing power to build relevant applications and inform decision making." -- From Digital Earth Australia Website

Suggested Activities:
+++++++++++++++++++++

1. Integrate development teams between Geoscence Australia and the USGS EROS LPIP Teams
2. Provide data and supporting engineering for use by the Open Data Cube Community
3. Pilot test Open Data Cube in several infrastructure ecosystems
4. Validate cloud approaches for "data lake" storage
5. Develop "self-directed" work plans and strategies to maximize the impact of the Open Data Cube **research** activities using an **immersive approach**
6. Foster relationships and develop team charters that cross projects from LSAA and LPIP
7. Develop, promote and explain lean methods for configuring, provisioning and deploying cloud infrastructure via Infrastructure as Code methodologies
8. Develop objective and subjective methods for evaluating software and hardware systems and present findings to peers and customers.
9. Participate on the ODC **Steering Council** and foster effective processes and practices.
10. Test LCMAP algorithms (pyccd first) running on top of the Open Data Cube framework/libraries
11. Demonstrate and expose time-series and pixel level visualizations to the LSAA and Data Science elements at EROS
12. Develop an ODC Engineering Handbook
13. Develop automated data delivery tools for ordering, delivering, unpacking and cloud optimizing Landsat Level1 and Level 2 data from USGS EROS Data Ordering Systems
14. Participate in GA, USGS Collaboration Teleconferences and update high level work plans in **Confluence**
15. Organize the work plan, technology plan and study findings in a set of web based documentation using ODC documentation methods. **This website**

Expected Outcomes:
++++++++++++++++++

1. Data standards for Level 2 SR Data in the cloud - that enable ODC-like applications

* Documented COG Recipe
* Product meta-data standards (json,XML,MTL) useful for cloud exploitation of long time-series datasets

2. Open source tools in Github repositories of **prototype** code, mostly python

* dataDog -- code for delivering, unpacking and cogifying Level 1 scene based imagery
* ODC-LCMAP -- this code indexes several types of data including

   * Level 1 UTM Scenes
   * ESPA generated Level 2 UTM Scenes
   * USARD Tiles and range get ready geotiffs

* anotebooks -- these jupyter notebooks visualize products 
* pyccd -- this includes wrappers that convert xarrays to a set of series via the Z-axis (time dimension)
* espaDog -- automates ESPA ordering pipeline as an interim capability until Level2 data is pervasive in the AWS cloud

3. Evaluation criteria documented in weighted decision matrices
4. Deploy or help deploy "Official" Data Cubes as part of the 20 by 20 initiative

* SGT California Cloud ODC Instance
* Oregon USARD AWS Cloud ODC Instance
* ODC Development Sandbox Initiative
    * Africa and Africa Islands datasets for the testbed
* Data Only for all of Mexico - on-premise ODC Instance (INEGI)

5. Sample data lakes with emerging Level 2 datasets covering international locations
6. ODC Engineering Handbook
7. Technology recommendations gleaned/culled from the immense universe of AWS services and coding patterns

Immersive Approach
++++++++++++++++++

In order to be an effective peer and contributing member of the communities examined/collaborated with, a full immersive approach was taken and this has proven effective in delivering the 2018 milestones in a timely fashion with a fairly lean staff and minimal external assistance.

What I mean by an immersive approach is to use the exact same platforms utilized/deployed by ODC and LCMAP including documentation using Sphinx, markdown and restructured text along with the potential to publish any content in open forums on the read-the-docs sites.

Further several technical topics such as: coding paradigms (Structured, OOP, Functional), cloud infrastructure, orchestration and scaling practices, architectural software patterns, were examined in detail by exploring github repositories and writing prototype code to understand code complexity as a factor in determining successful reuse. Seemingly innocent topics such as Python with its deceptively small language grammar have proven to be quite complex when actually deploying them with the massive library packages linked for data science exploitation.

Remote Sensed data and its associated "product data" can in itself be complicated, especially at scale.

While I think my approaches have been agile, unique and efficient, I have tried to add accountability to customers that require information packaged in more tradition ways.

Reference
+++++++++


Clean Code
""""""""""
https://cvuorinen.net/2014/04/what-is-clean-code-and-why-should-you-care/

.. note:: Clean code is code that is easy to understand and easy to change.


Other
*****
`ODC Links <notes/odclinks.html>`_


Books
^^^^^


* Living Clojure: An Introduction and Training Plan for Developers Carin Meier
* Understanding Software: Max Kanat-Alexander on simplicity, coding, and how to suck less as a programmer Max Kanat-Alexander
* Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering) Paul Clements
* Clean Architecture: A Craftsman's Guide to Software Structure and Design (Robert C. Martin Series) Robert C. Martin
* The Hitchhiker's Guide to Python: Best Practices for Development Kenneth Reitz
* AWS Billing and Cost Management: User Guide Amazon Web Services
* Amazon Elastic Container Service: Developer Guide Amazon Web Services
* The Complete Works of Henry David Thoreau: Canoeing in the Wilderness, Walden, Walking, Civil Disobedience and More Henry David Thoreau
* Amazon Simple Storage Service (S3) Getting Started Guide Amazon Web Services
* Security Solutions for AWS: Understanding Network Security and Performance Monitoring for Amazon Web Services (Argent Software Simply Safe Book 1) Argent University
* The Terraform Book James Turnbull
* CISSP For Dummies Lawrence C. Miller
* Modern Tkinter for Busy Python Developers: Quickly learn to create great looking user interfaces for Windows, Mac and Linux using Python's standard GUI toolkit Mark Roseman
* Making Games with Python & Pygame Al Sweigart
* Python: Learn Web Scraping with Python In A DAY! - The Ultimate Crash Course to Learning the Basics of Web Scraping with Python In No Time (Web Scraping ... Python Books, Python for Beginners) Acodemy
* CSS (with HTML5): Learn CSS in One Day and Learn It Well. CSS for Beginners with Hands-on Project. Includes HTML5. (Learn Coding Fast with Hands-On Project Book 2) LCF Publishing
* Python: Learn Python in One Day and Learn It Well. Python for Beginners with Hands-on Project. (Learn Coding Fast with Hands-On Project Book 1) LCF Publishing
* Python: Complete Crash Course for Becoming an Expert in Python Programming (2nd Edition) Nick Goddard
* Python Cookbook: Recipes for Mastering Python 3 David Beazley
* Red Hat RHCSA/RHCE 7 Cert Guide: Red Hat Enterprise Linux 7 (EX200 and EX300) (Certification Guide) van Vugt
* Summary - Good to Great: By Jim Collins - 
* The Logstash Book James Turnbull
* Head First JavaScript Programming: A Brain-Friendly Guide Eric Freeman
* A New Earth - Philosophers Notes Summary Brian Johnson
* Effortless Reading: The Simple Way to Read and Guarantee Remarkable Results Vu Tran
* Thinking Fast and Slow by Daniel Kahneman: An Action Steps Summary and Analysis
* Real Happiness at Work: Meditations for Accomplishment, Achievement, and Peace, Regular Version Sharon Salzberg
* Ansible: Up and Running: Automating Configuration Management and Deployment the Easy Way Lorin Hochstein
* The Docker Book: Containerization is the new virtualization James Turnbull
* Understanding Zen Benjamin Radcliff
* OpenStack Operations Guide: Set Up and Manage Your OpenStack Cloud Tom Fifield
