# KIPerWeb deployment <img align="right" height="100" top=-100 src="figures/kip.jpg">
[![](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)

kip-deploy is a docker image for deployment of the recommenders developed within 
the python package kiprec. 

## Installation
To install use following commands:
```bash
docker build -t kip .
```

## Usage
To run build docker image use:
```bash
docker run -d -name kip -p 8080:80 kip
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to 
discuss what you would like to change.

## License
[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## About the project

The KIPerWeb deployment project has been developed as a part of a project [KIPerWeb](https://www.f-bb.de/unsere-arbeit/projekte/ki-gestuetzte-personalisierung-in-der-berufsbezogenen-weiterbildung-kiperweb). The project
promotes the use of AI in the vocational education. It included not just the development
of the research prototypes but also their implementation into the day-to-day educational
practice of the industry partners in the project. As a result all industry unlocked
the potential of data use for supporting their students.

## Consortia

![](/figures/bfz.jpg)
![](/figures/bnw.jpg)
![](/figures/dfki.jpg)
![](/figures/f-bb.jpg)
![](/figures/ifbb.jpg)
![](/figures/oncampus.jpg)
![](/figures/provadis.jpg)

## Supported by

![](/figures/bibb.png)
![](/figures/bmbf.png)
