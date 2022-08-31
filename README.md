# Mercator series
Mercator series and connected infinite product converging to 2

Computes: e^(1-1/2)\*e(1/3-1/4)\*e^(1/5-1/6).... = e^((Sum[(-1)^(k+1)/k,{k,1,Inf}]) = e^(ln(2)) = 2

See this video for more context:

[Interesting infinite product converging to 2](https://www.youtube.com/watch?v=lj65p3U3So8)
[Mercator Series](https://en.wikipedia.org/wiki/Mercator_series)

## Usage:
```
$./mercator_series.py
Iteration       Sum                     Exp(Sum)                Product                 Product-Exp(Sum)
10              0.6687714031754278      1.9518378251774227      1.9518378251774222      -4.440892098500626e-16
100             0.690653430481824       1.9950187134670618      1.9950187134670612      -6.661338147750939e-16
1000            0.6928972430599384      1.9995001874635359      1.9995001874635285      -7.327471962526033e-15
10000           0.6931221811849471      1.999950001874967       1.9999500018749374      -2.9531932455029164e-14
```

