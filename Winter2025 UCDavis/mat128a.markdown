# mat128a #


- [mat128a](#mat128a)
  - [summary](#summary)
  - [1st lecture](#1st-lecture)
    - [IEEE-754 Standard](#ieee-754-standard)
  - [2nd lecture](#2nd-lecture)
    - [more on question about how computer represent numerical stuff](#more-on-question-about-how-computer-represent-numerical-stuff)
    - [abosolute and relative error](#abosolute-and-relative-error)
    - [how computer did the mathmatical operation for floating calculation](#how-computer-did-the-mathmatical-operation-for-floating-calculation)
  - [3rd lecture](#3rd-lecture)
    - [Taylor expansion](#taylor-expansion)
    - [Lagrange interpolation](#lagrange-interpolation)
  - [4th lecture](#4th-lecture)
    - [lagrange basis function](#lagrange-basis-function)
    - [Why lagrange is better than Taylor approximation](#why-lagrange-is-better-than-taylor-approximation)
    - [python code for lagrange basis](#python-code-for-lagrange-basis)
  - [5th lecture](#5th-lecture)
    - [lagrange error approximation](#lagrange-error-approximation)
    - [technique for doing lagrange interpolation](#technique-for-doing-lagrange-interpolation)

----------------------------------------------------------------------------------------

## summary ##

| lecture      | content
|:------------:|:-------
| lecture1     | IEEE-754 with double precision
| lecture2     | absolute error and relative error
| lecture3     | taylor expansion, [lagrange interpolation](https://www.youtube.com/watch?v=nvkX1Bd90Gk)
| lecture4     | lagrange basis function
| lecture5     | approximation theorem, taylor,lagrange error approximation
| lecture6     | Neville's method(optimized lagrange interpolation), hermite interpolation

----------------------------------------------------------------------------------------

## 1st lecture ##

there is no way to store `pi` and `e` in the computer scale
since these are infinite digit numer, it's okay for 1/7 representation in computer scale
we need to find a way for make good approximation

- binary form for computer
  - hardware limitation 
  - easy for computer to do binary work
  - we also learned how to convert binary and decimal form

- decimal
  - 10^0 for first digit
  - 10^1 for second digit

- binary
  - 2^0 for first digit
  - 2^1 for first digit
  - 2^2 for second digit

### IEEE-754 Standard ###

example how computer decide a huge long binary number

with a 64 digit number as example

first digit
 - signs(s)
   - if this is 0, this is positive(+1)
   - if this is 1, this is negative(-1)

later 2 - 12 digit 
- exponent(c)
  - real number part of digit
  - 2^(c-1023)
  - since usually, longest digit on the this 11 digit long
  - is 2^10, that's why we minus 1023 there

later 13 - 64 digit
- mantissa(f)
  - this is the digit part of number representation
  - this is sort of polynominal that each digit represent the (1/2)^b
  - each time the digit location means b += 1
  - each 1 represent 1*(1/2)^b
  - final representation would be (1+ the polynominal)
  - this polynominal would defintely have value between 0<= f <= 1

the final output
```sign(either +1 or -1) * (real number part of this number) * (polynomial for digital number out there)```

this is also called `double precision`
- `double precision`
  - 64 digits
- `single precision`
  - 1 for sign, 8 for exponent, 23 for fractional

----------------------------------------------------------------------------------------

## 2nd lecture ##

a key thing to remember here after the HW1 is , whenever we are doing the chopping or rounding, we shall check out our siginificant digit problem, that sometimes we might misunderstand the siginificant digit, it counts as whenever we reach the first non-zero value instead of all those zeros in our consideration

### more on question about how computer represent numerical stuff ###

- overflow
  - any number that larger than the limit of double precision would result in 0: lose all the information

- *chopping*
  - this means a number like 3.14159 chooping to 5 digit
  - this gonna be 3.1415
  
- *rounding*
  - this means a number like 3.14159 rounding to 5 digit
  - this gonna be 3.1416

### abosolute and relative error ###

- absolute error
  - `| p - p* | ` 
  - ` p* = fl(p) `
  - f --> k digit chopping
  - l --> k digit rounding
  - this means how much the estimated value is deviated from the original value
  - ` | p - fl(p) | `

- relative error
  - `absolute error / |p|`
  - ` | p - p* |    / |p| `
  - ` | p - fl(p) | / |p| `

### how computer did the mathmatical operation for floating calculation ###

- case1: x + y
  - imagine x and y have so much digit that memory cannot store all of them
  - `fl( fl(x) + fl(y) )` : each time of operation, it would lost some information of them
  - so basically, the computer made not preciece calcualtion there rather it did the formulative estimation

- example1: x = 5/7 ; y = 1/3 ; fl = five digit chopping ; x + y

```
x = 5/7 = 0.714285714285
fl(x) = 0.71428

y = 1/3 = 0.333333333333
fl(y) = 0.33333

fl(x) + fl(y) = 1.04761
fl( fl(x) + fl(y) ) = 0.10476 x 10^1
most of the time, the ultimate representation would be 0.xxx * 10^n
```

- absolute error calculation 

```
x + y = 5/7 + 1/3 = 22/21
22/21 = some value out there

absolute error = | 22/21 - 1.0476 | = 0.19 x 10^-4
relative error = | absolute error / (x+y) | = 0.19 x 10^-4/ 22/21 = 0.182 * 10^-4
```

- example2: p = 0.54617 ; q = 0.54601 ; fl = 4 digit rounding ; p - q
  
```
p - q = fl ( fl(p) - fl(q) )
p - q = fl ( 0.5462 - 0.5460 )
p - q = fl ( 0.002 )
p - q = 0.002

abosolute error = | p - p* | 
relative error  = | absolute error | / |p| = 0.25 huge on this one
```

----------------------------------------------------------------------------------------

## 3rd lecture ##

### Taylor expansion ###

- *approximate of functions*
  - given a function f(x) ; the area of from point a to point x gonna be this formula
  - f(x) ≈ f(a) + f'(a)(x-a) 
  - linear function approximation 
  - yeah, it's true as linear approach
  - this is not such good approximation ; scope limited

- quadratic function? higher polynominal approximation
  - f(x) ≈ f(a) + f'(a)(x-a) + f''(a)/2!(x-a)^2
  - reason why this one is better
    - they share the same point at q(a)[new f(a)] = f(a)
    - they have the same slope ; first derivative
    - they have the same curvarate ; second derivative

- with this logic, given a higher polynominal taylor expression
  - we could get Σ(n, k=0) f(k)(a) / ( (k!) (x-a)^k )
  - the error approximation term gonna be : f(n+1)(error)/( (n+1)! ) (x-a)^(n+1)

### Lagrange interpolation ###

- given the simplest form of function(x) approximation given coordinates of two points
  - y = k[slope](x - xo) + f(xo)
  - k = ( f(x1) - f(xo) ) / (x1 - xo) = Δy/Δx
  - the general term below shows that
    - x = xo --> f(xo)
    - x = x1 --> f(x1) 

```
y =  ( ( f(x1) - f(xo) ) / (x1 - xo) )(x - xo) + f(xo)
y = ( f(x1)/(x1 - xo) - f(xo)/(x1 - xo)  )((x - xo) ) + f(xo)  <-- just extend the term k
y =  ( (x - xo)/(x1 - xo) )f(x1) -  ( (x - xo)/(x1 - xo) )f(xo) + f(xo) <-- further extension here
y = (x - xo)/(x1 - xo) )f(x1) + (x - xo)/(xo - x1) )f(xo) + f(xo) <-- flip the sign
y = (x - xo)/(x1 - xo) )f(x1) + ( (x - xo)/(xo - x1) + 1 )f(xo)   <-- short the term
y = (x - xo)/(x1 - xo) )f(x1) + (x - x1)/(xo - x1)f(xo) <-- general form for linear out there
```

- introducing quaradic function back
  - we need three points right now for quadratic function approximation
  - if we look back the linear general form; we can conduct that
  - (x - x1)(x - x2)/(xo - x1)(xo - x2) f(xo) + (x - xo)(x - x2)/(x1 - xo)(x1 - x2) f(x1) + (x - xo)(x - x1)/(x2 - xo)(x2 - x1)f(x2)
  - he said we could proof this similarly , three points are on f(x)
  - not sure how, btw
  - x = xo --> f(xo) + o + o = f(xo)
  - x = x1 --> f(x1)
  - x = x2 --> f(x2)
  
- n-terms of lagrange interpolation
  - f(x) ≈ Pn(x) = a_n x^n + a_n-1 x^n-1 + ... a1 x1 + ao
  - if we expand this, this gonna looks terrible
  - btw ho we doing this, is shown above
  - the final formula gonna be `Pn(x) = Σ(n, k=0) ( Π(n, i=0) (x-xi/xk-xi) ) f(xk)

----------------------------------------------------------------------------------------------------

## 4th lecture ##

he continue illustration about the lagrange interpolation  

### lagrange basis function ###

whenever we want make approximatio for any p(x) ≈ f(x) , and such P(xi) = f(xi)   
$$P(x) = \sum_{k=0}^{n}[ \prod_{i=o ; i \neq k}^{n} \frac{(x-xi)}{(xk - xi)} ]f(xt)$$
$[ \prod_{i=o ; i \neq k}^{n} \frac{(x-xi)}{(xk - xi)} ] = Ln,k(x)$   
he said the basis function is sort of lineaer algebra ideas about basis   
it's just making linear combination way for making such approximation

- for a given system
  - x =  1 ; $x=xk$
  - x =  0 ; when x for any number except x = xk

- this can be solve by lagrange basis function
  - $P(x) = \sum_{k=0}^{n} f(xk) Ln,k(x)$
  - f(xk) is some number

- $P(xi) = \sum_{k=0}^{n}f(xi) | n,k(xi)$
  - when k = i --> Ln,k(xi) =  1
  - when $ k != i --> Ln,k(xi) = 0
  - so that we can simply this whole equation into 
  - $P(xi) = \sum_{k=i}f(x)$
  - final solution: $f(xi)$

- text-book example
  - f(x) = 1/x ; xo = 2 ; x1 = 2.75 ; x2 = 4 ; we wanna make approximation on f(3) ≈ what 
  - L2,0(x) = $\frac{(x-x1)(x-x2)}{(xo-x1)(xo-x2)}$
  - L2,1(x) = $\frac{(x-x0)(x-x2)}{(x1-x0)(x1-x2)}$
  - L2,2(x) = $\frac{(x-x0)(x-x1)}{(x2-x1)(x2-x1)}$

- so the original function become P(x) = f(xo)L3,0(x) + f(x1)L3,1(x) + f(x2)L3,2(x)
  - how we did calculation this shit
  - x = whatever x value we wannt find ; legit P(x) <-- x
  - x0, x1, x2 is the terms given before 
  - f(3) through such approximation P(3) is 0.32955
  - to be honest, this approximation sounds like the `Gram-Schmidt algorithm`
  
### Why lagrange is better than Taylor approximation ###

- theorem  f ∈ $C^{n+1}[a,b]$ , assume x0, x1, .... , xn ∈ [a,b] and $f^{n+1}$ exists and continous   
  - then for any x ∈ [a,b]   
  - in the lagrange way
    - f(x) = P(x) + $\frac{f^{n+1}(δ)}{(n+1)!} (x-xo)(x-x1)....(x-xn)$
  - in the Taylor way
    - f(x) = P(x) + $\frac{f^{n+1}(δ)}{(n+1)!} (x-a)^{n+1}$ 

- conclusion
  - in lagrange way; each n-a term is dynamically changed by making next possible value
  - than in Taylor way; each x - a term is fixed, not changing

### python code for lagrange basis ###

he showed with python code; we wanna make approximation for the sin(x) function   
well he didn't show how to write that in the python ; he use library numpy for making function and matploit to graph   
it's clear that as long as the n become larger, the approximation become better ; it works   

----------------------------------------------------------------------------------------------------

## 5th lecture ##

he give us some adminstrative stuff about coding problem in HW ; he already did 99% percent of the code for u out there, just finish the rest is all good

### lagrange error approximation ###

$$| f(x) - P(x)| = | \frac{ f^{n+1}(δ) }{ (n+1)! }(x-xo)(x-x1)...(x-xn) |$$

- given example f(x) = $\frac{1}{2}$ x ∈ [2, 4] 
- we calculate the term on the left first which is $\frac{ f^{n+1}(δ) }{ (n+1)! }$
  - xo = 2, x1 = 3, x2 = 4
  - n = 2 
  - δ is either number between the range 2,4
  - $f^{3}$ we did third time derivaive to determine what's general solution of it
  - we plug in value to know $f^{3}$ is largest when δ = 2

- we next ought to find the maximum value of the g(x) there
  - $g(x) = (x-2)(x-3)(x-4)$ for x ∈ [2, 4]
  - one way to calculate this is expand the whole thing and take derivative to find local maximum
  - it's interesting to use `product rule` out there to calculate the formula
  - whole term become $g'(x) = (x-2)'(x-3)(x-4) + (x-2)[(x-3)(x-4)]'$
    - we can apply the product rule further
    -  $g'(x) = (x-2)'(x-3)(x-4) + (x-2)[(x-3)'(x-4) + (x-4)'(x-3)]$
    -  $g'(x) = (x-3)(x-4) + (x-2)(x-4 + x-3)$
    -  $g'(x) = 3x^{2} - 18x + 26$  
    -  once we get two values, we need graphical understanding to determine which value gives the local max there
    -  and we calculate it back

### technique for doing lagrange interpolation ###

- $f(x) = e^{x}$ ; xo = 1, x1 = 2, x2 = 3, x3 = 4, x5 = 6 
  -  P0,1(x)   <-- Lagrange linear polynomial by using x0, x1
  -  P1,2,4(x) <--  some function using variable x1, x2, x4
  -  it's sort of using dynamic programming ; like using answers of lagrange interpolation by linear poly
  -  then used to compute the higher dimension functions

- $P0,1(x) = \frac{x-x1}{x0-x1} f(xo) + \frac{x-xo}{x1-xo}f(x1) = \frac{1}{x1-xo} ((x-xo)P1 - (x-x1)Po)$
- $P1,2(x) = \frac{1}{x2-x1} ((x-x1)P2 - (x-x1)P1)$
- how are we gonna solve P0,1,2(x) through P0,1(x) and P1,2(x)
  - $P0,1,2(x) = \frac{1}{x2-x0} [(x-xo)P1,2 - (x-x2)P0,1]$
  - this is the formula used for calculating higher degree by using answer of lower order 

----------------------------------------------------------------------------------------------------

## 7 lecture ##

reivew lecture, ta taught us about how to do those interpolation questions, yeah pre-midterm preview

| typical questions                                   | how to solve them
|:---------------------------------------------------:|:------------------
| lagrange interpolation estimate error approximation | use error formula and make derivative of original function ; examine critical points for maximum of the function
| lagrange interpolation exact error approximation    | $|f(x) - P(x)|$ ; check f(x) ; check critical points
| lagrange conceptual check                           | purely conceptual, better be smarter
| neville's method                                    | understand how to calculate lagrange interpolation wisely
| neville's method conceptual check                   | understand how neville's method save up computation power
| Hermite interpolation                               | understand how the hermite interpolation to make calculation
| hermites interpolation conceptual check             | know how hermite interpolation gonna ; hermite polynomial gonna make a exact function? 
