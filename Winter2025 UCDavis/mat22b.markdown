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

------------------------------------------------------------------------------------------------------------

## lecutre 3 ##

### first oder linear equation ###

- linear ; scalar, first order ODEs
  - y' + p(t)y = g(t)
  - where p(t) , g(t) are given continous functions
  
- Homogeneous if g(t) = 0
  - ( <=> y(t) = 0 is a solution) 
  - otherwise non-homogeneous

- constant coefficient 
  - if p(t) = a is a constant
  - otherwise variable coefficient
  
| example     |  homogenous | coefficient |
|:-----------:|:-----------:|:-------------
| y' + ty = 2 | non-homo    | variable cf |
| y' + 2y = t | non-homo    | constant cf |
| y' + 2y = 0 | homo        | constant cf |

### integration factor method{2.1 text} ###

- $y' + p(t)y = g(t)$
  - try integrating ODE
  - $∫ y'(t)dt + ∫ p(t)y(t)dt = ∫ g(t)dt + C$
  - $y(t) + ∫ p(t)y(t)dt = ∫ g(t)dt + C$
  - converted a differential equation to an integral equation; this don't help out there
  
- introduce our method here
  - seek an integrating factor u(t) such that we can integrate the ODE to get y(t)
  - $u(t)y' + p(t)u(t)y = u(t)g(t)$
    - one thing about this method, we try to make the left hand sight could be directly product of one differentiation
    - ( uy )' = uy' + puy <-- this is the product rule
    - (uy)' = uy' + u'y
    - we need u(t) to satisfy that : u' = pu
  
- we need a formal calculation to find u' here
  - below is the overall breakdown formula conduction for our question 
  - $du/dt = pu$
  - $∫ du/u = ∫ p(t)dt$
  - $ln|u| = \int p(t)dt + C$
  - $|u(t)| = C e^{∫p(t)dt}$ ; make every single time become e^original term here
  - $u(t)  = \pm C e^{∫p(t)dt}$
  - $u(t)  = e^{∫p(t)dt}$
  - final formula for u(t): $u(t) = e^{∫p(t)dt}$

- check on formula conduction
  - $du/dt = e^{∫p(t)dt * \frac{d}/{d∫p(t)dt} }$
  - $du/dt = u(t)*p(t)$ 
  - so this proof that our formula work out there
  - $u' = pu$

- back to original system
  - $y' + py = g$
  - $uy' + upy = ug$
  - $(uy)' = ug$
  - $\int (uy)'dt = \int ug dt + C$
  - $uy = \int ugdt + C$
  - $y(t) = \frac{1}{u(t)} \int u(t) g(t) \, dt + \frac{C}{u(t)}$
  - e to any circumstance is non-zero
  - so define such u(t) is not gonna be a problem
  - key take away: $u(t) = e^(p(t))$
  
- example $y' + ty = t$
  - $p(t) = t$ ; $g(t) = t$
  - $\int p(t)dt = \int tdt = \frac{1}{2} t^{2}$
  - $u(t) = e^{\int pdt} = e^{\frac{1}{2} t^{2}}$
  - $e^{\frac{t^{2}}{2}}y' + te^{\frac{t^{2}}{2}} = te^{\frac{t^{2}}{2}}$
  - $(e^{\frac{t^{2}}{2}})' = te^{\frac{t^{2}}{2}}$
  - $e^{\frac{t^{2}}{2}}y = \int tte^{\frac{t^{2}}{2}}dt+ C$
  - solving the right hand side with further substitution
    - $u = \frac{t^{2}}{2}$ $du = tdt$ 
    - $\int tte^{\frac{t^{2}}{2}}dt = \int e^{u}du = e^{u} + C$
    - $e^{\frac{1}{2}t^{2}} + C
  - **final solution here**: $y(t) = 1 + Ce^{-\frac{1}{2}t^{2}}$
  - we now get the general solution for the differential equation here

- check back the original system
  - $y' + ty = -C(t)e^{-\frac{1}{2}t^{2}} + t(1+Ce^{-\frac{1}{2}t^{2}})
  - they cancel out
  - y' + ty = t ; we get back the same answer out there 

- further understanding
  - solution of homogeneous equation
  - $z' + tz = 0$ is $z(t) = Ce^{-\frac{1}{2}t^{2}}$ 
  - $y(t) = 1 + Ce^{-\frac{1}{2}t^{2}}$
  - number 1 is the particular solution of non-homogeneous ODE
  - exponent of e is the aribitrary constant C times a solution of corresponding homogenous ODE
  - get general solution by superposing a particular solution of nonhomogenous equation and constant x solution of homogeneous equation

------------------------------------------------------------------------------------------------------------

## lecture 4 ##

- **integrating factor method**
  - recall from last lecture
  - $y' + p(t)y g(t)$
  - 1 compute integrating factor
    - $u(t) = e^{\int p(t)dt}$
  - 2 multiply ODE by u(t) and write left-handside as an exact derivative
    - $(uy)' = ug
  - 3 integrate and solve for y(t)
    - we now get the general solution that depending on arbitary constant of integration C  

- to solve an initial value problem (IVP)
  - $$\begin{cases} y' + p(t)y = g(t), \\y(t_0) = y_0.\end{cases}$$
  - 1 find general solution
  - 2 use initial condition to find c in terms of yo

### example solved by integrating factor method ###

- y' + ty = t 
  - $u(t) = e^{\int tdt} = e^{\frac{1}{2}t^{2}}$   
  - $e^{\frac{1}{2}t^{2}}y' + te^{\frac{1}{2}t^{2}}y = te^{\frac{1}{2}t^{2}}$
  - $(e^{\frac{1}{2}t^{2}}y)' = te^{\frac{1}{2}t^{2}}$
  - $(e^{\frac{1}{2}t^{2}}y) = \int{t e^{\frac{1}{2}t^{2}} } + C = e^{\frac{1}{2}t^{2}} + C$
  - $y(t) = 1 + Ce^{-\frac{1}{2}t^{2}}$

### example on solving initial value probelm

- $$\begin{cases} y' + ty = t, \\y(2) = 0.\end{cases}$$
  - giving previous general solution $y(t) = 1 + Ce^{-\frac{1}{2}t^{2}}$
  - evaluate at to = 2
  - $y(2) = 1 + Ce^{-2}$
  - $0 = 1 + Ce^{-2}$
  - $Ce^{-2} = -1$
  - $C = -e^{2}$
  - final answer: $y(t) = 1 - e^{2}e^{-\frac{1}{2}t^{2}}$

- not quite sure, btw he also talks about some property about even and odd function
  - for verify the final answer

### mass falliong under gravity example ###

| condition | meaning 
|:---------:|:---------
| v(t)      | velocity
| m         | mass
| g         | accerlation gravity
| $\rho$    | drag constant

- $m \frac{dV}{dt} = mg - \rho v$
  - $\frac{dV}{dt} = g -  λv$ ;  $λ = \frac{\rho}{m}$
  - $\frac{dV}{dt} +  λv = g$ ; p(t) =  λ
  - $\int{p(t)dt} = \int λdt = λt ; u(t) = e^{λt}$
  - $e^{λt}\frac{dV}{dt} + λe^{λt}v = ge^{λt}$
  - $(e^{λt}v)' =ge^{λt}$
  - $\int{e^{λt}v}'dt = \int{ge^{λt}dt} + C
  - $e^{λt}v = \frac{g}{λ}e^{λt} + C ; v = \frac{g}{λ}$
  - $v(t) = v + Ce^{-λt}$
  - now we find the general solution there

- initial value problem
  - $$\begin{cases} \frac{dV}{dt} = g - λv \\v(0) = vo\end{cases}$$ 
  - $v(t) = v* + Ce^{-λt}$ ; v* = g/λ
  - At t = 0 ; $vo = v* + C$ --> $C = vo - v*$
  - $v(t) = v* + (vo - v*)e^{-λt}$

### another example ###

-  y' + ty = 1
  - $p(t) = t \int p(t)dt = \frac{1}{2}t^{2} u(t) = e^{\frac{1}{2}t^{2}}$
  - times everything
  - $e^{\frac{1}{2}t^{2}}y = \int e^{\frac{1}{2}t^{2}} dt + C$
  - $y(t) = e^{-\frac{1}{2}t^{2}} \int e^{\frac{1}{2}t^{2}}dt + Ce^{-\frac{1}{2}t^{2}}$
  - as long as it's here, it's considered to solve here
  
- y(0) = 2; initial value problem here
  -  $\int e^{\frac{1}{2}t^{2}}dt = \int_{0}^{t}e^{\frac{1}{2}s^{2}}ds + C$
  -  $y(t) = e^{-\frac{1}{2}t^{2}}\int_{0}^{t}e^{\frac{1}{2}s^{2}}ds + Ce^{-\frac{1}{2}t^{2}}$
  -  y(0) = 2 
  -  $2 = Ce^{0}$ ; c = 2
  -  $y(t) = e^{-\frac{1}{2}t^{2}} \int_{0}^{t}e^{\frac{1}{2}s^{2}}ds + 2e^{-\frac{1}{2}t^{2}}$