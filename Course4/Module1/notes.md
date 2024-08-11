# Module 1: Relational Database Concepts

## Fundamental Relational Database Concepts

### Review of Data Fundamentals

- Definition of Data
- Data Structures: 
    - Structured: Data with a pre-defined format, often in form of row and columns:
        - Spreadsheets
        - SQL databases
        - Online forms
         
    - Unstructured: Lacks a predefined format or organization:
        - text files
        - Media files: images, audi, video
        - web pages
        - Social media content: posts, tweets

        
    - Semi-structured: has some organized properties:
        - JSON files
        - XML documents
        - Emails
        - zip files

- Data sources
    - Traditional databases
    - Flat files
    - XML data sets
    - Web scraping
    - Data streams and feeds
    - IoT devices
    - Social media platforms

- File formats
    - Delimited text files:
        - Rows of variables separated by character
        - Examples: CSV, TSV files
    - Spreadsheets:
        - Data in rows and columns
    - Language files:
        - Set rules and structures for encoding data
        - Examples: JSON, XML

- Data repositories:
    - A central data archive to store, manage and organize data merged from various data sources
    - Include relational and non-relational databases
- Relational databases
    - Include structured data stored in tabels
    - The link between the tables minimizes data duplication
    - Examples: 
        - IBM DB2
        - Microsoft SQL server
        - Oracle
        - MySQL
        - PostgreSQL
    - Disigned for OnLine Transaction Processing (OLTP) Systems used to support database activities such as:
        - Custumer transactions
        - Human resources activities
        - Bank transactions
- Non-relational databases: Offer flexibility
    - Examples: 
        - MongoDB:
            - A document-oriented database
            - Stores semi-structured and unstructured data
        - Cassandra
        - Redis

- OLAP(OnLine Analytics Processing) enables complex analytics

### Information and Data Models

Information model and data model are the two key concepts that play a crucial role in data organization


#### Information Model
[What is an Information Model](https://www.archixl.nl/en/blog/what-is-an-information-model/#:~:text=For%20example%2C%20in%20an%20information,%2C%20Age%2C%20and%20Student%20Number.)
- A conceptual framework
- Represents in an abstract way entities with their
    - Properties/attributes
    - Relationship
    - Functions
- Key aspects:
    - Help to understand the different types of informations an organization uses
    - simplifies the complexity of real-world entities and relationships
    - It includes important ideas that can be used in different parts of the organization.
    - Help understand and define business concepts and rules

#### Data Model
- A plan for translating conceptual information model into a practical database structures
- Defines organization, storage and retrieval mechanisms for database systems
- Keys aspects:
    - They specify:
        - Data elements
        - Structures
        - constraints
        - Relationships
    - Often tailored to a particular DBMS, they define the schema including:
        - tables
        - columns
        - data types
        - indexes
        - relationship between data entities, like foreign keys
    - Ofen involve normalization processes to:
        - ensure data integrity
        - reduce redundancy

#### Differences between Information and Data Models

- Level of Detail
- Purpose
- Usage
- System development

![alt text](image.png)

##### Hierechical Model
- Serves as a physical implementation of information systems
- Organizes data in tree like format where:
    - nodes are entities
    - connections represent relationship
- Usage:
    - Organizational structures
    - File systems
    - XML documents
- Structural limitations: Redundancy

##### Types of Data Model
- Relational Model
    - The msot widely used data model for databases
    - allows for data independance
    - Stores data in tables
    - Provides logical, physical and storage independance
    - offeres simplicity, flexibility and ease of use

- Entity Relational Model (ERD):
    - Offers an alternative to relational model
    - Presents databases as a collection of entities and objects existing independently in the database
    - Uses Entity Relationship diagram (ER diagram) to represent entities and their relationships

- It is easy to convert ER diagram into tables. Building blocks are entities and attributes
    - Entities are represented by rectangles
    - Attributes are represented by ovales
    - Example with libraries:
        - Books as entity 
        - Authors as entitie with firstname, lastname end email as attributes
        - Entities become table in the database with attributes as colums

Concepts in Database Management
- Ensure adaptibility and efficiency. Key features:
    - Logical data independance: The modification of the database structrues(adding new cols, changing cols types) should not impact the existing applications/queries
    - Physical data independance: Allows tweaking the internal database organization, like changing the data storage type or indexing startegy
    - Physicall storage independance: Allows organizing the data on physical storage devices

### ERDs and Types of Relationships
- Entity Relationship Diagram(ERD):
    - Avisual representation
    - Illustrates relationships and interactions between entities
    - Shows the logical structure of the database system
    - Entities: boxes and Relationships: lines connecting the boxes

- Fundamental components: ![alt text](image-1.png)
    - Entities:
        - Represent people, objects or concepts
        - Serve as a fundamental building block
        - Represented by rectangles with attributes in ovales
        - Contain attributes describing specific properties
        - Form the basis for relationships
    - Relationships sets:
        - Illustrate how entities are connected
        - Represented by diamonds
    - Crow's foot notations:
        - A visual representation to indicate relationship between entities
        - Uses symbols to mention the nature and quantity of the relationship
            - Describe wethere the relation is one to one, many to many or many to many
        - Use symboles such as
            - greater than
            - less than
            - vertical line

ERD for Book entity
![alt text](image-2.png)

ERD for Author entity
![alt text](image-3.png)

Relationships between entities

![alt text](image-4.png)

1 to 1

![alt text](image-5.png)

1 to many(and many to one)

![alt text](image-6.png)


many to many

![alt text](image-7.png)

### Mapping Entities and Tables

ERD: a graphical representation of entities and relationships
- Relational Database:
    - framework that helps to manage and manipulate structured data
    - Data organized in tables
    - Relationsships between tables depend on the common fields
- Mapping an ERD into a table:
    - Entities become tables
    - Attributes become table
    - Best practices:
        - Primary key designation: Uniquely identify an entry in the table:
            - Ex: Book id in the book table
        - Data Validation: Ensure accuracy and consistency of data:
            - Process: check for data types, ranges and formats
            - Ex: Published year only accepts numerical values within a specified range
        - Default values:
            - Ex: Set "Unkown" as the default value for the author column in the book table
        - Use of views:
            - Present a customized and simplified perspective of data, expecially for complex queries or reporting purposes
            - Ex: create a view that combines information from the book and author tables to present a comprehensive list of books and their authors
        - Concurency control: 
            - Manage multiple users access and modifications to the database concurrently
            - THis prevents data inconsistency and conflicts
            - Ex: Include a "lastModified" timestamp in the book table
### Data Types

The data types assigned to a column controls the data the column can store
Varchar: store character strings of varying length
- varchar(100): 
    - allocates storage for up to 100 characters
    - Efficiency: It only uses the spaces needed, not the full 100 characters space
    - Flexibility: Strings varying in lenght
#### Date and Time
Date  for storing dates
Time for storing time of the day
DATETIME TIMESTAMP
#### Float and Decimal
They are numerical data types
- Float:
    - A floating-point number
    - Used when exact precision is not necessary
Decimal:
    - Used for exat arithmetic calculations
    - More suitable for fiancial calulations

#### Integer types
bigint int small int
- Store whole numbers
- Each type has a different range

### Binary data types
Store binary data like images and files
Binary Large Object (BLOB)
Store data as a sequence of bytes

#### Character/char
Used for fixed-lenght strings
uses a specific number of characters

- alway the data choose the data type that best suits your data and the requirements of your database system
Advantages of using the appropriate data types

data integration 
data sorting
range selection
data collection

### Relational Model Concepts

- Relationnal model
    - Introduced in 1970
    - Helps in organizing and understanding data
    - Involves two fundamental concepts:
        - Sets:
            - An unordered collection of distinct elements
            - Involve the use of curly braces {}
            - Plays a crucial role in mathmatics especially in:
                - Algebra
                - Geometry
                - Progability
            - Set operations:
                - Membership
                - Subset
                - Union
                - Intersection
                - Difference
                - Empty set
                - Power set P(A): the set of all possible subsets of A, including the empty set and A itself
                - Universal set U: The set that contains all objects
                - Disjoint set
                - Ven diagram: Visual representation of logical relation between sets

        - Relations:
            - A mathmatical concept based on sets
            - Describe the connection between elements of sets
            - Crucial in set theory and logic
            - Include:
                - Binary relations:
                    - Establish a connection between two elements
                    - Ex: 3<9
                - Ordered pairs:
                    - A subset of a cartesian prodct
                    - Denotes a binary relation on subsets A and B denoted as (A,B)
            - Properties of relations:
                - Reflexivity:
                    - Each element of is in relation with itself
                    - Example: the equality relation
                - Symetry: 
                    - a relates to b implies b relates to a
                    - Examples:
                        - The equality relation
                        - "The is sibling of" relation
                - Transitivity:
                    - a relates to b and b relates to c implies a relates to c
                    - Examples:
                        - The equality relation
                        - The "less then" (<) relation
                - Anisymetry:
                    - a relates to be and b relates to a implies a=b
                    - Examples:
                        - =
                        - <=
            - Components of relations:
                - Relational Schema: Specifies the structure: ![alt text](image-8.png)
                    - The name of the relation
                    - Name and type of each column
                - Relational Instance: Represents the actual data
                    - The real worl data stored in a table
                    - Consists of rows and columns:
                        - columns correspond to attributes
                        - Rows represent tuples
            - Key concepts:
                - Degree: the number of columns/attributes
                - Cardinality: The number of rows/tuples

                    
## Introducing Relational Database Products

### Database Architecture
- Deployment topology: 
    - configurations of 
        - Hardware
        - Software
        - Network components
    - It's choice depends on:
        - Scalability
        - Performance
        - Reliability
        - Nature of the application
    - Common deployment topologies:
        - Single tier architecture:
            - Deploys all components of the application, including user interfaces, application logic, data storage, on a single server
            - The entire application operates within a single environment
        - Client server architecture or two-tier architecture:
            - Divide the application into two layers:
                - Client layer: responsible for user interface:
                    - Application:
                        - where the user interacts with the system
                        - can be written in various programming languages like C, Java, Python, or Ruby.
                    - Database Client:
                        - Establish connection with the database server
                        - Communication: Send queries to the database server and get result set back
                        - Manage connections:
                            - Multiple connections
                            - Connection closing when no longer needed
                    - DB API/Framework: offers a set of functions, protocols, and conventions that simplify database operations like connecting, querying, and updating data
                - Server layer: manages the application logic and data storage; The server of the DBMS consists of three layers:
                    - Database Acess Layer/Data Acess Interfaces: Allows the client systems to acess the database server through interfaces:
                        - API(Application Programming Interface): a set of defined functions for accessing the database
                        - CLP (Command Line Processor): A command line interface for acesing the database
                        - Proprietary Interfaces: 
                            - Vendor-specific interfaces provided by database vendors for optimized performance.
                            - Tailored to a specific DBMS
                    - Database Engine Layer:
                        - Compile queries
                        - Retrieve data
                        - Process data
                        - Deliver the result set bac to the client
                    - Database Storage Layer: Where the data is stored
                        
            - A remote server hosts the database
            - Users acess it from client systems, commonly through a web page or a local application
        - Three-tier architecture:
            - Layers
                - Client Layer
                - Database Server
                - Application server
            - Most production environments restricts access to database server except admins. The reasons:
                - Security: Database server contains sensitive informations
                - Performance optimization: Avoid overloading the server with unnecessary traffic
                - Maintainability
            - ![alt text](image-9.png)
        - Cloud-based deployment
            - It' use is becoming increasing and popular
            - Eliminates the need to download database software locally
            - Easybily acessible to users from any where at any time with internet
            - Client applications/Users interact with the database server through the application server situated within the cloud environment
            - Suitable for:
                - Development
                - Testing
                - Production

### Distributed Architecture and Clustered Databases

- Helpful for large-scale workloads
- Support high availability or scalability
- Involves clusters of machines interconnected through a network
- Benefits: Enhance
    - Scalability
    - Fault tolerance
    - Performance
- Types:
    - Shared disk architecture:
        - Multiple database servers processing workloads in parallel/concurently/simultaneously
        - Each server establishes a connection to shared storage and communications with other servers
        - Advantages:
            - effective distribution of workload
            - scalability as demand grows
            - high availability and minimizing service disruptions: rerroute clients to other servers in case of failure
    - Shared nothing architecture: Uses either replication or partitionning techniques:
        - Distribuate clients workloads across multiple nodes
        - Promotes parallel processing and an efficient resources utilization
        - Enhance fault tolerance by rerouting clients
         
    - Combination and specialized architectures: 
        - Use a combination of:
            - Shared disk
            - Shared nothing
            - Replication or partitionning techniques
        - Integrate specialized hardware components
- Common techniques:
    - Database replication: 
        - copy changes from one detabase server to one or more replicas
        - Distribute client worload across multiple servers
        - Called High availability (HA) replica when the replica reside in the same location
        - In case of failure due to hardware or software issue, the system redirects client to HA replica
        - To mitigate broader disasters, organizations establish replicas in geographically distributed locations. This guarantees that during instances of complete data center outages, be it due to power loss, fire, earthquake or flood, clients can be rerouted to disaster recovery replicas
    - Database partionning and sharding: involves placing partitions on separate nodes, facilitating increased parallel processing and improved overall performance


### Database Usage Patterns

- Data engineers and database administrators
    - Tasks:
        - Creation and management of database objects
        - Access control
        - Monitoring and performance tuning
    - Primary focus: Create a solid fundation for Storing and managing data efficiently
    - Mechanisms employed:
        - GUIs oe web-based management tools
        - Command line interfaces and utilities
        - APIs
- Data scientists and buiness anlysts:
    - Tasks: 
        - Data analysis, insight derivation and data-driven predictions
        - Reading from existing data sources
        - Create and pupluate existing database objects occasionally
    - Tools: 
        - Data Science tools
            - Jupyter
            - R Studio
            - Zepplin
            - SAS
            - SPSS
        - BI tools
            - Excel
            - Pwer BI
            - Miscrosof Tableau
            - MicroStrategy
- Application developers
    - Do not access databases directly
    - Create applications that can require both read and write access to the databases
    - Use programming languages: C++, C#, Java, JavaScript, .NET, PHP, Perl, Python, Ruby
    - Programming languages communicate with database through interfaces and APIs
    - Use Object Relational Mapping (ORM) frameworks:
        - Tools and software that facilitate interactions between a relation database and an OOP languange
        - Examples:
            - Django in Python
            - ActiveRecord in Ruby
            - Entity Framework in .NET
            - Hibernate in Java
            - Sequelize in JavaScript
### Introduction to Relational Database Offering

The first relational database product, IBM Sabre, a Transaction Processing System (TPS) was created in 1960 by IBM, for American Airline
![alt text](image-10.png)

Cloud:
Amazone RDS
IBM DB2 on Cloud
Microsoft SQL Azure
Oracle Cloud

open source relational databases examples


![alt text](image-11.png)


Popularity of databases

![alt text](image-12.png)

2021 the 10 most popular databases

![alt text](image-22.png)


popularity of license type

![alt text](image-23.png)

cloud database: examples


![alt text](image-13.png)

### DB2
DB2=Database2
- Created by IBM in 1983
- originally designed for mainframes:
    - Mainframes are very powerful computers mainly used by big companies for critical tasks suchas:
        - Census
        - Industry and consumer statistics
        - Entreprise resource planning
        - Transactions processing
- later for:
    - OS/2 an OS created in collaboration by IBM and Microsoft
    - UNIX
    - Linux
    - Windows
- after sometime the prodduct was rewritten for portability accross multiple operating systems (so that you can easily port applications accessing Db2 data from one operating system to another)
- Today, DB2 consists of many database products:
    - DB 2 database: Possibilities of use
        - Community license can be used for free with a 1 GB data limit
        - Dowload a free docker image of DB2 databse
    - DB2 on Cloud:
        - The frree lite plan available for development and evaluation purposes
    - Db2 Datawarehouse: Only commnity edition available in no-cost trial editions 
    - DB2 Datawarehouse on Cloud: a free version available with up to 1GB of data
    - DB2 Big SQL
    - DB2 for z/OS

DB2 features
migrations possible from on-promises prod to the corresponding cloud product
![alt text](image-15.png)

DB2 products

![alt text](image-16.png)

![alt text](image-17.png)

MPP: Massively Parallel Processing
![alt text](image-18.png)

![alt text](image-19.png)

![alt text](image-20.png)

Thrre node High Availability clustering  for standard and entrprise edition of DB2 on Cloud
![alt text](image-21.png)

DB2 on cloud can be deployed on
- IBM Cloud
- AWS

Once running you can work with DB2 on Cloud using
- CLPPlus Ccommand line interface
- GUI console
- standard APIs such as ODBC, JDBC and rest

Using the GUI console, You can load data to DB2 Cloud from
- CSV or Excel files
- Amazone S3

You can programmatically load data from IBM cloud object storage

Db2 provides high availability, disaster recovery, or HADR functionality to support high availability systems. HADR replicates changes made at a primary database to multiple standby servers. If the primary database fails for any reason, hardware, software, or network issues, you can automatically promote one of the standby databases to be the primary database. Redirect client applications to this new primary database, and continue to replicate to the other standby servers in the group. When the original primary database comes back online, it can either take the place of a standby server or be promoted back to the primary position.


DB2 warehouse offers scalability with partitionning
- Scale up the storage capability to meet peak demand
- Scale down it to reduce cost when demand is low

Datawarehouse store data in nodes
![alt text](image-14.png)

- To scale up storage capacity, add a node to your deployment; the partitions and their workloads automatically rebalanced accross the new node setup

![alt text](image-24.png)


- To scale dow, remove a node

### MySQL
Introduction
- A RDBMS
- reliable, scalable and easy to use
- include diverse flavors and editions
- offers a clustered version
- widely used as an adabtable database solution

History
- MySQL initially developed by a Swedish comapnay(a company in Sweden), MySQL AB
- Named MySQL after My, a daughter of Monte Widenius, a co-founder of MySQL AB
- Sun Microsystems acquired MySQL AB
- Oracle Corporation acquired Sun Microsystems
- MySQL logo shows a dolphin, named Sakila, selected from suggestions in a name the dolphin contest
- gained popularity in the late 1990s and early 2000s because it played a crucial role in:
    - Linux OS, 
    - Apache Web Server
    - MySQL database
    - PHP scripting language
    - LAMP stack
- Has dual licensing:
    - GNU GPL (General Public License) for open source usage:
        - led to the emergence of various forks including MariaDB
    - commercil license for embedded applications

Compatibility
- Compatibility with: UNIX, Linux, Windows
- Suport many modern programming languages
- Uses SQL
- Introduces extensions for added functionalities:
    - Ex: Use of the LOAD DATA statement  which swiftly imports rows from a text file into a database table

Data types and storage engine
Works primary with relational data but also supports JSON

Support multiple storage engines

Sorage engines:
 - Handle the SQL operations on a table
 - Defines what features that table can use

So choose the engine based on the expected workflow and the table requirements

InnoDB: the default MySQL storage engine
![alt text](image-25.png)


MyISAM: suitebale for workloads with mainly read operations and few updates such as datawarehouses or web aps

NBD engine
![alt text](image-27.png)

Availability and scalability

MySQL supports high availability and scalability. You can use replication to create a copy of your data on one or more replicas. Changes in the source database are then simultaneously executed at the replicas. Multiple copies of the same data mean that you can share certain read loads for your data across the replica set improving scalability. Additionally, replication boosts availability. If the source database experiences a failure, you can perform a failover to use one of the replicas instead.

CLustering
Clustering is the practice of connecting multiple independent computing resources to work together as a unified system

MySQL provides 2 clustering options
- InnoDB storage engine with group replication

uses the InnoDB storage engine with group replication and enables you to work with one read-write primary server and multiple secondary servers. You can then use MySQL router to load balance client applications across the multiple server instances. In the event of unplanned downtime of any of the servers, MySQL router will reconnect client applications to an available server

- MySQL cluster Ediction with NDB storage engine

 provide a highly available and scalable solution. Multiple MySQL server nodes access a set of data nodes usually stored in memory. Running multiple data nodes provides redundancy and hence increased availability in the event of failure, and running multiple server nodes provides scalability

![alt text](image-26.png)

### PostgreSQL

History

- originates from the PROSGRES project at the university of California, used :
    - for Reasearch and production applications
    - Accross finance, avaiation and medicine
- In 1994, open source posgres95 was released:
    - Included SQL
- Renamed to PostreSQL:
    - generally today prounouced simply postgres
    - Can be used for LAPP stack: Linux, Apache, Apache, PostgreSQL, PHP for web apps and websites 
    - You can use extensions such as PostGix for geographic and spatial data handling

What is POstgreSQL

Supports Inheritance and Overloading:
Inheritance: In PostgreSQL, tables can inherit properties from parent tables. This allows for the creation of a hierarchical structure of tables, where a child table can inherit columns and constraints from a parent table. This feature is similar to the concept of inheritance in object-oriented programming, where a class can inherit attributes and methods from another class.
Overloading: PostgreSQL supports function and operator overloading, meaning you can create multiple functions or operators with the same name but different parameter types. This allows for more flexible and expressive database operations.


- free and open source RDMS
- compatible with Linux, Windows, Solaris
- Supports many programming languages, such as Python, Java, C++/C
- supports standard relational databse constructs:
    - keys
    - transactions
    - views
    - functions
    - stored procedures
- supports some NoSQL functionalities:
    - JSON for structured data
    - HSTORE for non-hirerarchical data


Hign vailability
- Support  replication:
    - 2 nodes synchronous replication 
    This stores a copy of your data on a second server and applies each change you make to Node 1 at Node 2. You can then share read loads across the two servers. And if Node 1 fails, you can enable Node 2 to service all clients until Node 1 is running again. It also supports multi-node asynchronous replication for high availability and scalability. Here, one master node distributes its changes to multiple read-only replicas for scalability purposes. And again, if the read-write node fails, you can quickly replace it with one of the read-only replicas.
For even greater flexibility for scaling applications, you can use commercial additions such as EDB PostgreSQL replication server, which provide multi-master read/write replication. This enables you to run multiple read/write databases that all replicate changes with each other. If one fails, users can easily be redirected to another instance until it is available again. Other technologies that have been added to PostgreSQL in recent releases to enhance scalability and working with larger data sets include partitioning, which enables you to split a large table into multiple smaller sections or partitions to improve query performance. And sharding, which enables you to store horizontal partitions across multiple remote servers. In this video


[Reading: Deep Dive into Advanced Relational Model Concepts](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL3JlcXVTZ1JFTHlxZGVTNFlXcnp1VUEvRGVlcCUyMERpdmUlMjBpbnRvJTIwQWR2YW5jZWQlMjBSZWxhdGlvbmFsJTIwTW9kZWwlMjBDb25jZXB0c3MtdjEubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzIzMDE1Mzc0fQ.JxfgLW2-eQ0fAlZIM_0mfQblYSF-KRb7YKK3LTmPJio)


[Hands-on Lab: Advanced Relational Model Concepts](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1EQjAxMTBFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvQWR2YW5jZWRfUmVsYXRpb25hbF9Nb2RlbF9Db25jZXB0cy9JbnN0cnVjdGlvbmFsLWxhYnMubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzIxMTkxMTYyfQ.I5cCkRvMPt9qIa97tsHWjcZyzXPGU6hB3bxO8BfYU0U)



https://www.analyticsvidhya.com/blog/2023/09/top-web-scraping-projects-to-do/