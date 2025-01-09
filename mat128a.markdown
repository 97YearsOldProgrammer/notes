# mat128a #

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
