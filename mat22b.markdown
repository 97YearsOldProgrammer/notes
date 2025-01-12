# MAT22B #

- [lecture1](#lecture-1)
- [lecture2](#lecture-2)
----------------------------------------------------------------------------------------------------------------

## lecture 1 ##

### differential equations ###

- Ordinary differential equation (ODE)
  - for functions y(t) of a single independent variable
  - this class that are gonna focus on

- Partial differential equation (PDE)
  - for function u(x, y, z, t) of several independent variables
  - not discuss in this course

### exponential growth and decay ( chapter1 ) ###

**example1**
- y` = y
- y(t)  y`(t) = dy/dy(t) 

 - y(t) is function such that if you differentiate y(t) ; you get back y(t)
  - e^x is one example ;  y(t) = e^(x) ; each spot ; slope is the function itself
  - also, y(t) = 0 is one solution
  - also, y(t) = C*e^t ; solution for any constant C

solution above is every differential equations
for y(t) = c*e^t ; how are we gonna determine C?  we need some supplementary condition; as initial condition

> y(0) = y0
> y'(t) = y(t)

this is called `INP` = initial value problem
this is kinda determinant constant solution to the general form of initial value problem

> y(t) = ce^t at t = 0
> ce^0 = c = y0
> y(t) = y0 e^t

**example2**
- question: for system of y'(t) = ry(t)
  - r = constant; y(t) = ce^rt

- if we have one more condition in the system
- y'(t) = ry(t) y(0) = y
  - y(t) = ce^rt   c = y0
  - solution of IVP: is y(t) = y0 e^rt

application

- whenever r is positive; we would have exponential growth function
  - population growth function

### radioactive decay example ###

- whenever r is negative; we would have exponential decay function
  - radioactive decay
  - N(t) = number of radioactive atom (assumed very large)
  - r       = decay rate  (how fast the atom decay)
  - dN/dt = - rN
  - N(0) = No (initial condition)
  - final solution: N(t) = No e^(-rt)

dimensions(units) of this example

- [x] = units of X
  - [N] = number of atoms
  - [r]  = 1/time = 1/T

mean lifetime of radioactive material

- whenver γ = 1/r (dimensions of time)
- it means it require γ units to decay
  - at t = γ, N(γ) = No e^(-rγ) = No e^(-1)
  - fraction 1/e of atoms decay over time γ

half-life example

- half-life T(1/2) = time taken for half of atoms to decay
  - N(T 1/2) = 1/2 No
  - N(t) = No e^(-rt)
  - No e^(-rT1/2) = 1/2No
  - e^(-rT1/2) = 1/2
  - -r T1/2 = ln(1/2)
  - T 1/2 = - 1/r ln(1/2) = ln2/r
  - T 1/2 = (ln2) γ  [ γ = 1/r before ]

------------------------------------------------------------------------------------------------------------

## lecture 2 ##

### object falling under gravity ###

- initial conditions
  - mass of object = m
  - falling force = mg
  - mass of resistance (sort AR) = - rv
  - falling velocity = v(t) 
  - acceleration due to gravity (approx 9.8 m/s^2)
  - gravitational force = mg
  - friction constant = λ 

- newton's 2nd law
  - F = ma
  - m* dv/dt = mg - rv 
  - dv/dt = g - λv ; v(0) = v0 (initial value problem)
  
Mass m falling under gravity with gravitational acceleration g
Resistance proportional to downward velocity v(t) of mass

- what's sontant solution v(t) = V* this ODE have?
  - 0 = g - λv* --> v* = g/λ (terminal velocity)
  - dv/dt = -λ (v - g/λ) = - λ(v - v*)
    - since dv/dt = g - λv --> -λ(v - g/λ)
  - v(t) = v* + w(t) <-- introduce new function ; v - v* = w assunme this
  - dw/dt = - λw <-- this is similar to exponential growth function
  - initial value problem gonna change if we introduce the new function
    - vo = v* + wo ( since v - v* = w )
    - wo = vo - v*  
  - with given this condition:  dw/dt = - λw
    - we could tell that solution is w(t) = wo*e^(-λt)
    - since we have proof that for the same change of speed only exponential function satisfy this 
  - if we substitute everything backward
    - v(t) = v* + (vo - v*)e^(-λt)

- how does this mean graphically
  - imagine a vt graph; v as y axis; t as x axis
  - v* is something that a constant that fits the falling terminal speed; it's a horizontal line that parallel to x axis
  - no matter what v0(initial speed) ; either fast or slow
  - it would approach to the v* as t approaches to infinity 


### classification of ODEs (chapter 1.3) ###

- *order* of ODE
  - order of highest derivative in ODE

| example     | order
|:-----------:|:------
| y' = y-t    | 1st order (linear)
| y''=6y^2 + t| 2nd order (non-linear)
| y'''+yy''=0 | 3rd order (non-linear)

- higher the order of ODE; the harder the system to solve
  - third order ODE in some liquid mechanics

- *linear/non-linear* of ODE
  - ODE y(t) is linear if all terms in the ODE are proportional to y.y'.y''.... or are given functions of t otherwise non-linear

| example     | linear or not
|:-----------:|:-------------
| y' = y - t^2| linear
| y' = y^2 - t| nonlinear

- nonlinear ODEs are much harder to analyze than linear ODEs
  - linear ODEs have a *superposition property*
  - you can construct general solution as linear combinations of specific solutions
  - basically, we can use linear ODEs into the linear combination way

- *scalar/system*
  - ODE is scalar if it involves only one dependent variable y(t)
  - ODe is a system if it involves serveral dependet variable e.g. x(t), y(t), z(t)

- example
  - x' = x - xy ; y' = xy - y 2x2 system ; first order; nonlinear equation 
  - x' = 5x + 2y ; y' = -3x + 7y linear constant coefficient 

- difficulty of linear and nonlinear system
  - nonlinear >> linear 
  - higher order ODE >> lower ODE 
  - systems >> scalar equations

### first order, scalar ODEs (chapter2) ###

- f(t) continous function
  - ∫f(t)dt = F(t) + C
  - this means F(t) is an antiderivative (or indefinite integral of f(t) i.e. )
  - F'(t) = f(t)

- graph example for integral function
  - F(t) = ∫(t to t0) f(s) ds
  - imagine a st graph, s as x-axis, t as y-axis
  - function y = f(S) ; a ; line
  - definite integral means a sum of Rienmann sum for area under this function from point t to to ; change of t   

- Fundamental Theorem of Calculus (FTC) says 
  - F(t) is differentiable and F'(t) = f(t)
  - F(to) = 0  

- exampke for antiderivative function
  - ∫t^2 dt = 1/3 t^3 + C
  - ∫ (t, 1) s^2 ds = [1/3 s^3](t, 1) = 1/3t^3 - 1/3 

