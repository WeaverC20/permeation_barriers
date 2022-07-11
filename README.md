# Modelling permeation barriers

The interface condition between materials used in FESTIM is the conservation of chemical potential:

$\left(\frac{c_{\mathrm{m}}}{K_{s}}\right)^- = \left(\frac{c_{\mathrm{m}}}{K_{s}}\right)^+$

Analytical solutions have been evaluated for a cartesian and cylindrical case:

<img src="https://user-images.githubusercontent.com/65899899/178293496-d67d7431-d1f8-4478-aa82-21988f8cf6a8.jpg" width="500"/>

<img src="https://user-images.githubusercontent.com/65899899/178293593-fee437f5-e3a7-4180-b464-a5877179f6ec.jpg" width="500"/>



To be able to run scripts:

##  Run FESTIM

Run a FEniCS container:

```
docker run -ti -v ${PWD}:/home/fenics/shared --name permeation_barriers quay.io/fenicsproject/stable:latest
```

Install FESTIM v0.10.0 inside container:

```
pip install git+https://github.com/RemDelaporteMathurin/FESTIM@v0.10.0
```

To run the FESTIM simulation:

```
python3 example.py
```

This will produce any detailed results files