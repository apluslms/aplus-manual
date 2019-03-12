pkg load statistics

#######################################
## Read the parameters given by the user from the command-line arguments.
inputstring1 = argv(){1};
inputstring2 = argv(){2};
# str2num evaluates the string input as code, but it is the only easy way
# to convert strings into matrixes.
# Limit the length of the input strings for the sake of security.
if (length (inputstring1) > 16)
  disp ("Error: The mean vector input accepts at most 16 characters.");
  exit (1);
endif
if (length (inputstring2) > 30)
  disp ("Error: The covariance matrix input accepts at most 30 characters.");
  exit (1);
endif

[mu, muok] = str2num (inputstring1);
[Sigma, sok] = str2num (inputstring2);

if (! muok)
  disp ("Error: The mean vector must be a numeric vector.");
  exit (1);
endif
if (! sok)
  disp ("Error: The covariance matrix must be a numeric matrix.");
  exit (1);
endif

[murows, mucols] = size (mu);
if (murows != 1 || mucols != 2)
  disp ("Error: The mean vector must have dimensions 1x2.");
  exit (1);
endif

[srows, scols] = size (Sigma);
if (srows != 2 || scols != 2)
  disp ("Error: The covariance matrix must have dimensions 2x2.");
  exit (1);
endif
if (Sigma(1,1) <= 0)
  disp ("Error: Variance (sigma1) must be positive.");
  exit (1);
endif
if (Sigma(2,2) <= 0)
  disp ("Error: Variance (sigma2) must be positive.");
  exit (1);
endif
if (Sigma(1,2) != Sigma(2,1))
  disp ("Error: The covariance matrix cells including correlation must be equal.");
  exit (1);
endif

#######################################
## Plot the 2-dimensional normal distribution.

x1 = -3:.2:3;
x2 = -3:.2:3;
[X1, X2] = meshgrid (x1,x2);
F = mvnpdf ([X1(:) X2(:)], mu, Sigma);
F = reshape (F, length(x2), length(x1));
surf (x1, x2, F);
caxis ([min(F(:)) - .5*range(F(:)), max(F(:))]);
axis ([-3 3 -3 3 0 .25]);
xlabel ('X_1');
ylabel ('X_2');
zlabel ('Probability Density');

#######################################
## Write the plot to an image file plot.png.
print plot.png -dpngcairo "-S640,600";
