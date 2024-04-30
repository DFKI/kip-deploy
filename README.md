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
