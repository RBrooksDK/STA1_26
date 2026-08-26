# Calculating Metrics in Simple Linear Regression

This note collects the main hand-calculation formulas for simple linear
regression. In Python, use a tested implementation such as statsmodels for a
complete analysis; the formulas here explain what the software calculates.

## Population model and fitted line

For observations at predictor values (x_i), the simple linear regression
model is

\[
Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i,
\qquad E[\varepsilon_i\mid x_i]=0.
\]

The parameters \(\beta_0\) and \(\beta_1\) describe the population model. The
estimates calculated from a sample are written \(\hat\beta_0\) and
\(\hat\beta_1\). The fitted value for observation \(i\) is

\[
\hat y_i=\hat\beta_0+\hat\beta_1x_i.
\]

The fitted slope estimates the change in the conditional mean response
associated with a one-unit difference in the predictor. This association is
not automatically causal.

## Least-squares estimates

Define the centred sums

\[
S_{xx}=\sum_{i=1}^n(x_i-\bar x)^2,
\qquad
S_{xy}=\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y).
\]

Provided \(S_{xx}>0\), the least-squares estimates are

\[
\boxed{\hat\beta_1=\frac{S_{xy}}{S_{xx}}},
\qquad
\boxed{\hat\beta_0=\bar y-\hat\beta_1\bar x}.
\]

The condition \(S_{xx}>0\) means that the predictor values cannot all be
identical.

### Equivalent raw-sum formulas

The centred sums can also be written

\[
S_{xy}=\sum_{i=1}^n x_i y_i-n\bar x\bar y,
\qquad
S_{xx}=\sum_{i=1}^n x_i^2-n\bar x^2.
\]

Therefore,

\[
\hat\beta_1=
\frac{n\sum_{i=1}^n x_i y_i-
\left(\sum_{i=1}^n x_i\right)\left(\sum_{i=1}^n y_i\right)}
{n\sum_{i=1}^n x_i^2-
\left(\sum_{i=1}^n x_i\right)^2}.
\]

These identities are convenient for hand calculations. Directly subtracting
large, nearly equal raw sums can be numerically unstable, so centred
calculations or a regression library are preferable in code.

### Covariance and variance form

With sample covariance and variance

\[
s_{xy}=\frac{S_{xy}}{n-1},
\qquad
s_x^2=\frac{S_{xx}}{n-1},
\]

the fitted slope is equivalently

\[
\hat\beta_1=\frac{s_{xy}}{s_x^2}.
\]

## Correlation

Define

\[
S_{yy}=\sum_{i=1}^n(y_i-\bar y)^2.
\]

Provided both \(S_{xx}>0\) and \(S_{yy}>0\), Pearson's sample correlation is

\[
\boxed{r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}}.
\]

Because

\[
s_x=\sqrt{\frac{S_{xx}}{n-1}},
\qquad
s_y=\sqrt{\frac{S_{yy}}{n-1}},
\]

the relationship between slope and correlation is

\[
r=\hat\beta_1\frac{s_x}{s_y}.
\]

Using standard scores

\[
z_{x,i}=\frac{x_i-\bar x}{s_x},
\qquad
z_{y,i}=\frac{y_i-\bar y}{s_y},
\]

we can also write

\[
r=\frac{1}{n-1}\sum_{i=1}^n z_{x,i}z_{y,i}.
\]

The factor \(n-1\) appears because the standard scores use sample standard
deviations. It does not make \(r\) an unbiased estimator of the population
correlation; Pearson's \(r\) is generally biased.

## Coefficient of determination

For ordinary least-squares regression with one predictor and an intercept,

\[
R^2=r^2.
\]

Use the unambiguous sums-of-squares notation

\[
SS_{\mathrm{tot}}=\sum_{i=1}^n(y_i-\bar y)^2,
\]

\[
SS_{\mathrm{model}}=\sum_{i=1}^n(\hat y_i-\bar y)^2,
\qquad
SS_{\mathrm{res}}=\sum_{i=1}^n(y_i-\hat y_i)^2.
\]

For least-squares regression with an intercept,

\[
SS_{\mathrm{tot}}=SS_{\mathrm{model}}+SS_{\mathrm{res}},
\]

and hence

\[
\boxed{R^2=\frac{SS_{\mathrm{model}}}{SS_{\mathrm{tot}}}
=1-\frac{SS_{\mathrm{res}}}{SS_{\mathrm{tot}}}}.
\]

Here \(e_i=y_i-\hat y_i\) is an observed residual; it is not the same object
as the unobservable model error \(\varepsilon_i\). \(R^2\) is the proportion
of the observed total variation in \(y\) accounted for in-sample by the fitted
linear model. It is not evidence of causation or, by itself, evidence of good
out-of-sample prediction.

The notation avoids `SSR`, because statsmodels uses `.ssr` for the sum of
squared residuals, while some textbooks use SSR for the regression sum of
squares.

## Worked calculation from summary statistics

The following archived exercise is retained as an arithmetic illustration.
A lecturer surveyed \(n=12\) colleagues about professional meetings attended
in five years \((x)\) and journal papers submitted in the same period \((y)\).
The supplied summaries are

\[
\bar x=4,\qquad \bar y=12,\qquad
\sum_{i=1}^n x_i^2=232,\qquad
\sum_{i=1}^n x_i y_i=318.
\]

First calculate

\[
S_{xy}=318-12\cdot4\cdot12=-258
\]

and

\[
S_{xx}=232-12\cdot4^2=40.
\]

The estimated slope and intercept are therefore

\[
\hat\beta_1=\frac{-258}{40}=-6.45,
\qquad
\hat\beta_0=12-(-6.45)(4)=37.8.
\]

The fitted line is

\[
\boxed{\hat y=37.8-6.45x}.
\]

Within the observed predictor range, one additional meeting is associated
with 6.45 fewer submitted papers on average according to this fitted line.
The summary statistics alone do not let us inspect the scatterplot or
residuals, assess whether a linear model is suitable, or justify a causal
interpretation. The line also produces impossible negative counts for large
values of \(x\), so it must not be extrapolated mechanically.
