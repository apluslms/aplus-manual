pkg load statistics

#######################################
## Read the parameter given by the user from the command-line arguments.
# Replace commas (,) with dots (.) because str2double ignores commas completely.
inputstring = argv(){1};
inputstring( inputstring == "," ) = ".";
lambda = str2double (inputstring);

# Valid number?
if (! isscalar (lambda) || isnan (lambda))
  disp ("Error: Not a valid number. Example input: 0.4");
  exit (1);
endif
# Negative values or zero are not allowed.
if (lambda <= 0)
  disp ("Error: The parameter must be positive.");
  exit (1);
endif

#######################################
## Plot the exponential distribution.
x = [0:0.001:expinv(0.9999,1/lambda)];
subplot (2, 1, 1);
plot (x, exppdf(x,1/lambda), "b", "linewidth", 5);
hold;
title ("Probability density function");
grid on;
subplot (2, 1, 2);
plot (x, expcdf(x,1/lambda), "r", "linewidth", 5);
hold on;
title ("Cumulative distribution function");
grid on;

#######################################
## Write the plot to an image file plot.png.
print plot.png -dpngcairo "-S640,600";
